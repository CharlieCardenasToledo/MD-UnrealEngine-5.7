# Get Pose Cache Items

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheItems

> Application Version: 5.7

### Description

Returns the items in the hierarchy pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetItemsItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetItemsItemArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to retrieve the items from | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| ElementType | The type of items to retrieve | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting items in the pose | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |
