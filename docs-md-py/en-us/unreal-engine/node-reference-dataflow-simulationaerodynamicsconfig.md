# SimulationAerodynamicsConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig

> Application Version: 5.7

### Description

SimulationAerodynamicsConfig (v1)

Aerodynamics properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Aerodynamics Config |
| Type | [FChaosClothAssetSimulationAerodynamicsConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_6) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FluidDensity | The density of the medium in which the aerodynamic forces take place, usually air. The fluid density is given in kg/m^3. Air density is considered to be around 1.225 kg/m^3 in average atmospheric conditions. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.225000 |
| WindVelocitySpace | Wind velocity is specified in this space. | [EChaosSoftsSimulationSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/EChaosSoftsSimulationSpace) | WorldSpace |
| WindVelocity | The fixed wind velocity [m/s] for this asset. For reference a wind gust is above 8m/s (18mph). | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Drag | The aerodynamic coefficient of drag applying on each particle. When "Outer Drag" is enabled, this acts as the "Inner Drag", i.e., drag applied when the air velocity is moving in the mesh normal direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.035000,High=1.000000,WeightMap="Drag",bImportFabricBounds=False,bBuildFabricMaps=False) |
| bEnableOuterDrag |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| OuterDrag | The aerodynamic coefficient of drag applying on each particle when the air velocity is moving against the mesh normal direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.035000,High=1.000000,WeightMap="OuterDrag",bImportFabricBounds=False,bBuildFabricMaps=False) |
| Lift | The aerodynamic coefficient of lift applying on each particle. When "Outer Lift" is enabled, this acts as the "Inner Lift", i.e., lift applied when the air velocity is moving in the mesh normal direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.035000,High=1.000000,WeightMap="Lift",bImportFabricBounds=False,bBuildFabricMaps=False) |
| bEnableOuterLift |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| OuterLift | The aerodynamic coefficient of lift applying on each particle when the air velocity is moving against the mesh normal direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.035000,High=1.000000,WeightMap="OuterLift",bImportFabricBounds=False,bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
