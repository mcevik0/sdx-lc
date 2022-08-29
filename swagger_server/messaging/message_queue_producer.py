import json

import pika


class RabbitmqConfigure:
    def __init__(
        self,
        queue="hello",
        host="aw-sdx-monitor.renci.org",
        routingKey="hello",
        exchange="",
    ):
        # Configure Rabbit Mq Server
        self.queue = queue
        self.host = host
        self.routingKey = routingKey
        self.exchange = exchange


class RabbitMq:
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host)
        )
        self._channel = self._connection.channel()

    def publish(self, body={}):
        result = self._channel.queue_declare(queue=self.server.queue)
        callback_queue = result.method.queue
        self._channel.basic_publish(
            exchange=self.server.exchange,
            routing_key=self.server.routingKey,
            properties=pika.BasicProperties(
                reply_to=callback_queue,
            ),
            body=str(body),
        )

        print("Published Message: {}".format(body))

        self._connection.close()


if __name__ == "__main__":

    server = RabbitmqConfigure(
        queue="hello", host="localhost", routingKey="hello", exchange=""
    )

    with open("./mq-test/local-ctlr-1/local-ctlr-1.manifest") as f:
        data = json.load(f)
        RabbitMq(server).publish(body=data)
