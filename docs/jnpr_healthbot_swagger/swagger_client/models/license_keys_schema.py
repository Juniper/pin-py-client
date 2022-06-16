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


class LicenseKeysSchema(object):
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
        'license_key': 'list[LicenseKeySchema]'
    }

    attribute_map = {
        'license_key': 'license-key'
    }

    def __init__(self, license_key=None):  # noqa: E501
        """LicenseKeysSchema - a model defined in Swagger"""  # noqa: E501

        self._license_key = None
        self.discriminator = None

        if license_key is not None:
            self.license_key = license_key

    @property
    def license_key(self):
        """Gets the license_key of this LicenseKeysSchema.  # noqa: E501


        :return: The license_key of this LicenseKeysSchema.  # noqa: E501
        :rtype: list[LicenseKeySchema]
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this LicenseKeysSchema.


        :param license_key: The license_key of this LicenseKeysSchema.  # noqa: E501
        :type: list[LicenseKeySchema]
        """

        self._license_key = license_key

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
        if issubclass(LicenseKeysSchema, dict):
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
        if not isinstance(other, LicenseKeysSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
