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


class RuleSchemaField(object):
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
        'constant': 'RuleSchemaConstant',
        'description': 'str',
        'field_name': 'str',
        'formula': 'RuleSchemaFormula',
        'reference': 'RuleSchemaReference',
        'sensor': 'list[RuleSchemaSensor]',
        'type': 'str'
    }

    attribute_map = {
        'constant': 'constant',
        'description': 'description',
        'field_name': 'field-name',
        'formula': 'formula',
        'reference': 'reference',
        'sensor': 'sensor',
        'type': 'type'
    }

    def __init__(self, constant=None, description=None, field_name=None, formula=None, reference=None, sensor=None, type=None):  # noqa: E501
        """RuleSchemaField - a model defined in Swagger"""  # noqa: E501

        self._constant = None
        self._description = None
        self._field_name = None
        self._formula = None
        self._reference = None
        self._sensor = None
        self._type = None
        self.discriminator = None

        if constant is not None:
            self.constant = constant
        if description is not None:
            self.description = description
        self.field_name = field_name
        if formula is not None:
            self.formula = formula
        if reference is not None:
            self.reference = reference
        if sensor is not None:
            self.sensor = sensor
        if type is not None:
            self.type = type

    @property
    def constant(self):
        """Gets the constant of this RuleSchemaField.  # noqa: E501


        :return: The constant of this RuleSchemaField.  # noqa: E501
        :rtype: RuleSchemaConstant
        """
        return self._constant

    @constant.setter
    def constant(self, constant):
        """Sets the constant of this RuleSchemaField.


        :param constant: The constant of this RuleSchemaField.  # noqa: E501
        :type: RuleSchemaConstant
        """

        self._constant = constant

    @property
    def description(self):
        """Gets the description of this RuleSchemaField.  # noqa: E501

        Description about this field  # noqa: E501

        :return: The description of this RuleSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleSchemaField.

        Description about this field  # noqa: E501

        :param description: The description of this RuleSchemaField.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def field_name(self):
        """Gets the field_name of this RuleSchemaField.  # noqa: E501

        Name of the field. Should be of pattern [a-z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The field_name of this RuleSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this RuleSchemaField.

        Name of the field. Should be of pattern [a-z][a-zA-Z0-9_-]*  # noqa: E501

        :param field_name: The field_name of this RuleSchemaField.  # noqa: E501
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501
        if field_name is not None and len(field_name) > 64:
            raise ValueError("Invalid value for `field_name`, length must be less than or equal to `64`")  # noqa: E501
        if field_name is not None and not re.search(r'^[a-z][a-zA-Z0-9_-]*$', field_name):  # noqa: E501
            raise ValueError(r"Invalid value for `field_name`, must be a follow pattern or equal to `/^[a-z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._field_name = field_name

    @property
    def formula(self):
        """Gets the formula of this RuleSchemaField.  # noqa: E501


        :return: The formula of this RuleSchemaField.  # noqa: E501
        :rtype: RuleSchemaFormula
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this RuleSchemaField.


        :param formula: The formula of this RuleSchemaField.  # noqa: E501
        :type: RuleSchemaFormula
        """

        self._formula = formula

    @property
    def reference(self):
        """Gets the reference of this RuleSchemaField.  # noqa: E501


        :return: The reference of this RuleSchemaField.  # noqa: E501
        :rtype: RuleSchemaReference
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this RuleSchemaField.


        :param reference: The reference of this RuleSchemaField.  # noqa: E501
        :type: RuleSchemaReference
        """

        self._reference = reference

    @property
    def sensor(self):
        """Gets the sensor of this RuleSchemaField.  # noqa: E501


        :return: The sensor of this RuleSchemaField.  # noqa: E501
        :rtype: list[RuleSchemaSensor]
        """
        return self._sensor

    @sensor.setter
    def sensor(self, sensor):
        """Sets the sensor of this RuleSchemaField.


        :param sensor: The sensor of this RuleSchemaField.  # noqa: E501
        :type: list[RuleSchemaSensor]
        """

        self._sensor = sensor

    @property
    def type(self):
        """Gets the type of this RuleSchemaField.  # noqa: E501


        :return: The type of this RuleSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleSchemaField.


        :param type: The type of this RuleSchemaField.  # noqa: E501
        :type: str
        """
        allowed_values = ["string", "integer", "unsigned-integer", "float"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(RuleSchemaField, dict):
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
        if not isinstance(other, RuleSchemaField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
