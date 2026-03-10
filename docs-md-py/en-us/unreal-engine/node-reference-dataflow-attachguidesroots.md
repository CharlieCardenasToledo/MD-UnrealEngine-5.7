# AttachGuidesRoots

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AttachGuidesRoots

> Application Version: 5.7

### Description

AttachGuidesRoots (v1)
Experimental

Attach the guides roots by setting their kinematic weights to 1.0f

Input(s) :
Collection - Managed array collection to be used to store datas

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
KinematicWeightsKey - Point Kinematic weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Type | FAttachGuidesRootsDataflowNode |

### Inputs

| Name | Description | Type | DefaultValue |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

### Outputs

| Name | Description | Type |
| --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |
| KinematicWeightsKey | Point Kinematic weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |
