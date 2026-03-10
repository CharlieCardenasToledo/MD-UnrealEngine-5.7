# SpringInterp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterp

> Application Version: 5.7

### Description

Uses a simple spring model to interpolate a float from Current to Target.
Uses a simple spring model to interpolate a vector from Current to Target.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Simulation|Springs |
| Tags | SpringInterp,Spring Interpolate,Alpha,SpringInterpolate,Verlet |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | Rest/target position of the spring. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Strength | The spring strength determines how hard it will pull towards the target. The value is the frequency at which it will oscillate when there is no damping. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 4.000000 |
| CriticalDamping | The amount of damping in the spring. Set it smaller than 1 to make the spring oscillate before stabilizing on the target. Set it equal to 1 to reach the target without overshooting. Set it higher than one to make the spring take longer to reach the target. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Force | Extra force to apply (since the mass is 1, this is also the acceleration). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| bUseCurrentInput | If true, then the Current input will be used to initialize the state, and is required to be a variable that holds the current state. If false then the Target value will be used to initialize the state and the Current input will be ignored/unnecessary as a state will be maintained by this node. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Current | Current position of the spring. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| TargetVelocityAmount | The amount that the velocity should be passed through to the spring. A value of 1 will result in more responsive output, but if the input is noisy or has step changes, these discontinuities will be passed through to the output much more than if a smaller value such as 0 is used. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bInitializeFromTarget | If true, then the initial value will be taken from the target value, and not from the current value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | New position of the spring after delta time. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Velocity | The resulting velocity of this spring | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
