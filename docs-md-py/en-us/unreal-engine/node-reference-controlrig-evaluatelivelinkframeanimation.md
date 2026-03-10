# Evaluate Live Link Frame (Animation)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameAnimation

> Application Version: 5.7

### Description

Evaluate current Live Link Animation associated with supplied subject

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkEvaluteFrameAnimation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkEvaluteFrameAni-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectName | The name of the subject to evaluate a frame for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bDrawDebug | If True debug data will be drawn for the subject | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugColor | The color to use for the debug drawing | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| DebugDrawOffset | The world offset to use when drawing the debug data | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectFrame | The resulting subject's frame | [Subject Frame Handle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/LiveLinkInterface/FSubjectFrameHandle) |  |
