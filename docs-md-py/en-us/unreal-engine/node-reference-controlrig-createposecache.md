# Create Pose Cache

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CreatePoseCache

> Application Version: 5.7

### Description

Creates the hierarchy's pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State,MakePoseCache,NewPoseCache,EmptyPoseCache |
| Type | [FRigUnit\_HierarchyCreatePoseItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyCreatePoseItem-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Entries | The entries to create | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_HierarchyCreatePoseItemArray\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyCreatePoseItem-_1)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The resulting pose | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) |  |
