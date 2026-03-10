# CollectionTransformSelectByFloatAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByFloatAttribute

> Application Version: 5.7

### Description

CollectionTransformSelectByFloatAttribute (v1)

Selects bones by a float attribute

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionByFloatAttrDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Group name for the attr | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Transform |
| AttrName | Attribute name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Min | Minimum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Max | Maximum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| RangeSetting | Values for the selection has to be inside or outside [Min, Max] range | [ERangeSettingEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERangeSettingEnum) | Dataflow\_RangeSetting\_InsideRange |
| bInclusive | If true then range includes Min and Max values | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Min | Minimum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Max | Maximum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
