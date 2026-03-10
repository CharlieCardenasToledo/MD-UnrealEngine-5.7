# SetVertexColorFromFloatArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromFloatArray

> Application Version: 5.7

### Description

SetVertexColorFromFloatArray (v1)

Set the vertex color on the collection based on the normalized float array.

Input(s) :
Collection [Intrinsic] - Collection Passthrough
FloatArray [Intrinsic] - Float array to use as a scalar for the color

Output(s):
Collection [Passthrough] - Collection Passthrough

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Collection|Utilities |
| Type | [FSetVertexColorFromFloatArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetVertexColorFromFloatArrayDat-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bNormalizeInput | Enable normalization of input array | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color | Base color for the normalized float array | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection Passthrough | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FloatArray | Float array to use as a scalar for the color | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection Passthrough | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
