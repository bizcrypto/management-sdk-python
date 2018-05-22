# PhysicalSpecialParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_parameters** | [**ApplicationParameters**](ApplicationParameters.md) | Specifies parameters that are related to applications running on the Protection Source. | [optional] 
**enable_system_backup** | **bool** | Specifies whether to allow system backup using 3rd party tools installed on the Protection Host. System backups are used for doing bare metal recovery later. This field is applicable only for System backups. | [optional] 
**file_paths** | [**list[FilePathParameters]**](FilePathParameters.md) | Specifies a list of directories or files to protect in a Physical Server. | [optional] 
**volume_guid** | **list[str]** | Specifies the subset of mounted volumes to protect in a Physical Server. If not specified, all mounted volumes on a Physical Server are protected. | [optional] 
**windows_parameters** | [**WindowsHostSnapshotParameters**](WindowsHostSnapshotParameters.md) | Specifies parameters applicable only to Windows hosts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


