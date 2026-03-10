# Spawn Integer Animation Channel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel

> Application Version: 5.7

### Description

Adds a new animation channel to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,AddAnimationChannel,NewAnimationChannel,CreateAnimationChannel,AddChannel,NewChannel,CreateChannel,SpawnChannel |
| Type | [FRigUnit\_HierarchyAddAnimationChannelInteger](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_4) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InitialValue | The initial value of the new animation channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MinimumValue | The minimum value of the new animation channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MaximumValue | The maximum value for the animation channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| LimitsEnabled | The enable settings for the limits | [Rig Unit Hierarchy Add Animation Channel Single Limit Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_9) | (Enabled=(bMinimum=True,bMaximum=True)) |
| ControlEnum | The enum to use to find valid values | Enum | None |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewChannel |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |
