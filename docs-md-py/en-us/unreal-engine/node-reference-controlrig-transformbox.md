# Transform Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformBox

> Application Version: 5.7

### Description

Transforms the box by a given transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,BoundingBox |
| Type | [FRigVMFunction\_MathBoxTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | the box to transform | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Transform | the transform to apply to the box | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | the resulting transformed box | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
