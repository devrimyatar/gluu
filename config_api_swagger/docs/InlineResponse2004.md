# InlineResponse2004

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis_provider_type** | **str** | Type of connection. | [optional] 
**servers** | **str** | server details separated by comma e.g. &#x27;server1:8080server2:8081&#x27;. | [optional] 
**password** | **str** | Redis password. | [optional] 
**default_put_expiration** | **int** | defaultPutExpiration timeout value. | [optional] 
**sentinel_master_group_name** | **str** | Sentinel Master Group Name (required if SENTINEL type of connection is selected). | [optional] 
**use_ssl** | **bool** | Enable SSL communication between Gluu Server and Redis cache. | [optional] 
**ssl_trust_store_file_path** | **str** | Directory Path to Trust Store. | [optional] 
**max_idle_connections** | **int** | The cap on the number of \\idle\\ instances in the pool. If max idle is set too low on heavily loaded systems it is possible you will see objects being destroyed and almost immediately new objects being created. This is a result of the active threads momentarily returning objects faster than they are requesting them causing the number of idle objects to rise above max idle. The best value for max idle for heavily loaded system will vary but the default is a good starting point. | [optional] 
**max_total_connections** | **int** | The number of maximum connection instances in the pool. | [optional] 
**connection_timeout** | **int** | Connection time out. | [optional] 
**so_timeout** | **int** | With this option set to a non-zero timeout a read() call on the InputStream associated with this Socket will block for only this amount of time. If the timeout expires a java.net.SocketTimeoutException is raised though the Socket is still valid. The option must be enabled prior to entering the blocking operation to have effect. The timeout must be &gt; 0. A timeout of zero is interpreted as an infinite timeout. | [optional] 
**max_retry_attempts** | **int** | Maximum retry attempts in case of failure. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

