# Update Physics Control Target

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UpdatePhysicsControlTarget

> Application Version: 5.7

### Description

Sets the target for a physics control and updates the target velocities based on the previews
targets (which will be overwritten)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyUpdateControlTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyUpdateControlT-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| TargetPosition | The target position of the child body, relative to the parent body | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| TargetOrientation | The target orientation of the child body, relative to the parent body | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Pitch=0.000000,Yaw=0.000000,Roll=0.000000) |
| DeltaTime | The delta time used to calculate the target velocity | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
