# swagger_client.OAuthUMAResourcesApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_oauth_uma_resources_by_id**](OAuthUMAResourcesApi.md#delete_oauth_uma_resources_by_id) | **DELETE** /jans-config-api/api/v1/uma/resources/{id} | Deletes an UMA resource.
[**get_oauth_uma_resources**](OAuthUMAResourcesApi.md#get_oauth_uma_resources) | **GET** /jans-config-api/api/v1/uma/resources | Gets list of UMA resources.
[**get_oauth_uma_resources_by_id**](OAuthUMAResourcesApi.md#get_oauth_uma_resources_by_id) | **GET** /jans-config-api/api/v1/uma/resources/{id} | Gets an UMA resource by ID.
[**patch_oauth_uma_resources_by_id**](OAuthUMAResourcesApi.md#patch_oauth_uma_resources_by_id) | **PATCH** /jans-config-api/api/v1/uma/resources/{id} | Partially updates an UMA resource by Inum.
[**post_oauth_uma_resources**](OAuthUMAResourcesApi.md#post_oauth_uma_resources) | **POST** /jans-config-api/api/v1/uma/resources | Creates an UMA resource.
[**put_oauth_uma_resources**](OAuthUMAResourcesApi.md#put_oauth_uma_resources) | **PUT** /jans-config-api/api/v1/uma/resources | Updates an UMA resource.

# **delete_oauth_uma_resources_by_id**
> delete_oauth_uma_resources_by_id(id)

Deletes an UMA resource.

Deletes an UMA resource.

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
api_instance = swagger_client.OAuthUMAResourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Resource description ID.

try:
    # Deletes an UMA resource.
    api_instance.delete_oauth_uma_resources_by_id(id)
except ApiException as e:
    print("Exception when calling OAuthUMAResourcesApi->delete_oauth_uma_resources_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Resource description ID. | 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_uma_resources**
> list[InlineResponse20014] get_oauth_uma_resources(limit=limit, pattern=pattern)

Gets list of UMA resources.

Gets list of UMA resources.

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
api_instance = swagger_client.OAuthUMAResourcesApi(swagger_client.ApiClient(configuration))
limit = 50 # int | Search size - max size of the results to return. (optional) (default to 50)
pattern = 'pattern_example' # str | Search pattern. (optional)

try:
    # Gets list of UMA resources.
    api_response = api_instance.get_oauth_uma_resources(limit=limit, pattern=pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthUMAResourcesApi->get_oauth_uma_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Search size - max size of the results to return. | [optional] [default to 50]
 **pattern** | **str**| Search pattern. | [optional] 

### Return type

[**list[InlineResponse20014]**](InlineResponse20014.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_uma_resources_by_id**
> UMAResource1 get_oauth_uma_resources_by_id(id)

Gets an UMA resource by ID.

Gets an UMA resource by ID.

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
api_instance = swagger_client.OAuthUMAResourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Resource description ID.

try:
    # Gets an UMA resource by ID.
    api_response = api_instance.get_oauth_uma_resources_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthUMAResourcesApi->get_oauth_uma_resources_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Resource description ID. | 

### Return type

[**UMAResource1**](UMAResource1.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_oauth_uma_resources_by_id**
> UMAResource1 patch_oauth_uma_resources_by_id(id, body=body)

Partially updates an UMA resource by Inum.

Partially updates an UMA resource by Inum.

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
api_instance = swagger_client.OAuthUMAResourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Resource description ID.
body = swagger_client.PatchRequest() # PatchRequest |  (optional)

try:
    # Partially updates an UMA resource by Inum.
    api_response = api_instance.patch_oauth_uma_resources_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthUMAResourcesApi->patch_oauth_uma_resources_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Resource description ID. | 
 **body** | [**PatchRequest**](PatchRequest.md)|  | [optional] 

### Return type

[**UMAResource1**](UMAResource1.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_oauth_uma_resources**
> UMAResource1 post_oauth_uma_resources(body=body)

Creates an UMA resource.

Creates an UMA resource.

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
api_instance = swagger_client.OAuthUMAResourcesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UMAResource1() # UMAResource1 |  (optional)

try:
    # Creates an UMA resource.
    api_response = api_instance.post_oauth_uma_resources(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthUMAResourcesApi->post_oauth_uma_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UMAResource1**](UMAResource1.md)|  | [optional] 

### Return type

[**UMAResource1**](UMAResource1.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_oauth_uma_resources**
> UMAResource put_oauth_uma_resources(body=body)

Updates an UMA resource.

Updates an UMA resource.

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
api_instance = swagger_client.OAuthUMAResourcesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UMAResource() # UMAResource |  (optional)

try:
    # Updates an UMA resource.
    api_response = api_instance.put_oauth_uma_resources(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthUMAResourcesApi->put_oauth_uma_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UMAResource**](UMAResource.md)|  | [optional] 

### Return type

[**UMAResource**](UMAResource.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

