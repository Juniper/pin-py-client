# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IngestsettingsSchemaIngestsettings(object):
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
        'flow': 'IngestsettingsSchemaIngestsettingsFlow',
        'syslog': 'IngestsettingsSchemaIngestsettingsSyslog',
        'byoi': 'IngestsettingsSchemaIngestsettingsByoi',
        'frequency_profile': 'list[IngestsettingsSchemaIngestsettingsFrequencyprofile]'
    }

    attribute_map = {
        'flow': 'flow',
        'syslog': 'syslog',
        'byoi': 'byoi',
        'frequency_profile': 'frequency-profile'
    }

    def __init__(self, flow=None, syslog=None, byoi=None, frequency_profile=None):  # noqa: E501
        """IngestsettingsSchemaIngestsettings - a model defined in Swagger"""  # noqa: E501

        self._flow = None
        self._syslog = None
        self._byoi = None
        self._frequency_profile = None
        self.discriminator = None

        if flow is not None:
            self.flow = flow
        if syslog is not None:
            self.syslog = syslog
        if byoi is not None:
            self.byoi = byoi
        if frequency_profile is not None:
            self.frequency_profile = frequency_profile

    @property
    def flow(self):
        """Gets the flow of this IngestsettingsSchemaIngestsettings.  # noqa: E501


        :return: The flow of this IngestsettingsSchemaIngestsettings.  # noqa: E501
        :rtype: IngestsettingsSchemaIngestsettingsFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this IngestsettingsSchemaIngestsettings.


        :param flow: The flow of this IngestsettingsSchemaIngestsettings.  # noqa: E501
        :type: IngestsettingsSchemaIngestsettingsFlow
        """

        self._flow = flow

    @property
    def syslog(self):
        """Gets the syslog of this IngestsettingsSchemaIngestsettings.  # noqa: E501


        :return: The syslog of this IngestsettingsSchemaIngestsettings.  # noqa: E501
        :rtype: IngestsettingsSchemaIngestsettingsSyslog
        """
        return self._syslog

    @syslog.setter
    def syslog(self, syslog):
        """Sets the syslog of this IngestsettingsSchemaIngestsettings.


        :param syslog: The syslog of this IngestsettingsSchemaIngestsettings.  # noqa: E501
        :type: IngestsettingsSchemaIngestsettingsSyslog
        """

        self._syslog = syslog

    @property
    def byoi(self):
        """Gets the byoi of this IngestsettingsSchemaIngestsettings.  # noqa: E501


        :return: The byoi of this IngestsettingsSchemaIngestsettings.  # noqa: E501
        :rtype: IngestsettingsSchemaIngestsettingsByoi
        """
        return self._byoi

    @byoi.setter
    def byoi(self, byoi):
        """Sets the byoi of this IngestsettingsSchemaIngestsettings.


        :param byoi: The byoi of this IngestsettingsSchemaIngestsettings.  # noqa: E501
        :type: IngestsettingsSchemaIngestsettingsByoi
        """

        self._byoi = byoi

    @property
    def frequency_profile(self):
        """Gets the frequency_profile of this IngestsettingsSchemaIngestsettings.  # noqa: E501


        :return: The frequency_profile of this IngestsettingsSchemaIngestsettings.  # noqa: E501
        :rtype: list[IngestsettingsSchemaIngestsettingsFrequencyprofile]
        """
        return self._frequency_profile

    @frequency_profile.setter
    def frequency_profile(self, frequency_profile):
        """Sets the frequency_profile of this IngestsettingsSchemaIngestsettings.


        :param frequency_profile: The frequency_profile of this IngestsettingsSchemaIngestsettings.  # noqa: E501
        :type: list[IngestsettingsSchemaIngestsettingsFrequencyprofile]
        """

        self._frequency_profile = frequency_profile

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
        if issubclass(IngestsettingsSchemaIngestsettings, dict):
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
        if not isinstance(other, IngestsettingsSchemaIngestsettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
