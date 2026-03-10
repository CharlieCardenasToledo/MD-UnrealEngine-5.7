# Position From Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PositionFromSpline

> Application Version: 5.7

### Description

Retrieves the position from a given Spline and U value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Point From Spline |
| Type | [FRigUnit\_PositionFromControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_PositionFromControlRigS-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| U | The U value along the spline to evaluate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Position | The resulting position on the spline | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
