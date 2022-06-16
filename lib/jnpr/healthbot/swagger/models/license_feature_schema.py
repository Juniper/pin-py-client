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


class LicenseFeatureSchema(object):
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
        'feature_id': 'int',
        'feature_name': 'str',
        'feature_description': 'str',
        'license_total': 'int',
        'license_remaining': 'int',
        'license_requested': 'int',
        'license_usage': 'int',
        'max_remaining_days': 'int',
        'validity_type': 'str',
        'mode': 'str',
        'compliance': 'bool',
        'end_date': 'int',
        'valid_until': 'str'
    }

    attribute_map = {
        'feature_id': 'feature-id',
        'feature_name': 'feature-name',
        'feature_description': 'feature-description',
        'license_total': 'license-total',
        'license_remaining': 'license-remaining',
        'license_requested': 'license-requested',
        'license_usage': 'license-usage',
        'max_remaining_days': 'max-remaining-days',
        'validity_type': 'validity-type',
        'mode': 'mode',
        'compliance': 'compliance',
        'end_date': 'end-date',
        'valid_until': 'valid-until'
    }

    def __init__(self, feature_id=None, feature_name=None, feature_description=None, license_total=None, license_remaining=None, license_requested=None, license_usage=None, max_remaining_days=None, validity_type=None, mode=None, compliance=None, end_date=None, valid_until=None):  # noqa: E501
        """LicenseFeatureSchema - a model defined in Swagger"""  # noqa: E501

        self._feature_id = None
        self._feature_name = None
        self._feature_description = None
        self._license_total = None
        self._license_remaining = None
        self._license_requested = None
        self._license_usage = None
        self._max_remaining_days = None
        self._validity_type = None
        self._mode = None
        self._compliance = None
        self._end_date = None
        self._valid_until = None
        self.discriminator = None

        if feature_id is not None:
            self.feature_id = feature_id
        self.feature_name = feature_name
        self.feature_description = feature_description
        self.license_total = license_total
        if license_remaining is not None:
            self.license_remaining = license_remaining
        if license_requested is not None:
            self.license_requested = license_requested
        self.license_usage = license_usage
        self.max_remaining_days = max_remaining_days
        self.validity_type = validity_type
        self.mode = mode
        self.compliance = compliance
        self.end_date = end_date
        self.valid_until = valid_until

    @property
    def feature_id(self):
        """Gets the feature_id of this LicenseFeatureSchema.  # noqa: E501

        Unique ID of the licensed feature  # noqa: E501

        :return: The feature_id of this LicenseFeatureSchema.  # noqa: E501
        :rtype: int
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this LicenseFeatureSchema.

        Unique ID of the licensed feature  # noqa: E501

        :param feature_id: The feature_id of this LicenseFeatureSchema.  # noqa: E501
        :type: int
        """
        if feature_id is not None and feature_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `feature_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._feature_id = feature_id

    @property
    def feature_name(self):
        """Gets the feature_name of this LicenseFeatureSchema.  # noqa: E501

        Name of the licensed feature  # noqa: E501

        :return: The feature_name of this LicenseFeatureSchema.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this LicenseFeatureSchema.

        Name of the licensed feature  # noqa: E501

        :param feature_name: The feature_name of this LicenseFeatureSchema.  # noqa: E501
        :type: str
        """
        if feature_name is None:
            raise ValueError("Invalid value for `feature_name`, must not be `None`")  # noqa: E501

        self._feature_name = feature_name

    @property
    def feature_description(self):
        """Gets the feature_description of this LicenseFeatureSchema.  # noqa: E501

        Brief description of the licensed feature  # noqa: E501

        :return: The feature_description of this LicenseFeatureSchema.  # noqa: E501
        :rtype: str
        """
        return self._feature_description

    @feature_description.setter
    def feature_description(self, feature_description):
        """Sets the feature_description of this LicenseFeatureSchema.

        Brief description of the licensed feature  # noqa: E501

        :param feature_description: The feature_description of this LicenseFeatureSchema.  # noqa: E501
        :type: str
        """
        if feature_description is None:
            raise ValueError("Invalid value for `feature_description`, must not be `None`")  # noqa: E501

        self._feature_description = feature_description

    @property
    def license_total(self):
        """Gets the license_total of this LicenseFeatureSchema.  # noqa: E501

        Total license count for feature  # noqa: E501

        :return: The license_total of this LicenseFeatureSchema.  # noqa: E501
        :rtype: int
        """
        return self._license_total

    @license_total.setter
    def license_total(self, license_total):
        """Sets the license_total of this LicenseFeatureSchema.

        Total license count for feature  # noqa: E501

        :param license_total: The license_total of this LicenseFeatureSchema.  # noqa: E501
        :type: int
        """
        if license_total is None:
            raise ValueError("Invalid value for `license_total`, must not be `None`")  # noqa: E501
        if license_total is not None and license_total < 0:  # noqa: E501
            raise ValueError("Invalid value for `license_total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._license_total = license_total

    @property
    def license_remaining(self):
        """Gets the license_remaining of this LicenseFeatureSchema.  # noqa: E501

        Remaining license count for feature  # noqa: E501

        :return: The license_remaining of this LicenseFeatureSchema.  # noqa: E501
        :rtype: int
        """
        return self._license_remaining

    @license_remaining.setter
    def license_remaining(self, license_remaining):
        """Sets the license_remaining of this LicenseFeatureSchema.

        Remaining license count for feature  # noqa: E501

        :param license_remaining: The license_remaining of this LicenseFeatureSchema.  # noqa: E501
        :type: int
        """
        if license_remaining is not None and license_remaining < 0:  # noqa: E501
            raise ValueError("Invalid value for `license_remaining`, must be a value greater than or equal to `0`")  # noqa: E501

        self._license_remaining = license_remaining

    @property
    def license_requested(self):
        """Gets the license_requested of this LicenseFeatureSchema.  # noqa: E501

        Local requested license count for feature  # noqa: E501

        :return: The license_requested of this LicenseFeatureSchema.  # noqa: E501
        :rtype: int
        """
        return self._license_requested

    @license_requested.setter
    def license_requested(self, license_requested):
        """Sets the license_requested of this LicenseFeatureSchema.

        Local requested license count for feature  # noqa: E501

        :param license_requested: The license_requested of this LicenseFeatureSchema.  # noqa: E501
        :type: int
        """
        if license_requested is not None and license_requested < 0:  # noqa: E501
            raise ValueError("Invalid value for `license_requested`, must be a value greater than or equal to `0`")  # noqa: E501

        self._license_requested = license_requested

    @property
    def license_usage(self):
        """Gets the license_usage of this LicenseFeatureSchema.  # noqa: E501

        License feature usage count  # noqa: E501

        :return: The license_usage of this LicenseFeatureSchema.  # noqa: E501
        :rtype: int
        """
        return self._license_usage

    @license_usage.setter
    def license_usage(self, license_usage):
        """Sets the license_usage of this LicenseFeatureSchema.

        License feature usage count  # noqa: E501

        :param license_usage: The license_usage of this LicenseFeatureSchema.  # noqa: E501
        :type: int
        """
        if license_usage is None:
            raise ValueError("Invalid value for `license_usage`, must not be `None`")  # noqa: E501
        if license_usage is not None and license_usage < 0:  # noqa: E501
            raise ValueError("Invalid value for `license_usage`, must be a value greater than or equal to `0`")  # noqa: E501

        self._license_usage = license_usage

    @property
    def max_remaining_days(self):
        """Gets the max_remaining_days of this LicenseFeatureSchema.  # noqa: E501

        Maximum remaining time of the feature's license in days  # noqa: E501

        :return: The max_remaining_days of this LicenseFeatureSchema.  # noqa: E501
        :rtype: int
        """
        return self._max_remaining_days

    @max_remaining_days.setter
    def max_remaining_days(self, max_remaining_days):
        """Sets the max_remaining_days of this LicenseFeatureSchema.

        Maximum remaining time of the feature's license in days  # noqa: E501

        :param max_remaining_days: The max_remaining_days of this LicenseFeatureSchema.  # noqa: E501
        :type: int
        """
        if max_remaining_days is None:
            raise ValueError("Invalid value for `max_remaining_days`, must not be `None`")  # noqa: E501
        if max_remaining_days is not None and max_remaining_days < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_remaining_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_remaining_days = max_remaining_days

    @property
    def validity_type(self):
        """Gets the validity_type of this LicenseFeatureSchema.  # noqa: E501

        License validity type  # noqa: E501

        :return: The validity_type of this LicenseFeatureSchema.  # noqa: E501
        :rtype: str
        """
        return self._validity_type

    @validity_type.setter
    def validity_type(self, validity_type):
        """Sets the validity_type of this LicenseFeatureSchema.

        License validity type  # noqa: E501

        :param validity_type: The validity_type of this LicenseFeatureSchema.  # noqa: E501
        :type: str
        """
        if validity_type is None:
            raise ValueError("Invalid value for `validity_type`, must not be `None`")  # noqa: E501
        allowed_values = ["invalid", "countdown", "date-based", "permanent"]  # noqa: E501
        if validity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `validity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(validity_type, allowed_values)
            )

        self._validity_type = validity_type

    @property
    def mode(self):
        """Gets the mode of this LicenseFeatureSchema.  # noqa: E501

        License mode of operation  # noqa: E501

        :return: The mode of this LicenseFeatureSchema.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this LicenseFeatureSchema.

        License mode of operation  # noqa: E501

        :param mode: The mode of this LicenseFeatureSchema.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["invalid", "standalone", "network"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def compliance(self):
        """Gets the compliance of this LicenseFeatureSchema.  # noqa: E501

        Compliance status indicating if the feature usage is in compliance or not  # noqa: E501

        :return: The compliance of this LicenseFeatureSchema.  # noqa: E501
        :rtype: bool
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this LicenseFeatureSchema.

        Compliance status indicating if the feature usage is in compliance or not  # noqa: E501

        :param compliance: The compliance of this LicenseFeatureSchema.  # noqa: E501
        :type: bool
        """
        if compliance is None:
            raise ValueError("Invalid value for `compliance`, must not be `None`")  # noqa: E501

        self._compliance = compliance

    @property
    def end_date(self):
        """Gets the end_date of this LicenseFeatureSchema.  # noqa: E501

        Feature end date timestamp  # noqa: E501

        :return: The end_date of this LicenseFeatureSchema.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this LicenseFeatureSchema.

        Feature end date timestamp  # noqa: E501

        :param end_date: The end_date of this LicenseFeatureSchema.  # noqa: E501
        :type: int
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501
        if end_date is not None and end_date < 0:  # noqa: E501
            raise ValueError("Invalid value for `end_date`, must be a value greater than or equal to `0`")  # noqa: E501

        self._end_date = end_date

    @property
    def valid_until(self):
        """Gets the valid_until of this LicenseFeatureSchema.  # noqa: E501

        Validity information of license feature  # noqa: E501

        :return: The valid_until of this LicenseFeatureSchema.  # noqa: E501
        :rtype: str
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this LicenseFeatureSchema.

        Validity information of license feature  # noqa: E501

        :param valid_until: The valid_until of this LicenseFeatureSchema.  # noqa: E501
        :type: str
        """
        if valid_until is None:
            raise ValueError("Invalid value for `valid_until`, must not be `None`")  # noqa: E501

        self._valid_until = valid_until

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
        if issubclass(LicenseFeatureSchema, dict):
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
        if not isinstance(other, LicenseFeatureSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
