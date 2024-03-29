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

class AppConfigurationCorsConfigurationFilters(object):
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
        'filter_name': 'str',
        'cors_enabled': 'bool',
        'cors_allowed_origins': 'str',
        'cors_allowed_methods': 'str',
        'cors_allowed_headers': 'str',
        'cors_exposed_headers': 'str',
        'cors_support_credentials': 'bool',
        'cors_logging_enabled': 'bool',
        'cors_preflight_max_age': 'int',
        'cors_request_decorate': 'bool'
    }

    attribute_map = {
        'filter_name': 'filterName',
        'cors_enabled': 'corsEnabled',
        'cors_allowed_origins': 'corsAllowedOrigins',
        'cors_allowed_methods': 'corsAllowedMethods',
        'cors_allowed_headers': 'corsAllowedHeaders',
        'cors_exposed_headers': 'corsExposedHeaders',
        'cors_support_credentials': 'corsSupportCredentials',
        'cors_logging_enabled': 'corsLoggingEnabled',
        'cors_preflight_max_age': 'corsPreflightMaxAge',
        'cors_request_decorate': 'corsRequestDecorate'
    }

    def __init__(self, filter_name=None, cors_enabled=True, cors_allowed_origins='\*', cors_allowed_methods='GET, POST, HEAD, OPTIONS', cors_allowed_headers='Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers', cors_exposed_headers=None, cors_support_credentials=True, cors_logging_enabled=False, cors_preflight_max_age=1800, cors_request_decorate=True):  # noqa: E501
        """AppConfigurationCorsConfigurationFilters - a model defined in Swagger"""  # noqa: E501
        self._filter_name = None
        self._cors_enabled = None
        self._cors_allowed_origins = None
        self._cors_allowed_methods = None
        self._cors_allowed_headers = None
        self._cors_exposed_headers = None
        self._cors_support_credentials = None
        self._cors_logging_enabled = None
        self._cors_preflight_max_age = None
        self._cors_request_decorate = None
        self.discriminator = None
        if filter_name is not None:
            self.filter_name = filter_name
        if cors_enabled is not None:
            self.cors_enabled = cors_enabled
        if cors_allowed_origins is not None:
            self.cors_allowed_origins = cors_allowed_origins
        if cors_allowed_methods is not None:
            self.cors_allowed_methods = cors_allowed_methods
        if cors_allowed_headers is not None:
            self.cors_allowed_headers = cors_allowed_headers
        if cors_exposed_headers is not None:
            self.cors_exposed_headers = cors_exposed_headers
        if cors_support_credentials is not None:
            self.cors_support_credentials = cors_support_credentials
        if cors_logging_enabled is not None:
            self.cors_logging_enabled = cors_logging_enabled
        if cors_preflight_max_age is not None:
            self.cors_preflight_max_age = cors_preflight_max_age
        if cors_request_decorate is not None:
            self.cors_request_decorate = cors_request_decorate

    @property
    def filter_name(self):
        """Gets the filter_name of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The filter_name of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: str
        """
        return self._filter_name

    @filter_name.setter
    def filter_name(self, filter_name):
        """Sets the filter_name of this AppConfigurationCorsConfigurationFilters.


        :param filter_name: The filter_name of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: str
        """

        self._filter_name = filter_name

    @property
    def cors_enabled(self):
        """Gets the cors_enabled of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_enabled of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: bool
        """
        return self._cors_enabled

    @cors_enabled.setter
    def cors_enabled(self, cors_enabled):
        """Sets the cors_enabled of this AppConfigurationCorsConfigurationFilters.


        :param cors_enabled: The cors_enabled of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: bool
        """

        self._cors_enabled = cors_enabled

    @property
    def cors_allowed_origins(self):
        """Gets the cors_allowed_origins of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_allowed_origins of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: str
        """
        return self._cors_allowed_origins

    @cors_allowed_origins.setter
    def cors_allowed_origins(self, cors_allowed_origins):
        """Sets the cors_allowed_origins of this AppConfigurationCorsConfigurationFilters.


        :param cors_allowed_origins: The cors_allowed_origins of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: str
        """

        self._cors_allowed_origins = cors_allowed_origins

    @property
    def cors_allowed_methods(self):
        """Gets the cors_allowed_methods of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_allowed_methods of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: str
        """
        return self._cors_allowed_methods

    @cors_allowed_methods.setter
    def cors_allowed_methods(self, cors_allowed_methods):
        """Sets the cors_allowed_methods of this AppConfigurationCorsConfigurationFilters.


        :param cors_allowed_methods: The cors_allowed_methods of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: str
        """

        self._cors_allowed_methods = cors_allowed_methods

    @property
    def cors_allowed_headers(self):
        """Gets the cors_allowed_headers of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_allowed_headers of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: str
        """
        return self._cors_allowed_headers

    @cors_allowed_headers.setter
    def cors_allowed_headers(self, cors_allowed_headers):
        """Sets the cors_allowed_headers of this AppConfigurationCorsConfigurationFilters.


        :param cors_allowed_headers: The cors_allowed_headers of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: str
        """

        self._cors_allowed_headers = cors_allowed_headers

    @property
    def cors_exposed_headers(self):
        """Gets the cors_exposed_headers of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_exposed_headers of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: str
        """
        return self._cors_exposed_headers

    @cors_exposed_headers.setter
    def cors_exposed_headers(self, cors_exposed_headers):
        """Sets the cors_exposed_headers of this AppConfigurationCorsConfigurationFilters.


        :param cors_exposed_headers: The cors_exposed_headers of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: str
        """

        self._cors_exposed_headers = cors_exposed_headers

    @property
    def cors_support_credentials(self):
        """Gets the cors_support_credentials of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_support_credentials of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: bool
        """
        return self._cors_support_credentials

    @cors_support_credentials.setter
    def cors_support_credentials(self, cors_support_credentials):
        """Sets the cors_support_credentials of this AppConfigurationCorsConfigurationFilters.


        :param cors_support_credentials: The cors_support_credentials of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: bool
        """

        self._cors_support_credentials = cors_support_credentials

    @property
    def cors_logging_enabled(self):
        """Gets the cors_logging_enabled of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_logging_enabled of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: bool
        """
        return self._cors_logging_enabled

    @cors_logging_enabled.setter
    def cors_logging_enabled(self, cors_logging_enabled):
        """Sets the cors_logging_enabled of this AppConfigurationCorsConfigurationFilters.


        :param cors_logging_enabled: The cors_logging_enabled of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: bool
        """

        self._cors_logging_enabled = cors_logging_enabled

    @property
    def cors_preflight_max_age(self):
        """Gets the cors_preflight_max_age of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_preflight_max_age of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: int
        """
        return self._cors_preflight_max_age

    @cors_preflight_max_age.setter
    def cors_preflight_max_age(self, cors_preflight_max_age):
        """Sets the cors_preflight_max_age of this AppConfigurationCorsConfigurationFilters.


        :param cors_preflight_max_age: The cors_preflight_max_age of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: int
        """

        self._cors_preflight_max_age = cors_preflight_max_age

    @property
    def cors_request_decorate(self):
        """Gets the cors_request_decorate of this AppConfigurationCorsConfigurationFilters.  # noqa: E501


        :return: The cors_request_decorate of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :rtype: bool
        """
        return self._cors_request_decorate

    @cors_request_decorate.setter
    def cors_request_decorate(self, cors_request_decorate):
        """Sets the cors_request_decorate of this AppConfigurationCorsConfigurationFilters.


        :param cors_request_decorate: The cors_request_decorate of this AppConfigurationCorsConfigurationFilters.  # noqa: E501
        :type: bool
        """

        self._cors_request_decorate = cors_request_decorate

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
        if issubclass(AppConfigurationCorsConfigurationFilters, dict):
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
        if not isinstance(other, AppConfigurationCorsConfigurationFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
