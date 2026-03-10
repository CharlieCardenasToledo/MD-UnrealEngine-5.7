# CollectionTransformSelectByPercentage

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByPercentage

> Application Version: 5.7

### Description

CollectionTransformSelectByPercentage (v1)

Outputs the specified percentage of the selected bones

Input(s) :
TransformSelection [Intrinsic] - Array of the selected bone indices
RandomSeed - Seed value for the random generation

Output(s):
TransformSelection [Passthrough] - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionByPercentageDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Percentage | Percentage to keep from the original selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| bDeterministic | Sets the random generation to deterministic | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Percentage | Percentage to keep from the original selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| RandomSeed | Seed value for the random generation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -94812.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
