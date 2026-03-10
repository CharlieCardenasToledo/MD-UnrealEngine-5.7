# SimulationMassConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMassConfig

> Application Version: 5.7

### Description

SimulationMassConfig (v1)

Mass properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Mass Config |
| Type | [FChaosClothAssetSimulationMassConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSimulationMassCo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MassMode | How cloth particle mass is determined - Uniform Mass: Every particle's mass will be set to the value specified in the UniformMass setting. Mostly to avoid as it can cause some serious issues with irregular tessellations. - Total Mass: The total mass is distributed equally over all the particles. Useful when referencing a specific garment size and feel. - Density: A constant mass density is used. Density is usually the preferred way of setting mass since it allows matching real life materials' density values. | [EClothMassMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/ClothingSystemRuntimeCommon/EClothMassMode) | Density |
| UniformMassWeighted | The value used when the Mass Mode is set to Uniform Mass. | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=0.000150,High=0.000150,WeightMap="UniformMass",bImportFabricBounds=False,bBuildFabricMaps=False) |
| TotalMass | The value used when Mass Mode is set to TotalMass. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| DensityWeighted | Density in kg/m^2. Melton Wool: 0.7 Heavy leather: 0.6 Polyurethane: 0.5 Denim: 0.4 Light leather: 0.3 Cotton: 0.2 Silk: 0.1 | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=0.350000,High=0.350000,WeightMap="Density",bImportFabricBounds=False,bBuildFabricMaps=False) |
| MinPerParticleMass | Calculated particle masses will be clamped to this minimum value (or 1e-8, whichever is larger). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000100 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
