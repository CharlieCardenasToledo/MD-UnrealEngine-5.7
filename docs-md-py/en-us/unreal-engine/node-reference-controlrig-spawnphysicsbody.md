# Spawn Physics Body

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody

> Application Version: 5.7

### Description

Adds a new physics body as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_AddPhysicsBody](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsBody) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Solver | The solver to relate this new physics body should be added to | [Rig Physics Body Solver Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsBodySolverSettings) | (PhysicsSolverComponentKey=(ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver"),bUseAutomaticSolver=True,SourceBone=(Type=None,Name=""),TargetBone=(Type=None,Name=""),bIncludeInChecksForReset=True) |
| Dynamics | The dynamics properties of the new physics element | [Rig Physics Dynamics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDynamics) | (Density=1.000000,MassOverride=1.000000,bOverrideCentreOfMass=False,CentreOfMassOverride=(X=0.000000,Y=0.000000,Z=0.000000),CentreOfMassNudge=(X=0.000000,Y=0.000000,Z=0.000000),bOverrideMomentsOfInertia=False,MomentsOfInertiaOverride=(X=1.000000,Y=1.000000,Z=1.000000),LinearDamping=0.000000,AngularDamping=0.000000) |
| Collision | The collision properties of the new physics element | [Rig Physics Collision](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsCollision) | (Boxes=,Spheres=,Capsules=,Material=(Friction=1.000000,Restitution=0.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply)) |
| BodyData | The runtime modifiable data | [Physics Control Modifier Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlModifierData) | (MovementType=Simulated,CollisionType=QueryAndPhysics,KinematicTargetSpace=OffsetInBoneSpace,GravityMultiplier=1.000000,PhysicsBlendWeight=1.000000,bUpdateKinematicFromSimulation=True) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body component key that was created | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |
