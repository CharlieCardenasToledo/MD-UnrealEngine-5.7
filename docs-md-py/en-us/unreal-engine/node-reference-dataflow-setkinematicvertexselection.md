# SetKinematicVertexSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetKinematicVertexSelection

> Application Version: 5.7

### Description

SetKinematicVertexSelection (v1)

Set VertexSelection to be kinematic. Note that kinematic particles need skin weights.

Input(s) :
VertexSelection - Vertex Selection set to be kinematic

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Tags | Set Vertex Collection to be kinematic |
| Type | [FGeometryCollectionSetKinematicVertexSelectionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| KinematicValue |  | [ESetKinematicVertexSelectionKinematicValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESetKinematicVertexSelectionKine-) | SetKinematic |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex Selection set to be kinematic | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
