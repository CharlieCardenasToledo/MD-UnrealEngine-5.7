# CorrectSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights

> Application Version: 5.7

### Description

CorrectSkinWeights (v1)
Experimental

Correct skin weights vertex properties.

Input(s) :
BoneIndicesKey - Bone indices key to be used in other nodes if necessary
BoneWeightsKey - Bone weights key to be used in other nodes if necessary
SelectionMapKey - Selection map key to be used in other nodes if necessary
SmoothingIterations - Number of iteration required for the smoothing
SmoothingFactor - Lerp value in between the current and the average weight values
bUseSelectionAsPerVertexFactor - When true, use the decimal values of the selection as a per vertex factor for the selected operation - Currently available for Relax operation only - false by default
PruningThreshold - All weights below this threshold will be pruned
ClampingNumber - Max number of bones to consider for the skin weights
SelectionThreshold - Selection threshold to consider a neighbor skin weight

Output(s):
BoneIndicesKey [Passthrough] - Bone indices key to be used in other nodes if necessary
BoneWeightsKey [Passthrough] - Bone weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [DataflowEditor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor) |
| Category | Collection |
| Tags | Correct skin weights and save it to collection |
| Type | [FDataflowCorrectSkinWeightsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/FDataflowCorrectSkinWeightsNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndicesName | The name to be set for the bone indices. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| BoneWeightsName | The name to be set for the bone weights. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| SelectionMapName | Map name to be used to select vertices to correct | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| CorrectionType | Selection map key to be used in other nodes if necessary | [ESkinWeightsCorrectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/ESkinWeightsCorrectionType) | Relax |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SelectionMapKey | Selection map key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SmoothingIterations | Number of iteration required for the smoothing | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| SmoothingFactor | Lerp value in between the current and the average weight values | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| bUseSelectionAsPerVertexFactor | When true, use the decimal values of the selection as a per vertex factor for the selected operation - Currently available for Relax operation only - false by default | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| PruningThreshold | All weights below this threshold will be pruned | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| ClampingNumber | Max number of bones to consider for the skin weights | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| SelectionThreshold | Selection threshold to consider a neighbor skin weight | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
