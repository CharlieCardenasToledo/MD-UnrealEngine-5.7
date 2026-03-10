# Set Physics Control Linear Damping Ratio

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlLinearDampingRatio

> Application Version: 5.7

### Description

Sets the Linear Damping Ratio of a Physics Control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlLinearDampingRatio](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlLine-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| DampingRatio | The linear damping ratio for the control. When this is 1, there is just enough damping to stop the control from oscillating about its target, due to the control strength (in the absence of any other influences). Values above this will add more damping, and values below will make the system tend to oscillate, as it will be under-ramped. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
