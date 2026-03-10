# Set Physics Solver Simulation Space Settings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsSolverSimulationSpaceSettings

> Application Version: 5.7

### Description

Sets the solver's simulation space settings

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_SetPhysicsSolverSimulationSpaceSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_SetPhysicsSolverSimulat-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The physics solver | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| SimulationSpaceSettings | The new simulation space settings | [Rig Physics Simulation Space Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSimulationSpaceSettin-) | (SpaceMovementAmount=1.000000,VelocityScaleZ=1.000000,bClampLinearVelocity=False,MaxLinearVelocity=10000.000000,bClampAngularVelocity=False,MaxAngularVelocity=10000.000000,bClampLinearAcceleration=False,MaxLinearAcceleration=10000.000000,bClampAngularAcceleration=False,MaxAngularAcceleration=10000.000000,LinearAccelerationThresholdForTeleport=100000.000000,AngularAccelerationThresholdForTeleport=100000.000000,PositionChangeThresholdForTeleport=100.000000,OrientationChangeThresholdForTeleport=30.000000,LinearDragMultiplier=1.000000,AngularDragMultiplier=1.000000,ExternalLinearDrag=(X=0.000000,Y=0.000000,Z=0.000000),ExternalLinearVelocity=(X=0.000000,Y=0.000000,Z=0.000000),ExternalAngularVelocity=(X=0.000000,Y=0.000000,Z=0.000000),ExternalTurbulenceVelocity=(X=0.000000,Y=0.000000,Z=0.000000)) |
