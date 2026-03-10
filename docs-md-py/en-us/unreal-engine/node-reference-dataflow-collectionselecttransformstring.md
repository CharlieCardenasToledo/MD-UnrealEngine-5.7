# CollectionSelectTransformString

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString

> Application Version: 5.7

### Description

CollectionSelectTransformString (v1)

Selects transforms by name using a the BoneName attributeor other Transform group string typed attributes

Input(s) :
Collection [Intrinsic] - Collection for the selection
Attribute - Text to serach in the name
SearchText - Text to serach in the name

Output(s):
Collection [Passthrough] - Collection for the selection
TransformSelection - output selection of the matching transforms

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Tags | Name, Bone, Attribute |
| Type | [FCollectionSelectTransformStringDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectTransformString-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Method | Method to use to match the name | [EDataflowCollectionSelectionByNameMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowCollectionSelectionByNa-) | Contains |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SearchText | Text to serach in the name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Attribute | Text to serach in the name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | BoneName |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | output selection of the matching transforms | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
