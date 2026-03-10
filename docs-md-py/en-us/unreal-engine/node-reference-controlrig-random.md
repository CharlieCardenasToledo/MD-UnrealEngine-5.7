# Random

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Random

> Application Version: 5.7

### Description

Generates a random float between a min and a max
Generates a random vector between a min and a max

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Random |
| Tags | Random,Random (Float),Random (Vector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Seed | The seed for the random number generator | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 217 |
| Minimum | The minimum value for the random number range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | The maximum value for the random number range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Duration | The duration at which the number won't change. Use 0 for a different number every time. A negative number (for ex: -1) results in an infinite duration. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting random number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
