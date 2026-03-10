# WeightMapToSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WeightMapToSelection

> Application Version: 5.7

### Description

WeightMapToSelection (v1)

Convert a vertex weight map to an integer selection set.

Input(s) :
WeightMapName - The name of the Weight Map to convert.

Output(s):
SelectionName - The name of the select attribute that will be added to the collection.
If left empty the same name as the Weight Map name will be used instead.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Weight Map To Selection |
| Type | [FChaosClothAssetWeightMapToSelectionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightMapToSelec-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionType | The type of element the selection refers to | [EChaosClothAssetWeightMapConvertableSelectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_5) | SimVertices3D |
| SelectionThreshold | Map values above this will be selected. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.950000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| WeightMapName | The name of the Weight Map to convert. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SelectionName | The name of the select attribute that will be added to the collection. If left empty the same name as the Weight Map name will be used instead. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
