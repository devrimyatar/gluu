# swagger_client.ConfigurationLoggingApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_logging**](ConfigurationLoggingApi.md#get_config_logging) | **GET** /jans-config-api/api/v1/logging | Returns Jans Authorization Server logging settings.
[**put_config_logging**](ConfigurationLoggingApi.md#put_config_logging) | **PUT** /jans-config-api/api/v1/logging | Updates Jans Authorization Server logging settings.

# **get_config_logging**
> list[InlineResponse2009] get_config_logging()

Returns Jans Authorization Server logging settings.

Returns Jans Authorization Server logging settings.

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
api_instance = swagger_client.ConfigurationLoggingApi(swagger_client.ApiClient(configuration))

try:
    # Returns Jans Authorization Server logging settings.
    api_response = api_instance.get_config_logging()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationLoggingApi->get_config_logging: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2009]**](InlineResponse2009.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_logging**
> put_config_logging(body=body)

Updates Jans Authorization Server logging settings.

Updates Jans Authorization Server logging settings.

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
api_instance = swagger_client.ConfigurationLoggingApi(swagger_client.ApiClient(configuration))
body = [swagger_client.InlineResponse2009()] # list[InlineResponse2009] |  (optional)

try:
    # Updates Jans Authorization Server logging settings.
    api_instance.put_config_logging(body=body)
except ApiException as e:
    print("Exception when calling ConfigurationLoggingApi->put_config_logging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[InlineResponse2009]**](InlineResponse2009.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

