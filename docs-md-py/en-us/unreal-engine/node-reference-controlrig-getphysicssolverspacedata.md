# Get Physics Solver Space Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsSolverSpaceData

> Application Version: 5.7

### Description

Retrieves the simulation space data that were generated during the simulation step, so the values
returned will relate to the previous update if the solver has not yet been stepped.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Debug |
| Type | [FRigUnit\_GetPhysicsSolverSpaceData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_GetPhysicsSolverSpaceDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The solver to relate this new physics element to | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| LinearVelocity | The velocity of the simulation space (in world space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| AngularVelocity | The angular velocity of the simulation space (in world space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| LinearAcceleration | The linear acceleration of the simulation space (in world space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| AngularAcceleration | The angular acceleration of the simulation space (in world space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Gravity | The gravitational acceleration that will be applied (in simulation space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
