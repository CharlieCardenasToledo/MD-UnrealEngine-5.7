# AutoCluster

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster

> Application Version: 5.7

### Description

AutoCluster (v1)

Automatically group pieces of a fractured Collection into a specified number of clusters

Input(s) :
ClusterSites - Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries
ClusterFraction - Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process
SiteSize - Choose the Edge-Size of the cube used to groups bones under a cluster (in cm).
ClusterGridWidth - Choose the number of cluster sites to distribute along the X axis
ClusterGridDepth - Choose the number of cluster sites to distribute along the Y axis
ClusterGridHeight - Choose the number of cluster sites to distribute along the Z axis
MinimumSize - If a cluster has volume less than this value (in cm) cubed, then the auto-cluster process will attempt to merge it into a neighboring cluster.
Collection [Intrinsic] - Fractured GeometryCollection to cluster
TransformSelection [Intrinsic] - Bone selection for the clustering

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FAutoClusterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAutoClusterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClusterSizeMethod | How to choose the size of the clusters to create | [EClusterSizeMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EClusterSizeMethodEnum) | Dataflow\_ClusterSizeMethod\_ByNumber |
| DriftIterations | For a grid distribution, optionally iteratively recenter the grid points to the center of the cluster geometry (technically: applying K-Means iterations) to balance the shape and distribution of the clusters | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bPreferConvexity | Whether to favor clusters that have a convex shape. (Note: Does not support ByGrid clustering.) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ConcavityTolerance | If > 0, cube root of maximum concave volume to add per cluster (ignoring concavity of individual parts) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AutoCluster | If true, bones will only be added to the same cluster if they are physically connected (either directly, or via other bones in the same cluster) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| EnforceSiteParameters | If true, make sure the site parameters are matched as close as possible ( bEnforceConnectivity can make the number of site larger than the requested input may produce without it ) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AvoidIsolated | If true, prevent the creation of clusters with only a single child. Either by merging into a neighboring cluster, or not creating the cluster. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color |  | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=0.000000,A=1.000000) |
| LineWidthMultiplier |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| CenterColor |  | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| CenterSize |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 12.000000 |
| bRandomizeColor | Randomize color per connection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection for the clustering | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| ClusterSites | Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| ClusterFraction | Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.250000 |
| SiteSize | Choose the Edge-Size of the cube used to groups bones under a cluster (in cm). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ClusterGridWidth | Choose the number of cluster sites to distribute along the X axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ClusterGridDepth | Choose the number of cluster sites to distribute along the Y axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ClusterGridHeight | Choose the number of cluster sites to distribute along the Z axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| MinimumSize | If a cluster has volume less than this value (in cm) cubed, then the auto-cluster process will attempt to merge it into a neighboring cluster. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bPreferConvexity | Whether to favor clusters that have a convex shape. (Note: Does not support ByGrid clustering.) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ConcavityTolerance | If > 0, cube root of maximum concave volume to add per cluster (ignoring concavity of individual parts) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
