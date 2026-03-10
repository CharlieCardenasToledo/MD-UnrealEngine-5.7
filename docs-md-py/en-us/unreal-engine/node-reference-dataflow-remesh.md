# Remesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Remesh

> Application Version: 5.7

### Description

Remesh (v2)

Remesh the cloth surface(s) to get the specified mesh resolution(s).
NOTE: Weight Maps, Skinning Data, Self Collision Spheres, and Long Range Attachment Constraints will be reconstructed on the output mesh, however all other Selections will be removed

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Remesh |
| Type | [FChaosClothAssetRemeshNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetRemeshNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bRemeshSim |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DensityMapSim | Range of target mesh resolutions, as a percentage of input triangle mesh resolution. A value of 50 on all vertices should roughly halve the total number of triangles. If a valid vertex weight map is specified, it will use vertex weights to interpolate between the Lo and Hi values. Otherwise it will use the Lo value on all vertices. | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=100.000000,High=200.000000,WeightMap="DensityMapSim",bImportFabricBounds=False,bBuildFabricMaps=False) |
| IterationsSim |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| SmoothingSim |  | double | 0.250000 |
| bRemeshRender |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RemeshMethodRender |  | [EChaosClothAssetRemeshMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetRemeshMethod) | Remesh |
| DensityMapRender | Range of target mesh resolutions when using the Remesh method, as a percentage of input triangle mesh resolution. A value of 50 on all vertices should roughly halve the total number of triangles. If a valid vertex weight map is specified, it will use vertex weights to interpolate between the Lo and Hi values. Otherwise it will use the Lo value on all vertices. | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=100.000000,High=200.000000,WeightMap="DensityMapRender",bImportFabricBounds=False,bBuildFabricMaps=False) |
| TargetPercentRender | Target mesh resolution when using the Simplify method, as a percentage of input triangle mesh resolution. A value of 50 should roughly halve the total number of triangles. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| IterationsRender |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| SmoothingRender |  | double | 0.250000 |
| bRemeshRenderSeams | If checked, attempt to find matching vertices along Render mesh boundaries and remesh these separately | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderSeamRemeshIterations | Number of remesh iterations over the Render mesh seams | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
