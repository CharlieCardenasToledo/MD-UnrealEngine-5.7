# GetOutfitClothCollections

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections

> Application Version: 5.7

### Description

GetOutfitClothCollections (v1)
Experimental

Extract the cloth collections contained into the specified source outfit.

Input(s) :
Outfit - The source outfit.
LodIndex - The LOD to output in the cloth collections array. Set to -1 to output all LODs

Output(s):
Outfit [Passthrough] - The source outfit.
ClothCollections - The outfit cloth collections array in group of consecutives LODs for each of the outfit pieces.
NumLods - The number of LODs output in the cloth collections array.
NumPieces - The number of cloth pieces output in the cloth collections array.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Cloth Collections |
| Type | FChaosGetOutfitClothCollectionsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| LodIndex | The LOD to output in the cloth collections array. Set to -1 to output all LODs | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| ClothCollections | The outfit cloth collections array in group of consecutives LODs for each of the outfit pieces. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |
| NumLods | The number of LODs output in the cloth collections array. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| NumPieces | The number of cloth pieces output in the cloth collections array. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
