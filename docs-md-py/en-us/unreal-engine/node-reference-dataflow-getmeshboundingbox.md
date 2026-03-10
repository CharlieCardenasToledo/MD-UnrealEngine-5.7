# GetMeshBoundingBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox

> Application Version: 5.7

### Description

GetMeshBoundingBox (v1)

Get the local geometric bounding box a dynamic mesh

Input(s) :
Mesh - dynamic mesh to compute the bouning box from

Output(s):
BoundingBox - Geometric bounding box of the input dynamic mesh
Center - Center of the resulting bounding box
Dimensions - Dimensions of the resulting bounding box in centimers

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh |
| Tags | Bounds Size Dimensions Extents Center |
| Type | [FGetMeshBoundingBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetMeshBoundingBoxDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | dynamic mesh to compute the bouning box from | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | Geometric bounding box of the input dynamic mesh | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center | Center of the resulting bounding box | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Dimensions | Dimensions of the resulting bounding box in centimers | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
