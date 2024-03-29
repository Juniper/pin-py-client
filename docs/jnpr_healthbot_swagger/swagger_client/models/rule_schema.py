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


class RuleSchema(object):
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
        'field': 'list[RuleSchemaField]',
        'function': 'list[RuleSchemaFunction]',
        'keys': 'list[str]',
        'network_rule': 'list[object]',
        'disable_no_data_alarm': 'list[object]',
        'pre_hook': 'list[RuleSchemaPrehook]',
        'post_hook': 'list[RuleSchemaPrehook]',
        'redirect_to': 'RuleSchemaRedirectto',
        'rule_frequency': 'str',
        'rule_name': 'str',
        'sensor': 'list[RuleSchemaSensor1]',
        'synopsis': 'str',
        'field_aggregation_time_range': 'str',
        'trigger': 'list[RuleSchemaTrigger]',
        'variable': 'list[RuleSchemaVariable]',
        'vector': 'list[RuleSchemaVector]',
        'rule_properties': 'RuleSchemaRuleproperties'
    }

    attribute_map = {
        'description': 'description',
        'field': 'field',
        'function': 'function',
        'keys': 'keys',
        'network_rule': 'network-rule',
        'disable_no_data_alarm': 'disable-no-data-alarm',
        'pre_hook': 'pre-hook',
        'post_hook': 'post-hook',
        'redirect_to': 'redirect-to',
        'rule_frequency': 'rule-frequency',
        'rule_name': 'rule-name',
        'sensor': 'sensor',
        'synopsis': 'synopsis',
        'field_aggregation_time_range': 'field-aggregation-time-range',
        'trigger': 'trigger',
        'variable': 'variable',
        'vector': 'vector',
        'rule_properties': 'rule-properties'
    }

    def __init__(self, description=None, field=None, function=None, keys=None, network_rule=None, disable_no_data_alarm=None, pre_hook=None, post_hook=None, redirect_to=None, rule_frequency=None, rule_name=None, sensor=None, synopsis=None, field_aggregation_time_range=None, trigger=None, variable=None, vector=None, rule_properties=None):  # noqa: E501
        """RuleSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._field = None
        self._function = None
        self._keys = None
        self._network_rule = None
        self._disable_no_data_alarm = None
        self._pre_hook = None
        self._post_hook = None
        self._redirect_to = None
        self._rule_frequency = None
        self._rule_name = None
        self._sensor = None
        self._synopsis = None
        self._field_aggregation_time_range = None
        self._trigger = None
        self._variable = None
        self._vector = None
        self._rule_properties = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if field is not None:
            self.field = field
        if function is not None:
            self.function = function
        if keys is not None:
            self.keys = keys
        if network_rule is not None:
            self.network_rule = network_rule
        if disable_no_data_alarm is not None:
            self.disable_no_data_alarm = disable_no_data_alarm
        if pre_hook is not None:
            self.pre_hook = pre_hook
        if post_hook is not None:
            self.post_hook = post_hook
        if redirect_to is not None:
            self.redirect_to = redirect_to
        if rule_frequency is not None:
            self.rule_frequency = rule_frequency
        self.rule_name = rule_name
        if sensor is not None:
            self.sensor = sensor
        if synopsis is not None:
            self.synopsis = synopsis
        if field_aggregation_time_range is not None:
            self.field_aggregation_time_range = field_aggregation_time_range
        if trigger is not None:
            self.trigger = trigger
        if variable is not None:
            self.variable = variable
        if vector is not None:
            self.vector = vector
        if rule_properties is not None:
            self.rule_properties = rule_properties

    @property
    def description(self):
        """Gets the description of this RuleSchema.  # noqa: E501

        Description about the rule  # noqa: E501

        :return: The description of this RuleSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleSchema.

        Description about the rule  # noqa: E501

        :param description: The description of this RuleSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def field(self):
        """Gets the field of this RuleSchema.  # noqa: E501


        :return: The field of this RuleSchema.  # noqa: E501
        :rtype: list[RuleSchemaField]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this RuleSchema.


        :param field: The field of this RuleSchema.  # noqa: E501
        :type: list[RuleSchemaField]
        """

        self._field = field

    @property
    def function(self):
        """Gets the function of this RuleSchema.  # noqa: E501


        :return: The function of this RuleSchema.  # noqa: E501
        :rtype: list[RuleSchemaFunction]
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this RuleSchema.


        :param function: The function of this RuleSchema.  # noqa: E501
        :type: list[RuleSchemaFunction]
        """

        self._function = function

    @property
    def keys(self):
        """Gets the keys of this RuleSchema.  # noqa: E501


        :return: The keys of this RuleSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this RuleSchema.


        :param keys: The keys of this RuleSchema.  # noqa: E501
        :type: list[str]
        """

        self._keys = keys

    @property
    def network_rule(self):
        """Gets the network_rule of this RuleSchema.  # noqa: E501

        Flag to denote a network rule  # noqa: E501

        :return: The network_rule of this RuleSchema.  # noqa: E501
        :rtype: list[object]
        """
        return self._network_rule

    @network_rule.setter
    def network_rule(self, network_rule):
        """Sets the network_rule of this RuleSchema.

        Flag to denote a network rule  # noqa: E501

        :param network_rule: The network_rule of this RuleSchema.  # noqa: E501
        :type: list[object]
        """

        self._network_rule = network_rule

    @property
    def disable_no_data_alarm(self):
        """Gets the disable_no_data_alarm of this RuleSchema.  # noqa: E501

        Disable No Data Alarm  # noqa: E501

        :return: The disable_no_data_alarm of this RuleSchema.  # noqa: E501
        :rtype: list[object]
        """
        return self._disable_no_data_alarm

    @disable_no_data_alarm.setter
    def disable_no_data_alarm(self, disable_no_data_alarm):
        """Sets the disable_no_data_alarm of this RuleSchema.

        Disable No Data Alarm  # noqa: E501

        :param disable_no_data_alarm: The disable_no_data_alarm of this RuleSchema.  # noqa: E501
        :type: list[object]
        """

        self._disable_no_data_alarm = disable_no_data_alarm

    @property
    def pre_hook(self):
        """Gets the pre_hook of this RuleSchema.  # noqa: E501

        List of pre hook workflows per rule  # noqa: E501

        :return: The pre_hook of this RuleSchema.  # noqa: E501
        :rtype: list[RuleSchemaPrehook]
        """
        return self._pre_hook

    @pre_hook.setter
    def pre_hook(self, pre_hook):
        """Sets the pre_hook of this RuleSchema.

        List of pre hook workflows per rule  # noqa: E501

        :param pre_hook: The pre_hook of this RuleSchema.  # noqa: E501
        :type: list[RuleSchemaPrehook]
        """

        self._pre_hook = pre_hook

    @property
    def post_hook(self):
        """Gets the post_hook of this RuleSchema.  # noqa: E501

        List of post hook workflows per rule  # noqa: E501

        :return: The post_hook of this RuleSchema.  # noqa: E501
        :rtype: list[RuleSchemaPrehook]
        """
        return self._post_hook

    @post_hook.setter
    def post_hook(self, post_hook):
        """Sets the post_hook of this RuleSchema.

        List of post hook workflows per rule  # noqa: E501

        :param post_hook: The post_hook of this RuleSchema.  # noqa: E501
        :type: list[RuleSchemaPrehook]
        """

        self._post_hook = post_hook

    @property
    def redirect_to(self):
        """Gets the redirect_to of this RuleSchema.  # noqa: E501


        :return: The redirect_to of this RuleSchema.  # noqa: E501
        :rtype: RuleSchemaRedirectto
        """
        return self._redirect_to

    @redirect_to.setter
    def redirect_to(self, redirect_to):
        """Sets the redirect_to of this RuleSchema.


        :param redirect_to: The redirect_to of this RuleSchema.  # noqa: E501
        :type: RuleSchemaRedirectto
        """

        self._redirect_to = redirect_to

    @property
    def rule_frequency(self):
        """Gets the rule_frequency of this RuleSchema.  # noqa: E501

        Frequency at which the rule’s field, reference, and vector elements should be computed. Required only when a rule doesn’t have a sensor defined. Specify integer >= 0 followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s  # noqa: E501

        :return: The rule_frequency of this RuleSchema.  # noqa: E501
        :rtype: str
        """
        return self._rule_frequency

    @rule_frequency.setter
    def rule_frequency(self, rule_frequency):
        """Sets the rule_frequency of this RuleSchema.

        Frequency at which the rule’s field, reference, and vector elements should be computed. Required only when a rule doesn’t have a sensor defined. Specify integer >= 0 followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s  # noqa: E501

        :param rule_frequency: The rule_frequency of this RuleSchema.  # noqa: E501
        :type: str
        """
        if rule_frequency is not None and not re.search(r'^[1-9][0-9]*[smhdwy]$', rule_frequency):  # noqa: E501
            raise ValueError(r"Invalid value for `rule_frequency`, must be a follow pattern or equal to `/^[1-9][0-9]*[smhdwy]$/`")  # noqa: E501

        self._rule_frequency = rule_frequency

    @property
    def rule_name(self):
        """Gets the rule_name of this RuleSchema.  # noqa: E501

        Name of the rule. Should be of pattern [a-z][a-z0-9_-]*  # noqa: E501

        :return: The rule_name of this RuleSchema.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this RuleSchema.

        Name of the rule. Should be of pattern [a-z][a-z0-9_-]*  # noqa: E501

        :param rule_name: The rule_name of this RuleSchema.  # noqa: E501
        :type: str
        """
        if rule_name is None:
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501
        if rule_name is not None and len(rule_name) > 64:
            raise ValueError("Invalid value for `rule_name`, length must be less than or equal to `64`")  # noqa: E501
        if rule_name is not None and not re.search(r'^[a-z][a-z0-9_-]*$', rule_name):  # noqa: E501
            raise ValueError(r"Invalid value for `rule_name`, must be a follow pattern or equal to `/^[a-z][a-z0-9_-]*$/`")  # noqa: E501

        self._rule_name = rule_name

    @property
    def sensor(self):
        """Gets the sensor of this RuleSchema.  # noqa: E501


        :return: The sensor of this RuleSchema.  # noqa: E501
        :rtype: list[RuleSchemaSensor1]
        """
        return self._sensor

    @sensor.setter
    def sensor(self, sensor):
        """Sets the sensor of this RuleSchema.


        :param sensor: The sensor of this RuleSchema.  # noqa: E501
        :type: list[RuleSchemaSensor1]
        """

        self._sensor = sensor

    @property
    def synopsis(self):
        """Gets the synopsis of this RuleSchema.  # noqa: E501

        Synopsis about the rule  # noqa: E501

        :return: The synopsis of this RuleSchema.  # noqa: E501
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """Sets the synopsis of this RuleSchema.

        Synopsis about the rule  # noqa: E501

        :param synopsis: The synopsis of this RuleSchema.  # noqa: E501
        :type: str
        """

        self._synopsis = synopsis

    @property
    def field_aggregation_time_range(self):
        """Gets the field_aggregation_time_range of this RuleSchema.  # noqa: E501

        How much back in time should we look for field aggregation. Specify positive integer followed by o/s/m/h/d/w/y/offset representing seconds/minutes/hours/days/weeks/years. Eg: 2s  # noqa: E501

        :return: The field_aggregation_time_range of this RuleSchema.  # noqa: E501
        :rtype: str
        """
        return self._field_aggregation_time_range

    @field_aggregation_time_range.setter
    def field_aggregation_time_range(self, field_aggregation_time_range):
        """Sets the field_aggregation_time_range of this RuleSchema.

        How much back in time should we look for field aggregation. Specify positive integer followed by o/s/m/h/d/w/y/offset representing seconds/minutes/hours/days/weeks/years. Eg: 2s  # noqa: E501

        :param field_aggregation_time_range: The field_aggregation_time_range of this RuleSchema.  # noqa: E501
        :type: str
        """
        if field_aggregation_time_range is not None and not re.search(r'^[1-9][0-9]*(o|s|m|h|d|w|y|offset)$', field_aggregation_time_range):  # noqa: E501
            raise ValueError(r"Invalid value for `field_aggregation_time_range`, must be a follow pattern or equal to `/^[1-9][0-9]*(o|s|m|h|d|w|y|offset)$/`")  # noqa: E501

        self._field_aggregation_time_range = field_aggregation_time_range

    @property
    def trigger(self):
        """Gets the trigger of this RuleSchema.  # noqa: E501


        :return: The trigger of this RuleSchema.  # noqa: E501
        :rtype: list[RuleSchemaTrigger]
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this RuleSchema.


        :param trigger: The trigger of this RuleSchema.  # noqa: E501
        :type: list[RuleSchemaTrigger]
        """

        self._trigger = trigger

    @property
    def variable(self):
        """Gets the variable of this RuleSchema.  # noqa: E501

        Playbook variable configuration  # noqa: E501

        :return: The variable of this RuleSchema.  # noqa: E501
        :rtype: list[RuleSchemaVariable]
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this RuleSchema.

        Playbook variable configuration  # noqa: E501

        :param variable: The variable of this RuleSchema.  # noqa: E501
        :type: list[RuleSchemaVariable]
        """

        self._variable = variable

    @property
    def vector(self):
        """Gets the vector of this RuleSchema.  # noqa: E501


        :return: The vector of this RuleSchema.  # noqa: E501
        :rtype: list[RuleSchemaVector]
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        """Sets the vector of this RuleSchema.


        :param vector: The vector of this RuleSchema.  # noqa: E501
        :type: list[RuleSchemaVector]
        """

        self._vector = vector

    @property
    def rule_properties(self):
        """Gets the rule_properties of this RuleSchema.  # noqa: E501


        :return: The rule_properties of this RuleSchema.  # noqa: E501
        :rtype: RuleSchemaRuleproperties
        """
        return self._rule_properties

    @rule_properties.setter
    def rule_properties(self, rule_properties):
        """Sets the rule_properties of this RuleSchema.


        :param rule_properties: The rule_properties of this RuleSchema.  # noqa: E501
        :type: RuleSchemaRuleproperties
        """

        self._rule_properties = rule_properties

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
        if issubclass(RuleSchema, dict):
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
        if not isinstance(other, RuleSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
