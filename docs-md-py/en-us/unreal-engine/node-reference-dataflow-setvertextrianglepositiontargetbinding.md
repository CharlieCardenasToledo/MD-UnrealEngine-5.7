# SetVertexTrianglePositionTargetBinding

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding

> Application Version: 5.7

### Description

SetVertexTrianglePositionTargetBinding (v1)

Create point-triangle weak constraints (springs) between surface meshes of different geometries based on search radius.

Input(s) :
VertexSelection - (optional) only create weak constraints from surface vertices in VertexSelection to triangles in other geometries

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetVertexTrianglePositionTargetBindingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetVertexTrianglePositionTarget-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PositionTargetStiffness |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SearchRadius | Search radius for point-triangle pairs between geometry surfaces. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bAllowSliding | if point-triangle weak constraints created are anisotropic and allow sliding along the triangle plane | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bZeroRestLengthEditable |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bUseZeroRestLengthSprings | if point-triangle weak constraints created are zero rest-length. if true, this will cause point triangle pair to stick together, as opposed to separated by their rest state distance. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | (optional) only create weak constraints from surface vertices in VertexSelection to triangles in other geometries | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
