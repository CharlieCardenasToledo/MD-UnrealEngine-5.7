# FixTinyGeo

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo

> Application Version: 5.7

### Description

FixTinyGeo (v1)

Editor Fracture Mode / Utilities / TinyGeo tool
Merge pieces of geometry onto their neighbors -- use it to, for example, clean up too small pieces of geometry.

Input(s) :
Collection [Intrinsic] - Collection to use
TransformSelection - The selected pieces to use
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to use

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FFixTinyGeoDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFixTinyGeoDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MergeType | Whether to merge small geometry, or small clusters | [EFixTinyGeoMergeType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoMergeType) | MergeGeometry |
| bOnFractureLevel | Only consider bones at the current Fracture Level | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bOnlyClusters | Only auto-consider clusters for merging. Note that leaf nodes can still be consider if manually selected. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bOnlySameParent | Only merge clusters to neighbors with the same parent in the hierarchy | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bGeometryOnlySameParent | Only merge geometry to neighbors with the same parent in the hierarchy | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| NeighborSelection |  | [EFixTinyGeoNeighborSelectionMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoNeighborSelectionMeth-) | LargestNeighbor |
| bOnlyToConnected | Only merge pieces that are connected in the proximity graph.If unchecked, connected pieces will still be favored, but if none are available the closest disconnected piece can be merged. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseCollectionProximityForConnections | Whether to use the Proximity (as computed by the Proximity node) to determine which bones are connected, and thus can be considered for merging. Otherwise will compute and use a reasonable default connectivity. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| UseBoneSelection | Options for using the current bone selection | [EFixTinyGeoUseBoneSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoUseBoneSelection) | NoEffect |
| SelectionMethod |  | [EFixTinyGeoGeometrySelectionMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoGeometrySelectionMeth-) | RelativeVolume |
| MinVolumeCubeRoot | If size (cube root of volume) is less than this value, geometry should be merged into neighbors -- i.e. a value of 2 merges geometry smaller than a 2x2x2 cube | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RelativeVolume | If cube root of volume relative to the overall shape's cube root of volume is less than this, the geometry should be merged into its neighbors. (Note: This is a bit different from the histogram viewer's "Relative Size," which instead shows values relative to the largest rigid bone.) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The selected pieces to use | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
