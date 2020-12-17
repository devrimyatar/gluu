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
from swagger_client.api.cache_configuration__redis_api import CacheConfigurationRedisApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCacheConfigurationRedisApi(unittest.TestCase):
    """CacheConfigurationRedisApi unit test stubs"""

    def setUp(self):
        self.api = CacheConfigurationRedisApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_config_cache_redis(self):
        """Test case for get_config_cache_redis

        Returns Redis cache configuration.  # noqa: E501
        """
        pass

    def test_put_config_cache_redis(self):
        """Test case for put_config_cache_redis

        Updates Redis cache configuration.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
