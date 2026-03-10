# To Integer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToInteger

> Application Version: 5.7

### Description

Converts a string to an integer

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | ToInt,Number |
| Type | [FRigVMFunction\_StringToInteger](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringToInteger) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to convert to integer | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| ChopLeft | chops non-digit characters from the left of the string | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ChopRight | chops non-digit characters from the right of the string | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting integer number (or INDEX\_NONE) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Success | True if the string was successfully converted to integer | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
