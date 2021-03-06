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


import pprint
import re  # noqa: F401

import six

from jnpr.healthbot.swagger.models.associated_role_schema import AssociatedRoleSchema  # noqa: F401,E501
from jnpr.healthbot.swagger.models.associated_user_schema import AssociatedUserSchema  # noqa: F401,E501


class InlineResponse2007(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'group_id': 'str',
        'group_name': 'str',
        'group_description': 'str',
        'roles': 'AssociatedRoleSchema',
        'users': 'AssociatedUserSchema'
    }

    attribute_map = {
        'group_id': 'groupId',
        'group_name': 'groupName',
        'group_description': 'groupDescription',
        'roles': 'roles',
        'users': 'users'
    }

    def __init__(self, group_id=None, group_name=None, group_description=None, roles=None, users=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501

        self._group_id = None
        self._group_name = None
        self._group_description = None
        self._roles = None
        self._users = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if group_description is not None:
            self.group_description = group_description
        if roles is not None:
            self.roles = roles
        if users is not None:
            self.users = users

    @property
    def group_id(self):
        """Gets the group_id of this InlineResponse2007.  # noqa: E501

        ID generated by system  # noqa: E501

        :return: The group_id of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this InlineResponse2007.

        ID generated by system  # noqa: E501

        :param group_id: The group_id of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this InlineResponse2007.  # noqa: E501

        Name of the group  # noqa: E501

        :return: The group_name of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this InlineResponse2007.

        Name of the group  # noqa: E501

        :param group_name: The group_name of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_description(self):
        """Gets the group_description of this InlineResponse2007.  # noqa: E501

        Details of the group  # noqa: E501

        :return: The group_description of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._group_description

    @group_description.setter
    def group_description(self, group_description):
        """Sets the group_description of this InlineResponse2007.

        Details of the group  # noqa: E501

        :param group_description: The group_description of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._group_description = group_description

    @property
    def roles(self):
        """Gets the roles of this InlineResponse2007.  # noqa: E501


        :return: The roles of this InlineResponse2007.  # noqa: E501
        :rtype: AssociatedRoleSchema
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this InlineResponse2007.


        :param roles: The roles of this InlineResponse2007.  # noqa: E501
        :type: AssociatedRoleSchema
        """

        self._roles = roles

    @property
    def users(self):
        """Gets the users of this InlineResponse2007.  # noqa: E501


        :return: The users of this InlineResponse2007.  # noqa: E501
        :rtype: AssociatedUserSchema
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this InlineResponse2007.


        :param users: The users of this InlineResponse2007.  # noqa: E501
        :type: AssociatedUserSchema
        """

        self._users = users

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
