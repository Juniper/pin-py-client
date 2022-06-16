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


class TaggingprofileSchemaWhenDoesnotmatchwith(object):
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
        'left_operand': 'str',
        'right_operand': 'str',
        'in_memory': 'bool'
    }

    attribute_map = {
        'left_operand': 'left-operand',
        'right_operand': 'right-operand',
        'in_memory': 'in-memory'
    }

    def __init__(self, left_operand=None, right_operand=None, in_memory=None):  # noqa: E501
        """TaggingprofileSchemaWhenDoesnotmatchwith - a model defined in Swagger"""  # noqa: E501

        self._left_operand = None
        self._right_operand = None
        self._in_memory = None
        self.discriminator = None

        self.left_operand = left_operand
        self.right_operand = right_operand
        if in_memory is not None:
            self.in_memory = in_memory

    @property
    def left_operand(self):
        """Gets the left_operand of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501

        Left operand. This is the string in which we have to match the expression  # noqa: E501

        :return: The left_operand of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501
        :rtype: str
        """
        return self._left_operand

    @left_operand.setter
    def left_operand(self, left_operand):
        """Sets the left_operand of this TaggingprofileSchemaWhenDoesnotmatchwith.

        Left operand. This is the string in which we have to match the expression  # noqa: E501

        :param left_operand: The left_operand of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501
        :type: str
        """
        if left_operand is None:
            raise ValueError("Invalid value for `left_operand`, must not be `None`")  # noqa: E501

        self._left_operand = left_operand

    @property
    def right_operand(self):
        """Gets the right_operand of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501

        Right operand. This is the match expression  # noqa: E501

        :return: The right_operand of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501
        :rtype: str
        """
        return self._right_operand

    @right_operand.setter
    def right_operand(self, right_operand):
        """Sets the right_operand of this TaggingprofileSchemaWhenDoesnotmatchwith.

        Right operand. This is the match expression  # noqa: E501

        :param right_operand: The right_operand of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501
        :type: str
        """
        if right_operand is None:
            raise ValueError("Invalid value for `right_operand`, must not be `None`")  # noqa: E501

        self._right_operand = right_operand

    @property
    def in_memory(self):
        """Gets the in_memory of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501

        Look for right-operand in internal cache  # noqa: E501

        :return: The in_memory of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501
        :rtype: bool
        """
        return self._in_memory

    @in_memory.setter
    def in_memory(self, in_memory):
        """Sets the in_memory of this TaggingprofileSchemaWhenDoesnotmatchwith.

        Look for right-operand in internal cache  # noqa: E501

        :param in_memory: The in_memory of this TaggingprofileSchemaWhenDoesnotmatchwith.  # noqa: E501
        :type: bool
        """

        self._in_memory = in_memory

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
        if issubclass(TaggingprofileSchemaWhenDoesnotmatchwith, dict):
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
        if not isinstance(other, TaggingprofileSchemaWhenDoesnotmatchwith):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
