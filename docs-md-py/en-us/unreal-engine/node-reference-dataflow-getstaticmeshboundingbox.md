# GetStaticMeshBoundingBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetStaticMeshBoundingBox

> Application Version: 5.7

### Description

GetStaticMeshBoundingBox (v1)

Get the local geometric bounding box a static mesh

Input(s) :
StaticMesh - Static Mesh to compute the bouning box from

Output(s):
BoundingBox - Geometric bounding box of the input Static Mesh
Center - Center of the resulting bounding box
Dimensions - Dimensions of the resulting bounding box in centimers

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Static Mesh |
| Tags | Bounds Size Dimensions Extents Center |
| Type | [FGetStaticMeshBoundingBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FGetStaticMeshBoundingBoxDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StaticMesh | Static Mesh to compute the bouning box from | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | Geometric bounding box of the input Static Mesh | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center | Center of the resulting bounding box | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Dimensions | Dimensions of the resulting bounding box in centimers | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
