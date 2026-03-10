# CreateTetrahedron

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron

> Application Version: 5.7

### Description

CreateTetrahedron (v1)

Create Tetrahedron Dataflow Node

Input(s) :
Collection - Input pass-through collection. When connected, the generated tetrahedron will be nested into
its associated parents transform.
SourceCollection - Source collection used to generate the tetrahedron from. Closed geometry within the collections geometry group will be used to
generate tetrahedron.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCreateTetrahedronDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCreateTetrahedronDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Method | Tetrahedral meshing method (TetWild or ISO-stuffing) | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[TetMeshingMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/TetMeshingMethod)> | IsoStuffing |
| Selection | Name of the mesh in the collection. This is defined from the name of the mesh's parent transform. CollectionKey("BoneName","Vertices") | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| NumCells | General control for density for the tetrahedron. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 32 |
| OffsetPercent | Surface offset percentage to increase or decrease the surface alignment. | double | 0.050000 |
| IdealEdgeLengthRel | ! Desired relative edge length, as a fraction of bounding box size | double | 0.050000 |
| MaxIterations | ! Maximum number of optimization iterations. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 80 |
| StopEnergy | ! Energy at which to stop optimizing tet quality and accept the result. | double | 10.000000 |
| EpsRel | ! Relative tolerance, controlling how closely the mesh must follow the input surface. | double | 0.001000 |
| bCoarsen | ! Coarsen the tet mesh result. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bExtractManifoldBoundarySurface | ! Enforce that the output boundary surface should be manifold. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bSkipSimplification | ! Skip the initial simplification step. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bInvertOutputTets | ! Invert tetrahedra. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDiscardInteriorTriangles | Common | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input pass-through collection. When connected, the generated tetrahedron will be nested into its associated parents transform. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SourceCollection | Source collection used to generate the tetrahedron from. Closed geometry within the collections geometry group will be used to generate tetrahedron. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input pass-through collection. When connected, the generated tetrahedron will be nested into its associated parents transform. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
