# Curve Exists

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CurveExists

> Application Version: 5.7

### Description

CurveExists is used to check whether a curve exists or not.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Curve |
| Tags | CurveExists,bool |
| Type | [FRigUnit\_CurveExists](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CurveExists) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Curve | The name of the Curve to retrieve the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Exists | Boolean indicating whether the named curve exists or not. Does not indicate whether the curve's value is valid or not. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
