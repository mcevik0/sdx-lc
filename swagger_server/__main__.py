#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.messaging.topic_queue_consumer import *
from swagger_server.utils.db_utils import *

from optparse import OptionParser
import argparse
import time
import threading
import logging
import json


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True


def start_consumer(thread_queue, db_instance):
    logger = logging.getLogger(__name__)
    logging.getLogger("pika").setLevel(logging.WARNING)

    MESSAGE_ID = 0
    HEARTBEAT_ID = 0

    rpc = TopicQueueConsumer(thread_queue, "connection")
    t1 = threading.Thread(target=rpc.start_consumer, args=())
    t1.start()


def main():
    logging.basicConfig(level=logging.INFO)

    # Run swagger service
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api("swagger.yaml", arguments={"title": "SDX LC"}, pythonic_params=True)
    # Run swagger in a thread
    threading.Thread(target=lambda: app.run(port=8080)).start()

    DB_NAME = os.environ.get("DB_NAME") + ".sqlite3"
    MANIFEST = os.environ.get("MANIFEST")

    # Get DB connection and tables set up.
    db_tuples = [("config_table", "test-config")]

    db_instance = DbUtils()
    db_instance._initialize_db(DB_NAME, db_tuples)
    thread_queue = Queue()
    start_consumer(thread_queue, db_instance)


if __name__ == "__main__":
    main()
