# GetCurveAttributes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCurveAttributes

> Application Version: 5.7

### Description

GetCurveAttributes (v1)
Experimental

Get the kinematic weights attributes names

Output(s):
AttributeKey - Attribute key to build

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGetCurveAttributesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGetCurveAttributesDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeType | Type of attribute to use | [EGroomAttributeType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/EGroomAttributeType) | KinematicWeights |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeKey | Attribute key to build | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
