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


class RuleSchemaFormula1(object):
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
        '_and': 'RuleSchemaFormula1And',
        '_or': 'RuleSchemaFormula1Or',
        'unique': 'RuleSchemaFormula1Unique',
        'unless': 'RuleSchemaFormula1Unless'
    }

    attribute_map = {
        '_and': 'and',
        '_or': 'or',
        'unique': 'unique',
        'unless': 'unless'
    }

    def __init__(self, _and=None, _or=None, unique=None, unless=None):  # noqa: E501
        """RuleSchemaFormula1 - a model defined in Swagger"""  # noqa: E501

        self.__and = None
        self.__or = None
        self._unique = None
        self._unless = None
        self.discriminator = None

        if _and is not None:
            self._and = _and
        if _or is not None:
            self._or = _or
        if unique is not None:
            self.unique = unique
        if unless is not None:
            self.unless = unless

    @property
    def _and(self):
        """Gets the _and of this RuleSchemaFormula1.  # noqa: E501


        :return: The _and of this RuleSchemaFormula1.  # noqa: E501
        :rtype: RuleSchemaFormula1And
        """
        return self.__and

    @_and.setter
    def _and(self, _and):
        """Sets the _and of this RuleSchemaFormula1.


        :param _and: The _and of this RuleSchemaFormula1.  # noqa: E501
        :type: RuleSchemaFormula1And
        """

        self.__and = _and

    @property
    def _or(self):
        """Gets the _or of this RuleSchemaFormula1.  # noqa: E501


        :return: The _or of this RuleSchemaFormula1.  # noqa: E501
        :rtype: RuleSchemaFormula1Or
        """
        return self.__or

    @_or.setter
    def _or(self, _or):
        """Sets the _or of this RuleSchemaFormula1.


        :param _or: The _or of this RuleSchemaFormula1.  # noqa: E501
        :type: RuleSchemaFormula1Or
        """

        self.__or = _or

    @property
    def unique(self):
        """Gets the unique of this RuleSchemaFormula1.  # noqa: E501


        :return: The unique of this RuleSchemaFormula1.  # noqa: E501
        :rtype: RuleSchemaFormula1Unique
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this RuleSchemaFormula1.


        :param unique: The unique of this RuleSchemaFormula1.  # noqa: E501
        :type: RuleSchemaFormula1Unique
        """

        self._unique = unique

    @property
    def unless(self):
        """Gets the unless of this RuleSchemaFormula1.  # noqa: E501


        :return: The unless of this RuleSchemaFormula1.  # noqa: E501
        :rtype: RuleSchemaFormula1Unless
        """
        return self._unless

    @unless.setter
    def unless(self, unless):
        """Sets the unless of this RuleSchemaFormula1.


        :param unless: The unless of this RuleSchemaFormula1.  # noqa: E501
        :type: RuleSchemaFormula1Unless
        """

        self._unless = unless

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
        if issubclass(RuleSchemaFormula1, dict):
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
        if not isinstance(other, RuleSchemaFormula1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
