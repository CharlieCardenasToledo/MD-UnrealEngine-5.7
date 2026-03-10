# MakeSizedOutfit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSizedOutfit

> Application Version: 5.7

### Description

MakeSizedOutfit (v1)
Experimental

Add multiple cloth asset objects to an outfit collection.

Output(s):
Outfit - The outfit output.
OutfitCollection - The outfit collection output, provided for convenience as a view into the outfit object metadata.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Cloth Asset Make Sized Outfit |
| Type | FChaosOutfitAssetMakeSizedOutfitNode |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit output. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| OutfitCollection | The outfit collection output, provided for convenience as a view into the outfit object metadata. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
