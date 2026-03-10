# Branch

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Branch

> Application Version: 5.7

### Description

Executes either the True or False branch based on the condition

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | If |
| Type | [FRigVMFunction\_ControlFlowBranch](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_ControlFlowBranch) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | The input execution pin to hook up to the graph | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Condition | The condition based on which to pick between the True and False branches | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| True | The branch to run if the condition is True | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| False | The branch to run if the condition is False | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Completed | The execute flow to run when the True or False branch is complete | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
