# RemoteVaultRestoreTaskStatusCurrentIndexingStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time of the time range that is being indexed. The indexing task is creating an index of the Job Runs that occurred between the startTimeUsecs and this endTimeUsecs. This field is recorded as a Unix epoch Timestamp (in microseconds). | [optional] 
**error** | **str** | Specifies the error message if the indexing Job/task fails. | [optional] 
**indexing_task_end_time_usecs** | **int** | Specifies when the indexing task completed. This time is recorded as a Unix epoch Timestamp (in microseconds). This field is not set if the indexing task is still in progress. | [optional] 
**indexing_task_start_time_usecs** | **int** | Specifies when the indexing task started. This time is recorded as a Unix epoch Timestamp (in microseconds). | [optional] 
**indexing_task_status** | **str** | Specifies the status of the indexing Job/task. &#39;kJobRunning&#39; indicates that the Job/task is currently running. &#39;kJobFinished&#39; indicates that the Job/task completed and finished. &#39;kJobFailed&#39; indicates that the Job/task failed and did not complete. &#39;kJobCanceled&#39; indicates that the Job/task was canceled. &#39;kJobPaused&#39; indicates the Job/task is paused. | [optional] 
**indexing_task_uid** | [**RemoteRestoreIndexingStatusIndexingTaskUid**](RemoteRestoreIndexingStatusIndexingTaskUid.md) |  | [optional] 
**latest_expiry_time_usecs** | **int** | For all the Snapshots retrieved by this Job, specifies the latest time when a Snapshot expires. | [optional] 
**progress_monitor_task** | **str** | Specifies the path to progress monitor task to track the progress of building the index. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the time range that is being indexed. The indexing task is creating an index of the Job Runs that occurred between this startTimeUsecs and the endTimeUsecs. This field is recorded as a Unix epoch Timestamp (in microseconds). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


