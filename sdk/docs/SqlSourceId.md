# SqlSourceId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date_msecs** | **int** | Specifies a unique identifier generated from the date the database is created or renamed. Cohesity uses this identifier in combination with the databaseId to uniquely identify a database. | [optional] 
**database_id** | **int** | Specifies a unique id of the database but only for the life of the database. SQL Server may reuse database ids. Cohesity uses the createDateMsecs in combination with this databaseId to uniquely identify a database. | [optional] 
**instance_id** | **list[int]** | Specifies unique id for the SQL Server instance. This id does not change during the life of the instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


