# Aim Constraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AimConstraint

> Application Version: 5.7

### Description

Orients an item such that its aim axis points towards a global target.
Note: This node operates in global space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Lookat, Aim |
| Type | [FRigUnit\_AimConstraintLocalSpaceOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraintLocalSpace-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The name of the item to apply aim | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| bMaintainOffset | Maintains the offset between child and weighted average of parents based on initial transforms | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | Filters the final rotation by axes based on the euler rotation order defined in the node's advanced settings If flipping is observed, try adjusting the rotation order | [Filter Option Per Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FFilterOptionPerAxis) | (bX=True,bY=True,bZ=True) |
| AimAxis | Child is rotated so that its AimAxis points to the parents | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| UpAxis | Child is rotated around the AimAxis so that its UpAxis points to/Aligns with the WorldUp target | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| WorldUp | Defines how Child should rotate around the AimAxis. This is the aim target for the UpAxis | [Rig Unit Aim Constraint World Up](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraint_WorldUp) | (Target=(X=0.000000,Y=0.000000,Z=1.000000),Kind=Direction,Space=(Type=None,Name="")) |
| Parents | The array of parents to constaint this aim to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings to use for the constraint | [Rig Unit Aim Constraint Advanced Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraint_AdvancedS-) | (DebugSettings=(bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))),RotationOrderForFilter=XZY) |
| Weight | The weight to use when applying the resulting transform to the child | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
