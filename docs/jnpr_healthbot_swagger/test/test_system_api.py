# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.system_api import SystemApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.system_api.SystemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_available_nodes(self):
        """Test case for retrieve_available_nodes

        List of available nodes  # noqa: E501
        """
        pass

    def test_retrieve_sensor_device_group(self):
        """Test case for retrieve_sensor_device_group

        Get all All API's.  # noqa: E501
        """
        pass

    def test_retrieve_system_details(self):
        """Test case for retrieve_system_details

        Retrieve system details.  # noqa: E501
        """
        pass

    def test_retrieve_tsdb_counters(self):
        """Test case for retrieve_tsdb_counters

        TSDB counters  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
