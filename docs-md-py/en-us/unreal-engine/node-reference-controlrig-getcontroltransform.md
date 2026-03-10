# Get Control Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlTransform

> Application Version: 5.7

### Description

GetControlTransform is used to retrieve a single transform from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlTransform |
| Type | [FRigUnit\_GetControlTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the Control's transform should be retrieved in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The current value of the control. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
