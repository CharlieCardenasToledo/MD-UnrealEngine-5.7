# OutfitQuery

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery

> Application Version: 5.7

### Description

OutfitQuery (v1)

Query an Outfit about its properties.

Input(s) :
Outfit - Input/output collection (Output is always a passthrough)

Output(s):
Outfit [Passthrough] - Input/output collection (Output is always a passthrough)
bHasAnyValidPieces - Has this outfit any valid pieces?
bHasAnyValidBodySizes - Has this outfit any valid body sizes?

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Query |
| Type | FChaosOutfitAssetOutfitQueryNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bBodyPartMustExist | Check that body parts are present in the asset registry when checking for valid body sizes. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bMeasurementsMustExist | Check that measurements are valid when checking for valid body sizes. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bInterpolationDataMustExist | Check that some interpolation data exists when checking for valid body sizes. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | Input/output collection (Output is always a passthrough) | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | Input/output collection (Output is always a passthrough) | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| bHasAnyValidPieces | Has this outfit any valid pieces? | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasAnyValidBodySizes | Has this outfit any valid body sizes? | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
