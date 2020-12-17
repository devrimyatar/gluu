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
from swagger_client.api.o_auth___scopes_api import OAuthScopesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOAuthScopesApi(unittest.TestCase):
    """OAuthScopesApi unit test stubs"""

    def setUp(self):
        self.api = OAuthScopesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_oauth_scopes_by_id(self):
        """Test case for delete_oauth_scopes_by_id

        Delete Scope.  # noqa: E501
        """
        pass

    def test_get_oauth_scopes(self):
        """Test case for get_oauth_scopes

        Gets list of Scopes.  # noqa: E501
        """
        pass

    def test_get_oauth_scopes_by_inum(self):
        """Test case for get_oauth_scopes_by_inum

        Get Scope by Inum  # noqa: E501
        """
        pass

    def test_patch_oauth_scopes_by_id(self):
        """Test case for patch_oauth_scopes_by_id

        Update modified attributes of existing Scope by Inum.  # noqa: E501
        """
        pass

    def test_post_oauth_scopes(self):
        """Test case for post_oauth_scopes

        Create Scope.  # noqa: E501
        """
        pass

    def test_put_oauth_scopes(self):
        """Test case for put_oauth_scopes

        Updates existing Scope.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
