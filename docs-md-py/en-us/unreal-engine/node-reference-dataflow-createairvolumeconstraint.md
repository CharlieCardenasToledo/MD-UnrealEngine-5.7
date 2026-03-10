# CreateAirVolumeConstraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirVolumeConstraint

> Application Version: 5.7

### Description

CreateAirVolumeConstraint (v1)
Experimental

Creates volume constraint (defined by point-triangle tetrahedron volume) between surface meshes of different geometries.
This constraint allow sliding of the point along the triangle plane.

Input(s) :
VertexSelection - (optional) only create volume constraints from surface vertices in VertexSelection to triangles in other geometries.
For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries.
No constraints will be created between two geometries that are not in the VertexSelection.

Output(s):
DynamicMesh - Render dynamic mesh of the boundary mesh of added volume

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCreateAirVolumeConstraintDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCreateAirVolumeConstraintDatafl-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SearchRadius | search radius for point-triangle pairs | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Stiffness | Stiffness of the volume constraint. This should be around the same magnitude as Young's modulus. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | (optional) only create volume constraints from surface vertices in VertexSelection to triangles in other geometries. For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries. No constraints will be created between two geometries that are not in the VertexSelection. | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| DynamicMesh | Render dynamic mesh of the boundary mesh of added volume | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
