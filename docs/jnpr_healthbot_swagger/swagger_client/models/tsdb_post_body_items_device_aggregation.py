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


class TsdbPostBodyItemsDeviceAggregation(object):
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
        'add_device_as_tag': 'bool',
        'bottom_limit': 'int',
        'field': 'str',
        'top_limit': 'int'
    }

    attribute_map = {
        'add_device_as_tag': 'addDeviceAsTag',
        'bottom_limit': 'bottomLimit',
        'field': 'field',
        'top_limit': 'topLimit'
    }

    def __init__(self, add_device_as_tag=None, bottom_limit=None, field=None, top_limit=None):  # noqa: E501
        """TsdbPostBodyItemsDeviceAggregation - a model defined in Swagger"""  # noqa: E501

        self._add_device_as_tag = None
        self._bottom_limit = None
        self._field = None
        self._top_limit = None
        self.discriminator = None

        if add_device_as_tag is not None:
            self.add_device_as_tag = add_device_as_tag
        if bottom_limit is not None:
            self.bottom_limit = bottom_limit
        self.field = field
        if top_limit is not None:
            self.top_limit = top_limit

    @property
    def add_device_as_tag(self):
        """Gets the add_device_as_tag of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501

        Add device-id tag as basis for aggregation  # noqa: E501

        :return: The add_device_as_tag of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501
        :rtype: bool
        """
        return self._add_device_as_tag

    @add_device_as_tag.setter
    def add_device_as_tag(self, add_device_as_tag):
        """Sets the add_device_as_tag of this TsdbPostBodyItemsDeviceAggregation.

        Add device-id tag as basis for aggregation  # noqa: E501

        :param add_device_as_tag: The add_device_as_tag of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501
        :type: bool
        """

        self._add_device_as_tag = add_device_as_tag

    @property
    def bottom_limit(self):
        """Gets the bottom_limit of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501

        Fetch bottom N results  # noqa: E501

        :return: The bottom_limit of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501
        :rtype: int
        """
        return self._bottom_limit

    @bottom_limit.setter
    def bottom_limit(self, bottom_limit):
        """Sets the bottom_limit of this TsdbPostBodyItemsDeviceAggregation.

        Fetch bottom N results  # noqa: E501

        :param bottom_limit: The bottom_limit of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501
        :type: int
        """

        self._bottom_limit = bottom_limit

    @property
    def field(self):
        """Gets the field of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501

        Field based on whiuch to aggregate data  # noqa: E501

        :return: The field of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this TsdbPostBodyItemsDeviceAggregation.

        Field based on whiuch to aggregate data  # noqa: E501

        :param field: The field of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501
        :type: str
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def top_limit(self):
        """Gets the top_limit of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501

        Fetch Top N results  # noqa: E501

        :return: The top_limit of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501
        :rtype: int
        """
        return self._top_limit

    @top_limit.setter
    def top_limit(self, top_limit):
        """Sets the top_limit of this TsdbPostBodyItemsDeviceAggregation.

        Fetch Top N results  # noqa: E501

        :param top_limit: The top_limit of this TsdbPostBodyItemsDeviceAggregation.  # noqa: E501
        :type: int
        """

        self._top_limit = top_limit

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
        if issubclass(TsdbPostBodyItemsDeviceAggregation, dict):
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
        if not isinstance(other, TsdbPostBodyItemsDeviceAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
