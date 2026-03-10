# PlaneFalloffField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PlaneFalloffField

> Application Version: 5.7

### Description

PlaneFalloffField (v1)

PlaneFalloff Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FPlaneFalloffFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FPlaneFalloffFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FalloffType |  | [EDataflowFieldFalloffType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowFieldFalloffType) | Dataflow\_FieldFalloffType\_Linear |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Position |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Normal |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| Distance |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Translation |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MinRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Default |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldSelectionMask |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
