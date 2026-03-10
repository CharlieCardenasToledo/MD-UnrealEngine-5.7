# Intersect Plane

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane

> Application Version: 5.7

## Intersect Plane (FRigVMFunction\_MathRayIntersectPlane)

Returns the closest point intersection of a ray with a plane

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Ray |
| Tags | Closest,Ray,Cross |
| Type | [FRigVMFunction\_MathRayIntersectPlane](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathRayIntersectP-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Ray | The ray to intersect with the plane | [Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |
| PlanePoint | The point on the plane to intersect the ray with | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PlaneNormal | The normal of the plane to intersect the ray with | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting intersection position | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance of the ray origin to the plane | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Ratio | The ratio along the ray up to the intersection point | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

## Intersect Plane (FRigVMFunction\_MathIntersectPlane)

Intersects a plane with a vector given a start and direction

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Collide,Intersect,Raycast |
| Type | [FRigVMFunction\_MathIntersectPlane](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathIntersectPlan-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | The start of the ray to intersect with the plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Direction | The direction of the ray to intersect with the plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| PlanePoint | The point on the plane to intersect with | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PlaneNormal | The normal of the plane to intersect with | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting position on the plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance along the ray to the intersection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
