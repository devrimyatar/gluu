# swagger_client.CacheConfigurationMemcachedApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_cache_memcached**](CacheConfigurationMemcachedApi.md#get_config_cache_memcached) | **GET** /jans-config-api/api/v1/config/cache/memcached | Returns Memcached cache configuration.
[**put_config_cache_memcached**](CacheConfigurationMemcachedApi.md#put_config_cache_memcached) | **PUT** /jans-config-api/api/v1/config/cache/memcached | Updates Memcached cache configuration.

# **get_config_cache_memcached**
> MemcachedConfiguration get_config_cache_memcached()

Returns Memcached cache configuration.

Returns Memcached cache configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: jans-auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CacheConfigurationMemcachedApi(swagger_client.ApiClient(configuration))

try:
    # Returns Memcached cache configuration.
    api_response = api_instance.get_config_cache_memcached()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationMemcachedApi->get_config_cache_memcached: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MemcachedConfiguration**](MemcachedConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_cache_memcached**
> MemcachedConfiguration put_config_cache_memcached(body=body)

Updates Memcached cache configuration.

Updates Memcached cache configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: jans-auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CacheConfigurationMemcachedApi(swagger_client.ApiClient(configuration))
body = swagger_client.MemcachedConfiguration() # MemcachedConfiguration |  (optional)

try:
    # Updates Memcached cache configuration.
    api_response = api_instance.put_config_cache_memcached(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationMemcachedApi->put_config_cache_memcached: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MemcachedConfiguration**](MemcachedConfiguration.md)|  | [optional] 

### Return type

[**MemcachedConfiguration**](MemcachedConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

