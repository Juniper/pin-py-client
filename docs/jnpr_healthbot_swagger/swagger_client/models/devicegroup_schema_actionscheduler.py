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


class DevicegroupSchemaActionscheduler(object):
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
        'disable_trigger_action_schedulers': 'bool'
    }

    attribute_map = {
        'disable_trigger_action_schedulers': 'disable-trigger-action-schedulers'
    }

    def __init__(self, disable_trigger_action_schedulers=None):  # noqa: E501
        """DevicegroupSchemaActionscheduler - a model defined in Swagger"""  # noqa: E501

        self._disable_trigger_action_schedulers = None
        self.discriminator = None

        if disable_trigger_action_schedulers is not None:
            self.disable_trigger_action_schedulers = disable_trigger_action_schedulers

    @property
    def disable_trigger_action_schedulers(self):
        """Gets the disable_trigger_action_schedulers of this DevicegroupSchemaActionscheduler.  # noqa: E501

        If true, disable trigger-action-schedulers service  # noqa: E501

        :return: The disable_trigger_action_schedulers of this DevicegroupSchemaActionscheduler.  # noqa: E501
        :rtype: bool
        """
        return self._disable_trigger_action_schedulers

    @disable_trigger_action_schedulers.setter
    def disable_trigger_action_schedulers(self, disable_trigger_action_schedulers):
        """Sets the disable_trigger_action_schedulers of this DevicegroupSchemaActionscheduler.

        If true, disable trigger-action-schedulers service  # noqa: E501

        :param disable_trigger_action_schedulers: The disable_trigger_action_schedulers of this DevicegroupSchemaActionscheduler.  # noqa: E501
        :type: bool
        """

        self._disable_trigger_action_schedulers = disable_trigger_action_schedulers

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
        if issubclass(DevicegroupSchemaActionscheduler, dict):
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
        if not isinstance(other, DevicegroupSchemaActionscheduler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
