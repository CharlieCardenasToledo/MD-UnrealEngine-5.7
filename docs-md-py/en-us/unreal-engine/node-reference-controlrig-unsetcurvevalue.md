# Unset Curve Value

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UnsetCurveValue

> Application Version: 5.7

### Description

UnsetCurveValue is used to perform a change in the curve container by invalidating a single Curve value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Curve |
| Tags | UnsetCurveValue |
| Type | [FRigUnit\_UnsetCurveValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_UnsetCurveValue) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Curve | The name of the Curve to set the Value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
