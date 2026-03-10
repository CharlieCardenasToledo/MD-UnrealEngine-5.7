# Verlet (Vector)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VerletVector

> Application Version: 5.7

### Description

Simulates a single position over time using Verlet integration. It is recommended to use SpringInterp instead as it
is more accurate and stable, and has more meaningful parameters.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Springs |
| Tags | Simulate,Integrate |
| Type | [FRigVMFunction\_VerletIntegrateVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VerletIntegrateVe-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | The target value to interpolate / integrate towards | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Strength | The strength of the verlet spring | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 64.000000 |
| Damp | The amount of damping to apply ( 0.0 to 1.0, but usually really low like 0.005 ) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| Blend | The amount of blending to apply per second | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| Force | The force feeding into the solver. Can be used for gravity. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Position | The resulting simulated position | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Velocity | The resulting simulated velocity | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Acceleration | The resulting simulated acceleration | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
