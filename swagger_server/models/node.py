# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.port import Port  # noqa: F401,E501
from swagger_server import util


class Node(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, short_name: str=None, ports: List[Port]=None):  # noqa: E501
        """Node - a model defined in Swagger

        :param id: The id of this Node.  # noqa: E501
        :type id: str
        :param name: The name of this Node.  # noqa: E501
        :type name: str
        :param short_name: The short_name of this Node.  # noqa: E501
        :type short_name: str
        :param ports: The ports of this Node.  # noqa: E501
        :type ports: List[Port]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'short_name': str,
            'ports': List[Port]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'short_name': 'short_name',
            'ports': 'ports'
        }
        self._id = id
        self._name = name
        self._short_name = short_name
        self._ports = ports

    @classmethod
    def from_dict(cls, dikt) -> 'Node':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The node of this Node.  # noqa: E501
        :rtype: Node
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Node.


        :return: The id of this Node.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Node.


        :param id: The id of this Node.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Node.


        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Node.


        :param name: The name of this Node.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def short_name(self) -> str:
        """Gets the short_name of this Node.


        :return: The short_name of this Node.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name: str):
        """Sets the short_name of this Node.


        :param short_name: The short_name of this Node.
        :type short_name: str
        """

        self._short_name = short_name

    @property
    def ports(self) -> List[Port]:
        """Gets the ports of this Node.


        :return: The ports of this Node.
        :rtype: List[Port]
        """
        return self._ports

    @ports.setter
    def ports(self, ports: List[Port]):
        """Sets the ports of this Node.


        :param ports: The ports of this Node.
        :type ports: List[Port]
        """
        if ports is None:
            raise ValueError("Invalid value for `ports`, must not be `None`")  # noqa: E501

        self._ports = ports
