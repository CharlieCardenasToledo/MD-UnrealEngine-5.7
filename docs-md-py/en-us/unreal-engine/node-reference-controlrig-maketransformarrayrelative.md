# Make Transform Array Relative

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeTransformArrayRelative

> Application Version: 5.7

### Description

Treats the provided transforms as a chain with global / local transforms, and
projects each transform into the target space. Optionally you can provide
a custom parent indices array, with which you can represent more than just chains.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | Local,Global,Absolute,Array,Accumulate |
| Type | [FRigVMFunction\_MathTransformAccumulateArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformAccu-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | The input transform array to accumulate | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetSpace | Defines the space to project to | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| Root | Provides the parent transform for the root | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| ParentIndices | If this array is the same size as the transforms array the indices will be used to look up each transform's parent. They are expected to be in order. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
