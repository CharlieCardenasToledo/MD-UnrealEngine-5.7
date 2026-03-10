# UVResizeController

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UVResizeController

> Application Version: 5.7

### Description

UVResizeController (v1)
Experimental

UV Resizing logic.
Returns whether this dynamic mesh is suitable for UV resizing and which UV channels to use.

Input(s) :
Mesh - The input/output Dataflow mesh.

Output(s):
Mesh [Passthrough] - The input/output Dataflow mesh.
UVChannelIndices - The UV channels to resize.
SourceUVChannelIndices - The matching UV channels on the original source mesh.
bHasUVChannelsToResize - Whether the input mesh has any UV channels to resize.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | UV Resize Controller |
| Type | FUVResizeControllerNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TextureSuffix | The texture name suffix . | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Texture |
| UVChannelSuffix | The suffix to replace the texture name with pointing to the UV channel index scalar parameter. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | UVIndex |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | The input/output Dataflow mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | The input/output Dataflow mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| UVChannelIndices | The UV channels to resize. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SourceUVChannelIndices | The matching UV channels on the original source mesh. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| bHasUVChannelsToResize | Whether the input mesh has any UV channels to resize. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
