# Spawn Physics Solver

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsSolver

> Application Version: 5.7

### Description

Adds a new physics solver as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Simulation |
| Type | [FRigUnit\_AddPhysicsSolver](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsSolver) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| SolverSettings | Settings for the physics solver that will be added | [Rig Physics Solver Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSolverSettings) | (bAutomaticallyAddPhysicsComponents=True,SimulationSpace=Component,CollisionSpace=Component,SpaceBone=(Type=None,Name=""),Collision=(Boxes=,Spheres=,Capsules=,Material=(Friction=1.000000,Restitution=1.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply)),Gravity=(X=0.000000,Y=0.000000,Z=-981.000000),WorldCollisionType=None,WorldCollisionExpiryFrames=3,WorldCollisionBoundsExpansion=1.100000,PositionIterations=8,VelocityIterations=4,ProjectionIterations=1,MaxNumRollingAverageStepTimes=1,CollisionBoundsExpansion=2.000000,BoundsVelocityMultiplier=1.000000,MaxVelocityBoundsExpansion=25.000000,MaxDepenetrationVelocity=0.000000,FixedTimeStep=0.020000,MaxTimeSteps=10,MaxDeltaTime=0.020000,bUseLinearJointSolver=True,bSolveJointPositionsLast=True,bUseManifolds=True,PositionThresholdForReset=0.000000,KinematicSpeedThresholdForReset=5000.000000,KinematicAccelerationThresholdForReset=0.000000) |
| SimulationSpaceSettings | Settings for the solver that apply to when it uses a simulation space other than "world". These typically relate to the movement of the simulation space itself, and how that is used by the solver. | [Rig Physics Simulation Space Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSimulationSpaceSettin-) | (SpaceMovementAmount=1.000000,VelocityScaleZ=1.000000,bClampLinearVelocity=False,MaxLinearVelocity=10000.000000,bClampAngularVelocity=False,MaxAngularVelocity=10000.000000,bClampLinearAcceleration=False,MaxLinearAcceleration=10000.000000,bClampAngularAcceleration=False,MaxAngularAcceleration=10000.000000,LinearAccelerationThresholdForTeleport=100000.000000,AngularAccelerationThresholdForTeleport=100000.000000,PositionChangeThresholdForTeleport=100.000000,OrientationChangeThresholdForTeleport=30.000000,LinearDragMultiplier=1.000000,AngularDragMultiplier=1.000000,ExternalLinearDrag=(X=0.000000,Y=0.000000,Z=0.000000),ExternalLinearVelocity=(X=0.000000,Y=0.000000,Z=0.000000),ExternalAngularVelocity=(X=0.000000,Y=0.000000,Z=0.000000),ExternalTurbulenceVelocity=(X=0.000000,Y=0.000000,Z=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The component key of the solver that has been added | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |
