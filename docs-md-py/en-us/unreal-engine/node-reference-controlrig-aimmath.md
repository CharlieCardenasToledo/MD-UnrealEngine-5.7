# Aim Math

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AimMath

> Application Version: 5.7

### Description

Outputs an aligned transform of a primary and secondary axis of an input transform to a world target.
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Lookat |
| Type | [FRigUnit\_AimBoneMath](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBoneMath) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InputTransform | The transform (in global space) before the aim was applied (optional) | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Primary | The primary target for the aim | [Rig Unit Aim Item Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=1.000000,Y=0.000000,Z=0.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Secondary | The secondary target for the aim - also referred to as PoleVector / UpVector | [Rig Unit Aim Item Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=0.000000,Y=0.000000,Z=1.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DebugSettings | The debug setting for the node | [Rig Unit Aim Bone Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBone_DebugSettings) | (bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
