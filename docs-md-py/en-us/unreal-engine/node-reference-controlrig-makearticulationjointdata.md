# Make Articulation Joint Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationJointData

> Application Version: 5.7

### Description

Helper to simplify creation of joint data for a typical articulation (i.e. locked linear motion,
but with an angular limit)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_MakeArticulationJointData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_MakeArticulationJointDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AngularLimit | The angular limit in Degrees (twist, swing1, swing2) -ve indicates the limit range is free | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=-1.000000,Y=-1.000000,Z=-1.000000) |
| SoftStrength | If limited, then this will be used to control the softness of the limit -ve indicates the limit is hard A value of 1 is reasonably soft | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=-1.000000,Y=-1.000000,Z=-1.000000) |
| SoftDampingRatio | If limited, then this will be used to control the damping ratio of the limit | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| JointData | Joint data that can be used in a Physics Joint, calculated according to the values set here, and configured to act as a "normal" articulation joint. | [Rig Physics Joint Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) |  |
