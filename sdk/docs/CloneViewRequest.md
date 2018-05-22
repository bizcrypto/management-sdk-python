# CloneViewRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_sids** | **list[str]** | Specifies the list of security identifiers (SIDs) for the restricted Principals who have access to this View. | [optional] 
**clone_view_name** | **str** | Specifies the name of the new View that is cloned from the source View. | [optional] 
**data_lock_expiry_usecs** | **int** | DataLock (Write Once Read Many) lock expiry epoch time in microseconds. If specified, a view will be marked as a DataLock view. If a view is marked as a DataLock view, only a Data Security Officer (a user having Data Security Privilege) can delete the view until the lock expiry time. | [optional] 
**description** | **str** | Specifies an optional text description about the View. | [optional] 
**enable_filer_audit_logging** | **bool** | Specifies if Filer Audit Logging is enabled for this view. | [optional] 
**enable_mixed_mode_permissions** | **bool** | If set, mixed mode (NFS and SMB) access is enabled for this view. | [optional] 
**enable_smb_access_based_enumeration** | **bool** | Specifies if access-based enumeration should be enabled. If &#39;true&#39;, only files and folders that the user has permissions to access are visible on the SMB share for that user. | [optional] 
**enable_smb_view_discovery** | **bool** | If set, it enables discovery of view for SMB. | [optional] 
**file_extension_filter** | [**FileExtensionFilter**](FileExtensionFilter.md) | Optional filtering criteria that should be satisfied by all the files created in this view. It does not affect existing files. | [optional] 
**logical_quota** | [**CloneTaskRequestCloneViewParametersLogicalQuota**](CloneTaskRequestCloneViewParametersLogicalQuota.md) |  | [optional] 
**protocol_access** | **str** | Specifies the supported Protocols for the View. | [optional] 
**qos** | [**QoS**](QoS.md) | Specifies the Quality of Service (QoS) Policy for the View. | [optional] 
**smb_permissions_info** | [**SmbPermissionsInfo**](SmbPermissionsInfo.md) | Specifies the SMB permissions for the View. | [optional] 
**source_view_name** | **str** | Specifies the name of the source View that will be cloned. | [optional] 
**storage_policy_override** | [**StoragePolicyOverride**](StoragePolicyOverride.md) | Specifies if inline deduplication and compression settings inherited from the Storage Domain (View Box) should be disabled for this View. | [optional] 
**subnet_whitelist** | [**list[Subnet]**](Subnet.md) | Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides the Subnets specified at the global Cohesity Cluster level.) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


