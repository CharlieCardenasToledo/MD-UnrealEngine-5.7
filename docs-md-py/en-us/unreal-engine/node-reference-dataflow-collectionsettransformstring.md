# CollectionSetTransformString

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSetTransformString

> Application Version: 5.7

### Description

CollectionSetTransformString (v1)

Set selected transform string value
the string format can use the following predefined value :

* {Current} current value of the attribute
* {Index} index in the selection passed as input

Input(s) :
Collection [Intrinsic] - Collection for the selection
TransformSelection - input selection of the transforms to set - if not connected use all
Attribute - Text to serach in the name
TextToSet - Text to set

Output(s):
Collection [Passthrough] - Collection for the selection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Tags | Bone Name Attribute |
| Type | [FCollectionSetTransformStringValueDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSetTr-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TextToSet | Text to set | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| TransformSelection | input selection of the transforms to set - if not connected use all | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Attribute | Text to serach in the name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | BoneName |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
