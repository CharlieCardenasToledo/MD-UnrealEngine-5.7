# BreakTransform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform

> Application Version: 5.7

### Description

BreakTransform (v1)

Break a Transform into Translation, Rotation (Euler, Rotator, Quaternion), Scale

Input(s) :
Transform - Transform to break into components

Output(s):
Translation - Translation
Rotation - Rotation as Euler
Rotator - Rotation as a rotator
Quat - Rotation as a quaternion
Scale - Scale

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Transform |
| Type | [FBreakTransformDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBreakTransformDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | Transform to break into components | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Translation | Translation | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |
| Rotation | Rotation as Euler | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Rotator | Rotation as a rotator | [FRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Quat | Rotation as a quaternion | [FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Scale | Scale | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |
