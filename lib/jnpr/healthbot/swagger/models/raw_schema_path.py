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


class RawSchemaPath(object):
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
        'aggregation_functions': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'aggregation_functions': 'aggregation-functions',
        'name': 'name'
    }

    def __init__(self, aggregation_functions=None, name=None):  # noqa: E501
        """RawSchemaPath - a model defined in Swagger"""  # noqa: E501

        self._aggregation_functions = None
        self._name = None
        self.discriminator = None

        self.aggregation_functions = aggregation_functions
        self.name = name

    @property
    def aggregation_functions(self):
        """Gets the aggregation_functions of this RawSchemaPath.  # noqa: E501


        :return: The aggregation_functions of this RawSchemaPath.  # noqa: E501
        :rtype: list[str]
        """
        return self._aggregation_functions

    @aggregation_functions.setter
    def aggregation_functions(self, aggregation_functions):
        """Sets the aggregation_functions of this RawSchemaPath.


        :param aggregation_functions: The aggregation_functions of this RawSchemaPath.  # noqa: E501
        :type: list[str]
        """
        if aggregation_functions is None:
            raise ValueError("Invalid value for `aggregation_functions`, must not be `None`")  # noqa: E501
        allowed_values = ["latest", "sum", "count", "mean", "min", "max", "on-change", "stddev"]  # noqa: E501
        if not set(aggregation_functions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `aggregation_functions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(aggregation_functions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._aggregation_functions = aggregation_functions

    @property
    def name(self):
        """Gets the name of this RawSchemaPath.  # noqa: E501

        Sensor field path for which summarization should be changed. Apart from JTI OC sensor path, '<sensor-name>:' should be prepended to the sensor path  # noqa: E501

        :return: The name of this RawSchemaPath.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RawSchemaPath.

        Sensor field path for which summarization should be changed. Apart from JTI OC sensor path, '<sensor-name>:' should be prepended to the sensor path  # noqa: E501

        :param name: The name of this RawSchemaPath.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

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
        if issubclass(RawSchemaPath, dict):
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
        if not isinstance(other, RawSchemaPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other