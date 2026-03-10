# Get Control Vector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlVector

> Application Version: 5.7

### Description

GetControlVector is used to retrieve a single Vector from a hierarchy, can be used for Controls of type "Position" or "Scale".

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlVector, GetControlPosition, GetControlScale |
| Type | [FRigUnit\_GetControlVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlVector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the Vector for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the Control's Vector should be retrieved in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector | The current value of the control. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
