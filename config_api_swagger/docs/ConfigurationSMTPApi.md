# swagger_client.ConfigurationSMTPApi

All URIs are relative to *https://jans.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_config_smtp**](ConfigurationSMTPApi.md#delete_config_smtp) | **DELETE** /jans-config-api/api/v1/config/smtp | Deletes SMTP server configuration.
[**get_config_smtp**](ConfigurationSMTPApi.md#get_config_smtp) | **GET** /jans-config-api/api/v1/config/smtp | Returns SMTP server configuration.
[**post_config_smtp**](ConfigurationSMTPApi.md#post_config_smtp) | **POST** /jans-config-api/api/v1/config/smtp | Adds SMTP server configuration.
[**put_config_smtp**](ConfigurationSMTPApi.md#put_config_smtp) | **PUT** /jans-config-api/api/v1/config/smtp | Updates SMTP server configuration.
[**test_config_smtp**](ConfigurationSMTPApi.md#test_config_smtp) | **GET** /jans-config-api/api/v1/config/smtp/test | Test SMTP server configuration.

# **delete_config_smtp**
> delete_config_smtp()

Deletes SMTP server configuration.

Deletes SMTP server configuration.

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
api_instance = swagger_client.ConfigurationSMTPApi(swagger_client.ApiClient(configuration))

try:
    # Deletes SMTP server configuration.
    api_instance.delete_config_smtp()
except ApiException as e:
    print("Exception when calling ConfigurationSMTPApi->delete_config_smtp: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_smtp**
> SmtpConfiguration get_config_smtp()

Returns SMTP server configuration.

Returns SMTP server configuration.

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
api_instance = swagger_client.ConfigurationSMTPApi(swagger_client.ApiClient(configuration))

try:
    # Returns SMTP server configuration.
    api_response = api_instance.get_config_smtp()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSMTPApi->get_config_smtp: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SmtpConfiguration**](SmtpConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_config_smtp**
> SmtpConfiguration post_config_smtp(body=body)

Adds SMTP server configuration.

Adds SMTP server configuration.

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
api_instance = swagger_client.ConfigurationSMTPApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmtpConfiguration() # SmtpConfiguration |  (optional)

try:
    # Adds SMTP server configuration.
    api_response = api_instance.post_config_smtp(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSMTPApi->post_config_smtp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmtpConfiguration**](SmtpConfiguration.md)|  | [optional] 

### Return type

[**SmtpConfiguration**](SmtpConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_smtp**
> SmtpConfiguration put_config_smtp(body=body)

Updates SMTP server configuration.

Updates SMTP server configuration.

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
api_instance = swagger_client.ConfigurationSMTPApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmtpConfiguration() # SmtpConfiguration |  (optional)

try:
    # Updates SMTP server configuration.
    api_response = api_instance.put_config_smtp(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSMTPApi->put_config_smtp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmtpConfiguration**](SmtpConfiguration.md)|  | [optional] 

### Return type

[**SmtpConfiguration**](SmtpConfiguration.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_config_smtp**
> InlineResponse200 test_config_smtp()

Test SMTP server configuration.

Test SMTP server configuration.

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
api_instance = swagger_client.ConfigurationSMTPApi(swagger_client.ApiClient(configuration))

try:
    # Test SMTP server configuration.
    api_response = api_instance.test_config_smtp()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSMTPApi->test_config_smtp: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[jans-auth](../README.md#jans-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

