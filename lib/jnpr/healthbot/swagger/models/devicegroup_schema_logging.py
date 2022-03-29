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


class DevicegroupSchemaLogging(object):
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
        'i_agent': 'DevicegroupSchemaLoggingIAgent',
        'log_level': 'str',
        'native_gpb': 'DevicegroupSchemaLoggingNativegpb',
        'non_sensor_rules': 'DevicegroupSchemaLoggingNonsensorrules',
        'open_config': 'DevicegroupSchemaLoggingOpenconfig',
        'server_monitoring': 'DevicegroupSchemaLoggingServermonitoring',
        'reports_generation': 'DevicegroupSchemaLoggingReportsgeneration',
        'snmp': 'DevicegroupSchemaLoggingSnmp',
        'trigger_evaluation': 'DevicegroupSchemaLoggingTriggerevaluation',
        'ml_model_builder': 'DevicegroupSchemaLoggingMLmodelbuilder',
        'resource_discovery': 'DevicegroupSchemaLoggingResourcediscovery',
        'flow': 'DevicegroupSchemaLoggingFlow',
        'sflow': 'DevicegroupSchemaLoggingSflow',
        'byoi': 'DevicegroupSchemaLoggingByoi',
        'snmp_notification': 'DevicegroupSchemaLoggingSnmpnotification',
        'syslog': 'DevicegroupSchemaLoggingSyslog'
    }

    attribute_map = {
        'i_agent': 'iAgent',
        'log_level': 'log-level',
        'native_gpb': 'native-gpb',
        'non_sensor_rules': 'non-sensor-rules',
        'open_config': 'open-config',
        'server_monitoring': 'server-monitoring',
        'reports_generation': 'reports-generation',
        'snmp': 'snmp',
        'trigger_evaluation': 'trigger-evaluation',
        'ml_model_builder': 'ML-model-builder',
        'resource_discovery': 'resource-discovery',
        'flow': 'flow',
        'sflow': 'sflow',
        'byoi': 'byoi',
        'snmp_notification': 'snmp-notification',
        'syslog': 'syslog'
    }

    def __init__(self, i_agent=None, log_level=None, native_gpb=None, non_sensor_rules=None, open_config=None, server_monitoring=None, reports_generation=None, snmp=None, trigger_evaluation=None, ml_model_builder=None, resource_discovery=None, flow=None, sflow=None, byoi=None, snmp_notification=None, syslog=None):  # noqa: E501
        """DevicegroupSchemaLogging - a model defined in Swagger"""  # noqa: E501

        self._i_agent = None
        self._log_level = None
        self._native_gpb = None
        self._non_sensor_rules = None
        self._open_config = None
        self._server_monitoring = None
        self._reports_generation = None
        self._snmp = None
        self._trigger_evaluation = None
        self._ml_model_builder = None
        self._resource_discovery = None
        self._flow = None
        self._sflow = None
        self._byoi = None
        self._snmp_notification = None
        self._syslog = None
        self.discriminator = None

        if i_agent is not None:
            self.i_agent = i_agent
        if log_level is not None:
            self.log_level = log_level
        if native_gpb is not None:
            self.native_gpb = native_gpb
        if non_sensor_rules is not None:
            self.non_sensor_rules = non_sensor_rules
        if open_config is not None:
            self.open_config = open_config
        if server_monitoring is not None:
            self.server_monitoring = server_monitoring
        if reports_generation is not None:
            self.reports_generation = reports_generation
        if snmp is not None:
            self.snmp = snmp
        if trigger_evaluation is not None:
            self.trigger_evaluation = trigger_evaluation
        if ml_model_builder is not None:
            self.ml_model_builder = ml_model_builder
        if resource_discovery is not None:
            self.resource_discovery = resource_discovery
        if flow is not None:
            self.flow = flow
        if sflow is not None:
            self.sflow = sflow
        if byoi is not None:
            self.byoi = byoi
        if snmp_notification is not None:
            self.snmp_notification = snmp_notification
        if syslog is not None:
            self.syslog = syslog

    @property
    def i_agent(self):
        """Gets the i_agent of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The i_agent of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingIAgent
        """
        return self._i_agent

    @i_agent.setter
    def i_agent(self, i_agent):
        """Sets the i_agent of this DevicegroupSchemaLogging.


        :param i_agent: The i_agent of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingIAgent
        """

        self._i_agent = i_agent

    @property
    def log_level(self):
        """Gets the log_level of this DevicegroupSchemaLogging.  # noqa: E501

        Global log level  # noqa: E501

        :return: The log_level of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this DevicegroupSchemaLogging.

        Global log level  # noqa: E501

        :param log_level: The log_level of this DevicegroupSchemaLogging.  # noqa: E501
        :type: str
        """
        allowed_values = ["error", "debug", "warn", "info"]  # noqa: E501
        if log_level not in allowed_values:
            raise ValueError(
                "Invalid value for `log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(log_level, allowed_values)
            )

        self._log_level = log_level

    @property
    def native_gpb(self):
        """Gets the native_gpb of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The native_gpb of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingNativegpb
        """
        return self._native_gpb

    @native_gpb.setter
    def native_gpb(self, native_gpb):
        """Sets the native_gpb of this DevicegroupSchemaLogging.


        :param native_gpb: The native_gpb of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingNativegpb
        """

        self._native_gpb = native_gpb

    @property
    def non_sensor_rules(self):
        """Gets the non_sensor_rules of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The non_sensor_rules of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingNonsensorrules
        """
        return self._non_sensor_rules

    @non_sensor_rules.setter
    def non_sensor_rules(self, non_sensor_rules):
        """Sets the non_sensor_rules of this DevicegroupSchemaLogging.


        :param non_sensor_rules: The non_sensor_rules of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingNonsensorrules
        """

        self._non_sensor_rules = non_sensor_rules

    @property
    def open_config(self):
        """Gets the open_config of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The open_config of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingOpenconfig
        """
        return self._open_config

    @open_config.setter
    def open_config(self, open_config):
        """Sets the open_config of this DevicegroupSchemaLogging.


        :param open_config: The open_config of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingOpenconfig
        """

        self._open_config = open_config

    @property
    def server_monitoring(self):
        """Gets the server_monitoring of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The server_monitoring of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingServermonitoring
        """
        return self._server_monitoring

    @server_monitoring.setter
    def server_monitoring(self, server_monitoring):
        """Sets the server_monitoring of this DevicegroupSchemaLogging.


        :param server_monitoring: The server_monitoring of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingServermonitoring
        """

        self._server_monitoring = server_monitoring

    @property
    def reports_generation(self):
        """Gets the reports_generation of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The reports_generation of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingReportsgeneration
        """
        return self._reports_generation

    @reports_generation.setter
    def reports_generation(self, reports_generation):
        """Sets the reports_generation of this DevicegroupSchemaLogging.


        :param reports_generation: The reports_generation of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingReportsgeneration
        """

        self._reports_generation = reports_generation

    @property
    def snmp(self):
        """Gets the snmp of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The snmp of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingSnmp
        """
        return self._snmp

    @snmp.setter
    def snmp(self, snmp):
        """Sets the snmp of this DevicegroupSchemaLogging.


        :param snmp: The snmp of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingSnmp
        """

        self._snmp = snmp

    @property
    def trigger_evaluation(self):
        """Gets the trigger_evaluation of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The trigger_evaluation of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingTriggerevaluation
        """
        return self._trigger_evaluation

    @trigger_evaluation.setter
    def trigger_evaluation(self, trigger_evaluation):
        """Sets the trigger_evaluation of this DevicegroupSchemaLogging.


        :param trigger_evaluation: The trigger_evaluation of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingTriggerevaluation
        """

        self._trigger_evaluation = trigger_evaluation

    @property
    def ml_model_builder(self):
        """Gets the ml_model_builder of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The ml_model_builder of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingMLmodelbuilder
        """
        return self._ml_model_builder

    @ml_model_builder.setter
    def ml_model_builder(self, ml_model_builder):
        """Sets the ml_model_builder of this DevicegroupSchemaLogging.


        :param ml_model_builder: The ml_model_builder of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingMLmodelbuilder
        """

        self._ml_model_builder = ml_model_builder

    @property
    def resource_discovery(self):
        """Gets the resource_discovery of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The resource_discovery of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingResourcediscovery
        """
        return self._resource_discovery

    @resource_discovery.setter
    def resource_discovery(self, resource_discovery):
        """Sets the resource_discovery of this DevicegroupSchemaLogging.


        :param resource_discovery: The resource_discovery of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingResourcediscovery
        """

        self._resource_discovery = resource_discovery

    @property
    def flow(self):
        """Gets the flow of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The flow of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this DevicegroupSchemaLogging.


        :param flow: The flow of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingFlow
        """

        self._flow = flow

    @property
    def sflow(self):
        """Gets the sflow of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The sflow of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingSflow
        """
        return self._sflow

    @sflow.setter
    def sflow(self, sflow):
        """Sets the sflow of this DevicegroupSchemaLogging.


        :param sflow: The sflow of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingSflow
        """

        self._sflow = sflow

    @property
    def byoi(self):
        """Gets the byoi of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The byoi of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingByoi
        """
        return self._byoi

    @byoi.setter
    def byoi(self, byoi):
        """Sets the byoi of this DevicegroupSchemaLogging.


        :param byoi: The byoi of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingByoi
        """

        self._byoi = byoi

    @property
    def snmp_notification(self):
        """Gets the snmp_notification of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The snmp_notification of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingSnmpnotification
        """
        return self._snmp_notification

    @snmp_notification.setter
    def snmp_notification(self, snmp_notification):
        """Sets the snmp_notification of this DevicegroupSchemaLogging.


        :param snmp_notification: The snmp_notification of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingSnmpnotification
        """

        self._snmp_notification = snmp_notification

    @property
    def syslog(self):
        """Gets the syslog of this DevicegroupSchemaLogging.  # noqa: E501


        :return: The syslog of this DevicegroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingSyslog
        """
        return self._syslog

    @syslog.setter
    def syslog(self, syslog):
        """Sets the syslog of this DevicegroupSchemaLogging.


        :param syslog: The syslog of this DevicegroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingSyslog
        """

        self._syslog = syslog

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
        if issubclass(DevicegroupSchemaLogging, dict):
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
        if not isinstance(other, DevicegroupSchemaLogging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other