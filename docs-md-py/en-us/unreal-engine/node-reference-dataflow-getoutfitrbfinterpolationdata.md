# GetOutfitRBFInterpolationData

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData

> Application Version: 5.7

### Description

GetOutfitRBFInterpolationData (v1)
Experimental

Extract the Body Part RBF Interpolation Data from an outfit.

Input(s) :
Outfit - The source outfit.
BodySizeIndex - The body size index.
BodyPartIndex - The body part (sub) index.

Output(s):
Outfit [Passthrough] - The source outfit.
InterpolationData - The interpolation data.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit RBF Interpolation Data |
| Type | FChaosGetOutfitRBFInterpolationDataNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| BodySizeIndex | The body size index. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| BodyPartIndex | The body part (sub) index. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| InterpolationData | The interpolation data. | [FMeshResizingRBFInterpolationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) |  |
