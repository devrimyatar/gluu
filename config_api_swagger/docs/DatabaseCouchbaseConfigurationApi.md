# swagger_client.DatabaseCouchbaseConfigurationApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_config_database_couchbase_by_name**](DatabaseCouchbaseConfigurationApi.md#delete_config_database_couchbase_by_name) | **DELETE** /jans-config-api/api/v1/config/database/couchbase/{name} | Deletes a Couchbase configurations by name.
[**get_config_database_couchbase**](DatabaseCouchbaseConfigurationApi.md#get_config_database_couchbase) | **GET** /jans-config-api/api/v1/config/database/couchbase | Gets list of existing Couchbase configurations.
[**get_config_database_couchbase_by_name**](DatabaseCouchbaseConfigurationApi.md#get_config_database_couchbase_by_name) | **GET** /jans-config-api/api/v1/config/database/couchbase/{name} | Gets a Couchbase configurations by name.
[**patch_config_database_couchbase_by_name**](DatabaseCouchbaseConfigurationApi.md#patch_config_database_couchbase_by_name) | **PATCH** /jans-config-api/api/v1/config/database/couchbase/{name} | Partially modify an Couchbase configuration.
[**post_config_database_couchbase**](DatabaseCouchbaseConfigurationApi.md#post_config_database_couchbase) | **POST** /jans-config-api/api/v1/config/database/couchbase | Adds a new Couchbase configuration.
[**post_config_database_couchbase_test**](DatabaseCouchbaseConfigurationApi.md#post_config_database_couchbase_test) | **POST** /jans-config-api/api/v1/config/database/couchbase/test | Tests an Couchbase configuration.
[**put_config_database_couchbase**](DatabaseCouchbaseConfigurationApi.md#put_config_database_couchbase) | **PUT** /jans-config-api/api/v1/config/database/couchbase | Updates Couchbase configuration.

# **delete_config_database_couchbase_by_name**
> delete_config_database_couchbase_by_name(name)

Deletes a Couchbase configurations by name.

Deletes a Couchbase configurations by name.

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
api_instance = swagger_client.DatabaseCouchbaseConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of Couchbase configuration.

try:
    # Deletes a Couchbase configurations by name.
    api_instance.delete_config_database_couchbase_by_name(name)
except ApiException as e:
    print("Exception when calling DatabaseCouchbaseConfigurationApi->delete_config_database_couchbase_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of Couchbase configuration. | 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_database_couchbase**
> list[CouchbaseConfiguration] get_config_database_couchbase()

Gets list of existing Couchbase configurations.

Gets list of existing Couchbase configurations.

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
api_instance = swagger_client.DatabaseCouchbaseConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Gets list of existing Couchbase configurations.
    api_response = api_instance.get_config_database_couchbase()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseCouchbaseConfigurationApi->get_config_database_couchbase: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CouchbaseConfiguration]**](CouchbaseConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_database_couchbase_by_name**
> CouchbaseConfiguration get_config_database_couchbase_by_name(name)

Gets a Couchbase configurations by name.

Gets a Couchbase configurations by name.

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
api_instance = swagger_client.DatabaseCouchbaseConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of Couchbase configuration.

try:
    # Gets a Couchbase configurations by name.
    api_response = api_instance.get_config_database_couchbase_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseCouchbaseConfigurationApi->get_config_database_couchbase_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of Couchbase configuration. | 

### Return type

[**CouchbaseConfiguration**](CouchbaseConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_config_database_couchbase_by_name**
> CouchbaseConfiguration patch_config_database_couchbase_by_name(name, body=body)

Partially modify an Couchbase configuration.

Partially modify an Couchbase configuration.

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
api_instance = swagger_client.DatabaseCouchbaseConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of Couchbase configuration.
body = [swagger_client.PatchRequest()] # list[PatchRequest] |  (optional)

try:
    # Partially modify an Couchbase configuration.
    api_response = api_instance.patch_config_database_couchbase_by_name(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseCouchbaseConfigurationApi->patch_config_database_couchbase_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of Couchbase configuration. | 
 **body** | [**list[PatchRequest]**](PatchRequest.md)|  | [optional] 

### Return type

[**CouchbaseConfiguration**](CouchbaseConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_config_database_couchbase**
> CouchbaseConfiguration post_config_database_couchbase(body)

Adds a new Couchbase configuration.

Adds a new Couchbase configuration.

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
api_instance = swagger_client.DatabaseCouchbaseConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CouchbaseConfiguration() # CouchbaseConfiguration | 

try:
    # Adds a new Couchbase configuration.
    api_response = api_instance.post_config_database_couchbase(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseCouchbaseConfigurationApi->post_config_database_couchbase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CouchbaseConfiguration**](CouchbaseConfiguration.md)|  | 

### Return type

[**CouchbaseConfiguration**](CouchbaseConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_config_database_couchbase_test**
> bool post_config_database_couchbase_test(body)

Tests an Couchbase configuration.

Tests an Couchbase configuration.

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
api_instance = swagger_client.DatabaseCouchbaseConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CouchbaseConfiguration() # CouchbaseConfiguration | 

try:
    # Tests an Couchbase configuration.
    api_response = api_instance.post_config_database_couchbase_test(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseCouchbaseConfigurationApi->post_config_database_couchbase_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CouchbaseConfiguration**](CouchbaseConfiguration.md)|  | 

### Return type

**bool**

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_database_couchbase**
> CouchbaseConfiguration put_config_database_couchbase(body)

Updates Couchbase configuration.

Updates Couchbase configuration.

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
api_instance = swagger_client.DatabaseCouchbaseConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CouchbaseConfiguration() # CouchbaseConfiguration | 

try:
    # Updates Couchbase configuration.
    api_response = api_instance.put_config_database_couchbase(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseCouchbaseConfigurationApi->put_config_database_couchbase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CouchbaseConfiguration**](CouchbaseConfiguration.md)|  | 

### Return type

[**CouchbaseConfiguration**](CouchbaseConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

