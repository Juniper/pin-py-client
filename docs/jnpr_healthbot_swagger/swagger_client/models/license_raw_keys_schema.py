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


class LicenseRawKeysSchema(object):
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
        'license_raw_key': 'list[LicenseRawKeySchema]'
    }

    attribute_map = {
        'license_raw_key': 'license-raw-key'
    }

    def __init__(self, license_raw_key=None):  # noqa: E501
        """LicenseRawKeysSchema - a model defined in Swagger"""  # noqa: E501

        self._license_raw_key = None
        self.discriminator = None

        self.license_raw_key = license_raw_key

    @property
    def license_raw_key(self):
        """Gets the license_raw_key of this LicenseRawKeysSchema.  # noqa: E501


        :return: The license_raw_key of this LicenseRawKeysSchema.  # noqa: E501
        :rtype: list[LicenseRawKeySchema]
        """
        return self._license_raw_key

    @license_raw_key.setter
    def license_raw_key(self, license_raw_key):
        """Sets the license_raw_key of this LicenseRawKeysSchema.


        :param license_raw_key: The license_raw_key of this LicenseRawKeysSchema.  # noqa: E501
        :type: list[LicenseRawKeySchema]
        """
        if license_raw_key is None:
            raise ValueError("Invalid value for `license_raw_key`, must not be `None`")  # noqa: E501

        self._license_raw_key = license_raw_key

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
        if issubclass(LicenseRawKeysSchema, dict):
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
        if not isinstance(other, LicenseRawKeysSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
