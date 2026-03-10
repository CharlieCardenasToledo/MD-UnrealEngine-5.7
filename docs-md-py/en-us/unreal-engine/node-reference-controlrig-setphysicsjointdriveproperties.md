# Set Physics Joint Drive Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointDriveProperties

> Application Version: 5.7

### Description

Sets the joint drive for a physics component body

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetJointDriveData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetJointDriveD-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsJoint") |
| DriveData | The Physics Joint drive data that should be used | [Rig Physics Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) | (LinearDriveConstraint=(PositionTarget=(X=0.000000,Y=0.000000,Z=0.000000),VelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),XDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),YDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),ZDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),bAccelerationMode=True),AngularDriveConstraint=(TwistDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SwingDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SlerpDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),OrientationTarget=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000),AngularVelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),AngularDriveMode=SLERP,bAccelerationMode=True),bUseSkeletalAnimation=True,SkeletalAnimationVelocityMultiplier=1.000000) |
