# Axis

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Axis

> Application Version: 5.7

### Description

Extracts an axis from a quaternion rotation

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | GetAxis,xAxis,yAxis,zAxis |
| Type | [FRigVMFunction\_MathQuaternionGetAxis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionGet-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Quaternion | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| Axis | The axis to extract | [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | X |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting extracted axis | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
