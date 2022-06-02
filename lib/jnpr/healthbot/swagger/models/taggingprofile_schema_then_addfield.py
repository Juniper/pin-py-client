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


class TaggingprofileSchemaThenAddfield(object):
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
        'name': 'str',
        'type': 'str',
        'value': 'str',
        'in_memory': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'value': 'value',
        'in_memory': 'in-memory'
    }

    def __init__(self, name=None, type=None, value=None, in_memory=None):  # noqa: E501
        """TaggingprofileSchemaThenAddfield - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._value = None
        self._in_memory = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        self.value = value
        if in_memory is not None:
            self.in_memory = in_memory

    @property
    def name(self):
        """Gets the name of this TaggingprofileSchemaThenAddfield.  # noqa: E501

        Tagged field name  # noqa: E501

        :return: The name of this TaggingprofileSchemaThenAddfield.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaggingprofileSchemaThenAddfield.

        Tagged field name  # noqa: E501

        :param name: The name of this TaggingprofileSchemaThenAddfield.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search(r'^[a-z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this TaggingprofileSchemaThenAddfield.  # noqa: E501


        :return: The type of this TaggingprofileSchemaThenAddfield.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaggingprofileSchemaThenAddfield.


        :param type: The type of this TaggingprofileSchemaThenAddfield.  # noqa: E501
        :type: str
        """
        allowed_values = ["string", "integer", "unsigned-integer", "float"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this TaggingprofileSchemaThenAddfield.  # noqa: E501

        Tagged value  # noqa: E501

        :return: The value of this TaggingprofileSchemaThenAddfield.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TaggingprofileSchemaThenAddfield.

        Tagged value  # noqa: E501

        :param value: The value of this TaggingprofileSchemaThenAddfield.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def in_memory(self):
        """Gets the in_memory of this TaggingprofileSchemaThenAddfield.  # noqa: E501

        Look for value in internal cache  # noqa: E501

        :return: The in_memory of this TaggingprofileSchemaThenAddfield.  # noqa: E501
        :rtype: bool
        """
        return self._in_memory

    @in_memory.setter
    def in_memory(self, in_memory):
        """Sets the in_memory of this TaggingprofileSchemaThenAddfield.

        Look for value in internal cache  # noqa: E501

        :param in_memory: The in_memory of this TaggingprofileSchemaThenAddfield.  # noqa: E501
        :type: bool
        """

        self._in_memory = in_memory

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
        if issubclass(TaggingprofileSchemaThenAddfield, dict):
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
        if not isinstance(other, TaggingprofileSchemaThenAddfield):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
