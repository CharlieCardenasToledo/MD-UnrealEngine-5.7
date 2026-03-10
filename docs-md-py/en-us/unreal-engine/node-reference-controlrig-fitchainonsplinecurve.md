# Fit Chain on Spline Curve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FitChainonSplineCurve

> Application Version: 5.7

### Description

Fits a given chain to a spline curve.
Additionally provides rotational control matching the features of the Distribute Rotation node.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Fit,Resample,Spline |
| Type | [FRigUnit\_FitChainToSplineCurveItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_FitChainToSplineCurveIt-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to align | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Spline | The curve to align to | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| Alignment | Specifies how to align the chain on the curve | [Control Rig Curve Alignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigCurveAlignment) | Stretched |
| Minimum | The minimum U value to use on the curve | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | The maximum U value to use on the curve | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SamplingPrecision | The number of samples to use on the curve. Clamped at 64. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |
| PrimaryAxis | The major axis being aligned - along the bone | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The minor axis being aligned - towards the pole vector. You can use (0.0, 0.0, 0.0) to disable it. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PoleVectorPosition | The position of the pole vector used for aligning the secondary axis. Only has an effect if the secondary axis is set. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Rotations | The list of rotations to be applied along the curve | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_FitChainToCurve\_Rotation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FitChainToCurve_Rotatio-)> | () |
| RotationEaseType | The easing to use between to rotations. | [Rig VMAnim Easing Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | Linear |
| Weight | The weight of the solver - how much the rotation should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugSettings | The debug settings to use | [Rig Unit Fit Chain to Curve Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FitChainToCurve_DebugSe-) | (bEnabled=False,Scale=1.000000,CurveColor=(R=1.000000,G=1.000000,B=0.000000,A=1.000000),SegmentsColor=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |
