# Set Physics Body Material

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMaterial

> Application Version: 5.7

### Description

Applies the material settings to all the collision shapes

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyMaterial](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_4) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| Material | The physics material to be used for collision on the Physics Body | [Rig Physics Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsMaterial) | (Friction=1.000000,Restitution=0.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply) |
