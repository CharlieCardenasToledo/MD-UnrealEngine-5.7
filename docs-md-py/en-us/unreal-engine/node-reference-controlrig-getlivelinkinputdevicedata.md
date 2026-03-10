# Get Live Link Input Device Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetLiveLinkInputDeviceData

> Application Version: 5.7

### Description

A node to evaluate a live link input device value

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkEvaluateInputDeviceValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkEvaluateInputDe-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectName | Name of the subject we would like to get Live Link device data. This should be the subject attached to the gamepad. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InputDeviceData | Gamepad device data for the current frame. | [Live Link Gamepad Input Device Frame Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/LiveLinkInterface/FLiveLinkGamepadInputDeviceFrame-) |  |
