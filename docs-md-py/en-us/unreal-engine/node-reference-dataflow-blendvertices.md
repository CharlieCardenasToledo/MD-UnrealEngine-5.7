# BlendVertices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices

> Application Version: 5.7

### Description

BlendVertices (v1)

Blend vertex values from another cloth collection. The topology of the Collection will remain the same.

Input(s) :
Collection - Input/output collection
BlendCollection - Collection to blend in.

Output(s):
Collection [Passthrough] - Input/output collection

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Blend Vertices |
| Type | [FChaosClothAssetBlendVerticesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetBlendVerticesNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bRequireSameVertexCounts | Require same vertex counts between Collection and BlendCollection in order to blend a vertex type. Otherwise the shared subset will be blended. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| BlendingWeight | Blending Weight. 0 = Keep existing values in Collection. 1 = Set values from BlendCollection. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bBlendSimMesh | Blend Sim Mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlend2DSimPositions | Blend 2D Sim Positions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlend3DSimPositions | Blend 3D Sim Positions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendSimNormals | Blend 3D Sim Normals. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderMesh | Blend Render Mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderPositions | Blend Render Positions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderNormalsAndTangents | Blend Render Normals and Tangents. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderUVs | Blend Render UVs. Only existing UV sets on Collection will be updated. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderColors | Blend Render Colors. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BlendCollection | Collection to blend in. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
