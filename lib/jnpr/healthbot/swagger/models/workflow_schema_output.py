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


class WorkflowSchemaOutput(object):
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
        'artifact': 'WorkflowSchemaArtifact',
        'command_tag': 'str',
        'data_xml': 'WorkflowSchemaDataxml',
        'description': 'str',
        'grok': 'WorkflowSchemaGrok',
        'json': 'WorkflowSchemaJson',
        'name': 'str',
        'result': 'list[object]',
        'regex': 'WorkflowSchemaRegex'
    }

    attribute_map = {
        'artifact': 'artifact',
        'command_tag': 'command-tag',
        'data_xml': 'data-xml',
        'description': 'description',
        'grok': 'grok',
        'json': 'json',
        'name': 'name',
        'result': 'result',
        'regex': 'regex'
    }

    def __init__(self, artifact=None, command_tag=None, data_xml=None, description=None, grok=None, json=None, name=None, result=None, regex=None):  # noqa: E501
        """WorkflowSchemaOutput - a model defined in Swagger"""  # noqa: E501

        self._artifact = None
        self._command_tag = None
        self._data_xml = None
        self._description = None
        self._grok = None
        self._json = None
        self._name = None
        self._result = None
        self._regex = None
        self.discriminator = None

        if artifact is not None:
            self.artifact = artifact
        if command_tag is not None:
            self.command_tag = command_tag
        if data_xml is not None:
            self.data_xml = data_xml
        if description is not None:
            self.description = description
        if grok is not None:
            self.grok = grok
        if json is not None:
            self.json = json
        self.name = name
        if result is not None:
            self.result = result
        if regex is not None:
            self.regex = regex

    @property
    def artifact(self):
        """Gets the artifact of this WorkflowSchemaOutput.  # noqa: E501


        :return: The artifact of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: WorkflowSchemaArtifact
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this WorkflowSchemaOutput.


        :param artifact: The artifact of this WorkflowSchemaOutput.  # noqa: E501
        :type: WorkflowSchemaArtifact
        """

        self._artifact = artifact

    @property
    def command_tag(self):
        """Gets the command_tag of this WorkflowSchemaOutput.  # noqa: E501

        Command tag whose output is used for pattern match  # noqa: E501

        :return: The command_tag of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_tag

    @command_tag.setter
    def command_tag(self, command_tag):
        """Sets the command_tag of this WorkflowSchemaOutput.

        Command tag whose output is used for pattern match  # noqa: E501

        :param command_tag: The command_tag of this WorkflowSchemaOutput.  # noqa: E501
        :type: str
        """

        self._command_tag = command_tag

    @property
    def data_xml(self):
        """Gets the data_xml of this WorkflowSchemaOutput.  # noqa: E501


        :return: The data_xml of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: WorkflowSchemaDataxml
        """
        return self._data_xml

    @data_xml.setter
    def data_xml(self, data_xml):
        """Sets the data_xml of this WorkflowSchemaOutput.


        :param data_xml: The data_xml of this WorkflowSchemaOutput.  # noqa: E501
        :type: WorkflowSchemaDataxml
        """

        self._data_xml = data_xml

    @property
    def description(self):
        """Gets the description of this WorkflowSchemaOutput.  # noqa: E501

        Exported output field desciption  # noqa: E501

        :return: The description of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowSchemaOutput.

        Exported output field desciption  # noqa: E501

        :param description: The description of this WorkflowSchemaOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def grok(self):
        """Gets the grok of this WorkflowSchemaOutput.  # noqa: E501


        :return: The grok of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: WorkflowSchemaGrok
        """
        return self._grok

    @grok.setter
    def grok(self, grok):
        """Sets the grok of this WorkflowSchemaOutput.


        :param grok: The grok of this WorkflowSchemaOutput.  # noqa: E501
        :type: WorkflowSchemaGrok
        """

        self._grok = grok

    @property
    def json(self):
        """Gets the json of this WorkflowSchemaOutput.  # noqa: E501


        :return: The json of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: WorkflowSchemaJson
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this WorkflowSchemaOutput.


        :param json: The json of this WorkflowSchemaOutput.  # noqa: E501
        :type: WorkflowSchemaJson
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this WorkflowSchemaOutput.  # noqa: E501

        Output parameter name exported from the workflow. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The name of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowSchemaOutput.

        Output parameter name exported from the workflow. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param name: The name of this WorkflowSchemaOutput.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def result(self):
        """Gets the result of this WorkflowSchemaOutput.  # noqa: E501

        Export stdout output (stdout) of the step  # noqa: E501

        :return: The result of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: list[object]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this WorkflowSchemaOutput.

        Export stdout output (stdout) of the step  # noqa: E501

        :param result: The result of this WorkflowSchemaOutput.  # noqa: E501
        :type: list[object]
        """

        self._result = result

    @property
    def regex(self):
        """Gets the regex of this WorkflowSchemaOutput.  # noqa: E501


        :return: The regex of this WorkflowSchemaOutput.  # noqa: E501
        :rtype: WorkflowSchemaRegex
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this WorkflowSchemaOutput.


        :param regex: The regex of this WorkflowSchemaOutput.  # noqa: E501
        :type: WorkflowSchemaRegex
        """

        self._regex = regex

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
        if issubclass(WorkflowSchemaOutput, dict):
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
        if not isinstance(other, WorkflowSchemaOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other