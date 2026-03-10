# UVUnwrapNode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UVUnwrapNode

> Application Version: 5.7

### Description

UVUnwrapNode (v1)
Experimental

UVUnwrap Node

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | UV Unwrap |
| Type | FUVUnwrapNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Method |  | EUVUnwrapMethod | SpectralConformal |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| UVChannelIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| UVChannelIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
