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


class Snmpv3UsmUserSchema(object):
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
        'authentication': 'Snmpv3usmuserSchemaAuthentication',
        'authentication_none': 'list[ERRORUNKNOWN]',
        'privacy': 'Snmpv3usmuserSchemaPrivacy',
        'privacy_none': 'list[ERRORUNKNOWN]',
        'username': 'str'
    }

    attribute_map = {
        'authentication': 'authentication',
        'authentication_none': 'authentication-none',
        'privacy': 'privacy',
        'privacy_none': 'privacy-none',
        'username': 'username'
    }

    def __init__(self, authentication=None, authentication_none=None, privacy=None, privacy_none=None, username=None):  # noqa: E501
        """Snmpv3UsmUserSchema - a model defined in Swagger"""  # noqa: E501

        self._authentication = None
        self._authentication_none = None
        self._privacy = None
        self._privacy_none = None
        self._username = None
        self.discriminator = None

        if authentication is not None:
            self.authentication = authentication
        if authentication_none is not None:
            self.authentication_none = authentication_none
        if privacy is not None:
            self.privacy = privacy
        if privacy_none is not None:
            self.privacy_none = privacy_none
        self.username = username

    @property
    def authentication(self):
        """Gets the authentication of this Snmpv3UsmUserSchema.  # noqa: E501


        :return: The authentication of this Snmpv3UsmUserSchema.  # noqa: E501
        :rtype: Snmpv3usmuserSchemaAuthentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this Snmpv3UsmUserSchema.


        :param authentication: The authentication of this Snmpv3UsmUserSchema.  # noqa: E501
        :type: Snmpv3usmuserSchemaAuthentication
        """

        self._authentication = authentication

    @property
    def authentication_none(self):
        """Gets the authentication_none of this Snmpv3UsmUserSchema.  # noqa: E501

        Configure no authentication for the SNMPv3 user  # noqa: E501

        :return: The authentication_none of this Snmpv3UsmUserSchema.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._authentication_none

    @authentication_none.setter
    def authentication_none(self, authentication_none):
        """Sets the authentication_none of this Snmpv3UsmUserSchema.

        Configure no authentication for the SNMPv3 user  # noqa: E501

        :param authentication_none: The authentication_none of this Snmpv3UsmUserSchema.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._authentication_none = authentication_none

    @property
    def privacy(self):
        """Gets the privacy of this Snmpv3UsmUserSchema.  # noqa: E501


        :return: The privacy of this Snmpv3UsmUserSchema.  # noqa: E501
        :rtype: Snmpv3usmuserSchemaPrivacy
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this Snmpv3UsmUserSchema.


        :param privacy: The privacy of this Snmpv3UsmUserSchema.  # noqa: E501
        :type: Snmpv3usmuserSchemaPrivacy
        """

        self._privacy = privacy

    @property
    def privacy_none(self):
        """Gets the privacy_none of this Snmpv3UsmUserSchema.  # noqa: E501

        Configure no privacy for the SNMPv3 user  # noqa: E501

        :return: The privacy_none of this Snmpv3UsmUserSchema.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._privacy_none

    @privacy_none.setter
    def privacy_none(self, privacy_none):
        """Sets the privacy_none of this Snmpv3UsmUserSchema.

        Configure no privacy for the SNMPv3 user  # noqa: E501

        :param privacy_none: The privacy_none of this Snmpv3UsmUserSchema.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._privacy_none = privacy_none

    @property
    def username(self):
        """Gets the username of this Snmpv3UsmUserSchema.  # noqa: E501

        SNMPv3 username  # noqa: E501

        :return: The username of this Snmpv3UsmUserSchema.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Snmpv3UsmUserSchema.

        SNMPv3 username  # noqa: E501

        :param username: The username of this Snmpv3UsmUserSchema.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if username is not None and len(username) > 255:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

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
        if issubclass(Snmpv3UsmUserSchema, dict):
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
        if not isinstance(other, Snmpv3UsmUserSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
