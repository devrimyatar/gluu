# swagger_client.CacheConfigurationInMemoryApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_cache_in_memory**](CacheConfigurationInMemoryApi.md#get_config_cache_in_memory) | **GET** /jans-config-api/api/v1/config/cache/in-memory | Returns in-Memory cache configuration.
[**put_config_cache_in_memory**](CacheConfigurationInMemoryApi.md#put_config_cache_in_memory) | **PUT** /jans-config-api/api/v1/config/cache/in-memory | Updates in-Memory cache configuration.

# **get_config_cache_in_memory**
> InlineResponse2005 get_config_cache_in_memory()

Returns in-Memory cache configuration.

Returns in-Memory cache configuration.

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
api_instance = swagger_client.CacheConfigurationInMemoryApi(swagger_client.ApiClient(configuration))

try:
    # Returns in-Memory cache configuration.
    api_response = api_instance.get_config_cache_in_memory()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationInMemoryApi->get_config_cache_in_memory: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_cache_in_memory**
> Body2 put_config_cache_in_memory(body=body)

Updates in-Memory cache configuration.

Updates in-Memory cache configuration.

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
api_instance = swagger_client.CacheConfigurationInMemoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body2() # Body2 |  (optional)

try:
    # Updates in-Memory cache configuration.
    api_response = api_instance.put_config_cache_in_memory(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationInMemoryApi->put_config_cache_in_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**Body2**](Body2.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

