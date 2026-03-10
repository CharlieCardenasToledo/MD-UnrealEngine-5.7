# Get Control Offset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlOffset

> Application Version: 5.7

### Description

GetControlOffset returns the offset transform of a given control.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlOffset,Initial,InitialTransform,GetInitialTransform,GetInitialControlTransform |
| Type | [FRigUnit\_GetControlOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlOffset) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the transform should be retrieved in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OffsetTransform | The current transform of the given item - or identity in case it wasn't found. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
