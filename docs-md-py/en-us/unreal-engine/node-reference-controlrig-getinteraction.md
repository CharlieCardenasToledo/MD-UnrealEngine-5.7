# Get Interaction

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetInteraction

> Application Version: 5.7

### Description

Returns true if the Control Rig is being interacted

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Execution |
| Tags | IsInteracting,Gizmo,Manipulation,Interaction,Tracking |
| Type | [FRigUnit\_IsInteracting](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_IsInteracting) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bIsInteracting | True if there is currently an interaction happening | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsTranslating | True if the current interaction is a translation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsRotating | True if the current interaction is a rotation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsScaling | True if the current interaction is scaling | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Items | The items being interacted on | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |
