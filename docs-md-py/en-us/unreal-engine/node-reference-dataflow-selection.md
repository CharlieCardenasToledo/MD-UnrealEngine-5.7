# Selection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection

> Application Version: 5.7

### Description

Selection (v2)

Chaos Cloth Asset Selection Node V 2

Input(s) :
TransferCollection - The collection used to transfer sets from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Selection |
| Type | [FChaosClothAssetSelectionNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSelectionNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutputName | The name to be use as a selection. | [FChaosClothAssetConnectableOStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableOStri-) | (StringValue="") |
| InputName | The name to populate this set from and override based on Selection Override Type. Output Name will be used if Input Name is empty. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |
| SelectionOverrideType | How to apply this node's Indices onto existing sets. Changing this value will change the output set. To change how the node's stored indices are calculated, change the equivalent value on the Selection Tool context. | [EChaosClothAssetSelectionOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetSelectionOverrid-) | ReplaceAll |
| Group | The type of element the selection refers to | [FChaosClothAssetNodeSelectionGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetNodeSelectionGro-) | (Name="") |
| Indices | Selected element indices | [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | () |
| RemoveIndices | Indices to remove from the Input selection | [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | () |
| Import | Import (replace) the current selection from the input Collection's selection with the given Input Name (or Output Name if Input Name is empty). | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ImportSecondary | Import (replace) the current selection from the input Collection's secondary selection with the given Input Name (or Output Name if Input Name is empty). Secondary selections are only supported in v1 of this node. This function is provided as a migration tool to this current version. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| SimTransferType | The type of transfer used to transfer the sim mesh sets when a TransferCollection is connected. This property is disabled when no TransferCollection input has been connected. | [EChaosClothAssetWeightMapTransferType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapTransfe-) | Use2DSimMesh |
| TransferSelectionThreshold | Selections are internally converted to maps in order to do the transfer and then converted back. This value is used to do the conversion back. Decrease this value to (possibly) expand the converted selection. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.950000 |
| Transfer | Transfer the selection from the connected Transfer Collection containing a selection with Input Name (or Output Name if Input Name is empty). | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransferCollection | The collection used to transfer sets from. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| OutputName.StringValue | The value for this property. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
