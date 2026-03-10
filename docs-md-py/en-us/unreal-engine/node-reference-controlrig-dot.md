# Dot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Dot

> Application Version: 5.7

## Dot (FRigVMFunction\_MathQuaternionDot)

Returns the dot product between two quaternions

### Information

|  |  |  |
| --- | --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |  |
| Category | Math|Quaternion |  |
| Tags | Dot, |  |
| Type | [FRigVMFunction\_MathQuaternionDot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionDot) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first quaternion to compute the dot product for | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| B | The second quaternion to compute the dot product for | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting dot product between two quaternions | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

## Dot (FRigVMFunction\_MathVectorDot)

Returns the dot product between two vectors

### Information

|  |  |  |
| --- | --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |  |
| Category | Math|Vector |  |
| Tags | Dot, |  |
| Type | [FRigVMFunction\_MathVectorDot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorDot) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first vector compute the dot product for | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| B | The second vector compute the dot product for | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting dot product between A and B | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
