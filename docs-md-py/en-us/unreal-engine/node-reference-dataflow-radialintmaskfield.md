# RadialIntMaskField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialIntMaskField

> Application Version: 5.7

### Description

RadialIntMaskField (v1)

RadialIntMask Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FRadialIntMaskFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRadialIntMaskFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SetMaskConditionType |  | [EDataflowSetMaskConditionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowSetMaskConditionType) | Dataflow\_SetMaskConditionType\_Always |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Sphere |  | [FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Center=(X=0.000000,Y=0.000000,Z=0.000000),W=0.000000) |
| Translation |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| InteriorValue |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| ExteriorValue |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldIntResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
