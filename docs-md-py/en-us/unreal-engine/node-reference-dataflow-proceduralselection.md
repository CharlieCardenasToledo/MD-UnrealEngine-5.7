# ProceduralSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ProceduralSelection

> Application Version: 5.7

### Description

ProceduralSelection (v1)

Procedurally generate a Cloth Selection set.

Input(s) :
ConversionInputName - Selection set to convert from when using Conversion selection type.

Output(s):
OutputName - The name to be use as a selection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Procedural Selection |
| Type | [FChaosClothAssetProceduralSelectionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetProceduralSelect-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Group | The type of element the selection refers to | [FChaosClothAssetNodeSelectionGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetNodeSelectionGro-) | (Name="") |
| SelectionType | The procedural selection method | [EChaosClothAssetProceduralSelectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetProceduralSelect-) | SelectAll |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| OutputName | The name to be use as a selection. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
