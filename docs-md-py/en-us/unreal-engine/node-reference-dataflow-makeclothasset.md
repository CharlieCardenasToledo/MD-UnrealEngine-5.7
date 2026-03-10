# MakeClothAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeClothAsset

> Application Version: 5.7

### Description

MakeClothAsset (v1)
Experimental

Cloth terminal node to generate a cloth asset from a cloth collection.

Input(s) :
CollectionLodsArray - Input cloth collections for this LOD -- Array connection. Individual CollectionLods will be ignored if there is a CollectionLodsArray connection.

Output(s):
ClothAsset - The cloth asset output.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Make Cloth Asset |
| Type | FChaosClothAssetMakeClothAssetNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CollectionLodsArray | Input cloth collections for this LOD -- Array connection. Individual CollectionLods will be ignored if there is a CollectionLodsArray connection. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClothAsset | The cloth asset output. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosClothAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetEngine/UChaosClothAsset)> |  |
