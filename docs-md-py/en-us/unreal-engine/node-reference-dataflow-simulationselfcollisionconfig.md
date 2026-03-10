# SimulationSelfCollisionConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig

> Application Version: 5.7

### Description

SimulationSelfCollisionConfig (v2)

Self-collision repulsion forces (point-face) properties configuration node.
Note that the kinematic collider has been deprecated in favor of SkinnedTriangleMesh Physics Asset bodies

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Self Collision Config |
| Type | [FChaosClothAssetSimulationSelfCollisionConfigNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_29) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseSelfCollisions | Activating this node will enable self collisions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SelfCollisionThickness | The self collision offset per side. Total thickness of cloth is 2x this value. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.500000,High=0.500000,WeightMap="SelfCollisionThickness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| SelfCollisionStiffness | The stiffness of the springs used to control self collision. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| SelfCollisionFriction | Friction coefficient for cloth - cloth interaction. | [FChaosClothAssetImportedFloatValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportedFloatVal-) | (ImportedValue=0.000000,bUseImportedValue=False) |
| SelfCollisionDisableNeighborDistance | Disabled neighbor collision ring. Collisions are disabled between vertices within this N-ring connectivity distance. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| SelfCollisionLayers | Self collision layers face int map. Generate this map using the SelectionsToIntMap node with SimFace Selections. Faces labeled with -1 will collide normally without any layering behavior. Faces labeled with any other number will keep higher layer numbers outside lower layer numbers (outside = front facing normal direction). | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="SelfCollisionLayers",bBuildFabricMaps=False) |
| SelfCollisionDisabledFaces | Sim face selection set of faces which should not self collide | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="SelfCollisionDisabledFaces",bBuildFabricMaps=False) |
| bUseSelfIntersections | Enable self intersection resolution. This will try to fix any cloth intersections that are not handled by collision repulsions. Can be expensive. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseGlobalIntersectionAnalysis | Do global intersection analysis to determine the correct normals for the collision springs | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseContourMinimization | Do a step of contour minimization at the beginning of the timestep. Contour minimization will attempt to resolve intersections by shortening the intersection edge. Helpful with open intersections that global intersection analysis can't fix. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| NumContourMinimizationPostSteps | Number of post timestep contour minimization steps to do. (Very Expensive!) Contour minimization will attempt to resolve intersections by shortening the intersection edge.Helpful with open intersections that global intersection analysis can't fix. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bUseGlobalPostStepContours | Use global contour gradients when doing post timestep contour minimization | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
