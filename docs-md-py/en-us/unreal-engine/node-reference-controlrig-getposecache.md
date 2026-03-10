# Get Pose Cache

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCache

> Application Version: 5.7

### Description

Returns the hierarchy's pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_HierarchyGetPoseItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyGetPoseItemArr-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Initial | If True the pose will use the initial transforms | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ElementType | The element type to retrieve the pose for | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |
| ItemsToGet | An optional collection to filter against | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The resulting pose | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) |  |
