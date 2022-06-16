# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

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


class RuleSchemaRulepropertiesSupporteddevicesReleases(object):
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
        'release_name': 'str',
        'release_support': 'str',
        'sensors': 'list[str]'
    }

    attribute_map = {
        'release_name': 'release-name',
        'release_support': 'release-support',
        'sensors': 'sensors'
    }

    def __init__(self, release_name=None, release_support=None, sensors=None):  # noqa: E501
        """RuleSchemaRulepropertiesSupporteddevicesReleases - a model defined in Swagger"""  # noqa: E501

        self._release_name = None
        self._release_support = None
        self._sensors = None
        self.discriminator = None

        self.release_name = release_name
        if release_support is not None:
            self.release_support = release_support
        if sensors is not None:
            self.sensors = sensors

    @property
    def release_name(self):
        """Gets the release_name of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501

        Release name  # noqa: E501

        :return: The release_name of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """Sets the release_name of this RuleSchemaRulepropertiesSupporteddevicesReleases.

        Release name  # noqa: E501

        :param release_name: The release_name of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501
        :type: str
        """
        if release_name is None:
            raise ValueError("Invalid value for `release_name`, must not be `None`")  # noqa: E501
        if release_name is not None and len(release_name) > 64:
            raise ValueError("Invalid value for `release_name`, length must be less than or equal to `64`")  # noqa: E501
        if release_name is not None and len(release_name) < 1:
            raise ValueError("Invalid value for `release_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._release_name = release_name

    @property
    def release_support(self):
        """Gets the release_support of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501

        Specifies the min/max support for this release  # noqa: E501

        :return: The release_support of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501
        :rtype: str
        """
        return self._release_support

    @release_support.setter
    def release_support(self, release_support):
        """Sets the release_support of this RuleSchemaRulepropertiesSupporteddevicesReleases.

        Specifies the min/max support for this release  # noqa: E501

        :param release_support: The release_support of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501
        :type: str
        """
        allowed_values = ["max-supported-release", "only-on-this-release", "min-supported-release"]  # noqa: E501
        if release_support not in allowed_values:
            raise ValueError(
                "Invalid value for `release_support` ({0}), must be one of {1}"  # noqa: E501
                .format(release_support, allowed_values)
            )

        self._release_support = release_support

    @property
    def sensors(self):
        """Gets the sensors of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501


        :return: The sensors of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501
        :rtype: list[str]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this RuleSchemaRulepropertiesSupporteddevicesReleases.


        :param sensors: The sensors of this RuleSchemaRulepropertiesSupporteddevicesReleases.  # noqa: E501
        :type: list[str]
        """

        self._sensors = sensors

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
        if issubclass(RuleSchemaRulepropertiesSupporteddevicesReleases, dict):
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
        if not isinstance(other, RuleSchemaRulepropertiesSupporteddevicesReleases):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
