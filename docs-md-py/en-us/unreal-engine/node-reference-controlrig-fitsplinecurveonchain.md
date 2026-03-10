# Fit Spline Curve on Chain

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FitSplineCurveonChain

> Application Version: 5.7

### Description

Fits a given spline curve to a chain.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Fit,Resample,Spline |
| Type | [FRigUnit\_FitSplineCurveToChainItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_FitSplineCurveToChainIt-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The curve to align | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to align to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
