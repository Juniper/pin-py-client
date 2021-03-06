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
from swagger_client.api.administration_api import AdministrationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdministrationApi(unittest.TestCase):
    """AdministrationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.administration_api.AdministrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_groups(self):
        """Test case for create_groups

        Create groups  # noqa: E501
        """
        pass

    def test_create_users(self):
        """Test case for create_users

        Create an user.  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete groups  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete list of users.  # noqa: E501
        """
        pass

    def test_flush_groups(self):
        """Test case for flush_groups

        Flush the groups  # noqa: E501
        """
        pass

    def test_flush_users(self):
        """Test case for flush_users

        Flush user base with new set of records.  # noqa: E501
        """
        pass

    def test_get_group_details(self):
        """Test case for get_group_details

        Get lits of all the groups  # noqa: E501
        """
        pass

    def test_get_user_details(self):
        """Test case for get_user_details

        Get lits of all the users  # noqa: E501
        """
        pass

    def test_retrieve_groups(self):
        """Test case for retrieve_groups

        Get lits of all the groups  # noqa: E501
        """
        pass

    def test_retrieve_roles(self):
        """Test case for retrieve_roles

        Get list of all the roles  # noqa: E501
        """
        pass

    def test_retrieve_users(self):
        """Test case for retrieve_users

        Get lits of all the users  # noqa: E501
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Get lits of all the roles  # noqa: E501
        """
        pass

    def test_update_user_profile(self):
        """Test case for update_user_profile

        Update user profile informations.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
