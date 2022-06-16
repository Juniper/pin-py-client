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


class RuleSchemaTrigger(object):
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
        'frequency': 'str',
        'synopsis': 'str',
        'disable_alarm_deduplication': 'list[object]',
        'term': 'list[RuleSchemaTerm]',
        'trigger_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'frequency': 'frequency',
        'synopsis': 'synopsis',
        'disable_alarm_deduplication': 'disable-alarm-deduplication',
        'term': 'term',
        'trigger_name': 'trigger-name'
    }

    def __init__(self, description=None, frequency=None, synopsis=None, disable_alarm_deduplication=None, term=None, trigger_name=None):  # noqa: E501
        """RuleSchemaTrigger - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._frequency = None
        self._synopsis = None
        self._disable_alarm_deduplication = None
        self._term = None
        self._trigger_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if frequency is not None:
            self.frequency = frequency
        if synopsis is not None:
            self.synopsis = synopsis
        if disable_alarm_deduplication is not None:
            self.disable_alarm_deduplication = disable_alarm_deduplication
        self.term = term
        self.trigger_name = trigger_name

    @property
    def description(self):
        """Gets the description of this RuleSchemaTrigger.  # noqa: E501

        Description about the trigger  # noqa: E501

        :return: The description of this RuleSchemaTrigger.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleSchemaTrigger.

        Description about the trigger  # noqa: E501

        :param description: The description of this RuleSchemaTrigger.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def frequency(self):
        """Gets the frequency of this RuleSchemaTrigger.  # noqa: E501

        Frequency or time interval at which the trigger needs to be evaluated. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :return: The frequency of this RuleSchemaTrigger.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this RuleSchemaTrigger.

        Frequency or time interval at which the trigger needs to be evaluated. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :param frequency: The frequency of this RuleSchemaTrigger.  # noqa: E501
        :type: str
        """
        if frequency is not None and not re.search(r'^[1-9][0-9]*(\\.[0-9]+)?(o|s|m|h|d|w|y|offset)$', frequency):  # noqa: E501
            raise ValueError(r"Invalid value for `frequency`, must be a follow pattern or equal to `/^[1-9][0-9]*(\\.[0-9]+)?(o|s|m|h|d|w|y|offset)$/`")  # noqa: E501

        self._frequency = frequency

    @property
    def synopsis(self):
        """Gets the synopsis of this RuleSchemaTrigger.  # noqa: E501

        Synopsis about the trigger  # noqa: E501

        :return: The synopsis of this RuleSchemaTrigger.  # noqa: E501
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """Sets the synopsis of this RuleSchemaTrigger.

        Synopsis about the trigger  # noqa: E501

        :param synopsis: The synopsis of this RuleSchemaTrigger.  # noqa: E501
        :type: str
        """

        self._synopsis = synopsis

    @property
    def disable_alarm_deduplication(self):
        """Gets the disable_alarm_deduplication of this RuleSchemaTrigger.  # noqa: E501

        Disable alarm deduplication, so that alarms are always generated  # noqa: E501

        :return: The disable_alarm_deduplication of this RuleSchemaTrigger.  # noqa: E501
        :rtype: list[object]
        """
        return self._disable_alarm_deduplication

    @disable_alarm_deduplication.setter
    def disable_alarm_deduplication(self, disable_alarm_deduplication):
        """Sets the disable_alarm_deduplication of this RuleSchemaTrigger.

        Disable alarm deduplication, so that alarms are always generated  # noqa: E501

        :param disable_alarm_deduplication: The disable_alarm_deduplication of this RuleSchemaTrigger.  # noqa: E501
        :type: list[object]
        """

        self._disable_alarm_deduplication = disable_alarm_deduplication

    @property
    def term(self):
        """Gets the term of this RuleSchemaTrigger.  # noqa: E501


        :return: The term of this RuleSchemaTrigger.  # noqa: E501
        :rtype: list[RuleSchemaTerm]
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this RuleSchemaTrigger.


        :param term: The term of this RuleSchemaTrigger.  # noqa: E501
        :type: list[RuleSchemaTerm]
        """
        if term is None:
            raise ValueError("Invalid value for `term`, must not be `None`")  # noqa: E501

        self._term = term

    @property
    def trigger_name(self):
        """Gets the trigger_name of this RuleSchemaTrigger.  # noqa: E501

        Trigger name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The trigger_name of this RuleSchemaTrigger.  # noqa: E501
        :rtype: str
        """
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, trigger_name):
        """Sets the trigger_name of this RuleSchemaTrigger.

        Trigger name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param trigger_name: The trigger_name of this RuleSchemaTrigger.  # noqa: E501
        :type: str
        """
        if trigger_name is None:
            raise ValueError("Invalid value for `trigger_name`, must not be `None`")  # noqa: E501
        if trigger_name is not None and len(trigger_name) > 64:
            raise ValueError("Invalid value for `trigger_name`, length must be less than or equal to `64`")  # noqa: E501
        if trigger_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', trigger_name):  # noqa: E501
            raise ValueError(r"Invalid value for `trigger_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._trigger_name = trigger_name

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
        if issubclass(RuleSchemaTrigger, dict):
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
        if not isinstance(other, RuleSchemaTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
