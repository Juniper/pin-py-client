# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IngestsettingsSchemaIngestsettingsByoiDefaultplugin(object):
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
        'tlive_kafka_oc': 'list[TliveKafkaOcSchema]'
    }

    attribute_map = {
        'tlive_kafka_oc': 'tlive-kafka-oc'
    }

    def __init__(self, tlive_kafka_oc=None):  # noqa: E501
        """IngestsettingsSchemaIngestsettingsByoiDefaultplugin - a model defined in Swagger"""  # noqa: E501

        self._tlive_kafka_oc = None
        self.discriminator = None

        if tlive_kafka_oc is not None:
            self.tlive_kafka_oc = tlive_kafka_oc

    @property
    def tlive_kafka_oc(self):
        """Gets the tlive_kafka_oc of this IngestsettingsSchemaIngestsettingsByoiDefaultplugin.  # noqa: E501

        TLive Kafka ingest  # noqa: E501

        :return: The tlive_kafka_oc of this IngestsettingsSchemaIngestsettingsByoiDefaultplugin.  # noqa: E501
        :rtype: list[TliveKafkaOcSchema]
        """
        return self._tlive_kafka_oc

    @tlive_kafka_oc.setter
    def tlive_kafka_oc(self, tlive_kafka_oc):
        """Sets the tlive_kafka_oc of this IngestsettingsSchemaIngestsettingsByoiDefaultplugin.

        TLive Kafka ingest  # noqa: E501

        :param tlive_kafka_oc: The tlive_kafka_oc of this IngestsettingsSchemaIngestsettingsByoiDefaultplugin.  # noqa: E501
        :type: list[TliveKafkaOcSchema]
        """

        self._tlive_kafka_oc = tlive_kafka_oc

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
        if issubclass(IngestsettingsSchemaIngestsettingsByoiDefaultplugin, dict):
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
        if not isinstance(other, IngestsettingsSchemaIngestsettingsByoiDefaultplugin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
