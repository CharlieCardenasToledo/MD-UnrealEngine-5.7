# If

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/If

> Application Version: 5.7

### Description

Chooses between two values based on a condition

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | Branch,Condition |
| Type | [FRigVMDispatch\_If](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_If) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Condition | The condition on which we'll decide between the True and False values | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| True | The value to use if the condition is True | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| False | The value to use if the condition is False | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value - either True or False based on the condition | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
