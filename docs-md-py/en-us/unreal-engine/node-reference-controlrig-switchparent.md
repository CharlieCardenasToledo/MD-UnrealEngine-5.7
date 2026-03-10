# Switch Parent

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SwitchParent

> Application Version: 5.7

### Description

Switches an element to a new parent.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Children,Parent,Constraint,Space,Switch |
| Type | [FRigUnit\_SwitchParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SwitchParent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mode | Depending on this the child will switch to the world, \* back to its default or to the item provided by the Parent pin | [Rig Switch Parent Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigSwitchParentMode) | ParentItem |
| Child | The child to switch to a new parent | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Parent | The optional parent to switch to. This is only used if the mode is set to 'Parent Item' | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| bMaintainGlobal | If set to true the item will maintain its global transform, \* otherwise it will maintain local | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
