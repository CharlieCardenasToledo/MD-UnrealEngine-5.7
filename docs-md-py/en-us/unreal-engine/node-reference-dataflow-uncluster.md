# Uncluster

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Uncluster

> Application Version: 5.7

### Description

Uncluster (v1)

Uncluster selected nodes

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to uncluster
TransformSelection - Bone selection

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to uncluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterUnclusterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterUnclusterDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to uncluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to uncluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
