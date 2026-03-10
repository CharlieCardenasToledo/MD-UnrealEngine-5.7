# AuthorSceneCollisionCandidates

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates

> Application Version: 5.7

### Description

AuthorSceneCollisionCandidates (v1)

Marks mesh vertices as candidates for scene collision raycasts. Each vertex has an associated
bone index to use as the origin of the raycast. The runtime distance between the vertex and the
bone designates the range of the scene query depth.

Input(s) :
VertexIndices - ! Indices to use with environment collisions. If this input is not connected, then all
! indicies are used.
OriginBoneIndex - ! Bone index to use as the world raycast origin. -1 denotes the component transform.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAuthorSceneCollisionCandidates](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAuthorSceneCollisionCandidates) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSurfaceVerticesOnly | ! Restricts vertices to only ones on the surface. All vertices otherwise. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexIndices | ! Indices to use with environment collisions. If this input is not connected, then all ! indicies are used. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| OriginBoneIndex | ! Bone index to use as the world raycast origin. -1 denotes the component transform. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
