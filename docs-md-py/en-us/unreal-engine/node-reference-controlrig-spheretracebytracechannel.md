# Sphere Trace By Trace Channel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByTraceChannel

> Application Version: 5.7

### Description

Sweeps a sphere against the world and return the first blocking hit using a specific channel. Target objects can have different object types, but they need to have the same trace channel set to "block" in their collision response settings.
You can create custom trace channels in Project Setting - Collision.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Collision |
| Tags | Sweep,Raytrace,Collision,Collide,Trace |
| Type | [FRigUnit\_SphereTraceByTraceChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SphereTraceByTraceChann-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | Start of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | End of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| TraceChannel | The 'channel' that this trace is in, used to determine which components to hit | [Trace Type Query](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/ETraceTypeQuery) | TraceTypeQuery1 |
| Radius | Radius of the sphere to use for sweeping / tracing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bHit | Returns true if there was a hit | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitLocation | Hit location in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitNormal | Hit normal in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
