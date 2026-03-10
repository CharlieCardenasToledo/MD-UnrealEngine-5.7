# Send Event

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SendEvent

> Application Version: 5.7

### Description

SendEvent is used to notify the engine / editor of a change that happend within the Control Rig.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Event,Notify,Notification |
| Type | [FRigUnit\_SendEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SendEvent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Event | The event to send to the engine | [Rig Event](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigEvent) | RequestAutoKey |
| Item | The item to send the event for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| OffsetInSeconds | The time offset to use for the send event | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bEnable | The event will be sent if this is checked | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bOnlyDuringInteraction | The event will be sent if this only during an interaction | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
