# Calculate Physics Collision

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CalculatePhysicsCollision

> Application Version: 5.7

### Description

Discards any existing collision data and replaces it with a box based on the joint positions.
Note that this must be called before the physics solver is instantiated/stepped.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyAutoCalculateCollision](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyAutoCalculateC-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| MinAspectRatio | For boxes: The minimum box extent, as a proportion of the maximum box extent. For capsules: The minimum radius, as a proportion of the length (not including the radius) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.250000 |
| MinSize | For boxes: The minimum side length. For capsules: The minimum radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
