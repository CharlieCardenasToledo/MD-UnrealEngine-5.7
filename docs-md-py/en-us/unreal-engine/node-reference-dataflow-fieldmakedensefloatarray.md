# FieldMakeDenseFloatArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray

> Application Version: 5.7

### Description

FieldMakeDenseFloatArray (v1)

Converts a sparse FloatArray (a selected subset of the whole incoming array) into a dense FloatArray
(same number of elements as the incoming array using NumSamplePositions) using the Remap input
NumSamplePositions controls the size of the output array, only indices smaller than l to than NumSamplePositions
will be processed

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FFieldMakeDenseFloatArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFieldMakeDenseFloatArrayDataflo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Default |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatInput |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
