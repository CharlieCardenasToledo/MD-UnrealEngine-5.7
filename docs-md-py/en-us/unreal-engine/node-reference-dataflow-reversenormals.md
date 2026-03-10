# ReverseNormals

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals

> Application Version: 5.7

### Description

ReverseNormals (v1)

Reverse the geometry's normals or/and winding order of the simulation or/and render meshes stored in the cloth collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Reverse Simulation Render Mesh Normals |
| Type | [FChaosClothAssetReverseNormalsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetReverseNormalsNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimPatterns | List of sim patterns to apply the operation on. All patterns will be used if left empty. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bReverseSimMeshNormals | Whether to reverse the simulation mesh normals. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bReverseSimMeshWindingOrder | Whether to reverse the simulation mesh triangles' winding order. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderPatterns | List of render patterns to apply the operation on. All patterns will be used if left empty. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bReverseRenderMeshNormals | Whether to reverse the render mesh normals. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bReverseRenderMeshWindingOrder | Whether to reverse the render mesh triangles' winding order. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
