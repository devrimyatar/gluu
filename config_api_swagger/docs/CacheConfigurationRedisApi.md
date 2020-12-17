# swagger_client.CacheConfigurationRedisApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_cache_redis**](CacheConfigurationRedisApi.md#get_config_cache_redis) | **GET** /jans-config-api/api/v1/config/cache/redis | Returns Redis cache configuration.
[**put_config_cache_redis**](CacheConfigurationRedisApi.md#put_config_cache_redis) | **PUT** /jans-config-api/api/v1/config/cache/redis | Updates Redis cache configuration.

# **get_config_cache_redis**
> InlineResponse2004 get_config_cache_redis()

Returns Redis cache configuration.

Returns Redis cache configuration.

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
api_instance = swagger_client.CacheConfigurationRedisApi(swagger_client.ApiClient(configuration))

try:
    # Returns Redis cache configuration.
    api_response = api_instance.get_config_cache_redis()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationRedisApi->get_config_cache_redis: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_cache_redis**
> Body1 put_config_cache_redis(body=body)

Updates Redis cache configuration.

Updates Redis cache configuration.

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
api_instance = swagger_client.CacheConfigurationRedisApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body1() # Body1 |  (optional)

try:
    # Updates Redis cache configuration.
    api_response = api_instance.put_config_cache_redis(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheConfigurationRedisApi->put_config_cache_redis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**Body1**](Body1.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

