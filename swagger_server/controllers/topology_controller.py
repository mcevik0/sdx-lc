import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.topology import Topology  # noqa: E501
from swagger_server import util


def add_topology(body):  # noqa: E501
    """Send a new topology to SDX-LC

     # noqa: E501

    :param body: topology object that needs to be sent to the SDX LC
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topology.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_topology(topology_id, api_key=None):  # noqa: E501
    """Deletes a topology

     # noqa: E501

    :param topology_id: ID of topology to delete
    :type topology_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


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
    return 'do some magic!'


def get_topology():  # noqa: E501
    """get an existing topology

    ID of the topology # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def get_topologyby_version(topology_id, version):  # noqa: E501
    """Find topology by version

    Returns a single topology # noqa: E501

    :param topology_id: ID of topology to return
    :type topology_id: int
    :param version: version of topology to return
    :type version: int

    :rtype: Topology
    """
    return 'do some magic!'


def topology_version(topology_id):  # noqa: E501
    """Finds topology version

    Topology version # noqa: E501

    :param topology_id: topology id
    :type topology_id: str

    :rtype: Topology
    """
    return 'do some magic!'


def update_topology(body):  # noqa: E501
    """Update an existing topology

    ID of topology that needs to be updated. \\\\ The topology update only updates the addition or deletion \\\\ of node, port, link. # noqa: E501

    :param body: topology object that needs to be sent to the SDX LC
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topology.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def upload_file(topology_id, body=None):  # noqa: E501
    """uploads an topology image

     # noqa: E501

    :param topology_id: ID of topology to update
    :type topology_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
