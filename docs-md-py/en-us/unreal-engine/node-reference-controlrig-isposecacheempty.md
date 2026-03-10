# Is Pose Cache Empty

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsPoseCacheEmpty

> Application Version: 5.7

### Description

Returns true if the hierarchy pose is empty (has no items)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseIsEmpty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseIsEmpty) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to check | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IsEmpty | True if the pose is empty | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
