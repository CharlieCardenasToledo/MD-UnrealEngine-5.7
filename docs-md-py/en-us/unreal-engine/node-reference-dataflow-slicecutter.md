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
