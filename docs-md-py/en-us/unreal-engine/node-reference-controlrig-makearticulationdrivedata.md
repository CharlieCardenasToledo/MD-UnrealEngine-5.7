# Make Articulation Drive Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationDriveData

> Application Version: 5.7

### Description

Helper to simplify creation of drive data for a typical articulation (i.e. no linear drive, but
with an angular drive)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_MakeArticulationDriveData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_MakeArticulationDriveDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bEnableAngularDrive | Whether to enable the angular drive | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AngularDriveMode | The type of drive. Note that SLERP drives don't work if any axis is locked | [Angular Drive Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/EAngularDriveMode__Type) | SLERP |
| AngularStrength | The strength used to drive angular motion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| AngularDampingRatio | The amount of damping associated with the angular strength. A value of 1 Results in critically damped motion where the control drives as quickly as possible to the target without overshooting. Values > 1 result in more damped motion, and values below 1 result in faster, but more "wobbly" motion. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| AngularExtraDamping | The amount of additional angular damping. This is added to the damping that comes from AngularDampingRatio and can be useful when you want damping even when AngularStrength is zero. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SkeletalAnimationVelocityMultiplier | The amount of skeletal animation velocity to use in the targets | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DriveData | The drive data that can be set in a Physics Joint, reflecting the setup specified here. | [Rig Physics Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) |  |
