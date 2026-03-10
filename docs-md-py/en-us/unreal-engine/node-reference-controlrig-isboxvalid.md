# Is Box Valid

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsBoxValid

> Application Version: 5.7

### Description

Returns true if the box has any content / is valid

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | IsValid,HasVolume,ContainsPoints,Bounds,BoundingBox,Bbox |
| Type | [FRigVMFunction\_MathBoxIsValid](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxIsValid) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to check | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | Returns true if the box has any content / is valid | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
