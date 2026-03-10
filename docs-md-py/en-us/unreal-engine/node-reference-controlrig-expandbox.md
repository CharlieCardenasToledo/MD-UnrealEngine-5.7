# Expand Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ExpandBox

> Application Version: 5.7

### Description

Expands the size of the box by a given amount

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,Scale,Grow,Shrink,BoundingBox |
| Type | [FRigVMFunction\_MathBoxExpand](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxExpand) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | the box to expand | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Amount | the amount to grow / shrink the box by | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | the resulting expanded box | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
