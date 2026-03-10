# Sphere Trace By Object Types

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByObjectTypes

> Application Version: 5.7

### Description

Sweeps a sphere against the world and return the first blocking hit. The trace is filtered by object types only, the collision response settings are ignored.
You can create custom object types in Project Setting - Collision

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Collision |
| Tags | Sweep,Raytrace,Collision,Collide,Trace |
| Type | [FRigUnit\_SphereTraceByObjectTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SphereTraceByObjectType-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | Start of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | End of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ObjectTypes | The types of objects that this trace can hit | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EObjectTypeQuery](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/EObjectTypeQuery)>> | () |
| Radius | Radius of the sphere to use for sweeping / tracing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bHit | Returns true if there was a hit | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitLocation | Hit location in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitNormal | Hit normal in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
