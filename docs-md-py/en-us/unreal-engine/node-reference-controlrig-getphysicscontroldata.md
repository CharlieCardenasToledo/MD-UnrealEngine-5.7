# Get Physics Control Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsControlData

> Application Version: 5.7

### Description

Gets the control data for a physics control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyGetControlData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyGetControlData) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component from which to retrieve data | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ControlData | The current control data (strengths etc) | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) |  |
