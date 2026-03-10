# Aim

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Aim

> Application Version: 5.7

### Description

Aligns the rotation of a primary and secondary axis of an item to a global target.
Note: This node operates in global space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Lookat |
| Type | [FRigUnit\_AimItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The name of the item to align | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Primary | The primary target for the aim | [Rig Unit Aim Item Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=1.000000,Y=0.000000,Z=0.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Secondary | The secondary target for the aim - also referred to as PoleVector / UpVector | [Rig Unit Aim Item Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=0.000000,Y=0.000000,Z=1.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DebugSettings | The debug setting for the node | [Rig Unit Aim Bone Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBone_DebugSettings) | (bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |
