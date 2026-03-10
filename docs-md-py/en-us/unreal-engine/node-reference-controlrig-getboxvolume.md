# Get Box Volume

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBoxVolume

> Application Version: 5.7

### Description

Returns the volume of a given box

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,BoundingBox |
| Type | [FRigVMFunction\_MathBoxGetVolume](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxGetVolume) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to retrieve the volume for | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Volume | The volume of the box | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
