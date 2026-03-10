# Visual Debug Vector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebugVector

> Application Version: 5.7

### Description

Debug draw parameters for a Point or Vector given a vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,Point |
| Type | [FRigVMFunction\_VisualDebugVectorNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualDebugVector-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The pass through vector to draw | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Mode | The mode to draw the vector with | [Rig Unit Visual Debug Point Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigUnitVisualDebugPointMode) | Point |
| Color | The color to use for the debug draw | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use for the drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Scale | The scale to apply to the vector when drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |
