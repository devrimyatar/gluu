# Scope

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** |  | [optional] 
**id** | **str** | The base64url encoded id. | [optional] 
**inum** | **str** | Unique id identifying the attribute | [optional] 
**display_name** | **str** | A human-readable name of the scope. | [optional] 
**description** | **str** | A human-readable string describing the scope. | [optional] 
**icon_url** | **str** | A URL for a graphic icon representing the scope. The referenced icon MAY be used by the authorization server in any user interface it presents to the resource owner. | [optional] 
**authorization_policies** | **list[str]** | Policies associated with all scopes. | [optional] 
**default_scope** | **bool** | Boolean value to specify default scope. | [optional] 
**scope_type** | **str** | The scopes type associated with Access Tokens determine what resources will. | [optional] 
**jans_claim** | **list[str]** | Claim attributes associated with the scope. | [optional] 
**uma_type** | **bool** |  | [optional] 
**uma_authorization_policies** | **list[str]** |  | [optional] 
**attributes** | [**ScopeAttributes**](ScopeAttributes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

