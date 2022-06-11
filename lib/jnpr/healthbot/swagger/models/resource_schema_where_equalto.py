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


class ResourceSchemaWhereEqualto(object):
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
        'right_operand': 'str'
    }

    attribute_map = {
        'left_operand': 'left-operand',
        'right_operand': 'right-operand'
    }

    def __init__(self, left_operand=None, right_operand=None):  # noqa: E501
        """ResourceSchemaWhereEqualto - a model defined in Swagger"""  # noqa: E501

        self._left_operand = None
        self._right_operand = None
        self.discriminator = None

        self.left_operand = left_operand
        self.right_operand = right_operand

    @property
    def left_operand(self):
        """Gets the left_operand of this ResourceSchemaWhereEqualto.  # noqa: E501

        Left operand  # noqa: E501

        :return: The left_operand of this ResourceSchemaWhereEqualto.  # noqa: E501
        :rtype: str
        """
        return self._left_operand

    @left_operand.setter
    def left_operand(self, left_operand):
        """Sets the left_operand of this ResourceSchemaWhereEqualto.

        Left operand  # noqa: E501

        :param left_operand: The left_operand of this ResourceSchemaWhereEqualto.  # noqa: E501
        :type: str
        """
        if left_operand is None:
            raise ValueError("Invalid value for `left_operand`, must not be `None`")  # noqa: E501
        if left_operand is not None and not re.search(r'^\\S+$', left_operand):  # noqa: E501
            raise ValueError(r"Invalid value for `left_operand`, must be a follow pattern or equal to `/^\\S+$/`")  # noqa: E501

        self._left_operand = left_operand

    @property
    def right_operand(self):
        """Gets the right_operand of this ResourceSchemaWhereEqualto.  # noqa: E501

        right operand  # noqa: E501

        :return: The right_operand of this ResourceSchemaWhereEqualto.  # noqa: E501
        :rtype: str
        """
        return self._right_operand

    @right_operand.setter
    def right_operand(self, right_operand):
        """Sets the right_operand of this ResourceSchemaWhereEqualto.

        right operand  # noqa: E501

        :param right_operand: The right_operand of this ResourceSchemaWhereEqualto.  # noqa: E501
        :type: str
        """
        if right_operand is None:
            raise ValueError("Invalid value for `right_operand`, must not be `None`")  # noqa: E501
        if right_operand is not None and not re.search(r'^\\S+$', right_operand):  # noqa: E501
            raise ValueError(r"Invalid value for `right_operand`, must be a follow pattern or equal to `/^\\S+$/`")  # noqa: E501

        self._right_operand = right_operand

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
        if issubclass(ResourceSchemaWhereEqualto, dict):
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
        if not isinstance(other, ResourceSchemaWhereEqualto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
