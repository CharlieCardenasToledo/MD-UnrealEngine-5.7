# Rotation Constraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RotationConstraint

> Application Version: 5.7

### Description

Constrains an item's rotation to multiple items' rotations

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent,Orientation,Orient,Rotate |
| Type | [FRigUnit\_RotationConstraintLocalSpaceOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_RotationConstraintLocal-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to constrain | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bMaintainOffset | If True the offset will be computed based on the current delta between each child and parent | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | The filter to apply on the transform | [Filter Option Per Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FFilterOptionPerAxis) | (bX=True,bY=True,bZ=True) |
| Parents | The array of parents to constrain the child to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings of the constraint operation | [Rig Unit Rotation Constraint Advanced Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_RotationConstraint_Adva-) | (InterpolationType=Average,RotationOrderForFilter=XZY) |
| Weight | The weight to use when applying the resulting transform to the child | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
