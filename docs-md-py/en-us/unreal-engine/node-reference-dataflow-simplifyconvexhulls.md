# SimplifyConvexHulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimplifyConvexHulls

> Application Version: 5.7

### Description

SimplifyConvexHulls (v1)

Simplify Convex Hulls Dataflow Node

Input(s) :
OptionalSelectionFilter - Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed.
SimplificationAngleThreshold - Simplified hull should preserve angles larger than this (in degrees). Used by the AngleTolerance simplification method.
SimplificationDistanceThreshold - Simplified hull should stay within this distance of the initial convex hull. Used by the MeshQSlim simplification method.
MinTargetTriangleCount - The minimum number of faces to use for the convex hull. For MeshQSlim simplification, this is a triangle count, which may be further reduced on conversion back to a convex hull.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FSimplifyConvexHullsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSimplifyConvexHullsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimplifyMethod |  | [EConvexHullSimplifyMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EConvexHullSimplifyMethod) | MeshQSlim |
| bUseExistingVertices | Whether to restrict the simplified hulls to only use vertices from the original hulls. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OptionalSelectionFilter | Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| SimplificationAngleThreshold | Simplified hull should preserve angles larger than this (in degrees). Used by the AngleTolerance simplification method. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| SimplificationDistanceThreshold | Simplified hull should stay within this distance of the initial convex hull. Used by the MeshQSlim simplification method. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MinTargetTriangleCount | The minimum number of faces to use for the convex hull. For MeshQSlim simplification, this is a triangle count, which may be further reduced on conversion back to a convex hull. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
