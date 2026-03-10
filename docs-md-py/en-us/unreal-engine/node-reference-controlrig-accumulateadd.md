# AccumulateAdd

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateAdd

> Application Version: 5.7

### Description

Adds a value over time over and over again
Adds a vector over time over and over again

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateAdd,Accumulate Add (Float),Simulate,++,Accumulate Add (Vector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Increment | The increment to add for every iteration | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| InitialValue | The initial value to start at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| bIntegrateDeltaTime | If True the integration will be relying on the delta time to create more deterministic results with varying framerates. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting accumulated value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
