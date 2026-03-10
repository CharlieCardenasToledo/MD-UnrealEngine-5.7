# VertexWeightedPointSampling

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VertexWeightedPointSampling

> Application Version: 5.7

### Description

VertexWeightedPointSampling (v1)

VertexWeighted Sampling on a DynamicMesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to sample points on
VertexWeights [Intrinsic] - Weight array
SamplingRadius - Desired "radius" of sample points. Spacing between samples is at least 2x this value.
MaxNumSamples - Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled
SubSampleDensity - Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results.
RandomSeed - Random Seed used to initialize sampling strategies
MaxSamplingRadius - If MaxSampleRadius > SampleRadius, then output sample radius will be in range [SampleRadius, MaxSampleRadius]
SizeDistributionPower - SizeDistributionPower is used to control how extreme the Size Distribution shift is. Valid range is [1,10]

Output(s):
SamplePoints - Sampled positions on the mesh
SampleRadii - Sampled radii
SampleTriangleIDs - Sampled triangleID
SampleBarycentricCoords - Barycentric Coordinates of each Sample Point in it's respective Triangle.
NumSamplePoints - Number of Sampled positions on the mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | [FVertexWeightedPointSamplingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVertexWeightedPointSamplingData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SizeDistribution | SizeDistribution setting controls the distribution of sample radii | [ENonUniformSamplingDistributionMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/ENonUniformSamplingDistributionM-) | ENonUniformSamplingDistributionMode\_Uniform |
| WeightMode |  | [ENonUniformSamplingWeightMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/ENonUniformSamplingWeightMode) | ENonUniformSamplingWeightMode\_WeightedRandom |
| bInvertWeights |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to sample points on | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| VertexWeights | Weight array | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| SamplingRadius | Desired "radius" of sample points. Spacing between samples is at least 2x this value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MaxNumSamples | Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SubSampleDensity | Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| RandomSeed | Random Seed used to initialize sampling strategies | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MaxSamplingRadius | If MaxSampleRadius > SampleRadius, then output sample radius will be in range [SampleRadius, MaxSampleRadius] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| SizeDistributionPower | SizeDistributionPower is used to control how extreme the Size Distribution shift is. Valid range is [1,10] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Sampled positions on the mesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleRadii | Sampled radii | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| SampleTriangleIDs | Sampled triangleID | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleBarycentricCoords | Barycentric Coordinates of each Sample Point in it's respective Triangle. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePoints | Number of Sampled positions on the mesh | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
