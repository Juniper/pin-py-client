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


class PatternSetSchema(object):
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
        'description': 'str',
        'name': 'str',
        'pattern_names': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'pattern_names': 'pattern-names'
    }

    def __init__(self, description=None, name=None, pattern_names=None):  # noqa: E501
        """PatternSetSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self._pattern_names = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        if pattern_names is not None:
            self.pattern_names = pattern_names

    @property
    def description(self):
        """Gets the description of this PatternSetSchema.  # noqa: E501

        Pattern-set description  # noqa: E501

        :return: The description of this PatternSetSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatternSetSchema.

        Pattern-set description  # noqa: E501

        :param description: The description of this PatternSetSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this PatternSetSchema.  # noqa: E501

        Name of a pattern-set. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The name of this PatternSetSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatternSetSchema.

        Name of a pattern-set. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param name: The name of this PatternSetSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def pattern_names(self):
        """Gets the pattern_names of this PatternSetSchema.  # noqa: E501


        :return: The pattern_names of this PatternSetSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._pattern_names

    @pattern_names.setter
    def pattern_names(self, pattern_names):
        """Sets the pattern_names of this PatternSetSchema.


        :param pattern_names: The pattern_names of this PatternSetSchema.  # noqa: E501
        :type: list[str]
        """

        self._pattern_names = pattern_names

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
        if issubclass(PatternSetSchema, dict):
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
        if not isinstance(other, PatternSetSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
