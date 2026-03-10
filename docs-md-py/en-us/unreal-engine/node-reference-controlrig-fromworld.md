# From World

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromWorld

> Application Version: 5.7

### Description

Converts a transform from world space to rig (global) space
Converts a position / location from world space to rig (global) space
Converts a rotation from world space to rig (global) space

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | From World,Global,Local,World,Actor,ComponentSpace,ToRig |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input transform in world | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Global | The result transform in global / rig space | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
