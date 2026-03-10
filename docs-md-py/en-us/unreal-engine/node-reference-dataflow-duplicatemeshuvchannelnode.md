# DuplicateMeshUVChannelNode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode

> Application Version: 5.7

### Description

DuplicateMeshUVChannelNode (v1)

Create a new UV layer/channel in a UDataflowMesh

Input(s) :
Mesh [Intrinsic] - DataflowMesh input/output

Output(s):
Mesh [Passthrough] - DataflowMesh input/output
NewUVChannel - Index of the added UV channel

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Tags | Mesh UV DataflowMesh |
| Type | [FDuplicateMeshUVChannelNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDuplicateMeshUVChannelNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceUVChannel | Index of the source UV channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DataflowMesh input/output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DataflowMesh input/output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| NewUVChannel | Index of the added UV channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
