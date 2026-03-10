# SimulationDefaultConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationDefaultConfig

> Application Version: 5.7

### Description

SimulationDefaultConfig (v1)

Add default simulation properties to the cloth collection in the format of the skeletal mesh cloth editor.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Default Config |
| Type | [FChaosClothAssetSimulationDefaultConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_17) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationConfig | Cloth Simulation Properties. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosClothConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosCloth/UChaosClothConfig)> | /Script/ChaosCloth.ChaosClothConfig'/Engine/Transient.ChaosClothConfig\_0' |
| SharedSimulationConfig | Cloth Shared Simulation Properties. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosClothSharedSimConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosCloth/UChaosClothSharedSimConfig)> | /Script/ChaosCloth.ChaosClothSharedSimConfig'/Engine/Transient.ChaosClothSharedSimConfig\_0' |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
