# SimulationDampingConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationDampingConfig

> Application Version: 5.7

### Description

SimulationDampingConfig (v1)

Damping properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Damping Config |
| Type | [FChaosClothAssetSimulationDampingConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_16) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DampingCoefficientWeighted | The amount of global damping applied to the cloth velocities, also known as point damping. Point damping improves simulation stability, but can also cause an overall slow-down effect and therefore is best left to very small percentage amounts. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.010000,High=0.010000,WeightMap="DampingCoefficient",bImportFabricBounds=False,bBuildFabricMaps=False) |
| LocalDampingSpace | The space in which local damping is calculated. Center of mass adds the expense of calculating the center of mass. | [EChaosSoftsLocalDampingSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/EChaosSoftsLocalDampingSpace) | CenterOfMass |
| LocalDampingLinearCoefficient | The amount of local linear damping applied to the cloth velocities. This type of damping only damps individual deviations of the particles velocities from the global linear motion. It makes the cloth deformations more cohesive and reduces jitter without affecting the overall movement. It can also produce synchronization artifacts where part of the cloth mesh are disconnected (which might well be desirable, or not). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| LocalDampingAngularCoefficient | The amount of local angular damping applied to the cloth velocities. This type of damping only damps individual deviations of the particles velocities from the global angular motion. It makes the cloth deformations more cohesive and reduces jitter without affecting the overall movement. It can also produce synchronization artifacts where part of the cloth mesh are disconnected (which might well be desirable, or not). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
