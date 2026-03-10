# Basic IK Positions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions

> Application Version: 5.7

### Description

Solves the two bone IK given positions
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | TwoBone,IK |
| Type | [FRigUnit\_TwoBoneIKSimpleVectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_TwoBoneIKSimpleVectors) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Effector | The position of the effector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Root | The position of the root of the triangle | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PoleVector | The position of the pole of the triangle | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bEnableStretch | If set to true the stretch feature of the solver will be enabled | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| StretchStartRatio | The ratio where the stretch starts | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| StretchMaximumRatio | The maximum allowed stretch ratio | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.250000 |
| BoneALength | The length of the first bone. If set to 0.0 it will be determined by the hierarchy | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| BoneBLength | The length of the second bone. If set to 0.0 it will be determined by the hierarchy | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Elbow | The resulting elbow position | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
