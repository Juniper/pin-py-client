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


class AffectedGroups(object):
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
        'device_groups': 'list[str]',
        'network_groups': 'list[str]'
    }

    attribute_map = {
        'device_groups': 'device-groups',
        'network_groups': 'network-groups'
    }

    def __init__(self, device_groups=None, network_groups=None):  # noqa: E501
        """AffectedGroups - a model defined in Swagger"""  # noqa: E501

        self._device_groups = None
        self._network_groups = None
        self.discriminator = None

        if device_groups is not None:
            self.device_groups = device_groups
        if network_groups is not None:
            self.network_groups = network_groups

    @property
    def device_groups(self):
        """Gets the device_groups of this AffectedGroups.  # noqa: E501


        :return: The device_groups of this AffectedGroups.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_groups

    @device_groups.setter
    def device_groups(self, device_groups):
        """Sets the device_groups of this AffectedGroups.


        :param device_groups: The device_groups of this AffectedGroups.  # noqa: E501
        :type: list[str]
        """

        self._device_groups = device_groups

    @property
    def network_groups(self):
        """Gets the network_groups of this AffectedGroups.  # noqa: E501


        :return: The network_groups of this AffectedGroups.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_groups

    @network_groups.setter
    def network_groups(self, network_groups):
        """Sets the network_groups of this AffectedGroups.


        :param network_groups: The network_groups of this AffectedGroups.  # noqa: E501
        :type: list[str]
        """

        self._network_groups = network_groups

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
        if issubclass(AffectedGroups, dict):
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
        if not isinstance(other, AffectedGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
