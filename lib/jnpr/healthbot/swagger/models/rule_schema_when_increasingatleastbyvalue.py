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


class RuleSchemaWhenIncreasingatleastbyvalue(object):
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
        'all': 'list[object]',
        'any': 'list[object]',
        'latest': 'list[object]',
        'field_name': 'str',
        'time_range': 'str',
        'value': 'str'
    }

    attribute_map = {
        'all': 'all',
        'any': 'any',
        'latest': 'latest',
        'field_name': 'field-name',
        'time_range': 'time-range',
        'value': 'value'
    }

    def __init__(self, all=None, any=None, latest=None, field_name=None, time_range=None, value=None):  # noqa: E501
        """RuleSchemaWhenIncreasingatleastbyvalue - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self._any = None
        self._latest = None
        self._field_name = None
        self._time_range = None
        self._value = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if any is not None:
            self.any = any
        if latest is not None:
            self.latest = latest
        self.field_name = field_name
        if time_range is not None:
            self.time_range = time_range
        if value is not None:
            self.value = value

    @property
    def all(self):
        """Gets the all of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501

        With this flag, result is set to True only if all the data matches the given condition  # noqa: E501

        :return: The all of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :rtype: list[object]
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this RuleSchemaWhenIncreasingatleastbyvalue.

        With this flag, result is set to True only if all the data matches the given condition  # noqa: E501

        :param all: The all of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :type: list[object]
        """

        self._all = all

    @property
    def any(self):
        """Gets the any of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501

        With this flag, result is set to True if any one of the data matches the condition  # noqa: E501

        :return: The any of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :rtype: list[object]
        """
        return self._any

    @any.setter
    def any(self, any):
        """Sets the any of this RuleSchemaWhenIncreasingatleastbyvalue.

        With this flag, result is set to True if any one of the data matches the condition  # noqa: E501

        :param any: The any of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :type: list[object]
        """

        self._any = any

    @property
    def latest(self):
        """Gets the latest of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501

        With this flag, result is set to True if the latest data matches the condition  # noqa: E501

        :return: The latest of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :rtype: list[object]
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this RuleSchemaWhenIncreasingatleastbyvalue.

        With this flag, result is set to True if the latest data matches the condition  # noqa: E501

        :param latest: The latest of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :type: list[object]
        """

        self._latest = latest

    @property
    def field_name(self):
        """Gets the field_name of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501

        Field name. Should match the pattern $[a-z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The field_name of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this RuleSchemaWhenIncreasingatleastbyvalue.

        Field name. Should match the pattern $[a-z][a-zA-Z0-9_-]*  # noqa: E501

        :param field_name: The field_name of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501
        if field_name is not None and not re.search(r'^\\$[a-z][a-zA-Z0-9_-]*$', field_name):  # noqa: E501
            raise ValueError(r"Invalid value for `field_name`, must be a follow pattern or equal to `/^\\$[a-z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._field_name = field_name

    @property
    def time_range(self):
        """Gets the time_range of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :return: The time_range of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this RuleSchemaWhenIncreasingatleastbyvalue.

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :param time_range: The time_range of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :type: str
        """
        if time_range is not None and not re.search(r'^[1-9][0-9]*(\\.[0-9]+)?(o|s|m|h|d|w|y|offset)$', time_range):  # noqa: E501
            raise ValueError(r"Invalid value for `time_range`, must be a follow pattern or equal to `/^[1-9][0-9]*(\\.[0-9]+)?(o|s|m|h|d|w|y|offset)$/`")  # noqa: E501

        self._time_range = time_range

    @property
    def value(self):
        """Gets the value of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501

        Value of increase between current and last reported values  # noqa: E501

        :return: The value of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RuleSchemaWhenIncreasingatleastbyvalue.

        Value of increase between current and last reported values  # noqa: E501

        :param value: The value of this RuleSchemaWhenIncreasingatleastbyvalue.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(RuleSchemaWhenIncreasingatleastbyvalue, dict):
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
        if not isinstance(other, RuleSchemaWhenIncreasingatleastbyvalue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
