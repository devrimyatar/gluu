# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.configuration__properties_api import ConfigurationPropertiesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestConfigurationPropertiesApi(unittest.TestCase):
    """ConfigurationPropertiesApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationPropertiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_properties(self):
        """Test case for get_properties

        Gets all Jans authorization server configuration properties.  # noqa: E501
        """
        pass

    def test_patch_properties(self):
        """Test case for patch_properties

        Partially modifies Jans authorization server Application configuration properties.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
