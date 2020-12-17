# swagger_client.DatabaseLDAPConfigurationApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_config_database_ldap_by_name**](DatabaseLDAPConfigurationApi.md#delete_config_database_ldap_by_name) | **DELETE** /jans-config-api/api/v1/config/database/ldap/{name} | Deletes an LDAP configuration.
[**get_config_database_ldap**](DatabaseLDAPConfigurationApi.md#get_config_database_ldap) | **GET** /jans-config-api/api/v1/config/database/ldap | Gets list of existing LDAP configurations.
[**get_config_database_ldap_by_name**](DatabaseLDAPConfigurationApi.md#get_config_database_ldap_by_name) | **GET** /jans-config-api/api/v1/config/database/ldap/{name} | Gets an LDAP configuration by name.
[**patch_config_database_ldap_by_name**](DatabaseLDAPConfigurationApi.md#patch_config_database_ldap_by_name) | **PATCH** /jans-config-api/api/v1/config/database/ldap/{name} | Partially modify an LDAP configuration.
[**post_config_database_ldap**](DatabaseLDAPConfigurationApi.md#post_config_database_ldap) | **POST** /jans-config-api/api/v1/config/database/ldap | Adds a new LDAP configuration.
[**post_config_database_ldap_test**](DatabaseLDAPConfigurationApi.md#post_config_database_ldap_test) | **POST** /jans-config-api/api/v1/config/database/ldap/test | Tests a LDAP configurations by name.
[**put_config_database_ldap**](DatabaseLDAPConfigurationApi.md#put_config_database_ldap) | **PUT** /jans-config-api/api/v1/config/database/ldap | Updates LDAP configuration.

# **delete_config_database_ldap_by_name**
> delete_config_database_ldap_by_name(name)

Deletes an LDAP configuration.

Deletes an LDAP configuration.

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
api_instance = swagger_client.DatabaseLDAPConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of LDAP configuration.

try:
    # Deletes an LDAP configuration.
    api_instance.delete_config_database_ldap_by_name(name)
except ApiException as e:
    print("Exception when calling DatabaseLDAPConfigurationApi->delete_config_database_ldap_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of LDAP configuration. | 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_database_ldap**
> list[LdapConfiguration] get_config_database_ldap()

Gets list of existing LDAP configurations.

Gets list of existing LDAP configurations.

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
api_instance = swagger_client.DatabaseLDAPConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Gets list of existing LDAP configurations.
    api_response = api_instance.get_config_database_ldap()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseLDAPConfigurationApi->get_config_database_ldap: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LdapConfiguration]**](LdapConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_database_ldap_by_name**
> LdapConfiguration get_config_database_ldap_by_name(name)

Gets an LDAP configuration by name.

Gets an LDAP configuration by name.

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
api_instance = swagger_client.DatabaseLDAPConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of LDAP configuration.

try:
    # Gets an LDAP configuration by name.
    api_response = api_instance.get_config_database_ldap_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseLDAPConfigurationApi->get_config_database_ldap_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of LDAP configuration. | 

### Return type

[**LdapConfiguration**](LdapConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_config_database_ldap_by_name**
> LdapConfiguration patch_config_database_ldap_by_name(name, body=body)

Partially modify an LDAP configuration.

Partially modify an LDAP configuration.

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
api_instance = swagger_client.DatabaseLDAPConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of LDAP configuration.
body = swagger_client.PatchRequest() # PatchRequest |  (optional)

try:
    # Partially modify an LDAP configuration.
    api_response = api_instance.patch_config_database_ldap_by_name(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseLDAPConfigurationApi->patch_config_database_ldap_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of LDAP configuration. | 
 **body** | [**PatchRequest**](PatchRequest.md)|  | [optional] 

### Return type

[**LdapConfiguration**](LdapConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_config_database_ldap**
> LdapConfiguration post_config_database_ldap(body)

Adds a new LDAP configuration.

Adds a new LDAP configuration.

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
api_instance = swagger_client.DatabaseLDAPConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.LdapConfiguration() # LdapConfiguration | 

try:
    # Adds a new LDAP configuration.
    api_response = api_instance.post_config_database_ldap(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseLDAPConfigurationApi->post_config_database_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapConfiguration**](LdapConfiguration.md)|  | 

### Return type

[**LdapConfiguration**](LdapConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_config_database_ldap_test**
> bool post_config_database_ldap_test(body)

Tests a LDAP configurations by name.

Tests a LDAP configurations by name.

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
api_instance = swagger_client.DatabaseLDAPConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.LdapConfiguration() # LdapConfiguration | 

try:
    # Tests a LDAP configurations by name.
    api_response = api_instance.post_config_database_ldap_test(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseLDAPConfigurationApi->post_config_database_ldap_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapConfiguration**](LdapConfiguration.md)|  | 

### Return type

**bool**

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_database_ldap**
> LdapConfiguration put_config_database_ldap(body)

Updates LDAP configuration.

Updates LDAP configuration.

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
api_instance = swagger_client.DatabaseLDAPConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.LdapConfiguration() # LdapConfiguration | 

try:
    # Updates LDAP configuration.
    api_response = api_instance.put_config_database_ldap(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseLDAPConfigurationApi->put_config_database_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapConfiguration**](LdapConfiguration.md)|  | 

### Return type

[**LdapConfiguration**](LdapConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

