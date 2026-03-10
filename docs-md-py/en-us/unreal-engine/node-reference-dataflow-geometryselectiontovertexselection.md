# GeometrySelectionToVertexSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometrySelectionToVertexSelection

> Application Version: 5.7

### Description

GeometrySelectionToVertexSelection (v1)

Converts GeometrySelection to VertexSelection

Input(s) :
Collection - GeometryCollection
GeometrySelection - Input geometry selection

Output(s):
VertexSelection - Vertex selection output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|All |
| Type | [FGeometrySelectionToVertexSelectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometrySelecti-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GeometryIndices | Space separated list of geometry indices to specify the selection when GeometrySelection is not connected | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| GeometrySelection | Input geometry selection | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexSelection | Vertex selection output | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |
