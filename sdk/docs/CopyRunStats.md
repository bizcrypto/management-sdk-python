# CopyRunStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the time when this replication ended. If not set, then the replication has not ended yet. | [optional] 
**is_incremental** | **bool** | Specifies whether this archival is incremental for archival targets. | [optional] 
**logical_bytes_transferred** | **int** | Specifies the number of logical bytes transferred for this replication so far. This value can never exceed the total logical size of the replicated view. | [optional] 
**logical_size_bytes** | **int** | Specifies the total amount of logical data to be transferred for this replication. | [optional] 
**logical_transfer_rate_bps** | **int** | Specifies average logical bytes transfer rate in bytes per second for archchival targets. | [optional] 
**physical_bytes_transferred** | **int** | Specifies the number of physical bytes sent over the wire for replication targets. | [optional] 
**start_time_usecs** | **int** | Specifies the time when this replication was started. If not set, then replication has not been started yet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


