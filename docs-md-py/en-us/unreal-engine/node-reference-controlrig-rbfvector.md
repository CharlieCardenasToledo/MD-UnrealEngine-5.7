# RBF Vector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFVector

> Application Version: 5.7

### Description

A RBF interpolator from vector to float
A RBF interpolator from vector to vector
A RBF interpolator from vector to color
A RBF interpolator from vector to quaternion
A RBF interpolator from vector to transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|RBF Interpolation |
| Tags | RBF Vector,RBF Vector to Float,RBF,Interpolate,Vector,RBF Vector to Vector,RBF Vector to Color,RBF Vector to Quat,RBF Vector to Transform |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Targets | The array of targets to interpolate within | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorFloat\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorFloat_T-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorVector\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorVector_-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorColor\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorColor_T-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorQuat\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorQuat_Ta-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorXform\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorXform_T-)> | () |
| Input | The input vector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| DistanceFunction | The distance function to use | [RBFVector Distance Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFVectorDistanceType) | Euclidean |
| SmoothingFunction | The smoothing function to use | [RBFKernel Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFKernelType) | Gaussian |
| SmoothingRadius | The radius to apply for the smoothing function | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| bNormalizeOutput | If true the resulting output will be normalized | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output | The interpolated result | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |
