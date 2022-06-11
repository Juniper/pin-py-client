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


class ResourceSchemaForeverydevice(object):
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
        'across_all_device_groups': 'bool',
        'in_groups': 'list[str]',
        'label_as': 'str'
    }

    attribute_map = {
        'across_all_device_groups': 'across-all-device-groups',
        'in_groups': 'in-groups',
        'label_as': 'label-as'
    }

    def __init__(self, across_all_device_groups=None, in_groups=None, label_as=None):  # noqa: E501
        """ResourceSchemaForeverydevice - a model defined in Swagger"""  # noqa: E501

        self._across_all_device_groups = None
        self._in_groups = None
        self._label_as = None
        self.discriminator = None

        if across_all_device_groups is not None:
            self.across_all_device_groups = across_all_device_groups
        if in_groups is not None:
            self.in_groups = in_groups
        self.label_as = label_as

    @property
    def across_all_device_groups(self):
        """Gets the across_all_device_groups of this ResourceSchemaForeverydevice.  # noqa: E501

        evaluate for all device groups  # noqa: E501

        :return: The across_all_device_groups of this ResourceSchemaForeverydevice.  # noqa: E501
        :rtype: bool
        """
        return self._across_all_device_groups

    @across_all_device_groups.setter
    def across_all_device_groups(self, across_all_device_groups):
        """Sets the across_all_device_groups of this ResourceSchemaForeverydevice.

        evaluate for all device groups  # noqa: E501

        :param across_all_device_groups: The across_all_device_groups of this ResourceSchemaForeverydevice.  # noqa: E501
        :type: bool
        """

        self._across_all_device_groups = across_all_device_groups

    @property
    def in_groups(self):
        """Gets the in_groups of this ResourceSchemaForeverydevice.  # noqa: E501


        :return: The in_groups of this ResourceSchemaForeverydevice.  # noqa: E501
        :rtype: list[str]
        """
        return self._in_groups

    @in_groups.setter
    def in_groups(self, in_groups):
        """Sets the in_groups of this ResourceSchemaForeverydevice.


        :param in_groups: The in_groups of this ResourceSchemaForeverydevice.  # noqa: E501
        :type: list[str]
        """

        self._in_groups = in_groups

    @property
    def label_as(self):
        """Gets the label_as of this ResourceSchemaForeverydevice.  # noqa: E501


        :return: The label_as of this ResourceSchemaForeverydevice.  # noqa: E501
        :rtype: str
        """
        return self._label_as

    @label_as.setter
    def label_as(self, label_as):
        """Sets the label_as of this ResourceSchemaForeverydevice.


        :param label_as: The label_as of this ResourceSchemaForeverydevice.  # noqa: E501
        :type: str
        """
        if label_as is None:
            raise ValueError("Invalid value for `label_as`, must not be `None`")  # noqa: E501
        if label_as is not None and len(label_as) > 64:
            raise ValueError("Invalid value for `label_as`, length must be less than or equal to `64`")  # noqa: E501
        if label_as is not None and len(label_as) < 1:
            raise ValueError("Invalid value for `label_as`, length must be greater than or equal to `1`")  # noqa: E501
        if label_as is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9-]*$', label_as):  # noqa: E501
            raise ValueError(r"Invalid value for `label_as`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9-]*$/`")  # noqa: E501

        self._label_as = label_as

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
        if issubclass(ResourceSchemaForeverydevice, dict):
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
        if not isinstance(other, ResourceSchemaForeverydevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other