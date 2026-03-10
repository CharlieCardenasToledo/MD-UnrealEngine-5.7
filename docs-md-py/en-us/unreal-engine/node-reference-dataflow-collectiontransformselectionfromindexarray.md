# CollectionTransformSelectionFromIndexArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray

> Application Version: 5.7

### Description

CollectionTransformSelectionFromIndexArray (v1)

Convert index array to a transform selection

Input(s) :
Collection [Intrinsic] - Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection.
BoneIndices - Array of bone indices to convert to a trannsform selection

Output(s):
Collection [Passthrough] - Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection.
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Array |
| Type | [FCollectionTransformSelectionFromIndexArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_11) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndices | Array of bone indices to convert to a trannsform selection | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
