# ClusterScatterPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints

> Application Version: 5.7

### Description

ClusterScatterPoints (v1)

Cluster Scatter Points Dataflow Node

Input(s) :
NumberClustersMin - Minimum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max
NumberClustersMax - Maximum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max
PointsPerClusterMin - Minimum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max
PointsPerClusterMax - Maximum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max
ClusterRadiusFractionMin - Minimum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this.
Each point will be placed at least this far (plus the Cluster Radius Offset) from its cluster center.
ClusterRadiusFractionMax - Maximum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this.
Each point will be placed at most this far (plus the Cluster Radius Offset) from its cluster center.
ClusterRadiusOffset - Cluster radius offset (in cm). This offset will be added to the 'Min/Max Dist from Center' distance
RandomSeed - Seed for random
BoundingBox - BoundingBox to generate points inside of

Output(s):
Points - Generated points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FClusterScatterPointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterScatterPointsDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | BoundingBox to generate points inside of | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| NumberClustersMin | Minimum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| NumberClustersMax | Maximum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| PointsPerClusterMin | Minimum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| PointsPerClusterMax | Maximum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 30 |
| ClusterRadiusFractionMin | Minimum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this. Each point will be placed at least this far (plus the Cluster Radius Offset) from its cluster center. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| ClusterRadiusFractionMax | Maximum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this. Each point will be placed at most this far (plus the Cluster Radius Offset) from its cluster center. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.200000 |
| ClusterRadiusOffset | Cluster radius offset (in cm). This offset will be added to the 'Min/Max Dist from Center' distance | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Generated points | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
