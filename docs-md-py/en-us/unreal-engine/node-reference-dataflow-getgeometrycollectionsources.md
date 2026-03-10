# GetGeometryCollectionSources

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources

> Application Version: 5.7

### Description

GetGeometryCollectionSources (v1)

Get the list of the original mesh information used to create a specific geometryc collection asset
each entry contains a mesh, a transform and a list of override materials

Input(s) :
Asset - Asset to get geometry sources from

Output(s):
Sources - array of geometry sources

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FGetGeometryCollectionSourcesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetGeometryCollectionSourcesDat-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Asset | Asset to get geometry sources from | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGeometryCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/UGeometryCollection)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Sources | array of geometry sources | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionSource](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionSource)> |  |
