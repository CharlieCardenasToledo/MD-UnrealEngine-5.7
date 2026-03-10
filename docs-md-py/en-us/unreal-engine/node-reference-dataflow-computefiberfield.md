# ComputeFiberField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField

> Application Version: 5.7

### Description

ComputeFiberField (v1)

Computes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra,
vertices, and origin & insertion vertex fields. Fiber directions should smoothly follow the geometry
oriented from the origin vertices pointing to the insertion vertices.

Input(s) :
Collection - typedef FManagedArrayCollection DataType;

Output(s):
Collection [Passthrough] - typedef FManagedArrayCollection DataType;

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FComputeFiberFieldNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FComputeFiberFieldNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OriginInsertionGroupName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OriginVertexFieldName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Origin |
| InsertionVertexFieldName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Insertion |
| MaxIterations |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| Tolerance |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bShowMuscleColor | If muscles are colored by the flow from origins (blue) to insertions (red). This becomes optional in 5.6 | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

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
