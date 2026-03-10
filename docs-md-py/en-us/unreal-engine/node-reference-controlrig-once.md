# Once

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Once

> Application Version: 5.7

### Description

Returns true once the first time this node is hit

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Tags | FlipFlop,Toggle,Changed,Different |
| Type | [FRigVMFunction\_MathBoolOnce](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolOnce) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Duration | The duration in seconds at which the result is true Use 0 for a different result every time. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value - true once the first time this node is hit | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
