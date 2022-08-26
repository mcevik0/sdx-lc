# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.node import Node  # noqa: E501
from swagger_server.models.location import Location
from swagger_server.models.port import Port
from swagger_server.test import BaseTestCase


class TestNodeController(BaseTestCase):
    """NodeController integration test stubs"""

    def test_add_node(self):
        """Test case for add_node

        add a new node to the topology
        """
        location = Location(
            address = "unknown",
            latitude = 0.0,
            longitude = 0.0,
        )
        ports = [Port(
            id = "test_add_node_port_id",
            name = "test_add_node_port_name",
            short_name = "test_add_node_port_short_name",
            node = "test_add_node_id",
            label_range = None,
            status = "unknown",
            state = "unknown",
            private_attributes = None,
        )]
        body = Node(
            id = "test_add_node_id",
            name = "test_add_node_name",
            short_name = "test_add_node_short_name",
            location = location,
            ports = ports,
            private_attributes = None,
        )
        response = self.client.open(
            "/SDX-LC/1.0.0/node",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_node(self):
        """Test case for delete_node

        Deletes a node
        """
        query_string = [("node_id", 789)]
        headers = [("api_key", "api_key_example")]
        response = self.client.open(
            "/SDX-LC/1.0.0/node",
            method="DELETE",
            headers=headers,
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_node(self):
        """Test case for get_node

        get an existing node
        """
        response = self.client.open("/SDX-LC/1.0.0/node", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_update_node(self):
        """Test case for update_node

        Update an existing node
        """
        body = Node()
        response = self.client.open(
            "/SDX-LC/1.0.0/node",
            method="PUT",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
