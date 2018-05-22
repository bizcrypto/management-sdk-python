# VolumeSecurityInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | Specifies the Unix group ID for this volume. 0 indicates the root id. | [optional] 
**permissions** | **str** | Specifies the Unix permission bits in octal string format. | [optional] 
**style** | **str** | Specifies the security style associated with this volume. Specifies the type of a NetApp Volume. &#39;kUnix&#39; indicates Unix-style security. &#39;kNtfs&#39; indicates Windows NTFS-style security. &#39;kMixed&#39; indicates mixed-style security. &#39;kUnified&#39; indicates Unified-style security. | [optional] 
**user_id** | **int** | Specifies the Unix user id for this volume. 0 indicates the root id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


