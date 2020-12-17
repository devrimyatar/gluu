# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustomScriptScriptError(object):
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
        'raised_at': 'date',
        'stack_trace': 'str'
    }

    attribute_map = {
        'raised_at': 'raisedAt',
        'stack_trace': 'stackTrace'
    }

    def __init__(self, raised_at=None, stack_trace=None):  # noqa: E501
        """CustomScriptScriptError - a model defined in Swagger"""  # noqa: E501
        self._raised_at = None
        self._stack_trace = None
        self.discriminator = None
        if raised_at is not None:
            self.raised_at = raised_at
        if stack_trace is not None:
            self.stack_trace = stack_trace

    @property
    def raised_at(self):
        """Gets the raised_at of this CustomScriptScriptError.  # noqa: E501


        :return: The raised_at of this CustomScriptScriptError.  # noqa: E501
        :rtype: date
        """
        return self._raised_at

    @raised_at.setter
    def raised_at(self, raised_at):
        """Sets the raised_at of this CustomScriptScriptError.


        :param raised_at: The raised_at of this CustomScriptScriptError.  # noqa: E501
        :type: date
        """

        self._raised_at = raised_at

    @property
    def stack_trace(self):
        """Gets the stack_trace of this CustomScriptScriptError.  # noqa: E501


        :return: The stack_trace of this CustomScriptScriptError.  # noqa: E501
        :rtype: str
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this CustomScriptScriptError.


        :param stack_trace: The stack_trace of this CustomScriptScriptError.  # noqa: E501
        :type: str
        """

        self._stack_trace = stack_trace

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
        if issubclass(CustomScriptScriptError, dict):
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
        if not isinstance(other, CustomScriptScriptError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
