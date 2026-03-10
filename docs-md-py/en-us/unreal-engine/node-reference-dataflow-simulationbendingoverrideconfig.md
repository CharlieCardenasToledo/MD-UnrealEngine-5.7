# SimulationBendingOverrideConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingOverrideConfig

> Application Version: 5.7

### Description

SimulationBendingOverrideConfig (v1)
Experimental

Bending constraint property override configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Bending Override Config |
| Type | [FChaosClothAssetSimulationBendingOverrideConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_10) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OverrideFlatnessRatio | Flatness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| FlatnessRatio | Flatness override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideBendingStiffness | Bending stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BendingStiffness | Bending stiffness override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| bApplyUniformBendingStiffnessOverride | Whether or not to apply the Bending Stiffness Override to warp, weft, and bias stiffnesses of anisotropic bending elements. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bApplyBendingStiffnessOverrideToBuckling | Whether or not to apply the Bending Stiffness Override to buckling stiffnesses. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| OverrideBucklingRatio | Buckling ratio override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BucklingRatio | Buckling ratio override value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| OverrideBucklingStiffness | Buckling stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BucklingStiffness | Buckling stiffness override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| bApplyUniformBucklingStiffnessOverride | Whether or not to apply the Buckling Stiffness Override to warp, weft, and bias stiffnesses of anisotropic bending elements. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| OverrideBendingStiffnessWarp | Warp stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BendingStiffnessWarp | Bending stiffness warp override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideBendingStiffnessWeft | Weft stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BendingStiffnessWeft | Bending stiffness weft override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideBendingStiffnessBias | Bias stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BendingStiffnessBias | Bending stiffness bias override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideBucklingStiffnessWarp | Warp buckling stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BucklingStiffnessWarp | Buckling stiffness warp override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideBucklingStiffnessWeft | Weft buckling stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BucklingStiffnessWeft | Buckling stiffness Weft override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideBucklingStiffnessBias | Bias buckling stiffness override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BucklingStiffnessBias | Buckling stiffness Bias override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideBendingDamping | Damping override type. | [EChaosClothAssetConstraintOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| BendingDamping | Bending damping override value. | [FChaosClothAssetWeightedValueOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
