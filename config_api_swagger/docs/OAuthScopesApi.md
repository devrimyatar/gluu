# swagger_client.OAuthScopesApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_oauth_scopes_by_id**](OAuthScopesApi.md#delete_oauth_scopes_by_id) | **DELETE** /jans-config-api/api/v1/scopes/{inum} | Delete Scope.
[**get_oauth_scopes**](OAuthScopesApi.md#get_oauth_scopes) | **GET** /jans-config-api/api/v1/scopes | Gets list of Scopes.
[**get_oauth_scopes_by_inum**](OAuthScopesApi.md#get_oauth_scopes_by_inum) | **GET** /jans-config-api/api/v1/scopes/{inum} | Get Scope by Inum
[**patch_oauth_scopes_by_id**](OAuthScopesApi.md#patch_oauth_scopes_by_id) | **PATCH** /jans-config-api/api/v1/scopes/{inum} | Update modified attributes of existing Scope by Inum.
[**post_oauth_scopes**](OAuthScopesApi.md#post_oauth_scopes) | **POST** /jans-config-api/api/v1/scopes | Create Scope.
[**put_oauth_scopes**](OAuthScopesApi.md#put_oauth_scopes) | **PUT** /jans-config-api/api/v1/scopes | Updates existing Scope.

# **delete_oauth_scopes_by_id**
> delete_oauth_scopes_by_id(inum)

Delete Scope.

Delete Scope.

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
api_instance = swagger_client.OAuthScopesApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | 

try:
    # Delete Scope.
    api_instance.delete_oauth_scopes_by_id(inum)
except ApiException as e:
    print("Exception when calling OAuthScopesApi->delete_oauth_scopes_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_scopes**
> list[Scope] get_oauth_scopes(type=type, limit=limit, pattern=pattern)

Gets list of Scopes.

Gets list of Scopes. Optionally type to filter the scope, max-size of the result and pattern can be provided.

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
api_instance = swagger_client.OAuthScopesApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Scope type. (optional)
limit = 50 # int | Search size - max size of the results to return. (optional) (default to 50)
pattern = 'pattern_example' # str | Search pattern. (optional)

try:
    # Gets list of Scopes.
    api_response = api_instance.get_oauth_scopes(type=type, limit=limit, pattern=pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthScopesApi->get_oauth_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Scope type. | [optional] 
 **limit** | **int**| Search size - max size of the results to return. | [optional] [default to 50]
 **pattern** | **str**| Search pattern. | [optional] 

### Return type

[**list[Scope]**](Scope.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_scopes_by_inum**
> Scope get_oauth_scopes_by_inum(inum)

Get Scope by Inum

Get Scope by Inum

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
api_instance = swagger_client.OAuthScopesApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | 

try:
    # Get Scope by Inum
    api_response = api_instance.get_oauth_scopes_by_inum(inum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthScopesApi->get_oauth_scopes_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**|  | 

### Return type

[**Scope**](Scope.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_oauth_scopes_by_id**
> Scope patch_oauth_scopes_by_id(inum, body=body)

Update modified attributes of existing Scope by Inum.

Update modified attributes of existing Scope by Inum.

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
api_instance = swagger_client.OAuthScopesApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | 
body = [swagger_client.PatchRequest()] # list[PatchRequest] |  (optional)

try:
    # Update modified attributes of existing Scope by Inum.
    api_response = api_instance.patch_oauth_scopes_by_id(inum, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthScopesApi->patch_oauth_scopes_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**|  | 
 **body** | [**list[PatchRequest]**](PatchRequest.md)|  | [optional] 

### Return type

[**Scope**](Scope.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_oauth_scopes**
> Scope post_oauth_scopes(body=body)

Create Scope.

Create Scope.

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
api_instance = swagger_client.OAuthScopesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Scope() # Scope |  (optional)

try:
    # Create Scope.
    api_response = api_instance.post_oauth_scopes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthScopesApi->post_oauth_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scope**](Scope.md)|  | [optional] 

### Return type

[**Scope**](Scope.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_oauth_scopes**
> Scope put_oauth_scopes(body=body)

Updates existing Scope.

Updates existing Scope.

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
api_instance = swagger_client.OAuthScopesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Scope() # Scope |  (optional)

try:
    # Updates existing Scope.
    api_response = api_instance.put_oauth_scopes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthScopesApi->put_oauth_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scope**](Scope.md)|  | [optional] 

### Return type

[**Scope**](Scope.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

