# ProtectionSourceNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_nodes** | **list[object]** | Specifies the child subtree used to store additional application-level Objects. Different environments use the subtree to store application-level information. For example for SQL Server, this subtree stores the SQL Server instances running on a VM. | [optional] 
**logical_size** | **int** | Specifies the logical size of the data in bytes for the Object on this node. Presence of this field indicates this node is a leaf node. | [optional] 
**nodes** | **list[object]** | Specifies children of the current node in the Protection Sources hierarchy. When representing Objects in memory, the entire Object subtree hierarchy is represented. You can use this subtree to navigate down the Object hierarchy. | [optional] 
**protected_sources_summary** | [**list[AggregatedSubtreeInfo]**](AggregatedSubtreeInfo.md) | Specifies aggregated information about all the child Objects of this node that are currently protected by a Protection Job. There is one entry for each environment that is being backed up. The aggregated information for the Object hierarchy&#39;s environment will be available at the 0th index of the vector. | [optional] 
**protection_source** | [**ProtectionSourceNodeProtectionSource**](ProtectionSourceNodeProtectionSource.md) |  | [optional] 
**registration_info** | [**ProtectionSourceNodeRegistrationInfo**](ProtectionSourceNodeRegistrationInfo.md) |  | [optional] 
**unprotected_sources_summary** | [**list[AggregatedSubtreeInfo]**](AggregatedSubtreeInfo.md) | Specifies aggregated information about all the child Objects of this node that are not protected by any Protection Jobs. The aggregated information for the Objects hierarchy&#39;s environment will be available at the 0th index of the vector. NOTE: This list includes Objects that were protected at some point in the past but are no longer actively protected. Snapshots containing these Objects may even exist on the Cohesity Cluster and be available to recover from. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


