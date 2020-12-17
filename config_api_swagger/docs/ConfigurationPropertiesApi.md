# swagger_client.ConfigurationPropertiesApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_properties**](ConfigurationPropertiesApi.md#get_properties) | **GET** /jans-config-api/api/v1/jans-auth-server/config | Gets all Jans authorization server configuration properties.
[**patch_properties**](ConfigurationPropertiesApi.md#patch_properties) | **PATCH** /jans-config-api/api/v1/jans-auth-server/config | Partially modifies Jans authorization server Application configuration properties.

# **get_properties**
> list[AppConfiguration] get_properties()

Gets all Jans authorization server configuration properties.

Gets all Jans authorization server configuration properties.

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
api_instance = swagger_client.ConfigurationPropertiesApi(swagger_client.ApiClient(configuration))

try:
    # Gets all Jans authorization server configuration properties.
    api_response = api_instance.get_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationPropertiesApi->get_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AppConfiguration]**](AppConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_properties**
> list[AppConfiguration] patch_properties(body=body)

Partially modifies Jans authorization server Application configuration properties.

Partially modifies Jans authorization server AppConfiguration properties.

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
api_instance = swagger_client.ConfigurationPropertiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchRequest() # PatchRequest |  (optional)

try:
    # Partially modifies Jans authorization server Application configuration properties.
    api_response = api_instance.patch_properties(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationPropertiesApi->patch_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchRequest**](PatchRequest.md)|  | [optional] 

### Return type

[**list[AppConfiguration]**](AppConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

