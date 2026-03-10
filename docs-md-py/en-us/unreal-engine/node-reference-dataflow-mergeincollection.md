# MergeInCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeInCollection

> Application Version: 5.7

### Description

MergeInCollection (v1)

Merges selected bones into a single bone

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to merge
TransformSelection [Intrinsic] - Transform selection for merging

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to merge

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Edit |
| Type | [FMergeInCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMergeInCollectionDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to merge | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Transform selection for merging | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to merge | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
