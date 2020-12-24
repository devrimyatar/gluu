# LdapConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Unique identifier - Name | [optional] 
**bind_dn** | **str** | This contains the username to connect to the backend server. You need to use full DN here. As for example, cn&#x3D;jans,dc&#x3D;company,dc&#x3D;org. | [optional] 
**bind_password** | **str** | Ldap password for binding. | [optional] 
**servers** | **list[str]** | List of LDAP authentication servers. | [optional] 
**max_connections** | **int** | This value defines the maximum number of connections that are allowed to read the backend Active Directory/LDAP server. | [optional] [default to 2]
**use_ssl** | **bool** | Enable SSL communication between Jans Server and LDAP server. | [optional] 
**base_d_ns** | **list[str]** | List contains the location of the Active Directory/LDAP tree from where the Gluu Server shall read the user information. | [optional] 
**primary_key** | **str** | Used to search and bind operations in configured LDAP server. | [optional] 
**local_primary_key** | **str** | Used to search local user entry in Gluu Server’s internal LDAP directory. | [optional] 
**use_anonymous_bind** | **bool** | Boolean value used to indicate if the LDAP Server will allow anonymous bind request. | [optional] 
**enabled** | **bool** | Boolean value used to indicate if the LDAP Server is enabled. Do not use this unless the server administrator has entered all the required values. | [optional] 
**version** | **int** | LDAP server version. | [optional] 
**level** | **int** | A string that indicates the level. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

