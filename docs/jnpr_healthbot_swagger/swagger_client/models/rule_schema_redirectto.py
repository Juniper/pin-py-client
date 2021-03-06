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


class RuleSchemaRedirectto(object):
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
        'mandatory_fields': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'mandatory_fields': 'mandatory-fields',
        'name': 'name'
    }

    def __init__(self, mandatory_fields=None, name=None):  # noqa: E501
        """RuleSchemaRedirectto - a model defined in Swagger"""  # noqa: E501

        self._mandatory_fields = None
        self._name = None
        self.discriminator = None

        if mandatory_fields is not None:
            self.mandatory_fields = mandatory_fields
        self.name = name

    @property
    def mandatory_fields(self):
        """Gets the mandatory_fields of this RuleSchemaRedirectto.  # noqa: E501


        :return: The mandatory_fields of this RuleSchemaRedirectto.  # noqa: E501
        :rtype: list[str]
        """
        return self._mandatory_fields

    @mandatory_fields.setter
    def mandatory_fields(self, mandatory_fields):
        """Sets the mandatory_fields of this RuleSchemaRedirectto.


        :param mandatory_fields: The mandatory_fields of this RuleSchemaRedirectto.  # noqa: E501
        :type: list[str]
        """

        self._mandatory_fields = mandatory_fields

    @property
    def name(self):
        """Gets the name of this RuleSchemaRedirectto.  # noqa: E501

        Measurement name for redirecting rule data. Format: <topic-name>/<rule-name>. Should be of pattern [a-z][a-z-]*(\\.{1}[a-z0-9-]+)*/[a-z][a-z0-9_-]*  # noqa: E501

        :return: The name of this RuleSchemaRedirectto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleSchemaRedirectto.

        Measurement name for redirecting rule data. Format: <topic-name>/<rule-name>. Should be of pattern [a-z][a-z-]*(\\.{1}[a-z0-9-]+)*/[a-z][a-z0-9_-]*  # noqa: E501

        :param name: The name of this RuleSchemaRedirectto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 129:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `129`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search(r'^[a-z][a-z-]*(\\.{1}[a-z0-9-]+)*\/[a-z][a-z0-9_-]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-z][a-z-]*(\\.{1}[a-z0-9-]+)*\/[a-z][a-z0-9_-]*$/`")  # noqa: E501

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
        if issubclass(RuleSchemaRedirectto, dict):
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
        if not isinstance(other, RuleSchemaRedirectto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
