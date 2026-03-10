# Set Animation Attribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute

> Application Version: 5.7

### Description

Modify an animation attribute if one is found, otherwise add a new animation attribute

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Animation Attribute |
| Type | [FRigDispatch\_SetAnimAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_SetAnimAttribute) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the animation attribute | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| BoneName | The name of the bone that stores the attribute, default to root bone if set to none | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Value | The value to get / set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore),[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString),[FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),User Defined Structs,[FPoseHistoryAnimationAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PoseSearch/FPoseHistoryAnimationAttribute) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Success | Returns true if the animation attribute was successfully stored | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
