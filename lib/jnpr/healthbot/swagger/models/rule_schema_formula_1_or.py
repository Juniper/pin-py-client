{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
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


class RuleSchemaFormula1Or(object):
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
        'left_vector': 'str',
        'right_vector': 'str'
    }

    attribute_map = {
        'left_vector': 'left-vector',
        'right_vector': 'right-vector'
    }

    def __init__(self, left_vector=None, right_vector=None):  # noqa: E501
        """RuleSchemaFormula1Or - a model defined in Swagger"""  # noqa: E501

        self._left_vector = None
        self._right_vector = None
        self.discriminator = None

        self.left_vector = left_vector
        self.right_vector = right_vector

    @property
    def left_vector(self):
        """Gets the left_vector of this RuleSchemaFormula1Or.  # noqa: E501

        Vector name. Pattern for giving vector name is @[a-z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The left_vector of this RuleSchemaFormula1Or.  # noqa: E501
        :rtype: str
        """
        return self._left_vector

    @left_vector.setter
    def left_vector(self, left_vector):
        """Sets the left_vector of this RuleSchemaFormula1Or.

        Vector name. Pattern for giving vector name is @[a-z][a-zA-Z0-9_-]*  # noqa: E501

        :param left_vector: The left_vector of this RuleSchemaFormula1Or.  # noqa: E501
        :type: str
        """
        if left_vector is None:
            raise ValueError("Invalid value for `left_vector`, must not be `None`")  # noqa: E501
        if left_vector is not None and not re.search('^@[a-z][a-zA-Z0-9_-]*$', left_vector):  # noqa: E501
            raise ValueError("Invalid value for `left_vector`, must be a follow pattern or equal to `/^@[a-z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._left_vector = left_vector

    @property
    def right_vector(self):
        """Gets the right_vector of this RuleSchemaFormula1Or.  # noqa: E501

        Vector name. Pattern for giving vector name is @[a-z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The right_vector of this RuleSchemaFormula1Or.  # noqa: E501
        :rtype: str
        """
        return self._right_vector

    @right_vector.setter
    def right_vector(self, right_vector):
        """Sets the right_vector of this RuleSchemaFormula1Or.

        Vector name. Pattern for giving vector name is @[a-z][a-zA-Z0-9_-]*  # noqa: E501

        :param right_vector: The right_vector of this RuleSchemaFormula1Or.  # noqa: E501
        :type: str
        """
        if right_vector is None:
            raise ValueError("Invalid value for `right_vector`, must not be `None`")  # noqa: E501
        if right_vector is not None and not re.search('^@[a-z][a-zA-Z0-9_-]*$', right_vector):  # noqa: E501
            raise ValueError("Invalid value for `right_vector`, must be a follow pattern or equal to `/^@[a-z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._right_vector = right_vector

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RuleSchemaFormula1Or):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
