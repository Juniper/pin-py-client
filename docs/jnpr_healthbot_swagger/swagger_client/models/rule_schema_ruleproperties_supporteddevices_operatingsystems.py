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


class RuleSchemaRulepropertiesSupporteddevicesOperatingsystems(object):
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
        'os_name': 'str',
        'products': 'list[RuleSchemaRulepropertiesSupporteddevicesProducts]',
        'sensors': 'list[str]'
    }

    attribute_map = {
        'os_name': 'os-name',
        'products': 'products',
        'sensors': 'sensors'
    }

    def __init__(self, os_name=None, products=None, sensors=None):  # noqa: E501
        """RuleSchemaRulepropertiesSupporteddevicesOperatingsystems - a model defined in Swagger"""  # noqa: E501

        self._os_name = None
        self._products = None
        self._sensors = None
        self.discriminator = None

        self.os_name = os_name
        if products is not None:
            self.products = products
        if sensors is not None:
            self.sensors = sensors

    @property
    def os_name(self):
        """Gets the os_name of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501

        Operating system for the supported devices  # noqa: E501

        :return: The os_name of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.

        Operating system for the supported devices  # noqa: E501

        :param os_name: The os_name of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501
        :type: str
        """
        if os_name is None:
            raise ValueError("Invalid value for `os_name`, must not be `None`")  # noqa: E501
        if os_name is not None and len(os_name) > 64:
            raise ValueError("Invalid value for `os_name`, length must be less than or equal to `64`")  # noqa: E501
        if os_name is not None and len(os_name) < 1:
            raise ValueError("Invalid value for `os_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._os_name = os_name

    @property
    def products(self):
        """Gets the products of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501

        Product information of the device  # noqa: E501

        :return: The products of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501
        :rtype: list[RuleSchemaRulepropertiesSupporteddevicesProducts]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.

        Product information of the device  # noqa: E501

        :param products: The products of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501
        :type: list[RuleSchemaRulepropertiesSupporteddevicesProducts]
        """

        self._products = products

    @property
    def sensors(self):
        """Gets the sensors of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501


        :return: The sensors of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501
        :rtype: list[str]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.


        :param sensors: The sensors of this RuleSchemaRulepropertiesSupporteddevicesOperatingsystems.  # noqa: E501
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
        if issubclass(RuleSchemaRulepropertiesSupporteddevicesOperatingsystems, dict):
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
        if not isinstance(other, RuleSchemaRulepropertiesSupporteddevicesOperatingsystems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
