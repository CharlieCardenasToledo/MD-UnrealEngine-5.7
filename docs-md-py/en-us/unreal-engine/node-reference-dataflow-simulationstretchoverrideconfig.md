# SimulationStretchOverrideConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig

> Application Version: 5.7

### Description

SimulationStretchOverrideConfig (v1)
Experimental

Stretching constraint property override configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Stretching Override Config |
| Type | [FChaosClothAssetSimulationStretchOverrideConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_33) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bOverrideStretchUse3dRestLengths | Enable overriding Stretch Use 3d Rest Lengths | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bStretchUse3dRestLengths | Whether to use the 3D draped space as rest lengths, or use the 2D pattern space instead. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| OverrideStretchStiffness | Stretch stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchStiffness | Stretch stiffness override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| bApplyUniformStretchStiffnessOverride | Whether or not to apply the Stretch Stiffness Override to warp, weft, and bias stiffnesses of anisotropic springs. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| OverrideStretchStiffnessWarp | Warp stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchStiffnessWarp | Stretch stiffness warp override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideStretchStiffnessWeft | Weft stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchStiffnessWeft | Stretch stiffness weft override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideStretchStiffnessBias | Bias stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchStiffnessBias | Stretch stiffness bias override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideStretchDamping | Damping override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchDamping | Stretch damping override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideWarpScale | Warp scale override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| WarpScale | Stretch damping override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideWeftScale | Weft scale override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| WeftScale | Stretch damping override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
