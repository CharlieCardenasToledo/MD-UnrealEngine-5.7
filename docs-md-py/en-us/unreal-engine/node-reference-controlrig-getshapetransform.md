# Get Shape Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetShapeTransform

> Application Version: 5.7

### Description

GetShapeTransform is used to retrieve single control's shape transform.
This is typically only used during the Construction Event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlShapeTransform,Gizmo,GizmoTransform,MeshTransform |
| Type | [FRigUnit\_GetShapeTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetShapeTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The shape transform to set for the control | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
