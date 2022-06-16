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


class PlaybookSchema(object):
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
        'playbook_name': 'str',
        'rules': 'list[str]',
        'synopsis': 'str',
        'classification': 'str'
    }

    attribute_map = {
        'description': 'description',
        'playbook_name': 'playbook-name',
        'rules': 'rules',
        'synopsis': 'synopsis',
        'classification': 'classification'
    }

    def __init__(self, description=None, playbook_name=None, rules=None, synopsis=None, classification=None):  # noqa: E501
        """PlaybookSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._playbook_name = None
        self._rules = None
        self._synopsis = None
        self._classification = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.playbook_name = playbook_name
        if rules is not None:
            self.rules = rules
        if synopsis is not None:
            self.synopsis = synopsis
        if classification is not None:
            self.classification = classification

    @property
    def description(self):
        """Gets the description of this PlaybookSchema.  # noqa: E501

        Description about this playbook  # noqa: E501

        :return: The description of this PlaybookSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PlaybookSchema.

        Description about this playbook  # noqa: E501

        :param description: The description of this PlaybookSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def playbook_name(self):
        """Gets the playbook_name of this PlaybookSchema.  # noqa: E501

        Name of the playbook. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The playbook_name of this PlaybookSchema.  # noqa: E501
        :rtype: str
        """
        return self._playbook_name

    @playbook_name.setter
    def playbook_name(self, playbook_name):
        """Sets the playbook_name of this PlaybookSchema.

        Name of the playbook. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param playbook_name: The playbook_name of this PlaybookSchema.  # noqa: E501
        :type: str
        """
        if playbook_name is None:
            raise ValueError("Invalid value for `playbook_name`, must not be `None`")  # noqa: E501
        if playbook_name is not None and len(playbook_name) > 64:
            raise ValueError("Invalid value for `playbook_name`, length must be less than or equal to `64`")  # noqa: E501
        if playbook_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', playbook_name):  # noqa: E501
            raise ValueError(r"Invalid value for `playbook_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._playbook_name = playbook_name

    @property
    def rules(self):
        """Gets the rules of this PlaybookSchema.  # noqa: E501


        :return: The rules of this PlaybookSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this PlaybookSchema.


        :param rules: The rules of this PlaybookSchema.  # noqa: E501
        :type: list[str]
        """

        self._rules = rules

    @property
    def synopsis(self):
        """Gets the synopsis of this PlaybookSchema.  # noqa: E501

        Short description about this playbook  # noqa: E501

        :return: The synopsis of this PlaybookSchema.  # noqa: E501
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """Sets the synopsis of this PlaybookSchema.

        Short description about this playbook  # noqa: E501

        :param synopsis: The synopsis of this PlaybookSchema.  # noqa: E501
        :type: str
        """

        self._synopsis = synopsis

    @property
    def classification(self):
        """Gets the classification of this PlaybookSchema.  # noqa: E501

        Classification info for this playbook  # noqa: E501

        :return: The classification of this PlaybookSchema.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this PlaybookSchema.

        Classification info for this playbook  # noqa: E501

        :param classification: The classification of this PlaybookSchema.  # noqa: E501
        :type: str
        """

        self._classification = classification

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
        if issubclass(PlaybookSchema, dict):
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
        if not isinstance(other, PlaybookSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
