# swagger_client.CacheConfigurationApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_cache**](CacheConfigurationApi.md#get_config_cache) | **GET** /jans-config-api/api/v1/config/cache | Returns cache configuration.
[**patch_config_cache**](CacheConfigurationApi.md#patch_config_cache) | **PATCH** /jans-config-api/api/v1/config/cache | Partially modifies cache configuration.

# **get_config_cache**
> CacheConfiguration get_config_cache()

Returns cache configuration.

Returns cache configuration.

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
api_instance = swagger_client.CacheConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Returns cache configuration.
    api_response = api_instance.get_config_cache()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationApi->get_config_cache: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CacheConfiguration**](CacheConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_config_cache**
> CacheConfiguration patch_config_cache(body=body)

Partially modifies cache configuration.

Partially modifies cache configuration.

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
api_instance = swagger_client.CacheConfigurationApi(swagger_client.ApiClient(configuration))
body = [swagger_client.PatchRequest()] # list[PatchRequest] |  (optional)

try:
    # Partially modifies cache configuration.
    api_response = api_instance.patch_config_cache(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationApi->patch_config_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PatchRequest]**](PatchRequest.md)|  | [optional] 

### Return type

[**CacheConfiguration**](CacheConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

