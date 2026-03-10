# MeshWarp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWarp

> Application Version: 5.7

### Description

MeshWarp (v1)
Experimental

Mesh Warp Node

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Warp |
| Type | FMeshWarpNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Alpha |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| WarpMethod |  | EMeshResizingWarpMethod | RBFInterpolate |
| NumInterpolationPoints |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| bInterpolateNormals |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshToResize |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| SourceMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| TargetMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BlendedTargetMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| ResizedMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
