# ClothAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetTerminal

> Application Version: 5.7

### Description

ClothAssetTerminal (v2)

Cloth terminal node to generate a cloth asset from a cloth collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Terminal |
| Type | [FChaosClothAssetTerminalNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetTerminalNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Refresh | Refresh the asset even if the ClothCollection hasn't changed. Note that it is not required to manually refresh the cloth asset, this is done automatically when there is a change in the Dataflow. This function is a developper utility used for debugging. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
