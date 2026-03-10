# GetOrMakeOutfitFromAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOrMakeOutfitFromAsset

> Application Version: 5.7

### Description

GetOrMakeOutfitFromAsset (v1)
Experimental

Extract the Outfit from an Outfit Asset.
If the Outfit does not exist (e.g., this OutfitAsset has been cooked),
recreate a new one.

Input(s) :
OutfitAsset - The outfit asset input.

Output(s):
Outfit - The outfit output.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Get Make Outfit |
| Type | FChaosOutfitAssetGetOrMakeOutfitFromAssetNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutfitAsset | The outfit asset input. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfitAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfitAsset)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit output. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
