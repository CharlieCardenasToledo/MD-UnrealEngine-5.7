# ClusterMergeToNeighbors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors

> Application Version: 5.7

### Description

ClusterMergeToNeighbors (v1)

Merge selected bones to their neighbors

Input(s) :
Collection [Intrinsic] - Collection on which to merge bones into a neighboring cluster
TransformSelection - Bone selection
MinVolumeCubeRoot - Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value
bOnlyToConnected - Whether to only allow clusters to merge if their bones are connected in the proximity graph
bOnlySameParent - Whether to only allow clusters to merge if they have the same parent bone

Output(s):
Collection [Passthrough] - Collection on which to merge bones into a neighboring cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterMergeToNeighborsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterMergeToNeighborsDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NeighborSelectionMethod | Method to choose which neighbor to merge | [EClusterNeighborSelectionMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EClusterNeighborSelectionMethodE-) | Dataflow\_ClusterNeighborSelectionMethod\_LargestNeighbor |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a neighboring cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| MinVolumeCubeRoot | Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bOnlyToConnected | Whether to only allow clusters to merge if their bones are connected in the proximity graph | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bOnlySameParent | Whether to only allow clusters to merge if they have the same parent bone | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a neighboring cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
