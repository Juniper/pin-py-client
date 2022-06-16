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


class RollupsummarizationSchemaMeasurement(object):
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
        'apply_on_existing_data': 'list[ERRORUNKNOWN]',
        'field': 'list[RollupsummarizationSchemaField1]',
        'measurement_name': 'str'
    }

    attribute_map = {
        'apply_on_existing_data': 'apply-on-existing-data',
        'field': 'field',
        'measurement_name': 'measurement-name'
    }

    def __init__(self, apply_on_existing_data=None, field=None, measurement_name=None):  # noqa: E501
        """RollupsummarizationSchemaMeasurement - a model defined in Swagger"""  # noqa: E501

        self._apply_on_existing_data = None
        self._field = None
        self._measurement_name = None
        self.discriminator = None

        if apply_on_existing_data is not None:
            self.apply_on_existing_data = apply_on_existing_data
        if field is not None:
            self.field = field
        self.measurement_name = measurement_name

    @property
    def apply_on_existing_data(self):
        """Gets the apply_on_existing_data of this RollupsummarizationSchemaMeasurement.  # noqa: E501

        If configured, existing data will also be considered for roll up summarization, else only the newly incoming data will be considered  # noqa: E501

        :return: The apply_on_existing_data of this RollupsummarizationSchemaMeasurement.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._apply_on_existing_data

    @apply_on_existing_data.setter
    def apply_on_existing_data(self, apply_on_existing_data):
        """Sets the apply_on_existing_data of this RollupsummarizationSchemaMeasurement.

        If configured, existing data will also be considered for roll up summarization, else only the newly incoming data will be considered  # noqa: E501

        :param apply_on_existing_data: The apply_on_existing_data of this RollupsummarizationSchemaMeasurement.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._apply_on_existing_data = apply_on_existing_data

    @property
    def field(self):
        """Gets the field of this RollupsummarizationSchemaMeasurement.  # noqa: E501


        :return: The field of this RollupsummarizationSchemaMeasurement.  # noqa: E501
        :rtype: list[RollupsummarizationSchemaField1]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this RollupsummarizationSchemaMeasurement.


        :param field: The field of this RollupsummarizationSchemaMeasurement.  # noqa: E501
        :type: list[RollupsummarizationSchemaField1]
        """

        self._field = field

    @property
    def measurement_name(self):
        """Gets the measurement_name of this RollupsummarizationSchemaMeasurement.  # noqa: E501

        Measurement of the database for which the roll-up summarization profile will be applied.  # noqa: E501

        :return: The measurement_name of this RollupsummarizationSchemaMeasurement.  # noqa: E501
        :rtype: str
        """
        return self._measurement_name

    @measurement_name.setter
    def measurement_name(self, measurement_name):
        """Sets the measurement_name of this RollupsummarizationSchemaMeasurement.

        Measurement of the database for which the roll-up summarization profile will be applied.  # noqa: E501

        :param measurement_name: The measurement_name of this RollupsummarizationSchemaMeasurement.  # noqa: E501
        :type: str
        """
        if measurement_name is None:
            raise ValueError("Invalid value for `measurement_name`, must not be `None`")  # noqa: E501

        self._measurement_name = measurement_name

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
        if issubclass(RollupsummarizationSchemaMeasurement, dict):
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
        if not isinstance(other, RollupsummarizationSchemaMeasurement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
