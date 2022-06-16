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
from swagger_client.api.debug_api import DebugApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDebugApi(unittest.TestCase):
    """DebugApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.debug_api.DebugApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_healthbot_debug_generate_configuration(self):
        """Test case for healthbot_debug_generate_configuration

        Request Healthbot MGD service to generate the debug related configuration for healthbot debugger to consume.  # noqa: E501
        """
        pass

    def test_retrieve_debug_for_scenario(self):
        """Test case for retrieve_debug_for_scenario

        Run debugging for the given scenario name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
