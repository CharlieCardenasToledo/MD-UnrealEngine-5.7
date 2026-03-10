# To World

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToWorld

> Application Version: 5.7

### Description

Converts a transform from rig (global) space to world space
Converts a position / location from rig (global) space to world space
Converts a rotation from rig (global) space to world space

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | To World,Global,Local,World,Actor,ComponentSpace,FromRig |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input transform in global / rig space | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| World | The result transform in world space | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
