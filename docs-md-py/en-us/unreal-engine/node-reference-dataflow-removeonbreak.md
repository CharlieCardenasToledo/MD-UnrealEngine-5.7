# RemoveOnBreak

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak

> Application Version: 5.7

### Description

RemoveOnBreak (v1)

Remove on Break Dataflow Node

Input(s) :
Collection [Intrinsic] - Collection to set theremoval data on
TransformSelection - selection to apply the data on ( if not specified the entire collection will be set )
bEnabledRemoval - Whether or not to enable the removal on the selection
PostBreakTimer - How long after the break the removal will start ( Min / Max )
RemovalTimer - How long removal will last ( Min / Max )
bClusterCrumbling - If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect

Output(s):
Collection [Passthrough] - Collection to set theremoval data on

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FRemoveOnBreakDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRemoveOnBreakDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to set theremoval data on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | selection to apply the data on ( if not specified the entire collection will be set ) | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| bEnabledRemoval | Whether or not to enable the removal on the selection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| PostBreakTimer | How long after the break the removal will start ( Min / Max ) | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| RemovalTimer | How long removal will last ( Min / Max ) | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000) |
| bClusterCrumbling | If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to set theremoval data on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
