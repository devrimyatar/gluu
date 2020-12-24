# CustomScript

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** |  | [optional] 
**inum** | **str** | XRI i-number. Identifier to uniquely identify the script. | [optional] 
**name** | **str** | Name should contain only letters, digits and underscores. | [optional] 
**aliases** | **list[str]** | List of possible alias for the script. | [optional] 
**description** | **str** | Details describing the script. | [optional] 
**script** | **str** | Actual script. | [optional] 
**script_type** | **str** | Type of script. | [optional] 
**programming_language** | **str** | Programming language of the custom script. | [optional] 
**module_properties** | [**list[CustomScriptModuleProperties]**](CustomScriptModuleProperties.md) | Module-level properties applicable to the script. | [optional] 
**configuration_properties** | [**list[CustomScriptConfigurationProperties]**](CustomScriptConfigurationProperties.md) | Configuration properties applicable to the script. | [optional] 
**level** | **int** | Script level. | [optional] 
**revision** | **int** | Update revision number of the script. | [optional] 
**enabled** | **bool** | boolean value indicating if script enabled. | [optional] 
**script_error** | [**CustomScriptScriptError**](CustomScriptScriptError.md) |  | [optional] 
**modified** | **bool** | boolean value indicating if the script is modified. | [optional] 
**internal** | **bool** | boolean value indicating if the script is interanl. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

