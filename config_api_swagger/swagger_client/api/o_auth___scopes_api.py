# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class OAuthScopesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_oauth_scopes_by_id(self, inum, **kwargs):  # noqa: E501
        """Delete Scope.  # noqa: E501

        Delete Scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_oauth_scopes_by_id(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_oauth_scopes_by_id_with_http_info(inum, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_oauth_scopes_by_id_with_http_info(inum, **kwargs)  # noqa: E501
            return data

    def delete_oauth_scopes_by_id_with_http_info(self, inum, **kwargs):  # noqa: E501
        """Delete Scope.  # noqa: E501

        Delete Scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_oauth_scopes_by_id_with_http_info(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_oauth_scopes_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inum' is set
        if ('inum' not in params or
                params['inum'] is None):
            raise ValueError("Missing the required parameter `inum` when calling `delete_oauth_scopes_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inum' in params:
            path_params['inum'] = params['inum']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/scopes/{inum}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_oauth_scopes(self, **kwargs):  # noqa: E501
        """Gets list of Scopes.  # noqa: E501

        Gets list of Scopes. Optionally type to filter the scope, max-size of the result and pattern can be provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_oauth_scopes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Scope type.
        :param int limit: Search size - max size of the results to return.
        :param str pattern: Search pattern.
        :return: list[Scope]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_oauth_scopes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_oauth_scopes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_oauth_scopes_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of Scopes.  # noqa: E501

        Gets list of Scopes. Optionally type to filter the scope, max-size of the result and pattern can be provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_oauth_scopes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Scope type.
        :param int limit: Search size - max size of the results to return.
        :param str pattern: Search pattern.
        :return: list[Scope]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'limit', 'pattern']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_oauth_scopes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'pattern' in params:
            query_params.append(('pattern', params['pattern']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/scopes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Scope]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_oauth_scopes_by_inum(self, inum, **kwargs):  # noqa: E501
        """Get Scope by Inum  # noqa: E501

        Get Scope by Inum  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_oauth_scopes_by_inum(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: (required)
        :return: Scope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_oauth_scopes_by_inum_with_http_info(inum, **kwargs)  # noqa: E501
        else:
            (data) = self.get_oauth_scopes_by_inum_with_http_info(inum, **kwargs)  # noqa: E501
            return data

    def get_oauth_scopes_by_inum_with_http_info(self, inum, **kwargs):  # noqa: E501
        """Get Scope by Inum  # noqa: E501

        Get Scope by Inum  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_oauth_scopes_by_inum_with_http_info(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: (required)
        :return: Scope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_oauth_scopes_by_inum" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inum' is set
        if ('inum' not in params or
                params['inum'] is None):
            raise ValueError("Missing the required parameter `inum` when calling `get_oauth_scopes_by_inum`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inum' in params:
            path_params['inum'] = params['inum']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/scopes/{inum}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Scope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_oauth_scopes_by_id(self, inum, **kwargs):  # noqa: E501
        """Update modified attributes of existing Scope by Inum.  # noqa: E501

        Update modified attributes of existing Scope by Inum.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_oauth_scopes_by_id(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: (required)
        :param PatchRequest body:
        :return: Scope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_oauth_scopes_by_id_with_http_info(inum, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_oauth_scopes_by_id_with_http_info(inum, **kwargs)  # noqa: E501
            return data

    def patch_oauth_scopes_by_id_with_http_info(self, inum, **kwargs):  # noqa: E501
        """Update modified attributes of existing Scope by Inum.  # noqa: E501

        Update modified attributes of existing Scope by Inum.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_oauth_scopes_by_id_with_http_info(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: (required)
        :param PatchRequest body:
        :return: Scope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inum', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_oauth_scopes_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inum' is set
        if ('inum' not in params or
                params['inum'] is None):
            raise ValueError("Missing the required parameter `inum` when calling `patch_oauth_scopes_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inum' in params:
            path_params['inum'] = params['inum']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/scopes/{inum}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Scope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_oauth_scopes(self, **kwargs):  # noqa: E501
        """Create Scope.  # noqa: E501

        Create Scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_oauth_scopes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scope body:
        :return: Scope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_oauth_scopes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_oauth_scopes_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_oauth_scopes_with_http_info(self, **kwargs):  # noqa: E501
        """Create Scope.  # noqa: E501

        Create Scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_oauth_scopes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scope body:
        :return: Scope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_oauth_scopes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/scopes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Scope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_oauth_scopes(self, **kwargs):  # noqa: E501
        """Updates existing Scope.  # noqa: E501

        Updates existing Scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_oauth_scopes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scope body:
        :return: Scope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_oauth_scopes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.put_oauth_scopes_with_http_info(**kwargs)  # noqa: E501
            return data

    def put_oauth_scopes_with_http_info(self, **kwargs):  # noqa: E501
        """Updates existing Scope.  # noqa: E501

        Updates existing Scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_oauth_scopes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scope body:
        :return: Scope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_oauth_scopes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/scopes', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Scope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
