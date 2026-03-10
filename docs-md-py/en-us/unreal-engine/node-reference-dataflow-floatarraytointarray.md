# FloatArrayToIntArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray

> Application Version: 5.7

### Description

FloatArrayToIntArray (v1)

Converts a Float array to Int array using the specified method.

Input(s) :
FloatArray - Float array value to convert

Output(s):
IntArray - Int array output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Conversions |
| Type | [FFloatArrayToIntArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayToIntArrayDataflowNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Function | Conversion method: Floor takes the floor of each input float value - 1.1 turns into 1. Ceil takes the ceil - 1.1 turns into 2. Round rounds to the nearest integer - 1.1 turns into 1. Tuncate trucates like a type cast - 1.1 turns into 1. Non-zero to Index appends the index of all non-zero values to the output array. Zero to Index appends the index of all zero values to the output array. | [EFloatArrayToIntArrayFunctionEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EFloatArrayToIntArrayFunctionEnu-) | Dataflow\_FloatToInt\_NonZeroToIndex |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Float array value to convert | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IntArray | Int array output | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
