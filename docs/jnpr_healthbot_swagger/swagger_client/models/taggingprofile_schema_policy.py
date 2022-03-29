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


class TaggingprofileSchemaPolicy(object):
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
        'name': 'str',
        'rules': 'list[str]',
        'term': 'list[TaggingprofileSchemaTerm]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'rules': 'rules',
        'term': 'term'
    }

    def __init__(self, description=None, name=None, rules=None, term=None):  # noqa: E501
        """TaggingprofileSchemaPolicy - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self._rules = None
        self._term = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        self.rules = rules
        self.term = term

    @property
    def description(self):
        """Gets the description of this TaggingprofileSchemaPolicy.  # noqa: E501

        Description about policy  # noqa: E501

        :return: The description of this TaggingprofileSchemaPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaggingprofileSchemaPolicy.

        Description about policy  # noqa: E501

        :param description: The description of this TaggingprofileSchemaPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this TaggingprofileSchemaPolicy.  # noqa: E501

        Policy name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The name of this TaggingprofileSchemaPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaggingprofileSchemaPolicy.

        Policy name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param name: The name of this TaggingprofileSchemaPolicy.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def rules(self):
        """Gets the rules of this TaggingprofileSchemaPolicy.  # noqa: E501


        :return: The rules of this TaggingprofileSchemaPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this TaggingprofileSchemaPolicy.


        :param rules: The rules of this TaggingprofileSchemaPolicy.  # noqa: E501
        :type: list[str]
        """
        if rules is None:
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501

        self._rules = rules

    @property
    def term(self):
        """Gets the term of this TaggingprofileSchemaPolicy.  # noqa: E501


        :return: The term of this TaggingprofileSchemaPolicy.  # noqa: E501
        :rtype: list[TaggingprofileSchemaTerm]
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this TaggingprofileSchemaPolicy.


        :param term: The term of this TaggingprofileSchemaPolicy.  # noqa: E501
        :type: list[TaggingprofileSchemaTerm]
        """
        if term is None:
            raise ValueError("Invalid value for `term`, must not be `None`")  # noqa: E501

        self._term = term

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
        if issubclass(TaggingprofileSchemaPolicy, dict):
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
        if not isinstance(other, TaggingprofileSchemaPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other