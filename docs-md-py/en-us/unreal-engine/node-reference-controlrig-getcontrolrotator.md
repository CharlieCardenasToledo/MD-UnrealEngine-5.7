# Get Control Rotator

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlRotator

> Application Version: 5.7

### Description

GetControlRotator is used to retrieve a single Rotator from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlRotator |
| Type | [FRigUnit\_GetControlRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlRotator) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the Rotator for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the Control's Rotator should be retrieved in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Rotator | The current value of the control. | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
