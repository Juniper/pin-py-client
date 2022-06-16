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


class RuleSchemaSensor(object):
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
        'data_if_missing': 'RuleSchemaDataifmissing',
        'path': 'str',
        'sensor_name': 'str',
        'where': 'list[RuleSchemaWhere]',
        'zero_suppression': 'list[object]'
    }

    attribute_map = {
        'data_if_missing': 'data-if-missing',
        'path': 'path',
        'sensor_name': 'sensor-name',
        'where': 'where',
        'zero_suppression': 'zero-suppression'
    }

    def __init__(self, data_if_missing=None, path=None, sensor_name=None, where=None, zero_suppression=None):  # noqa: E501
        """RuleSchemaSensor - a model defined in Swagger"""  # noqa: E501

        self._data_if_missing = None
        self._path = None
        self._sensor_name = None
        self._where = None
        self._zero_suppression = None
        self.discriminator = None

        if data_if_missing is not None:
            self.data_if_missing = data_if_missing
        self.path = path
        self.sensor_name = sensor_name
        if where is not None:
            self.where = where
        if zero_suppression is not None:
            self.zero_suppression = zero_suppression

    @property
    def data_if_missing(self):
        """Gets the data_if_missing of this RuleSchemaSensor.  # noqa: E501


        :return: The data_if_missing of this RuleSchemaSensor.  # noqa: E501
        :rtype: RuleSchemaDataifmissing
        """
        return self._data_if_missing

    @data_if_missing.setter
    def data_if_missing(self, data_if_missing):
        """Sets the data_if_missing of this RuleSchemaSensor.


        :param data_if_missing: The data_if_missing of this RuleSchemaSensor.  # noqa: E501
        :type: RuleSchemaDataifmissing
        """

        self._data_if_missing = data_if_missing

    @property
    def path(self):
        """Gets the path of this RuleSchemaSensor.  # noqa: E501

        Sensor path  # noqa: E501

        :return: The path of this RuleSchemaSensor.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RuleSchemaSensor.

        Sensor path  # noqa: E501

        :param path: The path of this RuleSchemaSensor.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if path is not None and not re.search(r'^\\S+$', path):  # noqa: E501
            raise ValueError(r"Invalid value for `path`, must be a follow pattern or equal to `/^\\S+$/`")  # noqa: E501

        self._path = path

    @property
    def sensor_name(self):
        """Gets the sensor_name of this RuleSchemaSensor.  # noqa: E501

        Name of the sensor  # noqa: E501

        :return: The sensor_name of this RuleSchemaSensor.  # noqa: E501
        :rtype: str
        """
        return self._sensor_name

    @sensor_name.setter
    def sensor_name(self, sensor_name):
        """Sets the sensor_name of this RuleSchemaSensor.

        Name of the sensor  # noqa: E501

        :param sensor_name: The sensor_name of this RuleSchemaSensor.  # noqa: E501
        :type: str
        """
        if sensor_name is None:
            raise ValueError("Invalid value for `sensor_name`, must not be `None`")  # noqa: E501
        if sensor_name is not None and len(sensor_name) > 64:
            raise ValueError("Invalid value for `sensor_name`, length must be less than or equal to `64`")  # noqa: E501
        if sensor_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', sensor_name):  # noqa: E501
            raise ValueError(r"Invalid value for `sensor_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._sensor_name = sensor_name

    @property
    def where(self):
        """Gets the where of this RuleSchemaSensor.  # noqa: E501

        List of where clauses to filter ingest data  # noqa: E501

        :return: The where of this RuleSchemaSensor.  # noqa: E501
        :rtype: list[RuleSchemaWhere]
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this RuleSchemaSensor.

        List of where clauses to filter ingest data  # noqa: E501

        :param where: The where of this RuleSchemaSensor.  # noqa: E501
        :type: list[RuleSchemaWhere]
        """

        self._where = where

    @property
    def zero_suppression(self):
        """Gets the zero_suppression of this RuleSchemaSensor.  # noqa: E501

        Assign zero as default value for field in case of zero-suppression  # noqa: E501

        :return: The zero_suppression of this RuleSchemaSensor.  # noqa: E501
        :rtype: list[object]
        """
        return self._zero_suppression

    @zero_suppression.setter
    def zero_suppression(self, zero_suppression):
        """Sets the zero_suppression of this RuleSchemaSensor.

        Assign zero as default value for field in case of zero-suppression  # noqa: E501

        :param zero_suppression: The zero_suppression of this RuleSchemaSensor.  # noqa: E501
        :type: list[object]
        """

        self._zero_suppression = zero_suppression

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
        if issubclass(RuleSchemaSensor, dict):
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
        if not isinstance(other, RuleSchemaSensor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
