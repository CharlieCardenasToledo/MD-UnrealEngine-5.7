# BuildCurveWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights

> Application Version: 5.7

### Description

BuildCurveWeights (v1)
Experimental

Build a weight map that will be identical on every curves

Input(s) :
Collection - Managed array collection to be used to store datas
CurveSelection - Curve selection to focus the geometry transfer spatially
WeightsAttribute - Vertex kinematic weights key to be used in other nodes if necessary

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildCurveWeightsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildCurveWeightsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CurveWeights | This curve determines the weight value from root to tip. The X axis range is [0,1], 0 mapping the root and 1 the tip | [FRuntimeFloatCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=,DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the geometry transfer spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |
| WeightsAttribute | Vertex kinematic weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
