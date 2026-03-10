# To Vectors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors

> Application Version: 5.7

## To Vectors (FRigVMFunction\_MathMatrixToVectors)

Converts the matrix to its vectors

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Matrix |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathMatrixToVectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathMatrixToVecto-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The matrix to split up to vectors | [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (XPlane=(W=0.000000,X=1.000000,Y=0.000000,Z=0.000000),YPlane=(W=0.000000,X=0.000000,Y=1.000000,Z=0.000000),ZPlane=(W=0.000000,X=0.000000,Y=0.000000,Z=1.000000),WPlane=(W=1.000000,X=0.000000,Y=0.000000,Z=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | The resulting origin | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| X | The resulting X component | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Y | The resulting Y component | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Z | The resulting Z component | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## To Vectors ()

Retrieves the forward, right and up vectors of a quaternion
Retrieves the forward, right and up vectors of a transform's quaternion

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | ToVectors,To Vectors,Forward,Right,Up |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Forward | The forward axis of the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Right | The right axis of the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Up | The up axis of the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
