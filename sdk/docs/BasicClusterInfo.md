# BasicClusterInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_software_version** | **str** | Specifies the current release of the Cohesity software running on this Cohesity Cluster. | [optional] 
**cluster_type** | **str** | Specifies the type of Cohesity Cluster. &#39;kPhysical&#39; indicates the Cohesity Cluster is hosted directly on hardware. &#39;kVirtualRobo&#39; indicates the Cohesity Cluster is hosted in a VM on a ESXi Host of a VMware vCenter Server using Cohesity&#39;s Virtual Edition. &#39;kMicrosoftCloud&#39; indicates the Cohesity Cluster is hosed in a VM on Microsoft Azure using Cohesity&#39;s Cloud Edition. &#39;kAmazonCloud&#39; indicates the Cohesity Cluster is hosed in a VM on Amazon S3 using Cohesity&#39;s Cloud Edition. &#39;kGoogleCloud&#39; indicates the Cohesity Cluster is hosed in a VM on Google Cloud Platform using Cohesity&#39;s Cloud Edition. | [optional] 
**domains** | **list[str]** | Specifies a list of domains joined to the Cohesity Cluster, including the default LOCAL Cohesity domain used to store the local Cohesity users. | [optional] 
**language_locale** | **str** | Specifies the language and locale for the Cohesity Cluster. | [optional] 
**name** | **str** | Specifies the name of the Cohesity Cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


