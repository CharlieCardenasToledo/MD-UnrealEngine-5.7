# GenerateRBFResizingWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights

> Application Version: 5.7

### Description

GenerateRBFResizingWeights (v1)
Experimental

Sample points and generate RBF Interpolation data for a given Source mesh.

Input(s) :
MeshToResize - The mesh to resize. This is currently unused but may be used to improve point sampling in the future.
SourceMesh - The source mesh to be sampled.
NumInterpolationPoints - The number of interpolation points to be sampled.

Output(s):
InterpolationData - The calculated interpolation points and RBF weights

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Generate RBF Resizing Weights |
| Type | FGenerateRBFResizingWeightsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceMesh | The source mesh to be sampled. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| NumInterpolationPoints | The number of interpolation points to be sampled. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1500 |
| MeshToResize | The mesh to resize. This is currently unused but may be used to improve point sampling in the future. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InterpolationData | The calculated interpolation points and RBF weights | [FMeshResizingRBFInterpolationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) |  |
