# StoragePolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_spill_vault_id** | **int** | Specifies the vault id assigned for an external Storage Target to facilitate cloud spill. | [optional] 
**compression_policy** | **str** | Specifies the compression setting to be applied to a Storage Domain (View Box). &#39;kCompressionNone&#39; indicates that data is not compressed. &#39;kCompressionLow&#39; indicates that data is compressed. | [optional] 
**deduplicate_compress_delay_secs** | **int** | Specifies the time in seconds when deduplication and compression of data on the Storage Domain (View Box) starts. If set to 0, deduplication and compression is done inline (as the data is being written). Otherwise, post-process deduplication and compression is done after the specified delay. | [optional] 
**deduplication_enabled** | **bool** | Specifies if deduplication is enabled for the Storage Domain (View Box). If deduplication is enabled, the Cohesity Cluster eliminates duplicate blocks of repeating data stored on the Cluster thus reducing the amount of storage space needed to store data. | [optional] 
**encryption_policy** | **str** | Specifies the encryption setting for the Storage Domain (View Box). &#39;kEncryptionNone&#39; indicates the data is not encrypted. &#39;kEncryptionStrong&#39; indicates the data is encrypted. | [optional] 
**erasure_coding_info** | [**ErasureCodingInfo**](ErasureCodingInfo.md) | Specifies information about erasure coding algorithm if erasure coding is enabled. | [optional] 
**inline_compress** | **bool** | Specifies if compression should occur inline (as the data is being written). This field is only relevant if compression is enabled. If deduplication is set to inline, Cohesity recommends setting compression to inline. | [optional] 
**inline_deduplicate** | **bool** | Specifies if deduplication should occur inline (as the data is being written). This field is only relevant if deduplication is enabled. | [optional] 
**num_failures_tolerated** | **int** | Number of failures to tolerate. This is an optional field. Default value is 1 for cluster having 3 or more nodes. If erasure coding is not enabled, then this specifies the replication factor for the Storage Domain (View Box). For RF&#x3D;2, number of failures to tolerate should be specified as 1. If erasure coding is enabled, then this value will be same as number of coded stripes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


