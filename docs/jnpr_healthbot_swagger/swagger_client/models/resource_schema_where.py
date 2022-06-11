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


class ResourceSchemaWhere(object):
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
        'does_not_match_with': 'list[ResourceSchemaWhereDoesnotmatchwith]',
        'equal_to': 'list[ResourceSchemaWhereEqualto]',
        'eval': 'list[TaggingprofileSchemaWhenEval]',
        'greater_than': 'list[ResourceSchemaWhereEqualto]',
        'greater_than_or_equal_to': 'list[ResourceSchemaWhereEqualto]',
        'less_than': 'list[ResourceSchemaWhereEqualto]',
        'less_than_or_equal_to': 'list[ResourceSchemaWhereEqualto]',
        'matches_with': 'list[ResourceSchemaWhereMatcheswith]',
        'not_equal_to': 'list[ResourceSchemaWhereEqualto]',
        'user_defined_function': 'list[ResourceSchemaWhereUserdefinedfunction]'
    }

    attribute_map = {
        'does_not_match_with': 'does-not-match-with',
        'equal_to': 'equal-to',
        'eval': 'eval',
        'greater_than': 'greater-than',
        'greater_than_or_equal_to': 'greater-than-or-equal-to',
        'less_than': 'less-than',
        'less_than_or_equal_to': 'less-than-or-equal-to',
        'matches_with': 'matches-with',
        'not_equal_to': 'not-equal-to',
        'user_defined_function': 'user-defined-function'
    }

    def __init__(self, does_not_match_with=None, equal_to=None, eval=None, greater_than=None, greater_than_or_equal_to=None, less_than=None, less_than_or_equal_to=None, matches_with=None, not_equal_to=None, user_defined_function=None):  # noqa: E501
        """ResourceSchemaWhere - a model defined in Swagger"""  # noqa: E501

        self._does_not_match_with = None
        self._equal_to = None
        self._eval = None
        self._greater_than = None
        self._greater_than_or_equal_to = None
        self._less_than = None
        self._less_than_or_equal_to = None
        self._matches_with = None
        self._not_equal_to = None
        self._user_defined_function = None
        self.discriminator = None

        if does_not_match_with is not None:
            self.does_not_match_with = does_not_match_with
        if equal_to is not None:
            self.equal_to = equal_to
        if eval is not None:
            self.eval = eval
        if greater_than is not None:
            self.greater_than = greater_than
        if greater_than_or_equal_to is not None:
            self.greater_than_or_equal_to = greater_than_or_equal_to
        if less_than is not None:
            self.less_than = less_than
        if less_than_or_equal_to is not None:
            self.less_than_or_equal_to = less_than_or_equal_to
        if matches_with is not None:
            self.matches_with = matches_with
        if not_equal_to is not None:
            self.not_equal_to = not_equal_to
        if user_defined_function is not None:
            self.user_defined_function = user_defined_function

    @property
    def does_not_match_with(self):
        """Gets the does_not_match_with of this ResourceSchemaWhere.  # noqa: E501


        :return: The does_not_match_with of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereDoesnotmatchwith]
        """
        return self._does_not_match_with

    @does_not_match_with.setter
    def does_not_match_with(self, does_not_match_with):
        """Sets the does_not_match_with of this ResourceSchemaWhere.


        :param does_not_match_with: The does_not_match_with of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereDoesnotmatchwith]
        """

        self._does_not_match_with = does_not_match_with

    @property
    def equal_to(self):
        """Gets the equal_to of this ResourceSchemaWhere.  # noqa: E501


        :return: The equal_to of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereEqualto]
        """
        return self._equal_to

    @equal_to.setter
    def equal_to(self, equal_to):
        """Sets the equal_to of this ResourceSchemaWhere.


        :param equal_to: The equal_to of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereEqualto]
        """

        self._equal_to = equal_to

    @property
    def eval(self):
        """Gets the eval of this ResourceSchemaWhere.  # noqa: E501


        :return: The eval of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[TaggingprofileSchemaWhenEval]
        """
        return self._eval

    @eval.setter
    def eval(self, eval):
        """Sets the eval of this ResourceSchemaWhere.


        :param eval: The eval of this ResourceSchemaWhere.  # noqa: E501
        :type: list[TaggingprofileSchemaWhenEval]
        """

        self._eval = eval

    @property
    def greater_than(self):
        """Gets the greater_than of this ResourceSchemaWhere.  # noqa: E501


        :return: The greater_than of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereEqualto]
        """
        return self._greater_than

    @greater_than.setter
    def greater_than(self, greater_than):
        """Sets the greater_than of this ResourceSchemaWhere.


        :param greater_than: The greater_than of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereEqualto]
        """

        self._greater_than = greater_than

    @property
    def greater_than_or_equal_to(self):
        """Gets the greater_than_or_equal_to of this ResourceSchemaWhere.  # noqa: E501


        :return: The greater_than_or_equal_to of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereEqualto]
        """
        return self._greater_than_or_equal_to

    @greater_than_or_equal_to.setter
    def greater_than_or_equal_to(self, greater_than_or_equal_to):
        """Sets the greater_than_or_equal_to of this ResourceSchemaWhere.


        :param greater_than_or_equal_to: The greater_than_or_equal_to of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereEqualto]
        """

        self._greater_than_or_equal_to = greater_than_or_equal_to

    @property
    def less_than(self):
        """Gets the less_than of this ResourceSchemaWhere.  # noqa: E501


        :return: The less_than of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereEqualto]
        """
        return self._less_than

    @less_than.setter
    def less_than(self, less_than):
        """Sets the less_than of this ResourceSchemaWhere.


        :param less_than: The less_than of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereEqualto]
        """

        self._less_than = less_than

    @property
    def less_than_or_equal_to(self):
        """Gets the less_than_or_equal_to of this ResourceSchemaWhere.  # noqa: E501


        :return: The less_than_or_equal_to of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereEqualto]
        """
        return self._less_than_or_equal_to

    @less_than_or_equal_to.setter
    def less_than_or_equal_to(self, less_than_or_equal_to):
        """Sets the less_than_or_equal_to of this ResourceSchemaWhere.


        :param less_than_or_equal_to: The less_than_or_equal_to of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereEqualto]
        """

        self._less_than_or_equal_to = less_than_or_equal_to

    @property
    def matches_with(self):
        """Gets the matches_with of this ResourceSchemaWhere.  # noqa: E501


        :return: The matches_with of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereMatcheswith]
        """
        return self._matches_with

    @matches_with.setter
    def matches_with(self, matches_with):
        """Sets the matches_with of this ResourceSchemaWhere.


        :param matches_with: The matches_with of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereMatcheswith]
        """

        self._matches_with = matches_with

    @property
    def not_equal_to(self):
        """Gets the not_equal_to of this ResourceSchemaWhere.  # noqa: E501


        :return: The not_equal_to of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereEqualto]
        """
        return self._not_equal_to

    @not_equal_to.setter
    def not_equal_to(self, not_equal_to):
        """Sets the not_equal_to of this ResourceSchemaWhere.


        :param not_equal_to: The not_equal_to of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereEqualto]
        """

        self._not_equal_to = not_equal_to

    @property
    def user_defined_function(self):
        """Gets the user_defined_function of this ResourceSchemaWhere.  # noqa: E501

        User defined function to populate field value  # noqa: E501

        :return: The user_defined_function of this ResourceSchemaWhere.  # noqa: E501
        :rtype: list[ResourceSchemaWhereUserdefinedfunction]
        """
        return self._user_defined_function

    @user_defined_function.setter
    def user_defined_function(self, user_defined_function):
        """Sets the user_defined_function of this ResourceSchemaWhere.

        User defined function to populate field value  # noqa: E501

        :param user_defined_function: The user_defined_function of this ResourceSchemaWhere.  # noqa: E501
        :type: list[ResourceSchemaWhereUserdefinedfunction]
        """

        self._user_defined_function = user_defined_function

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
        if issubclass(ResourceSchemaWhere, dict):
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
        if not isinstance(other, ResourceSchemaWhere):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
