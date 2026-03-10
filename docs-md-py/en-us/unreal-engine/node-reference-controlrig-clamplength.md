# ClampLength

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampLength

> Application Version: 5.7

### Description

Clamps the length of a given vector between a minimum and maximum

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Unit,Normalize,Scale |
| Type | [FRigVMFunction\_MathVectorClampLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorClampLe-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input vector to clamp the length of | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| MinimumLength | The minimum length to clamp by | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaximumLength | The maximum length to clamp by | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting clamped input vector \* (or 0,0,0 in case the input was also 0,0,0) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
