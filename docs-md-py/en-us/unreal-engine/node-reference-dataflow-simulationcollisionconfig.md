# SimulationCollisionConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig

> Application Version: 5.7

### Description

SimulationCollisionConfig (v1)

Chaos Cloth Asset Simulation Collision Config Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Collision Config |
| Type | [FChaosClothAssetSimulationCollisionConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_15) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CollisionThicknessImported | The added thickness of collision shapes. | [FChaosClothAssetImportedFloatValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportedFloatVal-) | (ImportedValue=1.000000,bUseImportedValue=False) |
| FrictionCoefficientWeighted | Friction coefficient for cloth - collider interaction. Currently only Skinned Triangle Meshes use the weighted value. All other collisions only use the Low value. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.800000,High=0.800000,WeightMap="FrictionCoefficient",bImportFabricBounds=False,bBuildFabricMaps=False) |
| bEnableSimpleColliders | Enable colliding against any simple (e.g., capsules, convexes, spheres, boxes) colliders.. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUsePlanarConstraintForSimpleColliders | Use Planar Constraints for simple (e.g., capsules, convexes, spheres, boxes) colliders when doing multiple iterations. Planar constraints are cheaper than full collision detection, but less accurate. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bEnableComplexColliders | Enable colliding against any complex (e.g., SkinnedLevelSet, MLLevelSet) colliders. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUsePlanarConstraintForComplexColliders | Use Planar Constraints for complex (e.g., SkinnedLevelSet, MLLevelSet) colliders when doing multiple iterations. Planar constraints are cheaper than full collision detection, but less accurate. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bEnableSkinnedTriangleMeshCollisions | Enable colliding against any Skinned Triangle Mesh colliders. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseSelfCollisionSubstepsForSkinnedTriangleMeshes | Use 'NumSelfCollisionSubsteps' (Located on SimulationSolverConfig) to also control Skinned Triangle Mesh collision updates | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ClothCollisionThicknessImported | Thickness added to the cloth when colliding against collision shapes. Currently only Skinned Triangle Meshes use the weighted value. All other collisions only use the Low value. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=0.000000,WeightMap="ClothCollisionThickness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| ProximityStiffness | Stiffness for proximity repulsion forces (Force-based solver only). Units = kg cm/ s^2 (same as XPBD springs) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| bUseCCD | Use continuous collision detection (CCD) to prevent any missed collisions between fast moving particles and colliders. This has a negative effect on performance compared to when resolving collision without using CCD. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
