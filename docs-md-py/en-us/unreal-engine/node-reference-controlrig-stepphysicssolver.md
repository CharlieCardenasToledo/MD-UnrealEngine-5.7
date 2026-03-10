# Step Physics Solver

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StepPhysicsSolver

> Application Version: 5.7

### Description

Steps the specified physics solver

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Simulate |
| Type | [FRigUnit\_StepPhysicsSolver](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_StepPhysicsSolver) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The physics solver that should be stepped | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| DeltaTimeOverride | If this is zero, then the execute context time will be used. If this is positive then it will override the delta time. A negative value will prevent the solver from stepping, but there will still be update costs associated with the node. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SimulationSpaceDeltaTimeOverride | If this is zero, then the simulation delta time will be used for evaluating movement of the simulation space. If this is positive then it will override. This may be needed if the component movement is being done in parallel, in which case you might need to pass in the previous time delta here. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Alpha | How much of the simulation is combined with the input bone. This currently happens in component space. Note that the simulation will continue to run, even if alpha = 0 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| VisualizationSettings | Settings that specify how the solver state should be visualized during/after the step | [Rig Physics Visualization Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsVisualizationSettings) | (bEnableVisualization=True,LineThickness=1.000000,ShapeSize=1,ShapeDetail=16,bShowBodies=True,bShowCentreOfMass=False,bShowJoints=True,bShowControls=False,bShowWorldObjects=True,bShowWorldOverlapBox=False,bShowActiveContacts=True,bShowInactiveContacts=False) |
