# CollectionSelectInternalFaces

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectInternalFaces

> Application Version: 5.7

### Description

CollectionSelectInternalFaces (v1)

Select internal faces

Input(s) :
Collection [Intrinsic] - Collection to select the internal faces from
TransformSelection - Transform selection to get the internal faces from
if this input is not connected, then all internal faces from the collection will be returned

Output(s):
Collection [Passthrough] - Collection to select the internal faces from
FaceSelection - selection containing Internal faces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection |
| Type | [FCollectionSelectInternalFacesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectInternalFacesDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to select the internal faces from | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Transform selection to get the internal faces from if this input is not connected, then all internal faces from the collection will be returned | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to select the internal faces from | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| FaceSelection | selection containing Internal faces | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) |  |
