# RBF Quaternion

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFQuaternion

> Application Version: 5.7

### Description

A RBF interpolator from quaternion to float
A RBF interpolator from quaternion to vector
A RBF interpolator from quaternion to color
A RBF interpolator from quaternion to quaternion
A RBF interpolator from quaternion to transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|RBF Interpolation |
| Tags | RBF Quaternion,RBF Quaternion to Float,RBF,Interpolate,Quaternion,RBF Quaternion to Vector,RBF Quaternion to Color,RBF Quaternion to Quaternion,RBF Quaternion to Transform |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Targets | The array of targets to interpolate within | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatFloat\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatFloat_Tar-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatVector\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatVector_Ta-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatColor\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatColor_Tar-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatQuat\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatQuat_Targ-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatXform\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatXform_Tar-)> | () |
| Input | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| DistanceFunction | The distance function to use | [RBFQuat Distance Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFQuatDistanceType) | ArcLength |
| SmoothingFunction | The smoothing function to use | [RBFKernel Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFKernelType) | Gaussian |
| SmoothingAngle | The smoothing angle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 45.000000 |
| bNormalizeOutput | If true the resulting output will be normalized | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| TwistAxis | The twist axis of the input quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output | The interpolated result | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |
