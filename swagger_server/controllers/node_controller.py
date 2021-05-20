import connexion
import six

from swagger_server.models.node import Node  # noqa: E501
from swagger_server import util


def add_node(body):  # noqa: E501
    """add a new node to the topology

     # noqa: E501

    :param body: node object that needs to be sent to the SDX LC
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Node.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_node(node_id, api_key=None):  # noqa: E501
    """Deletes a node

     # noqa: E501

    :param node_id: ID of node to delete
    :type node_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_node():  # noqa: E501
    """get an existing node

    ID of the node # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
