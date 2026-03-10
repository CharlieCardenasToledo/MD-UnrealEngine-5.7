# Parent Constraint Math

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraintMath

> Application Version: 5.7

### Description

Computes the output transform by constraining the input transform to multiple parents

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent,Orient,Scale |
| Type | [FRigUnit\_ParentConstraintMath](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraintMath) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Input | Input is used to calculate offsets from parents' initial transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Parents | The array of parents to compute the constrained transform for | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings to use for the constraint compute | [Rig Unit Parent Constraint Math Advanced Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraintMath_Ad-) | (InterpolationType=Average) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output | The resulting constrained transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
