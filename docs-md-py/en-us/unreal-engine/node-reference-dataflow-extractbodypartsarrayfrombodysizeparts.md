# ExtractBodyPartsArrayFromBodySizeParts

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractBodyPartsArrayFromBodySizeParts

> Application Version: 5.7

### Description

ExtractBodyPartsArrayFromBodySizeParts (v1)
Experimental

Extract the array of BodyParts from a FChaosOutfitBodySizeBodyParts

Input(s) :
BodySizeParts - The source outfit.

Output(s):
BodyParts - The outfit body parts grouped by BodySize.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Extract Outfit Body Parts Skeletal Mesh |
| Type | FChaosExtractBodyPartsArrayFromBodySizePartsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BodySizeParts | The source outfit. | FChaosOutfitBodySizeBodyParts | (BodyParts=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BodyParts | The outfit body parts grouped by BodySize. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)>> |  |
