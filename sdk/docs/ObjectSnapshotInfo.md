# ObjectSnapshotInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_partition_id** | **int** | Specifies the Cohesity Cluster partition id where this object is stored. | [optional] 
**job_id** | **int** | Specifies the id for the Protection Job that is currently associated with the object. If the object was backed up on current Cohesity Cluster, this field contains the id for the Job that captured this backup object. If the object was backed up on a Primary Cluster and replicated to this Cohesity Cluster, a new Inactive Job is created, the object is now associated with new Inactive Job, and this field contains the id of the new Inactive Job. | [optional] 
**job_name** | **str** | Specifies the name of the Protection Job that captured the backup. | [optional] 
**job_uid** | [**ObjectSnapshotInfoJobUid**](ObjectSnapshotInfoJobUid.md) |  | [optional] 
**object_name** | **str** | Specifies the primary name of the object. | [optional] 
**os_type** | **str** | Specifies the inferred OS type. | [optional] 
**registered_source** | [**ProtectionSource**](ProtectionSource.md) | Specifies the id of the original root Protection Source tree (such as a vCenter Server) that was accessed by the Protection Job to capture a backup of this object. | [optional] 
**snapshotted_source** | [**ProtectionSource**](ProtectionSource.md) | Specifies the Protection Source that represents the original object being backed up. When a root Protection Source is registered, it creates a tree of source Protection Source objects. This field defines the specific Protection Source leaf object (such as a VM) that was backed up. | [optional] 
**versions** | [**list[SnapshotVersion]**](SnapshotVersion.md) | Specifies all snapshot versions of this object. Each time a Job Run of a Job executes, it may create a new snapshot version of an object. This array stores the different snapshots versions of the object. | [optional] 
**view_box_id** | **int** | Specifies the id of the Domain (View Box) where this object is stored. | [optional] 
**view_name** | **str** | Specifies the View name where this object is stored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


