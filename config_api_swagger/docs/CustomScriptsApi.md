# swagger_client.CustomScriptsApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_config_scripts_by_inum**](CustomScriptsApi.md#delete_config_scripts_by_inum) | **DELETE** /jans-config-api/api/v1/config/scripts/{inum} | Deletes a custom script.
[**get_config_scripts**](CustomScriptsApi.md#get_config_scripts) | **GET** /jans-config-api/api/v1/config/scripts | Gets a list of custom scripts.
[**get_config_scripts_by_inum**](CustomScriptsApi.md#get_config_scripts_by_inum) | **GET** /jans-config-api/api/v1/config/scripts/inum/{inum} | Gets a script by Inum.
[**get_config_scripts_by_type**](CustomScriptsApi.md#get_config_scripts_by_type) | **GET** /jans-config-api/api/v1/config/scripts/type/{type} | Gets list of scripts by type.
[**post_config_scripts**](CustomScriptsApi.md#post_config_scripts) | **POST** /jans-config-api/api/v1/config/scripts | Adds a new custom script.
[**put_config_scripts**](CustomScriptsApi.md#put_config_scripts) | **PUT** /jans-config-api/api/v1/config/scripts | Updates a custom script.

# **delete_config_scripts_by_inum**
> delete_config_scripts_by_inum(inum)

Deletes a custom script.

Deletes a custom script.

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
api_instance = swagger_client.CustomScriptsApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Script identifier.

try:
    # Deletes a custom script.
    api_instance.delete_config_scripts_by_inum(inum)
except ApiException as e:
    print("Exception when calling CustomScriptsApi->delete_config_scripts_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Script identifier. | 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_scripts**
> list[CustomScript] get_config_scripts()

Gets a list of custom scripts.

Gets a list of custom scripts.

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
api_instance = swagger_client.CustomScriptsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of custom scripts.
    api_response = api_instance.get_config_scripts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomScriptsApi->get_config_scripts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomScript]**](CustomScript.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_scripts_by_inum**
> CustomScript get_config_scripts_by_inum(inum)

Gets a script by Inum.

Gets a script by Inum.

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
api_instance = swagger_client.CustomScriptsApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Script identifier.

try:
    # Gets a script by Inum.
    api_response = api_instance.get_config_scripts_by_inum(inum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomScriptsApi->get_config_scripts_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Script identifier. | 

### Return type

[**CustomScript**](CustomScript.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_scripts_by_type**
> list[CustomScript] get_config_scripts_by_type(type, pattern=pattern, limit=limit)

Gets list of scripts by type.

Gets list of scripts by type.

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
api_instance = swagger_client.CustomScriptsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Script type.
pattern = 'pattern_example' # str | Search pattern. (optional)
limit = 50 # int | Search size - max size of the results to return. (optional) (default to 50)

try:
    # Gets list of scripts by type.
    api_response = api_instance.get_config_scripts_by_type(type, pattern=pattern, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomScriptsApi->get_config_scripts_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Script type. | 
 **pattern** | **str**| Search pattern. | [optional] 
 **limit** | **int**| Search size - max size of the results to return. | [optional] [default to 50]

### Return type

[**list[CustomScript]**](CustomScript.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_config_scripts**
> CustomScript post_config_scripts()

Adds a new custom script.

Adds a new custom script.

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
api_instance = swagger_client.CustomScriptsApi(swagger_client.ApiClient(configuration))

try:
    # Adds a new custom script.
    api_response = api_instance.post_config_scripts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomScriptsApi->post_config_scripts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomScript**](CustomScript.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_scripts**
> put_config_scripts(body=body)

Updates a custom script.

Updates a custom script.

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
api_instance = swagger_client.CustomScriptsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.CustomScript()] # list[CustomScript] |  (optional)

try:
    # Updates a custom script.
    api_instance.put_config_scripts(body=body)
except ApiException as e:
    print("Exception when calling CustomScriptsApi->put_config_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CustomScript]**](CustomScript.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

