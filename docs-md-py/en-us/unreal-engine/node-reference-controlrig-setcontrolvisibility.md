# Set Control Visibility

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVisibility

> Application Version: 5.7

### Description

SetControlVisibility is used to change the visibility on a control at runtime

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlVisibility,Visibility,Hide,Show,Hidden,Visible,SetGizmoVisibility |
| Type | [FRigUnit\_SetControlVisibility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlVisibility) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The name of the Control to set the visibility for. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Pattern | If the ControlName is set to None this can be used to look for a series of Controls | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| bVisible | The visibility to set for the control | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
