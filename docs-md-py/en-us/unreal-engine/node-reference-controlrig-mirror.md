# Mirror

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Mirror

> Application Version: 5.7

### Description

Mirror a rotation about a central transform.
Mirror a transform about a central transform.
Mirror a vector about a central transform.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Mirror |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| MirrorAxis | the axis to mirror against | [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | X |
| AxisToFlip | the axis to flip for rotations | [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | Z |
| CentralTransform | The transform about which to mirror | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting mirrored rotation | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
