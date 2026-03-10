# Set Control Rotator

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlRotator

> Application Version: 5.7

### Description

SetControlRotator is used to perform a change in the hierarchy by setting a single control's Rotator value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlRotator,SetGizmoRotator |
| Type | [FRigUnit\_SetControlRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlRotator) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Rotator | The vector value to get / set for the given Control. | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Pitch=0.000000,Yaw=0.000000,Roll=0.000000) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Space | Defines if the bone's transform should be set in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
