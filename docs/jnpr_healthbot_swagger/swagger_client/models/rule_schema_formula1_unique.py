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


class RuleSchemaFormula1Unique(object):
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
        'vector_name': 'str'
    }

    attribute_map = {
        'vector_name': 'vector-name'
    }

    def __init__(self, vector_name=None):  # noqa: E501
        """RuleSchemaFormula1Unique - a model defined in Swagger"""  # noqa: E501

        self._vector_name = None
        self.discriminator = None

        self.vector_name = vector_name

    @property
    def vector_name(self):
        """Gets the vector_name of this RuleSchemaFormula1Unique.  # noqa: E501

        Vector name in which unique elements needs to be computed. Pattern for giving vector name is @[a-z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The vector_name of this RuleSchemaFormula1Unique.  # noqa: E501
        :rtype: str
        """
        return self._vector_name

    @vector_name.setter
    def vector_name(self, vector_name):
        """Sets the vector_name of this RuleSchemaFormula1Unique.

        Vector name in which unique elements needs to be computed. Pattern for giving vector name is @[a-z][a-zA-Z0-9_-]*  # noqa: E501

        :param vector_name: The vector_name of this RuleSchemaFormula1Unique.  # noqa: E501
        :type: str
        """
        if vector_name is None:
            raise ValueError("Invalid value for `vector_name`, must not be `None`")  # noqa: E501
        if vector_name is not None and not re.search(r'^@[a-z][a-zA-Z0-9_-]*$', vector_name):  # noqa: E501
            raise ValueError(r"Invalid value for `vector_name`, must be a follow pattern or equal to `/^@[a-z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._vector_name = vector_name

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
        if issubclass(RuleSchemaFormula1Unique, dict):
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
        if not isinstance(other, RuleSchemaFormula1Unique):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other