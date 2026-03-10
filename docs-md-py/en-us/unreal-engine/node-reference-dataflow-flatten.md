# Flatten

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Flatten

> Application Version: 5.7

### Description

Flatten (v1)

Flattens selected bones. If no selection is provided, flattens all bones to level 1

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to flatten
OptionalTransformSelection - If connected, clusters under the selected bones will be flattened. If no selection is provided, all bones will be flattened to level 1.

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to flatten

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterFlattenDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterFlattenDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to flatten | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OptionalTransformSelection | If connected, clusters under the selected bones will be flattened. If no selection is provided, all bones will be flattened to level 1. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to flatten | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
