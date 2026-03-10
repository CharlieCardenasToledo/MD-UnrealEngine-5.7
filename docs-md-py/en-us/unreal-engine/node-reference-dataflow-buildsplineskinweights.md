# BuildSplineSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights

> Application Version: 5.7

### Description

BuildSplineSkinWeights (v1)
Experimental

Build spline skinning data from skeletal mesh

Input(s) :
Collection - Managed array collection to be used to store datas
VertexSelection - Vertex selection to focus the geometry transfer spatially
SkeletalMesh - SkeletalMesh used to compute spline skinning weights. Will be stored onto the groom asset
LODIndex - LOD used to build skinning weights
RootBones - Root bones to be used for spline skinning. Uses all bones if empty. Note that branches in the skeleton is currently not supported.
SamplesPerSegment - Number of spline samples per bone segment.

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
SplineParamKey - Spline Skinning Parameter key
SplineBonesKey - Spline Bones key containing root and end spline bone. To be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildSplineSkinWeightsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildSplineSkinWeightsDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection to focus the geometry transfer spatially | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| SkeletalMesh | SkeletalMesh used to compute spline skinning weights. Will be stored onto the groom asset | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| LODIndex | LOD used to build skinning weights | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| RootBones | Root bones to be used for spline skinning. Uses all bones if empty. Note that branches in the skeleton is currently not supported. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| SamplesPerSegment | Number of spline samples per bone segment. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 64 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SplineParamKey | Spline Skinning Parameter key | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| SplineBonesKey | Spline Bones key containing root and end spline bone. To be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
