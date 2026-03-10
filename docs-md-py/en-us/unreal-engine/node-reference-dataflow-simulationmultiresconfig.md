# SimulationMultiResConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMultiResConfig

> Application Version: 5.7

### Description

SimulationMultiResConfig (v1)
Experimental

Experimental Solver multires configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation MultiRes Config |
| Type | [FChaosClothAssetSimulationMultiResConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_22) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bIsFineLOD | Enable multi-res simulation for this LOD. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bIsCoarseMultiResLOD | This LOD is a coarse LOD for a finer LOD's multi-res simulation. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MultiResCoarseLODIndex | Index of the coarse LOD for multi-res simulation. That LOD also needs a Multi Res Config node with "Is Coarse Multi Res LOD" = true. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| bMultiResUseXPBD | Use XPBD-style constraints | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MultiResStiffness | MultiRes Spring Stiffness | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="WeightMap",bImportFabricBounds=False,bBuildFabricMaps=False) |
| MultiResVelocityTargetStiffness | MultiRes Velocity Target Spring Stiffness (non-XPBD only) | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="WeightMap",bImportFabricBounds=False,bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
