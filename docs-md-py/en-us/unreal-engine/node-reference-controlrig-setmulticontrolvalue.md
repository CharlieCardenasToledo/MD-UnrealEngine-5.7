# SetMultiControlValue

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultiControlValue

> Application Version: 5.7

### Description

SetMultiControlFloat is used to perform a change in the hierarchy by setting multiple controls' float value.
SetMultiControlInteger is used to perform a change in the hierarchy by setting multiple controls' integer value.
SetMultiControlVector2D is used to perform a change in the hierarchy by setting multiple controls' vector2D value.
SetMultiControlRotator is used to perform a change in the hierarchy by setting multiple controls' rotator value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetMultiControlValue,Set Multiple Controls Float,SetMultipleControlsFloat,SetControlFloat,SetGizmoFloat,Set Multiple Controls Integer,SetMultipleControlsInteger,SetControlInteger,SetGizmoInteger,Set Multiple Controls Vector2D,SetMultipleControlsVector2D,SetControlVector2D,SetGizmoVector2D,Set Multiple Controls Rotator,SetMultipleControlsRotator,SetControlRotator,SetGizmoRotator |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Entries | The array of control-float pairs to be processed | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlFloat\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlFloat_En-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlInteger\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlInteger_-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlVector2D\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlVector2D-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlRotator\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlRotator_-)> | (()) |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
