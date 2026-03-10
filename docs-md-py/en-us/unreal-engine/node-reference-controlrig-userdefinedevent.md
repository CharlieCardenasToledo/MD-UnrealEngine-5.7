# User Defined Event

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UserDefinedEvent

> Application Version: 5.7

### Description

User Defined Event for running custom logic

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Events |
| Tags | Event,Entry,MyEvent |
| Type | [FRigVMFunction\_UserDefinedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_UserDefinedEvent) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| EventName | The name of the event. Given this name the event can be invoked using the run event node. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | My Event |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
