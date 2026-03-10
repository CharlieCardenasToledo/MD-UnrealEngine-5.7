# BakeTextureFromCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection

> Application Version: 5.7

### Description

BakeTextureFromCollection (v1)

* Bake a texture from a geometry collection
* Output to a 4 channels Image object ( RGBA )

Input(s) :
Collection [Intrinsic] - Target Collection
FaceSelection - selection of faces to bake : if not connected, all faces will be used
Resolution - resolution of the image to bake
GutterSize - Approximate space to leave between UV islands, measured in texels
UVChannel - Index of the added UV channel
MaxDistance - Max distance to search for the outer mesh surface
OcclusionRays - Number of occlusion rays
OcclusionBlurRadius - Pixel Radius of Gaussian Blur Kernel applied to AO map (0 will apply no blur)
CurvatureBlurRadius - Pixel Radius of Gaussian Blur Kernel applied to Curvature map (0 will apply no blur)
VoxelResolution - Voxel resolution of smoothed shape representation
SmoothingIterations - Amount of smoothing iterations to apply before computing curvature
ThicknessFactor - Distance to search for correspondence between fractured shape and smoothed shape, as factor of voxel size
MaxCurvature - Curvatures in the range [-MaxCurvature, MaxCurvature] will be mapped from [0,1]. Values outside that range will be clamped

Output(s):
Collection [Passthrough] - Target Collection
Image - Output image with the bake attributes
UVChannel [Passthrough] - Index of the added UV channel

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Texture |
| Type | [FBakeTextureFromCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBakeTextureFromCollectionDatafl-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RedChannel | Attribute to bake in the red channel | [ECollectionBakeTextureAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECollectionBakeTextureAttribute) | DistanceToExternal |
| GreenChannel | Attribute to bake in the green channel | [ECollectionBakeTextureAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECollectionBakeTextureAttribute) | AmbientOcclusion |
| BlueChannel | Attribute to bake in the blue channel | [ECollectionBakeTextureAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECollectionBakeTextureAttribute) | Curvature |
| AlphaChannel | Attribute to bake in the alpha channel | [ECollectionBakeTextureAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECollectionBakeTextureAttribute) | None |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | selection of faces to bake : if not connected, all faces will be used | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| UVChannel | Index of the added UV channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| GutterSize | Approximate space to leave between UV islands, measured in texels | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| Resolution | resolution of the image to bake | [EDataflowImageResolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageResolution) | Resolution512 |
| MaxDistance | Max distance to search for the outer mesh surface | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| OcclusionRays | Number of occlusion rays | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| OcclusionBlurRadius | Pixel Radius of Gaussian Blur Kernel applied to AO map (0 will apply no blur) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.250000 |
| CurvatureBlurRadius | Pixel Radius of Gaussian Blur Kernel applied to Curvature map (0 will apply no blur) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.250000 |
| VoxelResolution | Voxel resolution of smoothed shape representation | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 128 |
| SmoothingIterations | Amount of smoothing iterations to apply before computing curvature | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| ThicknessFactor | Distance to search for correspondence between fractured shape and smoothed shape, as factor of voxel size | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 4.000000 |
| MaxCurvature | Curvatures in the range [-MaxCurvature, MaxCurvature] will be mapped from [0,1]. Values outside that range will be clamped | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Image | Output image with the bake attributes | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
| UVChannel | Index of the added UV channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
