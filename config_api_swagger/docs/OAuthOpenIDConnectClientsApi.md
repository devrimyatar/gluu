# swagger_client.OAuthOpenIDConnectClientsApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_oauth_openid_clients_by_inum**](OAuthOpenIDConnectClientsApi.md#delete_oauth_openid_clients_by_inum) | **DELETE** /jans-config-api/api/v1/openid/clients/{inum} | Delete OpenId Connect client.
[**get_oauth_openid_clients**](OAuthOpenIDConnectClientsApi.md#get_oauth_openid_clients) | **GET** /jans-config-api/api/v1/openid/clients | Gets list of OpenID Connect clients
[**get_oauth_openid_clients_by_inum**](OAuthOpenIDConnectClientsApi.md#get_oauth_openid_clients_by_inum) | **GET** /jans-config-api/api/v1/openid/clients/{inum} | Get OpenId Connect Client by Inum
[**patch_oauth_openid_clients_by_inum**](OAuthOpenIDConnectClientsApi.md#patch_oauth_openid_clients_by_inum) | **PATCH** /jans-config-api/api/v1/openid/clients/{inum} | Update modified properties of OpenId Connect client by Inum.
[**post_oauth_openid_clients**](OAuthOpenIDConnectClientsApi.md#post_oauth_openid_clients) | **POST** /jans-config-api/api/v1/openid/clients | Create new OpenId connect client
[**put_oauth_openid_clients**](OAuthOpenIDConnectClientsApi.md#put_oauth_openid_clients) | **PUT** /jans-config-api/api/v1/openid/clients | Update OpenId Connect client.

# **delete_oauth_openid_clients_by_inum**
> delete_oauth_openid_clients_by_inum(inum)

Delete OpenId Connect client.

Delete OpenId Connect client.

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
api_instance = swagger_client.OAuthOpenIDConnectClientsApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Client identifier

try:
    # Delete OpenId Connect client.
    api_instance.delete_oauth_openid_clients_by_inum(inum)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectClientsApi->delete_oauth_openid_clients_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Client identifier | 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_openid_clients**
> list[Client] get_oauth_openid_clients(limit=limit, pattern=pattern)

Gets list of OpenID Connect clients

Gets list of OpenID Connect clients

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
api_instance = swagger_client.OAuthOpenIDConnectClientsApi(swagger_client.ApiClient(configuration))
limit = 50 # int | Search size - max size of the results to return. (optional) (default to 50)
pattern = 'pattern_example' # str | Search pattern. (optional)

try:
    # Gets list of OpenID Connect clients
    api_response = api_instance.get_oauth_openid_clients(limit=limit, pattern=pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectClientsApi->get_oauth_openid_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Search size - max size of the results to return. | [optional] [default to 50]
 **pattern** | **str**| Search pattern. | [optional] 

### Return type

[**list[Client]**](Client.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_openid_clients_by_inum**
> Client get_oauth_openid_clients_by_inum(inum)

Get OpenId Connect Client by Inum

Get OpenId Connect Client by Inum.

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
api_instance = swagger_client.OAuthOpenIDConnectClientsApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Client identifier

try:
    # Get OpenId Connect Client by Inum
    api_response = api_instance.get_oauth_openid_clients_by_inum(inum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectClientsApi->get_oauth_openid_clients_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Client identifier | 

### Return type

[**Client**](Client.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_oauth_openid_clients_by_inum**
> Client patch_oauth_openid_clients_by_inum(inum, body=body)

Update modified properties of OpenId Connect client by Inum.

Update modified properties of OpenId Connect client by Inum.

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
api_instance = swagger_client.OAuthOpenIDConnectClientsApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Client identifier
body = [swagger_client.PatchRequest()] # list[PatchRequest] |  (optional)

try:
    # Update modified properties of OpenId Connect client by Inum.
    api_response = api_instance.patch_oauth_openid_clients_by_inum(inum, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectClientsApi->patch_oauth_openid_clients_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Client identifier | 
 **body** | [**list[PatchRequest]**](PatchRequest.md)|  | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_oauth_openid_clients**
> Client post_oauth_openid_clients(body=body)

Create new OpenId connect client

Create new OpenId connect client

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
api_instance = swagger_client.OAuthOpenIDConnectClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Client() # Client |  (optional)

try:
    # Create new OpenId connect client
    api_response = api_instance.post_oauth_openid_clients(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectClientsApi->post_oauth_openid_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Client**](Client.md)|  | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_oauth_openid_clients**
> Client put_oauth_openid_clients(body=body)

Update OpenId Connect client.

Update OpenId Connect client.

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
api_instance = swagger_client.OAuthOpenIDConnectClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Client() # Client |  (optional)

try:
    # Update OpenId Connect client.
    api_response = api_instance.put_oauth_openid_clients(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectClientsApi->put_oauth_openid_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Client**](Client.md)|  | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

