# SetVisibilityInCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVisibilityInCollection

> Application Version: 5.7

### Description

SetVisibilityInCollection (v1)

Sets all selected bone's visibilty to Visible/Hidden

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to set visibility
TransformSelection [Intrinsic] - Transform selection for setting visibility
FaceSelection [Intrinsic] - Face selection for setting visibility

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to set visibility

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Edit |
| Type | [FSetVisibilityInCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetVisibilityInCollectionDatafl-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Visibility | What to set the visibility of the selected bones | [EVisibiltyOptionsEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EVisibiltyOptionsEnum) | Dataflow\_VisibilityOptions\_Invisible |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to set visibility | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Transform selection for setting visibility | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| FaceSelection | Face selection for setting visibility | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to set visibility | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
