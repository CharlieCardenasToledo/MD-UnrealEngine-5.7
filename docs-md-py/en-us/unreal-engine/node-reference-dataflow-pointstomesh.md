# PointsToMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PointsToMesh

> Application Version: 5.7

### Description

PointsToMesh (v1)

Converts points into a DynamicMesh

Input(s) :
Points [Intrinsic] - Points input

Output(s):
Mesh - Mesh output
TriangleCount - Mesh triangle count

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FPointsToMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FPointsToMeshDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Points input | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Mesh output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| TriangleCount | Mesh triangle count | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
