# swagger_client.ConfigurationJWKJSONWebKeyJWKApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_jwks**](ConfigurationJWKJSONWebKeyJWKApi.md#get_config_jwks) | **GET** /jans-config-api/api/v1/config/jwks | Gets list of JSON Web Key (JWK) used by server.
[**patch_config_jwks**](ConfigurationJWKJSONWebKeyJWKApi.md#patch_config_jwks) | **PATCH** /jans-config-api/api/v1/config/jwks | Patch JWKS
[**put_config_jwks**](ConfigurationJWKJSONWebKeyJWKApi.md#put_config_jwks) | **PUT** /jans-config-api/api/v1/config/jwks | Puts/replaces JWKS

# **get_config_jwks**
> WebKeysConfiguration get_config_jwks()

Gets list of JSON Web Key (JWK) used by server.

Gets list of JSON Web Key (JWK) used by server. JWK is a JSON data structure that represents a set of public keys as a JSON object [RFC4627].

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
api_instance = swagger_client.ConfigurationJWKJSONWebKeyJWKApi(swagger_client.ApiClient(configuration))

try:
    # Gets list of JSON Web Key (JWK) used by server.
    api_response = api_instance.get_config_jwks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationJWKJSONWebKeyJWKApi->get_config_jwks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebKeysConfiguration**](WebKeysConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_config_jwks**
> patch_config_jwks(body=body)

Patch JWKS

Patch JSON Web Keys (JWKS).

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
api_instance = swagger_client.ConfigurationJWKJSONWebKeyJWKApi(swagger_client.ApiClient(configuration))
body = [swagger_client.PatchRequest()] # list[PatchRequest] |  (optional)

try:
    # Patch JWKS
    api_instance.patch_config_jwks(body=body)
except ApiException as e:
    print("Exception when calling ConfigurationJWKJSONWebKeyJWKApi->patch_config_jwks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PatchRequest]**](PatchRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_jwks**
> put_config_jwks(body=body)

Puts/replaces JWKS

Puts/replaces JSON Web Keys (JWKS).

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
api_instance = swagger_client.ConfigurationJWKJSONWebKeyJWKApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebKeysConfiguration() # WebKeysConfiguration |  (optional)

try:
    # Puts/replaces JWKS
    api_instance.put_config_jwks(body=body)
except ApiException as e:
    print("Exception when calling ConfigurationJWKJSONWebKeyJWKApi->put_config_jwks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebKeysConfiguration**](WebKeysConfiguration.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

