# SetOutfitClothCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetOutfitClothCollection

> Application Version: 5.7

### Description

SetOutfitClothCollection (v1)
Experimental

Replace the ClothCollection in an Outfit with a new one.
Any data derived from the ClothCollection (e.g., Simulation Model, Render Data) will NOT be regenerated in the Outfit.

Input(s) :
Outfit - The outfit to be edited.
ClothCollection - The replacement cloth collection.
PieceIndex - The Outfit Piece to replace.
LODIndex - The Outfit LOD to replace.

Output(s):
Outfit [Passthrough] - The outfit to be edited.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Cloth Collections |
| Type | FChaosSetOutfitClothCollectionNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to be edited. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| ClothCollection | The replacement cloth collection. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| PieceIndex | The Outfit Piece to replace. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| LODIndex | The Outfit LOD to replace. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to be edited. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
