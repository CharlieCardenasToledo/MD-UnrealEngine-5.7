# Time Loop

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeLoop

> Application Version: 5.7

### Description

Simulates a time value - and outputs loop information

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | Playback,Pause,Timeline |
| Type | [FRigVMFunction\_TimeLoop](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_TimeLoop) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Speed | The speed to play-back the time at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Duration | the duration of a single loop in seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Normalize | if set to true the output relative and flipflop will be normalized over the duration. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Absolute | the overall time in seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Relative | the relative time in seconds (within the loop) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| FlipFlop | the relative time in seconds (within the loop), going from 0 to duration and then back from duration to 0, or 0 to 1 and 1 to 0 if Normalize is turned on | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Even | true if the iteration of the loop is even | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
