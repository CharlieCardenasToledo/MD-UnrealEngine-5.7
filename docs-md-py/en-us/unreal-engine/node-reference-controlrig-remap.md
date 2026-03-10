# Remap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Remap

> Application Version: 5.7

### Description

Remaps the given value from a source range to a target range.
Remaps the given value from a source range to a target range for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Remap,Rescale,Scale |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to remap | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SourceMinimum | The minimum of the range of the input / source value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SourceMaximum | The maximum of the range of the input / source value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| TargetMinimum | The minimum of the range of the output / target value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| TargetMaximum | The maximum of the range of the output / target value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| bClamp | If set to true the result is clamped to the target range | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting remapped value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
