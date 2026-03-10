# CollectionSelectionConvert

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionConvert

> Application Version: 5.7

### Description

CollectionSelectionConvert (v1)

Converts Vertex/Face/Transform selection into Vertex/Face/Transform selection

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
TransformSelection - Transform selection including the new indices
FaceSelection - Face selection including the new indices
VertexSelection - Vertex selection including the new indices

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection [Passthrough] - Transform selection including the new indices
FaceSelection [Passthrough] - Face selection including the new indices
VertexSelection [Passthrough] - Vertex selection including the new indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection |
| Type | [FCollectionSelectionConvertDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionConvertDataf-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAllElementsMustBeSelected | If true then for converting vertex/face selection to transform selection all vertex/face must be selected for selecting the associated transform | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection including the new indices | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| FaceSelection | Face selection including the new indices | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| TransformSelection | Transform selection including the new indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Transform selection including the new indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| FaceSelection | Face selection including the new indices | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) |  |
| VertexSelection | Vertex selection including the new indices | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |
