# SpawnAnimationChannel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnAnimationChannel

> Application Version: 5.7

### Description

Adds a new animation channel to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | SpawnAnimationChannel,Spawn Bool Animation Channel,Construction,Create,New,AddAnimationChannel,NewAnimationChannel,CreateAnimationChannel,AddChannel,NewChannel,CreateChannel,SpawnChannel,Spawn Float Animation Channel,Spawn Vector2D Animation Channel,Spawn Vector Animation Channel,Spawn Rotator Animation Channel |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InitialValue | The initial value of the new animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MinimumValue | The minimum value of the new animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaximumValue | The maximum value for the animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| LimitsEnabled | The enable settings for the limits | [Rig Unit Hierarchy Add Animation Channel Empty Limit Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_2)   [Rig Unit Hierarchy Add Animation Channel Single Limit Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_9)   [FRigUnit\_HierarchyAddAnimationChannel2DLimitSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-)   [FRigUnit\_HierarchyAddAnimationChannelVectorLimitSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_12)   [FRigUnit\_HierarchyAddAnimationChannelRotatorLimitSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_6) | () |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewChannel |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |
