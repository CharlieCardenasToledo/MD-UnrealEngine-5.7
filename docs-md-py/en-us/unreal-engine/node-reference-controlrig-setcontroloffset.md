# SetControlOffset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlOffset

> Application Version: 5.7

### Description

SetControlOffset is used to perform a change in the hierarchy by setting a single control's transform.
This is typically only used during the Construction Event.
SetControlTranslationOffset is used to perform a change in the hierarchy by setting a single control's translation offset.
This is typically only used during the Construction Event.
SetControlRotationOffset is used to perform a change in the hierarchy by setting a single control's rotation offset.
This is typically only used during the Construction Event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlOffset,Set Control Offset,Initial,InitialTransform,SetInitialTransform,SetInitialControlTransform,Set Control Translation Offset,SetControlTranslationOffset,SetInitialTranslation,SetInitialLocation,Set Control Rotation Offset,SetControlRotationOffset,SetInitialRotation |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Offset | The offset transform to set on the control | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the control's transform should be set in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
