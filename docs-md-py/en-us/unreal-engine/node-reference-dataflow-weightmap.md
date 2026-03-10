# WeightMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WeightMap

> Application Version: 5.7

### Description

WeightMap (v1)

For Name implicit operators.

Input(s) :
TransferCollection - The collection used to transfer weight map from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Weight Map |
| Type | [FChaosClothAssetWeightMapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightMapNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutputName | The name to be set as a weight map attribute. | [FChaosClothAssetConnectableOStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableOStri-) | (StringValue="") |
| InputName | The name to populate this map from and override based on Map Override Type. Output Name will be used if Input Name is empty. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |
| MeshTarget |  | [EChaosClothAssetWeightMapMeshTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapMeshTar-) | Simulation |
| MapOverrideType | How to apply this node's weight values onto existing maps. Changing this value will change the output map. To change how the node's stored weights are calculated, change the equivalent value on the Weight Map Paint Tool context. | [EChaosClothAssetWeightMapOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapOverrid-) | ReplaceChanged |
| TransferType | The type of transfer used to transfer the weight map when a TransferCollection is connected and MeshTarget is Simulation. Render weight maps always do a 3D transfer. This property is disabled when no TransferCollection input has been connected. | [EChaosClothAssetWeightMapTransferType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapTransfe-) | Use2DSimMesh |
| Transfer | Transfer the weight map from the connected Transfer Collection containing a weight map with Input Name (or Output Name if Input Name is empty). | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransferCollection | The collection used to transfer weight map from. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| OutputName.StringValue | The value for this property. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
