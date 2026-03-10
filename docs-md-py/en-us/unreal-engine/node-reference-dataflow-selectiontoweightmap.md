# SelectionToWeightMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap

> Application Version: 5.7

### Description

SelectionToWeightMap (v1)

Convert an integer index selection to a vertex weight map where different map values can be set for selected and unselected vertices.

Input(s) :
SelectionName - The name of the selection to convert.

Output(s):
WeightMapName - The name of the weight map attribute that will be added to the collection.
If left empty the same name as the selection name will be used instead.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Selection To Weight Map |
| Type | [FChaosClothAssetSelectionToWeightMapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSelectionToWeigh-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| UnselectedValue | The value unselected vertices receive. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SelectedValue | The value selected vertices receive. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SelectionName | The name of the selection to convert. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| WeightMapName | The name of the weight map attribute that will be added to the collection. If left empty the same name as the selection name will be used instead. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
