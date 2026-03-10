# PaintWeightMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PaintWeightMap

> Application Version: 5.7

### Description

PaintWeightMap (v1)

Scalar vertex properties.

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Tags | Paint a weight map and save it to collection |
| Type | [FDataflowCollectionAddScalarVertexPropertyNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionAddScalarVert-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name to be set as a weight map attribute. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| TargetGroup |  | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| OverrideType | This type will define how the data are applied to the input data | [EDataflowWeightMapOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/EDataflowWeightMapOverrideType) | ReplaceAll |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey |  | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| AttributeKey |  | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
