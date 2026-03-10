# OutfitAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitAssetTerminal

> Application Version: 5.7

### Description

OutfitAssetTerminal (v1)
Experimental

Outfit terminal node to generate an outfit asset from several cloth assets.

Input(s) :
Outfit - Input outfit collection.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Terminal |
| Type | FChaosOutfitAssetTerminalNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ConvertToSkeletalMesh | Convert this outfit to a SkeletalMesh asset. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | Input outfit collection. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
