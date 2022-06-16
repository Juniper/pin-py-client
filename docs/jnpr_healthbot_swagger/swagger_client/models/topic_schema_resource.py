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


class TopicSchemaResource(object):
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
        'depends_on': 'list[TopicSchemaDependson]',
        'description': 'str',
        'field': 'list[TopicSchemaField]',
        'function': 'list[TopicSchemaFunction]',
        'keys': 'list[str]',
        'resource_name': 'str',
        'variable': 'list[TopicSchemaVariable]'
    }

    attribute_map = {
        'depends_on': 'depends-on',
        'description': 'description',
        'field': 'field',
        'function': 'function',
        'keys': 'keys',
        'resource_name': 'resource-name',
        'variable': 'variable'
    }

    def __init__(self, depends_on=None, description=None, field=None, function=None, keys=None, resource_name=None, variable=None):  # noqa: E501
        """TopicSchemaResource - a model defined in Swagger"""  # noqa: E501

        self._depends_on = None
        self._description = None
        self._field = None
        self._function = None
        self._keys = None
        self._resource_name = None
        self._variable = None
        self.discriminator = None

        if depends_on is not None:
            self.depends_on = depends_on
        if description is not None:
            self.description = description
        if field is not None:
            self.field = field
        if function is not None:
            self.function = function
        if keys is not None:
            self.keys = keys
        self.resource_name = resource_name
        if variable is not None:
            self.variable = variable

    @property
    def depends_on(self):
        """Gets the depends_on of this TopicSchemaResource.  # noqa: E501


        :return: The depends_on of this TopicSchemaResource.  # noqa: E501
        :rtype: list[TopicSchemaDependson]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """Sets the depends_on of this TopicSchemaResource.


        :param depends_on: The depends_on of this TopicSchemaResource.  # noqa: E501
        :type: list[TopicSchemaDependson]
        """

        self._depends_on = depends_on

    @property
    def description(self):
        """Gets the description of this TopicSchemaResource.  # noqa: E501

        Description about the resource  # noqa: E501

        :return: The description of this TopicSchemaResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TopicSchemaResource.

        Description about the resource  # noqa: E501

        :param description: The description of this TopicSchemaResource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def field(self):
        """Gets the field of this TopicSchemaResource.  # noqa: E501


        :return: The field of this TopicSchemaResource.  # noqa: E501
        :rtype: list[TopicSchemaField]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this TopicSchemaResource.


        :param field: The field of this TopicSchemaResource.  # noqa: E501
        :type: list[TopicSchemaField]
        """

        self._field = field

    @property
    def function(self):
        """Gets the function of this TopicSchemaResource.  # noqa: E501


        :return: The function of this TopicSchemaResource.  # noqa: E501
        :rtype: list[TopicSchemaFunction]
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this TopicSchemaResource.


        :param function: The function of this TopicSchemaResource.  # noqa: E501
        :type: list[TopicSchemaFunction]
        """

        self._function = function

    @property
    def keys(self):
        """Gets the keys of this TopicSchemaResource.  # noqa: E501


        :return: The keys of this TopicSchemaResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this TopicSchemaResource.


        :param keys: The keys of this TopicSchemaResource.  # noqa: E501
        :type: list[str]
        """

        self._keys = keys

    @property
    def resource_name(self):
        """Gets the resource_name of this TopicSchemaResource.  # noqa: E501

        Name of the resource. Should be of pattern [a-z][a-z0-9-]*  # noqa: E501

        :return: The resource_name of this TopicSchemaResource.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this TopicSchemaResource.

        Name of the resource. Should be of pattern [a-z][a-z0-9-]*  # noqa: E501

        :param resource_name: The resource_name of this TopicSchemaResource.  # noqa: E501
        :type: str
        """
        if resource_name is None:
            raise ValueError("Invalid value for `resource_name`, must not be `None`")  # noqa: E501
        if resource_name is not None and len(resource_name) > 64:
            raise ValueError("Invalid value for `resource_name`, length must be less than or equal to `64`")  # noqa: E501
        if resource_name is not None and len(resource_name) < 1:
            raise ValueError("Invalid value for `resource_name`, length must be greater than or equal to `1`")  # noqa: E501
        if resource_name is not None and not re.search(r'^[a-z][a-z0-9-]*$', resource_name):  # noqa: E501
            raise ValueError(r"Invalid value for `resource_name`, must be a follow pattern or equal to `/^[a-z][a-z0-9-]*$/`")  # noqa: E501

        self._resource_name = resource_name

    @property
    def variable(self):
        """Gets the variable of this TopicSchemaResource.  # noqa: E501

        Resource variable configuration  # noqa: E501

        :return: The variable of this TopicSchemaResource.  # noqa: E501
        :rtype: list[TopicSchemaVariable]
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this TopicSchemaResource.

        Resource variable configuration  # noqa: E501

        :param variable: The variable of this TopicSchemaResource.  # noqa: E501
        :type: list[TopicSchemaVariable]
        """

        self._variable = variable

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
        if issubclass(TopicSchemaResource, dict):
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
        if not isinstance(other, TopicSchemaResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
