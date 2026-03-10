# From Euler

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromEuler

> Application Version: 5.7

### Description

Makes a quaternion from euler values in degrees

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathQuaternionFromEuler](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionFro-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Euler | The euler representation of the rotation in degrees. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RotationOrder | The rotation order to use when interpreting the euler angles | [Euler Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | ZYX |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting composed quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
