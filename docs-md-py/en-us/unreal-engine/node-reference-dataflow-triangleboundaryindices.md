# TriangleBoundaryIndices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TriangleBoundaryIndices

> Application Version: 5.7

### Description

TriangleBoundaryIndices (v1)
Experimental

Outputs boundary nodes of a triangle mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Flesh|Experimental |
| Type | [FTriangleBoundaryIndicesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FTriangleBoundaryIndicesNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundaryIndicesOut |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
