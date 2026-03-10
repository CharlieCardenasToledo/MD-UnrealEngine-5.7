# CreateAirTetrahedralConstraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint

> Application Version: 5.7

### Description

CreateAirTetrahedralConstraint (v1)

Create air tetrahedral constraint between point-triangle pair from surface meshes of different geometries based on search radius.
The added tetrahedra help to maintain distance between geometries.
This node renders the boundary of the added tetrahedral mesh.

Input(s) :
VertexSelection - (optional) only create tetrahedral constraints from surface vertices in VertexSelection to triangles in other geometries.
For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries.
No constraints will be created between two geometries that are not in the VertexSelection.

Output(s):
DynamicMesh - Render dynamic mesh of the boundary mesh of added tetrahedra

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCreateAirTetrahedralConstraintDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCreateAirTetrahedralConstraintD-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SearchRadius | tetrahedral constraint search radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | (optional) only create tetrahedral constraints from surface vertices in VertexSelection to triangles in other geometries. For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries. No constraints will be created between two geometries that are not in the VertexSelection. | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| DynamicMesh | Render dynamic mesh of the boundary mesh of added tetrahedra | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
