# Set Curve Value

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetCurveValue

> Application Version: 5.7

### Description

SetCurveValue is used to perform a change in the curve container by setting a single Curve value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Curve |
| Tags | SetCurveValue |
| Type | [FRigUnit\_SetCurveValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetCurveValue) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Curve | The name of the Curve to set the Value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Value | The value to set for the given Curve. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
