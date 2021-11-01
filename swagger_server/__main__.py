#!/usr/bin/env python3

import connexion
import os
import time

from swagger_server import encoder
from swagger_server.messaging.message_queue_producer import *
from swagger_server.utils.db_utils import *
# from swagger_server.messaging.rpc_queue_producer import *

from optparse import OptionParser
import argparse


def main():
    # Sleep 10 seconds waiting for RabbitMQ to be ready
    time.sleep(7)

    MQ_HOST = os.environ.get('MQ_HOST')

    parser = OptionParser()

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-m", "--manifest", dest="manifest", type=str, 
                        action="store", help="specifies the manifest")

    parser.add_argument("-d", "--database", dest="database", type=str, 
                         action="store", help="Specifies the database ", 
                         default=":memory:")

    options = parser.parse_args()
    print(options.manifest)

    dbname = options.database
    # Get DB connection and tables set up.
    db_tuples = [('config_table', "test-config")]
    
    db_util = DbUtils()
    db_util._initialize_db(dbname, db_tuples)
    

    # serverconfigure = RabbitmqConfigure(queue='hello',
    #                            host='localhost',
    #                            routingKey='hello',
    #                            exchange='')

    # rabbitmq = RabbitMq(serverconfigure)
    # # Testing message
    # rabbitmq.publish(body={"localctlr":1})

    # message queue rpc test
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=MQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')

    # Run swagger service
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'SDX LC'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
