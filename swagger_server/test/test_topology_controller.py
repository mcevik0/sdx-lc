# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.topology import Topology  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTopologyController(BaseTestCase):
    """TopologyController integration test stubs"""

    def test_add_topology(self):
        """Test case for add_topology

        Send a new topology to SDX-LC
        """
        body = Topology()
        response = self.client.open(
            "/SDX-LC/1.0.0/topology",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_topology(self):
        """Test case for delete_topology

        Deletes a topology
        """
        query_string = [("topology_id", 789)]
        headers = [("api_key", "api_key_example")]
        response = self.client.open(
            "/SDX-LC/1.0.0/topology",
            method="DELETE",
            headers=headers,
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_topology_version(self):
        """Test case for delete_topology_version

        Deletes a topology version
        """
        query_string = [("topology_id", 789)]
        headers = [("api_key", "api_key_example")]
        response = self.client.open(
            "/SDX-LC/1.0.0/topology/{version}".format(version=789),
            method="DELETE",
            headers=headers,
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_topology(self):
        """Test case for get_topology

        get an existing topology
        """
        response = self.client.open("/SDX-LC/1.0.0/topology", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_topologyby_version(self):
        """Test case for get_topologyby_version

        Find topology by version
        """
        query_string = [("topology_id", 789)]
        response = self.client.open(
            "/SDX-LC/1.0.0/topology/{version}".format(version=789),
            method="GET",
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_topology_version(self):
        """Test case for topology_version

        Finds topology version
        """
        query_string = [("topology_id", "topology_id_example")]
        response = self.client.open(
            "/SDX-LC/1.0.0/topology/version", method="GET", query_string=query_string
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_update_topology(self):
        """Test case for update_topology

        Update an existing topology
        """
        body = Topology()
        response = self.client.open(
            "/SDX-LC/1.0.0/topology",
            method="PUT",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_upload_file(self):
        """Test case for upload_file

        uploads an topology image
        """
        body = Topology()
        response = self.client.open(
            "/SDX-LC/1.0.0/topology/{topology_id}/uploadImage".format(topology_id=789),
            method="POST",
            data=json.dumps(body),
            content_type="application/octet-stream",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
