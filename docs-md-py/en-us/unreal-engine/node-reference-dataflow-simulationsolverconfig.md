# SimulationSolverConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig

> Application Version: 5.7

### Description

SimulationSolverConfig (v1)

Solver properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Solver Config |
| Type | [FChaosClothAssetSimulationSolverConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_31) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumIterations | The number of time step dependent solver iterations. This sets iterations at 60fps. NumIterations can never be bigger than MaxNumIterations. At lower fps up to MaxNumIterations may be used instead. At higher fps as low as one single iteration might be used. Higher number of iterations will increase the stiffness of all constraints and improve convergence, but will also increase the CPU cost of the simulation. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| MaxNumIterations | The maximum number of solver iterations. This is the upper limit of the number of iterations set in solver, when the frame rate is lower than 60fps. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 6 |
| NumSubstepsImported | The number of solver substeps. This will increase the precision of the collision inputs and help with constraint resolutions but will increase the CPU cost. | [FChaosClothAssetImportedIntValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportedIntValue) | (ImportedValue=1,bUseImportedValue=False) |
| bEnableDynamicSubstepping | Enable dynamic substepping. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DynamicSubstepDeltaTime | Choose the number of substeps based on a target substep delta time in milliseconds. Substeps are clamped to [1, NumSubsteps]. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 16.670000 |
| bEnableNumSelfCollisionSubsteps | Enable setting separate SelfCollisionSubsteps. Otherwise, self collisions will be detected every substep. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| NumSelfCollisionSubsteps | Set a separate number of self collision substeps. Lower this number to increase speed at the expense of lower self collision accuracy. Actual value always clamped between [1, NumSubsteps]. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
