#!/usr/bin/env python
import pika
import uuid
import os
import time
import threading

MQ_HOST = 'aw-sdx-monitor.renci.org'

class RpcProducer(object):
    def __init__(self, timeout):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=MQ_HOST))

        self.channel = self.connection.channel()
        self.timeout = timeout

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(queue=self.callback_queue,
                            on_message_callback=self.on_response,
                            auto_ack=True)

    def keep_live(self):
        while True:
            time.sleep(30)
            self.connection.process_data_events()

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                routing_key='rpc_queue',
                                properties=pika.BasicProperties(
                                    reply_to=self.callback_queue,
                                    correlation_id=self.corr_id,
                                ),
                                body=str(body))
        print("Waiting for response...")
        timer = 0
        while self.response is None:
            time.sleep(1)
            timer += 1
            # print("Waiting for response..." + str(timer))
            if timer == self.timeout:
                return "No response from MQ receiver"
            self.connection.process_data_events()

        self.channel.close()
        return self.response

if __name__ == "__main__":
    rpc = RpcProducer()
    body = "test body"
    print("Published Message: {}".format(body))
    response = rpc.call(body)
    print(" [.] Got response: " + str(response))