# GetBoundingBoxesFromCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoundingBoxesFromCollection

> Application Version: 5.7

### Description

GetBoundingBoxesFromCollection (v1)

Gets BoundingBoxes of pieces from a Collection

Input(s) :
Collection - Input Collection
TransformSelection - The BoundingBoxes will be output for the bones selected in the TransformSelection

Output(s):
BoundingBoxes - Output BoundingBoxes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetBoundingBoxesFromCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetBoundingBoxesFromCollectionD-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The BoundingBoxes will be output for the bones selected in the TransformSelection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBoxes | Output BoundingBoxes | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
