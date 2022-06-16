# ResourceSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depends_on** | [**list[ResourceSchemaDependson]**](ResourceSchemaDependson.md) |  | [optional] 
**description** | **str** | Description about the resource | [optional] 
**field** | [**list[ResourceSchemaField]**](ResourceSchemaField.md) |  | [optional] 
**function** | [**list[ResourceSchemaFunction]**](ResourceSchemaFunction.md) |  | [optional] 
**keys** | **list[str]** |  | [optional] 
**resource_name** | **str** | Name of the resource. Should be of pattern [a-z][a-z0-9-]* | 
**is_default** | **bool** | Flag to denote default resource | [optional] 
**is_modified** | **bool** | Flag to denote if default resource is modified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


