# FloatArrayComputeStatistics

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics

> Application Version: 5.7

### Description

FloatArrayComputeStatistics (v1)

Computes statistics of a float array

Input(s) :
FloatArray [Intrinsic] - Array to compute values from
TransformSelection - TransformSelection describes which values to use, if not connected all the elements will be used

Output(s):
Value - Computed value
Indices - Indices of elements with the computed value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Type | [FFloatArrayComputeStatisticsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayComputeStatisticsData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OperationName | Statistics Operation | [EStatisticsOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStatisticsOperationEnum) | Dataflow\_EStatisticsOperationEnum\_Min |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Array to compute values from | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| TransformSelection | TransformSelection describes which values to use, if not connected all the elements will be used | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | Computed value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Indices | Indices of elements with the computed value | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
