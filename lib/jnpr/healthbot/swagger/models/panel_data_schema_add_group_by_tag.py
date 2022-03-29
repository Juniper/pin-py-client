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


class PanelDataSchemaAddGroupByTag(object):
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
        'data_type': 'str',
        'label': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'data_type': 'dataType',
        'label': 'label',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, data_type=None, label=None, type=None, value=None):  # noqa: E501
        """PanelDataSchemaAddGroupByTag - a model defined in Swagger"""  # noqa: E501

        self._data_type = None
        self._label = None
        self._type = None
        self._value = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def data_type(self):
        """Gets the data_type of this PanelDataSchemaAddGroupByTag.  # noqa: E501

        Data type of the tag  # noqa: E501

        :return: The data_type of this PanelDataSchemaAddGroupByTag.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this PanelDataSchemaAddGroupByTag.

        Data type of the tag  # noqa: E501

        :param data_type: The data_type of this PanelDataSchemaAddGroupByTag.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def label(self):
        """Gets the label of this PanelDataSchemaAddGroupByTag.  # noqa: E501

        label name  # noqa: E501

        :return: The label of this PanelDataSchemaAddGroupByTag.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PanelDataSchemaAddGroupByTag.

        label name  # noqa: E501

        :param label: The label of this PanelDataSchemaAddGroupByTag.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this PanelDataSchemaAddGroupByTag.  # noqa: E501

        key type or field type  # noqa: E501

        :return: The type of this PanelDataSchemaAddGroupByTag.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PanelDataSchemaAddGroupByTag.

        key type or field type  # noqa: E501

        :param type: The type of this PanelDataSchemaAddGroupByTag.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this PanelDataSchemaAddGroupByTag.  # noqa: E501

        Value of label  # noqa: E501

        :return: The value of this PanelDataSchemaAddGroupByTag.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PanelDataSchemaAddGroupByTag.

        Value of label  # noqa: E501

        :param value: The value of this PanelDataSchemaAddGroupByTag.  # noqa: E501
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
        if issubclass(PanelDataSchemaAddGroupByTag, dict):
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
        if not isinstance(other, PanelDataSchemaAddGroupByTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other