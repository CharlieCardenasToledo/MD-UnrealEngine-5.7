# SelectionToIntMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToIntMap

> Application Version: 5.7

### Description

SelectionToIntMap (v1)

Convert an integer index selection to an integer map. Map type will match the selection type.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Selection To Int Map |
| Type | [FChaosClothAssetSelectionToIntMapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSelectionToIntMa-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionName | The name of the selection to convert. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |
| IntMapName | The name of the integer map attribute that will be added to the collection. If left empty the same name as the selection name will be used instead. | [FChaosClothAssetConnectableIOStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIOStr-) | (StringValue="") |
| bKeepExistingUnselectedValues | If the IntMapName already exists, keep existing values rather than overwriting them with 'Unselected Value'. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| UnselectedValue | The value unselected elements receive. Unselected existing values can be kept by setting 'Keep Existing Unselected Values' | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SelectedValue | The value selected elements receive. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| IntMapName.StringValue | The value for this property. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
