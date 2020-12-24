# swagger_client.ConfigurationFido2Api

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_properties_fido2**](ConfigurationFido2Api.md#get_properties_fido2) | **GET** /jans-config-api/api/v1/fido2/config | Gets Jans Authorization Server Fido2 configuration properties.
[**put_properties_fido2**](ConfigurationFido2Api.md#put_properties_fido2) | **PUT** /jans-config-api/api/v1/fido2/config | Updates Fido2 configuration properties.

# **get_properties_fido2**
> JansFido2DynConfiguration get_properties_fido2()

Gets Jans Authorization Server Fido2 configuration properties.

Gets Jans Authorization Server Fido2 configuration properties.

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
api_instance = swagger_client.ConfigurationFido2Api(swagger_client.ApiClient(configuration))

try:
    # Gets Jans Authorization Server Fido2 configuration properties.
    api_response = api_instance.get_properties_fido2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationFido2Api->get_properties_fido2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JansFido2DynConfiguration**](JansFido2DynConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_properties_fido2**
> put_properties_fido2(body=body)

Updates Fido2 configuration properties.

Updates Fido2 configuration properties.

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
api_instance = swagger_client.ConfigurationFido2Api(swagger_client.ApiClient(configuration))
body = swagger_client.JansFido2DynConfiguration() # JansFido2DynConfiguration |  (optional)

try:
    # Updates Fido2 configuration properties.
    api_instance.put_properties_fido2(body=body)
except ApiException as e:
    print("Exception when calling ConfigurationFido2Api->put_properties_fido2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JansFido2DynConfiguration**](JansFido2DynConfiguration.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

