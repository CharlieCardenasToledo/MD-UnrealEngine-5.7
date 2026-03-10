# BuildGuidesLODs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildGuidesLODs

> Application Version: 5.7

### Description

BuildGuidesLODs (v1)
Experimental

Builds the guides LODs

Input(s) :
Collection - Managed array collection to be used to store data

Output(s):
Collection [Passthrough] - Managed array collection to be used to store data
CurveParentsKey - Curve parent indices key to be used in other nodes if necessary
CurveLodsKey - Curve lods indices key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Type | FBuildGuidesLODsDataflowNode |

### Inputs

| Name | Description | Type | DefaultValue |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

### Outputs

| Name | Description | Type |
| --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |
| CurveParentsKey | Curve parent indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |
| CurveLodsKey | Curve lods indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |
