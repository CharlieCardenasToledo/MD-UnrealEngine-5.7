# GetAt

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAt

> Application Version: 5.7

### Description

Returns the position on a ray

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Ray |
| Tags | Ratio,Percentage |
| Type | [FRigVMFunction\_MathRayGetAt](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathRayGetAt) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Ray | The ray to query | [Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |
| Ratio | The ratio to query the ray at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting position on the ray | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
