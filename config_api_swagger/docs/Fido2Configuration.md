# Fido2Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_certs_folder** | **str** | Authenticators certificates fodler. | [optional] 
**mds_certs_folder** | **str** | MDS TOC root certificates folder. | [optional] 
**mds_tocs_folder** | **str** | MDS TOC files folder. | [optional] 
**server_metadata_folder** | **str** | Authenticators metadata in json format. | [optional] 
**requested_parties** | [**list[RequestedParties]**](RequestedParties.md) | Authenticators metadata in json format. | [optional] 
**user_auto_enrollment** | **bool** | Allow to enroll users on enrollment/authentication requests. | [optional] 
**unfinished_request_expiration** | **int** | Expiration time in seconds for pending enrollment/authentication requests | [optional] 
**authentication_history_expiration** | **int** | Expiration time in seconds for approved authentication requests. | [optional] 
**requested_credential_types** | **list[str]** | List of Requested Credential Types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

