# AttachCurveRoots

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AttachCurveRoots

> Application Version: 5.7

### Description

AttachCurveRoots (v1)
Experimental

Attach the curve roots by setting their kinematic weights to 1.0f

Input(s) :
Collection - Managed array collection to be used to store datas
CurveSelection - Curve selection to focus the geometry transfer spatially

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
KinematicWeightsKey - Vertex kinematic weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FAttachCurveRootsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FAttachCurveRootsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the geometry transfer spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| KinematicWeightsKey | Vertex kinematic weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
