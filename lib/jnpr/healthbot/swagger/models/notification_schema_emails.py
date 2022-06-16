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


class NotificationSchemaEmails(object):
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
        'ids': 'list[str]',
        'filter': 'NotificationSchemaEmailsFilter'
    }

    attribute_map = {
        'ids': 'ids',
        'filter': 'filter'
    }

    def __init__(self, ids=None, filter=None):  # noqa: E501
        """NotificationSchemaEmails - a model defined in Swagger"""  # noqa: E501

        self._ids = None
        self._filter = None
        self.discriminator = None

        self.ids = ids
        if filter is not None:
            self.filter = filter

    @property
    def ids(self):
        """Gets the ids of this NotificationSchemaEmails.  # noqa: E501


        :return: The ids of this NotificationSchemaEmails.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this NotificationSchemaEmails.


        :param ids: The ids of this NotificationSchemaEmails.  # noqa: E501
        :type: list[str]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

    @property
    def filter(self):
        """Gets the filter of this NotificationSchemaEmails.  # noqa: E501


        :return: The filter of this NotificationSchemaEmails.  # noqa: E501
        :rtype: NotificationSchemaEmailsFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this NotificationSchemaEmails.


        :param filter: The filter of this NotificationSchemaEmails.  # noqa: E501
        :type: NotificationSchemaEmailsFilter
        """

        self._filter = filter

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
        if issubclass(NotificationSchemaEmails, dict):
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
        if not isinstance(other, NotificationSchemaEmails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
