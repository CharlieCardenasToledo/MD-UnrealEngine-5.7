# Pad Integer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PadInteger

> Application Version: 5.7

### Description

Converts an integer number to a string with padding

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | FromInt,Number,LeadingZeroes |
| Type | [FRigVMFunction\_StringPadInteger](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringPadInteger) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input number to convert to a string (for example 4) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Digits | The number of digits in total to use (for example 3) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting string representing the padded integer (for example '004') | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
