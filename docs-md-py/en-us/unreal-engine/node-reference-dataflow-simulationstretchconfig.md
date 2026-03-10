# SimulationStretchConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchConfig

> Application Version: 5.7

### Description

SimulationStretchConfig (v1)

Stretching constraint property configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Stretching Config |
| Type | [FChaosClothAssetSimulationStretchConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_32) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bStretchUse3dRestLengths | Whether to use the 3D draped space as rest lengths, or use the 2D pattern space instead. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SolverType | Constraint solver type. | [EChaosClothAssetConstraintSolverType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintSolver-) | PBD |
| DistributionType | Constraint distribution type. | [EChaosClothAssetConstraintDistributionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_3) | Isotropic |
| bAddAreaConstraint | Add an area constraint in case of isotropic distribution | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| StretchStiffnessWarp | The stiffness of the stretch constraints in the warp (vertical) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="StretchStiffnessWarp",bImportFabricBounds=False,bBuildFabricMaps=False) |
| StretchStiffnessWeft | The stiffness of the stretch constraints in the weft (horizontal) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="StretchStiffnessWeft",bImportFabricBounds=False,bBuildFabricMaps=False) |
| StretchStiffnessBias | The stiffness of the stretch constraints in the bias (diagonal) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="StretchStiffnessBias",bImportFabricBounds=False,bBuildFabricMaps=False) |
| StretchAnisoDamping | The damping of the stretch anisotropic constraints, relative to critical damping. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="StretchAnisoDamping",bImportFabricBounds=False,bBuildFabricMaps=False) |
| StretchStiffness | The stiffness of the stretch constraints. Note that PBD stiffnesses will be internally clamped to [0,1]. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="StretchStiffness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| StretchDamping | The damping of the stretch constraints, relative to critical damping. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="StretchDamping",bImportFabricBounds=False,bBuildFabricMaps=False) |
| bEnableStretchWarpAndWeftScale | Enable StretchWarp and WeftScale. This adds a small amount of memory and computational cost, so this is optional for the least expensive constraint type (PBD) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| StretchWarpScale | The scale of the stretch constraints at rest in the warp (vertical) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="StretchWarpScale",bImportFabricBounds=False,bBuildFabricMaps=False) |
| StretchWeftScale | The scale of the stretch constraints at rest in the weft (horizontal) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="StretchWeftScale",bImportFabricBounds=False,bBuildFabricMaps=False) |
| AreaStiffness | The stiffness of the surface area preservation constraints. Note that PBD stiffnesses will be internally clamped to [0,1]. Increase the solver iteration count for stiffer materials. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="AreaStiffness",bImportFabricBounds=False,bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
