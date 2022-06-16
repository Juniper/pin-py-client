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


class RollupsummarizationSchemaField1(object):
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
        'aggregate_function': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'aggregate_function': 'aggregate-function',
        'name': 'name'
    }

    def __init__(self, aggregate_function=None, name=None):  # noqa: E501
        """RollupsummarizationSchemaField1 - a model defined in Swagger"""  # noqa: E501

        self._aggregate_function = None
        self._name = None
        self.discriminator = None

        self.aggregate_function = aggregate_function
        self.name = name

    @property
    def aggregate_function(self):
        """Gets the aggregate_function of this RollupsummarizationSchemaField1.  # noqa: E501


        :return: The aggregate_function of this RollupsummarizationSchemaField1.  # noqa: E501
        :rtype: list[str]
        """
        return self._aggregate_function

    @aggregate_function.setter
    def aggregate_function(self, aggregate_function):
        """Sets the aggregate_function of this RollupsummarizationSchemaField1.


        :param aggregate_function: The aggregate_function of this RollupsummarizationSchemaField1.  # noqa: E501
        :type: list[str]
        """
        if aggregate_function is None:
            raise ValueError("Invalid value for `aggregate_function`, must not be `None`")  # noqa: E501
        allowed_values = ["mean", "count", "sum", "std-dev", "last", "first", "max", "min", "90pct", "95pct", "99pct"]  # noqa: E501
        if not set(aggregate_function).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `aggregate_function` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(aggregate_function) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._aggregate_function = aggregate_function

    @property
    def name(self):
        """Gets the name of this RollupsummarizationSchemaField1.  # noqa: E501

        Name of the field. Should be of pattern [a-z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The name of this RollupsummarizationSchemaField1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RollupsummarizationSchemaField1.

        Name of the field. Should be of pattern [a-z][a-zA-Z0-9_-]*  # noqa: E501

        :param name: The name of this RollupsummarizationSchemaField1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(RollupsummarizationSchemaField1, dict):
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
        if not isinstance(other, RollupsummarizationSchemaField1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
