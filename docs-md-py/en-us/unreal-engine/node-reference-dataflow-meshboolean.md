# MeshBoolean

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshBoolean

> Application Version: 5.7

### Description

MeshBoolean (v1)

Compute a Mesh Boolean between Mesh1 and Mesh2

Supported Boolean Operations:
Union (Mesh1 + Mesh2)
Difference (Mesh1 - Mesh2; removing what's inside of Mesh2 from Mesh1)
Intersection (Mesh1 & Mesh2; removing what's outside of Mesh2 from Mesh1)

Input(s) :
Mesh1 [Intrinsic] - Mesh input
Mesh2 [Intrinsic] - Mesh input

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryDataflowNodes) |
| Category | Mesh|Utilities |
| Type | [FMeshBooleanDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryDataflowNodes/FMeshBooleanDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Boolean operation | [EMeshBooleanOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryDataflowNodes/EMeshBooleanOperationEnum) | Dataflow\_MeshBoolean\_Intersect |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh1 | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| Mesh2 | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
