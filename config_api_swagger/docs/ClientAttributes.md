# ClientAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tls_client_auth_subject_dn** | **str** |  | [optional] 
**run_introspection_script_before_access_token_as_jwt_creation_and_include_claims** | **bool** | Run Introspection Script Before Access Token as Jwt Creation and Include Claims. Default value is false. | [optional] 
**keep_client_authorization_after_expiration** | **bool** | Keep Client Authorization After Expiration. | [optional] 
**allow_spontaneous_scopes** | **bool** |  | [optional] 
**spontaneous_scopes** | **list[str]** |  | [optional] 
**spontaneous_scope_script_dns** | **list[str]** |  | [optional] 
**backchannel_logout_uri** | **list[str]** |  | [optional] 
**backchannel_logout_session_required** | **bool** |  | [optional] 
**additional_audience** | **list[str]** |  | [optional] 
**post_authn_scripts** | **list[str]** |  | [optional] 
**consent_gathering_scripts** | **list[str]** |  | [optional] 
**introspection_scripts** | **list[str]** |  | [optional] 
**rpt_claims_scripts** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

