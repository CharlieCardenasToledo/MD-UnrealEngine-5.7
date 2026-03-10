# Set Physics Body Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyData

> Application Version: 5.7

### Description

Sets all the data on a body - but in a sparse way so you can decide which parameters get applied.
Note that the sparse data does not get displayed correctly (the flags that enable/disable all end up getting
reset if the user attempts to change them) so this should be used with caution until this is fixed.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodySparseData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_8) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| Data | Sparse data to be set on the Physics Body | [Physics Control Modifier Sparse Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlModifierSparseDat-) | (MovementType=Simulated,CollisionType=QueryAndPhysics,GravityMultiplier=1.000000,PhysicsBlendWeight=1.000000,KinematicTargetSpace=OffsetInBoneSpace,bUpdateKinematicFromSimulation=True,bEnableMovementType=True,bEnableCollisionType=True,bEnableGravityMultiplier=True,bEnablePhysicsBlendWeight=True,bEnableKinematicTargetSpace=True,bEnablebUpdateKinematicFromSimulation=True) |
