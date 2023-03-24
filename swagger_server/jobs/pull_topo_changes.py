import argparse
import json
import logging
import os.path
import sys
import threading
import time
import urllib.request

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from messaging.rpc_queue_producer import *
from utils.db_utils import *


DOMAIN_CONTROLLER_PULL_URL = os.environ.get("DOMAIN_CONTROLLER_PULL_URL")
DOMAIN_CONTROLLER_PULL_INTERVAL = os.environ.get("DOMAIN_CONTROLLER_PULL_INTERVAL")
logger = logging.getLogger(__name__)


def main():
    db_instance = DbUtils()
    db_instance.initialize_db()

    process_domain_controller_topo(db_instance)


def process_domain_controller_topo(db_instance):
    while True:
        latest_topology = db_instance.read_from_db("latest_topology")
        if not latest_topology:
            time.sleep(int(DOMAIN_CONTROLLER_PULL_INTERVAL))
            continue

        json_latest_topology = json.loads(latest_topology["latest_topology"])

        try:
            latest_topo_version = json_latest_topology["version"]
        except KeyError:
            logger.debug("Error getting topo version")
            continue

        pulled_topology = urllib.request.urlopen(DOMAIN_CONTROLLER_PULL_URL).read()

        if not pulled_topology:
            time.sleep(int(DOMAIN_CONTROLLER_PULL_INTERVAL))
            continue

        logger.debug("Pulled request from domain controller")

        json_pulled_topology = json.loads(pulled_topology)
        try:
            pulled_topo_version = json_pulled_topology["version"]
        except KeyError:
            logger.debug("Error getting topo version")
            continue

        if latest_topo_version == pulled_topo_version:
            time.sleep(5)
            continue

        logger.debug("Pulled topo with different version. Adding pulled topo to db")
        db_instance.add_key_value_pair_to_db(
            "topoVersion" + str(json_pulled_topology["version"]), pulled_topology
        )
        db_instance.add_key_value_pair_to_db("latest_topology", pulled_topology)
        logger.debug("Added pulled topo to db")
        # initiate rpc producer with 5 seconds timeout
        rpc_producer = RpcProducer(5, "", "topo")
        response = rpc_producer.call(pulled_topology)
        # Signal to end keep alive pings.
        rpc_producer.stop()

        time.sleep(int(DOMAIN_CONTROLLER_PULL_INTERVAL))


if __name__ == "__main__":
    main()
