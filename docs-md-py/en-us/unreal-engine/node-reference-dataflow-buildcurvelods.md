# BuildCurveLODs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs

> Application Version: 5.7

### Description

BuildCurveLODs (v1)
Experimental

Builds the curves LODs

Input(s) :
Collection - Managed array collection to be used to store data
CurveSelection - Curve selection to focus the geometry LODs spatially

Output(s):
Collection [Passthrough] - Managed array collection to be used to store data
CurveParentsKey - Curve parent indices key to be used in other nodes if necessary
CurveLodsKey - Curve lods indices key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildCurveLODsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildCurveLODsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the geometry LODs spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| CurveParentsKey | Curve parent indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| CurveLodsKey | Curve lods indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
