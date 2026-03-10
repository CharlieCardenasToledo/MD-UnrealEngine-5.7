# VectorArrayNormalize

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorArrayNormalize

> Application Version: 5.7

### Description

VectorArrayNormalize (v1)

Normalize all the selected vectors in a VectorArray

Input(s) :
InVectorArray [Intrinsic] - Input VectorArray
Selection - Selection for the operation

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Vector |
| Type | [FVectorArrayNormalizeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVectorArrayNormalizeDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InVectorArray | Input VectorArray | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Selection | Selection for the operation | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutVectorArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
