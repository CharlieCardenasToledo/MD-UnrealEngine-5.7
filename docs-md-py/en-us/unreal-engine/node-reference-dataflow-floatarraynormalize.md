# FloatArrayNormalize

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize

> Application Version: 5.7

### Description

FloatArrayNormalize (v1)

Normalize the selected float data in a FloatArray

Input(s) :
InFloatArray [Intrinsic] - Input VectorArray
Selection - Selection for the operation

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FFloatArrayNormalizeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayNormalizeDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InFloatArray | Input VectorArray | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| Selection | Selection for the operation | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| MinRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutFloatArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
