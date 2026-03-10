# EndsWith

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EndsWith

> Application Version: 5.7

### Description

Tests whether this name ends with given name
Tests whether this string ends with given string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | EndsWith,Ends With,Right |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to search within | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| Ending | The ending name to look for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the given input name ends with the given ending | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
