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


class DeviceSchemaSnmp(object):
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
        'port': 'int',
        'v2': 'DeviceSchemaSnmpV2',
        'v3': 'DeviceSchemaSnmpV3'
    }

    attribute_map = {
        'port': 'port',
        'v2': 'v2',
        'v3': 'v3'
    }

    def __init__(self, port=None, v2=None, v3=None):  # noqa: E501
        """DeviceSchemaSnmp - a model defined in Swagger"""  # noqa: E501

        self._port = None
        self._v2 = None
        self._v3 = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if v2 is not None:
            self.v2 = v2
        if v3 is not None:
            self.v3 = v3

    @property
    def port(self):
        """Gets the port of this DeviceSchemaSnmp.  # noqa: E501

        Port on which SNMP requests need to be sent. Port 161 is used if not configured.  # noqa: E501

        :return: The port of this DeviceSchemaSnmp.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DeviceSchemaSnmp.

        Port on which SNMP requests need to be sent. Port 161 is used if not configured.  # noqa: E501

        :param port: The port of this DeviceSchemaSnmp.  # noqa: E501
        :type: int
        """
        if port is not None and port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if port is not None and port < 1:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

    @property
    def v2(self):
        """Gets the v2 of this DeviceSchemaSnmp.  # noqa: E501


        :return: The v2 of this DeviceSchemaSnmp.  # noqa: E501
        :rtype: DeviceSchemaSnmpV2
        """
        return self._v2

    @v2.setter
    def v2(self, v2):
        """Sets the v2 of this DeviceSchemaSnmp.


        :param v2: The v2 of this DeviceSchemaSnmp.  # noqa: E501
        :type: DeviceSchemaSnmpV2
        """

        self._v2 = v2

    @property
    def v3(self):
        """Gets the v3 of this DeviceSchemaSnmp.  # noqa: E501


        :return: The v3 of this DeviceSchemaSnmp.  # noqa: E501
        :rtype: DeviceSchemaSnmpV3
        """
        return self._v3

    @v3.setter
    def v3(self, v3):
        """Sets the v3 of this DeviceSchemaSnmp.


        :param v3: The v3 of this DeviceSchemaSnmp.  # noqa: E501
        :type: DeviceSchemaSnmpV3
        """

        self._v3 = v3

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
        if issubclass(DeviceSchemaSnmp, dict):
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
        if not isinstance(other, DeviceSchemaSnmp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
