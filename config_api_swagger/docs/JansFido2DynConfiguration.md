# JansFido2DynConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | URL using the https scheme for Issuer identifier. | [optional] 
**base_endpoint** | **str** | The base URL for Fido2 endpoints. | [optional] 
**clean_service_interval** | **int** | Time interval for the Clean Service in seconds. | [optional] 
**clean_service_batch_chunk_size** | **int** | Each clean up iteration fetches chunk of expired data per base dn and removes it from storage. | [optional] 
**use_local_cache** | **bool** | Boolean value to indicate if Local Cache is to be used. | [optional] 
**disable_jdk_logger** | **bool** | Boolean value specifying whether to enable JDK Loggers. | [optional] 
**logging_level** | **str** | Logging level for Fido2 logger. | [optional] 
**logging_layout** | **str** | Logging layout used for Fido2. | [optional] 
**external_logger_configuration** | **str** | Path to external Fido2 logging configuration. | [optional] 
**metric_reporter_interval** | **int** | The interval for metric reporter in seconds. | [optional] 
**metric_reporter_keep_data_days** | **int** | The days to keep report data. | [optional] 
**metric_reporter_enabled** | **bool** | Boolean value specifying whether to enable Metric Reporter. | [optional] 
**person_custom_object_class_list** | **list[str]** | Custom object class list for dynamic person enrolment. | [optional] 
**fido2_configuration** | [**Fido2Configuration**](Fido2Configuration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

