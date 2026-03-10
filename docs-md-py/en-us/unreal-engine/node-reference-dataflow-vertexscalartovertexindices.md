# VertexScalarToVertexIndices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VertexScalarToVertexIndices

> Application Version: 5.7

### Description

VertexScalarToVertexIndices (v1)

Convert an vertex float array to a list of indices

Input(s) :
AttributeKey - The name of the vertex attribute and group to generate indices from.

Output(s):
VertexIndices - Output list of indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Tags | Collection Vertex Weight Map to Indices |
| Type | [FGeometryCollectionVertexScalarToVertexIndicesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-_4) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionThreshold | The value threshold for what is included in the vertex list. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey | The name of the vertex attribute and group to generate indices from. | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="Vertices") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexIndices | Output list of indices | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
