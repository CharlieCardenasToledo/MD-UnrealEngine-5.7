# To Euler

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToEuler

> Application Version: 5.7

### Description

Retrieves the euler angles in degrees

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathQuaternionToEuler](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionToE-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| RotationOrder | The rotation order to use when encoding the euler angles | [Euler Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | ZYX |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The euler angles in degrees representing the quaternion in the given rotation order | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
