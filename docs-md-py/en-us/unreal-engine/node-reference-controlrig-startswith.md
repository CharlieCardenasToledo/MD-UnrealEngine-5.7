# StartsWith

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StartsWith

> Application Version: 5.7

### Description

Tests whether this name starts with given name
Tests whether this string starts with given string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | StartsWith,Starts With,Left |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to search within | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| Start | The start name to look for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the given input name starts with the given start string | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
