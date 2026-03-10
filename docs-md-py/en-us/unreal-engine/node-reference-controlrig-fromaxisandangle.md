# From Axis And Angle

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromAxisAndAngle

> Application Version: 5.7

### Description

Makes a quaternion from an axis and an angle in radians

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathQuaternionFromAxisAndAngle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionFro-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Axis | The axis to use for the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| Angle | The angle in radians to use for the quaternion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting composed quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
