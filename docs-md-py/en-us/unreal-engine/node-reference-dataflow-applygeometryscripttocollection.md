# ApplyGeometryScriptToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyGeometryScriptToCollection

> Application Version: 5.7

### Description

ApplyGeometryScriptToCollection (v1)

Apply a Geometry Script Mesh Processors to the geometry of selected transforms in a geometry collection

Input(s) :
Collection [Intrinsic] - Input/Output mesh
TransformSelection - Selected bones will have geometry script processing applied (if they have geometry). If not connected, all geometry will be processed.

Output(s):
Collection [Passthrough] - Input/Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FApplyMeshProcessorToGeometryCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FApplyMeshProces-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bWeldVertices | Whether the processed mesh will have edges at normal/UV/color seams welded so they are treated as one edge during processing. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bPreserveIsolatedVertices | Whether to preserve isolated vertices which aren't used by any triangles. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/Output mesh | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Selected bones will have geometry script processing applied (if they have geometry). If not connected, all geometry will be processed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/Output mesh | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
