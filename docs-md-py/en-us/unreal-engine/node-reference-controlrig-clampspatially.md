# ClampSpatially

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampSpatially

> Application Version: 5.7

### Description

Clamps a transform's position using a plane collision, cylindric collision or spherical collision.
Clamps a position using a plane collision, cylindric collision or spherical collision.
The collision happens both towards an inner envelope (minimum) and towards an outer envelope (maximum).
You can disable the inner / outer envelope / collision by setting the minimum / maximum to 0.0.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | ClampSpatially,Clamp Spatially,Collide,Collision |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input transform to clamp | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Axis | The axis to use for the filter | [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | X |
| Type | The filter / spatial mode to use | [Rig VMClamp Spatial Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMClampSpatialMode__Type) | Plane |
| Minimum | The minimum allowed distance at which a collision occurs. Note: For capsule this represents the radius. Disable by setting to 0.0. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | This maximum allowed distance. A collision will occur towards the center at this wall. Note: For capsule this represents the length. Disable by setting to 0.0. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| Space | The space this spatial clamp happens within. The input position will be projected into this space. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bDrawDebug | Draws debug information if True | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugColor | The color to use for the debug draw | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| DebugThickness | The thickness to use for the debug draw | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting transform with a clamped position | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
