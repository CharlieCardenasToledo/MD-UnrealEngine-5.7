# Join

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Join

> Application Version: 5.7

### Description

Joins a string into multiple sections given a separator

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | Combine |
| Type | [FRigVMFunction\_StringJoin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringJoin) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Values | An array of input strings to join | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> | () |
| Separator | The separator to use when joining the parts | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting joined string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
