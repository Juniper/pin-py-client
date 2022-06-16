{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TlivekafkaocSchemaSecuritySasl(object):
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
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, password=None, username=None):  # noqa: E501
        """TlivekafkaocSchemaSecuritySasl - a model defined in Swagger"""  # noqa: E501

        self._password = None
        self._username = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if username is not None:
            self.username = username

    @property
    def password(self):
        """Gets the password of this TlivekafkaocSchemaSecuritySasl.  # noqa: E501

        SASL password  # noqa: E501

        :return: The password of this TlivekafkaocSchemaSecuritySasl.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TlivekafkaocSchemaSecuritySasl.

        SASL password  # noqa: E501

        :param password: The password of this TlivekafkaocSchemaSecuritySasl.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def username(self):
        """Gets the username of this TlivekafkaocSchemaSecuritySasl.  # noqa: E501

        SASL username  # noqa: E501

        :return: The username of this TlivekafkaocSchemaSecuritySasl.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TlivekafkaocSchemaSecuritySasl.

        SASL username  # noqa: E501

        :param username: The username of this TlivekafkaocSchemaSecuritySasl.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(TlivekafkaocSchemaSecuritySasl, dict):
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
        if not isinstance(other, TlivekafkaocSchemaSecuritySasl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
