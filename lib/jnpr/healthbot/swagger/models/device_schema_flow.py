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


class DeviceSchemaFlow(object):
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
        'source_ip_addresses': 'list[str]'
    }

    attribute_map = {
        'source_ip_addresses': 'source-ip-addresses'
    }

    def __init__(self, source_ip_addresses=None):  # noqa: E501
        """DeviceSchemaFlow - a model defined in Swagger"""  # noqa: E501

        self._source_ip_addresses = None
        self.discriminator = None

        if source_ip_addresses is not None:
            self.source_ip_addresses = source_ip_addresses

    @property
    def source_ip_addresses(self):
        """Gets the source_ip_addresses of this DeviceSchemaFlow.  # noqa: E501


        :return: The source_ip_addresses of this DeviceSchemaFlow.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_ip_addresses

    @source_ip_addresses.setter
    def source_ip_addresses(self, source_ip_addresses):
        """Sets the source_ip_addresses of this DeviceSchemaFlow.


        :param source_ip_addresses: The source_ip_addresses of this DeviceSchemaFlow.  # noqa: E501
        :type: list[str]
        """

        self._source_ip_addresses = source_ip_addresses

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
        if issubclass(DeviceSchemaFlow, dict):
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
        if not isinstance(other, DeviceSchemaFlow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
