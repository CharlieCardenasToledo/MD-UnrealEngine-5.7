# From Vectors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromVectors

> Application Version: 5.7

### Description

Makes a matrix from its vectors

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Matrix |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathMatrixFromVectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathMatrixFromVec-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | The input origin for the matrix | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| X | The input X component for the matrix | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| Y | The input Y component for the matrix | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=0.000000) |
| Z | The input Z component for the matrix | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting matrix | [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
