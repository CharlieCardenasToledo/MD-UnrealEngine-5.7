# UniformPointSampling

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling

> Application Version: 5.7

### Description

UniformPointSampling (v1)

Uniform Sampling on a DynamicMesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to sample points on
SamplingRadius - Desired "radius" of sample points. Spacing between samples is at least 2x this value.
MaxNumSamples - Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled
SubSampleDensity - Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results.
RandomSeed - Random Seed used to initialize sampling strategies

Output(s):
SamplePoints - Sampled positions on the mesh
SampleTriangleIDs - Sampled triangleID
SampleBarycentricCoords - Barycentric Coordinates of each Sample Point in it's respective Triangle.
NumSamplePoints - Number of Sampled positions on the mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | [FUniformPointSamplingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUniformPointSamplingDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to sample points on | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SamplingRadius | Desired "radius" of sample points. Spacing between samples is at least 2x this value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MaxNumSamples | Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SubSampleDensity | Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| RandomSeed | Random Seed used to initialize sampling strategies | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Sampled positions on the mesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleTriangleIDs | Sampled triangleID | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleBarycentricCoords | Barycentric Coordinates of each Sample Point in it's respective Triangle. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePoints | Number of Sampled positions on the mesh | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
