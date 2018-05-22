# WindowsHostSnapshotParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_only_backup** | **bool** | Specifies whether to backup regardless of the state of each file&#39;s backup history. Backup history will not be updated. Refer Microsoft documentation on VSS_BT_COPY. | [optional] 
**disable_metadata** | **bool** | Specifies whether to disable fetching and storing of some metadata on Cohesity Cluster to save storage space. Otherwise, there will be some metadata fetched and stored on Cohesity Cluster. | [optional] 
**disable_notification** | **bool** | Specifies whether to disable some notification steps when taking snapshots. | [optional] 
**excluded_vss_writers** | **list[str]** | For example, \&quot;ASR Writer\&quot;, \&quot;System Writer\&quot;. Refer Microsoft documentaion for a complete list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


