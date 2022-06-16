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


class DeviceSchemaOpenconfig(object):
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
        'initial_sync': 'bool',
        'gnmi': 'DevicegroupSchemaOpenconfigGnmi',
        'port': 'int'
    }

    attribute_map = {
        'initial_sync': 'initial-sync',
        'gnmi': 'gnmi',
        'port': 'port'
    }

    def __init__(self, initial_sync=None, gnmi=None, port=None):  # noqa: E501
        """DeviceSchemaOpenconfig - a model defined in Swagger"""  # noqa: E501

        self._initial_sync = None
        self._gnmi = None
        self._port = None
        self.discriminator = None

        if initial_sync is not None:
            self.initial_sync = initial_sync
        if gnmi is not None:
            self.gnmi = gnmi
        self.port = port

    @property
    def initial_sync(self):
        """Gets the initial_sync of this DeviceSchemaOpenconfig.  # noqa: E501

        If true, enable initial sync packets processing  # noqa: E501

        :return: The initial_sync of this DeviceSchemaOpenconfig.  # noqa: E501
        :rtype: bool
        """
        return self._initial_sync

    @initial_sync.setter
    def initial_sync(self, initial_sync):
        """Sets the initial_sync of this DeviceSchemaOpenconfig.

        If true, enable initial sync packets processing  # noqa: E501

        :param initial_sync: The initial_sync of this DeviceSchemaOpenconfig.  # noqa: E501
        :type: bool
        """

        self._initial_sync = initial_sync

    @property
    def gnmi(self):
        """Gets the gnmi of this DeviceSchemaOpenconfig.  # noqa: E501


        :return: The gnmi of this DeviceSchemaOpenconfig.  # noqa: E501
        :rtype: DevicegroupSchemaOpenconfigGnmi
        """
        return self._gnmi

    @gnmi.setter
    def gnmi(self, gnmi):
        """Sets the gnmi of this DeviceSchemaOpenconfig.


        :param gnmi: The gnmi of this DeviceSchemaOpenconfig.  # noqa: E501
        :type: DevicegroupSchemaOpenconfigGnmi
        """

        self._gnmi = gnmi

    @property
    def port(self):
        """Gets the port of this DeviceSchemaOpenconfig.  # noqa: E501

        Port on which gRPC connection needs to be established  # noqa: E501

        :return: The port of this DeviceSchemaOpenconfig.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DeviceSchemaOpenconfig.

        Port on which gRPC connection needs to be established  # noqa: E501

        :param port: The port of this DeviceSchemaOpenconfig.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501
        if port is not None and port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if port is not None and port < 1:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

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
        if issubclass(DeviceSchemaOpenconfig, dict):
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
        if not isinstance(other, DeviceSchemaOpenconfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
