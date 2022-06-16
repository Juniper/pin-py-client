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


class DeviceGroupsSchema(object):
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
        'device_group': 'list[DeviceGroupSchema]'
    }

    attribute_map = {
        'device_group': 'device-group'
    }

    def __init__(self, device_group=None):  # noqa: E501
        """DeviceGroupsSchema - a model defined in Swagger"""  # noqa: E501

        self._device_group = None
        self.discriminator = None

        self.device_group = device_group

    @property
    def device_group(self):
        """Gets the device_group of this DeviceGroupsSchema.  # noqa: E501


        :return: The device_group of this DeviceGroupsSchema.  # noqa: E501
        :rtype: list[DeviceGroupSchema]
        """
        return self._device_group

    @device_group.setter
    def device_group(self, device_group):
        """Sets the device_group of this DeviceGroupsSchema.


        :param device_group: The device_group of this DeviceGroupsSchema.  # noqa: E501
        :type: list[DeviceGroupSchema]
        """
        if device_group is None:
            raise ValueError("Invalid value for `device_group`, must not be `None`")  # noqa: E501

        self._device_group = device_group

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
        if issubclass(DeviceGroupsSchema, dict):
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
        if not isinstance(other, DeviceGroupsSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
