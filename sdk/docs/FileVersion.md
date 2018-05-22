# FileVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_time_usecs** | **int** | Specifies the time when the file or folder was last modified. Specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**size_bytes** | **int** | Specifies the size of the file or folder (in bytes) from the most recent snapshot. | [optional] 
**snapshots** | [**list[SnapshotAttempt]**](SnapshotAttempt.md) | Specifies the available snapshots of the file or folder. When a Job Run executes, it captures a snapshot of object (such as a VM) that contains the file or folder. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


