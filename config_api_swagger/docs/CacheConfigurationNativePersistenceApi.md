# swagger_client.CacheConfigurationNativePersistenceApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_cache_native_persistence**](CacheConfigurationNativePersistenceApi.md#get_config_cache_native_persistence) | **GET** /jans-config-api/api/v1/config/cache/native-persistence | Returns native persistence cache configuration.
[**put_config_cache_native_persistence**](CacheConfigurationNativePersistenceApi.md#put_config_cache_native_persistence) | **PUT** /jans-config-api/api/v1/config/cache/native-persistence | Updates native persistence cache configuration.

# **get_config_cache_native_persistence**
> NativePersistenceConfiguration get_config_cache_native_persistence()

Returns native persistence cache configuration.

Returns native persistence cache configuration.

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
api_instance = swagger_client.CacheConfigurationNativePersistenceApi(swagger_client.ApiClient(configuration))

try:
    # Returns native persistence cache configuration.
    api_response = api_instance.get_config_cache_native_persistence()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationNativePersistenceApi->get_config_cache_native_persistence: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NativePersistenceConfiguration**](NativePersistenceConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_cache_native_persistence**
> NativePersistenceConfiguration put_config_cache_native_persistence(body=body)

Updates native persistence cache configuration.

Updates native persistence cache configuration.

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
api_instance = swagger_client.CacheConfigurationNativePersistenceApi(swagger_client.ApiClient(configuration))
body = swagger_client.NativePersistenceConfiguration() # NativePersistenceConfiguration |  (optional)

try:
    # Updates native persistence cache configuration.
    api_response = api_instance.put_config_cache_native_persistence(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationNativePersistenceApi->put_config_cache_native_persistence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NativePersistenceConfiguration**](NativePersistenceConfiguration.md)|  | [optional] 

### Return type

[**NativePersistenceConfiguration**](NativePersistenceConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

