#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.messaging.message_queue_producer import *
from swagger_server.messaging.rpc_queue_producer import *

def main():
    # serverconfigure = RabbitmqConfigure(queue='hello',
    #                            host='localhost',
    #                            routingKey='hello',
    #                            exchange='')

    # rabbitmq = RabbitMq(serverconfigure)
    # # Testing message
    # rabbitmq.publish(body={"localctlr":1})

    # message queue rpc test
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')


    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'SDX LC'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
