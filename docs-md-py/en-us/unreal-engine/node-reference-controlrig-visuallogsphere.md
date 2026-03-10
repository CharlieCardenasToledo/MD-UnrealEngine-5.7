# Visual Log Sphere

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogSphere

> Application Version: 5.7

### Description

Logs sphere shape - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogSphere) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Center | The centre of the sphere | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Radius | The radius of the sphere | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| bWireframe | Whether to display as wireframe | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |
