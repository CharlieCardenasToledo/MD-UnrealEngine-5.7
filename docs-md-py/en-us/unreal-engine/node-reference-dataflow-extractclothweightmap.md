# ExtractClothWeightMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothWeightMap

> Application Version: 5.7

### Description

ExtractClothWeightMap (v1)
Experimental

Extract a weight map from a Cloth Collection.

Input(s) :
WeightMap - Name of the weight map to be extracted
DynamicMesh - Dynamic mesh used to reorder weights.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Extract Cloth Weight Map |
| Type | [FChaosClothAssetExtractWeightMapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetExtractWeightMap-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshTarget | Type of the weight map to be extracted | [EChaosClothAssetWeightMapMeshTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapMeshTar-) | Simulation |
| bReorderForDynamicMesh | Reorder extracted weights to match the order of a DynamicMesh that was created via ClothCollectionToDynamicMesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DynamicMesh | Dynamic mesh used to reorder weights. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExtractedWeightMap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
