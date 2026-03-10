# FilterSizedOutfit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit

> Application Version: 5.7

### Description

FilterSizedOutfit (v1)
Experimental

Select a single size for the passed Outfit and filter out all non matching sizes.

Input(s) :
Outfit - The outfit to filter.
SizeName - The name of the body size to use to filter.
If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements.
TargetBody - The target body skeletal mesh containing the measurements to select the required size to use to filter.
The target body is unused if Size Name is a valid name.

Output(s):
Outfit [Passthrough] - The outfit to filter.
OutfitCollection - The outfit collection output, provided for convenience as a view into the outfit object metadata.
SizeName [Passthrough] - The name of the body size to use to filter.
If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Filter Sized Outfit |
| Type | FChaosOutfitAssetFilterSizedOutfitNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to filter. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| SizeName | The name of the body size to use to filter. If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| TargetBody | The target body skeletal mesh containing the measurements to select the required size to use to filter. The target body is unused if Size Name is a valid name. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to filter. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| SizeName | The name of the body size to use to filter. If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OutfitCollection | The outfit collection output, provided for convenience as a view into the outfit object metadata. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
