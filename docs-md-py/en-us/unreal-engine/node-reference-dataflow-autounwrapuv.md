# AutoUnwrapUV

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV

> Application Version: 5.7

### Description

AutoUnwrapUV (v1)

Auto unwrap UVs for a specific UV channel

Input(s) :
Collection [Intrinsic] - Target Collection
FaceSelection - Faces to auto unwrap, no selection means all faces
UVChannel - UV channel to unwrap into ( 0 by default )
GutterSize - Approximate space to leave between UV islands, measured in texels for 512x512 texture

Output(s):
Collection [Passthrough] - Target Collection
UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default )

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|UV |
| Type | [FAutoUnwrapUVDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAutoUnwrapUVDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | Faces to auto unwrap, no selection means all faces | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| GutterSize | Approximate space to leave between UV islands, measured in texels for 512x512 texture | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
