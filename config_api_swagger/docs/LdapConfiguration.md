# LdapConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Unique identifier - Name | 
**bind_dn** | **str** | User Distingusihed Name for binding. | 
**max_connections** | **int** | Total number of simultaneous connections allowed. | [default to 2]
**primary_key** | **str** | Used to search and bind operations in configured LDAP server. | 
**local_primary_key** | **str** | Used to search local user entry in Gluu Server’s internal LDAP directory. | 
**servers** | **list[str]** | List of LDAP authentication servers. | 
**base_d_ns** | **list[str]** | list of LDAP base Distingusihed Name | 
**use_ssl** | **bool** |  | 
**bind_password** | **str** | User password for binding. | [optional] 
**use_anonymous_bind** | **bool** | Boolean value used to indicate if the LDAP Server will allow anonymous bind request. | [optional] 
**enabled** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

