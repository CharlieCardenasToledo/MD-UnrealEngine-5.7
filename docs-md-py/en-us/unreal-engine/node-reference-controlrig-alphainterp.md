# AlphaInterp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AlphaInterp

> Application Version: 5.7

### Description

Takes in a float value and outputs an accumulated value with a customized scale and clamp
Takes in a vector value and outputs an accumulated value with a customized scale and clamp
Takes in a quaternion value and outputs an accumulated value with a customized scale and clamp

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Time |
| Tags | AlphaInterp,Alpha Interpolate,Alpha,Lerp,LinearInterpolate |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to interpolate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Scale | The scale to apply to the interpolation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Bias | The bias to use for the interpolation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bMapRange | If True the input value will be mapped using the min and max range | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| InRange | The minimum and maximum for the input range | [Input Range](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FInputRange) | (Min=0.000000,Max=1.000000) |
| OutRange | The minimum and maximum for the output range | [Input Range](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FInputRange) | (Min=0.000000,Max=1.000000) |
| bClampResult | If True the output value will be clamped by the min and max | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ClampMin | The minimum for the output's clamp range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ClampMax | The maximum for the output's clamp range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bInterpResult | If True to the output result will be further intepolated | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| InterpSpeedIncreasing | The output interpolation increasing speed | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| InterpSpeedDecreasing | The output interpolation decreasing speed | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting interpolated value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
