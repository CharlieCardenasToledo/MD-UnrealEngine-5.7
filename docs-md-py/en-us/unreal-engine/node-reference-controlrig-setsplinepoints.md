# Set Spline Points

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetSplinePoints

> Application Version: 5.7

### Description

Set the points of a spline, given a spline and an array of positions

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_SetSplinePoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_SetSplinePoints) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to be updated | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | The points to set on the spline. The assumption is that the number of points provided matches the points on the spline. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
