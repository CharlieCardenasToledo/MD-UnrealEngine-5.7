# BoxProjectUV

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV

> Application Version: 5.7

### Description

BoxProjectUV (v1)

Generates UVs using a box projection

Input(s) :
Collection [Intrinsic] - Target Collection
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
| Type | [FBoxProjectUVDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoxProjectUVDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ProjectionScale |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000,Z=100.000000) |
| UVOffset |  | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.500000,Y=0.500000) |
| bAutoFitToBounds |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCenterBoxAtPivot |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bUniformProjectionScale |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| GutterSize | Approximate space to leave between UV islands, measured in texels for 512x512 texture | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
