# GetAnimationChannel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAnimationChannel

> Application Version: 5.7

### Description

Get Bool Channel is used to retrieve a control's animation channel value
Get Float Channel is used to retrieve a control's animation channel value
Get Int Channel is used to retrieve a control's animation channel value
Get Vector2D Channel is used to retrieve a control's animation channel value
Get Vector Channel is used to retrieve a control's animation channel value
Get Rotator Channel is used to retrieve a control's animation channel value
Get Transform Channel is used to retrieve a control's animation channel value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetAnimationChannel,Get Bool Channel,Animation,Channel,Get Float Channel,Get Int Channel,Get Vector2D Channel,Get Vector Channel,Get Rotator Channel,Get Transform Channel |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Channel | The name of the animation channel to retrieve the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bInitial | If set to true the initial value will be returned | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The current value of the animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
