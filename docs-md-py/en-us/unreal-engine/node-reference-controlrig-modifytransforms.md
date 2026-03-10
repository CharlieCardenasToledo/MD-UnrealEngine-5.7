# Modify Transforms

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ModifyTransforms

> Application Version: 5.7

### Description

Modify Transforms is used to perform a change in the hierarchy by setting one or more bones' transforms

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | ModifyBone |
| Type | [FRigUnit\_ModifyTransforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ModifyTransforms) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ItemToModify | The items to modify. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_ModifyTransforms\_PerItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ModifyTransforms_PerIte-)> | (()) |
| Weight | At 1 this sets the transform, between 0 and 1 the transform is blended with previous results. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| WeightMinimum | The minimum of the weight - defaults to 0.0 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WeightMaximum | The maximum of the weight - defaults to 1.0 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Mode | Defines if the bone's transform should be set in local or global space, additive or override. | [Control Rig Modify Bone Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigModifyBoneMode) | AdditiveLocal |
