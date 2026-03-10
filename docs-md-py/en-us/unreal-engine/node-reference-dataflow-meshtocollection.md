# MeshToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshToCollection

> Application Version: 5.7

### Description

MeshToCollection (v1)

Converts a DynamicMesh to a Collection

Input(s) :
Mesh [Intrinsic] - DynamicMesh to convert
bSplitIslands - Whether to split the mesh into multiple bones based on the mesh connectivity
bAddClusterRootForSingleMesh - Whether to add a root cluster for the single mesh case. Note if the mesh is split, the root cluster will always be added.

Output(s):
Collection - Output Collection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FMeshToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshToCollectionDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bConnectIslandsByVertexOverlap | Whether to consider coincident vertices as connected even if the topology does not connect them | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ConnectVerticesThreshold | Vertices closer than this distance are considered to be overlapping | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.001000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DynamicMesh to convert | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| bSplitIslands | Whether to split the mesh into multiple bones based on the mesh connectivity | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bAddClusterRootForSingleMesh | Whether to add a root cluster for the single mesh case. Note if the mesh is split, the root cluster will always be added. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Output Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
