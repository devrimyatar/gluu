# CouchbaseConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Unique identifier | 
**user_name** | **str** | Couchbase server user. | 
**user_password** | **str** | Encoded Couchbase server user password. | 
**servers** | **list[str]** | Couchbase server host and port. | 
**default_bucket** | **str** | Main bucket that application should use if other mapping rules were not applied. | 
**buckets** | **list[str]** | List of buckets defining mapping rules. | 
**password_encryption_method** | **str** |  | [optional] 
**operation_tracing_enabled** | **bool** |  | [optional] [default to False]
**mutation_tokens_enabled** | **bool** | If mutation tokens are enabled, they can be used for advanced durability requirements, as well as optimized RYOW consistency. | [optional] [default to False]
**connect_timeout** | **int** |  | [optional] 
**computation_pool_size** | **int** | Sets the pool size (number of threads to use) for all non-blocking operations, default value is the number of CPUs. | [optional] 
**use_ssl** | **bool** |  | [optional] 
**ssl_trust_store_file** | **str** | The path to the trust store file to use. It contains the trusted certificates. | [optional] 
**ssl_trust_store_pin** | **str** | The PIN to use to access the contents of the trust store. | [optional] 
**ssl_trust_store_format** | **str** | The format to use for the trust store. | [optional] 
**binary_attributes** | **list[str]** |  | [optional] 
**certificate_attributes** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

