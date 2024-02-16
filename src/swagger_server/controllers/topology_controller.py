import json
import logging
import os
import threading

import connexion
import six

from swagger_server import util
from swagger_server.messaging.rpc_queue_producer import RpcProducer
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.topology import Topology  # noqa: E501
from swagger_server.utils.db_utils import DbUtils

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pika").setLevel(logging.WARNING)

MANIFEST = os.environ.get("MANIFEST")
OXPO_ID = int(os.environ.get("OXPO_ID"))
SDX_LC_DOMAINS = os.environ.get("SDXLC_DOMAINS")
SDXLC_DOMAIN = SDX_LC_DOMAINS.split(",")[OXPO_ID]

# Get DB connection and tables set up.
db_instance = DbUtils()
db_instance.initialize_db()


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def add_topology(body):  # noqa: E501
    """Send a new topology to SDX-LC

     # noqa: E501

    :param body: topology object that needs to be sent to the SDX LC
    :type body: dict | bytes

    :rtype: None
    """
    logger.info(f"######## add topology #######")
    if connexion.request.is_json:
        body = connexion.request.get_json()

    msg_id = body["id"]
    if msg_id is None:
        return "ID is missing."

    logger.info(f"msg_id: {msg_id}")
    logger.info(f"SDX_LC domain: {SDXLC_DOMAIN}")
    domain_name = find_between(msg_id, "topology:", ".net")
    logger.info(f"domain name: {domain_name}")
    if msg_id != SDXLC_DOMAIN:
        logger.debug("Domain name not matching LC domain. Returning 400 status.")
        return "Domain name not matching LC domain. Please check again.", 400

    body["lc_queue_name"] = os.environ.get("SUB_TOPIC")
    json_body = json.dumps(body)

    logger.debug("Adding topology. Saving to database.")
    db_instance.add_key_value_pair_to_db(f"topoVersion{body['version']}", json_body)
    db_instance.add_key_value_pair_to_db("latest_topology", json_body)
    logger.debug("Saving to database complete.")

    # logger.info("Publishing Message to MQ: {}".format(body))

    # initiate rpc producer with 5 seconds timeout
    rpc = RpcProducer(5, "", "topo")
    response = rpc.call(json_body)
    # Signal to end keep alive pings.
    rpc.stop()

    logger.info(f"sdx lc response: {response}")
    # logger.info(f"json_body: {json_body}")
    # return str(response)
    return json_body


def delete_topology(topology_id, api_key=None):  # noqa: E501
    """Deletes a topology

     # noqa: E501

    :param topology_id: ID of topology to delete
    :type topology_id: int
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    return "do some magic!"


def delete_topology_version(topology_id, version, api_key=None):  # noqa: E501
    """Deletes a topology version

     # noqa: E501

    :param topology_id: ID of topology to return
    :type topology_id: int
    :param version: topology version to delete
    :type version: int
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    return "do some magic!"


def get_topology():  # noqa: E501
    """get an existing topology

    ID of the topology # noqa: E501


    :rtype: str
    """
    return "do some magic!"


def get_topologyby_version(topology_id, version):  # noqa: E501
    """Find topology by version

    Returns a single topology # noqa: E501

    :param topology_id: ID of topology to return
    :type topology_id: int
    :param version: version of topology to return
    :type version: int

    :rtype: Topology
    """
    return "do some magic!"


def topology_version(topology_id):  # noqa: E501
    """Finds topology version

    Topology version # noqa: E501

    :param topology_id: topology id
    :type topology_id: str

    :rtype: Topology
    """
    return "do some magic!"


def update_topology(body):  # noqa: E501
    """Update an existing topology

    ID of topology that needs to be updated. \\\\ The topology update only updates the addition or deletion \\\\ of node, port, link. # noqa: E501

    :param body: topology object that needs to be sent to the SDX LC
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topology.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    return body


def upload_file(topology_id, body=None):  # noqa: E501
    """uploads an topology image

     # noqa: E501

    :param topology_id: ID of topology to update
    :type topology_id: int
    :param body:
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    # if connexion.request.is_json:
    #     body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"
