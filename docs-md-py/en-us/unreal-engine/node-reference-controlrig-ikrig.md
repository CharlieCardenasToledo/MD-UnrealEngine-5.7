# IK Rig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IKRig

> Application Version: 5.7

### Description

Supply an IK Rig asset and provide goal transforms to run IK on the skeleton.

### Information

|  |  |
| --- | --- |
| Plugin | [IKRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/IKRig) |
| Category | Hierarchy |
| Tags | IK Rig, IK |
| Type | [FRigUnit\_IKRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/IKRig/FRigUnit_IKRig) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IKRigAsset | An IK Rig asset to be evaluated. | IKRig Definition | None |
| Goals | A list of Goals to solve. These must match what is in the IK Rig, any missing Goals will have their alphas set to zero. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FIKRigGoalInput](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/IKRig/FIKRigGoalInput)> | () |
