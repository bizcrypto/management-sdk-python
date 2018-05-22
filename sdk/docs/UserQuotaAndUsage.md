# UserQuotaAndUsage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota_policy** | [**QuotaPolicy**](QuotaPolicy.md) | User quota policy applied to this user. | [optional] 
**sid** | **str** | If interested in a user via smb_client, include SID. Otherwise, If valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. The string is of following format - S-1-IdentifierAuthority-SubAuthority1-SubAuthority2-...-SubAuthorityn. | [optional] 
**unix_uid** | **int** | If interested in a user via unix-identifier, include UnixUid. Otherwise, If valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. | [optional] 
**usage_bytes** | **int** | Current logical usage of user id in the input view. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


