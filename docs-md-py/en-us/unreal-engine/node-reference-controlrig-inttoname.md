# Int to Name

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/InttoName

> Application Version: 5.7

### Description

Converts an integer to a string
Converts an integer to a name

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Int |
| Tags | Int to Name,Int to String |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Number | The number to convert | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| PaddedSize | For positive numbers you can pad the result to a required width \* so rather than '13' return '00013' for a padded size of 5. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting potentially padded string | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
