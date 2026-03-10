# Set Physics Solver External Velocity

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsSolverExternalVelocity

> Application Version: 5.7

### Description

Sets the external velocity of the simulation - used for adding wind effects

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_SetPhysicsSolverExternalVelocity](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_SetPhysicsSolverExterna-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The physics solver | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| ExternalLinearVelocity | Additional velocity that is added to the component velocity so the simulation acts as if the actor is moving at speed, even when stationary. The vector is in world space. This could be used for wind effects etc. Typical values are similar to the velocity of the object or effect, and usually around or less than 1000 for characters/wind. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ExternalAngularVelocity | Additional angular velocity that is added to the component angular velocity. This can be used to make the simulation act as if the actor is rotating even when it is not. E.g., to apply physics to a character on a podium as the camera rotates around it, to emulate the podium itself rotating. Vector is in world space. Units are deg/s. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ExternalTurbulenceVelocity | This will treat the external velocity like a wind field and add turbulence to it. Units are the same as velocity, so this is the approximate magnitude of the turbulence. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
