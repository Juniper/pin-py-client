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


class RuleSchemaRulepropertiesHelperfiles(object):
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
        'file_type': 'str',
        'list_of_files': 'list[str]'
    }

    attribute_map = {
        'file_type': 'file-type',
        'list_of_files': 'list-of-files'
    }

    def __init__(self, file_type=None, list_of_files=None):  # noqa: E501
        """RuleSchemaRulepropertiesHelperfiles - a model defined in Swagger"""  # noqa: E501

        self._file_type = None
        self._list_of_files = None
        self.discriminator = None

        self.file_type = file_type
        self.list_of_files = list_of_files

    @property
    def file_type(self):
        """Gets the file_type of this RuleSchemaRulepropertiesHelperfiles.  # noqa: E501


        :return: The file_type of this RuleSchemaRulepropertiesHelperfiles.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this RuleSchemaRulepropertiesHelperfiles.


        :param file_type: The file_type of this RuleSchemaRulepropertiesHelperfiles.  # noqa: E501
        :type: str
        """
        if file_type is None:
            raise ValueError("Invalid value for `file_type`, must not be `None`")  # noqa: E501
        allowed_values = ["schema", "mib", "other"]  # noqa: E501
        if file_type not in allowed_values:
            raise ValueError(
                "Invalid value for `file_type` ({0}), must be one of {1}"  # noqa: E501
                .format(file_type, allowed_values)
            )

        self._file_type = file_type

    @property
    def list_of_files(self):
        """Gets the list_of_files of this RuleSchemaRulepropertiesHelperfiles.  # noqa: E501


        :return: The list_of_files of this RuleSchemaRulepropertiesHelperfiles.  # noqa: E501
        :rtype: list[str]
        """
        return self._list_of_files

    @list_of_files.setter
    def list_of_files(self, list_of_files):
        """Sets the list_of_files of this RuleSchemaRulepropertiesHelperfiles.


        :param list_of_files: The list_of_files of this RuleSchemaRulepropertiesHelperfiles.  # noqa: E501
        :type: list[str]
        """
        if list_of_files is None:
            raise ValueError("Invalid value for `list_of_files`, must not be `None`")  # noqa: E501

        self._list_of_files = list_of_files

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
        if issubclass(RuleSchemaRulepropertiesHelperfiles, dict):
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
        if not isinstance(other, RuleSchemaRulepropertiesHelperfiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
