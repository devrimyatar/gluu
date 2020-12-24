# swagger_client.OAuthOpenIDConnectSectorIdentifiersApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_oauth_openid_sectors_by_id**](OAuthOpenIDConnectSectorIdentifiersApi.md#delete_oauth_openid_sectors_by_id) | **DELETE** /jans-config-api/api/v1/openid/sectoridentifiers/{inum} | Delete OpenID Connect Sector.
[**get_oauth_openid_sectors**](OAuthOpenIDConnectSectorIdentifiersApi.md#get_oauth_openid_sectors) | **GET** /jans-config-api/api/v1/openid/sectoridentifiers | Gets list of OpenID Connect Sectors.
[**get_oauth_openid_sectors_by_id**](OAuthOpenIDConnectSectorIdentifiersApi.md#get_oauth_openid_sectors_by_id) | **GET** /jans-config-api/api/v1/openid/sectoridentifiers/{inum} | Get OpenID Connect Sector by Inum.
[**patch_oauth_openid_sectors_by_id**](OAuthOpenIDConnectSectorIdentifiersApi.md#patch_oauth_openid_sectors_by_id) | **PATCH** /jans-config-api/api/v1/openid/sectoridentifiers/{inum} | Partially update OpenId Connect Sector by Inum.
[**post_oauth_openid_sectors**](OAuthOpenIDConnectSectorIdentifiersApi.md#post_oauth_openid_sectors) | **POST** /jans-config-api/api/v1/openid/sectoridentifiers | Create new OpenID Connect Sector.
[**put_oauth_openid_sectors**](OAuthOpenIDConnectSectorIdentifiersApi.md#put_oauth_openid_sectors) | **PUT** /jans-config-api/api/v1/openid/sectoridentifiers | Update OpenId Connect Sector.

# **delete_oauth_openid_sectors_by_id**
> delete_oauth_openid_sectors_by_id(inum)

Delete OpenID Connect Sector.

Delete OpenID Connect Sector.

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
api_instance = swagger_client.OAuthOpenIDConnectSectorIdentifiersApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Scope ID.

try:
    # Delete OpenID Connect Sector.
    api_instance.delete_oauth_openid_sectors_by_id(inum)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectSectorIdentifiersApi->delete_oauth_openid_sectors_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Scope ID. | 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_openid_sectors**
> list[SectorIdentifier] get_oauth_openid_sectors()

Gets list of OpenID Connect Sectors.

Gets list of OpenID Connect Sectors.

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
api_instance = swagger_client.OAuthOpenIDConnectSectorIdentifiersApi(swagger_client.ApiClient(configuration))

try:
    # Gets list of OpenID Connect Sectors.
    api_response = api_instance.get_oauth_openid_sectors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectSectorIdentifiersApi->get_oauth_openid_sectors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SectorIdentifier]**](SectorIdentifier.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_openid_sectors_by_id**
> SectorIdentifier get_oauth_openid_sectors_by_id(inum)

Get OpenID Connect Sector by Inum.

Get OpenID Connect Sector by Inum.

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
api_instance = swagger_client.OAuthOpenIDConnectSectorIdentifiersApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Scope ID.

try:
    # Get OpenID Connect Sector by Inum.
    api_response = api_instance.get_oauth_openid_sectors_by_id(inum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectSectorIdentifiersApi->get_oauth_openid_sectors_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Scope ID. | 

### Return type

[**SectorIdentifier**](SectorIdentifier.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_oauth_openid_sectors_by_id**
> SectorIdentifier patch_oauth_openid_sectors_by_id(inum, body=body)

Partially update OpenId Connect Sector by Inum.

Partially update OpenId Connect Sector by Inum.

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
api_instance = swagger_client.OAuthOpenIDConnectSectorIdentifiersApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Scope ID.
body = [swagger_client.PatchRequest()] # list[PatchRequest] |  (optional)

try:
    # Partially update OpenId Connect Sector by Inum.
    api_response = api_instance.patch_oauth_openid_sectors_by_id(inum, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectSectorIdentifiersApi->patch_oauth_openid_sectors_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Scope ID. | 
 **body** | [**list[PatchRequest]**](PatchRequest.md)|  | [optional] 

### Return type

[**SectorIdentifier**](SectorIdentifier.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_oauth_openid_sectors**
> SectorIdentifier post_oauth_openid_sectors(body=body)

Create new OpenID Connect Sector.

Create new OpenID Connect Sector.

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
api_instance = swagger_client.OAuthOpenIDConnectSectorIdentifiersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SectorIdentifier() # SectorIdentifier |  (optional)

try:
    # Create new OpenID Connect Sector.
    api_response = api_instance.post_oauth_openid_sectors(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectSectorIdentifiersApi->post_oauth_openid_sectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SectorIdentifier**](SectorIdentifier.md)|  | [optional] 

### Return type

[**SectorIdentifier**](SectorIdentifier.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_oauth_openid_sectors**
> SectorIdentifier put_oauth_openid_sectors(body=body)

Update OpenId Connect Sector.

Update OpenId Connect Sector.

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
api_instance = swagger_client.OAuthOpenIDConnectSectorIdentifiersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SectorIdentifier() # SectorIdentifier |  (optional)

try:
    # Update OpenId Connect Sector.
    api_response = api_instance.put_oauth_openid_sectors(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthOpenIDConnectSectorIdentifiersApi->put_oauth_openid_sectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SectorIdentifier**](SectorIdentifier.md)|  | [optional] 

### Return type

[**SectorIdentifier**](SectorIdentifier.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

