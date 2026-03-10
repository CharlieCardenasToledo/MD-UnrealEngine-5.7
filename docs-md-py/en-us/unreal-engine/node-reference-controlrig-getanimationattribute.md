# Get Animation Attribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAnimationAttribute

> Application Version: 5.7

### Description

Get the value of an animation attribute from the skeletal mesh

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Animation Attribute |
| Type | [FRigDispatch\_GetAnimAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_GetAnimAttribute) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the animation attribute | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| BoneName | The name of the bone that stores the attribute, default to root bone if set to none | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Default | The default value used as a fallback if the animation attribute does not exist | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore),[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString),[FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),User Defined Structs,[FPoseHistoryAnimationAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PoseSearch/FPoseHistoryAnimationAttribute) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to get / set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore),[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString),[FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),User Defined Structs,[FPoseHistoryAnimationAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PoseSearch/FPoseHistoryAnimationAttribute) |  |
| Found | Returns true if the animation attribute exists with the specific type | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
