# Apply Pose Cache

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ApplyPoseCache

> Application Version: 5.7

### Description

Sets the hierarchy's pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_HierarchySetPoseItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchySetPoseItemArr-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to apply to the hierarchy | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| ElementType | The types of element to apply the pose for | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |
| Space | The space to use to apply the pose in | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| ItemsToSet | An optional collection to filter against | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Weight | The weight to use when applying the transforms | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
