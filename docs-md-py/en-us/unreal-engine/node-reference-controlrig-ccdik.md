# CCDIK

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CCDIK

> Application Version: 5.7

### Description

The CCID solver can solve N-Bone chains using
the Cyclic Coordinate Descent Inverse Kinematics algorithm.
For now this node supports single effector chains only.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | N-Bone,IK |
| Type | [FRigUnit\_CCDIKItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CCDIKItemArray) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The chain to use | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| EffectorTransform | The transform of the effector in global space | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Precision | The precision to use for the fabrik solver | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Weight | The weight of the solver - how much the IK should be applied. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MaxIterations | The maximum number of iterations. Values between 4 and 16 are common. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| bStartFromTail | If set to true the direction of the solvers is flipped. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| BaseRotationLimit | The general rotation limit to be applied to bones | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 30.000000 |
| RotationLimits | Defines the limits of rotation per bone. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_CCDIK\_RotationLimitPerItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CCDIK_RotationLimitPerI-)> | () |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
