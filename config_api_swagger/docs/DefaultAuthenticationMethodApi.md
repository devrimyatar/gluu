# swagger_client.DefaultAuthenticationMethodApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_acrs**](DefaultAuthenticationMethodApi.md#get_acrs) | **GET** /jans-config-api/api/v1/acrs | Gets default authentication method.
[**put_acrs**](DefaultAuthenticationMethodApi.md#put_acrs) | **PUT** /jans-config-api/api/v1/acrs | Updates default authentication method.

# **get_acrs**
> AuthenticationMethod get_acrs()

Gets default authentication method.

Gets default authentication method.

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
api_instance = swagger_client.DefaultAuthenticationMethodApi(swagger_client.ApiClient(configuration))

try:
    # Gets default authentication method.
    api_response = api_instance.get_acrs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultAuthenticationMethodApi->get_acrs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationMethod**](AuthenticationMethod.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_acrs**
> put_acrs(body=body)

Updates default authentication method.

Updates default authentication method.

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
api_instance = swagger_client.DefaultAuthenticationMethodApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthenticationMethod1() # AuthenticationMethod1 |  (optional)

try:
    # Updates default authentication method.
    api_instance.put_acrs(body=body)
except ApiException as e:
    print("Exception when calling DefaultAuthenticationMethodApi->put_acrs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationMethod1**](AuthenticationMethod1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

