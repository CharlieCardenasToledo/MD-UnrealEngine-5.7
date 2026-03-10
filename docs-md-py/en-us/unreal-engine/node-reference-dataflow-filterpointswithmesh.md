# FilterPointsWithMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh

> Application Version: 5.7

### Description

FilterPointsWithMesh (v1)

Filter a point set to only the points inside or outside of a given mesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to use to filter point set
bKeepInside - Whether to keep the points inside or (if false) outside the mesh, when filtering by Winding Number.
WindingThreshold - The winding number threshold to use for determining whether a point is inside or outside of the mesh, if corresponding Filter Method is set
MinDistance - The min distance to surface to keep, if corresponding Filter Method is set
MaxDistance - The max distance to surface to keep, if corresponding Filter Method is set
bUseSignedDistance - Whether to use signed distances for the Min and Max Distance thresholds. Otherwise, unsigned distance is used.
Note: Signs are computed via the Winding Number. The sign is negative if the point's Winding Number is below the Winding Threshold.
SamplePoints - Points to filter

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | FFilterPointSetWithMeshDataflowNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FilterMethod |  | [uint8](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to use to filter point set | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SamplePoints | Points to filter | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| bKeepInside | Whether to keep the points inside or (if false) outside the mesh, when filtering by Winding Number. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| WindingThreshold | The winding number threshold to use for determining whether a point is inside or outside of the mesh, if corresponding Filter Method is set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| MinDistance | The min distance to surface to keep, if corresponding Filter Method is set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxDistance | The max distance to surface to keep, if corresponding Filter Method is set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| bUseSignedDistance | Whether to use signed distances for the Min and Max Distance thresholds. Otherwise, unsigned distance is used. Note: Signs are computed via the Winding Number. The sign is negative if the point's Winding Number is below the Winding Threshold. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Points to filter | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
