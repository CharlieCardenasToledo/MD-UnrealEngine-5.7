# GroomAssetToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection

> Application Version: 5.7

### Description

GroomAssetToCollection (v1)
Experimental

Transform a groom asset to a collection

Input(s) :
GroomAsset - Input asset to read the guides from
CurvesType - Type of curves to use to fill the groom collection (guides/strands)
CurvesThickness - Curves thickness for geometry generation

Output(s):
Collection - Managed array collection used to store the curves

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGroomAssetToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGroomAssetToCollectionDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroomAsset | Input asset to read the guides from | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGroomAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsCore/UGroomAsset)> | None |
| CurvesThickness | Curves thickness for geometry generation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| CurvesType | Type of curves to use to fill the groom collection (guides/strands) | [EGroomCollectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/EGroomCollectionType) | Guides |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection used to store the curves | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
