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


class DeviceSchemaVendorPaloalto(object):
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
        'operating_system': 'str',
        'platform': 'str',
        'product': 'str',
        'release': 'str'
    }

    attribute_map = {
        'operating_system': 'operating-system',
        'platform': 'platform',
        'product': 'product',
        'release': 'release'
    }

    def __init__(self, operating_system=None, platform=None, product=None, release=None):  # noqa: E501
        """DeviceSchemaVendorPaloalto - a model defined in Swagger"""  # noqa: E501

        self._operating_system = None
        self._platform = None
        self._product = None
        self._release = None
        self.discriminator = None

        self.operating_system = operating_system
        if platform is not None:
            self.platform = platform
        if product is not None:
            self.product = product
        if release is not None:
            self.release = release

    @property
    def operating_system(self):
        """Gets the operating_system of this DeviceSchemaVendorPaloalto.  # noqa: E501

        Operating system of the device  # noqa: E501

        :return: The operating_system of this DeviceSchemaVendorPaloalto.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this DeviceSchemaVendorPaloalto.

        Operating system of the device  # noqa: E501

        :param operating_system: The operating_system of this DeviceSchemaVendorPaloalto.  # noqa: E501
        :type: str
        """
        if operating_system is None:
            raise ValueError("Invalid value for `operating_system`, must not be `None`")  # noqa: E501
        allowed_values = ["panos"]  # noqa: E501
        if operating_system not in allowed_values:
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

    @property
    def platform(self):
        """Gets the platform of this DeviceSchemaVendorPaloalto.  # noqa: E501

        Platform name of the device, Example: MX240  # noqa: E501

        :return: The platform of this DeviceSchemaVendorPaloalto.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this DeviceSchemaVendorPaloalto.

        Platform name of the device, Example: MX240  # noqa: E501

        :param platform: The platform of this DeviceSchemaVendorPaloalto.  # noqa: E501
        :type: str
        """
        if platform is not None and len(platform) > 64:
            raise ValueError("Invalid value for `platform`, length must be less than or equal to `64`")  # noqa: E501
        if platform is not None and len(platform) < 1:
            raise ValueError("Invalid value for `platform`, length must be greater than or equal to `1`")  # noqa: E501

        self._platform = platform

    @property
    def product(self):
        """Gets the product of this DeviceSchemaVendorPaloalto.  # noqa: E501

        Product category of the device, Example: MX  # noqa: E501

        :return: The product of this DeviceSchemaVendorPaloalto.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this DeviceSchemaVendorPaloalto.

        Product category of the device, Example: MX  # noqa: E501

        :param product: The product of this DeviceSchemaVendorPaloalto.  # noqa: E501
        :type: str
        """
        if product is not None and len(product) > 64:
            raise ValueError("Invalid value for `product`, length must be less than or equal to `64`")  # noqa: E501
        if product is not None and len(product) < 1:
            raise ValueError("Invalid value for `product`, length must be greater than or equal to `1`")  # noqa: E501

        self._product = product

    @property
    def release(self):
        """Gets the release of this DeviceSchemaVendorPaloalto.  # noqa: E501

        Release string of the device, Example: 19.2R1  # noqa: E501

        :return: The release of this DeviceSchemaVendorPaloalto.  # noqa: E501
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this DeviceSchemaVendorPaloalto.

        Release string of the device, Example: 19.2R1  # noqa: E501

        :param release: The release of this DeviceSchemaVendorPaloalto.  # noqa: E501
        :type: str
        """
        if release is not None and len(release) > 64:
            raise ValueError("Invalid value for `release`, length must be less than or equal to `64`")  # noqa: E501
        if release is not None and len(release) < 1:
            raise ValueError("Invalid value for `release`, length must be greater than or equal to `1`")  # noqa: E501

        self._release = release

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
        if issubclass(DeviceSchemaVendorPaloalto, dict):
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
        if not isinstance(other, DeviceSchemaVendorPaloalto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
