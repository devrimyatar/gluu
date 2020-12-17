# swagger_client.AttributeApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attributes_by_inum**](AttributeApi.md#delete_attributes_by_inum) | **DELETE** /jans-config-api/api/v1/attributes/{inum} | Deletes an attribute based on inum.
[**get_attributes**](AttributeApi.md#get_attributes) | **GET** /jans-config-api/api/v1/attributes | Gets a list of Gluu attributes.
[**get_attributes_by_inum**](AttributeApi.md#get_attributes_by_inum) | **GET** /jans-config-api/api/v1/attributes/{inum} | Gets an attribute based on inum.
[**patch_attributes_by_inum**](AttributeApi.md#patch_attributes_by_inum) | **PATCH** /jans-config-api/api/v1/attributes/{inum} | Partially modify a GluuAttribute.
[**post_attributes**](AttributeApi.md#post_attributes) | **POST** /jans-config-api/api/v1/attributes | Adds a new attribute.
[**put_attributes**](AttributeApi.md#put_attributes) | **PUT** /jans-config-api/api/v1/attributes | Updates an existing attribute.

# **delete_attributes_by_inum**
> delete_attributes_by_inum(inum)

Deletes an attribute based on inum.

Deletes an attribute based on inum.

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Attribute ID.

try:
    # Deletes an attribute based on inum.
    api_instance.delete_attributes_by_inum(inum)
except ApiException as e:
    print("Exception when calling AttributeApi->delete_attributes_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Attribute ID. | 

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> list[GluuAttribute] get_attributes(limit=limit, pattern=pattern, status=status)

Gets a list of Gluu attributes.

Gets all attributes. Optionally max-size of the result, attribute status and pattern can be provided.

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
limit = 50 # int | Search size - max size of the results to return. (optional) (default to 50)
pattern = 'pattern_example' # str | Search pattern. (optional)
status = 'all' # str | Status of the attribute (optional) (default to all)

try:
    # Gets a list of Gluu attributes.
    api_response = api_instance.get_attributes(limit=limit, pattern=pattern, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Search size - max size of the results to return. | [optional] [default to 50]
 **pattern** | **str**| Search pattern. | [optional] 
 **status** | **str**| Status of the attribute | [optional] [default to all]

### Return type

[**list[GluuAttribute]**](GluuAttribute.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_by_inum**
> GluuAttribute get_attributes_by_inum(inum)

Gets an attribute based on inum.

Gets an attribute based on inum.

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Attribute ID.

try:
    # Gets an attribute based on inum.
    api_response = api_instance.get_attributes_by_inum(inum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->get_attributes_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Attribute ID. | 

### Return type

[**GluuAttribute**](GluuAttribute.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attributes_by_inum**
> GluuAttribute patch_attributes_by_inum(inum, body=body)

Partially modify a GluuAttribute.

Partially modify a GluuAttribute.

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
inum = 'inum_example' # str | Attribute ID.
body = swagger_client.PatchRequest() # PatchRequest |  (optional)

try:
    # Partially modify a GluuAttribute.
    api_response = api_instance.patch_attributes_by_inum(inum, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->patch_attributes_by_inum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inum** | **str**| Attribute ID. | 
 **body** | [**PatchRequest**](PatchRequest.md)|  | [optional] 

### Return type

[**GluuAttribute**](GluuAttribute.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attributes**
> GluuAttribute post_attributes(name, display_name, description, data_type, status, jans_multivalued_attr, lifetime, source_attribute, salt, name_id_type, origin, edit_type, view_type, usage_type, jans_attr_name, see_also, saml1_uri, saml2_uri, urn, jans_scim_custom_attr, custom, requred, attribute_validation, gluu_tooltip)

Adds a new attribute.

Adds a new attribute.

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
display_name = ['display_name_example'] # list[str] | 
description = 'description_example' # str | 
data_type = 'data_type_example' # str | 
status = 'status_example' # str | 
jans_multivalued_attr = true # bool | 
lifetime = 'lifetime_example' # str | 
source_attribute = 'source_attribute_example' # str | 
salt = 'salt_example' # str | 
name_id_type = 'name_id_type_example' # str | 
origin = 'origin_example' # str | 
edit_type = ['edit_type_example'] # list[str] | 
view_type = ['view_type_example'] # list[str] | 
usage_type = ['usage_type_example'] # list[str] | 
jans_attr_name = 'jans_attr_name_example' # str | 
see_also = 'see_also_example' # str | 
saml1_uri = 'saml1_uri_example' # str | 
saml2_uri = 'saml2_uri_example' # str | 
urn = 'urn_example' # str | 
jans_scim_custom_attr = true # bool | 
custom = true # bool | 
requred = true # bool | 
attribute_validation = swagger_client.GluuAttributeAttributeValidation() # GluuAttributeAttributeValidation | 
gluu_tooltip = 'gluu_tooltip_example' # str | 

try:
    # Adds a new attribute.
    api_response = api_instance.post_attributes(name, display_name, description, data_type, status, jans_multivalued_attr, lifetime, source_attribute, salt, name_id_type, origin, edit_type, view_type, usage_type, jans_attr_name, see_also, saml1_uri, saml2_uri, urn, jans_scim_custom_attr, custom, requred, attribute_validation, gluu_tooltip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->post_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **display_name** | [**list[str]**](str.md)|  | 
 **description** | **str**|  | 
 **data_type** | **str**|  | 
 **status** | **str**|  | 
 **jans_multivalued_attr** | **bool**|  | 
 **lifetime** | **str**|  | 
 **source_attribute** | **str**|  | 
 **salt** | **str**|  | 
 **name_id_type** | **str**|  | 
 **origin** | **str**|  | 
 **edit_type** | [**list[str]**](str.md)|  | 
 **view_type** | [**list[str]**](str.md)|  | 
 **usage_type** | [**list[str]**](str.md)|  | 
 **jans_attr_name** | **str**|  | 
 **see_also** | **str**|  | 
 **saml1_uri** | **str**|  | 
 **saml2_uri** | **str**|  | 
 **urn** | **str**|  | 
 **jans_scim_custom_attr** | **bool**|  | 
 **custom** | **bool**|  | 
 **requred** | **bool**|  | 
 **attribute_validation** | [**GluuAttributeAttributeValidation**](.md)|  | 
 **gluu_tooltip** | **str**|  | 

### Return type

[**GluuAttribute**](GluuAttribute.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_attributes**
> list[GluuAttribute] put_attributes(body)

Updates an existing attribute.

Updates an existing attribute.

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
body = swagger_client.GluuAttribute() # GluuAttribute | 

try:
    # Updates an existing attribute.
    api_response = api_instance.put_attributes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->put_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GluuAttribute**](GluuAttribute.md)|  | 

### Return type

[**list[GluuAttribute]**](GluuAttribute.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

