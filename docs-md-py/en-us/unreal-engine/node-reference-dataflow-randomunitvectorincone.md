# RandomUnitVectorInCone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone

> Application Version: 5.7

### Description

RandomUnitVectorInCone (v1)

Returns a random vector with length of 1, within the specified cone, with uniform random distribution

Input(s) :
ConeDirection - The base "center" direction of the cone
ConeHalfAngle - The half-angle of the cone (from ConeDir to edge), in degrees

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Random |
| Type | [FRandomUnitVectorInConeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRandomUnitVectorInConeDataflowN-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeterministic |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RandomSeed |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -56694.234375 |
| ConeDirection | The base "center" direction of the cone | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| ConeHalfAngle | The half-angle of the cone (from ConeDir to edge), in degrees | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.785398 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
