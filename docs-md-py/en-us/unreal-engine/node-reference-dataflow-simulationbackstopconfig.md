# SimulationBackstopConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBackstopConfig

> Application Version: 5.7

### Description

SimulationBackstopConfig (v1)

Backstop properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Backstop Config |
| Type | [FChaosClothAssetSimulationBackstopConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_8) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BackstopDistance | The distance from the surface of a backstop collision sphere to its associated particle's skinned position along the mesh normal. Can be positive or negative depending on the desired effect. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=100.000000,WeightMap="BackstopDistance",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BackstopRadius | The radius of the backstop sphere that each particle collides with. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=100.000000,WeightMap="BackstopRadius",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BackstopMeshName | The name of the accessory mesh to use as the backstop mesh. If none is specified, the default animated mesh will be used | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
