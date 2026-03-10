# MeshCutter

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter

> Application Version: 5.7

### Description

MeshCutter (v1)

Editor Fracture Mode / Fracture / Mesh tool
Fracture using the shape of a chosen static mesh and/or array of dynamic meshes

Input(s) :
Collection [Intrinsic] - Collection to cut
BoundingBox - Boundingbox to create the cutting planes in
TransformSelection - The selected pieces to cut
Transform - Transform to apply to cut planes
CuttingDynamicMeshes - Dynamic Meshes to cut with
CuttingStaticMesh - Static Mesh to cut with
NumberToScatter - Number of meshes to random scatter
GridX - Number of meshes to add to grid in X
GridY - Number of meshes to add to grid in Y
GridZ - Number of meshes to add to grid in Z
Variability - Magnitude of random displacement to cutting meshes
MinScaleFactor - Minimum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max
MaxScaleFactor - Maximum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max
RollRange - Roll will be chosen between -Range and +Range
PitchRange - Pitch will be chosen between -Range and +Range
YawRange - Yaw will be chosen between -Range and +Range
RandomSeed - Seed for random
ChanceToFracture - Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to cut
TransformSelection [Passthrough] - The selected pieces to cut
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FMeshCutterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshCutterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseHiRes | If using a Static Mesh to cut, attempt to use the Nanite HiRes source mesh, if available and non-empty. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| LODLevel | If using a Static Mesh to cut, and not using the Nanite HiRes source mesh, use this LOD level's mesh | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| CutDistribution | How to arrange the mesh cuts in space | [EMeshCutterCutDistribution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EMeshCutterCutDistribution) | SingleCut |
| PerCutMeshSelection | When there are multiple cutting meshes, how to choose the cut mesh to apply at each location | [EMeshCutterPerCutMeshSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EMeshCutterPerCutMeshSelection) | All |
| bRandomOrientation | Whether to randomly vary the orientation of the cutting meshes | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoundingBox | Boundingbox to create the cutting planes in | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Transform | Transform to apply to cut planes | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| CuttingStaticMesh | Static Mesh to cut with | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| CuttingDynamicMeshes | Dynamic Meshes to cut with | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |
| NumberToScatter | Number of meshes to random scatter | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| GridX | Number of meshes to add to grid in X | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| GridY | Number of meshes to add to grid in Y | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| GridZ | Number of meshes to add to grid in Z | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| Variability | Magnitude of random displacement to cutting meshes | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MinScaleFactor | Minimum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| MaxScaleFactor | Maximum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.500000 |
| RollRange | Roll will be chosen between -Range and +Range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| PitchRange | Pitch will be chosen between -Range and +Range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| YawRange | Yaw will be chosen between -Range and +Range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ChanceToFracture | Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
