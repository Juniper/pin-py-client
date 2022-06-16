{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
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
from swagger_client.api.documentation_api import DocumentationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDocumentationApi(unittest.TestCase):
    """DocumentationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.documentation_api.DocumentationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_defined_api(self):
        """Test case for retrieve_defined_api

        Get all All API's.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
