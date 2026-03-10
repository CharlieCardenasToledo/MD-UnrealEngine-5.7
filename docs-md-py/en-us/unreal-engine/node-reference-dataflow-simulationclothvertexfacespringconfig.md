# SimulationClothVertexFaceSpringConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexFaceSpringConfig

> Application Version: 5.7

### Description

SimulationClothVertexFaceSpringConfig (v1)
Experimental

Node for creating vertex-face constraints and setting their simulation properties.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Vertex Face Spring |
| Type | [FChaosClothAssetSimulationClothVertexFaceSpringConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_11) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAppendToExisting | Append to existing set of constraints. Stiffnesses inherited from existing constraints. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bUseTetRepulsionConstraints | Treat as tetrahedral repulsion constraints (e.g., for self collisions) rather than spring constraints | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| VertexFaceSpringExtensionStiffness | Extension Stiffness is the spring stiffness applied when the spring is currently longer than its rest length. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000) |
| VertexFaceSpringCompressionStiffness | Compression Stiffness is the spring stiffness applied when the spring is currently shorter than its rest length. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000) |
| VertexFaceSpringDamping | This damping is the relative to critical damping. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| VertexFaceRepulsionStiffness | Stiffness for repulsion constraints | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| VertexFaceMaxRepulsionIters | Max Number of iterations to apply (per solver iteration). Helps resolve more collisions, but at additional compute cost. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| ConstructionSets | Construction data for procedurally generating constraints. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) | (()) |
| bUseThicknessMap | Use Thickness rather than current rest collection state to determine rest lengths. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Thickness | Thickness for calculating rest lengths. Rest length will be combined value of thickness on both end points. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=False,Low=0.500000,High=0.500000,WeightMap="SpringThickness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| RestLengthScale | Scale applied to the rest lengths of the springs. A value of 1 will preserve the distance in the rest collection. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| GenerateConstraints | Click on this button to generate constraints from the construction data. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
