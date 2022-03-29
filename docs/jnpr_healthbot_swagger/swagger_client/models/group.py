# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Group(object):
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
        'group_description': 'str',
        'roles': 'list[GroupgroupidRoles]',
        'users': 'list[GroupgroupidUsers]'
    }

    attribute_map = {
        'group_description': 'groupDescription',
        'roles': 'roles',
        'users': 'users'
    }

    def __init__(self, group_description=None, roles=None, users=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501

        self._group_description = None
        self._roles = None
        self._users = None
        self.discriminator = None

        if group_description is not None:
            self.group_description = group_description
        if roles is not None:
            self.roles = roles
        if users is not None:
            self.users = users

    @property
    def group_description(self):
        """Gets the group_description of this Group.  # noqa: E501

        Details of the group  # noqa: E501

        :return: The group_description of this Group.  # noqa: E501
        :rtype: str
        """
        return self._group_description

    @group_description.setter
    def group_description(self, group_description):
        """Sets the group_description of this Group.

        Details of the group  # noqa: E501

        :param group_description: The group_description of this Group.  # noqa: E501
        :type: str
        """

        self._group_description = group_description

    @property
    def roles(self):
        """Gets the roles of this Group.  # noqa: E501

        list of roles associated  # noqa: E501

        :return: The roles of this Group.  # noqa: E501
        :rtype: list[GroupgroupidRoles]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Group.

        list of roles associated  # noqa: E501

        :param roles: The roles of this Group.  # noqa: E501
        :type: list[GroupgroupidRoles]
        """

        self._roles = roles

    @property
    def users(self):
        """Gets the users of this Group.  # noqa: E501

        list of users associated  # noqa: E501

        :return: The users of this Group.  # noqa: E501
        :rtype: list[GroupgroupidUsers]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Group.

        list of users associated  # noqa: E501

        :param users: The users of this Group.  # noqa: E501
        :type: list[GroupgroupidUsers]
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
        if issubclass(Group, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other