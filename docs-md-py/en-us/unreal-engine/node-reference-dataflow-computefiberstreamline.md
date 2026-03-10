# ComputeFiberStreamline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline

> Application Version: 5.7

### Description

ComputeFiberStreamline (v1)

Computes fiber streamlines (line segments) flowing from muscle origins to insertions in the muscle fiber field.

Input(s) :
Collection - typedef FManagedArrayCollection DataType;

Output(s):
Collection [Passthrough] - typedef FManagedArrayCollection DataType;

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FComputeFiberStreamlineNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FComputeFiberStreamlineNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OriginInsertionGroupName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OriginVertexFieldName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Origin |
| InsertionVertexFieldName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Insertion |
| MaxStreamlineIterations |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 500 |
| MaxPointsPerLine |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| NumLinesMultiplier |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OriginIndices |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InsertionIndices |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| VectorField |  | [FFieldCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FFieldCollection) |  |
