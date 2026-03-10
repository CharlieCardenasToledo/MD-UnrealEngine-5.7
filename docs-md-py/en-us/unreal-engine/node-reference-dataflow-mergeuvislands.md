# MergeUVIslands

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeUVIslands

> Application Version: 5.7

### Description

MergeUVIslands (v1)

Merge adjacent UV Islands with similar normals for a specific UV channel

Input(s) :
Collection [Intrinsic] - Target Collection
FaceSelection - Faces to auto unwrap, no selection means all faces
UVChannel - UV channel to unwrap into ( 0 by default )
AreaDistortionThreshold - Threshold for allowed area distortion from merging islands (when we use ExpMap to compute new UVs for the merged island)
MaxNormalDeviationDeg - Threshold for allowed normal deviation between merge-able islands
NormalSmoothingRounds - Amount of normal smoothing to apply when computing new UVs for merged islands. More smoothing will result in UV maps that are less sensitive to local surface shape.
NormalSmoothingAlpha - Strength of normal smoothing to apply when computing new UVs for merged islands. Stronger smoothing will result in UV maps that are less sensitive to local surface shape.

Output(s):
Collection [Passthrough] - Target Collection
UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default )

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|UV |
| Type | [FMergeUVIslandsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMergeUVIslandsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | Faces to auto unwrap, no selection means all faces | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| AreaDistortionThreshold | Threshold for allowed area distortion from merging islands (when we use ExpMap to compute new UVs for the merged island) | double | 1.500000 |
| MaxNormalDeviationDeg | Threshold for allowed normal deviation between merge-able islands | double | 45.000000 |
| NormalSmoothingRounds | Amount of normal smoothing to apply when computing new UVs for merged islands. More smoothing will result in UV maps that are less sensitive to local surface shape. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| NormalSmoothingAlpha | Strength of normal smoothing to apply when computing new UVs for merged islands. Stronger smoothing will result in UV maps that are less sensitive to local surface shape. | double | 0.250000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
