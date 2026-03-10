# Unidad 20

Rango: archivos 2281 a 2400 de 3470

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-sign.md

# Sign

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Sign

> Application Version: 5.7

### Description

Sign (v1)

return -1, 0, +1 whether the input is respectively negative, zero or positive ( Sign(A) )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Minus Plus Positive Negative |
| Type | [FDataflowMathSignNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathSignNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simaccessorymeshnode.md

# SimAccessoryMeshNode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimAccessoryMeshNode

> Application Version: 5.7

### Description

SimAccessoryMeshNode (v1)

Add a SimAccessoryMesh by converting a cloth collection into an accessory mesh and attaching it to an existing cloth collection. Any unmatched vertices will use the existing cloth collection's sim mesh data to populate the accessory mesh data

Output(s):
AccessoryMeshName - Name of the new accessory mesh

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Sim Accessory Mesh |
| Type | FChaosClothAssetSimAccessoryMeshNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseSimImportVertexID | Use SimImportVertexID (e.g., imported vertex ID from an FBX->SKM->ClothCollection conversion) to match vertices | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SimAccessoryMeshCollection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| AccessoryMeshName | Name of the new accessory mesh | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simplifyconvexhulls.md

# SimplifyConvexHulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimplifyConvexHulls

> Application Version: 5.7

### Description

SimplifyConvexHulls (v1)

Simplify Convex Hulls Dataflow Node

Input(s) :
OptionalSelectionFilter - Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed.
SimplificationAngleThreshold - Simplified hull should preserve angles larger than this (in degrees). Used by the AngleTolerance simplification method.
SimplificationDistanceThreshold - Simplified hull should stay within this distance of the initial convex hull. Used by the MeshQSlim simplification method.
MinTargetTriangleCount - The minimum number of faces to use for the convex hull. For MeshQSlim simplification, this is a triangle count, which may be further reduced on conversion back to a convex hull.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FSimplifyConvexHullsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSimplifyConvexHullsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimplifyMethod |  | [EConvexHullSimplifyMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EConvexHullSimplifyMethod) | MeshQSlim |
| bUseExistingVertices | Whether to restrict the simplified hulls to only use vertices from the original hulls. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OptionalSelectionFilter | Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| SimplificationAngleThreshold | Simplified hull should preserve angles larger than this (in degrees). Used by the AngleTolerance simplification method. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| SimplificationDistanceThreshold | Simplified hull should stay within this distance of the initial convex hull. Used by the MeshQSlim simplification method. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MinTargetTriangleCount | The minimum number of faces to use for the convex hull. For MeshQSlim simplification, this is a triangle count, which may be further reduced on conversion back to a convex hull. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationaerodynamicsconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationanimdriveconfig.md

# SimulationAnimDriveConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAnimDriveConfig

> Application Version: 5.7

### Description

SimulationAnimDriveConfig (v1)

Anim drive properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation AnimDrive Config |
| Type | [FChaosClothAssetSimulationAnimDriveConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_7) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AnimDriveStiffness | The strength of the constraint driving the cloth towards the animated skinned/goal mesh. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=1.000000,WeightMap="AnimDriveStiffness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| AnimDriveDamping | The damping amount of the anim drive. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=1.000000,WeightMap="AnimDriveDamping",bImportFabricBounds=False,bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationbackstopconfig.md

# SimulationBackstopConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBackstopConfig

> Application Version: 5.7

### Description

SimulationBackstopConfig (v1)

Backstop properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Backstop Config |
| Type | [FChaosClothAssetSimulationBackstopConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_8) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BackstopDistance | The distance from the surface of a backstop collision sphere to its associated particle's skinned position along the mesh normal. Can be positive or negative depending on the desired effect. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=100.000000,WeightMap="BackstopDistance",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BackstopRadius | The radius of the backstop sphere that each particle collides with. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=100.000000,WeightMap="BackstopRadius",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BackstopMeshName | The name of the accessory mesh to use as the backstop mesh. If none is specified, the default animated mesh will be used | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationbendingconfig.md

# SimulationBendingConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig

> Application Version: 5.7

### Description

SimulationBendingConfig (v1)

Bending constraint property configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Bending Config |
| Type | [FChaosClothAssetSimulationBendingConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_9) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RestAngleType | Method for calculating the rest angles of the constraints. | [EChaosClothAssetRestAngleConstructionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_2) | Use3DRestAngles |
| FlatnessRatio | Calculate rest angles as a ratio between completely flat and whatever is the 3D rest angle. When FlatnessRatio = 0, this is equivalent to "Use3DRestAngles". When FlatnessRatio = 1, the rest angle will be 0 (completely flat). If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=0.000000,High=0.000000,WeightMap="FlatnessRatio",bImportFabricBounds=False,bBuildFabricMaps=False) |
| RestAngle | Set rest angles to be the explicit value set here (in degrees). 0 = Flat, Positive values fold away from the edge normal, Negative values fold toward the edge normal. When converting vertex weight values to edge values, the value with the smallest absolute value is selected. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=0.000000,High=0.000000,WeightMap="RestAngle",bImportFabricBounds=False,bBuildFabricMaps=False) |
| SolverType | Constraint solver type | [EChaosClothAssetConstraintSolverType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintSolver-) | PBD |
| DistributionType | Constraint distribution type | [EChaosClothAssetConstraintDistributionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_3) | Isotropic |
| ConstraintType | Constraint method type | [EChaosClothAssetBendingConstraintType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetBendingConstrain-) | HingeAngles |
| BendingStiffnessWarp | The stiffness of the bending constraints in the warp (vertical) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="BendingStiffnessWarp",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingStiffnessWeft | The stiffness of the bending constraints in the weft (horizontal) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="BendingStiffnessWeft",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingStiffnessBias | The stiffness of the bending constraints in the bias (diagonal) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="BendingStiffnessBias",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingAnisoDamping | The damping of the bending anisotropic constraints, relative to critical damping. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="BendingAnisoDamping",bImportFabricBounds=False,bBuildFabricMaps=False) |
| AnisoBucklingRatio | Once the element has bent such that it's folded more than this ratio from its rest angle ("buckled"), switch to using Buckling Stiffness instead of BendingElement Stiffness. When Buckling Ratio = 0, the Buckling Stiffness will never be used. When BucklingRatio = 1, the Buckling Stiffness will be used as soon as it's bent past its rest configuration. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.500000,High=0.500000,WeightMap="BucklingRatio",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingStiffnessWarp | The stiffness after buckling in the warp (vertical) direction. The constraint will use this stiffness instead of element Stiffness once the cloth has buckled, i.e., bent beyond a certain angle. Typically, Buckling Stiffness is set to be less than BendingElement Stiffness. Buckling Ratio determines the switch point between using BendingElement Stiffness and Buckling Stiffness. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=50.000000,High=50.000000,WeightMap="BucklingStiffnessWarp",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingStiffnessWeft | The stiffness after buckling in the weft (horizontal) direction. The constraint will use this stiffness instead of element Stiffness once the cloth has buckled, i.e., bent beyond a certain angle. Typically, Buckling Stiffness is set to be less than BendingElement Stiffness. Buckling Ratio determines the switch point between using BendingElement Stiffness and Buckling Stiffness. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=50.000000,High=50.000000,WeightMap="BucklingStiffnessWeft",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingStiffnessBias | The stiffness after buckling in the bias (diagonal) direction. The constraint will use this stiffness instead of element Stiffness once the cloth has buckled, i.e., bent beyond a certain angle. Typically, Buckling Stiffness is set to be less than BendingElement Stiffness. Buckling Ratio determines the switch point between using BendingElement Stiffness and Buckling Stiffness. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=50.000000,High=50.000000,WeightMap="BucklingStiffnessBias",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingStiffness | The Stiffness of the bending constraints. Increase the iteration count for stiffer materials. Note that PBD stiffnesses will be internally clamped to [0,1]. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="BendingStiffness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingDamping | The damping of the bending constraints, relative to critical damping. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="BendingDamping",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingStiffness | The stiffness after buckling. The constraint will use this stiffness instead of bending Stiffness once the cloth has buckled, i.e., bent beyond a certain angle. Typically, Buckling Stiffness is set to be less than Bending Stiffness. Note that PBD stiffnesses will be internally clamped to [0,1]. Buckling Ratio determines the switch point between using BendingElement Stiffness and Buckling Stiffness. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.900000,High=0.900000,WeightMap="BucklingStiffness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingRatioWeighted | Once the element has bent such that it's folded more than this ratio from its rest angle ("buckled"), switch to using Buckling Stiffness instead of BendingElement Stiffness. When Buckling Ratio = 0, the Buckling Stiffness will never be used. When BucklingRatio = 1, the Buckling Stiffness will be used as soon as it's bent past its rest configuration. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.500000,High=0.500000,WeightMap="BucklingRatio",bImportFabricBounds=False,bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationbendingoverrideconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationclothvertexfacespringconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationclothvertexspringconfig.md

# SimulationClothVertexSpringConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig

> Application Version: 5.7

### Description

SimulationClothVertexSpringConfig (v1)
Experimental

Node for creating vertex-vertex constraints and setting their simulation properties.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Vertex Spring |
| Type | [FChaosClothAssetSimulationClothVertexSpringConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_13) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAppendToExisting | Append to existing set of constraints. Stiffnesses inherited from existing constraints. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| VertexSpringExtensionStiffness | Extension Stiffness is the spring stiffness applied when the spring is currently longer than its rest length. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000) |
| VertexSpringCompressionStiffness | Compression Stiffness is the spring stiffness applied when the spring is currently shorter than its rest length. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000) |
| VertexSpringDamping | This damping is the relative to critical damping. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| ConstructionSets | Construction data for procedurally generating constraints. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) | (()) |
| RestLengthScale | Scale applied to the rest lengths of the springs. A value of 1 will preserve the distance in the rest collection. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| GenerateConstraints | Click on this button to generate constraints from the construction data. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ConstraintVertices | Raw constraint end point data. Modify at your own risk. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| RestLengths | Raw constraint rest length data. Modify at your own risk. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationcollisionconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationdampingconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationdefaultconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationgravityconfig.md

# SimulationGravityConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationGravityConfig

> Application Version: 5.7

### Description

SimulationGravityConfig (v1)

Gravity properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Gravity Config |
| Type | [FChaosClothAssetSimulationGravityConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_18) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseGravityOverride | Use the config gravity value instead of world gravity. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| GravityScaleWeighted | Scale factor applied to the world gravity and also to the clothing simulation interactor gravity. Does not affect the gravity if set using the override below. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="GravityScale",bImportFabricBounds=False,bBuildFabricMaps=False) |
| GravityOverrideImported | The gravitational acceleration vector [cm/s^2]. | [FChaosClothAssetImportedVectorValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportedVectorVa-) | (ImportedValue=(X=0.000000,Y=0.000000,Z=-980.664978),bUseImportedValue=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationlongrangeattachmentconfig.md

# SimulationLongRangeAttachmentConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationLongRangeAttachmentConfig

> Application Version: 5.7

### Description

SimulationLongRangeAttachmentConfig (v2)

Long range attachment constraint property configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Long Range Attachment Config |
| Type | [FChaosClothAssetSimulationLongRangeAttachmentConfigNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_19) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TetherStiffness | The tethers' stiffness of the long range attachment constraints. The long range attachment connects each of the cloth particles to its closest fixed point with a spring constraint. This can be used to compensate for a lack of stretch resistance when the iterations count is kept low for performance reasons. Can lead to an unnatural pull string puppet like behavior. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="TetherStiffness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| TetherScale | The limit scale of the long range attachment constraints (aka tether limit). If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="TetherScale",bImportFabricBounds=False,bBuildFabricMaps=False) |
| bUseGeodesicTethers | Use geodesic instead of euclidean distance calculations for the Long Range Attachment constraint, which is slower at setup but more accurate at establishing the correct position and length of the tethers, and therefore is less prone to artifacts during the simulation. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bEnableCustomTetherGeneration | Enable more granular control over tether generation via custom selection sets. Otherwise, all dynamic particles will be connect to the closest kinematic vertex as defined by FixedEndSet. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| FixedEndSet | The name of the vertex selection set used as fixed tether ends. When using custom tether generation, this set is still needed to contain all kinematic vertices. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="KinematicVertices3D",bBuildFabricMaps=False) |
| CustomTetherData | Pairs of vertex selections used for custom tether generation. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) | (()) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationmassconfig.md

# SimulationMassConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMassConfig

> Application Version: 5.7

### Description

SimulationMassConfig (v1)

Mass properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Mass Config |
| Type | [FChaosClothAssetSimulationMassConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSimulationMassCo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MassMode | How cloth particle mass is determined - Uniform Mass: Every particle's mass will be set to the value specified in the UniformMass setting. Mostly to avoid as it can cause some serious issues with irregular tessellations. - Total Mass: The total mass is distributed equally over all the particles. Useful when referencing a specific garment size and feel. - Density: A constant mass density is used. Density is usually the preferred way of setting mass since it allows matching real life materials' density values. | [EClothMassMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/ClothingSystemRuntimeCommon/EClothMassMode) | Density |
| UniformMassWeighted | The value used when the Mass Mode is set to Uniform Mass. | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=0.000150,High=0.000150,WeightMap="UniformMass",bImportFabricBounds=False,bBuildFabricMaps=False) |
| TotalMass | The value used when Mass Mode is set to TotalMass. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| DensityWeighted | Density in kg/m^2. Melton Wool: 0.7 Heavy leather: 0.6 Polyurethane: 0.5 Denim: 0.4 Light leather: 0.3 Cotton: 0.2 Silk: 0.1 | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=0.350000,High=0.350000,WeightMap="Density",bImportFabricBounds=False,bBuildFabricMaps=False) |
| MinPerParticleMass | Calculated particle masses will be clamped to this minimum value (or 1e-8, whichever is larger). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000100 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationmaxdistanceconfig.md

# SimulationMaxDistanceConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMaxDistanceConfig

> Application Version: 5.7

### Description

SimulationMaxDistanceConfig (v1)

Maximum distance constraint property configuration node.

Output(s):
KinematicVertices3D - The name of the kinematic vertex set generated by this node.
This is the union of InKinematic and any vertices which are below the solver max distance threshold.
The name of this set cannot be changed and is only provided for further tweaking.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation MaxDistance Config |
| Type | [FChaosClothAssetSimulationMaxDistanceConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_20) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaxDistance | The maximum distance a simulated particle can reach from its animated skinned cloth mesh position. If a particle has 0 for its maximum distance, it is no longer considered dynamic, and becomes kinematic to follow its animated position. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=100.000000,WeightMap="MaxDistance",bImportFabricBounds=False,bBuildFabricMaps=False) |
| InKinematic | Selection set of SimVertices3D that should be made kinematic regardless of the MaxDistance map value. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| KinematicVertices3D | The name of the kinematic vertex set generated by this node. This is the union of InKinematic and any vertices which are below the solver max distance threshold. The name of this set cannot be changed and is only provided for further tweaking. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationmorphtargetconfig.md

# SimulationMorphTargetConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMorphTargetConfig

> Application Version: 5.7

### Description

SimulationMorphTargetConfig (v1)

Simulation Morph Target configuration node. This node is necessary to set sim morph targets (e.g., via BP interactor)

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Morph Target Config |
| Type | [FChaosClothAssetSimulationMorphTargetConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_21) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ActiveMorphTarget | The name of the active sim morph target | [FChaosClothAssetMorphTargetSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetMorphTargetSelec-) | (Name="",Weight=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationmultiresconfig.md

# SimulationMultiResConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMultiResConfig

> Application Version: 5.7

### Description

SimulationMultiResConfig (v1)
Experimental

Experimental Solver multires configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation MultiRes Config |
| Type | [FChaosClothAssetSimulationMultiResConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_22) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bIsFineLOD | Enable multi-res simulation for this LOD. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bIsCoarseMultiResLOD | This LOD is a coarse LOD for a finer LOD's multi-res simulation. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MultiResCoarseLODIndex | Index of the coarse LOD for multi-res simulation. That LOD also needs a Multi Res Config node with "Is Coarse Multi Res LOD" = true. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| bMultiResUseXPBD | Use XPBD-style constraints | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MultiResStiffness | MultiRes Spring Stiffness | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="WeightMap",bImportFabricBounds=False,bBuildFabricMaps=False) |
| MultiResVelocityTargetStiffness | MultiRes Velocity Target Spring Stiffness (non-XPBD only) | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="WeightMap",bImportFabricBounds=False,bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationpressureconfig.md

# SimulationPressureConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationPressureConfig

> Application Version: 5.7

### Description

SimulationPressureConfig (v1)

Pressure properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Pressure Config |
| Type | [FChaosClothAssetSimulationPressureConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_27) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pressure | Pressure force strength applied in the normal direction(use negative value to push toward backface) If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=1.000000,WeightMap="Pressure",bImportFabricBounds=False,bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationproxiesterminal.md

# SimulationProxiesTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationProxiesTerminal

> Application Version: 5.7

### Description

SimulationProxiesTerminal (v1)

Main terminal node for simulation proxies

Input(s) :
SimulationProxies - Physics solvers to evaluate

### Information

|  |  |
| --- | --- |
| Module | [DataflowSimulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation) |
| Category | Terminal|Proxy |
| Tags | DataflowSimulationTag |
| Type | [FSimulationProxiesTerminalDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FSimulationProxiesTerminalDatafl-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationProxies | Physics solvers to evaluate | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationresolveextremedeformationconfig.md

# SimulationResolveExtremeDeformationConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationResolveExtremeDeformationConfig

> Application Version: 5.7

### Description

SimulationResolveExtremeDeformationConfig (v1)

Resolve extreme deformation properties configuration node.

Output(s):
ExtremeDeformationVertexSelection - The name of the extreme deformation vertex set generated by this node.
The name of this set cannot be changed and is only provided for further tweaking.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Resolve ExtremeDeformation Config |
| Type | [FChaosClothAssetSimulationResolveExtremeDeformationConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_28) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InputSelection | Vertex Selection to check for extreme deformations | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="InputSelection",bBuildFabricMaps=False) |
| ExtremeDeformationEdgeRatioThreshold | Edges deformed above this threshold will trigger position reset. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| ExtremeDeformationVertexSelection | The name of the extreme deformation vertex set generated by this node. The name of this set cannot be changed and is only provided for further tweaking. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationselfcollisionconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationselfcollisionspheresconfig.md

# SimulationSelfCollisionSpheresConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionSpheresConfig

> Application Version: 5.7

### Description

SimulationSelfCollisionSpheresConfig (v1)

Self-collision spheres properties configuration node.

Output(s):
SelfCollisionSphereSetName - The name of the output selection generated from the unculled vertices that receives the collision spheres.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Self Collision Spheres Config |
| Type | [FChaosClothAssetSimulationSelfCollisionSpheresConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_30) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelfCollisionSphereRadius | The radius of the spheres used in self collision centered at each vertex. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| SelfCollisionSphereStiffness | The stiffness of the springs used to control self collision. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SelfCollisionSphereRadiusCullMultiplier | Multiplier for culling the spheres generated by this node. Spheres are seeded on every vertex, and culled based on SelfCollisionSphereRadius \* SelfCollisionSphereRadiusCullMultiplier. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SelfCollisionSphereSetName | The name of the output selection generated from the unculled vertices that receives the collision spheres. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationsolverconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationstretchconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationstretchoverrideconfig.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-simulationvelocityscaleconfig.md

# SimulationVelocityScaleConfig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig

> Application Version: 5.7

### Description

SimulationVelocityScaleConfig (v1)

Velocity scale properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Velocity Scale Config |
| Type | [FChaosClothAssetSimulationVelocityScaleConfigNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_34) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VelocityScaleSpace | All vector properties on this node (e.g., Linear Velocity Scale, Max Linear Acceleration) will be evaluated in this space. | [EChaosSoftsSimulationSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/EChaosSoftsSimulationSpace) | ReferenceBoneSpace |
| LinearVelocityScale | The amount of linear velocities sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). This value will be clamped by "Max Velocity Scale". A velocity scale of > 1 will amplify the velocities from the reference bone. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.750000,Y=0.750000,Z=0.750000) |
| bEnableLinearVelocityClamping | Enable linear velocity clamping. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaxLinearVelocity | The maximum amount of linear velocity sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1000.000000,Y=1000.000000,Z=1000.000000) |
| bEnableLinearAccelerationClamping | Enable linear acceleration clamping. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaxLinearAcceleration | The maximum amount of linear acceleration sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=60000.000000,Y=60000.000000,Z=60000.000000) |
| AngularVelocityScale | The amount of angular velocities sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). This value will be clamped by "Max Velocity Scale". A velocity scale of > 1 will amplify the velocities from the reference bone. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| bEnableAngularVelocityClamping | Enable angular velocity clamping. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaxAngularVelocity | The maximum amount of angular velocity sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 200.000000 |
| bEnableAngularAccelerationClamping | Enable angular acceleration clamping. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaxAngularAcceleration | The maximum amount of angular acceleration sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 12000.000000 |
| MaxVelocityScale | Clamp on Linear and Angular Velocity Scale. The final velocity scale (e.g., including contributions from blueprints) will be clamped to this value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| FictitiousAngularScale | The portion of the angular velocity that is used to calculate the strength of all fictitious forces (e.g. centrifugal force). This parameter is only having an effect on the portion of the reference bone's angular velocity that has been removed from the simulation via the Angular Velocity Scale parameter. This means it has no effect when AngularVelocityScale is set to 1 and Angular Velocity and Acceleration clamps are disabled, in which case the cloth is simulated with full world space angular velocities and subjected to the true physical world inertial forces. Values range from 0 to 2, with 0 showing no centrifugal effect, 1 full centrifugal effect, and 2 an overdriven centrifugal effect. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-sin.md

# Sin

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Sin

> Application Version: 5.7

### Description

Sin (v1)

Sin(A) with A in radians

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Sine Trigonometry Circle Angle Degrees Radians |
| Type | [FDataflowMathSinNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathSinNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skeletalmesh.md

# SkeletalMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMesh

> Application Version: 5.7

### Description

SkeletalMesh (v1)

Get Skeletal Mesh Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | General |
| Tags | Skeletal Mesh |
| Type | [FGetSkeletalMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FGetSkeletalMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PropertyName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | SkeletalMesh |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skeletalmeshbone.md

# SkeletalMeshBone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshBone

> Application Version: 5.7

### Description

SkeletalMeshBone (v1)

Skeletal Mesh Bone Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | General |
| Tags | Skeletal Mesh |
| Type | [FSkeletalMeshBoneDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FSkeletalMeshBoneDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| PropertyName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Overrides |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndexOut |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skeletalmeshimport.md

# SkeletalMeshImport

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport

> Application Version: 5.7

### Description

SkeletalMeshImport (v2)

Import a skeletal mesh asset into the cloth collection simulation and/or render mesh containers.

Input(s) :
SkeletalMesh - The skeletal mesh to import.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Skeletal Mesh Import |
| Type | [FChaosClothAssetSkeletalMeshImportNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_42) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reimport | Reimport the imported skeletal mesh asset. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| LODIndex | The skeletal mesh LOD to import. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSingleSection | Enable single import section mode. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SectionIndex | The skeletal mesh LOD section to import. If not enabled, then all sections will be imported. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSimMesh | Whether to import the simulation mesh from the specified skeletal mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportRenderMesh | Whether to import the render mesh from the specified skeletal mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| UVChannel | UV channel of the skeletal mesh to import the 2D simulation mesh patterns from. If set to -1, or the specified UVChannel doesn't exist then the import will unwrap the 3D simulation mesh into 2D simulation mesh patterns. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| UVScale | Apply this scale to the UVs when populating Sim Mesh positions. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| bSetPhysicsAsset | Set the same physics asset as the one used by the imported skeletal mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bImportSimMorphTargets | Import morph targets as Sim Mesh Morph Targets | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh | The skeletal mesh to import. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skeletalmeshreferencetransform.md

# SkeletalMeshReferenceTransform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshReferenceTransform

> Application Version: 5.7

### Description

SkeletalMeshReferenceTransform (v1)

Skeletal Mesh Reference Transform Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | General |
| Tags | Skeletal Mesh |
| Type | [FSkeletalMeshReferenceTransformDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FSkeletalMeshReferenceTransformD-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| BoneIndexIn |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformOut |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skeletalmeshtocollection.md

# SkeletalMeshToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshToCollection

> Application Version: 5.7

### Description

SkeletalMeshToCollection (v1)

Skeletal Mesh to Collection Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FSkeletalMeshToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSkeletalMeshToCollectionDataflo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bImportTransformOnly |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skeletalmeshtomesh.md

# SkeletalMeshToMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshToMesh

> Application Version: 5.7

### Description

SkeletalMeshToMesh (v1)
Experimental

Converts a SkeletalMesh into a DynamicMesh with Imported Vertex information

Input(s) :
SkeletalMesh - SkeletalMesh to convert

Output(s):
Mesh - Output mesh
MaterialArray - Output materials

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | Mesh|Utilities |
| Type | FSkeletalMeshToMeshDataflowNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| LODLevel | Specifies the LOD level to use | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bRecordImportedVertices | Generate from the SkeletalMeshLODModel (vertex order will match SKM vertex order). Record ImportedVertices (if available) as NonManifold mapping data. This requires Editor-Only data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseMeshDescription | Generate from mesh description (vertex order will match mesh description / ImportedVertices). Requires Editor-Only data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh | SkeletalMesh to convert | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| MaterialArray | Output materials | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skeleton.md

# Skeleton

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Skeleton

> Application Version: 5.7

### Description

Skeleton (v1)

Get Skeleton Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | General |
| Tags | Skeletal Mesh |
| Type | [FGetSkeletonDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FGetSkeletonDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PropertyName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Skeleton |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Skeleton |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skeletonassetterminal.md

# SkeletonAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletonAssetTerminal

> Application Version: 5.7

### Description

SkeletonAssetTerminal (v1)

* Dataflow terminal node to save a skeleton asset

Input(s) :
SourceSkeleton - Source Skeleton used to override the skeleton asset
SkeletonAsset - Skeleton Asset to be saved

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Terminal |
| Type | [FSkeletonAssetTerminalNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FSkeletonAssetTerminalNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceSkeleton | Source Skeleton used to override the skeleton asset | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |
| SkeletonAsset | Skeleton Asset to be saved | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skinningblend.md

# SkinningBlend

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkinningBlend

> Application Version: 5.7

### Description

SkinningBlend (v1)

Initialize the RenderDeformerSkinningBlend weight map from the ProxyDeformer mapping data.

The weight map is used by the cloth render shader to decide how much to blend between skinned and simulated points.
Value ranges between 0 for fully deformed, to 1 for fully skinned.

Editing the RenderDeformerSkinningBlend is possible after this node (via a WeightMap node),
as the RenderDeformerSkinningBlend weight map is an intrinsic attribute of the ClothCollection.

Note: ProxyDeformer mapping data must exist on the input ClothCollection prior to using this node.

Output(s):
SkinningBlendName - The name of the render mesh weight map generated by this node detailing the contribution of the proxy deformer.
Value ranges between 0 (fully deformed) and 1 (fully skinned).
The name of this render mesh weight map cannot be changed and is only provided for further tweaking.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Skinning Blend |
| Type | [FChaosClothAssetSkinningBlendNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSkinningBlendNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| KinematicVertices3D | The name of a selection containing all the kinematic points. Must be of group type SimVertices2D, SimVertices3D, or SimFaces. Using an empty (or invalid) selection will make this node consider all points as dynamic. This selection is usually obtained from the MaxDistanceConfig node or built from the same weight map set to the MaxDistanceConfig node using a WeightMapToSelection node and a very low threshold. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |
| bUseSmoothTransition | Whether to create a smoothed RenderDeformerSkinningBlend weight map to ease the transition between the deformed part and the skinned part of the render mesh. When no transition is created there will be a visible step in the rendered triangles around the edge of the kinematic/dynamic transition of the proxy simulation mesh. The RenderDeformerSkinningBlend weight map is created regardless of the transition being created smooth or not, and can be later adjusted by using the WeightMap node. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SkinningBlendName | The name of the render mesh weight map generated by this node detailing the contribution of the proxy deformer. Value ranges between 0 (fully deformed) and 1 (fully skinned). The name of this render mesh weight map cannot be changed and is only provided for further tweaking. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-skinsimulationproperties.md

# SkinSimulationProperties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkinSimulationProperties

> Application Version: 5.7

### Description

SkinSimulationProperties (v1)

Set triangle mesh to simulate using skin constraints

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSkinSimulationPropertiesDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSkinSimulationPropertiesDataflo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSkinConstraints |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-slicecutter.md

# SliceCutter

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SliceCutter

> Application Version: 5.7

### Description

SliceCutter (v1)

Editor Fracture Mode / Fracture / Slice tool
Fracture with a grid of X, Y, and Z slices, with optional random variation in angle and offset.

Input(s) :
Collection [Intrinsic] - Collection to fracture
TransformSelection - The selected pieces to cut
SlicesX - Number of slices along the X axis
SlicesY - Number of slices along the Y axis
SlicesZ - Number of slices along the Z axis
SliceAngleVariation - Maximum angle (in degrees) to randomly rotate each slicing plane
SliceOffsetVariation - Maximum distance (in cm) to randomly shift each slicing plane
RandomSeed - Seed for random
ChanceToFracture - Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.
Grout - Amount of space to leave between cut pieces
Amplitude - Size of the Perlin noise displacement (in cm). If 0, no noise will be applied
Frequency - Period of the Perlin noise. Smaller values will create a smoother noise pattern
Persistence - Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor
Lacunarity - Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor
OctaveNumber - Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity
Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains
PointSpacing - Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to fracture
TransformSelection [Passthrough] - The selected pieces to cut
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FSliceCutterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSliceCutterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to fracture | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoundingBox |  | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| SlicesX | Number of slices along the X axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |
| SlicesY | Number of slices along the Y axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |
| SlicesZ | Number of slices along the Z axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| SliceAngleVariation | Maximum angle (in degrees) to randomly rotate each slicing plane | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SliceOffsetVariation | Maximum distance (in cm) to randomly shift each slicing plane | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ChanceToFracture | Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Grout | Amount of space to leave between cut pieces | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Amplitude | Size of the Perlin noise displacement (in cm). If 0, no noise will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Frequency | Period of the Perlin noise. Smaller values will create a smoother noise pattern | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| Persistence | Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Lacunarity | Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| OctaveNumber | Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| PointSpacing | Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to fracture | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-smoothcurvepoints.md

# SmoothCurvePoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SmoothCurvePoints

> Application Version: 5.7

### Description

SmoothCurvePoints (v1)
Experimental

Smooth the curves for more stable deformation

Input(s) :
Collection - Managed array collection to be used to store data
CurveSelection - Curve selection to focus the guides smoothing spatially
SmoothingFactor - Smoothing factor between 0 and 1

Output(s):
Collection [Passthrough] - Managed array collection to be used to store data

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FSmoothCurvePointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FSmoothCurvePointsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the guides smoothing spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |
| SmoothingFactor | Smoothing factor between 0 and 1 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-smoothguidescurves.md

# SmoothGuidesCurves

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SmoothGuidesCurves

> Application Version: 5.7

### Description

SmoothGuidesCurves (v1)
Experimental

Smooth the guides for more stable simulation

Input(s) :
Collection - Managed array collection to be used to store data

Output(s):
Collection [Passthrough] - Managed array collection to be used to store data

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Type | FSmoothGuidesCurvesDataflowNode |

### Inputs

| Name | Description | Type | DefaultValue |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

### Outputs

| Name | Description | Type |
| --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-spherecoveringtomesh.md

# Sphere Covering to Mesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SphereCoveringtoMesh

> Application Version: 5.7

### Description

Sphere Covering to Mesh (v1)

Convert a sphere covering, as generated by the 'protect negative space' option on the "Generate Cluster Convex Hull" nodes, to a dynamic mesh

Input(s) :
SphereCovering [Intrinsic] - The sphere covering to convert to a mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Mesh |
| Type | [FSphereCoveringToMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSphereCoveringToMeshDataflowNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VerticesAlongEachSide | Number of vertices to use along each axis when creating a mesh for each sphere | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SphereCovering | The sphere covering to convert to a mesh | [FDataflowSphereCovering](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowSphereCovering) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-spherestopoints.md

# SpheresToPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SpheresToPoints

> Application Version: 5.7

### Description

SpheresToPoints (v1)

Outputs Spheres as Points and radius values

Output(s):
Points - Centers of the spheres
Radii - Radius values

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FSpheresToPointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSpheresToPointsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spheres | Input Spheres | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Centers of the spheres | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Radii | Radius values | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-splinetolinearskinweights.md

# SplineToLinearSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SplineToLinearSkinWeights

> Application Version: 5.7

### Description

SplineToLinearSkinWeights (v1)
Experimental

Convert spline skinning data to linear data

Input(s) :
Collection - Managed array collection to be used to store datas
VertexSelection - Vertex selection to process vertices subset
SplineParamKey - Spline skinning parameter key
SplineBonesKey - Spline bones key. Used for storing root and end spline bone for each vertex.

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
BoneIndicesKey - Bone indices key to be used in other nodes if necessary
BoneWeightsKey - Bone weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FSplineToLinearSkinWeightsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FSplineToLinearSkinWeightsDatafl-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection to process vertices subset | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| SplineParamKey | Spline skinning parameter key | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SplineBonesKey | Spline bones key. Used for storing root and end spline bone for each vertex. | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-splitdataflowmesh.md

# SplitDataflowMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SplitDataflowMesh

> Application Version: 5.7

### Description

SplitDataflowMesh (v1)

Split a UDataflow mesh into a UDynamicMesh and a material array

Input(s) :
InMesh [Intrinsic] - DataflowMesh input

Output(s):
Mesh - DyanmicMesh output
MaterialArray - Materials output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FSplitDataflowMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSplitDataflowMeshDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InMesh | DataflowMesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DyanmicMesh output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| MaterialArray | Materials output | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-splitmeshislands.md

# SplitMeshIslands

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SplitMeshIslands

> Application Version: 5.7

### Description

SplitMeshIslands (v1)

Split a mesh into a connected islands

Input(s) :
Mesh [Intrinsic] - Mesh input

Output(s):
Meshes - Meshes output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FSplitMeshIslandsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSplitMeshIslandsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SplitMethod | Whether to consider coincident vertices as connected even if the topology does not connect them | [EDataflowMeshSplitIslandsMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowMeshSplitIslandsMethod) | ByMeshTopology |
| ConnectVerticesThreshold | Vertices closer than this distance are considered to be overlapping | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.001000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Meshes | Meshes output | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-square.md

# Square

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Square

> Application Version: 5.7

### Description

Square (v1)

Square ( A \* A )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Type | [FDataflowMathSquareNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathSquareNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-squareroot.md

# SquareRoot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SquareRoot

> Application Version: 5.7

### Description

SquareRoot (v1)

Square Root ( sqrt(A) )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Type | [FDataflowMathSquareRootNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathSquareRootNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-staticmesh.md

# StaticMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMesh

> Application Version: 5.7

### Description

StaticMesh (v1)

Get Static Mesh Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | General |
| Tags | Static Mesh |
| Type | [FGetStaticMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FGetStaticMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PropertyName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | StaticMesh |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StaticMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-staticmeshimport.md

# StaticMeshImport

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport

> Application Version: 5.7

### Description

StaticMeshImport (v2)

Import a static mesh asset into the cloth collection simulation and/or render mesh containers.

Input(s) :
StaticMesh - The Static Mesh to import from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Static Mesh Import |
| Type | [FChaosClothAssetStaticMeshImportNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetStaticMeshImport-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reimport | Reimport the imported static mesh asset. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| LODIndex | Which static mesh Lod to import. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSimMesh | Import static mesh data as a simulation mesh data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SimMeshSection | Material section to import as sim mesh data. Use -1 to import all sections. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| UVChannel | UV channel of the static mesh to import the 2D simulation mesh patterns from. If set to -1, or the specified UVChannel doesn't exist then the import will unwrap the 3D simulation mesh into 2D simulation mesh patterns. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| UVScale | Apply this scale to the UVs when populating Sim Mesh positions. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| bImportRenderMesh | Import static mesh data as render mesh data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| RenderMeshSection | Material section to import as render mesh data. Use -1 to import all sections. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StaticMesh | The Static Mesh to import from. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-staticmeshtocollection.md

# StaticMeshToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshToCollection

> Application Version: 5.7

### Description

StaticMeshToCollection (v2)

Create a geometry collection from a UStaticMesh

Input(s) :
StaticMesh - Asset input
MeshTransform - Transform to apply to the mesh before converting it to a collection

Output(s):
Collection - Geometry collection newly created
Materials - Material array from the static mesh
InstancedMeshes - Array of instanced meshes
RootProxyMeshes - corresponding source proxies

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FStaticMeshToCollectionDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FStaticMeshToCollectionDataflowN-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSetInternalFromMaterialIndex | Set the internal faces from material index | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bSplitComponents | Split components - when enabled, each island of the mesh will be converted to an individual transform in the collection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StaticMesh | Asset input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| MeshTransform | Transform to apply to the mesh before converting it to a collection | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Geometry collection newly created | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Materials | Material array from the static mesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | Array of instanced meshes | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |
| RootProxyMeshes | corresponding source proxies | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-staticmeshtomesh.md

# StaticMeshToMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshToMesh

> Application Version: 5.7

### Description

StaticMeshToMesh (v1)

Converts a StaticMesh into a DynamicMesh

Input(s) :
StaticMesh - StaticMesh to convert

Output(s):
Mesh - Output mesh
MaterialArray - Output materials

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FStaticMeshToMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FStaticMeshToMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseHiRes | Output the HiRes representation, if set to true and HiRes doesn't exist it will output empty mesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| LODLevel | Specifies the LOD level to use | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StaticMesh | StaticMesh to convert | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| MaterialArray | Output materials | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-stringappend.md

# StringAppend

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StringAppend

> Application Version: 5.7

### Description

StringAppend (v2)

Concatenates strings together to make a new string

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|String |
| Type | [FStringAppendDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FStringAppendDataflowNode_v2) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| String |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-subgraphcall.md

# SubGraphCall

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphCall

> Application Version: 5.7

### Description

SubGraphCall (v1)

Call a subgraph

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | SubGraph |
| Type | [FDataflowCallSubGraphNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowCallSubGraphNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubGraphName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-subgraphinput.md

# SubGraphInput

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphInput

> Application Version: 5.7

### Description

SubGraphInput (v1)

This node represent the inputs of a dataflow subgraph

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | SubGraph |
| Type | [FDataflowSubGraphInputNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowSubGraphInputNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PropertyBag |  | [FInstancedPropertyBag](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FInstancedPropertyBag) | (Value=None) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-subgraphoutput.md

# SubGraphOutput

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphOutput

> Application Version: 5.7

### Description

SubGraphOutput (v1)

This node represent the Outputs of a dataflow subgraph

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | SubGraph |
| Type | [FDataflowSubGraphOutputNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowSubGraphOutputNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PropertyBag |  | [FInstancedPropertyBag](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FInstancedPropertyBag) | (Value=None) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-subtract.md

# Subtract

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Subtract

> Application Version: 5.7

### Description

Subtract (v1)

Subtraction (A - B)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | - Subtraction Minus |
| Type | [FDataflowMathSubtractNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathSubtractNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| B |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-subtractvector.md

# SubtractVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SubtractVector

> Application Version: 5.7

### Description

SubtractVector (v1)

Subtract two vectors component wise: V = (A - B)

Input(s) :
A - A Vector operand
B - B Vector operand

Output(s):
V - Add result V=A-B

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | - Minus Subtraction |
| Type | [FDataflowVectorSubtractNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorSubtractNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Add result V=A-B | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-sumscalarfield.md

# SumScalarField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SumScalarField

> Application Version: 5.7

### Description

SumScalarField (v1)

Sum Scalar Field Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FSumScalarFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSumScalarFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Operation |  | [EDataflowFloatFieldOperationType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowFloatFieldOperationType) | Dataflow\_FloatFieldFalloffType\_Add |
| bSwapInputs |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatLeft |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemapLeft |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldFloatRight |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemapRight |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-sumvectorfield.md

# SumVectorField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SumVectorField

> Application Version: 5.7

### Description

SumVectorField (v1)

Sum Vector Field Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FSumVectorFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSumVectorFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation |  | [EDataflowVectorFieldOperationType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowVectorFieldOperationTyp-) | Dataflow\_VectorFieldFalloffType\_Add |
| bSwapVectorInputs |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloat |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldFloatRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldVectorLeft |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemapLeft |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldVectorRight |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemapRight |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldVectorResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-tan.md

# Tan

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Tan

> Application Version: 5.7

### Description

Tan (v1)

Tan(A) with A in radians

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Tangent Trigonometry Circle Angle Degrees Radians |
| Type | [FDataflowMathTanNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathTanNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-textureterminal.md

# TextureTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TextureTerminal

> Application Version: 5.7

### Description

TextureTerminal (v1)

* terminal node to a save a dependent 2D texture

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | Terminal |
| Type | [FDataflowTextureTerminalNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowTextureTerminalNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| TextureAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-texturetoimage.md

# TextureToImage

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TextureToImage

> Application Version: 5.7

### Description

TextureToImage (v1)
Experimental

Import a texture asset as an image. Texture must have CPU availability.

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | Image |
| Tags | Texture Image |
| Type | [FDataflowTextureToImageNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowTextureToImageNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TextureAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transferlinearskinweights.md

# TransferLinearSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferLinearSkinWeights

> Application Version: 5.7

### Description

TransferLinearSkinWeights (v1)
Experimental

Build the curves skinning by transferring the indices weights from a skelmesh geometry

Input(s) :
Collection - Managed array collection to be used to store datas
VertexSelection - Vertex selection to focus the geometry transfer spatially
SkeletalMesh - SkeletalMesh used to transfer the skinning weights. Will be stored onto the groom asset
LODIndex - LOD used to transfer the weights
RelativeTransform - The relative transform between the skeletal mesh and the groom asset.

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
BoneIndicesKey - Bone indices key to be used in other nodes if necessary
BoneWeightsKey - Bone weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FTransferGeometrySkinWeightsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FTransferGeometrySkinWeightsData-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection to focus the geometry transfer spatially | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| SkeletalMesh | SkeletalMesh used to transfer the skinning weights. Will be stored onto the groom asset | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| LODIndex | LOD used to transfer the weights | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| RelativeTransform | The relative transform between the skeletal mesh and the groom asset. | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transferskinweights.md

# TransferSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights

> Application Version: 5.7

### Description

TransferSkinWeights (v1)

Transfer the skinning weights set on a skeletal mesh to the simulation and/or render mesh stored in the cloth collection.

Input(s) :
SkeletalMesh - The skeletal mesh to transfer the skin weights from.
SimCollection - The collection containing the sim mesh to use when the Render Mesh Transfer Source is set to Collection/Sim Collection. When this input isn't connected, the Collection input is used instead.
LodIndex - The skeletal mesh LOD to transfer the skin weights from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Transfer Skin Weights |
| Type | [FChaosClothAssetTransferSkinWeightsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetTransferSkinWeig-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMeshType | The type of cloth mesh the skeletal mesh transfer will be applied to, simulation, render mesh, or both. | [EChaosClothAssetTransferTargetMeshType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetTransferTargetMe-) | All |
| SimMeshSourceTypeHint | For the sim mesh, simulation mesh transfers always use the specified skeletal mesh. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Skeletal Mesh |
| RenderMeshSourceType | For the render mesh, choose which source to use, either the default or specified simulation mesh or the specified skeletal mesh. | [EChaosClothAssetTransferRenderMeshSource](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetTransferRenderMe-) | SimulationMesh |
| Transform | The relative transform between the skeletal mesh and the cloth asset. | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| TransferMethodHint | Algorithm used for the transfer method. When the Render Mesh Transfer Source is set to use the sim mesh from the Collection/Sim Collection input, only the ClosestPointOnSurface method is available. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Closest Point On Surface |
| TransferMethod | Algorithm used for the transfer method. Use the simple ClosestPointOnSurface method or the more complex InpaintWeights method for better results. Note: When using the simulation mesh as source for the render mesh transfer, the algorithm will always be the ClosestPointOnSurface method, whatever this setting is. | [EChaosClothAssetTransferSkinWeightsMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_4) | InpaintWeights |
| RadiusPercentage | Percentage of the bounding box diagonal of the simulation mesh to use as search radius for the InpaintWeights method. All points outside of the search radius will be ignored. When set to a negative value (e.g. -1), all points will be considered. | double | 0.050000 |
| NormalThreshold | Maximum angle difference (in degrees) between the target and source point normals to be considered a match for the InpaintWeights method. If set to a negative value (e.g. -1), normals will be ignored. | double | 30.000000 |
| LayeredMeshSupport | If true, when the closest point doesn't pass the normal threshold test, will try again with a flipped normal. This helps with layered meshes where the "inner" and "outer" layers are close to each other but whose normals are pointing in the opposite directions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| NumSmoothingIterations | The number of smoothing iterations applied to the vertices whose weights were automatically computed. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| SmoothingStrength | The smoothing strength of each smoothing iteration. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| InpaintMask | Optional mask where a non-zero value indicates that we want the skinning weights for the vertex to be computed automatically instead of it being copied over from the source mesh. | [FChaosClothAssetWeightedValueNonAnimatableNoLowHighRange](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_45) | (WeightMap="InpaintMask") |
| MaxNumInfluences | The maximum number of bones that will influence each vertex. | [EChaosClothAssetMaxNumInfluences](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetMaxNumInfluences) | Eight |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMesh | The skeletal mesh to transfer the skin weights from. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| LodIndex | The skeletal mesh LOD to transfer the skin weights from. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SimCollection | The collection containing the sim mesh to use when the Render Mesh Transfer Source is set to Collection/Sim Collection. When this input isn't connected, the Collection input is used instead. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transfervertexattribute.md

# TransferVertexAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexAttribute

> Application Version: 5.7

### Description

TransferVertexAttribute (v1)

Transfer float properties from a source collection to a target collection.
Component Transfer is used when all geometries from the source collection have matched names with the target collection.
Otherwise, Global Transfer is used.
Geometries are matched when the geometry's BoneName can be found as the start of the BoneName of a geometry in the target collection.
Use TransformNameSuffix to add extra string to the source geometry's BoneName to avoid multiple matched names.
For example, source geometry has name SK\_10 and target geometry has name SK\_10\_tet1
For all names, Check BoneName attribute in Transform group in the collection.

Input(s) :
Collection - Target collection to transfer vertex attribute to.
FromCollection - Source collection to transfer vertex attribute from.
AttributeKey - The name of the vertex attribute to generate indices from.

Output(s):
Collection [Passthrough] - Target collection to transfer vertex attribute to.
AttributeKey [Passthrough] - The name of the vertex attribute to generate indices from.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Tags | Transfer a named vertex attribute from the Source Collection to the Target Collection |
| Type | [FGeometryCollectionTransferVertexAttributeNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-_2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransferMethod | Transfer method [default: Paired Geometry Transfer] | [EDataflowTransferVertexAttributeNodeTransferMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-_2) | Global |
| BoundingVolumeType | Bounding volume type for source assets[default: Triangle] | [EDataflowTransferVertexAttributeNodeBoundingVolume](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-_1) | Triangle |
| SourceScale | Bounding volume hierarchy cell size for neighboring vertices to transfer into[default: Asset] | [EDataflowTransferVertexAttributeNodeSourceScale](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-) | Asset\_Bound |
| Falloff | Falloff of source value based on distance from source triangle[default: Squared] | [EDataflowTransferVertexAttributeNodeFalloff](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransferVertexAttribute-) | None |
| FalloffThreshold | Threshold based on distance from source triangle.Values past the threshold will falloff.[Defaults to 1 percent of triangle size(0.01)] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| EdgeMultiplier | Edge multiplier for the Bounding Volume Hierarchy(BVH) target's particle search radius. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| BoundMultiplier | Max bound multiplier for the Bounding Volume Hierarchy(BVH) target's particle search radius. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| TransformNameSuffix | Suffix of transform names added to the source geometry's BoneName for geometry matching during transfer[default: \_Tet]. In CreateTetrahedron node we add \_Tet to tetrahedral geometries. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | \_Tet |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target collection to transfer vertex attribute to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FromCollection | Source collection to transfer vertex attribute from. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey | The name of the vertex attribute to generate indices from. | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="Vertices") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target collection to transfer vertex attribute to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| AttributeKey | The name of the vertex attribute to generate indices from. | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transfervertexskinweights.md

# TransferVertexSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights

> Application Version: 5.7

### Description

TransferVertexSkinWeights (v1)

Transfer skin weights from a source collection to a target collection.
Component Transfer is used when all geometries from the source collection have matched names with the target collection.
Otherwise, Global Transfer is used.
Geometries are matched when the geometry's BoneName can be found as the start of the BoneName of a geometry in the target collection.
Use TransformNameSuffix to add extra string to the source geometry's BoneName to avoid multiple matched names.
For example, source geometry has name SK\_10 and target geometry has name SK\_10\_tet1
For all names, Check BoneName attribute in Transform group in the collection.

Input(s) :
Collection - Target collection to transfer vertex attribute to.
FromCollection - Source collection to transfer vertex attribute from.

Output(s):
Collection [Passthrough] - Target collection to transfer vertex attribute to.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Tags | Transfer vertex skin weights from the Source Collection to the Target Collection |
| Type | [FGeometryCollectionTransferVertexSkinWeightsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-_3) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransferMethod | Transfer method [default: Paired Geometry Transfer] | [EDataflowTransferVertexAttributeNodeTransferMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-_2) | Global |
| BoundingVolumeType | Bounding volume type for source assets[default: Triangle] | [EDataflowTransferVertexAttributeNodeBoundingVolume](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-_1) | Triangle |
| SourceScale | Bounding volume hierarchy cell size for neighboring vertices to transfer into[default: Asset] | [EDataflowTransferVertexAttributeNodeSourceScale](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-) | Asset\_Bound |
| Falloff | Falloff of source value based on distance from source triangle[default: Squared] | [EDataflowTransferVertexAttributeNodeFalloff](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransferVertexAttribute-) | None |
| FalloffThreshold | Threshold based on distance from source triangle.Values past the threshold will falloff.[Defaults to 1 percent of triangle size(0.01)] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| EdgeMultiplier | Edge multiplier for the Bounding Volume Hierarchy(BVH) target's particle search radius. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| BoundMultiplier | Max bound multiplier for the Bounding Volume Hierarchy(BVH) target's particle search radius. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| TransformNameSuffix | Suffix of transform names for geometry matching during transfer[default: \_Tet]. In CreateTetrahedron node we add \_Tet to tetrahedral geometries. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | \_Tet |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target collection to transfer vertex attribute to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FromCollection | Source collection to transfer vertex attribute from. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target collection to transfer vertex attribute to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transformcollection.md

# TransformCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformCollection

> Application Version: 5.7

### Description

TransformCollection (v1)

Transforms a Collection

Input(s) :
Collection [Intrinsic] - Output mesh
TransformSelection - Transform selection for transforming
Translate - Translation
Rotate - Rotation
Scale - Scale

Output(s):
Collection [Passthrough] - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Transform |
| Type | [FTransformCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FTransformCollectionDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RotationOrder | Rotation Order | [ERotationOrderEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERotationOrderEnum) | Dataflow\_RotationOrder\_XYZ |
| UniformScale | Uniform scale | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RotatePivot | Pivot for the rotation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ScalePivot | Pivot for the scale | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bInvertTransformation | Invert the transformation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Output mesh | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Transform selection for transforming | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Translate | Translation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Rotate | Rotation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Scale | Scale | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| RotationOrder | Rotation Order | [ERotationOrderEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERotationOrderEnum) | Dataflow\_RotationOrder\_XYZ |
| UniformScale | Uniform scale | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RotatePivot | Pivot for the rotation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ScalePivot | Pivot for the scale | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bInvertTransformation | Invert the transformation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Output mesh | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transformcollectionattribute.md

# TransformCollectionAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformCollectionAttribute

> Application Version: 5.7

### Description

TransformCollectionAttribute (v1)

Transform Collection Attribute Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FTransformCollectionAttributeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FTransformCollectionAttributeDat-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| LocalTransform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| GroupName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Vertices |
| AttributeName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Vertex |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformIn |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transformmesh.md

# TransformMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformMesh

> Application Version: 5.7

### Description

TransformMesh (v1)

Transforms a mesh

Input(s) :
Mesh [Intrinsic] - Output mesh
Translate - Translation
Rotate - Rotation
Scale - Scale
UniformScale - Uniform scale
ScalePivot - Pivot for the scale
bInvertTransformation - Invert the transformation

Output(s):
Mesh [Passthrough] - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Transform |
| Type | [FTransformMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FTransformMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RotationOrder | Rotation Order | [ERotationOrderEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERotationOrderEnum) | Dataflow\_RotationOrder\_XYZ |
| RotatePivot | Pivot for the rotation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| Translate | Translation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Rotate | Rotation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Scale | Scale | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| UniformScale | Uniform scale | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RotatePivot | Pivot for the rotation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ScalePivot | Pivot for the scale | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bInvertTransformation | Invert the transformation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transformpoints.md

# TransformPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPoints

> Application Version: 5.7

### Description

TransformPoints (v1)

Transform an array of points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FTransformPointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FTransformPointsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Transform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transformpositions.md

# TransformPositions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions

> Application Version: 5.7

### Description

TransformPositions (v1)

Chaos Cloth Asset Transform Positions Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Transform Positions |
| Type | [FChaosClothAssetTransformPositionsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetTransformPositio-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bTransform2DSimPositions | Enable Transforming 2D Sim Mesh Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Sim2DScale | 2D Sim Transform scale. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| Sim2DRotation | 2D Sim Transform rotation angle in degrees. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Sim2DTranslation | 2D Sim Transform translation. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| Sim2DPattern | Sim Pattern to transform. All patterns will be used when set to -1. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| bTransform3DSimPositions | Enable Transforming 3D Sim Mesh Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Sim3DScale | 3D Sim Transform scale. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Sim3DRotation | 3D Sim Transform rotation angle in degrees (Euler Angles) | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Sim3DTranslation | 3D Sim Transform translation. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bTransformRenderPositions | Enable Transforming Render Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderScale | Render Transform scale. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| RenderRotation | Render Transform rotation angle in degrees (Euler Angles) | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RenderTranslation | Render Transform translation. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RenderPattern | Render Pattern to transform. All patterns will be used when set to -1. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-transformuvs.md

# TransformUVs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformUVs

> Application Version: 5.7

### Description

TransformUVs (v1)

Chaos Cloth Asset Transform UVs Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Transform UV |
| Type | [FChaosClothAssetTransformUVsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetTransformUVsNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Scale | Transform scale. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| Rotation | Transform rotation angle in degrees. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Translation | Transform translation. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| Pattern | Pattern to transform. All patterns will be used when set to -1. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| UVChannel | UV channel to transform. All UV channels will be used when set to -1. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-triangleboundaryindices.md

# TriangleBoundaryIndices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TriangleBoundaryIndices

> Application Version: 5.7

### Description

TriangleBoundaryIndices (v1)
Experimental

Outputs boundary nodes of a triangle mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Flesh|Experimental |
| Type | [FTriangleBoundaryIndicesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FTriangleBoundaryIndicesNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundaryIndicesOut |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-trianglemeshsimulationproperties.md

# TriangleMeshSimulationProperties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TriangleMeshSimulationProperties

> Application Version: 5.7

### Description

TriangleMeshSimulationProperties (v1)

Convert tetmesh to simulate using surface traingle mesh only

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FTriangleMeshSimulationPropertiesDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FTriangleMeshSimulationPropertie-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshNames |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| TriangleMeshDensity |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| VertexTriangleMeshStiffness |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000000.000000 |
| VertexTriangleMeshDamping |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-trunc.md

# Trunc

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Trunc

> Application Version: 5.7

### Description

Trunc (v1)

Trunc ( 1.4 => 1.0 | 1.9 => 1.0 | -5.3 => -5.0)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Integer Truncate |
| Type | [FDataflowMathTruncNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathTruncNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uncluster.md

# Uncluster

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Uncluster

> Application Version: 5.7

### Description

Uncluster (v1)

Uncluster selected nodes

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to uncluster
TransformSelection - Bone selection

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to uncluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterUnclusterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterUnclusterDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to uncluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to uncluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uniformfracture.md

# UniformFracture

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformFracture

> Application Version: 5.7

### Description

UniformFracture (v1)

Editor Fracture Mode / Fracture / Uniform tool
Fracture using a Voronoi diagram with a uniform random pattern, creating fracture pieces of similar volume across the shape.

Input(s) :
Collection [Intrinsic] - Collection to fracture
TransformSelection - Bones to fracture, if not connected it will fracture all the bones
Transform - Transform to apply
MinVoronoiSites - Minimum Number of Voronoi sites. The amount of sites per Voronoi diagram will be chosen at random between Min and Max
MaxVoronoiSites - Maximum Number of Voronoi sites. The amount of sites per Voronoi diagram will be chosen at random between Min and Max
InternalMaterialID - ID for the material for the newly created internal faces
RandomSeed - Random number generator seed for repeatability. If the value is -1, a different random seed will be used every time, otherwise the specified seed will always be used
ChanceToFracture - Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.
Grout - Amount of space to leave between cut pieces
Amplitude - Size of the Perlin noise displacement (in cm). If 0, no noise will be applied
Frequency - Period of the Perlin noise. Smaller values will create a smoother noise pattern
Persistence - Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor
Lacunarity - Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor
OctaveNumber - Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity
Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains
PointSpacing - Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to fracture
TransformSelection [Passthrough] - Bones to fracture, if not connected it will fracture all the bones
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FUniformFractureDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUniformFractureDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupFracture | Generate a fracture pattern across all selected meshes. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to fracture | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bones to fracture, if not connected it will fracture all the bones | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Transform | Transform to apply | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| MinVoronoiSites | Minimum Number of Voronoi sites. The amount of sites per Voronoi diagram will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| MaxVoronoiSites | Maximum Number of Voronoi sites. The amount of sites per Voronoi diagram will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| InternalMaterialID | ID for the material for the newly created internal faces | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| RandomSeed | Random number generator seed for repeatability. If the value is -1, a different random seed will be used every time, otherwise the specified seed will always be used | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ChanceToFracture | Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Grout | Amount of space to leave between cut pieces | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Amplitude | Size of the Perlin noise displacement (in cm). If 0, no noise will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Frequency | Period of the Perlin noise. Smaller values will create a smoother noise pattern | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| Persistence | Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Lacunarity | Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| OctaveNumber | Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| PointSpacing | Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to fracture | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Bones to fracture, if not connected it will fracture all the bones | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uniformintegerfield.md

# UniformIntegerField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformIntegerField

> Application Version: 5.7

### Description

UniformIntegerField (v1)

UniformInteger Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FUniformIntegerFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUniformIntegerFieldDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldIntResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uniformpointsampling.md

# UniformPointSampling

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling

> Application Version: 5.7

### Description

UniformPointSampling (v1)

Uniform Sampling on a DynamicMesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to sample points on
SamplingRadius - Desired "radius" of sample points. Spacing between samples is at least 2x this value.
MaxNumSamples - Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled
SubSampleDensity - Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results.
RandomSeed - Random Seed used to initialize sampling strategies

Output(s):
SamplePoints - Sampled positions on the mesh
SampleTriangleIDs - Sampled triangleID
SampleBarycentricCoords - Barycentric Coordinates of each Sample Point in it's respective Triangle.
NumSamplePoints - Number of Sampled positions on the mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | [FUniformPointSamplingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUniformPointSamplingDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to sample points on | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SamplingRadius | Desired "radius" of sample points. Spacing between samples is at least 2x this value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MaxNumSamples | Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SubSampleDensity | Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| RandomSeed | Random Seed used to initialize sampling strategies | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Sampled positions on the mesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleTriangleIDs | Sampled triangleID | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleBarycentricCoords | Barycentric Coordinates of each Sample Point in it's respective Triangle. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePoints | Number of Sampled positions on the mesh | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uniformscalarfield.md

# UniformScalarField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformScalarField

> Application Version: 5.7

### Description

UniformScalarField (v1)

UniformScalar Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FUniformScalarFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUniformScalarFieldDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uniformscatterpoints.md

# UniformScatterPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformScatterPoints

> Application Version: 5.7

### Description

UniformScatterPoints (v2)

Uniform Scatter Points Dataflow Node V 2

Input(s) :
MinNumberOfPoints - Minimum for the random range
MaxNumberOfPoints - Maximum for the random range
RandomSeed - Seed for random
BoundingBox - BoundingBox to generate points inside of

Output(s):
Points - Generated points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FUniformScatterPointsDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUniformScatterPointsDataflowNod-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | BoundingBox to generate points inside of | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| MinNumberOfPoints | Minimum for the random range | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| MaxNumberOfPoints | Maximum for the random range | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Generated points | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uniformvectorfield.md

# UniformVectorField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformVectorField

> Application Version: 5.7

### Description

UniformVectorField (v1)

UniformVector Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FUniformVectorFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUniformVectorFieldDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Direction |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldVectorResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-unionintarrays.md

# UnionIntArrays

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UnionIntArrays

> Application Version: 5.7

### Description

UnionIntArrays (v1)

Union Int Arrays Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities |
| Type | [FUnionIntArraysDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUnionIntArraysDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InArray1 |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InArray2 |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-updateclothfromdynamicmesh.md

# UpdateClothFromDynamicMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh

> Application Version: 5.7

### Description

UpdateClothFromDynamicMesh (v1)
Experimental

Update cloth collection attributes from a DynamicMesh

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Update Cloth Collection Dynamic Mesh Cloth |
| Type | [FChaosClothAssetUpdateClothFromDynamicMeshNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_43) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bCopyToRenderPositions | Copy DynamicMesh Vertex Positions to Render Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyToRendeNormalsAndTangents | Copy DynamicMesh Vertex Normals and Tangents to Render Normals and Tangents | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyUVsToRenderUVs | Copy DynamicMesh UVs to Render UVs | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyToRenderMaterials | Copy input materials to Render Materials (order and number must match otherwise only the minimum common number of materials are updated) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyToSim3DPositions | Copy DynamicMesh Vertex Positions to Sim3D Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyToSimNormals | Copy DynamicMesh Vertex Normals to Sim Normals | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyUVsToSim2DPositions | Copy DynamicMesh UVs to Sim2D Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| UVChannelIndex | Which UV Channel to use at Sim2D Positions or Render UVs. Use -1 to copy all Render UVs. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DynamicMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| Materials |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-updatevolumeattributes.md

# UpdateVolumeAttributes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateVolumeAttributes

> Application Version: 5.7

### Description

UpdateVolumeAttributes (v1)

Update the Volume and Size attributes on the target Collection (and add them if they were not present)

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FUpdateVolumeAttributesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUpdateVolumeAttributesDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-usdimport.md

# USDImport

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport

> Application Version: 5.7

### Description

USDImport (v2)

Import a USD file from a third party garment construction software.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth USD Import |
| Type | [FChaosClothAssetUSDImportNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetUSDImportNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bImportSimMesh | Only import the simulation mesh data from the USD file. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportRenderMesh | Only import the render mesh data from the USD file. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportWithOpacity | Importing the render mesh with opacity requires transluscency to be enable in the project settings. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| UsdFile | Path of the USD file to import. | [FChaosClothAssetImportFilePath](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportFilePath) | (FilePath="",bForceReimport=False) |
| ReimportUsdFile | Click on this button to reimport the specified USD file and regenerate the intermediary assets. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ReloadSimStaticMesh | The USD import process generates an intermediary simulation static mesh. Click on this button to reimport it without reimporting the USD file. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ReloadRenderStaticMesh | The USD import process generates an intermediary render static mesh. Click on this button to reimport it without reimporting the USD file. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| PackagePath | Content folder where all the USD assets are imported. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| ImportedSimStaticMesh | The static mesh created from the USD import process used as simulation mesh. Note that this property can still be empty after successfully importing a simulation mesh depending on whether the simulation mesh is imported from an older version of USD cloth schema. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| ImportedUVScale | The UV scale used to import the patterns from the imported static mesh UV coordinates. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| ImportedRenderStaticMesh | The static mesh created from the USD import process used as render mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| ImportedSimAssets | List of all the simulation static mesh's dependent assets. This does not include any Engine, or Engine plugin content. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| ImportedRenderAssets | List of all the render static mesh's dependent assets. This does not include any Engine, or Engine plugin content. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uvmeshtransformnode.md

# UVMeshTransformNode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UVMeshTransformNode

> Application Version: 5.7

### Description

UVMeshTransformNode (v1)
Experimental

UVMesh Transform Node

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | UV Mesh Transform |
| Type | FUVMeshTransformNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Scale |  | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| Rotation | Rotation angle in degrees | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Translation |  | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| UVChannelIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| UVChannelIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uvresizecontroller.md

# UVResizeController

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UVResizeController

> Application Version: 5.7

### Description

UVResizeController (v1)
Experimental

UV Resizing logic.
Returns whether this dynamic mesh is suitable for UV resizing and which UV channels to use.

Input(s) :
Mesh - The input/output Dataflow mesh.

Output(s):
Mesh [Passthrough] - The input/output Dataflow mesh.
UVChannelIndices - The UV channels to resize.
SourceUVChannelIndices - The matching UV channels on the original source mesh.
bHasUVChannelsToResize - Whether the input mesh has any UV channels to resize.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | UV Resize Controller |
| Type | FUVResizeControllerNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TextureSuffix | The texture name suffix . | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Texture |
| UVChannelSuffix | The suffix to replace the texture name with pointing to the UV channel index scalar parameter. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | UVIndex |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | The input/output Dataflow mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | The input/output Dataflow mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| UVChannelIndices | The UV channels to resize. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SourceUVChannelIndices | The matching UV channels on the original source mesh. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| bHasUVChannelsToResize | Whether the input mesh has any UV channels to resize. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-uvunwrapnode.md

# UVUnwrapNode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UVUnwrapNode

> Application Version: 5.7

### Description

UVUnwrapNode (v1)
Experimental

UVUnwrap Node

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | UV Unwrap |
| Type | FUVUnwrapNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Method |  | EUVUnwrapMethod | SpectralConformal |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| UVChannelIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| UVChannelIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-validategeometrycollection.md

# ValidateGeometryCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ValidateGeometryCollection

> Application Version: 5.7

### Description

ValidateGeometryCollection (v1)

Editor Fracture Mode / Utilities / Validate tool
Ensures that geometrycollection is valid and clean.

Input(s) :
Collection [Intrinsic] - Collection to use

Output(s):
Collection [Passthrough] - Collection to use

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FValidateGeometryCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FValidateGeometryCollectionDataf-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bRemoveUnreferencedGeometry | Find and remove any unused geometry data | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bRemoveClustersOfOne | Whether to collapse any clusters with only a single child | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bRemoveDanglingClusters | Remove dangling clusters -- Note this can invalidate caches | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-vectorarraynormalize.md

# VectorArrayNormalize

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorArrayNormalize

> Application Version: 5.7

### Description

VectorArrayNormalize (v1)

Normalize all the selected vectors in a VectorArray

Input(s) :
InVectorArray [Intrinsic] - Input VectorArray
Selection - Selection for the operation

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Vector |
| Type | [FVectorArrayNormalizeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVectorArrayNormalizeDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InVectorArray | Input VectorArray | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Selection | Selection for the operation | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutVectorArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-vectorcrossproduct.md

# VectorCrossProduct

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorCrossProduct

> Application Version: 5.7

### Description

VectorCrossProduct (v1)

Compute the cross product of two vectors : CrossProduct = B^A
This node only operates in 3 dimensions, inputs will be converted to a 3D vector internally and result will be a vector with a zero W component

Input(s) :
A - A Vector operand
B - B Vector operand

Output(s):
CrossProduct - Resulting cross product of A and B : CrossProduct=B^A

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Type | [FDataflowVectorCrossProductNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorCrossProductNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CrossProduct | Resulting cross product of A and B : CrossProduct=B^A | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-vectordistance.md

# VectorDistance

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorDistance

> Application Version: 5.7

### Description

VectorDistance (v1)

Compute the distance between two vectors : Distance = |B-A|

Input(s) :
A - A Vector operand
B - B Vector operand

Output(s):
Distance - Distance between A and B : Distance=|B-A|

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Type | [FDataflowVectorDistanceNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorDistanceNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |  |  |
| --- | --- | --- | --- | --- | --- |
| Distance | Distance between A and B : Distance= | B-A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-vectordotproduct.md

# VectorDotProduct

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorDotProduct

> Application Version: 5.7

### Description

VectorDotProduct (v1)

Compute the dot product between two vectors : DotProduct = A.B

Input(s) :
A - A Vector operand
B - B Vector operand

Output(s):
DotProduct - Resulting dot product : DotProduct=A.B

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Project |
| Type | [FDataflowVectorDotProductNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorDotProductNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DotProduct | Resulting dot product : DotProduct=A.B | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-vectorlength.md

# VectorLength

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorLength

> Application Version: 5.7

### Description

VectorLength (v1)

Compute the Length of a vector : Length = |V|

Input(s) :
V - Vector to get length from

Output(s):
Length - Length of the input vector : Length=|V|

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Size Magnitude |
| Type | [FDataflowVectorLengthNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorLengthNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Vector to get length from | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |  |  |
| --- | --- | --- | --- | --- | --- |
| Length | Length of the input vector : Length= | V |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-vectorsquaredlength.md

# VectorSquaredLength

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorSquaredLength

> Application Version: 5.7

### Description

VectorSquaredLength (v1)

Compute the Squared length of a vector : Length = |V||V|

Input(s) :
V - Vector to get squared length from

Output(s):
SquaredLength - Length of the input vector : SquaredLength = |V||V|

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Size Magnitude |
| Type | [FDataflowVectorSquaredLengthNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorSquaredLengthNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Vector to get squared length from | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SquaredLength | Length of the input vector : SquaredLength = | V |  | V |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-vertexscalartovertexindices.md

# VertexScalarToVertexIndices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VertexScalarToVertexIndices

> Application Version: 5.7

### Description

VertexScalarToVertexIndices (v1)

Convert an vertex float array to a list of indices

Input(s) :
AttributeKey - The name of the vertex attribute and group to generate indices from.

Output(s):
VertexIndices - Output list of indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Tags | Collection Vertex Weight Map to Indices |
| Type | [FGeometryCollectionVertexScalarToVertexIndicesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-_4) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionThreshold | The value threshold for what is included in the vertex list. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey | The name of the vertex attribute and group to generate indices from. | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="Vertices") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexIndices | Output list of indices | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-vertexweightedpointsampling.md

# VertexWeightedPointSampling

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VertexWeightedPointSampling

> Application Version: 5.7

### Description

VertexWeightedPointSampling (v1)

VertexWeighted Sampling on a DynamicMesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to sample points on
VertexWeights [Intrinsic] - Weight array
SamplingRadius - Desired "radius" of sample points. Spacing between samples is at least 2x this value.
MaxNumSamples - Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled
SubSampleDensity - Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results.
RandomSeed - Random Seed used to initialize sampling strategies
MaxSamplingRadius - If MaxSampleRadius > SampleRadius, then output sample radius will be in range [SampleRadius, MaxSampleRadius]
SizeDistributionPower - SizeDistributionPower is used to control how extreme the Size Distribution shift is. Valid range is [1,10]

Output(s):
SamplePoints - Sampled positions on the mesh
SampleRadii - Sampled radii
SampleTriangleIDs - Sampled triangleID
SampleBarycentricCoords - Barycentric Coordinates of each Sample Point in it's respective Triangle.
NumSamplePoints - Number of Sampled positions on the mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | [FVertexWeightedPointSamplingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVertexWeightedPointSamplingData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SizeDistribution | SizeDistribution setting controls the distribution of sample radii | [ENonUniformSamplingDistributionMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/ENonUniformSamplingDistributionM-) | ENonUniformSamplingDistributionMode\_Uniform |
| WeightMode |  | [ENonUniformSamplingWeightMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/ENonUniformSamplingWeightMode) | ENonUniformSamplingWeightMode\_WeightedRandom |
| bInvertWeights |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to sample points on | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| VertexWeights | Weight array | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| SamplingRadius | Desired "radius" of sample points. Spacing between samples is at least 2x this value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MaxNumSamples | Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SubSampleDensity | Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| RandomSeed | Random Seed used to initialize sampling strategies | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MaxSamplingRadius | If MaxSampleRadius > SampleRadius, then output sample radius will be in range [SampleRadius, MaxSampleRadius] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| SizeDistributionPower | SizeDistributionPower is used to control how extreme the Size Distribution shift is. Valid range is [1,10] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Sampled positions on the mesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleRadii | Sampled radii | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| SampleTriangleIDs | Sampled triangleID | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleBarycentricCoords | Barycentric Coordinates of each Sample Point in it's respective Triangle. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePoints | Number of Sampled positions on the mesh | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-visualizefiberfield.md

# VisualizeFiberField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFiberField

> Application Version: 5.7

### Description

VisualizeFiberField (v1)

Visualizes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FVisualizeFiberFieldNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FVisualizeFiberFieldNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VectorScale |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VectorField |  | [FFieldCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FFieldCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-visualizefracture.md

# VisualizeFracture

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture

> Application Version: 5.7

### Description

VisualizeFracture (v1)

Visualizing fracture/cluster info in fractured collection

Input(s) :
Collection [Intrinsic] - Collection to visualize
RandomSeed - Seed for random
ExplodeAmount - Scale amount to expand the pieces uniformly in all directions
Scale - Scale amounts to expand the pieces in all 3 directions
Offset - Translate collection for exploded view

Output(s):
Collection [Passthrough] - Collection to visualize

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FVisualizeFractureDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVisualizeFractureDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bApplyExplodedView | Use cluster level for coloring and explode | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bApplyColor |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColoringType |  | [EDataflowVisualizeFractureColoringType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowVisualizeFractureColori-) | ColorByLevel |
| RandomColorRangeMin |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 40 |
| RandomColorRangeMax |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 190 |
| Attribute |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Min |  | [FMinSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMinSettings) | (MinAttrValue=0.000000,MinColor=(R=0.000000,G=1.000000,B=0.000000,A=1.000000)) |
| Max |  | [FMaxSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMaxSettings) | (MaxAttrValue=1.000000,MaxColor=(R=1.000000,G=0.000000,B=0.000000,A=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to visualize | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Level |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ExplodeAmount | Scale amount to expand the pieces uniformly in all directions | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Scale | Scale amounts to expand the pieces in all 3 directions | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Offset | Translate collection for exploded view | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to visualize | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-visualizekinematicfaces.md

# VisualizeKinematicFaces

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeKinematicFaces

> Application Version: 5.7

### Description

VisualizeKinematicFaces (v1)

Visualizes kinematic faces from GeometryCollection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FVisualizeKinematicFacesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FVisualizeKinematicFacesNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-visualizepositiontargets.md

# VisualizePositionTargets

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizePositionTargets

> Application Version: 5.7

### Description

VisualizePositionTargets (v1)

Visualizes position target vectors from GeometryCollection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FVisualizePositionTargetsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FVisualizePositionTargetsNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VectorField |  | [FFieldCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FFieldCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-visualizetetrahedrons.md

# VisualizeTetrahedrons

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeTetrahedrons

> Application Version: 5.7

### Description

VisualizeTetrahedrons (v1)

Visualize tetrahedrons in a collection

Input(s) :
Collection [Intrinsic] - Collection for the custom attribute

Output(s):
Collection [Passthrough] - Collection for the custom attribute

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Flesh|Utilities |
| Type | [FVisualizeTetrahedronsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVisualizeTetrahedronsDataflowNo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Vertices |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-voronoifracture.md

# VoronoiFracture

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VoronoiFracture

> Application Version: 5.7

### Description

VoronoiFracture (v2)

Voronoi fracture
Fracture using a Voronoi diagram with a uniform random pattern, creating fracture pieces of similar volume across the shape.

Input(s) :
Collection [Intrinsic] - Collection to fracture
Points [Intrinsic] - Voronoi source points
TransformSelection - Pieces to fracture
Transform - Transform to apply to cut planes
ChanceToFracture - Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.
Grout - Amount of space to leave between cut pieces
Amplitude - Size of the Perlin noise displacement (in cm). If 0, no noise will be applied
Frequency - Period of the Perlin noise. Smaller values will create a smoother noise pattern
Persistence - Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor
Lacunarity - Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor
OctaveNumber - Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity
Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains
PointSpacing - Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to fracture
TransformSelection [Passthrough] - Pieces to fracture
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FVoronoiFractureDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVoronoiFractureDataflowNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to fracture | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Points | Voronoi source points | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| TransformSelection | Pieces to fracture | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Transform | Transform to apply to cut planes | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| ChanceToFracture | Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Grout | Amount of space to leave between cut pieces | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Amplitude | Size of the Perlin noise displacement (in cm). If 0, no noise will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Frequency | Period of the Perlin noise. Smaller values will create a smoother noise pattern | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| Persistence | Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Lacunarity | Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| OctaveNumber | Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| PointSpacing | Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to fracture | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Pieces to fracture | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-wavescalarfield.md

# WaveScalarField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WaveScalarField

> Application Version: 5.7

### Description

WaveScalarField (v1)

WaveScalar Field Dataflow node v2

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FWaveScalarFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FWaveScalarFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FunctionType |  | [EDataflowWaveFunctionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowWaveFunctionType) | Dataflow\_WaveFunctionType\_Cosine |
| FalloffType |  | [EDataflowFieldFalloffType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowFieldFalloffType) | Dataflow\_FieldFalloffType\_Linear |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Position |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Translation |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Wavelength |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| Period |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-weightmap.md

# WeightMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WeightMap

> Application Version: 5.7

### Description

WeightMap (v1)

For Name implicit operators.

Input(s) :
TransferCollection - The collection used to transfer weight map from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Weight Map |
| Type | [FChaosClothAssetWeightMapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightMapNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutputName | The name to be set as a weight map attribute. | [FChaosClothAssetConnectableOStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableOStri-) | (StringValue="") |
| InputName | The name to populate this map from and override based on Map Override Type. Output Name will be used if Input Name is empty. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |
| MeshTarget |  | [EChaosClothAssetWeightMapMeshTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapMeshTar-) | Simulation |
| MapOverrideType | How to apply this node's weight values onto existing maps. Changing this value will change the output map. To change how the node's stored weights are calculated, change the equivalent value on the Weight Map Paint Tool context. | [EChaosClothAssetWeightMapOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapOverrid-) | ReplaceChanged |
| TransferType | The type of transfer used to transfer the weight map when a TransferCollection is connected and MeshTarget is Simulation. Render weight maps always do a 3D transfer. This property is disabled when no TransferCollection input has been connected. | [EChaosClothAssetWeightMapTransferType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapTransfe-) | Use2DSimMesh |
| Transfer | Transfer the weight map from the connected Transfer Collection containing a weight map with Input Name (or Output Name if Input Name is empty). | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransferCollection | The collection used to transfer weight map from. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| OutputName.StringValue | The value for this property. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-weightmaptoselection.md

# WeightMapToSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WeightMapToSelection

> Application Version: 5.7

### Description

WeightMapToSelection (v1)

Convert a vertex weight map to an integer selection set.

Input(s) :
WeightMapName - The name of the Weight Map to convert.

Output(s):
SelectionName - The name of the select attribute that will be added to the collection.
If left empty the same name as the Weight Map name will be used instead.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Weight Map To Selection |
| Type | [FChaosClothAssetWeightMapToSelectionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightMapToSelec-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionType | The type of element the selection refers to | [EChaosClothAssetWeightMapConvertableSelectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_5) | SimVertices3D |
| SelectionThreshold | Map values above this will be selected. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.950000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| WeightMapName | The name of the Weight Map to convert. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SelectionName | The name of the select attribute that will be added to the collection. If left empty the same name as the Weight Map name will be used instead. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-wrap.md

# Wrap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Wrap

> Application Version: 5.7

### Description

Wrap (v1)

Wrap Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FWrapDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FWrapDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Float |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Min |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Max |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-writestringtofile.md

# Write String to File

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WriteStringtoFile

> Application Version: 5.7

### Description

Write String to File (v1)

Write a string to a file

Input(s) :
FilePath - Where file should be written on disk
FileContents - Contents of the file to write

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Development |
| Type | [FWriteStringToFile](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FWriteStringToFile) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FileContents | Contents of the file to write | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| FilePath | Where file should be written on disk | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow.md

# Dataflow

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow

> Application Version: 5.7

### Cloth

| Node | Description |
| --- | --- |
| [AddStitch](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddStitch) | AddStitch (v1) Chaos Cloth Asset Add Stitch Node |
| [ApplyProxyDeformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyProxyDeformer) | ApplyProxyDeformer (v1) Update the Render Mesh by applying any existing proxy deformer data. |
| [ApplyResizing](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing) | ApplyResizing (v1) Experimental Apply resizing for a given Target Mesh. |
| [Attribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute) | Attribute (v2) Experimental Create a new attribute for the specified group. |
| [BindToRootBone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BindToRootBone) | BindToRootBone (v1) Bind an entire mesh to the single root bone of the current skeleton set on the cloth collection. |
| [BlendVertices](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices) | BlendVertices (v1) Blend vertex values from another cloth collection. |
| [ClothAssetImport](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport) | ClothAssetImport (v1) For Reimport Input(s) : ClothAsset - The Cloth Asset to import into a collection. |
| [ClothAssetTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetTerminal) | ClothAssetTerminal (v2) Cloth terminal node to generate a cloth asset from a cloth collection. |
| [ClothCollectionQuery](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothCollectionQuery) | ClothCollectionQuery (v1) Query a Managed Array Collection about its Cloth Collection properties. |
| [ClothCollectionToDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothCollectionToDynamicMesh) | ClothCollectionToDynamicMesh (v1) Experimental Convert a Cloth Collection mesh to a dynamic mesh. |
| [CopySimulationToRenderMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CopySimulationToRenderMesh) | CopySimulationToRenderMesh (v1) Copy the simulation mesh to the render mesh to be able to render the simulation mesh, or when not using a different mesh for rendering. |
| [CustomRegionResizing](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CustomRegionResizing) | CustomRegionResizing (v1) Experimental Node for adding custom region resizing data used by the ChaosOutfitAsset's Resizeable Outfit. |
| [DeleteElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteElement) | DeleteElement (v1) For EChaosClothAssetElementType |
| [EnableUVResizing](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EnableUVResizing) | EnableUVResizing (v1) Experimental Node for enabling UV Resizing used by the ChaosOutfitAsset's Resizeable Outfit. |
| [ExtractClothSelectionSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet) | ExtractClothSelectionSet (v1) Experimental Extract a selection set from a Cloth Collection. |
| [ExtractClothWeightMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothWeightMap) | ExtractClothWeightMap (v1) Experimental Extract a weight map from a Cloth Collection. |
| [GenerateSimMorphTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget) | GenerateSimMorphTarget (v1) Generate a Sim Morph target from a cloth collection sim mesh (with matching topology). |
| [ImportSimulationCache](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache) | ImportSimulationCache (v1) Experimental Set vertex values from a simulation cache. |
| [MakeClothAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeClothAsset) | MakeClothAsset (v1) Experimental Cloth terminal node to generate a cloth asset from a cloth collection. |
| [MergeClothCollections](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeClothCollections) | MergeClothCollections (v2) Merge multiple cloth collections into a single cloth collection of multiple patterns. |
| [ProceduralSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ProceduralSelection) | ProceduralSelection (v1) Procedurally generate a Cloth Selection set. |
| [ProxyDeformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ProxyDeformer) | ProxyDeformer (v3) Adds the proxy deformer information to this cloth collection's render data. |
| [RecalculateNormals](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RecalculateNormals) | RecalculateNormals (v1) Experimental Recalculate the geometry's normals. |
| [ReferenceBone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReferenceBone) | ReferenceBone (v1) Explicitly set the cloth Reference Bone (used when calculating SimulationVelocityScale). |
| [Remesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Remesh) | Remesh (v2) Remesh the cloth surface(s) to get the specified mesh resolution(s). |
| [ReverseNormals](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals) | ReverseNormals (v1) Reverse the geometry's normals or/and winding order of the simulation or/and render meshes stored in the cloth collection. |
| [Selection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection) | Selection (v2) Chaos Cloth Asset Selection Node V 2 Input(s) : TransferCollection - The collection used to transfer sets from. |
| [SelectionToIntMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToIntMap) | SelectionToIntMap (v1) Convert an integer index selection to an integer map. |
| [SelectionToWeightMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap) | SelectionToWeightMap (v1) Convert an integer index selection to a vertex weight map where different map values can be set for selected and unselected vertices. |
| [SetPhysicsAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetPhysicsAsset) | SetPhysicsAsset (v1) Replace the current physics assets to collide the simulation mesh against. |
| [SimAccessoryMeshNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimAccessoryMeshNode) | SimAccessoryMeshNode (v1) Add a SimAccessoryMesh by converting a cloth collection into an accessory mesh and attaching it to an existing cloth collection. |
| [SimulationAerodynamicsConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig) | SimulationAerodynamicsConfig (v1) Aerodynamics properties configuration node. |
| [SimulationAnimDriveConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAnimDriveConfig) | SimulationAnimDriveConfig (v1) Anim drive properties configuration node. |
| [SimulationBackstopConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBackstopConfig) | SimulationBackstopConfig (v1) Backstop properties configuration node. |
| [SimulationBendingConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig) | SimulationBendingConfig (v1) Bending constraint property configuration node. |
| [SimulationBendingOverrideConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingOverrideConfig) | SimulationBendingOverrideConfig (v1) Experimental Bending constraint property override configuration node. |
| [SimulationClothVertexFaceSpringConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexFaceSpringConfig) | SimulationClothVertexFaceSpringConfig (v1) Experimental Node for creating vertex-face constraints and setting their simulation properties. |
| [SimulationClothVertexSpringConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig) | SimulationClothVertexSpringConfig (v1) Experimental Node for creating vertex-vertex constraints and setting their simulation properties. |
| [SimulationCollisionConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig) | SimulationCollisionConfig (v1) Chaos Cloth Asset Simulation Collision Config Node |
| [SimulationDampingConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationDampingConfig) | SimulationDampingConfig (v1) Damping properties configuration node. |
| [SimulationDefaultConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationDefaultConfig) | SimulationDefaultConfig (v1) Add default simulation properties to the cloth collection in the format of the skeletal mesh cloth editor. |
| [SimulationGravityConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationGravityConfig) | SimulationGravityConfig (v1) Gravity properties configuration node. |
| [SimulationLongRangeAttachmentConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationLongRangeAttachmentConfig) | SimulationLongRangeAttachmentConfig (v2) Long range attachment constraint property configuration node. |
| [SimulationMassConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMassConfig) | SimulationMassConfig (v1) Mass properties configuration node. |
| [SimulationMaxDistanceConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMaxDistanceConfig) | SimulationMaxDistanceConfig (v1) Maximum distance constraint property configuration node. |
| [SimulationMorphTargetConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMorphTargetConfig) | SimulationMorphTargetConfig (v1) Simulation Morph Target configuration node. |
| [SimulationMultiResConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMultiResConfig) | SimulationMultiResConfig (v1) Experimental Experimental Solver multires configuration node. |
| [SimulationPressureConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationPressureConfig) | SimulationPressureConfig (v1) Pressure properties configuration node. |
| [SimulationResolveExtremeDeformationConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationResolveExtremeDeformationConfig) | SimulationResolveExtremeDeformationConfig (v1) Resolve extreme deformation properties configuration node. |
| [SimulationSelfCollisionConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig) | SimulationSelfCollisionConfig (v2) Self-collision repulsion forces (point-face) properties configuration node. |
| [SimulationSelfCollisionSpheresConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionSpheresConfig) | SimulationSelfCollisionSpheresConfig (v1) Self-collision spheres properties configuration node. |
| [SimulationSolverConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig) | SimulationSolverConfig (v1) Solver properties configuration node. |
| [SimulationStretchConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchConfig) | SimulationStretchConfig (v1) Stretching constraint property configuration node. |
| [SimulationStretchOverrideConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig) | SimulationStretchOverrideConfig (v1) Experimental Stretching constraint property override configuration node. |
| [SimulationVelocityScaleConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig) | SimulationVelocityScaleConfig (v1) Velocity scale properties configuration node. |
| [SkeletalMeshImport](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport) | SkeletalMeshImport (v2) Import a skeletal mesh asset into the cloth collection simulation and/or render mesh containers. |
| [SkinningBlend](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkinningBlend) | SkinningBlend (v1) Initialize the RenderDeformerSkinningBlend weight map from the ProxyDeformer mapping data. |
| [StaticMeshImport](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport) | StaticMeshImport (v2) Import a static mesh asset into the cloth collection simulation and/or render mesh containers. |
| [TransferSkinWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights) | TransferSkinWeights (v1) Transfer the skinning weights set on a skeletal mesh to the simulation and/or render mesh stored in the cloth collection. |
| [TransformPositions](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions) | TransformPositions (v1) Chaos Cloth Asset Transform Positions Node |
| [TransformUVs](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformUVs) | TransformUVs (v1) Chaos Cloth Asset Transform UVs Node |
| [UpdateClothFromDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh) | UpdateClothFromDynamicMesh (v1) Experimental Update cloth collection attributes from a DynamicMesh |
| [USDImport](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport) | USDImport (v2) Import a USD file from a third party garment construction software. |
| [WeightMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WeightMap) | WeightMap (v1) For Name implicit operators. |
| [WeightMapToSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WeightMapToSelection) | WeightMapToSelection (v1) Convert a vertex weight map to an integer selection set. |

### Collection

| Node | Description |
| --- | --- |
| [CorrectSkinWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights) | CorrectSkinWeights (v1) Experimental Correct skin weights vertex properties. |
| [EditSkeletonBones](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones) | EditSkeletonBones (v1) Experimental Edit skeleton bones properties. |
| [EditSkinWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights) | EditSkinWeights (v1) Experimental Edit skin weights vertex properties. |
| [GetSkinningSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSkinningSelection) | GetSkinningSelection (v1) Experimental Get skin weights selection attributes. |
| [PaintWeightMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PaintWeightMap) | PaintWeightMap (v1) Scalar vertex properties. |
| [SetSkinningSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetSkinningSelection) | SetSkinningSelection (v1) Experimental Set skin weights selection attributes. |
| [SetSkinningSkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetSkinningSkeletalMesh) | SetSkinningSkeletalMesh (v1) Experimental Set the skeletal mesh for the collection Input(s) : Collection - Managed array collection to be used to store datas SkeletalMesh - Skeletal mesh binding to be stored in the collection GeometrySelection - Geometries to set skinning skeletal mesh on Output(s): Collection [Passthrough] - Managed array collection to be used to store datas |

### Collection|Utilities

| Node | Description |
| --- | --- |
| [CreateColorArrayFromFloatArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray) | CreateColorArrayFromFloatArray (v1) Set the vertex color on the collection based on the normalized float array. |
| [SetVertexColorFromFloatArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromFloatArray) | SetVertexColorFromFloatArray (v1) Set the vertex color on the collection based on the normalized float array. |
| [SetVertexColorFromVertexIndices](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromVertexIndices) | SetVertexColorFromVertexIndices (v1) Set the vertex color of the collection based on the selection set. |
| [SetVertexColorFromVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromVertexSelection) | SetVertexColorFromVertexSelection (v1) Set the vertex color of the collection based on the selection set. |

### Convert

| Node | Description |
| --- | --- |
| [ConvertBoolArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertBoolArrayTypes) | ConvertBoolArrayTypes (v1) Convert Bool array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertBoolTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertBoolTypes) | ConvertBoolTypes (v1) Convert Bool types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertIndexArrayToSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertIndexArrayToSelection) | ConvertIndexArrayToSelection (v1) Convert Index Array to Selection Input(s) : Collection [Intrinsic] - Collection for the selection In [Intrinsic] - Input value Output(s): Collection [Passthrough] - Collection for the selection Out - Output value |
| [ConvertIndexToSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertIndexToSelection) | ConvertIndexToSelection (v1) Convert Index to Selection Input(s) : Collection [Intrinsic] - Collection for the selection In [Intrinsic] - Input value Output(s): Collection [Passthrough] - Collection for the selection Out - Output value |
| [ConvertNumericArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertNumericArrayTypes) | ConvertNumericArrayTypes (v1) Convert Numeric array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertNumericTypes) | ConvertNumericTypes (v1) Convert Numeric types (double, float, int64, uint64, int32, uint32, int16, uint16, int8, uint8) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertRotation](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertRotation) | ConvertRotation (v1) Convert Rotation (FQuat, FRotator, FVector) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertSelectionToIndexArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionToIndexArray) | ConvertSelectionToIndexArray (v1) Convert Selection to Index Array Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes) | ConvertSelectionTypes (v1) Convert Selection types Input(s) : Collection [Intrinsic] - GeometryCollection for the selection In [Intrinsic] - Input value Output(s): Collection [Passthrough] - GeometryCollection for the selection Out - Output value |
| [ConvertStringArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringArrayTypes) | ConvertStringArrayTypes (v1) Convert String array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertStringConvertibleTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringConvertibleTypes) | ConvertStringConvertibleTypes (v1) Convert String convertible types (String types, Numeric types, Vector types and Booleans) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertStringTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringTypes) | ConvertStringTypes (v1) Convert String types (FString or FName or FText) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertTransformArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertTransformArrayTypes) | ConvertTransformArrayTypes (v1) Convert Transform array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertTransformTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertTransformTypes) | ConvertTransformTypes (v1) Convert Transform types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertVectorArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertVectorArrayTypes) | ConvertVectorArrayTypes (v1) Convert Vector array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertVectorTypes) | ConvertVectorTypes (v1) Convert Vector types (2D, 3D and 4D vector, single and double precision) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |

### Core

| Node | Description |
| --- | --- |
| [Print](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Print) | Print (v1) Print value in the log Supports any type comnvertible to a string |
| [ReRouteNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReRouteNode) | ReRouteNode (v1) Dataflow Re Route Node |

### Dataflow

| Node | Description |
| --- | --- |
| [BreakAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakAttributeKey) | BreakAttributeKey (v1) Break Attribute Key Dataflow Node |
| [FloatOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatOverride) | FloatOverride (v1) Float Override Dataflow Node |
| [GetVariable](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetVariable) | GetVariable (v1) Get Dataflow Variable Node |
| [SelectionSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionSet) | SelectionSet (v1) Selection Set Dataflow Node |

### Fields

| Node | Description |
| --- | --- |
| [BoxFalloffField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxFalloffField) | BoxFalloffField (v1) BoxFalloff Field Dataflow node |
| [FieldMakeDenseFloatArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray) | FieldMakeDenseFloatArray (v1) Converts a sparse FloatArray (a selected subset of the whole incoming array) into a dense FloatArray (same number of elements as the incoming array using NumSamplePositions) using the Remap input NumSamplePositions controls the size of the output array, only indices smaller than l to than NumSamplePositions will be processed |
| [NoiseField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/NoiseField) | NoiseField (v1) Noise Field Dataflow node |
| [PlaneFalloffField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PlaneFalloffField) | PlaneFalloffField (v1) PlaneFalloff Field Dataflow node |
| [RadialFalloffField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialFalloffField) | RadialFalloffField (v1) RadialFalloff Field Dataflow node |
| [RadialIntMaskField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialIntMaskField) | RadialIntMaskField (v1) RadialIntMask Field Dataflow node |
| [RadialVectorField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialVectorField) | RadialVectorField (v1) RadialVector Field Dataflow node |
| [RandomVectorField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomVectorField) | RandomVectorField (v1) RandomVector Field Dataflow node |
| [SumScalarField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SumScalarField) | SumScalarField (v1) Sum Scalar Field Dataflow Node |
| [SumVectorField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SumVectorField) | SumVectorField (v1) Sum Vector Field Dataflow Node |
| [UniformIntegerField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformIntegerField) | UniformIntegerField (v1) UniformInteger Field Dataflow node |
| [UniformScalarField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformScalarField) | UniformScalarField (v1) UniformScalar Field Dataflow node |
| [UniformVectorField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformVectorField) | UniformVectorField (v1) UniformVector Field Dataflow node |
| [WaveScalarField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WaveScalarField) | WaveScalarField (v1) WaveScalar Field Dataflow node v2 |

### Flesh

| Node | Description |
| --- | --- |
| [AddKinematicParticles](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddKinematicParticles) | AddKinematicParticles (v1) Add Kinematic Particles Dataflow Node |
| [AppendTetrahedralCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection) | AppendTetrahedralCollection (v2) Append another Tetrahedral Collection to this collection. |
| [AppendToCollectionTransformAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendToCollectionTransformAttribute) | AppendToCollectionTransformAttribute (v1) @todo(deprecate), move to GeometryCollection as AppendCollectionTransformDataflowNode |
| [AuthorSceneCollisionCandidates](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates) | AuthorSceneCollisionCandidates (v1) Marks mesh vertices as candidates for scene collision raycasts. |
| [AuthorTetMetrics](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorTetMetrics) | AuthorTetMetrics (v1) Generate quality metrics Input(s) : Collection - Passthrough geometry collection. |
| [ComputeFiberField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField) | ComputeFiberField (v1) Computes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra, vertices, and origin & insertion vertex fields. |
| [ComputeFiberStreamline](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline) | ComputeFiberStreamline (v1) Computes fiber streamlines (line segments) flowing from muscle origins to insertions in the muscle fiber field. |
| [ComputeIslands](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeIslands) | ComputeIslands (v1) @todo(deprecate) |
| [ComputeMuscleActivationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeMuscleActivationData) | ComputeMuscleActivationData (v2) Determines muscles that are eligible for activation and computes muscle activation data. |
| [CreateAirTetrahedralConstraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint) | CreateAirTetrahedralConstraint (v1) Create air tetrahedral constraint between point-triangle pair from surface meshes of different geometries based on search radius. |
| [CreateAirVolumeConstraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirVolumeConstraint) | CreateAirVolumeConstraint (v1) Experimental Creates volume constraint (defined by point-triangle tetrahedron volume) between surface meshes of different geometries. |
| [CreateTetrahedron](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron) | CreateTetrahedron (v1) Create Tetrahedron Dataflow Node Input(s) : Collection - Input pass-through collection. |
| [DeleteFleshVertices](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteFleshVertices) | DeleteFleshVertices (v1) Extract a Tetrahedral Collection from this collection based on selected vertex. |
| [DeleteVertexTrianglePositionTargetBinding](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteVertexTrianglePositionTargetBinding) | DeleteVertexTrianglePositionTargetBinding (v1) Delete vertex-triangle weak constraints (zero rest length springs) between VertexSelection1 and VertexSelection2. |
| [GenerateOriginInsertion](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateOriginInsertion) | GenerateOriginInsertion (v1) Given two sets of vertex indices, generate two sets of vertex indices for origins and insertions that are within X distance away. |
| [GenerateSkeletalBindings](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSkeletalBindings) | GenerateSkeletalBindings (v1) Generate barycentric bindings (used by the FleshDeformer deformer graph) of a render surface to a tetrahedral mesh. |
| [GenerateSurfaceBindings](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings) | GenerateSurfaceBindings (v1) Generate barycentric bindings (used by the FleshDeformer deformer graph and Geometry Cache generation) of a render surface to a tetrahedral mesh and its surface. |
| [GetFleshAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetFleshAsset) | GetFleshAsset (v1) Get Flesh Asset Dataflow Node |
| [GetSurfaceIndices](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSurfaceIndices) | GetSurfaceIndices (v1) Get Surface Indices Node |
| [IsolateComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/IsolateComponent) | IsolateComponent (v1) Isolate Component Node Input(s) : Collection - typedef FManagedArrayCollection DataType; Output(s): Collection [Passthrough] - typedef FManagedArrayCollection DataType; |
| [KinematicBodySetupInitialization](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicBodySetupInitialization) | KinematicBodySetupInitialization (v1) @todo(deprecate), rename to FCollisionBodyConstraintDataflowNode |
| [KinematicInitialization](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicInitialization) | KinematicInitialization (v1) @todo(deprecate), rename to FKinematicConstraintDataflowNode |
| [KinematicMuscleAttachments](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicMuscleAttachments) | KinematicMuscleAttachments (v1) Kinematic Muscle Attachments Dataflow Node |
| [KinematicSkeletalMeshInitialization](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicSkeletalMeshInitialization) | KinematicSkeletalMeshInitialization (v1) @todo(deprecate), rename to FSkeletalMeshConstraintDataflowNode |
| [KinematicSkeletonConstraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicSkeletonConstraint) | KinematicSkeletonConstraint (v1) Bind a animation driven skeleton hierarchy into the tetrahedron on the collection. |
| [RadialTetrahedron](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialTetrahedron) | RadialTetrahedron (v1) @todo(deprecate), rename to FRadialTetrahedronDataflowNode |
| [ReadSkeletalMeshCurves](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReadSkeletalMeshCurves) | ReadSkeletalMeshCurves (v1) Read Skeletal Mesh Curves Dataflow Node |
| [SetCollidableVertices](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollidableVertices) | SetCollidableVertices (v1) Set custom vertices so that only these vertices can collide with other surfaces. |
| [SetFleshBonePositionTargetBinding](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding) | SetFleshBonePositionTargetBinding (v2) Binds vertices from Collection to bone skeletal mesh surface via kinematic or weak constraints. |
| [SetFleshDefaultProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties) | SetFleshDefaultProperties (v1) Set Flesh Default Properties Node |
| [SetMuscleActivationParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter) | SetMuscleActivationParameter (v1) Sets per-muscle parameters for custom muscle contraction. |
| [SetVertexTetrahedraPositionTargetBinding](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTetrahedraPositionTargetBinding) | SetVertexTetrahedraPositionTargetBinding (v1) Set Vertex Tetrahedra Position Target Binding Dataflow Node |
| [SetVertexTrianglePositionTargetBinding](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding) | SetVertexTrianglePositionTargetBinding (v1) Create point-triangle weak constraints (springs) between surface meshes of different geometries based on search radius. |
| [SetVertexVertexPositionTargetBinding](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexVertexPositionTargetBinding) | SetVertexVertexPositionTargetBinding (v1) Set Vertex Vertex Position Target Binding Dataflow Node |
| [SkinSimulationProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkinSimulationProperties) | SkinSimulationProperties (v1) Set triangle mesh to simulate using skin constraints |
| [TriangleMeshSimulationProperties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TriangleMeshSimulationProperties) | TriangleMeshSimulationProperties (v1) Convert tetmesh to simulate using surface traingle mesh only |
| [VisualizeFiberField](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFiberField) | VisualizeFiberField (v1) Visualizes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra. |
| [VisualizeKinematicFaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeKinematicFaces) | VisualizeKinematicFaces (v1) Visualizes kinematic faces from GeometryCollection. |
| [VisualizePositionTargets](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizePositionTargets) | VisualizePositionTargets (v1) Visualizes position target vectors from GeometryCollection. |

### Flesh|Experimental

| Node | Description |
| --- | --- |
| [TriangleBoundaryIndices](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TriangleBoundaryIndices) | TriangleBoundaryIndices (v1) Experimental Outputs boundary nodes of a triangle mesh |

### Flesh|Utilities

| Node | Description |
| --- | --- |
| [VisualizeTetrahedrons](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeTetrahedrons) | VisualizeTetrahedrons (v1) Visualize tetrahedrons in a collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute Output(s): Collection [Passthrough] - Collection for the custom attribute |

### FlowControl

| Node | Description |
| --- | --- |
| [Branch](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Branch) | Branch (v1) Dataflow Branch Node |
| [ForceDependency](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency) | ForceDependency (v1) Force an evaluation dependency between two values Input(s) : Value - Evaluating Value will force an evaluation of DependentValue DependentValue - Evaluating Value will force an evaluation of DependentValue Output(s): Value [Passthrough] - Evaluating Value will force an evaluation of DependentValue |
| [Select](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Select) | Select (v1) Dataflow Select Node |

### General

| Node | Description |
| --- | --- |
| [GetPhysicsAssetFromSkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetPhysicsAssetFromSkeletalMesh) | GetPhysicsAssetFromSkeletalMesh (v1) Get the physics assets from input skeletal mesh. |
| [SkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMesh) | SkeletalMesh (v1) Get Skeletal Mesh Dataflow Node |
| [SkeletalMeshBone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshBone) | SkeletalMeshBone (v1) Skeletal Mesh Bone Dataflow Node |
| [SkeletalMeshReferenceTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshReferenceTransform) | SkeletalMeshReferenceTransform (v1) Skeletal Mesh Reference Transform Dataflow Node |
| [Skeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Skeleton) | Skeleton (v1) Get Skeleton Dataflow Node |
| [StaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMesh) | StaticMesh (v1) Get Static Mesh Dataflow Node |

### Generators|Box

| Node | Description |
| --- | --- |
| [MakeBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeBox) | MakeBox (v1) Make a box |

### Generators|Collection

| Node | Description |
| --- | --- |
| [MakeCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCollection) | MakeCollection (v1) Make an empty ManagedArrayCollection |

### Generators|Mesh

| Node | Description |
| --- | --- |
| [MakeBoxMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeBoxMesh) | MakeBoxMesh (v1) Make a box mesh Output(s): Mesh - Output mesh |
| [MakeCapsuleMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCapsuleMesh) | MakeCapsuleMesh (v1) Make a capsule mesh Output(s): Mesh - Output mesh |
| [MakeCylinderMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCylinderMesh) | MakeCylinderMesh (v1) Make a cylinder mesh Output(s): Mesh - Output mesh |
| [MakeDiscMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeDiscMesh) | MakeDiscMesh (v1) Make a disc mesh Output(s): Mesh - Output mesh |
| [MakeRectangleMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRectangleMesh) | MakeRectangleMesh (v1) Make a rectangle mesh Input(s) : Origin - Rectangle will be translated so that center is at this point Normal - Normal vector of all vertices will be set to this value. |
| [MakeSphereMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSphereMesh) | MakeSphereMesh (v1) Make a sphere mesh Output(s): Mesh - Output mesh |
| [MakeStairMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeStairMesh) | MakeStairMesh (v1) Make a stair mesh Output(s): Mesh - Output mesh |
| [MakeTorusMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeTorusMesh) | MakeTorusMesh (v1) Make a torus mesh Input(s) : Origin - Torus will be translated so that center is at this point Output(s): Mesh - Output mesh |

### Generators|Plane

| Node | Description |
| --- | --- |
| [MakePlane](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakePlane) | MakePlane (v1) Make a plane Input(s) : BasePoint - Base point Normal - Normal vector Output(s): Plane - Output mesh |

### Generators|Point

| Node | Description |
| --- | --- |
| [AppendPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendPoints) | AppendPoints (v1) Combine two arrays of points into one |
| [ClusterScatterPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints) | ClusterScatterPoints (v1) Cluster Scatter Points Dataflow Node Input(s) : NumberClustersMin - Minimum number of clusters of points to create. |
| [GridScatterPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GridScatterPoints) | GridScatterPoints (v1) Grid Scatter Points Dataflow Node Input(s) : NumberOfPointsInX - Number of points in X direction NumberOfPointsInY - Number of points in Y direction NumberOfPointsInZ - Number of points in Z direction RandomSeed - Seed for random MaxRandomDisplacementX - Random displacement in X direction will be in the range (-MaxRandomDisplacementX, MaxRandomDisplacementX) MaxRandomDisplacementY - Random displacement in Y direction will be in the range (-MaxRandomDisplacementY, MaxRandomDisplacementY) MaxRandomDisplacementZ - Random displacement in Z direction will be in the range (-MaxRandomDisplacementZ, MaxRandomDisplacementZ) BoundingBox - BoundingBox to generate points inside of Output(s): Points - Generated points |
| [MakePoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakePoints) | MakePoints (v1) Make a points array from specified points |
| [RadialScatterPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialScatterPoints) | RadialScatterPoints (v2) Radial Scatter Points Dataflow Node V 2 Input(s) : BoundingBox - BoundingBox to generate points inside of Center - Center of generated pattern Normal - Normal to plane in which sites are generated RandomSeed - Seed for random AngularSteps - Number of angular steps AngleOffset - Angle offset at each radial step (in degrees) AngularNoise - Amount of global variation to apply to each angular step (in degrees) Radius - Pattern radius (in cm) RadialSteps - Number of radial steps RadialStepExponent - Radial steps will follow a distribution based on this exponent, i.e., Pow(distance from center, RadialStepExponent) RadialMinStep - Minimum radial separation between any two voronoi points (in cm) RadialNoise - Amount of global variation to apply to each radial step (in cm) RadialVariability - Amount to randomly displace each Voronoi site radially (in cm) AngularVariability - Amount to randomly displace each Voronoi site in angle (in degrees) AxialVariability - Amount to randomly displace each Voronoi site in the direction of the rotation axis (in cm) Output(s): Points - Generated points |
| [TransformPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPoints) | TransformPoints (v1) Transform an array of points |
| [UniformScatterPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformScatterPoints) | UniformScatterPoints (v2) Uniform Scatter Points Dataflow Node V 2 Input(s) : MinNumberOfPoints - Minimum for the random range MaxNumberOfPoints - Maximum for the random range RandomSeed - Seed for random BoundingBox - BoundingBox to generate points inside of Output(s): Points - Generated points |

### Generators|Sphere

| Node | Description |
| --- | --- |
| [MakeSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSphere) | MakeSphere (v1) Description for this node |

### Generators|Transform

| Node | Description |
| --- | --- |
| [MakeRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator) | MakeRotator (v1) Make a Rotator Input(s) : Pitch - Rotation around the right axis (around Y axis), Looking up and down (0=Straight Ahead, +Up, -Down) Yaw - Rotation around the up axis (around Z axis), Turning around (0=Forward, +Right, -Left) Roll - Rotation around the forward axis (around X axis), Tilting your head, (0=Straight, +Clockwise, -CCW) Output(s): Rotator - Rotator output |
| [MakeTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeTransform) | MakeTransform (v1) Make an FTransform Note: Originaly this version was depricated and replaced with FMakeTransformDataflowNode\_v2 but when AnyRotationType was introduced with the ConvertAnyRotation node FMakeTransformDataflowNode\_v2 became obsolete and this version became the current version again Input(s) : InTranslation - Translation InRotation - Rotation as Euler InScale - Scale Output(s): OutTransform - Result transform |

### GeometryCollection

| Node | Description |
| --- | --- |
| [AddRootProxyMeshToArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray) | AddRootProxyMeshToArray (v1)  *Add a root proxy object to an array of root proxy mesh*  \* (used by geometry collection assets) Input(s) : RootProxyMeshes - Root proxy array to add the mesh to Output(s): RootProxyMeshes [Passthrough] - Root proxy array to add the mesh to |
| [AppendCollections](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendCollections) | AppendCollections (v1) Description for this node |
| [CloseGeometryOnCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CloseGeometryOnCollection) | CloseGeometryOnCollection (v1) Close Geometry on Collection Dataflow Node |
| [CollectionToSkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToSkeletalMesh) | CollectionToSkeletalMesh (v1) Collection to Skeletal Mesh Dataflow Node |
| [MakeAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeAttributeKey) | MakeAttributeKey (v1) Make Attribute Key Dataflow Node |
| [MakeRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRootProxyMesh) | MakeRootProxyMesh (v1) Create a RootProxyMesh object (used by geometry collection assets) Input(s) : Mesh - mesh to use as a proxy Transform - transform to use for the proxy, relative to the asset it will be used for Output(s): RootProxyMesh - mesh to use as a proxy |
| [MakeRootProxyMeshArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRootProxyMeshArray) | MakeRootProxyMeshArray (v1) Create a RootProxyMesh Array (used by geometry collection assets) Output(s): RootProxyMeshes - newly created array |
| [SetKinematicVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetKinematicVertexSelection) | SetKinematicVertexSelection (v1) Set VertexSelection to be kinematic. |
| [SkeletalMeshToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshToCollection) | SkeletalMeshToCollection (v1) Skeletal Mesh to Collection Dataflow Node |
| [TransferVertexAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexAttribute) | TransferVertexAttribute (v1) Transfer float properties from a source collection to a target collection. |
| [TransferVertexSkinWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights) | TransferVertexSkinWeights (v1) Transfer skin weights from a source collection to a target collection. |
| [TransformCollectionAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformCollectionAttribute) | TransformCollectionAttribute (v1) Transform Collection Attribute Dataflow Node |
| [VertexScalarToVertexIndices](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VertexScalarToVertexIndices) | VertexScalarToVertexIndices (v1) Convert an vertex float array to a list of indices Input(s) : AttributeKey - The name of the vertex attribute and group to generate indices from. |

### GeometryCollection|Asset

| Node | Description |
| --- | --- |
| [BlueprintToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BlueprintToCollection) | BlueprintToCollection (v2) Create a geometry collection from an asset Output(s): Collection - Geometry collection newly created Materials - Material instances array from the static mesh InstancedMeshes - Array of instanced meshes RootProxyMeshes - corresponding source proxies |
| [CreateGeometryCollectionFromSources](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateGeometryCollectionFromSources) | CreateGeometryCollectionFromSources (v2) create a geometry collection from a set of geometry sources if the source array is not connected, the source array from the current asset is going to be used Input(s) : Sources - array of geometry sources Output(s): Collection - Geometry collection newly created Materials - Materials array to use for this asset InstancedMeshes - array of instanced meshes RootProxyMeshes - corresponding source proxies |
| [GeometryCollectionToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionToCollection) | GeometryCollectionToCollection (v2) Converts a UGeometryCollection asset to an FManagedArrayCollection Output(s): Collection - Geometry collection newly created Materials - Material instances array from the static mesh InstancedMeshes - Array of instanced meshes RootProxyMeshes - corresponding source proxies |
| [GetCollectionFromAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionFromAsset) | GetCollectionFromAsset (v1) Description for this node |
| [GetGeometryCollectionAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionAsset) | GetGeometryCollectionAsset (v1) Get Current geometry collection asset Note : Use with caution as this may get replaced in a near future for a more generic getAsset node Output(s): Asset - Asset this data flow graph instance is assigned to |
| [GetGeometryCollectionSources](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources) | GetGeometryCollectionSources (v1) Get the list of the original mesh information used to create a specific geometryc collection asset each entry contains a mesh, a transform and a list of override materials Input(s) : Asset - Asset to get geometry sources from Output(s): Sources - array of geometry sources |
| [StaticMeshToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshToCollection) | StaticMeshToCollection (v2) Create a geometry collection from a UStaticMesh Input(s) : StaticMesh - Asset input MeshTransform - Transform to apply to the mesh before converting it to a collection Output(s): Collection - Geometry collection newly created Materials - Material array from the static mesh InstancedMeshes - Array of instanced meshes RootProxyMeshes - corresponding source proxies |

### GeometryCollection|Cluster

| Node | Description |
| --- | --- |
| [AutoCluster](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster) | AutoCluster (v1) Automatically group pieces of a fractured Collection into a specified number of clusters Input(s) : ClusterSites - Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries ClusterFraction - Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process SiteSize - Choose the Edge-Size of the cube used to groups bones under a cluster (in cm). |
| [Cluster](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Cluster) | Cluster (v1) Cluster selected nodes under a new parent Input(s) : Collection [Intrinsic] - Collection on which to cluster nodes TransformSelection - Bone selection Output(s): Collection [Passthrough] - Collection on which to cluster nodes |
| [ClusterIsolatedRoots](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterIsolatedRoots) | ClusterIsolatedRoots (v1) Add a single cluster to the Geometry Collection if it only has a single transform with no clusters Input(s) : Collection [Intrinsic] - Collection to modify Output(s): Collection [Passthrough] - Collection to modify |
| [ClusterMagnet](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMagnet) | ClusterMagnet (v1) Cluster by grouping the selected bones with their adjacent, neighboring bones. |
| [ClusterMerge](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMerge) | ClusterMerge (v1) Merge selected bones under a new parent cluster Input(s) : Collection [Intrinsic] - Collection on which to merge bones into a cluster TransformSelection - Bone selection Output(s): Collection [Passthrough] - Collection on which to merge bones into a cluster |
| [ClusterMergeToNeighbors](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors) | ClusterMergeToNeighbors (v1) Merge selected bones to their neighbors Input(s) : Collection [Intrinsic] - Collection on which to merge bones into a neighboring cluster TransformSelection - Bone selection MinVolumeCubeRoot - Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value bOnlyToConnected - Whether to only allow clusters to merge if their bones are connected in the proximity graph bOnlySameParent - Whether to only allow clusters to merge if they have the same parent bone Output(s): Collection [Passthrough] - Collection on which to merge bones into a neighboring cluster |
| [Flatten](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Flatten) | Flatten (v1) Flattens selected bones. |
| [Uncluster](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Uncluster) | Uncluster (v1) Uncluster selected nodes Input(s) : Collection [Intrinsic] - Fractured GeometryCollection to uncluster TransformSelection - Bone selection Output(s): Collection [Passthrough] - Fractured GeometryCollection to uncluster |

### GeometryCollection|Development

| Node | Description |
| --- | --- |
| [Convert Mesh to OBJ String](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString) | Convert Mesh to OBJ String (v1) Convert a mesh to a string formatted as an OBJ file, which can be read by many external mesh viewers Input(s) : bInvertFaces - Whether to flip the orientation of the triangles in the OBJ output Output(s): StringOBJ - A string representing the input mesh in the OBJ file format |
| [Write String to File](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WriteStringtoFile) | Write String to File (v1) Write a string to a file Input(s) : FilePath - Where file should be written on disk FileContents - Contents of the file to write |

### GeometryCollection|Edit

| Node | Description |
| --- | --- |
| [MergeInCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeInCollection) | MergeInCollection (v1) Merges selected bones into a single bone Input(s) : Collection [Intrinsic] - Fractured GeometryCollection to merge TransformSelection [Intrinsic] - Transform selection for merging Output(s): Collection [Passthrough] - Fractured GeometryCollection to merge |
| [PruneInCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PruneInCollection) | PruneInCollection (v1) Deletes selected bones from Collection. |
| [SetVisibilityInCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVisibilityInCollection) | SetVisibilityInCollection (v1) Sets all selected bone's visibilty to Visible/Hidden Input(s) : Collection [Intrinsic] - Fractured GeometryCollection to set visibility TransformSelection [Intrinsic] - Transform selection for setting visibility FaceSelection [Intrinsic] - Face selection for setting visibility Output(s): Collection [Passthrough] - Fractured GeometryCollection to set visibility |

### GeometryCollection|Fracture

| Node | Description |
| --- | --- |
| [BrickCutter](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter) | BrickCutter (v1) Editor Fracture Mode / Fracture / Brick tool Fracture with a customizable brick pattern. |
| [MeshCutter](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter) | MeshCutter (v1) Editor Fracture Mode / Fracture / Mesh tool Fracture using the shape of a chosen static mesh and/or array of dynamic meshes Input(s) : Collection [Intrinsic] - Collection to cut BoundingBox - Boundingbox to create the cutting planes in TransformSelection - The selected pieces to cut Transform - Transform to apply to cut planes CuttingDynamicMeshes - Dynamic Meshes to cut with CuttingStaticMesh - Static Mesh to cut with NumberToScatter - Number of meshes to random scatter GridX - Number of meshes to add to grid in X GridY - Number of meshes to add to grid in Y GridZ - Number of meshes to add to grid in Z Variability - Magnitude of random displacement to cutting meshes MinScaleFactor - Minimum scale factor to apply to cutting meshes. |
| [PlaneCutter](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PlaneCutter) | PlaneCutter (v2) Editor Fracture Mode / Fracture / Planar tool Fracture using a set of noised up planes. |
| [SliceCutter](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SliceCutter) | SliceCutter (v1) Editor Fracture Mode / Fracture / Slice tool Fracture with a grid of X, Y, and Z slices, with optional random variation in angle and offset. |
| [UniformFracture](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformFracture) | UniformFracture (v1) Editor Fracture Mode / Fracture / Uniform tool Fracture using a Voronoi diagram with a uniform random pattern, creating fracture pieces of similar volume across the shape. |
| [VoronoiFracture](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VoronoiFracture) | VoronoiFracture (v2) Voronoi fracture Fracture using a Voronoi diagram with a uniform random pattern, creating fracture pieces of similar volume across the shape. |

### GeometryCollection|Fracture|Utilities

| Node | Description |
| --- | --- |
| [ExplodedView](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView) | ExplodedView (v1) "Explodes" the pieces from the Collection for better visualization Input(s) : Collection [Intrinsic] - Collection to explode UniformScale - Scale amount to expand the pieces uniformly in all directions Scale - Scale amounts to expand the pieces in all 3 directions Offset - Translate collection for exploded view Output(s): Collection [Passthrough] - Collection to explode |
| [FixTinyGeo](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo) | FixTinyGeo (v1) Editor Fracture Mode / Utilities / TinyGeo tool Merge pieces of geometry onto their neighbors -- use it to, for example, clean up too small pieces of geometry. |
| [RecomputeNormalsInGeometryCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RecomputeNormalsInGeometryCollection) | RecomputeNormalsInGeometryCollection (v1) Editor Fracture Mode / Utilities / Normals tool Recompute normals and tangents. |
| [ResampleGeometryCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ResampleGeometryCollection) | ResampleGeometryCollection (v1) Editor Fracture Mode / Utilities / Resample tool Resample to add collision particles in large flat regions that otherwise might have poor collision response. |
| [ValidateGeometryCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ValidateGeometryCollection) | ValidateGeometryCollection (v1) Editor Fracture Mode / Utilities / Validate tool Ensures that geometrycollection is valid and clean. |
| [VisualizeFracture](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture) | VisualizeFracture (v1) Visualizing fracture/cluster info in fractured collection Input(s) : Collection [Intrinsic] - Collection to visualize RandomSeed - Seed for random ExplodeAmount - Scale amount to expand the pieces uniformly in all directions Scale - Scale amounts to expand the pieces in all 3 directions Offset - Translate collection for exploded view Output(s): Collection [Passthrough] - Collection to visualize |

### GeometryCollection|Mesh

| Node | Description |
| --- | --- |
| [Convex Hull to Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvexHulltoMesh) | Convex Hull to Mesh (v1) Convert convex hulls on a geometry collection to a dynamic mesh Input(s) : OptionalSelectionFilter - Optional transform selection to convert hulls from -- if not provided, all convex hulls will be converted. |
| [Sphere Covering to Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SphereCoveringtoMesh) | Sphere Covering to Mesh (v1) Convert a sphere covering, as generated by the 'protect negative space' option on the "Generate Cluster Convex Hull" nodes, to a dynamic mesh Input(s) : SphereCovering [Intrinsic] - The sphere covering to convert to a mesh |

### GeometryCollection|Overrides

| Node | Description |
| --- | --- |
| [GetBoolOverrideFromAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoolOverrideFromAsset) | GetBoolOverrideFromAsset (v1) Get Bool Override from Asset Dataflow Node |
| [GetFloatOverrideFromAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetFloatOverrideFromAsset) | GetFloatOverrideFromAsset (v1) Get Float Override from Asset Dataflow Node |
| [GetIntOverrideFromAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetIntOverrideFromAsset) | GetIntOverrideFromAsset (v1) Get Int Override from Asset Dataflow Node |
| [GetStringOverrideFromAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetStringOverrideFromAsset) | GetStringOverrideFromAsset (v1) Get String Override from Asset Dataflow Node |

### GeometryCollection|Selection

| Node | Description |
| --- | --- |
| [CollectionSelectInternalFaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectInternalFaces) | CollectionSelectInternalFaces (v1) Select internal faces Input(s) : Collection [Intrinsic] - Collection to select the internal faces from TransformSelection - Transform selection to get the internal faces from if this input is not connected, then all internal faces from the collection will be returned Output(s): Collection [Passthrough] - Collection to select the internal faces from FaceSelection - selection containing Internal faces |
| [CollectionSelectionConvert](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionConvert) | CollectionSelectionConvert (v1) Converts Vertex/Face/Transform selection into Vertex/Face/Transform selection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection TransformSelection - Transform selection including the new indices FaceSelection - Face selection including the new indices VertexSelection - Vertex selection including the new indices Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection [Passthrough] - Transform selection including the new indices FaceSelection [Passthrough] - Face selection including the new indices VertexSelection [Passthrough] - Vertex selection including the new indices |
| [CollectionSelectionInvert](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionInvert) | CollectionSelectionInvert (v1) Inverts selection ( support all selection types ) Input(s) : Selection [Intrinsic] - selection to invert Output(s): Selection [Passthrough] - selection to invert |
| [CollectionSelectionSetOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation) | CollectionSelectionSetOperation (v1) Runs boolean operation on selection ( support all selection types ) Input(s) : SelectionA [Intrinsic] - First Selection object SelectionB [Intrinsic] - Second Selection object Output(s): Selection - Array of the selected bone indices after operation |

### GeometryCollection|Selection|All

| Node | Description |
| --- | --- |
| [CollectionSelectByAttr](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr) | CollectionSelectByAttr (v1) Selects specified Vertices/Faces/Transforms in the GeometryCollection by using an attribute value Currently supported attribute types: float, int32, String, bool Input(s) : Collection [Intrinsic] - GeometryCollection for the selection AttributeKey - AttributeKey input Output(s): Collection [Passthrough] - GeometryCollection for the selection VertexSelection - Vertex selection output FaceSelection - Face selection output TransformSelection - Transform selection output GeometrySelection - Geometry selection output MaterialSelection - Material selection output CurveSelection - Curve selection output |
| [GeometrySelectionToVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometrySelectionToVertexSelection) | GeometrySelectionToVertexSelection (v1) Converts GeometrySelection to VertexSelection Input(s) : Collection - GeometryCollection GeometrySelection - Input geometry selection Output(s): VertexSelection - Vertex selection output |

### GeometryCollection|Selection|Array

| Node | Description |
| --- | --- |
| [CollectionTransformSelectionFromIndexArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray) | CollectionTransformSelectionFromIndexArray (v1) Convert index array to a transform selection Input(s) : Collection [Intrinsic] - Collection to use for the selection. |
| [SelectFloatArrayIndicesInRange](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectFloatArrayIndicesInRange) | SelectFloatArrayIndicesInRange (v1) Selects indices of a float array by range Input(s) : Values - GeometryCollection for the selection Output(s): Indices - Indices of float Values matching the specified range |

### GeometryCollection|Selection|Face

| Node | Description |
| --- | --- |
| [CollectionFaceSelectCustom](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionFaceSelectCustom) | CollectionFaceSelectCustom (v1) Selects specified faces in the GeometryCollection by using a space separated list Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection FaceSelection - Face selection including the new indices |

### GeometryCollection|Selection|Transform

| Node | Description |
| --- | --- |
| [CollectionSelectTransformString](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString) | CollectionSelectTransformString (v1) Selects transforms by name using a the BoneName attributeor other Transform group string typed attributes Input(s) : Collection [Intrinsic] - Collection for the selection Attribute - Text to serach in the name SearchText - Text to serach in the name Output(s): Collection [Passthrough] - Collection for the selection TransformSelection - output selection of the matching transforms |
| [CollectionSetTransformString](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSetTransformString) | CollectionSetTransformString (v1) Set selected transform string value the string format can use the following predefined value : - {Current} current value of the attribute - {Index} index in the selection passed as input Input(s) : Collection [Intrinsic] - Collection for the selection TransformSelection - input selection of the transforms to set - if not connected use all Attribute - Text to serach in the name TextToSet - Text to set Output(s): Collection [Passthrough] - Collection for the selection |
| [CollectionTransformSelectAll](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectAll) | CollectionTransformSelectAll (v1) Selects all the bones for the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectByFloatAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByFloatAttribute) | CollectionTransformSelectByFloatAttribute (v1) Selects bones by a float attribute Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectByIntAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute) | CollectionTransformSelectByIntAttribute (v1) Selects bones by an int attribute Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Transform selection including the new indices |
| [CollectionTransformSelectByPercentage](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByPercentage) | CollectionTransformSelectByPercentage (v1) Outputs the specified percentage of the selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices RandomSeed - Seed value for the random generation Output(s): TransformSelection [Passthrough] - Array of the selected bone indices |
| [CollectionTransformSelectBySize](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectBySize) | CollectionTransformSelectBySize (v1) Selects pieces based on their size Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectByVolume](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByVolume) | CollectionTransformSelectByVolume (v1) Selects pieces based on their volume Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectChildren](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectChildren) | CollectionTransformSelectChildren (v1) Selects the children of the selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectCluster](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCluster) | CollectionTransformSelectCluster (v2) Selects the clusters in the Collection this version works properly and address the issues found in the deprecated version 1 Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectContact](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectContact) | CollectionTransformSelectContact (v1) Selects the contact(s) of the selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectCustom](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom) | CollectionTransformSelectCustom (v2) Selects specified bones in the GeometryCollection by using a comma separated list, e.g. "0, 2, 5-10, 12-15" Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectInBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectInBox) | CollectionTransformSelectInBox (v1) Selects bones if their Vertices/BoundingBox/Centroid in a box Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Box [Intrinsic] - Box to contain Vertices/BoundingBox/Centroid Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectInSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectInSphere) | CollectionTransformSelectInSphere (v1) Selects bones if their Vertices/BoundingBox/Centroid in a sphere Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Sphere [Intrinsic] - Sphere to contain Vertices/BoundingBox/Centroid Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectionInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionInfo) | CollectionTransformSelectionInfo (v1) Generates a formatted string of the bones and the selection Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection - GeometryCollection for the selection Output(s): String - Formatted string of the bones and selection |
| [CollectionTransformSelectLeaf](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectLeaf) | CollectionTransformSelectLeaf (v1) Selects the leaves in the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectNone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectNone) | CollectionTransformSelectNone (v1) Generates an empty bone selection for the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectParent) | CollectionTransformSelectParent (v1) Selects the parents of the currently selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectRandom](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectRandom) | CollectionTransformSelectRandom (v1) Selects bones randomly in the Collection Input(s) : RandomSeed - Seed for the random generation, only used if Deterministic is on RandomThreshold - Bones get selected if RandomValue > RandomThreshold Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectRoot](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectRoot) | CollectionTransformSelectRoot (v1) Selects the root bones in the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectSameLevel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectSameLevel) | CollectionTransformSelectSameLevel (v1) Expand the selection to include all nodes with the same level as the selected nodes Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectSiblings](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectSiblings) | CollectionTransformSelectSiblings (v1) Selects the siblings of the selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectTargetLevel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectTargetLevel) | CollectionTransformSelectTargetLevel (v1) Selects the root bones in the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection TargetLevel - Level to select Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |

### GeometryCollection|Selection|Vertex

| Node | Description |
| --- | --- |
| [CollectionVertexSelectByPercentage](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectByPercentage) | CollectionVertexSelectByPercentage (v1) Outputs the specified percentage of the selected vertices Input(s) : VertexSelection [Intrinsic] - Array of the selected bone indices RandomSeed - Seed value for the random generation Output(s): VertexSelection [Passthrough] - Array of the selected bone indices |
| [CollectionVertexSelectCustom](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom) | CollectionVertexSelectCustom (v1) Selects specified vertices in the GeometryCollection by using a space separated list Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection VertexSelection - Vertex selection including the new indices |

### GeometryCollection|Texture

| Node | Description |
| --- | --- |
| [BakeTextureFromCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection) | BakeTextureFromCollection (v1)  *Bake a texture from a geometry collection*  Output to a 4 channels Image object ( RGBA ) Input(s) : Collection [Intrinsic] - Target Collection FaceSelection - selection of faces to bake : if not connected, all faces will be used Resolution - resolution of the image to bake GutterSize - Approximate space to leave between UV islands, measured in texels UVChannel - Index of the added UV channel MaxDistance - Max distance to search for the outer mesh surface OcclusionRays - Number of occlusion rays OcclusionBlurRadius - Pixel Radius of Gaussian Blur Kernel applied to AO map (0 will apply no blur) CurvatureBlurRadius - Pixel Radius of Gaussian Blur Kernel applied to Curvature map (0 will apply no blur) VoxelResolution - Voxel resolution of smoothed shape representation SmoothingIterations - Amount of smoothing iterations to apply before computing curvature ThicknessFactor - Distance to search for correspondence between fractured shape and smoothed shape, as factor of voxel size MaxCurvature - Curvatures in the range [-MaxCurvature, MaxCurvature] will be mapped from [0,1]. |

### GeometryCollection|Utilities

| Node | Description |
| --- | --- |
| [AddCustomCollectionAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddCustomCollectionAttribute) | AddCustomCollectionAttribute (v1) Adds custom attribute to Collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute Output(s): Collection [Passthrough] - Collection for the custom attribute |
| [ClearConvexHulls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClearConvexHulls) | ClearConvexHulls (v1) Clear convex hulls from a collection Input(s) : TransformSelection - [Optional] selection of transforms to clear convex on, if not set all the transform will be used |
| [CollectionToPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToPoints) | CollectionToPoints (v1) Get vertices from a collection as a point cloud Input(s) : Collection [Intrinsic] - Collection storing the points Output(s): Collection [Passthrough] - Collection storing the points Points - Points from the collection |
| [CreateLeafConvexHulls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls) | CreateLeafConvexHulls (v1) Create Leaf Convex Hulls Dataflow Node Input(s) : OptionalSelectionFilter - Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed. |
| [CreateNonOverlappingConvexHulls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls) | CreateNonOverlappingConvexHulls (v1) Generates convex hull representation for the bones for simulation Input(s) : CanExceedFraction - Fraction (of geometry volume) by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children. |
| [GenerateClusterConvexHullsFromChildrenHulls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromChildrenHulls) | GenerateClusterConvexHullsFromChildrenHulls (v1) Generates cluster convex hulls for children hulls Input(s) : ConvexCount - Maximum number of convex to generate for a specific cluster. |
| [GenerateClusterConvexHullsFromLeafHulls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls) | GenerateClusterConvexHullsFromLeafHulls (v1) Generates cluster convex hulls for leafs hulls Input(s) : ConvexCount - Maximum number of convex to generate for a specific cluster. |
| [GetBoundingBoxesFromCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoundingBoxesFromCollection) | GetBoundingBoxesFromCollection (v1) Gets BoundingBoxes of pieces from a Collection Input(s) : Collection - Input Collection TransformSelection - The BoundingBoxes will be output for the bones selected in the TransformSelection Output(s): BoundingBoxes - Output BoundingBoxes |
| [GetCentroidsFromCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection) | GetCentroidsFromCollection (v1) Gets centroids of pieces from a Collection Input(s) : Collection - Input Collection TransformSelection - The centroids will be output for the bones selected in the TransformSelection Output(s): Centroids - Output centroids Levels - Hidden output to store computed level values for centroids |
| [GetCollectionAttributeDataTyped](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionAttributeDataTyped) | GetCollectionAttributeDataTyped (v1) Get attribute data from a Collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute AttributeKey - Input to drive the Attribute and Group name Output(s): BoolAttributeData - Bool type attribute data FloatAttributeData - Float type attribute data DoubleAttributeData - Float type attribute data Int32AttributeData - Int type attribute data StringAttributeData - Int type attribute data Vector3fAttributeData - Vector3f type attribute data Vector3dAttributeData - Vector3d type attribute data LinearColorAttributeData - Vector3d type attribute data |
| [GetConvexHullVolume](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume) | GetConvexHullVolume (v1) Get the sum of volumes of the convex hulls on the selected nodes Input(s) : TransformSelection [Intrinsic] - The transforms to consider Output(s): Volume - Sum of convex hull volumes |
| [GetNumElementsInCollectionGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup) | GetNumElementsInCollectionGroup (v1) Returns number of elements in a group in a Collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute Output(s): NumElements - Number of elements for the attribute |
| [GetRootIndexFromCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetRootIndexFromCollection) | GetRootIndexFromCollection (v1) Get the root node index |
| [GetSchema](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSchema) | GetSchema (v1) Collects group and attribute information from the Collection and outputs it into a formatted string Input(s) : Collection - GeometryCollection for the information Output(s): String - Formatted string containing the groups and attributes |
| [MakeConvexDecompositionSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeConvexDecompositionSettings) | MakeConvexDecompositionSettings (v1) Provide settings for running convex decomposition of geometry Input(s) : MinSizeToDecompose - If greater than zero, the minimum geometry size (cube root of volume) to consider for convex decomposition MaxGeoToHullVolumeRatioToDecompose - If the geo volume / hull volume ratio is greater than this, do not consider convex decomposition ErrorTolerance - Stop splitting when hulls have error less than this (expressed in cm; will be cubed for volumetric error). |
| [MergeConvexHulls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeConvexHulls) | MergeConvexHulls (v1) Merge convex hulls on transforms with multiple hulls Input(s) : MaxConvexCount - Maximum number of convex to generate per transform. |
| [PointsToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PointsToCollection) | PointsToCollection (v1) Add point cloud to a collection as vertices Input(s) : Collection [Intrinsic] - Collection to add the points to Points - Points to add to the collection Output(s): Collection [Passthrough] - Collection to add the points to |
| [Proximity](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity) | Proximity (v1) Update the proximity (contact) graph for the bones in a Collection Input(s) : DistanceThreshold - If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors ContactThreshold - If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity Collection [Intrinsic] - GeometryCollection to update the proximity graph on Output(s): Collection [Passthrough] - GeometryCollection to update the proximity graph on |
| [RemoveOnBreak](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak) | RemoveOnBreak (v1) Remove on Break Dataflow Node Input(s) : Collection [Intrinsic] - Collection to set theremoval data on TransformSelection - selection to apply the data on ( if not specified the entire collection will be set ) bEnabledRemoval - Whether or not to enable the removal on the selection PostBreakTimer - How long after the break the removal will start ( Min / Max ) RemovalTimer - How long removal will last ( Min / Max ) bClusterCrumbling - If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect Output(s): Collection [Passthrough] - Collection to set theremoval data on |
| [SetAnchorState](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetAnchorState) | SetAnchorState (v1) Sets the anchored state on the selected bones in a Collection Input(s) : Collection [Intrinsic] - GeometryCollection to set anchor state on TransformSelection [Intrinsic] - Bone selection for setting the state on Output(s): Collection [Passthrough] - GeometryCollection to set anchor state on |
| [SetCollectionAttributeDataTyped](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped) | SetCollectionAttributeDataTyped (v1) Set attribute data in a Collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute AttributeKey - Input to drive the Attribute and Group name BoolAttributeData - Bool type attribute data FloatAttributeData - Float type attribute data DoubleAttributeData - Float type attribute data Int32AttributeData - Int type attribute data StringAttributeData - Int type attribute data Vector3fAttributeData - Vector3f type attribute data Vector3dAttributeData - Vector3d type attribute data LinearColorAttributeData - LinearColor type attribute data Output(s): Collection [Passthrough] - Collection for the custom attribute |
| [SetDynamicState](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetDynamicState) | SetDynamicState (v1) Sets the dynamic state on the selected bones in a Collection Input(s) : Collection [Intrinsic] - GeometryCollection to set anchor state on TransformSelection [Intrinsic] - Bone selection for setting the state on Output(s): Collection [Passthrough] - GeometryCollection to set anchor state on |
| [SetPivot](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetPivot) | SetPivot (v1) Sets pivot for Collection Input(s) : Collection [Intrinsic] - Collection for the pivot change Transform - Pivot transform Output(s): Collection [Passthrough] - Collection for the pivot change |
| [SimplifyConvexHulls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimplifyConvexHulls) | SimplifyConvexHulls (v1) Simplify Convex Hulls Dataflow Node Input(s) : OptionalSelectionFilter - Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed. |
| [SpheresToPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SpheresToPoints) | SpheresToPoints (v1) Outputs Spheres as Points and radius values Output(s): Points - Centers of the spheres Radii - Radius values |
| [UpdateVolumeAttributes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateVolumeAttributes) | UpdateVolumeAttributes (v1) Update the Volume and Size attributes on the target Collection (and add them if they were not present) |

### GeometryCollection|UV

| Node | Description |
| --- | --- |
| [AddUVChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddUVChannel) | AddUVChannel (v1)  *Add a new UV channel to the collection*  note that there's a maximum of 8 channels that can be handled by a collection Input(s) : Collection [Intrinsic] - Target Collection Output(s): Collection [Passthrough] - Target Collection UVChannel - Index of the added UV channel |
| [AutoUnwrapUV](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV) | AutoUnwrapUV (v1) Auto unwrap UVs for a specific UV channel Input(s) : Collection [Intrinsic] - Target Collection FaceSelection - Faces to auto unwrap, no selection means all faces UVChannel - UV channel to unwrap into ( 0 by default ) GutterSize - Approximate space to leave between UV islands, measured in texels for 512x512 texture Output(s): Collection [Passthrough] - Target Collection UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default ) |
| [BoxProjectUV](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV) | BoxProjectUV (v1) Generates UVs using a box projection Input(s) : Collection [Intrinsic] - Target Collection UVChannel - UV channel to unwrap into ( 0 by default ) GutterSize - Approximate space to leave between UV islands, measured in texels for 512x512 texture Output(s): Collection [Passthrough] - Target Collection UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default ) |
| [MergeUVIslands](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeUVIslands) | MergeUVIslands (v1) Merge adjacent UV Islands with similar normals for a specific UV channel Input(s) : Collection [Intrinsic] - Target Collection FaceSelection - Faces to auto unwrap, no selection means all faces UVChannel - UV channel to unwrap into ( 0 by default ) AreaDistortionThreshold - Threshold for allowed area distortion from merging islands (when we use ExpMap to compute new UVs for the merged island) MaxNormalDeviationDeg - Threshold for allowed normal deviation between merge-able islands NormalSmoothingRounds - Amount of normal smoothing to apply when computing new UVs for merged islands. |

### Groom

| Node | Description |
| --- | --- |
| [AttachCurveRoots](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AttachCurveRoots) | AttachCurveRoots (v1) Experimental Attach the curve roots by setting their kinematic weights to 1.0f Input(s) : Collection - Managed array collection to be used to store datas CurveSelection - Curve selection to focus the geometry transfer spatially Output(s): Collection [Passthrough] - Managed array collection to be used to store datas KinematicWeightsKey - Vertex kinematic weights key to be used in other nodes if necessary |
| [BuildCurveLODs](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs) | BuildCurveLODs (v1) Experimental Builds the curves LODs Input(s) : Collection - Managed array collection to be used to store data CurveSelection - Curve selection to focus the geometry LODs spatially Output(s): Collection [Passthrough] - Managed array collection to be used to store data CurveParentsKey - Curve parent indices key to be used in other nodes if necessary CurveLodsKey - Curve lods indices key to be used in other nodes if necessary |
| [BuildCurveWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights) | BuildCurveWeights (v1) Experimental Build a weight map that will be identical on every curves Input(s) : Collection - Managed array collection to be used to store datas CurveSelection - Curve selection to focus the geometry transfer spatially WeightsAttribute - Vertex kinematic weights key to be used in other nodes if necessary Output(s): Collection [Passthrough] - Managed array collection to be used to store datas |
| [BuildSplineSkinWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights) | BuildSplineSkinWeights (v1) Experimental Build spline skinning data from skeletal mesh Input(s) : Collection - Managed array collection to be used to store datas VertexSelection - Vertex selection to focus the geometry transfer spatially SkeletalMesh - SkeletalMesh used to compute spline skinning weights. |
| [GenerateCurveGeometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry) | GenerateCurveGeometry (v1) Experimental Build the curve geometry from a collection containing curves Input(s) : Collection - Managed array collection to be used to store datas SourceCurves - Managed array collection to be used to store datas CurveSelection - Curve selection to focus the curves generation spatially CurveCount - Max number of guides Output(s): Collection [Passthrough] - Managed array collection to be used to store datas |
| [GetCurveAttributes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCurveAttributes) | GetCurveAttributes (v1) Experimental Get the kinematic weights attributes names Output(s): AttributeKey - Attribute key to build |
| [GetGroomAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGroomAsset) | GetGroomAsset (v2) Experimental Get the groom asset Output(s): GroomAsset - Groom asset that will be used in the dataflow graph |
| [GroomAssetTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetTerminal) | GroomAssetTerminal (v2) Experimental Groom Asset Terminal Dataflow Node V 2 |
| [GroomAssetToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection) | GroomAssetToCollection (v1) Experimental Transform a groom asset to a collection Input(s) : GroomAsset - Input asset to read the guides from CurvesType - Type of curves to use to fill the groom collection (guides/strands) CurvesThickness - Curves thickness for geometry generation Output(s): Collection - Managed array collection used to store the curves |
| [LinearToSplineSkinWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/LinearToSplineSkinWeights) | LinearToSplineSkinWeights (v1) Experimental Convert linear skinning data to spline skinning data Input(s) : Collection - Managed array collection to be used to store datas VertexSelection - Vertex selection to process vertices subset Output(s): Collection [Passthrough] - Managed array collection to be used to store datas SplineParamKey - Spline skinning parameter key SplineBonesKey - Spline bones key. |
| [ResampleCurvePoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ResampleCurvePoints) | ResampleCurvePoints (v1) Experimental Resample the curves with a fixed number of points Input(s) : Collection - Managed array collection to be used to store datas CurveSelection - Curve selection to focus the guides generation spatially NumPoints - Max number of points (to be able to plug into a variable since enum is not supported in dataflow) Output(s): Collection [Passthrough] - Managed array collection to be used to store datas |
| [SmoothCurvePoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SmoothCurvePoints) | SmoothCurvePoints (v1) Experimental Smooth the curves for more stable deformation Input(s) : Collection - Managed array collection to be used to store data CurveSelection - Curve selection to focus the guides smoothing spatially SmoothingFactor - Smoothing factor between 0 and 1 Output(s): Collection [Passthrough] - Managed array collection to be used to store data |
| [SplineToLinearSkinWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SplineToLinearSkinWeights) | SplineToLinearSkinWeights (v1) Experimental Convert spline skinning data to linear data Input(s) : Collection - Managed array collection to be used to store datas VertexSelection - Vertex selection to process vertices subset SplineParamKey - Spline skinning parameter key SplineBonesKey - Spline bones key. |
| [TransferLinearSkinWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferLinearSkinWeights) | TransferLinearSkinWeights (v1) Experimental Build the curves skinning by transferring the indices weights from a skelmesh geometry Input(s) : Collection - Managed array collection to be used to store datas VertexSelection - Vertex selection to focus the geometry transfer spatially SkeletalMesh - SkeletalMesh used to transfer the skinning weights. |

### Image

| Node | Description |
| --- | --- |
| [ImageCombineChannels](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels) | ImageCombineChannels (v1) Combine channels into a single RGBA image Outputs are single channel images Input(s) : Red - Red channel - if not connected, use black color Green - Green channel - if not connected, use black color Blue - Blue channel - if not connected, use black color Alpha - Alpha channel - if not connected, use black color Output(s): Image - Output image recombined from input channels |
| [ImageFromColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor) | ImageFromColor (v1) Create a RGBA image from a single color at a specific resolution Outputs are single channel images Input(s) : FillColor - color to fill the image with Resolution - resolution of the output image Output(s): Image - Output image |
| [ImageSplitChannels](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageSplitChannels) | ImageSplitChannels (v1) Split a image in individual channels Outputs are single channel images Input(s) : Image - Input image to split per channel Output(s): Red - Red channel Green - Green channel Blue - Blue channel Alpha - Alpha channel |
| [ImageToTexture](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageToTexture) | ImageToTexture (v1) Create a transient texture asset from an image |
| [TextureToImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TextureToImage) | TextureToImage (v1) Experimental Import a texture asset as an image. |

### Materials

| Node | Description |
| --- | --- |
| [AddToMaterialArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddToMaterialArray) | AddToMaterialArray (v1) Add material(s) to an array Input(s) : MaterialArray - Material array to add to Output(s): MaterialArray [Passthrough] - Material array to add to |
| [AssignMaterialToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection) | AssignMaterialToCollection (v1) Assign material to a set of face in a geometry collection Input(s) : Collection [Intrinsic] - Collection to assign material to FaceSelection - Faces that will be set with this material index, if no selection is connected , all faces will be set MaterialArray [Intrinsic] - Array holding the materials objects Material - Material to assign to the selection Output(s): Collection [Passthrough] - Collection to assign material to MaterialArray [Passthrough] - Array holding the materials objects MaterialIndex - Index where the material was set in the array |
| [GetMaterialAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMaterialAsset) | GetMaterialAsset (v1) Get a material interface from an existing asset Output(s): Material - Material asset to get |
| [MakeMaterialArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeMaterialArray) | MakeMaterialArray (v1) Make a array from a user defined list of material objects Output(s): MaterialArray - Material array set by the user |
| [MaterialInterfaceTextureOverride](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MaterialInterfaceTextureOverride) | MaterialInterfaceTextureOverride (v1) Experimental Duplicate the given material and replace the target texture with the override texture on the newly-created material |
| [SetIntoMaterialsArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetIntoMaterialsArray) | SetIntoMaterialsArray (v1) Set an element into a material array at a specific index (if the index does not match the range of the array, the array will remain unchanged) Input(s) : MaterialArray [Intrinsic] - Material array to modify Material - Material to set at the specific index into the array Index - Index Set the material at (if the index does not match the range of the array, the array will remain unchanged) Output(s): MaterialArray [Passthrough] - Material array to modify |

### Math

| Node | Description |
| --- | --- |
| [MathExpression](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MathExpression) | MathExpression (v1) Expression node for floats |

### Math|Boolean

| Node | Description |
| --- | --- |
| [BooleanOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BooleanOperation) | BooleanOperation (v1) Boolean operations Input(s) : bBoolA - Boolean input bBoolB - Boolean input Output(s): bResult - Boolean result of the operator |
| [MakeLiteralBool](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralBool) | MakeLiteralBool (v2) Make a bool value |

### Math|Compare

| Node | Description |
| --- | --- |
| [CompareFloat](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CompareFloat) | CompareFloat (v1) Comparison between floats Output(s): Result - Boolean result of the comparison |
| [CompareInt](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CompareInt) | CompareInt (v1) Comparison between integers Output(s): Result - Boolean result of the comparison |

### Math|Conversions

| Node | Description |
| --- | --- |
| [FloatArrayToIntArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray) | FloatArrayToIntArray (v1) Converts a Float array to Int array using the specified method. |

### Math|Double

| Node | Description |
| --- | --- |
| [MakeLiteralDouble](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralDouble) | MakeLiteralDouble (v1) Make a double value |

### Math|Float

| Node | Description |
| --- | --- |
| [Division (Whole and Remainder)](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DivisionWholeandRemainder) | Division (Whole and Remainder) (v1) Division Dataflow Node |
| [EFit](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EFit) | EFit (v1) Fits a value from one range to another Takes the value num from the range (oldmin, oldmax) and shifts it to the corresponding value in the new range (newmin, newmax). |
| [Fit](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Fit) | Fit (v1) Fits a value from one range to another Returns a number between newmin and newmax that is relative to num in the range between oldmin and oldmax. |
| [FloatArrayNormalize](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize) | FloatArrayNormalize (v1) Normalize the selected float data in a FloatArray Input(s) : InFloatArray [Intrinsic] - Input VectorArray Selection - Selection for the operation |
| [FloatMathExpression](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatMathExpression) | FloatMathExpression (v1) Expression node for floats |
| [Lerp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Lerp) | Lerp (v1) Linearly interpolates between A and B based on Alpha. |
| [MakeFloatArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeFloatArray) | MakeFloatArray (v1) M Input(s) : NumElements - Number of elements of the array Value - Value to initialize the array with Output(s): FloatArray - Output float array |
| [MakeLiteralFloat](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralFloat) | MakeLiteralFloat (v2) Make a float value |
| [NormalizeToRange](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/NormalizeToRange) | NormalizeToRange (v1) Returns Float normalized to the given range |
| [Wrap](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Wrap) | Wrap (v1) Wrap Dataflow Node |

### Math|Int

| Node | Description |
| --- | --- |
| [MakeLiteralInt](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralInt) | MakeLiteralInt (v2) Make an integer value |

### Math|Random

| Node | Description |
| --- | --- |
| [RandomFloat](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomFloat) | RandomFloat (v1) Generates a random float |
| [RandomFloatInRange](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomFloatInRange) | RandomFloatInRange (v1) Generates a random float between Min and Max |
| [RandomUnitVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVector) | RandomUnitVector (v1) Returns a random vector with length of 1 |
| [RandomUnitVectorInCone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone) | RandomUnitVectorInCone (v1) Returns a random vector with length of 1, within the specified cone, with uniform random distribution Input(s) : ConeDirection - The base "center" direction of the cone ConeHalfAngle - The half-angle of the cone (from ConeDir to edge), in degrees |

### Math|Scalar

| Node | Description |  |  |
| --- | --- | --- | --- |
| [Abs](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Abs) | Abs (v1) Absolute value ( | A | ) |
| [Add](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Add) | Add (v1) Addition (A + B) |  |  |
| [Ceil](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Ceil) | Ceil (v1) Ceil ( 1.4 => 2.0 | 1.9 => 2.0 | -5.3 => -5.0) |
| [Clamp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Clamp) | Clamp (v1) Clamp(A, Min, Max) clamp a value to specific range (inclusive) |  |  |
| [Constants](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Constants) | Constants (v1) Math constants ( see EDataflowMathConstantsEnum ) |  |  |
| [Cube](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Cube) | Cube (v1) Cube ( A  *A*  A ) |  |  |
| [Divide](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Divide) | Divide (v1) Division (A / B) if B is equal to 0, 0 is returned Fallback value |  |  |
| [Exp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Exp) | Exp (v1) Exponential ( Exp(A) ) |  |  |
| [Floor](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Floor) | Floor (v1) Floor ( 1.4 => 1.0 | 1.9 => 1.0 | -5.3 => -6.0 ) |
| [Frac](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Frac) | Frac (v1) Frac ( 1.4 => 0.4 | 1.9 => 0.9 | -5.3 => 0.3 ) |
| [InverseSquareRoot](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/InverseSquareRoot) | InverseSquareRoot (v1) Inverse Square Root ( 1 / sqrt(A) ) if A is equal to 0, returns Fallback |  |  |
| [Log](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Log) | Log (v1) Natural log ( Log(A) ) |  |  |
| [LogX](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/LogX) | LogX (v1) Log for a specific base ( Log[Base](A) ) If base is negative or zero returns 0 |  |  |
| [Maximum](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Maximum) | Maximum (v2) Maximum ( Max(A, B, C, ... ) ) |  |  |
| [Minimum](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Minimum) | Minimum (v2) Minimum ( Min(A, B, C, ... ) ) |  |  |
| [Multiply](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Multiply) | Multiply (v1) Multiplication (A \* B) |  |  |
| [Negate](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Negate) | Negate (v1) Negate ( -A ) |  |  |
| [OneMinus](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OneMinus) | OneMinus (v1) One minus (1 - A) |  |  |
| [Pow](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Pow) | Pow (v1) power ( A ^ B) |  |  |
| [Reciprocal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Reciprocal) | Reciprocal (v1) Reciprocal( 1 / A ) if A is equal to 0, returns Fallback |  |  |
| [Round](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Round) | Round (v1) Round ( 1.4 => 1.0 | 1.9 => 2.0 | -5.3 => -5.0) |
| [Sign](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Sign) | Sign (v1) return -1, 0, +1 whether the input is respectively negative, zero or positive ( Sign(A) ) |  |  |
| [Square](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Square) | Square (v1) Square ( A \* A ) |  |  |
| [SquareRoot](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SquareRoot) | SquareRoot (v1) Square Root ( sqrt(A) ) |  |  |
| [Subtract](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Subtract) | Subtract (v1) Subtraction (A - B) |  |  |
| [Trunc](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Trunc) | Trunc (v1) Trunc ( 1.4 => 1.0 | 1.9 => 1.0 | -5.3 => -5.0) |

### Math|Transform

| Node | Description |
| --- | --- |
| [BakeTransformsInCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTransformsInCollection) | BakeTransformsInCollection (v1) Bake transforms in Collection Input(s) : Collection [Intrinsic] - Collection to bake transforms in Output(s): Collection [Passthrough] - Collection to bake transforms in |
| [BreakTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform) | BreakTransform (v1) Break a Transform into Translation, Rotation (Euler, Rotator, Quaternion), Scale Input(s) : Transform - Transform to break into components Output(s): Translation - Translation Rotation - Rotation as Euler Rotator - Rotation as a rotator Quat - Rotation as a quaternion Scale - Scale |
| [InvertTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/InvertTransform) | InvertTransform (v1) Invert a transform. |
| [MultiplyTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MultiplyTransform) | MultiplyTransform (v1) Description for this node |
| [TransformCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformCollection) | TransformCollection (v1) Transforms a Collection Input(s) : Collection [Intrinsic] - Output mesh TransformSelection - Transform selection for transforming Translate - Translation Rotate - Rotation Scale - Scale Output(s): Collection [Passthrough] - Output mesh |
| [TransformMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformMesh) | TransformMesh (v1) Transforms a mesh Input(s) : Mesh [Intrinsic] - Output mesh Translate - Translation Rotate - Rotation Scale - Scale UniformScale - Uniform scale ScalePivot - Pivot for the scale bInvertTransformation - Invert the transformation Output(s): Mesh [Passthrough] - Output mesh |

### Math|Trig

| Node | Description |
| --- | --- |
| [ArcCos](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcCos) | ArcCos (v1) ArcCos(A) returns a value in radians |
| [ArcSin](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcSin) | ArcSin (v1) ArcSin(A) returns a value in radians |
| [ArcTan](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcTan) | ArcTan (v1) ArcTan(A) returns a value in radians |
| [ArcTan2](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcTan2) | ArcTan2 (v1) ArcTan2(A, B) returns a value in radians |
| [Cos](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Cos) | Cos (v1) Cos(A) with A in radians |
| [DegToRad](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DegToRad) | DegToRad (v1) DegToRad(A) convert degrees to radians |
| [RadToDeg](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadToDeg) | RadToDeg (v1) RadToDeg(A) convert radians to degrees |
| [Sin](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Sin) | Sin (v1) Sin(A) with A in radians |
| [Tan](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Tan) | Tan (v1) Tan(A) with A in radians |

### Math|Utilities

| Node | Description |
| --- | --- |
| [IsNearlyZero](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/IsNearlyZero) | IsNearlyZero (v1) Is Nearly Zero Dataflow Node |

### Math|Vector

| Node | Description |
| --- | --- |
| [MakeQuaternion](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeQuaternion) | MakeQuaternion (v1) Make Quaternion Dataflow Node |
| [VectorArrayNormalize](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorArrayNormalize) | VectorArrayNormalize (v1) Normalize all the selected vectors in a VectorArray Input(s) : InVectorArray [Intrinsic] - Input VectorArray Selection - Selection for the operation |

### Math|Vectors

| Node | Description |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [AddVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddVector) | AddVector (v1) Add two vectors component wise : V = (A + B) Input(s) : A - A Vector operand B - B Vector operand Output(s): V - Add result V=A+B |  |  |  |  |  |  |  |  |
| [BreakVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector) | BreakVector (v1) Break a vector in 4 components if the input vector is of a lower dimension than 4, the remaining components will be set to zero Input(s) : V - Vector to break into components Output(s): X - X component Y - Y component Z - Z component W - W component |  |  |  |  |  |  |  |  |
| [DivideVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DivideVector) | DivideVector (v1) Multiply two vectors component wise: V = (A / B) When a component of B is zero, use the falback value as a return value for the specific component Input(s) : A - A Vector operand B - B Vector operand Fallback - Fallback Vector used when components of B are zero Output(s): V - Add result V=A\*B |  |  |  |  |  |  |  |  |
| [MakeVector2](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector2) | MakeVector2 (v1) Make a 2D Vector Input(s) : X - X component Y - Y component Output(s): Vector2D - 2D Vector {X, Y} |  |  |  |  |  |  |  |  |
| [MakeVector3](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector3) | MakeVector3 (v1) Make a 3D Vector Input(s) : X - X component Y - Y component Z - Z component Output(s): Vector3D - 3D Vector {X, Y, Z} |  |  |  |  |  |  |  |  |
| [MakeVector4](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector4) | MakeVector4 (v1) Make a 4D Vector Input(s) : X - X component Y - Y component Z - Z component W - W component Output(s): Vector4D - 4D Vector {X, Y, Z, W} |  |  |  |  |  |  |  |  |
| [MultiplyVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MultiplyVector) | MultiplyVector (v1) Multiply two vectors component wise: V = (A  *B) Input(s) : A - A Vector operand B - B Vector operand Output(s): V - Add result V=A*B |  |  |  |  |  |  |  |  |
| [NormalizeVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/NormalizeVector) | NormalizeVector (v1) Normalize a vector : Normalized = V/ | V | Input(s) : V - Vector to normalize Output(s): Normalized - Normalized vector : Normalized=V/ | V |  |  |  |  |  |
| [ScaleVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ScaleVector) | ScaleVector (v1) Scale a vector by a scalar : Scaled = (V  *Scale) Input(s) : V - Vector to scale Scale - Scale factor Output(s): Scaled - Scaled vector : Scaled=(V*  Scale) |  |  |  |  |  |  |  |  |
| [SubtractVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SubtractVector) | SubtractVector (v1) Subtract two vectors component wise: V = (A - B) Input(s) : A - A Vector operand B - B Vector operand Output(s): V - Add result V=A-B |  |  |  |  |  |  |  |  |
| [VectorCrossProduct](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorCrossProduct) | VectorCrossProduct (v1) Compute the cross product of two vectors : CrossProduct = B^A This node only operates in 3 dimensions, inputs will be converted to a 3D vector internally and result will be a vector with a zero W component Input(s) : A - A Vector operand B - B Vector operand Output(s): CrossProduct - Resulting cross product of A and B : CrossProduct=B^A |  |  |  |  |  |  |  |  |
| [VectorDistance](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorDistance) | VectorDistance (v1) Compute the distance between two vectors : Distance = | B-A | Input(s) : A - A Vector operand B - B Vector operand Output(s): Distance - Distance between A and B : Distance= | B-A |  |  |  |  |  |
| [VectorDotProduct](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorDotProduct) | VectorDotProduct (v1) Compute the dot product between two vectors : DotProduct = A.B Input(s) : A - A Vector operand B - B Vector operand Output(s): DotProduct - Resulting dot product : DotProduct=A.B |  |  |  |  |  |  |  |  |
| [VectorLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorLength) | VectorLength (v1) Compute the Length of a vector : Length = | V | Input(s) : V - Vector to get length from Output(s): Length - Length of the input vector : Length= | V |  |  |  |  |  |
| [VectorSquaredLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorSquaredLength) | VectorSquaredLength (v1) Compute the Squared length of a vector : Length = | V |  | V | Input(s) : V - Vector to get squared length from Output(s): SquaredLength - Length of the input vector : SquaredLength = | V |  | V |  |

### Mesh

| Node | Description |
| --- | --- |
| [GetMeshBoundingBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox) | GetMeshBoundingBox (v1) Get the local geometric bounding box a dynamic mesh Input(s) : Mesh - dynamic mesh to compute the bouning box from Output(s): BoundingBox - Geometric bounding box of the input dynamic mesh Center - Center of the resulting bounding box Dimensions - Dimensions of the resulting bounding box in centimers |

### Mesh|Utilities

| Node | Description |
| --- | --- |
| [AppendMeshesToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendMeshesToCollection) | AppendMeshesToCollection (v1) Append Array of Meshes to Collection Input(s) : Collection [Intrinsic] - Meshes will be appended to this collection Meshes - Dynamic Meshes to append ParentIndex - Index of parent bone for appended meshes. |
| [ApplyGeometryScriptToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyGeometryScriptToCollection) | ApplyGeometryScriptToCollection (v1) Apply a Geometry Script Mesh Processors to the geometry of selected transforms in a geometry collection Input(s) : Collection [Intrinsic] - Input/Output mesh TransformSelection - Selected bones will have geometry script processing applied (if they have geometry). |
| [ApplyGeometryScriptToMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyGeometryScriptToMesh) | ApplyGeometryScriptToMesh (v1) Apply a Geometry Script Mesh Processors to an input UDynamicMesh Input(s) : Mesh [Intrinsic] - Input/Output mesh Output(s): Mesh [Passthrough] - Input/Output mesh |
| [BoxToMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxToMesh) | BoxToMesh (v1) Converts a BoundingBox into a DynamicMesh Input(s) : Box [Intrinsic] - BoundingBox input Output(s): Mesh - Mesh output TriangleCount - Mesh triangle count |
| [CollectionSelectionToMeshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionToMeshes) | CollectionSelectionToMeshes (v1) Converts a Collection to a set of Dynamic Meshes per selected Transform Input(s) : Collection [Intrinsic] - Collection to convert TransformSelection - Geometry on or under selected bones will be converted to meshes, optionally after filtering the selection to leaves. |
| [CollectionToMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToMesh) | CollectionToMesh (v1) Converts a Collection to a DynamicMesh Input(s) : Collection [Intrinsic] - Collection to convert TransformSelection - Geometry on or under selected bones will be appended to the output mesh. |
| [DataflowMeshAppend](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DataflowMeshAppend) | DataflowMeshAppend (v1) Combine two Dataflow meshes Input(s) : Mesh [Intrinsic] - Mesh input/output AppendMesh [Intrinsic] - Mesh to append Output(s): Mesh [Passthrough] - Mesh input/output |
| [DuplicateMeshUVChannelNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode) | DuplicateMeshUVChannelNode (v1) Create a new UV layer/channel in a UDataflowMesh Input(s) : Mesh [Intrinsic] - DataflowMesh input/output Output(s): Mesh [Passthrough] - DataflowMesh input/output NewUVChannel - Index of the added UV channel |
| [GetMeshData](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshData) | GetMeshData (v1) Outputs Mesh data Input(s) : Mesh [Intrinsic] - Mesh for the data Output(s): VertexCount - Number of vertices EdgeCount - Number of edges TriangleCount - Number of triangles |
| [MakeDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeDataflowMesh) | MakeDataflowMesh (v1) Create a UDataflow mesh from an input UDynamicMesh and material array Input(s) : InMesh [Intrinsic] - DynamicMesh input InMaterials [Intrinsic] - Materials input Output(s): Mesh - DataflowMesh output |
| [MeshAppend](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshAppend) | MeshAppend (v1) Appends two meshes Input(s) : Mesh1 [Intrinsic] - Mesh input Mesh2 [Intrinsic] - Mesh input Output(s): Mesh - Output mesh |
| [MeshBoolean](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshBoolean) | MeshBoolean (v1) Compute a Mesh Boolean between Mesh1 and Mesh2 Supported Boolean Operations: Union (Mesh1 + Mesh2) Difference (Mesh1 - Mesh2; removing what's inside of Mesh2 from Mesh1) Intersection (Mesh1 & Mesh2; removing what's outside of Mesh2 from Mesh1) Input(s) : Mesh1 [Intrinsic] - Mesh input Mesh2 [Intrinsic] - Mesh input Output(s): Mesh - Output mesh |
| [MeshInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshInfo) | MeshInfo (v1) Collects information from the DynamicMesh and outputs it into a formatted string Input(s) : Mesh [Intrinsic] - DynamicMesh for the information Output(s): InfoString - Formatted output string |
| [MeshToCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshToCollection) | MeshToCollection (v1) Converts a DynamicMesh to a Collection Input(s) : Mesh [Intrinsic] - DynamicMesh to convert bSplitIslands - Whether to split the mesh into multiple bones based on the mesh connectivity bAddClusterRootForSingleMesh - Whether to add a root cluster for the single mesh case. |
| [PointsToMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PointsToMesh) | PointsToMesh (v1) Converts points into a DynamicMesh Input(s) : Points [Intrinsic] - Points input Output(s): Mesh - Mesh output TriangleCount - Mesh triangle count |
| [ScatterMeshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ScatterMeshes) | ScatterMeshes (v1) Copies the same mesh with scale onto points Input(s) : Points [Intrinsic] - Points to copy meshes onto MeshToCopy [Intrinsic] - Mesh to copy onto points Output(s): Mesh - merged result mesh Meshes - Result meshes as individual ones |
| [SkeletalMeshToMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshToMesh) | SkeletalMeshToMesh (v1) Experimental Converts a SkeletalMesh into a DynamicMesh with Imported Vertex information Input(s) : SkeletalMesh - SkeletalMesh to convert Output(s): Mesh - Output mesh MaterialArray - Output materials |
| [SplitDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SplitDataflowMesh) | SplitDataflowMesh (v1) Split a UDataflow mesh into a UDynamicMesh and a material array Input(s) : InMesh [Intrinsic] - DataflowMesh input Output(s): Mesh - DyanmicMesh output MaterialArray - Materials output |
| [SplitMeshIslands](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SplitMeshIslands) | SplitMeshIslands (v1) Split a mesh into a connected islands Input(s) : Mesh [Intrinsic] - Mesh input Output(s): Meshes - Meshes output |
| [StaticMeshToMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshToMesh) | StaticMeshToMesh (v1) Converts a StaticMesh into a DynamicMesh Input(s) : StaticMesh - StaticMesh to convert Output(s): Mesh - Output mesh MaterialArray - Output materials |

### MeshResizing

| Node | Description |
| --- | --- |
| [AlignUVMeshNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AlignUVMeshNode) | AlignUVMeshNode (v1) Experimental Align UVMesh Node Input(s) : BaseUVChannelIndex - Base UV channel index in case it differs from the ResizingMesh UV channel index, or -1 to use the same channel. |
| [ApplyRBFResizing](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing) | ApplyRBFResizing (v1) Experimental Apply the interpolation data calculated by GenerateRBFResizingWeights to resize a mesh. |
| [GenerateInterpolatedProxy](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy) | GenerateInterpolatedProxy (v1) Experimental Generate a pair of Dynamic Meshes with the same topology that can be interpolated. |
| [GenerateRBFResizingWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights) | GenerateRBFResizingWeights (v1) Experimental Sample points and generate RBF Interpolation data for a given Source mesh. |
| [GenerateResizableProxy](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateResizableProxy) | GenerateResizableProxy (v1) Experimental Generate a pair of Dynamic Meshes with the same topology that can be interpolated. |
| [GrowTileRegion](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion) | GrowTileRegion (v1) Experimental Finds a square tile within a specified image region and duplicates it over the whole image. |
| [MeshConstrainedDeformationTestPlayground](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground) | MeshConstrainedDeformationTestPlayground (v1) Experimental Mesh Constrained Deformation Node |
| [MeshWarp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWarp) | MeshWarp (v1) Experimental Mesh Warp Node |
| [MeshWrap](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap) | MeshWrap (v1) Experimental Dataflow node for wrapping one mesh's topology to another mesh's shape. |
| [MeshWrapLandmarks](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrapLandmarks) | MeshWrapLandmarks (v1) Experimental Node for defining landmarks used by MeshWrapNode. |
| [UVMeshTransformNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UVMeshTransformNode) | UVMeshTransformNode (v1) Experimental UVMesh Transform Node |
| [UVResizeController](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UVResizeController) | UVResizeController (v1) Experimental UV Resizing logic. |
| [UVUnwrapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UVUnwrapNode) | UVUnwrapNode (v1) Experimental UVUnwrap Node |

### Outfit

| Node | Description |
| --- | --- |
| [ExtractBodyPartsArrayFromBodySizeParts](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractBodyPartsArrayFromBodySizeParts) | ExtractBodyPartsArrayFromBodySizeParts (v1) Experimental Extract the array of BodyParts from a FChaosOutfitBodySizeBodyParts Input(s) : BodySizeParts - The source outfit. |
| [FilterSizedOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit) | FilterSizedOutfit (v1) Experimental Select a single size for the passed Outfit and filter out all non matching sizes. |
| [GetClothAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetClothAsset) | GetClothAsset (v1) Experimental Get a cloth asset object into the graph. |
| [GetOrMakeOutfitFromAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOrMakeOutfitFromAsset) | GetOrMakeOutfitFromAsset (v1) Experimental Extract the Outfit from an Outfit Asset. |
| [GetOutfitAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitAsset) | GetOutfitAsset (v1) Experimental Get an outfit asset object into the graph. |
| [GetOutfitBodyParts](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitBodyParts) | GetOutfitBodyParts (v1) Experimental Extract the Body Part Skeletal Meshes from an Outfit. |
| [GetOutfitClothCollections](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections) | GetOutfitClothCollections (v1) Experimental Extract the cloth collections contained into the specified source outfit. |
| [GetOutfitRBFInterpolationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData) | GetOutfitRBFInterpolationData (v1) Experimental Extract the Body Part RBF Interpolation Data from an outfit. |
| [MakeOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeOutfit) | MakeOutfit (v1) Experimental Add multiple cloth asset objects to an outfit collection. |
| [MakeSizedOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSizedOutfit) | MakeSizedOutfit (v1) Experimental Add multiple cloth asset objects to an outfit collection. |
| [MergeOutfits](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeOutfits) | MergeOutfits (v1) Experimental Merge multiple outfits into a single outfits. |
| [OutfitAssetTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitAssetTerminal) | OutfitAssetTerminal (v1) Experimental Outfit terminal node to generate an outfit asset from several cloth assets. |
| [OutfitQuery](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery) | OutfitQuery (v1) Query an Outfit about its properties. |
| [SetOutfitClothCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetOutfitClothCollection) | SetOutfitClothCollection (v1) Experimental Replace the ClothCollection in an Outfit with a new one. |

### Physics|Common

| Node | Description |
| --- | --- |
| [GetSimulationTime](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSimulationTime) | GetSimulationTime (v1) Get the context simulation time Output(s): SimulationTime - Simulation time property coming from the context |

### Physics|Proxy

| Node | Description |
| --- | --- |
| [FilterSimulationProxies](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies) | FilterSimulationProxies (v1) Filter simulation proxies from context Input(s) : SimulationProxies - Simulation proxies coming from the context and filtered with the groups Output(s): FilteredProxies - Simulation proxies coming from the context and filtered with the groups |

### Physics|Solver

| Node | Description |
| --- | --- |
| [AddSolverDeformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer) | AddSolverDeformer (v1) Add a graph deformer to the groom simulation Input(s) : PhysicsSolvers - Physics solvers to advance in time SimulationTime - Delta time to use to advance the solver Output(s): PhysicsSolvers [Passthrough] - Physics solvers to advance in time |
| [AdvancePhysicsSolvers](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AdvancePhysicsSolvers) | AdvancePhysicsSolvers (v1) Advance the simulation physics solver in time Input(s) : SimulationTime - Delta time to use to advance the solver PhysicsSolvers - Physics solvers to advance in time Output(s): PhysicsSolvers [Passthrough] - Physics solvers to advance in time |
| [GetPhysicsSolvers](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetPhysicsSolvers) | GetPhysicsSolvers (v1) Get physics solvers from context Output(s): PhysicsSolvers - Physics solvers coming from the context and filtered with the groups |

### PointSampling

| Node | Description |
| --- | --- |
| [FilterPointsWithMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh) | FilterPointsWithMesh (v1) Filter a point set to only the points inside or outside of a given mesh Input(s) : TargetMesh [Intrinsic] - Mesh to use to filter point set bKeepInside - Whether to keep the points inside or (if false) outside the mesh, when filtering by Winding Number. |
| [NonUniformPointSampling](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/NonUniformPointSampling) | NonUniformPointSampling (v1) NonUniform Sampling on a DynamicMesh Input(s) : TargetMesh [Intrinsic] - Mesh to sample points on SamplingRadius - Desired "radius" of sample points. |
| [UniformPointSampling](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling) | UniformPointSampling (v1) Uniform Sampling on a DynamicMesh Input(s) : TargetMesh [Intrinsic] - Mesh to sample points on SamplingRadius - Desired "radius" of sample points. |
| [VertexWeightedPointSampling](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VertexWeightedPointSampling) | VertexWeightedPointSampling (v1) VertexWeighted Sampling on a DynamicMesh Input(s) : TargetMesh [Intrinsic] - Mesh to sample points on VertexWeights [Intrinsic] - Weight array SamplingRadius - Desired "radius" of sample points. |

### Selection|Utility

| Node | Description |
| --- | --- |
| [SelectionToVertexList](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToVertexList) | SelectionToVertexList (v1) Selection to Vertex List Dataflow Node |

### SphereCovering

| Node | Description |
| --- | --- |
| [Get Sphere Covering Sphere Count](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSphereCoveringSphereCount) | Get Sphere Covering Sphere Count (v1) Report the number of spheres in a sphere covering Input(s) : SphereCovering [Intrinsic] - The sphere covering to evaluate Output(s): NumSpheres - Number of spheres in the sphere covering |

### Static Mesh

| Node | Description |
| --- | --- |
| [GetStaticMeshBoundingBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetStaticMeshBoundingBox) | GetStaticMeshBoundingBox (v1) Get the local geometric bounding box a static mesh Input(s) : StaticMesh - Static Mesh to compute the bouning box from Output(s): BoundingBox - Geometric bounding box of the input Static Mesh Center - Center of the resulting bounding box Dimensions - Dimensions of the resulting bounding box in centimers |

### SubGraph

| Node | Description |
| --- | --- |
| [GetCurrentIndex](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCurrentIndex) | GetCurrentIndex (v1) Get the current index in a subgraph This is to be used in subgraph when iterating over an array |
| [SubGraphCall](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphCall) | SubGraphCall (v1) Call a subgraph |
| [SubGraphInput](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphInput) | SubGraphInput (v1) This node represent the inputs of a dataflow subgraph |
| [SubGraphOutput](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphOutput) | SubGraphOutput (v1) This node represent the Outputs of a dataflow subgraph |

### Terminal

| Node | Description |
| --- | --- |
| [CurveSamplingAnimationAssetTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal) | CurveSamplingAnimationAssetTerminal (v1) \* terminal node to create an animation asset for muscle activation MLD training. |
| [FleshAssetTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FleshAssetTerminal) | FleshAssetTerminal (v1) Flesh Asset Terminal Dataflow Node |
| [GeometryCollectionTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionTerminal) | GeometryCollectionTerminal (v2) \* Geometry Collection asset terminal node Input(s) : Materials - Materials to set on this asset InstancedMeshes - array of instanced meshes Output(s): Materials [Passthrough] - Materials to set on this asset InstancedMeshes [Passthrough] - array of instanced meshes |
| [SkeletonAssetTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletonAssetTerminal) | SkeletonAssetTerminal (v1) \* Dataflow terminal node to save a skeleton asset Input(s) : SourceSkeleton - Source Skeleton used to override the skeleton asset SkeletonAsset - Skeleton Asset to be saved |
| [TextureTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TextureTerminal) | TextureTerminal (v1) \* terminal node to a save a dependent 2D texture |

### Terminal|Proxy

| Node | Description |
| --- | --- |
| [SimulationProxiesTerminal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationProxiesTerminal) | SimulationProxiesTerminal (v1) Main terminal node for simulation proxies Input(s) : SimulationProxies - Physics solvers to evaluate |

### Utilities

| Node | Description |
| --- | --- |
| [UnionIntArrays](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UnionIntArrays) | UnionIntArrays (v1) Union Int Arrays Dataflow Node |

### Utilities|Array

| Node | Description |
| --- | --- |
| [BoolArrayToFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoolArrayToFaceSelection) | BoolArrayToFaceSelection (v1) Converts a TArray to a FDataflowFaceSelection Input(s) : BoolAttributeData [Intrinsic] - TArray data |
| [ConvertToArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertToArray) | ConvertToArray (v1) convert a single element to an array Input(s) : Element - Element to convert to an array Output(s): Array - Array to Convert to |
| [FloatArrayComputeStatistics](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics) | FloatArrayComputeStatistics (v1) Computes statistics of a float array Input(s) : FloatArray [Intrinsic] - Array to compute values from TransformSelection - TransformSelection describes which values to use, if not connected all the elements will be used Output(s): Value - Computed value Indices - Indices of elements with the computed value |
| [FloatArrayToVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToVertexSelection) | FloatArrayToVertexSelection (v1) Converts a TArray to a FDataflowVertexSelection Input(s) : FloatArray [Intrinsic] - TArray array |
| [GetArrayElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetArrayElement) | GetArrayElement (v1) Get an element from an array Input(s) : Array [Intrinsic] - Array to get the element from Index - Index to get the element at Output(s): Array [Passthrough] - Array to get the element from Element - Element from the array at the specified index |
| [GetArraySize](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetArraySize) | GetArraySize (v1) Get size of an array Input(s) : Array [Intrinsic] - Array to get size from Output(s): Size - Computed value |
| [MakeManagedArrayCollectionArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray) | MakeManagedArrayCollectionArray (v1) Append an element to an array of ManagedArrayCollections. |
| [RandomizeFloatArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomizeFloatArray) | RandomizeFloatArray (v1) Randomize elements in a float array (Random value will be in (RandomRangeMin, RandomRangeMax) Input(s) : FloatArray [Intrinsic] - Array to randomize RandomRangeMin - Random range min RandomRangeMax - Random range max RandomSeed - Seed for random Output(s): FloatArray [Passthrough] - Array to randomize |
| [RemoveFloatArrayElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveFloatArrayElement) | RemoveFloatArrayElement (v1) Removes the specified element from an array Input(s) : FloatArray [Intrinsic] - Array to remove the element from Output(s): FloatArray [Passthrough] - Array to remove the element from |

### Utilities|Box

| Node | Description |
| --- | --- |
| [BreakBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakBox) | BreakBox (v1) Description for this node |
| [GetBoxLengths](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoxLengths) | GetBoxLengths (v1) Create an array of lengths of bounding boxes (measured along an axis, diagonal, or the max/min axes) from an array of bounding boxes |
| [GetCollectionBoundingBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionBoundingBox) | GetCollectionBoundingBox (v1) Get the geometric bounding box a collection in collection space Input(s) : Collection - Collection to compute the bouning box from Output(s): BoundingBox - Geometric bounding box of the input collection Center - Center of the resulting bounding box Dimensions - Dimensions of the resulting bounding box in centimers |

### Utilities|FlowControl

| Node | Description |
| --- | --- |
| [BranchCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchCollection) | BranchCollection (v1) Branch between two Managed Array Collections based on Boolean condition Input(s) : TrueCollection - Collection input for the 'true' case FalseCollection - Collection input for the 'false' case Output(s): ChosenCollection - Output Collection |
| [BranchFloat](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchFloat) | BranchFloat (v1) Branch between two float inputs based on boolean condition Input(s) : A - Float input B - Float input Output(s): ReturnValue - Output |
| [BranchInt](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchInt) | BranchInt (v1) Branch between two int inputs based on boolean condition Input(s) : A - Int input B - Int input Output(s): ReturnValue - Output |
| [BranchMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh) | BranchMesh (v1) Branch between two mesh inputs based on boolean condition Input(s) : MeshA - Mesh input MeshB - Mesh input Output(s): Mesh - Output mesh |

### Utilities|Sphere

| Node | Description |
| --- | --- |
| [BoundingSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoundingSphere) | BoundingSphere (v1) Description for this node |
| [BreakBoundingSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakBoundingSphere) | BreakBoundingSphere (v1) Expands data of FSphere |

### Utilities|String

| Node | Description |
| --- | --- |
| [HashString](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/HashString) | HashString (v1) Generates a hash value from a string Input(s) : String - String to hash Output(s): Hash - Generated hash value |
| [MakeLiteralString](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralString) | MakeLiteralString (v2) Make a literal string |
| [StringAppend](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StringAppend) | StringAppend (v2) Concatenates strings together to make a new string |

### Utilities|Vector

| Node | Description |
| --- | --- |
| [BreakVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector) | BreakVector (v1) Expands a Vector into X, Y, Z components |
| [HashVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/HashVector) | HashVector (v1) Generates a hash value from a vector Input(s) : Vector - Vector to hash Output(s): Hash - Generated hash value |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference.md

# Unreal Engine Node References

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference

> Application Version: 5.7

## Overview

Unreal Engine provides several different node-based visual scripting tools to help you perform various tasks directly within the Unreal Editor. Below is a table of various node references available for you to use in the Unreal Editor.

## Node References

| Reference | Summary |
| --- | --- |
| [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig) | Suite of animation tools to rig and animate characters. |
| [Dataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow) | Node-based procedural asset generation environment. |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\nodes-in-unreal-engine.md

# Nodes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nodes-in-unreal-engine

> Application Version: 5.7

**Nodes** are objects such as events, function calls, flow control operations, variables, and so on that can be used in graphs to define the functionality of the particular graph and Blueprint that contains it.

## Working with Nodes

Each type of node performs a unique function; however, the way in which nodes are created and used is common to all nodes. This helps to make for an intuitive experience when creating node graphs.

### Placing Nodes

New nodes are added to a graph by selecting the type of node from the **Context menu**. The node types listed in the context menu depend on the manner in which the list is accessed and what is currently selected.

* **Right-clicking** on an empty space in the **Graph Editor** tab brings up a list of all nodes that can be added to the graph. If an Actor is selected, events supported by that type of Actor are also listed.

  ![Blueprint Context Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e763751-ed1f-4082-84b2-bb1272ab950b/k2_context.png)
* Dragging a connection from a pin on a node and releasing in empty space brings up a list of nodes compatible with the type of pin the connection originated from.

  ![Blueprint New Connection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/94666e30-61bf-4ab6-8787-2601f47f5b39/k2_connection_new.png)![Blueprint Context Menu - Pin Specific](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f97975a-7e1c-429f-84f4-63b28c1087e5/k2_context_compat.png)

### Selecting Nodes

Nodes are selected by clicking on the node in the **Graph Editor** tab.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4ed180e-4c13-4fe4-88f1-b60751b73759/selectnode.jpg)

A node can be added to, or removed from, the current selection by holding **Ctrl** and clicking on the node.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/abc8c637-65f6-4b75-bd72-d08663aa678e/varmessage.jpg)

Multiple nodes can be selected at once by clicking and dragging to create a marquee selection. Holding **Ctrl** + clicking and dragging creates a marquee selection that toggles selection. Holding **Shift** + clicking and dragging creates a marquee selection that adds to the current selection.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/62fd2f8f-fda2-426c-ae92-edf983ef7ddd/dotboxspawnemitter.jpg)

To deselect all nodes, simply click in an empty space of the **Graph Editor** tab.

### Moving Nodes

A node is moved by clicking on the node and dragging. If multiple nodes are selected, clicking on any node in the selection and dragging will move all of the nodes.

![Blueprint Moving Nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6bd1b5f5-0071-4553-8ea0-b0363f331cf0/k2_move.png)

### Pins

Nodes can have pins on either side. Pins on the left are input pins, while those on the right of the node are outputs.

![Blueprint Input and Output Pins](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16b664e9-447f-4525-ac64-fbdc991f51ae/k2_pins.png)

There are two main types of pins: execution pins and data pins.

#### Execution Pins

![Blueprint Exec Pins](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a73129f-ddc3-4f7f-9129-f0c8745dfd7f/k2_pins_exec.png)

**Execution pins** are used to connect nodes together to create a flow of execution. When an input execution pin is activated, the node is executed. Once execution of the node completes, it activates an output execution pin to continue the flow of execution. Execution pins are displayed as an outline when not wired, and solid when wired to another execution pin. Function Call nodes always have only a single input execution pin and a single output execution pin as functions only have one entry point and one exit point. Other types of nodes can have multiple input and output execution pins, allowing for different behavior dependent on which pin is activated.

#### Data Pins

![Blueprint Data Pin Types](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/344eb741-1c42-47ca-a70b-ce50b461f556/k2_pins_data_types.png)

**Data pins** are used for taking data into a node or outputting data from a node. Data pins are type-specific and can be wired to variables of the same type (which have data pins of their own) or a data pin of the same type on another node. Like execution pins, data pins are displayed as an outline when not wired to anything, and solid when wired.

![Blueprint Data Pins](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0be1b31f-1e55-4353-ab2b-e76bd67d9317/k2_pins_data.png)

Nodes can have any number of input or output data pins. The data pins of a Function Call node correspond to the parameters and return value of the corresponding function.

#### Auto-Casting

Connections can be made between certain pins of different data types by way of the auto-casting feature in Blueprints. Compatible types can be identified by the tooltip displayed when attempting to create a connection between two pins.

![Blueprint - Compatible Types Message](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84b7b5a3-51c0-40de-a46f-0e4c52217ef3/k2_autocast_message.png)

Dragging a wire from a pin of one type to a pin of a different, but compatible, type will cause an **autocast** node to be created with wires to both pins.

![Blueprint - Autocast Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a10810f5-efb4-4742-89d5-8db3726e57b0/k2_autocast_node.png)

#### Promote to Variable

The value represented by a data pin can be converted to a variable within the Blueprint using the **Promote to Variable** command. This command creates a new variable in the Blueprint and wires it to the data pin being promoted. In the case of an output data pin, a Set node is used to set the value of the new variable. Essentially, this is just a shortcut to manually adding a new variable, adding it to the graph and wiring it to the data pin.

You can also create variables by using **Promote to Variable**.

Right-click any input or output data pins on a Blueprint node and select **Promote to Variable**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0522186-18ed-4c7b-9684-78127ca71b3c/ht38.png)

By right-clicking the **New Light Color** pin and selecting **Promote to Variable**, we can assign a variable as the **New Light Color** value.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8ebdce8-c600-4194-921d-fc234400a347/ht40.png)

Alternatively, you can drag off an input or output pin and select **Promote to Variable**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/152ef092-0115-4120-b10f-0c4b212ed3bb/ht39.png)

### Wires

Connections between pins are called **Wires**. Wires can represent either the flow of execution or the flow of data.

#### Execution Wires

Wires between exec pins represent the flow of execution. Exec wires are displayed as white arrows spanning from an output exec pin to an input exec pin. The direction of the arrow indicates the flow of execution.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/15b74246-1f6b-4d1b-989d-47140dbe2032/selectnode.jpg)

Exec wires produce a visual indicator when being executed. During play, as one node completes execution and the next is activated, the wire between their execution pins highlights the fact that execution is being transferred from one node to another.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/90248d73-dbfd-4b58-9c1c-8d153c2cdaf9/k2_flow_exec.jpg)

The visual indicator for an exec wire fades away over time.

#### Data Wires

Data wires connect one data pin to another data pin of the same type. They are displayed as colored arrows and are used to visualize the transfer of data, with the direction of the arrow representing the direction the data is traveling. The color of a data wire is dependent upon the type of data, just as the color of the data pins.

![Blueprint Data Wire](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c583d5a-8afb-4033-93ba-6a7530e6e3bd/k2_flow_data.png)

#### Working with Wires

Wires are created in the **Graph Editor** tab using one of the methods below:

* Click on one pin and drag and release on another pin of the same type to create a direct connection.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/65f56836-1c5c-412a-b528-54f81cac7d4e/hovercheck.jpg)

  The connection can only be made between two compatible types of pins. If you drag a connection on to a pin that is not compatible, an error will be displayed informing you the connection cannot be made.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e889331-fb84-4d16-9478-47a45454518e/hovercheckno.jpg)
* Drag a connection from a pin and release in an empty space to summon a context-sensitive menu that lists all the nodes that are compatible with the type of pin the connection originated from. Selecting a node from this list creates a new instance of that node and makes a connection to a compatible pin on the new node.

  ![Blueprint Wire Creation - New Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e199fc6-d13c-40f1-b85d-77dc52d131c7/k2_connection_new.png)
  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a71a6ab-1f17-45fe-8a51-11ed92ac10a2/connectednodes.jpg)

  A wire between two pins can be broken using one of the methods below:
* **Alt + Click** on one of the connected pins.
* **Right-click** on one of the connected pins and choose Break Link(s).

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0a85b22-446c-4cbb-bd4d-d2c8a18b031a/breaklinknode.jpg)

### Collapsed Graphs

Collections of nodes in the graph can be collapsed into sub-graphs for organizational purposes. This creates a hierarchy of graphs and allows large or complex portions of a graph to be viewed as a single node in the parent graph, with inputs and outputs, while still being able to edit the contents of the collapsed graph.



Unlike macros, a set of collapsed nodes is not shared, even within a single Level Blueprint or Blueprint Class. If you copy the collapsed node, it duplicates the internal graph. This can be handy if you want to make several variants of the same approximate behavior, but it also means that any bug fixes would have to be applied to each copy. The feature is really more intended to 'tidy up' a graph, hiding complexity inside, rather than any sort of sharing or reuse.

#### Tunnels

The collapsed graph uses tunnel nodes to communicate and interact externally with the graph that contains it.

The **Inputs** tunnel node acts as the entry point into the collapsed graph. It contains the execution and data pins that correspond to the input pins on the collapsed graph node in the parent graph.

![Blueprint Tunnel Entrance Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/396d71eb-6f34-4432-92d6-f34e3d9d9e12/k2_tunnel_entrance.png)

The **Outputs** tunnel node acts as the exit point of the collapsed graph. It contains the execution and data pins corresponding to the output pins of the collapsed graph node in the parent sequence.

![Blueprint Tunnel Exit Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44c32b28-59f1-406e-b574-5055f7d41733/k2_tunnel_exit.png)

These pins are automatically generated when the nodes are collapsed. Any execution or data wires connected to pins on the first node in the sequence causes a corresponding pin to be created on the **Inputs** tunnel node which appear on the collapsed graph node in the parent sequence as input pins. Similarly, any execution or data wires connected to the last node in the sequence cause corresponding pins to be generated on the **Outputs** tunnel node, and thus as pins on the collapsed graph node in the parent sequence.

#### To Collapse a Collection of Nodes

1. Select the nodes to be collapsed in the graph by clicking and dragging a marquee selection box around them or **Ctrl + Clicking** on each node.
2. **Right-click** on one of the nodes and choose **Collapse Nodes**.

   ![Blueprint Collapse Nodes - Menu Option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dc07c358-6a70-49d7-b4f3-60827028df5e/k2_collapse_menu.png)
3. Enter a name for the collapsed graph in the text field of the new node that appears and press **Enter**.

   ![Blueprint Collapse Nodes - Graph Name](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/773ba9c7-f03e-4c9d-b7cf-d3eede63e404/k2_collapse_name.png)
4. The collapsed graph is now displayed as a single node, and a reference to the collapsed graph appears in the **My Blueprint** tab.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25adbe03-1b1c-45c5-82fb-188ea4e6a197/collapsed_graph_myblueprint.png)
5. To edit the collapsed nodes, **Double-click** the collapsed graph node or select the sub-graph in the **My Blueprint** tab.

#### To Expand a Collapsed Graph:

1. **Right-click** on a collapsed graph node and choose **Expand Node**.

   ![Blueprint Expand Node - Menu Option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b092e024-76ff-43c8-8269-28251a5a7b04/k2_expand_menu.png)
2. The collapsed graph node is replaced by the nodes it contained and is no longer present in the **My Blueprint** tab graph hierarchy.

   ![Blueprint Expand Node - Resulting Nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72d5e072-c581-4c13-9b9c-7c03e002cbca/k2_expand_graph.png)

---

## Fuente: .\docs-md-py\en-us\unreal-engine\normal-calculation-methods-with-the-proxy-geometry-tool-in-unreal-engine.md

# Normal Calculation Methods

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/normal-calculation-methods-with-the-proxy-geometry-tool-in-unreal-engine

> Application Version: 5.7

The Proxy Geometry tool will allow you to specify which method should be used when computing the Vertex Normals of a given Static Mesh. In the following How-To we will take a look at how you can change the Vertex Normal calculation method and the effect that will have on your generated Static Meshes.

## Steps

In the following section, we will take a look at how you can adjust the method that is used to calculate the Normals that are used for a Static Mesh.

1. First, locate a Static Mesh or group of Static Meshes that you want to generate new geometry for and select the Mesh or Meshes inside the Viewport.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5230fc54-8d11-4cc2-8f03-80f43512e3ad/normalcalculationmethod_02.png "NormalCalculationMethod_02.png")
2. Next, open the **Merge Actor** tool by going to **Window > Developer Tools > Merge Actors**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de0d6991-8878-4a30-807f-3a477fe233c3/gapfilling_02.png "GapFilling_02.png")
3. In the Merge Actor tool, click the **second icon** to access the **Proxy Geometry** tool and then expand the **Proxy Settings**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6f8fe1b-927a-4e7b-a8ce-b844c47b3373/normalcalculationmethod_03.png "NormalCalculationMethod_03.png")
4. Set the **Screen Size** value to **50** and make sure that the **Normal Calculation Method** is set to **Angle Weighted**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c7624d2-9637-4af5-903c-2dd20dd5f016/normalcalculationmethod_04.png "NormalCalculationMethod_04.png")

   By setting the Screen Size to a value of 50 we are telling the Proxy Geometry tool to reduce the amount of triangles used in the selected Static Mesh.
5. Next, click the **Merge Actors** button and input a name and location in the **Content Browser** for the newly created Static Mesh. Then click the **Save** button to start the merging process.
6. Once that has completed, double-click the Static Mesh to open it in the **Static Mesh Editor**, where you can see the results.

## End Results

Getting the best results is going to take some time and iteration as each object could require a different Normal Calculation Method to achieve the desired results. The results can also be very subtle depending on the type of object that you are using. The following image comparison shows how the Static Mesh used in this example looks when the Normal Calculation Method is set to Angle Weighted, Area Weighted and Equal Weighted.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ecc3f82-a7a0-422b-b76e-f7c95aa44976/angleweighted.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdd8c9b8-94fa-4dce-bfc4-bef374435502/areaweighted.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27b3f0e6-600d-42ed-8875-891faced811a/equalweighted.png)

The following image slider shows the results that each of the three Normal Calculation Methods can achieve. First you will see  Angle Weighted then Area Weighted and finally Equal Weighted.

---

## Fuente: .\docs-md-py\en-us\unreal-engine\nvidia-nsight-aftermath-for-gpu-pipeline-debugging-in-unreal-engine.md

# NVIDIA Nsight Aftermath for GPU Pipeline Debugging

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nvidia-nsight-aftermath-for-gpu-pipeline-debugging-in-unreal-engine

> Application Version: 5.7

Unreal Engine supports NVIDIA's **Nsight™ Aftermath** C++ library for Windows-based developers, which provides additional data from NVIDIA GeForce-based GPUs after a crash occurs. This data contains crucial information about what the GPU was doing when the crash occurred, enabling you to track down what's happening with the GPU in your own projects.

Aftermath is a lightweight tool that is unobtrusive and reduces the performance footprint needed by some debugging tools. In fact, it's lightweight enough that it can even ship with finished games to provide the data you need from your customers' machines. Aftermath enables programmers to insert markers into their code that assist in tracking the root causes of crashes. This is now being used in the Unreal Engine Editor to track down and fix reported or captured issues.

For additional information and how to use it in your own project, visit [NVIDIA's Nsight™ Aftermath documentation](https://developer.nvidia.com/nvidia-aftermath) page.

## Enabling NVIDIA Nsight™ Aftermath

Add the following console variable to your `ConsoleVariables.ini` configuration file to enable NVIDIA Nsight™ Aftermath in your project:tion file:

```
	r.GPUCrashDebugging=1
```

Or, you can enable it by passing it as a command line argument:

```
	-gpucrashdebugging
```

## Logs

Once you've enabled NVIDIA Aftermath, you should see the following output in your log:

```
	LogD3D11RHI: [Aftermath] Aftermath enabled and primed
```

You can access your log in Unreal Engine 4 by going to **File Menu > Window > Developer Tools > Output Log** or by opening the log text file from your project folder.

When a crash happens, the log displays something similar to:

```
	LogD3D11RHI: Error: Result failed at X:[Project Folder]\Engine\Source\Runtime\Windows\D3D11RHI\Private\D3D11Viewport.cpp:290 with error DXGI_ERROR_DEVICE_REMOVED DXGI_ERROR_DEVICE_HUNG
	LogRHI: Error: [Aftermath] Status: Timeout
	LogRHI: Error: [Aftermath] GPU Stack Dump
	LogRHI: Error: [Aftermath] 0: Frame2769
	LogRHI: Error: [Aftermath] 1: FRAME
	LogRHI: Error: [Aftermath] 2: Scene
	LogRHI: Error: [Aftermath] 3: ComputeLightGrid
	LogRHI: Error: [Aftermath] 4: Compact
	LogRHI: Error: [Aftermath] GPU Stack Dump
```

In this particular example, the GPU has crashed, and the resulting lines with the `[Aftermath]` preceeding indicate the current status and where in the frame the problem is so that you can investigate the root cause.

## Considerations

For an average project that has approximately 200 to 300 markers, Aftermath is fast enough but slowdowns can happen when you have certain things like lots of per-object shadows that increase its cost. For this reason, the feature is not enabled by default.

---

## Fuente: .\docs-md-py\en-us\unreal-engine\nvidia-sli-alternative-frame-rendering-in-unreal-engine.md

# NVIDIA SLI Alternate Frame Rendering

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nvidia-sli-alternative-frame-rendering-in-unreal-engine

> Application Version: 5.7

Unreal Engine supports NVIDIA's **Alternate Frame Rendering** (AFR) for packaged games running on NVIDIA SLI configurations. Alternate Frame Rendering works by alternating frames between the linked GPUs. One frame is rendered by GPU 1 with the next frame rendered by GPU 2, before repeating the procress. Using this method, image quality and performance are improved by using multiple GPUs on a single monitor.

Projects that intend to ship with support for Alternate Frame Rendering will need to work directly with NVIDIA to test their games and have it automatically switch over to use this functionality where possible.

For additional details, see NVIDIA documentation on their [SLI modes, specifically Alternate Frame Rendering](https://docs.nvidia.com/gameworks/content/technologies/desktop/sli.htm) here.

## Forcefully Enabling Alternate Frame Rendering

NVIDIA Control Panel allows for some applications to be manually added which support AFR forcibly enabling the SLI rendering mode. Add applications to the NVIDIA Control Panel using the following steps.

1. Open the **NVIDIA Control Panel** from your task tray, and navigate to **Manage 3D Settings**.
2. Click on the **Program Settings** tab. Under **Select a program to cumstomize** use the dropdown to select the program you want to add.
3. Next to **SLI Rendering Mode**, select **Force Alternate Frame Rendering**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9fa2579-26e5-43b3-9abb-9711f387272b/afrsetting.jpg)


This feature is not guaranteed to improve the quality or performance of your applications. It is not intended for use with the Unreal Engine Editor, specifically. Should to want this for your developed and released project, you will need to talk with NVIDIA directly to set up this functionality with their drivers.

---

## Fuente: .\docs-md-py\en-us\unreal-engine\object-pointers-in-unreal-engine.md

# Object Pointers

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/object-pointers-in-unreal-engine

> Application Version: 5.7

Unreal Engine provides several templated, smart pointers for a variety of use-cases. All Unreal Engine object pointer types must be constructed with `UObject` types, that is, classes that derive from `UObject`.

The following table provides an overview of the types of object pointers available in Unreal Engine and some of their properties. The table columns are:

- **Pointer Type**: Type of pointer.
- **Usage**: Is this pointer type commonly used, used with caution, marked for deprecation, or removed.
- **Supports UPROPERTY?**: Whether this pointer type can be marked as a `UPROPERTY`.
- **Impacts GC?**: Whether the existence of a pointer of this type to the target object keeps the referenced object alive.
- **Supports loading on-demand?**: Whether this pointer type tracks the path to the target object on disk so it can be loaded later.
- **Serialized?**: Whether this pointer type supports serializing the target object for storage.
- **Supports networking?**: Has network serializers and is used or supported in replicated properties or remote procedure calls.

Throughout this documentation page, assume a template type `T`.

| Pointer Type | Usage | Supports UPROPERTY? | Impacts GC? | Supports loading on-demand? | Serialized? | Networking support? |
| --- | --- | --- | --- | --- | --- | --- |
| `T*` (Raw Pointer) | Common | ❌\* | ❌\* | ❌ | ❌\* | ❌\* |
| `TObjectPtr<T>` | Common | ✔️ | ✔️ † | ❌ | ✔️ | ✔️ |
| `TLazyObjectPtr<T>` | Deprecated ‡ | ✔️ | ❌ | ❌ | ✔️ | ❌ |
| `TSoftObjectPtr<T>` | Common | ✔️ | ❌ | ✔️ | ✔️ | ✔️ |
| `TWeakObjectPtr<T>` | Common | ✔️ | ❌ | ❌ | ✔️ | ✔️ |
| `TStrongObjectPtr<T>` | Use Caution § | ❌ | ✔️ ❡ | ❌ | ❌ | ❌ |

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<b>Table Footnotes:</b>",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "* Unreal Header Tool (UHT) can be configured to enable raw pointers marked as <code class=\"inline-code\">UPROPERTY</code>, in which case raw pointers impact GC, support serialization, and support networking. Existing <code class=\"inline-code\">UPROPERTY</code>-marked raw pointers should migrate to use <code class=\"inline-code\">UPROPERTY</code>-marked <code class=\"inline-code\">TObjectPtr</code> if possible.    ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "† <code class=\"inline-code\">TObjectPtr</code> is only garbage collection safe if it is marked as a <code class=\"inline-code\">UPROPERTY</code>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "‡ \n\n<code class=\"inline-code\">TLazyObjectPtr</code> is deprecated and marked for removal in a future engine version, use <code class=\"inline-code\">TSoftObjectPtr</code> instead.    ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "§\n\nSee the <code class=\"inline-code\">TStrongObjectPtr</code> section below for more information.   ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "❡ Since <code class=\"inline-code\">TStrongObjectPtr</code> cannot be marked as a <code class=\"inline-code\">UPROPERTY</code>, it affects garbage collection everywhere (on the stack, captured in lambdas, etc.).",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Quick Guide to Object Pointers

Below is a quick guide to determine which pointer to use for the most common use-cases. `TLazyObjectPtr` is omitted from the following table as it is deprecated.

| Use Case... | Use Pointer Type... |
| --- | --- |
| Local variables, parameters, or short-lived references that are not `UPROPERTY`-marked fields. | `T*` (Raw Pointer) |
| Persistent `UObject` reference on a `UCLASS` or `USTRUCT` that is tracked for garbage collection, serialized, or replicated. | `TObjectPtr<T>` |
| Reference to an asset that should not be forced to load until requested or create a hard dependency. | `TSoftObjectPtr<T>` |
| Non-owning reference or cache to a `UObject` that may be destroyed at any point. | `TWeakObjectPtr<T>` |
| Strong reference to a `UObject` from a non-`UObject` class or struct. | `TStrongObjectPtr<T>` |

## Types of Pointers

This section goes into more detail about each pointer type and provides sample use-cases to help you determine when to use each type.

### TObjectPtr

`TObjectPtr` is meant as a drop-in replacement for a raw pointer. `TObjectPtr` can only be used with types derived from `UObject`. It is serialized in the same way as a raw pointer to a `UObject`. When `TObjectPtr` is marked as a `UPROPERTY`, it is a strong reference to an object that impacts garbage collection and prevents garbage collection from destroying the target object.

`TObjectPtr` should be used in place of raw pointers when possible as it supports advanced cook-time dependency tracking and enables barriers for garbage collection which unlocks incremental garbage collection marking. `TObjectPtr` also supports replication.

You should never directly access a `UObject` through a `TObjectPtr` from worker threads unless you are certain the objects they contain are properly rooted already and cannot be garbage collected while you’re accessing them. For working with `UObject`s from worker threads, use a `TWeakObjectPtr` with the `TWeakObjectPtr::Pin` method to obtain a `TStrongObjectPtr` to the target `UObject` if the target object is still valid.

Example use-cases for `TObjectPtr` include:

- `UPROPERTY`-maked pointer to a `UObject` inside another `UObject`.
- Hard reference to an actor component.

### TLazyObjectPtr

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">TLazyObjectPtr</code> is marked for deprecation in a future engine version. New features should use <code class=\"inline-code\">TSoftObjectPtr</code> instead.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

`TLazyObjectPtr` is a lazy, GUID-based, weak pointer. `TLazyObjectPtr` does not load the target object if not already loaded and can toggle between valid and pending as the object is loaded and unloaded into memory. `TLazyObjectPtr` does not prevent the target object from being garbage collected.

### TSoftObjectPtr

`TSoftObjectPtr` is a weak reference to an object that tracks the path to the target object on disk and has no impact on whether the pointed to object is garbage collected. Since `TSoftObjectPtr` tracks the path to the object on disk, it may change back and forth between valid and pending as the referenced object loads and unloads into and out of memory. This is useful for assets that you want to load asynchronously on demand or for preventing hard dependencies. You must explicitly load the target object synchronously or asynchronously if it is not yet valid.

Example use-cases for `TSoftObjectPtr` include:

- Synchronous or asynchronous loading of object by path.

### TWeakObjectPtr

`TWeakObjectPtr` is a weak pointer to an object. A `TWeakObjectPtr` does not need to be marked as a `UPROPERTY`, although `UPROPERTY` is supported. `TWeakObjectPtr` supports serialization and is also supported for networking. Most often, `TWeakObjectPtr` is used when you explicitly do not want to prevent an object from being garbage collected. If the target object is garbage collected or destroyed, the weak pointer becomes null automatically. Always check whether a `TWeakObjectPtr` is valid with `TWeakObjectPtr::IsValid` or use `TWeakObject::Get` and test nullity before use.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">TWeakObjectPtr</code> is not supported as a key in a <code class=\"inline-code\">TMap</code>, nor as an element in a <code class=\"inline-code\">TSet</code>. If you wish to use a <code class=\"inline-code\">UObject</code> as a key, use <code class=\"inline-code\">TObjectKey</code> instead.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

Example use-cases for `TWeakObjectPtr` include:

- Caching objects.
- Capture a weak object pointer in a lambda.

### TStrongObjectPtr

`TStrongObjectPtr` is a strong pointer to an object. `TStrongObjectPtr` counts references to the target object and prevents garbage collection while it is in scope forcibly keeping the target object alive. `TStrongObjectPtr` does not support `UPROPERTY`, so it is not suited for fields in `UObject`-derived classes. Marking a `TStrongObjectPtr` inside a `UObject` as a `UPROPERTY` is prone to creating uncollectable cycles. For example, if a `UObject`-derived class has a `TStrongObjectPtr` member field that is set to point to itself, this creates an uncollectable cycle, that is, the object will never be deleted, not even if there are no other references to that object (this is not the case with a `TObjectPtr` self-reference). Since `TStrongObjectPtr` does not support `UPROPERTY`, it is also less visible to debugging tools, which makes it more difficult to determine why the target object is still alive.

Creating and destroying a `TStrongObjectPtr` are expensive operations and should be avoided if possible. Use `TStronObjectPtr` for long-lived references that do not change often. As a result, `TStrongObjectPtr` should be avoided in systems such as Mass where objects are unlikely to be deleted between frame updates. Every `TStrongObjectPtr` adds a tracked reference for garbage collection. `TStrongObjectPtr` is always a strong reference keeping the target object alive, even if the object is unreachable and can be garbage collected. As a result, using `TStrongObjectPtr` can degrade performance.

`TStrongObjectPtr` is meant for storing strong references to a `UObject` inside a non-`UObject` owning class, such as a class that does not derive from `UObject` or a struct, since `UPROPERTY` is not available outside of a `UObject`.

For the following use-cases, use the suggested pointer type instead of `TStrongObjectPtr`:

- For owning references inside a `UObject` class, use a `TObjectPtr` marked as a `UPROPERTY`.
- For non-owning references, use a `TWeakObjectPtr`. For asset references, use a `TWeakObjectPtr`.

Example use-cases for `TStrongObjectPtr` include:

- Strong reference to `UObject` in non-`UObject` owner.

---

## Fuente: .\docs-md-py\en-us\unreal-engine\objects-in-unreal-engine.md

# Objects

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/objects-in-unreal-engine

> Application Version: 5.7

Unreal has a robust system for handling game objects. The base class for objects in Unreal is `UObject`. The `UCLASS` macro can be used to tag classes derived from `UObject` so that the **UObject** handling
system is aware of them.

## The UCLASS Macro

The **UCLASS** macro gives the `UObject` a reference to a `UCLASS` that describes its Unreal-based type. Each `UCLASS` maintains one Object called the **Class Default Object**(CDO). The CDO is essentially a default 'template' Object, generated by the class constructor and unmodified thereafter.

Both the UCLASS and the CDO can be retrieved for a given Object instance, although they should generally be considered read-only.
The UCLASS for an Object instance can be accessed at any time using the `GetClass()` function.

A `UCLASS` contains a set of properties and functions that define the class. These are normal C++ functions and variables available to standard C++ code, but tagged with Unreal Engine-specific metadata that controls how they behave within the Object system.
For more details about the tagging syntax, refer to the [Programming Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-cpp-in-unreal-engine).

A UObject class can include native-only properties that are not marked for reflection with UFUNCTION or UPROPERTY specifiers. However, only functions and properties that are marked with [specifier](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties#propertyspecifiers) macros will get listed within their corresponding UCLASS.

## Properties And Function Types

UObjects can have member variables (known as properties) or functions of any type. However, for the Unreal Engine to recognize and manipulate those variables or functions, they must be marked with special macros and must conform to certain type standards. For details on those standards, refer to the [Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties) and [UFunctions](https://dev.epicgames.com/documentation/en-us/unreal-engine/ufunctions-in-unreal-engine) reference pages.

## UObject Creation

UObjects do not support constructor arguments. All C++ UObjects are initialized on engine startup, and the engine calls their default constructor. If there is no default constructor, your UObject will not compile.

UObject constructors should be lightweight and only used to set up default values and subobjects, no other functionality should be called at construction time. For [Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-in-unreal-engine) and [Actor Components](https://dev.epicgames.com/documentation/en-us/unreal-engine/components-in-unreal-engine), initialization functionality should be put into the `BeginPlay()` method instead.

UObjects should only be constructed using NewObject at runtime, or CreateDefaultSubobject for constructors.

| Method | Description |
| --- | --- |
| [`NewObject<class>`](https://dev.epicgames.com/documentation/404) | Creates a new instance with optional parameters for all available creation options. Offers a wide range of flexibility, including simple use cases with an automatically generated name. |
| `CreateDefaultSubobject<class>` | Creates a component or subobject that provides a method for creating a child class and returning the parent class.  When creating a default subobject, because they are constructed at engine startup the class constructor of a UObject should only work with local data or load static assets. |

UObjects should never use the `new` operator. All UObjects are memory managed by Unreal Engine and garbage collected. When you manually manage your memory by using new or delete, you can cause corruption to your memory.

## Functionality Provided by UObjects

It is not required or even appropriate to use this system in all cases, but there are many benefits to doing so, including:

* Garbage collection
* Reference updating

* Reflection
* Serialization
* Automatic updating of default property changes
* Automatic property initialization
* Automatic editor integration
* Type information available at runtime
* Network replication

Most of these benefits apply to [UStructs](https://dev.epicgames.com/documentation/404), which have the same reflection and serialization capabilities as UObjects. UStructs are considered value types and are not garbage collected. For more detail on each of these systems, refer to the [Unreal Object Handling](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-object-handling-in-unreal-engine) documentation.

## The Unreal Header Tool

To harness the functionality provided by UObject-derived types, a preprocessing step needs to be run on the header files for these types to collate the information it needs.
This preprocessing step is performed by the UnrealHeaderTool, or UHT for short. UObject-derived types have a certain structure that needs to be adhered to.

## Header File Format

While a UObject's implementation in a source (.cpp) file is just like any other C++ class, its definition in a header (.h) file must adhere to a certain basic structure in order to work properly with Unreal Engine. Using the editor's **New C++ Class** command is the easiest way to set up a correctly-formatted header file. A basic header file for a UObject-derived class might look like this, assuming the UObject derivative is called UMyObject and the project in which it was created is called MyProject:

```
	#pragma once

	#include 'Object.h'
	#include 'MyObject.generated.h'
	
	UCLASS()
	class MYPROJECT_API UMyObject : public UObject
	{
		GENERATED_BODY()

	};
```

The Unreal-specific parts of this are as follows:

```
	#include "MyObject.generated.h"
```

This line is expected to be the the last `#include` directive in the file. If this header file needs to know about other classes, they can be forward declared anywhere in the file, or included above `MyObject.generated.h`.

```
	UCLASS()
```

The `UCLASS` macro makes `UMyObject` visible to Unreal Engine. The macro supports a variety of [Class Specifiers](https://dev.epicgames.com/documentation/en-us/unreal-engine/class-specifiers) that determine which features are turned on or off for the class.

```
	class MYPROJECT_API UMyObject : public UObject
```

Specifying `MYPROJECT_API` is necessary if MyProject wishes to expose the UMyObject class to other modules. This is most useful for modules or plugins that will be included by game projects and which deliberately expose classes to provide portable, self-contained functionality across multiple projects.

```
	GENERATED_BODY()
```

The `GENERATED_BODY` macro takes no arguments, but sets up the class to support the infrastructure required by the engine. It is required for all `UCLASS` and `USTRUCT`.

Unreal Header Tool supports a minimal set of C++. When wrapping parts of a UCLASS with custom `#ifdefs` macros, UHT will ignore macros that do not contain `WITH_EDITOR` or `WITHEDITORONLY_DATA` macros.

## Updating Objects

Ticking refers to how Objects are updated in Unreal Engine. All Actors have the ability to be ticked each frame, providing you a way to perform any update calculations or actions that are necessary.

Actors and ActorComponents have their Tick functions called automatically when registered to do so, however, `UObjects` do not possess any built-in update ability. When it is necessary for your project, this can be added by inheriting from the `FTickableGameObject` class using the inherits class specifier.
They can then implement the `Tick()` function, which will be called each frame by the engine.

Most in-game Objects will be [Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-in-unreal-engine), which can tick at user-set minimum intervals rather than once per frame.

## Destroying Objects

Object destruction is handled automatically by the garbage collection system when an Object is no longer referenced. This means that no `UPROPERTY` pointers, engine containers, `TStrongObjectPtr`, or class instances should have any strong references to them.

Note that [Weak Pointers](https://dev.epicgames.com/documentation/en-us/unreal-engine/weak-pointers-in-unreal-engine) have no impact on whether an Object is garbage collected or not.

When the garbage collector runs, unreferenced Objects found are removed from memory. In addition, the function `MarkPendingKill()` can be called directly on an Object. This function sets all pointers to the Object to `NULL` and removes the Object from global searches. The Object is fully deleted on the next garbage collection pass.

[Smart pointers](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-pointers-in-unreal-engine) are not intended to be used with UObjects.

* `Object->MarkPendingKill()` has been replaced with `Obj->MarkAsGarbage()`. This new function is now only for tracking stale objects, If `gc.PendingKillEnabled=true` then objects marked as `PendingKill` will be automatically nulled and destroyed by Garbage Collector.
* Strong references keep UObjects alive. If you don't want these references to keep the UObject alive, then those references should convert to using weak pointers, or be a normal pointer that is manually cleared by a programmer (if performance is critical.)

  You can replace Strong pointers with weak pointers and dereference them once during a gameplay operation as garbage collection only runs between frames.
* `IsValid()` is for checking if it's null or garbage, but most usages of IsValid can be replaced with proper programming conventions like clearing pointers to Actors when they have their `OnDestroy` event called.
* If `PendingKill()` is disabled, `MarkGarbage()`will flag to the owner of the object that it wants the object destroyed, but the object itself will not get garbage collected until all references to it are released.
* In the case of Actors, even if the Actor had `Destroy()` called on them, and they were removed from the level, then it will not be Garbage Collected until all references to it are released.
* The Main difference for licensees is that using the function `MarkPendingKill()` to force expensive objects to garbage collect will no longer work.
* Existing checks for nullptr should be replaced with `IsValid()` calls if you're not clearing them manually, since pointers will no longer get automatically cleared by the garbage collector through `MarkPendingKill()`.

---

## Fuente: .\docs-md-py\en-us\unreal-engine\oculus-development-requirements-in-unreal-engine.md

# Oculus Development Requirements

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/oculus-development-requirements-in-unreal-engine

> Application Version: 5.7

In this page you'll find hardware and software development kit (SDK) requirements needed to start developing for the Oculus platform.

## Unreal Engine 4.27

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 10 or later |
| **SDK Version** | Oculus Runtime v27.0 |
| **API Version** (Quest) | API Level 23 |

## Unreal Engine 4.26

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 10 or later |
| **SDK Version** | Oculus Runtime v19.0 |
| **API Version** (Quest) | API Level 23 |

The Oculus SDK versioning listed on this page has been changed to be consistent with Oculus releases. Version 19.0 is the same as version 1.51.

## Unreal Engine 4.25

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 7 or later MacOS 10.10 or later (x86 only) |
| **SDK Version** | Oculus Runtime 1.44 |
| **API Version** (Go/Quest) | API Level 23 |

## Unreal Engine 4.24

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 7 or later MacOS 10.10 or later (x86 only) |
| **SDK Version** | Oculus Runtime 1.40 |
| **API Version** (Go/Quest) | API Level 23 |

## Unreal Engine 4.23

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 7 or later MacOS 10.10 or later (x86 only) |
| **SDK Version** | Oculus Runtime 1.37 |

## Unreal Engine 4.22

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 7 or later MacOS 10.10 or later (x86 only) |
| **SDK Version** | Oculus Runtime 1.28 |

## Unreal Engine 4.21

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 7 or later. MacOS 10.10 or Later (x86 only) |
| **SDK Version** | Oculus Runtime 1.28 |

## Unreal Engine 4.20

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 7 or later. MacOS 10.10 or Later (x86 only) |
| **SDK Version** | Oculus Runtime 1.25 |

## Unreal Engine 4.19

| Hardware Requirements |  |
| --- | --- |
| **Recommended Desktop Hardware** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| **Supported VR Headsets** | See [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs) |
| Software Requirements |  |
| **Desktop Operating System** | Windows 7 or later. MacOS 10.10 or Later (x86 only) |
| **SDK Version** | Oculus Runtime 1.17 |

