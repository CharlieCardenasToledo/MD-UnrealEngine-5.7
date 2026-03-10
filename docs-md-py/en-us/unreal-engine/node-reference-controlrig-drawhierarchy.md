# Draw Hierarchy

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawHierarchy

> Application Version: 5.7

### Description

Draws vectors on each bone in the viewport across the entire hierarchy

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Debug |
| Type | [FRigUnit\_DebugHierarchy](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DebugHierarchy) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | the items to draw the pose for. if this is empty we'll draw the whole hierarchy | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Scale | The scale to apply to the drawn transform | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Color | The color to use when drawing | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| Thickness | The line thickness to use when drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the drawn transform with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |
