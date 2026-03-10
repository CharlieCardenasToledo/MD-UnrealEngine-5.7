# Unidad 17

Rango: archivos 1921 a 2040 de 3470

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-autounwrapuv.md

# AutoUnwrapUV

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV

> Application Version: 5.7

### Description

AutoUnwrapUV (v1)

Auto unwrap UVs for a specific UV channel

Input(s) :
Collection [Intrinsic] - Target Collection
FaceSelection - Faces to auto unwrap, no selection means all faces
UVChannel - UV channel to unwrap into ( 0 by default )
GutterSize - Approximate space to leave between UV islands, measured in texels for 512x512 texture

Output(s):
Collection [Passthrough] - Target Collection
UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default )

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|UV |
| Type | [FAutoUnwrapUVDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAutoUnwrapUVDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | Faces to auto unwrap, no selection means all faces | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| GutterSize | Approximate space to leave between UV islands, measured in texels for 512x512 texture | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-baketexturefromcollection.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-baketransformsincollection.md

# BakeTransformsInCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTransformsInCollection

> Application Version: 5.7

### Description

BakeTransformsInCollection (v1)

Bake transforms in Collection

Input(s) :
Collection [Intrinsic] - Collection to bake transforms in

Output(s):
Collection [Passthrough] - Collection to bake transforms in

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Transform |
| Type | [FBakeTransformsInCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBakeTransformsInCollectionDataf-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to bake transforms in | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to bake transforms in | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-bindtorootbone.md

# BindToRootBone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BindToRootBone

> Application Version: 5.7

### Description

BindToRootBone (v1)

Bind an entire mesh to the single root bone of the current skeleton set on the cloth collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Bind Skinning Weights To Root Bone |
| Type | [FChaosClothAssetBindToRootBoneNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetBindToRootBoneNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bBindSimMesh | Whether to bind the simulation mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBindRenderMesh | Whether to bind the render mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-blendvertices.md

# BlendVertices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices

> Application Version: 5.7

### Description

BlendVertices (v1)

Blend vertex values from another cloth collection. The topology of the Collection will remain the same.

Input(s) :
Collection - Input/output collection
BlendCollection - Collection to blend in.

Output(s):
Collection [Passthrough] - Input/output collection

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Blend Vertices |
| Type | [FChaosClothAssetBlendVerticesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetBlendVerticesNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bRequireSameVertexCounts | Require same vertex counts between Collection and BlendCollection in order to blend a vertex type. Otherwise the shared subset will be blended. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| BlendingWeight | Blending Weight. 0 = Keep existing values in Collection. 1 = Set values from BlendCollection. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bBlendSimMesh | Blend Sim Mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlend2DSimPositions | Blend 2D Sim Positions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlend3DSimPositions | Blend 3D Sim Positions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendSimNormals | Blend 3D Sim Normals. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderMesh | Blend Render Mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderPositions | Blend Render Positions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderNormalsAndTangents | Blend Render Normals and Tangents. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderUVs | Blend Render UVs. Only existing UV sets on Collection will be updated. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderColors | Blend Render Colors. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BlendCollection | Collection to blend in. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-blueprinttocollection.md

# BlueprintToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BlueprintToCollection

> Application Version: 5.7

### Description

BlueprintToCollection (v2)

Create a geometry collection from an asset

Output(s):
Collection - Geometry collection newly created
Materials - Material instances array from the static mesh
InstancedMeshes - Array of instanced meshes
RootProxyMeshes - corresponding source proxies

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FBlueprintToCollectionDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBlueprintToCollectionDataflowNo-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Blueprint | Asset input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UBlueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UBlueprint)> | None |
| bSplitComponents | Split components | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Geometry collection newly created | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Materials | Material instances array from the static mesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | Array of instanced meshes | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |
| RootProxyMeshes | corresponding source proxies | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-boolarraytofaceselection.md

# BoolArrayToFaceSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoolArrayToFaceSelection

> Application Version: 5.7

### Description

BoolArrayToFaceSelection (v1)

Converts a TArray to a FDataflowFaceSelection

Input(s) :
BoolAttributeData [Intrinsic] - TArray data

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Type | [FBoolArrayToFaceSelectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoolArrayToFaceSelectionDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoolAttributeData | TArray data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FaceSelection |  | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-booleanoperation.md

# BooleanOperation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BooleanOperation

> Application Version: 5.7

### Description

BooleanOperation (v1)

Boolean operations

Input(s) :
bBoolA - Boolean input
bBoolB - Boolean input

Output(s):
bResult - Boolean result of the operator

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Boolean |
| Type | [FBooleanOperationDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBooleanOperationDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Boolean operation | [EBooleanOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EBooleanOperationEnum) | Dataflow\_And |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bBoolA | Boolean input | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bBoolB | Boolean input | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bResult | Boolean result of the operator | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-boundingsphere.md

# BoundingSphere

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoundingSphere

> Application Version: 5.7

### Description

BoundingSphere (v1)

Description for this node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Sphere |
| Type | [FBoundingSphereDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoundingSphereDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingSphere |  | [FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-boxfallofffield.md

# BoxFalloffField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxFalloffField

> Application Version: 5.7

### Description

BoxFalloffField (v1)

BoxFalloff Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FBoxFalloffFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoxFalloffFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MinRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Default |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| FalloffType |  | [EDataflowFieldFalloffType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowFieldFalloffType) | Dataflow\_FieldFalloffType\_Linear |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Box |  | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Transform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MinRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Default |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldSelectionMask |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-boxprojectuv.md

# BoxProjectUV

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV

> Application Version: 5.7

### Description

BoxProjectUV (v1)

Generates UVs using a box projection

Input(s) :
Collection [Intrinsic] - Target Collection
UVChannel - UV channel to unwrap into ( 0 by default )
GutterSize - Approximate space to leave between UV islands, measured in texels for 512x512 texture

Output(s):
Collection [Passthrough] - Target Collection
UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default )

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|UV |
| Type | [FBoxProjectUVDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoxProjectUVDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ProjectionScale |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000,Z=100.000000) |
| UVOffset |  | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.500000,Y=0.500000) |
| bAutoFitToBounds |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCenterBoxAtPivot |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bUniformProjectionScale |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| GutterSize | Approximate space to leave between UV islands, measured in texels for 512x512 texture | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-boxtomesh.md

# BoxToMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxToMesh

> Application Version: 5.7

### Description

BoxToMesh (v1)

Converts a BoundingBox into a DynamicMesh

Input(s) :
Box [Intrinsic] - BoundingBox input

Output(s):
Mesh - Mesh output
TriangleCount - Mesh triangle count

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FBoxToMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoxToMeshDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | BoundingBox input | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Mesh output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| TriangleCount | Mesh triangle count | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-branch.md

# Branch

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Branch

> Application Version: 5.7

### Description

Branch (v1)

Dataflow Branch Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | FlowControl |
| Type | [FDataflowBranchNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowBranchNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TrueValue |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |
| FalseValue |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |
| bCondition |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-branchcollection.md

# BranchCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchCollection

> Application Version: 5.7

### Description

BranchCollection (v1)

Branch between two Managed Array Collections based on Boolean condition

Input(s) :
TrueCollection - Collection input for the 'true' case
FalseCollection - Collection input for the 'false' case

Output(s):
ChosenCollection - Output Collection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|FlowControl |
| Type | [FBranchCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBranchCollectionDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bCondition | Condition to select which Collection is chosen as ChosenCollection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TrueCollection | Collection input for the 'true' case | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FalseCollection | Collection input for the 'false' case | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| bCondition | Condition to select which Collection is chosen as ChosenCollection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ChosenCollection | Output Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-branchfloat.md

# BranchFloat

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchFloat

> Application Version: 5.7

### Description

BranchFloat (v1)

Branch between two float inputs based on boolean condition

Input(s) :
A - Float input
B - Float input

Output(s):
ReturnValue - Output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|FlowControl |
| Type | [FBranchFloatDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBranchFloatDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bCondition | If true, Output = A, otherwise Output = B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | Float input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| B | Float input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bCondition | If true, Output = A, otherwise Output = B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue | Output | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-branchint.md

# BranchInt

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchInt

> Application Version: 5.7

### Description

BranchInt (v1)

Branch between two int inputs based on boolean condition

Input(s) :
A - Int input
B - Int input

Output(s):
ReturnValue - Output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|FlowControl |
| Type | [FBranchIntDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBranchIntDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bCondition | If true, Output = A, otherwise Output = B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | Int input | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| B | Int input | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bCondition | If true, Output = A, otherwise Output = B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue | Output | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-branchmesh.md

# BranchMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh

> Application Version: 5.7

### Description

BranchMesh (v1)

Branch between two mesh inputs based on boolean condition

Input(s) :
MeshA - Mesh input
MeshB - Mesh input

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|FlowControl |
| Type | [FBranchMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBranchMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bCondition | If true, Output = MeshA, otherwise Output = MeshB | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshA | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| MeshB | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| bCondition | If true, Output = MeshA, otherwise Output = MeshB | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-breakattributekey.md

# BreakAttributeKey

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakAttributeKey

> Application Version: 5.7

### Description

BreakAttributeKey (v1)

Break Attribute Key Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Dataflow |
| Type | [FBreakAttributeKeyDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FBreakAttributeKeyDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeKeyIn |  | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeOut |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| GroupOut |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-breakboundingsphere.md

# BreakBoundingSphere

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakBoundingSphere

> Application Version: 5.7

### Description

BreakBoundingSphere (v1)

Expands data of FSphere

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Sphere |
| Tags | Expand Radius Center Volume |
| Type | [FExpandBoundingSphereDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FExpandBoundingSphereDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingSphere |  | [FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Center=(X=0.000000,Y=0.000000,Z=0.000000),W=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Center |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Radius |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Volume |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-breakbox.md

# BreakBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakBox

> Application Version: 5.7

### Description

BreakBox (v1)

Description for this node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Box |
| Tags | Bounds Bounding Expand Min Max Center Half Extents Volume |
| Type | [FExpandBoundingBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FExpandBoundingBoxDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox |  | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Min |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Max |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HalfExtents |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Volume |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-breaktransform.md

# BreakTransform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform

> Application Version: 5.7

### Description

BreakTransform (v1)

Break a Transform into Translation, Rotation (Euler, Rotator, Quaternion), Scale

Input(s) :
Transform - Transform to break into components

Output(s):
Translation - Translation
Rotation - Rotation as Euler
Rotator - Rotation as a rotator
Quat - Rotation as a quaternion
Scale - Scale

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Transform |
| Type | [FBreakTransformDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBreakTransformDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | Transform to break into components | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Translation | Translation | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |
| Rotation | Rotation as Euler | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Rotator | Rotation as a rotator | [FRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Quat | Rotation as a quaternion | [FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Scale | Scale | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-breakvector.md

# BreakVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector

> Application Version: 5.7

## BreakVector (FDataflowVectorBreakNode)

BreakVector (v1)

Break a vector in 4 components
if the input vector is of a lower dimension than 4, the remaining components will be set to zero

Input(s) :
V - Vector to break into components

Output(s):
X - X component
Y - Y component
Z - Z component
W - W component

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Expand Split X Y Z W Components |
| Type | [FDataflowVectorBreakNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorBreakNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Vector to break into components | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X | X component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |
| Y | Y component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |
| Z | Z component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |
| W | W component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

## BreakVector (FExpandVectorDataflowNode)

BreakVector (v1)

Expands a Vector into X, Y, Z components

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Vector |
| Tags | Expand X Y Z |
| Type | [FExpandVectorDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FExpandVectorDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Y |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Z |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-brickcutter.md

# BrickCutter

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter

> Application Version: 5.7

### Description

BrickCutter (v1)

Editor Fracture Mode / Fracture / Brick tool
Fracture with a customizable brick pattern.
Note: Currently only supports fracturing with at least some (non-zero) Grout.

Input(s) :
Collection [Intrinsic] - Collection to cut
BoundingBox - Boundingbox to create the cutting planes in
TransformSelection - The selected pieces to cut
Transform - Transform to apply to cut planes
BrickLength - Brick length (in cm)
BrickHeight - Brick height (in cm)
BrickDepth - Brick depth (in cm)
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
Collection [Passthrough] - Collection to cut
TransformSelection [Passthrough] - The selected pieces to cut
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FBrickCutterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBrickCutterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Bond | The brick bond pattern defines how the bricks are arranged | [EFractureBrickBondEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFractureBrickBondEnum) | Dataflow\_FractureBrickBond\_Stretcher |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoundingBox | Boundingbox to create the cutting planes in | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Transform | Transform to apply to cut planes | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| BrickLength | Brick length (in cm) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 194.000000 |
| BrickHeight | Brick height (in cm) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 57.000000 |
| BrickDepth | Brick depth (in cm) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 92.000000 |
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
| Collection | Collection to cut | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-buildcurvelods.md

# BuildCurveLODs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs

> Application Version: 5.7

### Description

BuildCurveLODs (v1)
Experimental

Builds the curves LODs

Input(s) :
Collection - Managed array collection to be used to store data
CurveSelection - Curve selection to focus the geometry LODs spatially

Output(s):
Collection [Passthrough] - Managed array collection to be used to store data
CurveParentsKey - Curve parent indices key to be used in other nodes if necessary
CurveLodsKey - Curve lods indices key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildCurveLODsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildCurveLODsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the geometry LODs spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| CurveParentsKey | Curve parent indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| CurveLodsKey | Curve lods indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-buildcurveweights.md

# BuildCurveWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights

> Application Version: 5.7

### Description

BuildCurveWeights (v1)
Experimental

Build a weight map that will be identical on every curves

Input(s) :
Collection - Managed array collection to be used to store datas
CurveSelection - Curve selection to focus the geometry transfer spatially
WeightsAttribute - Vertex kinematic weights key to be used in other nodes if necessary

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildCurveWeightsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildCurveWeightsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CurveWeights | This curve determines the weight value from root to tip. The X axis range is [0,1], 0 mapping the root and 1 the tip | [FRuntimeFloatCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=,DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the geometry transfer spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |
| WeightsAttribute | Vertex kinematic weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-buildguideslods.md

# BuildGuidesLODs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildGuidesLODs

> Application Version: 5.7

### Description

BuildGuidesLODs (v1)
Experimental

Builds the guides LODs

Input(s) :
Collection - Managed array collection to be used to store data

Output(s):
Collection [Passthrough] - Managed array collection to be used to store data
CurveParentsKey - Curve parent indices key to be used in other nodes if necessary
CurveLodsKey - Curve lods indices key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Type | FBuildGuidesLODsDataflowNode |

### Inputs

| Name | Description | Type | DefaultValue |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

### Outputs

| Name | Description | Type |
| --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |
| CurveParentsKey | Curve parent indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |
| CurveLodsKey | Curve lods indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-buildsplineskinweights.md

# BuildSplineSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights

> Application Version: 5.7

### Description

BuildSplineSkinWeights (v1)
Experimental

Build spline skinning data from skeletal mesh

Input(s) :
Collection - Managed array collection to be used to store datas
VertexSelection - Vertex selection to focus the geometry transfer spatially
SkeletalMesh - SkeletalMesh used to compute spline skinning weights. Will be stored onto the groom asset
LODIndex - LOD used to build skinning weights
RootBones - Root bones to be used for spline skinning. Uses all bones if empty. Note that branches in the skeleton is currently not supported.
SamplesPerSegment - Number of spline samples per bone segment.

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
SplineParamKey - Spline Skinning Parameter key
SplineBonesKey - Spline Bones key containing root and end spline bone. To be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildSplineSkinWeightsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildSplineSkinWeightsDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection to focus the geometry transfer spatially | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| SkeletalMesh | SkeletalMesh used to compute spline skinning weights. Will be stored onto the groom asset | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| LODIndex | LOD used to build skinning weights | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| RootBones | Root bones to be used for spline skinning. Uses all bones if empty. Note that branches in the skeleton is currently not supported. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| SamplesPerSegment | Number of spline samples per bone segment. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 64 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SplineParamKey | Spline Skinning Parameter key | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| SplineBonesKey | Spline Bones key containing root and end spline bone. To be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-ceil.md

# Ceil

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Ceil

> Application Version: 5.7

### Description

Ceil (v1)

Ceil ( 1.4 => 2.0 | 1.9 => 2.0 | -5.3 => -5.0)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Round Higher Integer |
| Type | [FDataflowMathCeilNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathCeilNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clamp.md

# Clamp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Clamp

> Application Version: 5.7

### Description

Clamp (v1)

Clamp(A, Min, Max) clamp a value to specific range (inclusive)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Saturate Limits |
| Type | [FDataflowMathClampNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathClampNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Min |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Max |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clearconvexhulls.md

# ClearConvexHulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClearConvexHulls

> Application Version: 5.7

### Description

ClearConvexHulls (v1)

Clear convex hulls from a collection

Input(s) :
TransformSelection - [Optional] selection of transforms to clear convex on, if not set all the transform will be used

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FClearConvexHullsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClearConvexHullsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | [Optional] selection of transforms to clear convex on, if not set all the transform will be used | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-closegeometryoncollection.md

# CloseGeometryOnCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CloseGeometryOnCollection

> Application Version: 5.7

### Description

CloseGeometryOnCollection (v1)

Close Geometry on Collection Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FCloseGeometryOnCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCloseGeometryOnCollectionDatafl-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clothassetimport.md

# ClothAssetImport

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport

> Application Version: 5.7

### Description

ClothAssetImport (v1)

For Reimport

Input(s) :
ClothAsset - The Cloth Asset to import into a collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Asset Import |
| Type | [FChaosClothAssetImportNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reimport | Reimport the imported cloth asset. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ImportLod | The LOD to import into the collection. Only one LOD can be imported at a time. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClothAsset | The Cloth Asset to import into a collection. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosClothAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetEngine/UChaosClothAsset)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clothassetterminal.md

# ClothAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetTerminal

> Application Version: 5.7

### Description

ClothAssetTerminal (v2)

Cloth terminal node to generate a cloth asset from a cloth collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Terminal |
| Type | [FChaosClothAssetTerminalNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetTerminalNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Refresh | Refresh the asset even if the ClothCollection hasn't changed. Note that it is not required to manually refresh the cloth asset, this is done automatically when there is a change in the Dataflow. This function is a developper utility used for debugging. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clothcollectionquery.md

# ClothCollectionQuery

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothCollectionQuery

> Application Version: 5.7

### Description

ClothCollectionQuery (v1)

Query a Managed Array Collection about its Cloth Collection properties.

Input(s) :
Collection - Input/output collection (Output is always a passthrough)

Output(s):
Collection [Passthrough] - Input/output collection (Output is always a passthrough)
bIsClothCollection - Is this collection a valid cloth collection
bHasClothSimMesh - Does this collection have a cloth sim mesh
bHasClothRenderMesh - Does this collection have a cloth render mesh
bHasClothProxyDeformer - Does this collection have proxy deformer data
bBooleanPropertyValue - Result of querying BooleanPropertyName. Default value if property doesn't exist matches node value.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Collection Query |
| Type | [FChaosClothAssetCollectionQueryNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetCollectionQueryN-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BooleanPropertyName | Name of boolean property to query | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | PropertyName |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection (Output is always a passthrough) | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection (Output is always a passthrough) | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| bIsClothCollection | Is this collection a valid cloth collection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasClothSimMesh | Does this collection have a cloth sim mesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasClothRenderMesh | Does this collection have a cloth render mesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasClothProxyDeformer | Does this collection have proxy deformer data | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bBooleanPropertyValue | Result of querying BooleanPropertyName. Default value if property doesn't exist matches node value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clothcollectiontodynamicmesh.md

# ClothCollectionToDynamicMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothCollectionToDynamicMesh

> Application Version: 5.7

### Description

ClothCollectionToDynamicMesh (v1)
Experimental

Convert a Cloth Collection mesh to a dynamic mesh.

Output(s):
SimDynamicMesh - Output sim collection dynamic mesh.
RenderDynamicMesh - Output render collection dynamic mesh.
RenderMaterials - Render materials.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Collection Dynamic Mesh |
| Type | [FChaosClothAssetCollectionToDynamicMeshNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimDynamicMesh | Output sim collection dynamic mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| RenderDynamicMesh | Output render collection dynamic mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| RenderMaterials | Render materials. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-cluster.md

# Cluster

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Cluster

> Application Version: 5.7

### Description

Cluster (v1)

Cluster selected nodes under a new parent

Input(s) :
Collection [Intrinsic] - Collection on which to cluster nodes
TransformSelection - Bone selection

Output(s):
Collection [Passthrough] - Collection on which to cluster nodes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to cluster nodes | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to cluster nodes | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clusterisolatedroots.md

# ClusterIsolatedRoots

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterIsolatedRoots

> Application Version: 5.7

### Description

ClusterIsolatedRoots (v1)

Add a single cluster to the Geometry Collection if it only has a single transform with no clusters

Input(s) :
Collection [Intrinsic] - Collection to modify

Output(s):
Collection [Passthrough] - Collection to modify

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterIsolatedRootsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterIsolatedRootsDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to modify | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to modify | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clustermagnet.md

# ClusterMagnet

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMagnet

> Application Version: 5.7

### Description

ClusterMagnet (v1)

Cluster by grouping the selected bones with their adjacent, neighboring bones.

Input(s) :
Collection [Intrinsic] - Collection on which to merge bones into a cluster
TransformSelection - Bone selection
Iterations - How many layers of neighbors to include in the clusters -- i.e. if 1, only direct neighbors are clustered; if 2, neighbors of neighbors are included, etc.

Output(s):
Collection [Passthrough] - Collection on which to merge bones into a cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterMagnetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterMagnetDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Iterations | How many layers of neighbors to include in the clusters -- i.e. if 1, only direct neighbors are clustered; if 2, neighbors of neighbors are included, etc. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clustermerge.md

# ClusterMerge

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMerge

> Application Version: 5.7

### Description

ClusterMerge (v1)

Merge selected bones under a new parent cluster

Input(s) :
Collection [Intrinsic] - Collection on which to merge bones into a cluster
TransformSelection - Bone selection

Output(s):
Collection [Passthrough] - Collection on which to merge bones into a cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterMergeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterMergeDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clustermergetoneighbors.md

# ClusterMergeToNeighbors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors

> Application Version: 5.7

### Description

ClusterMergeToNeighbors (v1)

Merge selected bones to their neighbors

Input(s) :
Collection [Intrinsic] - Collection on which to merge bones into a neighboring cluster
TransformSelection - Bone selection
MinVolumeCubeRoot - Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value
bOnlyToConnected - Whether to only allow clusters to merge if their bones are connected in the proximity graph
bOnlySameParent - Whether to only allow clusters to merge if they have the same parent bone

Output(s):
Collection [Passthrough] - Collection on which to merge bones into a neighboring cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterMergeToNeighborsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterMergeToNeighborsDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NeighborSelectionMethod | Method to choose which neighbor to merge | [EClusterNeighborSelectionMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EClusterNeighborSelectionMethodE-) | Dataflow\_ClusterNeighborSelectionMethod\_LargestNeighbor |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a neighboring cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| MinVolumeCubeRoot | Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bOnlyToConnected | Whether to only allow clusters to merge if their bones are connected in the proximity graph | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bOnlySameParent | Whether to only allow clusters to merge if they have the same parent bone | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a neighboring cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-clusterscatterpoints.md

# ClusterScatterPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints

> Application Version: 5.7

### Description

ClusterScatterPoints (v1)

Cluster Scatter Points Dataflow Node

Input(s) :
NumberClustersMin - Minimum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max
NumberClustersMax - Maximum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max
PointsPerClusterMin - Minimum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max
PointsPerClusterMax - Maximum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max
ClusterRadiusFractionMin - Minimum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this.
Each point will be placed at least this far (plus the Cluster Radius Offset) from its cluster center.
ClusterRadiusFractionMax - Maximum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this.
Each point will be placed at most this far (plus the Cluster Radius Offset) from its cluster center.
ClusterRadiusOffset - Cluster radius offset (in cm). This offset will be added to the 'Min/Max Dist from Center' distance
RandomSeed - Seed for random
BoundingBox - BoundingBox to generate points inside of

Output(s):
Points - Generated points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FClusterScatterPointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterScatterPointsDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | BoundingBox to generate points inside of | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| NumberClustersMin | Minimum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| NumberClustersMax | Maximum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| PointsPerClusterMin | Minimum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| PointsPerClusterMax | Maximum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 30 |
| ClusterRadiusFractionMin | Minimum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this. Each point will be placed at least this far (plus the Cluster Radius Offset) from its cluster center. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| ClusterRadiusFractionMax | Maximum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this. Each point will be placed at most this far (plus the Cluster Radius Offset) from its cluster center. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.200000 |
| ClusterRadiusOffset | Cluster radius offset (in cm). This offset will be added to the 'Min/Max Dist from Center' distance | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Generated points | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionfaceselectcustom.md

# CollectionFaceSelectCustom

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionFaceSelectCustom

> Application Version: 5.7

### Description

CollectionFaceSelectCustom (v1)

Selects specified faces in the GeometryCollection by using a
space separated list

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
FaceSelection - Face selection including the new indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Face |
| Type | [FCollectionFaceSelectionCustomDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionFaceSelectionCustomDa-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FaceIndicies | Space separated list of face indices to specify the selection | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceIndicies | Space separated list of face indices to specify the selection | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| FaceSelection | Face selection including the new indices | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionselectbyattr.md

# CollectionSelectByAttr

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr

> Application Version: 5.7

### Description

CollectionSelectByAttr (v1)

Selects specified Vertices/Faces/Transforms in the GeometryCollection by using an attribute value
Currently supported attribute types: float, int32, String, bool

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
AttributeKey - AttributeKey input

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
VertexSelection - Vertex selection output
FaceSelection - Face selection output
TransformSelection - Transform selection output
GeometrySelection - Geometry selection output
MaterialSelection - Material selection output
CurveSelection - Curve selection output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|All |
| Type | [FCollectionSelectionByAttrDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionByAttrDatafl-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Group | Group | [ESelectionByAttrGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESelectionByAttrGroup) | Faces |
| Attribute | Attribute for the selection | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Internal |
| Operation | Operation | [ESelectionByAttrOperation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESelectionByAttrOperation) | Equal |
| Value | Attribute value for the operation | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | true |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey | AttributeKey input | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| VertexSelection | Vertex selection output | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |
| FaceSelection | Face selection output | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) |  |
| TransformSelection | Transform selection output | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| GeometrySelection | Geometry selection output | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
| MaterialSelection | Material selection output | [FDataflowMaterialSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMaterialSelection) |  |
| CurveSelection | Curve selection output | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionselectinternalfaces.md

# CollectionSelectInternalFaces

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectInternalFaces

> Application Version: 5.7

### Description

CollectionSelectInternalFaces (v1)

Select internal faces

Input(s) :
Collection [Intrinsic] - Collection to select the internal faces from
TransformSelection - Transform selection to get the internal faces from
if this input is not connected, then all internal faces from the collection will be returned

Output(s):
Collection [Passthrough] - Collection to select the internal faces from
FaceSelection - selection containing Internal faces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection |
| Type | [FCollectionSelectInternalFacesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectInternalFacesDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to select the internal faces from | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Transform selection to get the internal faces from if this input is not connected, then all internal faces from the collection will be returned | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to select the internal faces from | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| FaceSelection | selection containing Internal faces | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionselectionconvert.md

# CollectionSelectionConvert

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionConvert

> Application Version: 5.7

### Description

CollectionSelectionConvert (v1)

Converts Vertex/Face/Transform selection into Vertex/Face/Transform selection

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
TransformSelection - Transform selection including the new indices
FaceSelection - Face selection including the new indices
VertexSelection - Vertex selection including the new indices

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection [Passthrough] - Transform selection including the new indices
FaceSelection [Passthrough] - Face selection including the new indices
VertexSelection [Passthrough] - Vertex selection including the new indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection |
| Type | [FCollectionSelectionConvertDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionConvertDataf-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAllElementsMustBeSelected | If true then for converting vertex/face selection to transform selection all vertex/face must be selected for selecting the associated transform | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection including the new indices | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| FaceSelection | Face selection including the new indices | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| TransformSelection | Transform selection including the new indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Transform selection including the new indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| FaceSelection | Face selection including the new indices | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) |  |
| VertexSelection | Vertex selection including the new indices | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionselectioninvert.md

# CollectionSelectionInvert

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionInvert

> Application Version: 5.7

### Description

CollectionSelectionInvert (v1)

Inverts selection ( support all selection types )

Input(s) :
Selection [Intrinsic] - selection to invert

Output(s):
Selection [Passthrough] - selection to invert

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection |
| Type | [FCollectionSelectionInvertDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionInvertDatafl-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Selection | selection to invert | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Selection | selection to invert | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionselectionsetoperation.md

# CollectionSelectionSetOperation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation

> Application Version: 5.7

### Description

CollectionSelectionSetOperation (v1)

Runs boolean operation on selection ( support all selection types )

Input(s) :
SelectionA [Intrinsic] - First Selection object
SelectionB [Intrinsic] - Second Selection object

Output(s):
Selection - Array of the selected bone indices after operation

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection |
| Type | [FCollectionSelectionSetOperationDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionSetOperation-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Boolean operation | [ESetOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESetOperationEnum) | Dataflow\_SetOperation\_AND |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionA | First Selection object | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |
| SelectionB | Second Selection object | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Selection | Array of the selected bone indices after operation | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionselectiontomeshes.md

# CollectionSelectionToMeshes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionToMeshes

> Application Version: 5.7

### Description

CollectionSelectionToMeshes (v1)

Converts a Collection to a set of Dynamic Meshes per selected Transform

Input(s) :
Collection [Intrinsic] - Collection to convert
TransformSelection - Geometry on or under selected bones will be converted to meshes, optionally after filtering the selection to leaves. If not connected, all geometry will be processed.

Output(s):
Meshes - Output Array of DynamicMesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FCollectionSelectionToMeshesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionToMeshesData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bConvertSelectionToLeaves | Whether to convert the input selection to only leaves, which may directly store geometry. Otherwise, meshes for selected cluster nodes will be generated by appending together geometry from leaf nodes. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bWeldVertices | Whether the processed mesh will have edges at normal/UV/color seams welded so they are treated as one edge during processing. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bPreserveIsolatedVertices | Whether to preserve isolated vertices which aren't used by any triangles. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to convert | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Geometry on or under selected bones will be converted to meshes, optionally after filtering the selection to leaves. If not connected, all geometry will be processed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Meshes | Output Array of DynamicMesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionselecttransformstring.md

# CollectionSelectTransformString

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString

> Application Version: 5.7

### Description

CollectionSelectTransformString (v1)

Selects transforms by name using a the BoneName attributeor other Transform group string typed attributes

Input(s) :
Collection [Intrinsic] - Collection for the selection
Attribute - Text to serach in the name
SearchText - Text to serach in the name

Output(s):
Collection [Passthrough] - Collection for the selection
TransformSelection - output selection of the matching transforms

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Tags | Name, Bone, Attribute |
| Type | [FCollectionSelectTransformStringDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectTransformString-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Method | Method to use to match the name | [EDataflowCollectionSelectionByNameMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowCollectionSelectionByNa-) | Contains |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SearchText | Text to serach in the name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Attribute | Text to serach in the name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | BoneName |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | output selection of the matching transforms | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionsettransformstring.md

# CollectionSetTransformString

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSetTransformString

> Application Version: 5.7

### Description

CollectionSetTransformString (v1)

Set selected transform string value
the string format can use the following predefined value :

* {Current} current value of the attribute
* {Index} index in the selection passed as input

Input(s) :
Collection [Intrinsic] - Collection for the selection
TransformSelection - input selection of the transforms to set - if not connected use all
Attribute - Text to serach in the name
TextToSet - Text to set

Output(s):
Collection [Passthrough] - Collection for the selection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Tags | Bone Name Attribute |
| Type | [FCollectionSetTransformStringValueDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSetTr-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TextToSet | Text to set | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| TransformSelection | input selection of the transforms to set - if not connected use all | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Attribute | Text to serach in the name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | BoneName |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontomesh.md

# CollectionToMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToMesh

> Application Version: 5.7

### Description

CollectionToMesh (v1)

Converts a Collection to a DynamicMesh

Input(s) :
Collection [Intrinsic] - Collection to convert
TransformSelection - Geometry on or under selected bones will be appended to the output mesh. If not connected, all geometry will be processed.

Output(s):
Mesh - Output DynamicMesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FCollectionToMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionToMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bCenterPivot | Whether to translate the mesh geometry to be centered around its bounding box. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bWeldVertices | Whether the processed mesh will have edges at normal/UV/color seams welded so they are treated as one edge during processing. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bPreserveIsolatedVertices | Whether to preserve isolated vertices which aren't used by any triangles. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to convert | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Geometry on or under selected bones will be appended to the output mesh. If not connected, all geometry will be processed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output DynamicMesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontopoints.md

# CollectionToPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToPoints

> Application Version: 5.7

### Description

CollectionToPoints (v1)

Get vertices from a collection as a point cloud

Input(s) :
Collection [Intrinsic] - Collection storing the points

Output(s):
Collection [Passthrough] - Collection storing the points
Points - Points from the collection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FCollectionToPointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionToPointsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection storing the points | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection storing the points | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Points | Points from the collection | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontoskeletalmesh.md

# CollectionToSkeletalMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToSkeletalMesh

> Application Version: 5.7

### Description

CollectionToSkeletalMesh (v1)

Collection to Skeletal Mesh Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FCollectionToSkeletalMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionToSkeletalMeshDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Materials |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> |  |
| Skeleton |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectall.md

# CollectionTransformSelectAll

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectAll

> Application Version: 5.7

### Description

CollectionTransformSelectAll (v1)

Selects all the bones for the Collection

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionAllDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTransformSelectionAll-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectbyfloatattribute.md

# CollectionTransformSelectByFloatAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByFloatAttribute

> Application Version: 5.7

### Description

CollectionTransformSelectByFloatAttribute (v1)

Selects bones by a float attribute

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionByFloatAttrDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Group name for the attr | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Transform |
| AttrName | Attribute name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Min | Minimum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Max | Maximum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| RangeSetting | Values for the selection has to be inside or outside [Min, Max] range | [ERangeSettingEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERangeSettingEnum) | Dataflow\_RangeSetting\_InsideRange |
| bInclusive | If true then range includes Min and Max values | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Min | Minimum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Max | Maximum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectbyintattribute.md

# CollectionTransformSelectByIntAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute

> Application Version: 5.7

### Description

CollectionTransformSelectByIntAttribute (v1)

Selects bones by an int attribute

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Transform selection including the new indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionByIntAttrDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Group name for the attr | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Transform |
| AttrName | Attribute name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Min | Minimum value for the selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Max | Maximum value for the selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1000 |
| RangeSetting | Values for the selection has to be inside or outside [Min, Max] range | [ERangeSettingEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERangeSettingEnum) | Dataflow\_RangeSetting\_InsideRange |
| bInclusive | If true then range includes Min and Max values | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Min | Minimum value for the selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Max | Maximum value for the selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Transform selection including the new indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectbypercentage.md

# CollectionTransformSelectByPercentage

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByPercentage

> Application Version: 5.7

### Description

CollectionTransformSelectByPercentage (v1)

Outputs the specified percentage of the selected bones

Input(s) :
TransformSelection [Intrinsic] - Array of the selected bone indices
RandomSeed - Seed value for the random generation

Output(s):
TransformSelection [Passthrough] - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionByPercentageDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Percentage | Percentage to keep from the original selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| bDeterministic | Sets the random generation to deterministic | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Percentage | Percentage to keep from the original selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| RandomSeed | Seed value for the random generation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -94812.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectbysize.md

# CollectionTransformSelectBySize

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectBySize

> Application Version: 5.7

### Description

CollectionTransformSelectBySize (v1)

Selects pieces based on their size

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionBySizeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_3) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SizeMin | Minimum size for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SizeMax | Maximum size for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| RangeSetting | Values for the selection has to be inside or outside [Min, Max] range | [ERangeSettingEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERangeSettingEnum) | Dataflow\_RangeSetting\_InsideRange |
| bInclusive | If true then range includes Min and Max values | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseRelativeSize | Whether to use the 'Relative Size' -- i.e., the Size / Largest Bone Size. Otherwise, Size is the cube root of Volume. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SizeMin | Minimum size for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SizeMax | Maximum size for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectbyvolume.md

# CollectionTransformSelectByVolume

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByVolume

> Application Version: 5.7

### Description

CollectionTransformSelectByVolume (v1)

Selects pieces based on their volume

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionByVolumeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_4) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VolumeMin | Minimum volume for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| VolumeMax | Maximum volume for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| RangeSetting | Values for the selection has to be inside or outside [Min, Max] range | [ERangeSettingEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERangeSettingEnum) | Dataflow\_RangeSetting\_InsideRange |
| bInclusive | If true then range includes Min and Max values | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VolumeMin | Minimum volume for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| VolumeMax | Maximum volume for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectchildren.md

# CollectionTransformSelectChildren

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectChildren

> Application Version: 5.7

### Description

CollectionTransformSelectChildren (v1)

Selects the children of the selected bones

Input(s) :
TransformSelection [Intrinsic] - Array of the selected bone indices
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
TransformSelection [Passthrough] - Array of the selected bone indices
Collection [Passthrough] - GeometryCollection for the selection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionChildrenDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_5) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectcluster.md

# CollectionTransformSelectCluster

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCluster

> Application Version: 5.7

### Description

CollectionTransformSelectCluster (v2)

Selects the clusters in the Collection
this version works properly and address the issues found in the deprecated version 1

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionClusterDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_7) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectcontact.md

# CollectionTransformSelectContact

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectContact

> Application Version: 5.7

### Description

CollectionTransformSelectContact (v1)

Selects the contact(s) of the selected bones

Input(s) :
TransformSelection [Intrinsic] - Array of the selected bone indices
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
TransformSelection [Passthrough] - Array of the selected bone indices
Collection [Passthrough] - GeometryCollection for the selection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionContactDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_8) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAllowContactInParentLevels | Whether to allow contact with bones that are in a parent level | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectcustom.md

# CollectionTransformSelectCustom

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom

> Application Version: 5.7

### Description

CollectionTransformSelectCustom (v2)

Selects specified bones in the GeometryCollection by using a
comma separated list, e.g. "0, 2, 5-10, 12-15"

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionCustomDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_10) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndices | Comma separated list of single or a range of bone indices to specify the selection, e.g. "0, 2, 5-10, 12-15" | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndices | Comma separated list of single or a range of bone indices to specify the selection, e.g. "0, 2, 5-10, 12-15" | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectinbox.md

# CollectionTransformSelectInBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectInBox

> Application Version: 5.7

### Description

CollectionTransformSelectInBox (v1)

Selects bones if their Vertices/BoundingBox/Centroid in a box

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
Box [Intrinsic] - Box to contain Vertices/BoundingBox/Centroid

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionInBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_12) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | Transform for the box | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Type | Subject (Vertices/BoundingBox/Centroid) to check against box | [ESelectSubjectTypeEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESelectSubjectTypeEnum) | Dataflow\_SelectSubjectType\_Centroid |
| bAllVerticesMustContainedInBox | If true all the vertices of the piece must be inside of box | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Box | Box to contain Vertices/BoundingBox/Centroid | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Transform | Transform for the box | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectinsphere.md

# CollectionTransformSelectInSphere

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectInSphere

> Application Version: 5.7

### Description

CollectionTransformSelectInSphere (v1)

Selects bones if their Vertices/BoundingBox/Centroid in a sphere

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
Sphere [Intrinsic] - Sphere to contain Vertices/BoundingBox/Centroid

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionInSphereDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_13) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | Transform for the sphere | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Type | Subject (Vertices/BoundingBox/Centroid) to check against box | [ESelectSubjectTypeEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESelectSubjectTypeEnum) | Dataflow\_SelectSubjectType\_Centroid |
| bAllVerticesMustContainedInSphere | If true all the vertices of the piece must be inside of box | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Sphere | Sphere to contain Vertices/BoundingBox/Centroid | [FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Center=(X=0.000000,Y=0.000000,Z=0.000000),W=0.000000) |
| Transform | Transform for the sphere | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectionfromindexarray.md

# CollectionTransformSelectionFromIndexArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray

> Application Version: 5.7

### Description

CollectionTransformSelectionFromIndexArray (v1)

Convert index array to a transform selection

Input(s) :
Collection [Intrinsic] - Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection.
BoneIndices - Array of bone indices to convert to a trannsform selection

Output(s):
Collection [Passthrough] - Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection.
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Array |
| Type | [FCollectionTransformSelectionFromIndexArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_11) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndices | Array of bone indices to convert to a trannsform selection | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectioninfo.md

# CollectionTransformSelectionInfo

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionInfo

> Application Version: 5.7

### Description

CollectionTransformSelectionInfo (v1)

Generates a formatted string of the bones and the selection

Input(s) :
TransformSelection [Intrinsic] - Array of the selected bone indices
Collection - GeometryCollection for the selection

Output(s):
String - Formatted string of the bones and selection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionInfoDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTransformSelectionInf-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| String | Formatted string of the bones and selection | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectleaf.md

# CollectionTransformSelectLeaf

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectLeaf

> Application Version: 5.7

### Description

CollectionTransformSelectLeaf (v1)

Selects the leaves in the Collection

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionLeafDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTransformSelectionLea-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectnone.md

# CollectionTransformSelectNone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectNone

> Application Version: 5.7

### Description

CollectionTransformSelectNone (v1)

Generates an empty bone selection for the Collection

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionNoneDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTransformSelectionNon-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectparent.md

# CollectionTransformSelectParent

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectParent

> Application Version: 5.7

### Description

CollectionTransformSelectParent (v1)

Selects the parents of the currently selected bones

Input(s) :
TransformSelection [Intrinsic] - Array of the selected bone indices
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
TransformSelection [Passthrough] - Array of the selected bone indices
Collection [Passthrough] - GeometryCollection for the selection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionParentDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_16) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectrandom.md

# CollectionTransformSelectRandom

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectRandom

> Application Version: 5.7

### Description

CollectionTransformSelectRandom (v1)

Selects bones randomly in the Collection

Input(s) :
RandomSeed - Seed for the random generation, only used if Deterministic is on
RandomThreshold - Bones get selected if RandomValue > RandomThreshold
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionRandomDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_17) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeterministic | If true, it always generates the same result for the same RandomSeed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| RandomSeed | Seed for the random generation, only used if Deterministic is on | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -51438.945312 |
| RandomThreshold | Bones get selected if RandomValue > RandomThreshold | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectroot.md

# CollectionTransformSelectRoot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectRoot

> Application Version: 5.7

### Description

CollectionTransformSelectRoot (v1)

Selects the root bones in the Collection

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionRootDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTransformSelectionRoo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectsamelevel.md

# CollectionTransformSelectSameLevel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectSameLevel

> Application Version: 5.7

### Description

CollectionTransformSelectSameLevel (v1)

Expand the selection to include all nodes with the same level as the selected nodes

Input(s) :
TransformSelection [Intrinsic] - Array of the selected bone indices
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
TransformSelection [Passthrough] - Array of the selected bone indices
Collection [Passthrough] - GeometryCollection for the selection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionLevelDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_15) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselectsiblings.md

# CollectionTransformSelectSiblings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectSiblings

> Application Version: 5.7

### Description

CollectionTransformSelectSiblings (v1)

Selects the siblings of the selected bones

Input(s) :
TransformSelection [Intrinsic] - Array of the selected bone indices
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
TransformSelection [Passthrough] - Array of the selected bone indices
Collection [Passthrough] - GeometryCollection for the selection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionSiblingsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_19) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectiontransformselecttargetlevel.md

# CollectionTransformSelectTargetLevel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectTargetLevel

> Application Version: 5.7

### Description

CollectionTransformSelectTargetLevel (v1)

Selects the root bones in the Collection

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
TargetLevel - Level to select

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionTargetLevelDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_20) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSkipEmbedded | Whether to avoid embedded geometry in the selection (i.e., only select rigid and cluster nodes) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TargetLevel | Level to select | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionvertexselectbypercentage.md

# CollectionVertexSelectByPercentage

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectByPercentage

> Application Version: 5.7

### Description

CollectionVertexSelectByPercentage (v1)

Outputs the specified percentage of the selected vertices

Input(s) :
VertexSelection [Intrinsic] - Array of the selected bone indices
RandomSeed - Seed value for the random generation

Output(s):
VertexSelection [Passthrough] - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Vertex |
| Type | [FCollectionVertexSelectionByPercentageDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionVerte-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Percentage | Percentage to keep from the original selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| bDeterministic | Sets the random generation to deterministic | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexSelection | Array of the selected bone indices | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Percentage | Percentage to keep from the original selection | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| RandomSeed | Seed value for the random generation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -302.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexSelection | Array of the selected bone indices | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-collectionvertexselectcustom.md

# CollectionVertexSelectCustom

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom

> Application Version: 5.7

### Description

CollectionVertexSelectCustom (v1)

Selects specified vertices in the GeometryCollection by using a
space separated list

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
VertexSelection - Vertex selection including the new indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Vertex |
| Type | [FCollectionVertexSelectionCustomDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionVertexSelectionCustom-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexIndicies | Space separated list of vertex indices to specify the selection | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexIndicies | Space separated list of vertex indices to specify the selection | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| VertexSelection | Vertex selection including the new indices | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-comparefloat.md

# CompareFloat

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CompareFloat

> Application Version: 5.7

### Description

CompareFloat (v1)

Comparison between floats

Output(s):
Result - Boolean result of the comparison

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Compare |
| Type | [FCompareFloatDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCompareFloatDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Comparison operation | [ECompareOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECompareOperationEnum) | Dataflow\_Compare\_Equal |
| FloatA | Float input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| FloatB | Float input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatA | Float input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| FloatB | Float input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | Boolean result of the comparison | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-compareint.md

# CompareInt

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CompareInt

> Application Version: 5.7

### Description

CompareInt (v1)

Comparison between integers

Output(s):
Result - Boolean result of the comparison

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Compare |
| Type | [FCompareIntDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCompareIntDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Comparison operation | [ECompareOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECompareOperationEnum) | Dataflow\_Compare\_Equal |
| IntA | Int input | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| IntB | Int input | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IntA | Int input | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| IntB | Int input | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | Boolean result of the comparison | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-computefiberfield.md

# ComputeFiberField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField

> Application Version: 5.7

### Description

ComputeFiberField (v1)

Computes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra,
vertices, and origin & insertion vertex fields. Fiber directions should smoothly follow the geometry
oriented from the origin vertices pointing to the insertion vertices.

Input(s) :
Collection - typedef FManagedArrayCollection DataType;

Output(s):
Collection [Passthrough] - typedef FManagedArrayCollection DataType;

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FComputeFiberFieldNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FComputeFiberFieldNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OriginInsertionGroupName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OriginVertexFieldName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Origin |
| InsertionVertexFieldName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Insertion |
| MaxIterations |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| Tolerance |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bShowMuscleColor | If muscles are colored by the flow from origins (blue) to insertions (red). This becomes optional in 5.6 | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OriginIndices |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InsertionIndices |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-computefiberstreamline.md

# ComputeFiberStreamline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline

> Application Version: 5.7

### Description

ComputeFiberStreamline (v1)

Computes fiber streamlines (line segments) flowing from muscle origins to insertions in the muscle fiber field.

Input(s) :
Collection - typedef FManagedArrayCollection DataType;

Output(s):
Collection [Passthrough] - typedef FManagedArrayCollection DataType;

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FComputeFiberStreamlineNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FComputeFiberStreamlineNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OriginInsertionGroupName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OriginVertexFieldName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Origin |
| InsertionVertexFieldName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Insertion |
| MaxStreamlineIterations |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 500 |
| MaxPointsPerLine |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| NumLinesMultiplier |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OriginIndices |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InsertionIndices |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| VectorField |  | [FFieldCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FFieldCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-computeislands.md

# ComputeIslands

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeIslands

> Application Version: 5.7

### Description

ComputeIslands (v1)

@todo(deprecate)

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FComputeIslandsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FComputeIslandsNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-computemuscleactivationdata.md

# ComputeMuscleActivationData

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeMuscleActivationData

> Application Version: 5.7

### Description

ComputeMuscleActivationData (v2)

Determines muscles that are eligible for activation and computes muscle activation data.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FComputeMuscleActivationDataNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FComputeMuscleActivationDataNode-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OriginIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InsertionIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-constants.md

# Constants

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Constants

> Application Version: 5.7

### Description

Constants (v1)

Math constants ( see EDataflowMathConstantsEnum )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Pi Half Two Four Inverse SquareRoot Sqrt Cube Square e Gamma Golden Ratio |
| Type | [FDataflowMathConstantNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathConstantNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Constant | Math constant to output | [EDataflowMathConstantsEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowMathConstantsEnum) | Dataflow\_Math\_Constants\_Pi |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertboolarraytypes.md

# ConvertBoolArrayTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertBoolArrayTypes

> Application Version: 5.7

### Description

ConvertBoolArrayTypes (v1)

Convert Bool array types

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertBoolArrayTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertBoolArrayTypesDataflowNo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowBoolArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowBoolArrayTypes) | (Value=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowBoolArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowBoolArrayTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertbooltypes.md

# ConvertBoolTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertBoolTypes

> Application Version: 5.7

### Description

ConvertBoolTypes (v1)

Convert Bool types

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertBoolTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertBoolTypesDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowBoolTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowBoolTypes) | (Value=True) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowBoolTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowBoolTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertindexarraytoselection.md

# ConvertIndexArrayToSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertIndexArrayToSelection

> Application Version: 5.7

### Description

ConvertIndexArrayToSelection (v1)

Convert Index Array to Selection

Input(s) :
Collection [Intrinsic] - Collection for the selection
In [Intrinsic] - Input value

Output(s):
Collection [Passthrough] - Collection for the selection
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertIndexArrayToSelectionTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertIndexArrayToSelectionTyp-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| In | Input value | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Out | Output value | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertindextoselection.md

# ConvertIndexToSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertIndexToSelection

> Application Version: 5.7

### Description

ConvertIndexToSelection (v1)

Convert Index to Selection

Input(s) :
Collection [Intrinsic] - Collection for the selection
In [Intrinsic] - Input value

Output(s):
Collection [Passthrough] - Collection for the selection
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertIndexToSelectionTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertIndexToSelectionTypesDat-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| In | Input value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Out | Output value | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertmeshtoobjstring.md

# Convert Mesh to OBJ String

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString

> Application Version: 5.7

### Description

Convert Mesh to OBJ String (v1)

Convert a mesh to a string formatted as an OBJ file, which can be read by many external mesh viewers

Input(s) :
bInvertFaces - Whether to flip the orientation of the triangles in the OBJ output

Output(s):
StringOBJ - A string representing the input mesh in the OBJ file format

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Development |
| Type | [FMeshToOBJStringDebugDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshToOBJStringDebugDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| bInvertFaces | Whether to flip the orientation of the triangles in the OBJ output | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StringOBJ | A string representing the input mesh in the OBJ file format | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertnumericarraytypes.md

# ConvertNumericArrayTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertNumericArrayTypes

> Application Version: 5.7

### Description

ConvertNumericArrayTypes (v1)

Convert Numeric array types

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertNumericArrayTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertNumericArrayTypesDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowNumericArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericArrayTypes) | (Value=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowNumericArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericArrayTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertnumerictypes.md

# ConvertNumericTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertNumericTypes

> Application Version: 5.7

### Description

ConvertNumericTypes (v1)

Convert Numeric types
(double, float, int64, uint64, int32, uint32, int16, uint16, int8, uint8)

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertNumericTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertNumericTypesDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertrotation.md

# ConvertRotation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertRotation

> Application Version: 5.7

### Description

ConvertRotation (v1)

Convert Rotation
(FQuat, FRotator, FVector)

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertRotationDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertRotationDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowRotationTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowRotationTypes) | (Value=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowRotationTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowRotationTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertselectiontoindexarray.md

# ConvertSelectionToIndexArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionToIndexArray

> Application Version: 5.7

### Description

ConvertSelectionToIndexArray (v1)

Convert Selection to Index Array

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertSelectionTypesToIndexArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertSelectionTypesToIndexArr-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertselectiontypes.md

# ConvertSelectionTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes

> Application Version: 5.7

### Description

ConvertSelectionTypes (v1)

Convert Selection types

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
In [Intrinsic] - Input value

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertSelectionTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertSelectionTypesDataflowNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAllElementsMustBeSelected | If true then for converting vertex/face selection to transform/geometry selection all vertex/face must be selected for selecting the associated transform/geometry or going from vertex to face selection all vertices must be selected to select the face | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| In | Input value | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Out | Output value | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertstringarraytypes.md

# ConvertStringArrayTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringArrayTypes

> Application Version: 5.7

### Description

ConvertStringArrayTypes (v1)

Convert String array types

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertStringArrayTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertStringArrayTypesDataflow-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowStringArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowStringArrayTypes) | (Value=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowStringArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowStringArrayTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertstringconvertibletypes.md

# ConvertStringConvertibleTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringConvertibleTypes

> Application Version: 5.7

### Description

ConvertStringConvertibleTypes (v1)

Convert String convertible types
(String types, Numeric types, Vector types and Booleans)

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertStringConvertibleTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertStringConvertibleTypesDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowStringConvertibleTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowStringConvertibleTypes) | (Value="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowStringConvertibleTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowStringConvertibleTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertstringtypes.md

# ConvertStringTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringTypes

> Application Version: 5.7

### Description

ConvertStringTypes (v1)

Convert String types
(FString or FName or FText)

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertStringTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertStringTypesDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowStringTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowStringTypes) | (Value="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowStringTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowStringTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-converttoarray.md

# ConvertToArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertToArray

> Application Version: 5.7

### Description

ConvertToArray (v1)

convert a single element to an array

Input(s) :
Element - Element to convert to an array

Output(s):
Array - Array to Convert to

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Tags | Element |
| Type | [FDataflowConvertToArrayNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowConvertToArrayNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Element | Element to convert to an array | [FDataflowAllTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAllTypes) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to Convert to | [FDataflowArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowArrayTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-converttransformarraytypes.md

# ConvertTransformArrayTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertTransformArrayTypes

> Application Version: 5.7

### Description

ConvertTransformArrayTypes (v1)

Convert Transform array types

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertTransformArrayTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertTransformArrayTypesDataf-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowTransformArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformArrayTypes) | (Value=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowTransformArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformArrayTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-converttransformtypes.md

# ConvertTransformTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertTransformTypes

> Application Version: 5.7

### Description

ConvertTransformTypes (v1)

Convert Transform types

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertTransformTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertTransformTypesDataflowNo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowTransformTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformTypes) | (Value=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowTransformTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertvectorarraytypes.md

# ConvertVectorArrayTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertVectorArrayTypes

> Application Version: 5.7

### Description

ConvertVectorArrayTypes (v1)

Convert Vector array types

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertVectorArrayTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertVectorArrayTypesDataflow-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowVectorArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorArrayTypes) | (Value=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowVectorArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorArrayTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convertvectortypes.md

# ConvertVectorTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertVectorTypes

> Application Version: 5.7

### Description

ConvertVectorTypes (v1)

Convert Vector types
(2D, 3D and 4D vector, single and double precision)

Input(s) :
In [Intrinsic] - Input value

Output(s):
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertVectorTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertVectorTypesDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| In | Input value | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Out | Output value | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-convexhulltomesh.md

# Convex Hull to Mesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvexHulltoMesh

> Application Version: 5.7

### Description

Convex Hull to Mesh (v1)

Convert convex hulls on a geometry collection to a dynamic mesh

Input(s) :
OptionalSelectionFilter - Optional transform selection to convert hulls from -- if not provided, all convex hulls will be converted.

Output(s):
Mesh - Single mesh aggregating all the convex hulls together
Meshes - Array of meshes for each convex hull found

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Mesh |
| Type | [FConvexHullToMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FConvexHullToMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseRobustHulls | Whether to robustly extract valid/manifold meshes to represent the convex hulls. Note: Not necessary for simple visualization, but useful for downstream processing. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OptionalSelectionFilter | Optional transform selection to convert hulls from -- if not provided, all convex hulls will be converted. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Single mesh aggregating all the convex hulls together | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| Meshes | Array of meshes for each convex hull found | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-copysimulationtorendermesh.md

# CopySimulationToRenderMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CopySimulationToRenderMesh

> Application Version: 5.7

### Description

CopySimulationToRenderMesh (v1)

Copy the simulation mesh to the render mesh to be able to render the simulation mesh, or when not using a different mesh for rendering.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Render Mesh |
| Type | [FChaosClothAssetCopySimulationToRenderMeshNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Material | New material for the render mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> | None |
| bGenerateSingleRenderPattern | Generate a single render pattern rather than a render pattern per sim pattern. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-correctskinweights.md

# CorrectSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights

> Application Version: 5.7

### Description

CorrectSkinWeights (v1)
Experimental

Correct skin weights vertex properties.

Input(s) :
BoneIndicesKey - Bone indices key to be used in other nodes if necessary
BoneWeightsKey - Bone weights key to be used in other nodes if necessary
SelectionMapKey - Selection map key to be used in other nodes if necessary
SmoothingIterations - Number of iteration required for the smoothing
SmoothingFactor - Lerp value in between the current and the average weight values
bUseSelectionAsPerVertexFactor - When true, use the decimal values of the selection as a per vertex factor for the selected operation - Currently available for Relax operation only - false by default
PruningThreshold - All weights below this threshold will be pruned
ClampingNumber - Max number of bones to consider for the skin weights
SelectionThreshold - Selection threshold to consider a neighbor skin weight

Output(s):
BoneIndicesKey [Passthrough] - Bone indices key to be used in other nodes if necessary
BoneWeightsKey [Passthrough] - Bone weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [DataflowEditor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor) |
| Category | Collection |
| Tags | Correct skin weights and save it to collection |
| Type | [FDataflowCorrectSkinWeightsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/FDataflowCorrectSkinWeightsNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndicesName | The name to be set for the bone indices. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| BoneWeightsName | The name to be set for the bone weights. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| SelectionMapName | Map name to be used to select vertices to correct | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| CorrectionType | Selection map key to be used in other nodes if necessary | [ESkinWeightsCorrectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/ESkinWeightsCorrectionType) | Relax |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SelectionMapKey | Selection map key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SmoothingIterations | Number of iteration required for the smoothing | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| SmoothingFactor | Lerp value in between the current and the average weight values | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| bUseSelectionAsPerVertexFactor | When true, use the decimal values of the selection as a per vertex factor for the selected operation - Currently available for Relax operation only - false by default | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| PruningThreshold | All weights below this threshold will be pruned | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| ClampingNumber | Max number of bones to consider for the skin weights | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| SelectionThreshold | Selection threshold to consider a neighbor skin weight | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-cos.md

# Cos

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Cos

> Application Version: 5.7

### Description

Cos (v1)

Cos(A) with A in radians

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Cosine Trigonometry Circle Angle Degrees Radians |
| Type | [FDataflowMathCosNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathCosNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-createairtetrahedralconstraint.md

# CreateAirTetrahedralConstraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint

> Application Version: 5.7

### Description

CreateAirTetrahedralConstraint (v1)

Create air tetrahedral constraint between point-triangle pair from surface meshes of different geometries based on search radius.
The added tetrahedra help to maintain distance between geometries.
This node renders the boundary of the added tetrahedral mesh.

Input(s) :
VertexSelection - (optional) only create tetrahedral constraints from surface vertices in VertexSelection to triangles in other geometries.
For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries.
No constraints will be created between two geometries that are not in the VertexSelection.

Output(s):
DynamicMesh - Render dynamic mesh of the boundary mesh of added tetrahedra

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCreateAirTetrahedralConstraintDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCreateAirTetrahedralConstraintD-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SearchRadius | tetrahedral constraint search radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | (optional) only create tetrahedral constraints from surface vertices in VertexSelection to triangles in other geometries. For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries. No constraints will be created between two geometries that are not in the VertexSelection. | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| DynamicMesh | Render dynamic mesh of the boundary mesh of added tetrahedra | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-createairvolumeconstraint.md

# CreateAirVolumeConstraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirVolumeConstraint

> Application Version: 5.7

### Description

CreateAirVolumeConstraint (v1)
Experimental

Creates volume constraint (defined by point-triangle tetrahedron volume) between surface meshes of different geometries.
This constraint allow sliding of the point along the triangle plane.

Input(s) :
VertexSelection - (optional) only create volume constraints from surface vertices in VertexSelection to triangles in other geometries.
For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries.
No constraints will be created between two geometries that are not in the VertexSelection.

Output(s):
DynamicMesh - Render dynamic mesh of the boundary mesh of added volume

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCreateAirVolumeConstraintDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCreateAirVolumeConstraintDatafl-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SearchRadius | search radius for point-triangle pairs | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Stiffness | Stiffness of the volume constraint. This should be around the same magnitude as Young's modulus. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | (optional) only create volume constraints from surface vertices in VertexSelection to triangles in other geometries. For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries. No constraints will be created between two geometries that are not in the VertexSelection. | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| DynamicMesh | Render dynamic mesh of the boundary mesh of added volume | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-createcolorarrayfromfloatarray.md

# CreateColorArrayFromFloatArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray

> Application Version: 5.7

### Description

CreateColorArrayFromFloatArray (v1)

Set the vertex color on the collection based on the normalized float array.

Input(s) :
FloatArray - Float array to use as a scalar for the color

Output(s):
ColorArray - Color array output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Collection|Utilities |
| Type | [FCreateColorArrayFromFloatArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateColorArrayFromFloatArrayD-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bNormalizeInput | Enable normalization of input array | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color | Base color for the normalized float array | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Float array to use as a scalar for the color | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ColorArray | Color array output | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-creategeometrycollectionfromsources.md

# CreateGeometryCollectionFromSources

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateGeometryCollectionFromSources

> Application Version: 5.7

### Description

CreateGeometryCollectionFromSources (v2)

create a geometry collection from a set of geometry sources
if the source array is not connected, the source array from the current asset is going to be used

Input(s) :
Sources - array of geometry sources

Output(s):
Collection - Geometry collection newly created
Materials - Materials array to use for this asset
InstancedMeshes - array of instanced meshes
RootProxyMeshes - corresponding source proxies

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FCreateGeometryCollectionFromSourcesDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateGeometryC-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Sources | array of geometry sources | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionSource](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionSource)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Geometry collection newly created | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Materials | Materials array to use for this asset | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | array of instanced meshes | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |
| RootProxyMeshes | corresponding source proxies | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-createleafconvexhulls.md

# CreateLeafConvexHulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls

> Application Version: 5.7

### Description

CreateLeafConvexHulls (v1)

Create Leaf Convex Hulls Dataflow Node

Input(s) :
OptionalSelectionFilter - Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed.
SimplificationDistanceThreshold - Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume).

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FCreateLeafConvexHullsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateLeafConvexHullsDataflowNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GenerateMethod | How convex hulls are generated -- computed from geometry, imported from external collision shapes, or an intersection of both options. | [EGenerateConvexMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/EGenerateConvexMethod) | ComputedFromGeometry |
| IntersectIfComputedIsSmallerByFactor | If GenerateMethod is Intersect, only actually intersect when the volume of the Computed Hull is less than this fraction of the volume of the External Hull(s). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MinExternalVolumeToIntersect | If GenerateMethod is Intersect, only actually intersect if the volume of the External Hull(s) exceed this threshold. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bComputeIntersectionsBeforeHull | Whether to compute the intersection before computing convex hulls. Typically should be enabled. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SphereCoveringDebugDrawRenderSettings |  | [FDataflowNodeSphereCoveringDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeSphereCoveringDebug-) | (bDisplaySphereCovering=False,RenderType=Wireframe,bTranslucent=True,LineWidthMultiplier=0.250000,ColorMethod=Single,Color=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),ColorRandomSeed=0,ColorA=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),ColorB=(R=0.000000,G=0.000000,B=1.000000,A=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OptionalSelectionFilter | Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| SimplificationDistanceThreshold | Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| ConvexDecompositionSettings |  | [FDataflowConvexDecompositionSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowConvexDecompositionSett-) | (MinSizeToDecompose=0.000000,MaxGeoToHullVolumeRatioToDecompose=1.000000,ErrorTolerance=0.000000,MaxHullsPerGeometry=-1,MinThicknessTolerance=0.000000,NumAdditionalSplits=4,bProtectNegativeSpace=False,bOnlyConnectedToHull=True,NegativeSpaceTolerance=2.000000,NegativeSpaceMinRadius=10.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SphereCovering |  | [FDataflowSphereCovering](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowSphereCovering) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-createnonoverlappingconvexhulls.md

# CreateNonOverlappingConvexHulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls

> Application Version: 5.7

### Description

CreateNonOverlappingConvexHulls (v1)

Generates convex hull representation for the bones for simulation

Input(s) :
CanExceedFraction - Fraction (of geometry volume) by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children. 0 means the convex volume cannot exceed the geometry volume; 1 means the convex volume is allowed to be 100% larger (2x) the geometry volume.
SimplificationDistanceThreshold - Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume)
OverlapRemovalShrinkPercent - Overlap removal will be computed as if convex hulls were this percentage smaller (in range 0-100)
CanRemoveFraction - Fraction of the convex hulls for a cluster that we can remove before using the hulls of the children

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FCreateNonOverlappingConvexHullsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateNonOverlappingConvexHulls-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OverlapRemovalMethod | Whether and in what cases to automatically cut away overlapping parts of the convex hulls, to avoid the simulation 'popping' to fix the overlaps | [EConvexOverlapRemovalMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EConvexOverlapRemovalMethodEnum) | Dataflow\_EConvexOverlapRemovalMethod\_All |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CanRemoveFraction | Fraction of the convex hulls for a cluster that we can remove before using the hulls of the children | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.300000 |
| SimplificationDistanceThreshold | Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CanExceedFraction | Fraction (of geometry volume) by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children. 0 means the convex volume cannot exceed the geometry volume; 1 means the convex volume is allowed to be 100% larger (2x) the geometry volume. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| OverlapRemovalShrinkPercent | Overlap removal will be computed as if convex hulls were this percentage smaller (in range 0-100) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-createtetrahedron.md

# CreateTetrahedron

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron

> Application Version: 5.7

### Description

CreateTetrahedron (v1)

Create Tetrahedron Dataflow Node

Input(s) :
Collection - Input pass-through collection. When connected, the generated tetrahedron will be nested into
its associated parents transform.
SourceCollection - Source collection used to generate the tetrahedron from. Closed geometry within the collections geometry group will be used to
generate tetrahedron.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCreateTetrahedronDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCreateTetrahedronDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Method | Tetrahedral meshing method (TetWild or ISO-stuffing) | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[TetMeshingMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/TetMeshingMethod)> | IsoStuffing |
| Selection | Name of the mesh in the collection. This is defined from the name of the mesh's parent transform. CollectionKey("BoneName","Vertices") | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| NumCells | General control for density for the tetrahedron. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 32 |
| OffsetPercent | Surface offset percentage to increase or decrease the surface alignment. | double | 0.050000 |
| IdealEdgeLengthRel | ! Desired relative edge length, as a fraction of bounding box size | double | 0.050000 |
| MaxIterations | ! Maximum number of optimization iterations. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 80 |
| StopEnergy | ! Energy at which to stop optimizing tet quality and accept the result. | double | 10.000000 |
| EpsRel | ! Relative tolerance, controlling how closely the mesh must follow the input surface. | double | 0.001000 |
| bCoarsen | ! Coarsen the tet mesh result. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bExtractManifoldBoundarySurface | ! Enforce that the output boundary surface should be manifold. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bSkipSimplification | ! Skip the initial simplification step. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bInvertOutputTets | ! Invert tetrahedra. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDiscardInteriorTriangles | Common | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input pass-through collection. When connected, the generated tetrahedron will be nested into its associated parents transform. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SourceCollection | Source collection used to generate the tetrahedron from. Closed geometry within the collections geometry group will be used to generate tetrahedron. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input pass-through collection. When connected, the generated tetrahedron will be nested into its associated parents transform. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-cube.md

# Cube

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Cube

> Application Version: 5.7

### Description

Cube (v1)

Cube ( A  *A*  A )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Type | [FDataflowMathCubeNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathCubeNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-curvesamplinganimationassetterminal.md

# CurveSamplingAnimationAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal

> Application Version: 5.7

### Description

CurveSamplingAnimationAssetTerminal (v1)

* terminal node to create an animation asset for muscle activation MLD training.
* The animation remains in the rest pose with the curves spiking from 0 to 1 to 0 in each block of frames (Number of frames per muscle)
* Curves will stay at value 0 most of the time. Only one curve is active at a time.
* Total animation frames = Frame Rate \* Number of frames per muscle

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Terminal |
| Type | [FCurveSamplingAnimationAssetTerminalNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCurveSamplingAnimationAssetTerm-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FrameRate | Frame rate of the animation | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 30 |
| NumFramesPerMuscle | Number of frames created for each curve. Within this window of frames, curve value will go from 0 to 1 to 0. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMeshAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| AnimationAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UAnimSequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UAnimSequence)> | None |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-customregionresizing.md

# CustomRegionResizing

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CustomRegionResizing

> Application Version: 5.7

### Description

CustomRegionResizing (v1)
Experimental

Node for adding custom region resizing data used by the ChaosOutfitAsset's Resizeable Outfit.

Output(s):
SimCustomResizingBlendName - The name of the sim mesh weight map generated by this node detailing the vertices should use Custom Regions as opposed to
traditional resizing interpolation.
Value ranges between 0 (use traditional resizing interpolation) and 1 (use resizing custom group interpolation).
These regions can be blended if desired.
The name of this sim mesh weight map cannot be changed and is only provided for further tweaking.
RenderCustomResizingBlend - The name of the render mesh weight map generated by this node detailing the vertices should use Custom Regions as opposed to
traditional resizing interpolation.
Value ranges between 0 (use traditional resizing interpolation) and 1 (use resizing custom group interpolation).
These regions can be blended if desired.
The name of this render mesh weight map cannot be changed and is only provided for further tweaking.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Outfit Custom Region Resizing |
| Type | [FChaosClothAssetCustomRegionResizingNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetCustomRegionResi-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InputGroupData | Input custom region data. This data will be stored in the resulting Cloth Asset, and available for use when resizing. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) | (()) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SimCustomResizingBlendName | The name of the sim mesh weight map generated by this node detailing the vertices should use Custom Regions as opposed to traditional resizing interpolation. Value ranges between 0 (use traditional resizing interpolation) and 1 (use resizing custom group interpolation). These regions can be blended if desired. The name of this sim mesh weight map cannot be changed and is only provided for further tweaking. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| RenderCustomResizingBlend | The name of the render mesh weight map generated by this node detailing the vertices should use Custom Regions as opposed to traditional resizing interpolation. Value ranges between 0 (use traditional resizing interpolation) and 1 (use resizing custom group interpolation). These regions can be blended if desired. The name of this render mesh weight map cannot be changed and is only provided for further tweaking. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-dataflowmeshappend.md

# DataflowMeshAppend

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DataflowMeshAppend

> Application Version: 5.7

### Description

DataflowMeshAppend (v1)

Combine two Dataflow meshes

Input(s) :
Mesh [Intrinsic] - Mesh input/output
AppendMesh [Intrinsic] - Mesh to append

Output(s):
Mesh [Passthrough] - Mesh input/output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FDataflowMeshAppendDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowMeshAppendDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Mesh input/output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| AppendMesh | Mesh to append | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Mesh input/output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-degtorad.md

# DegToRad

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DegToRad

> Application Version: 5.7

### Description

DegToRad (v1)

DegToRad(A) convert degrees to radians

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Trigonometry Circle Angle Degrees Radians Convert Unit |
| Type | [FDataflowMathDegToRadNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathDegToRadNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-deleteelement.md

# DeleteElement

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteElement

> Application Version: 5.7

### Description

DeleteElement (v1)

For EChaosClothAssetElementType

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Delete Element |
| Type | [FChaosClothAssetDeleteElementNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetDeleteElementNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeleteSimMesh | Delete the sim mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDeleteRenderMesh | Delete the render mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Group | Delete specific elements. | [FChaosClothAssetNodeSelectionGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetNodeSelectionGro-) | (Name="") |
| Elements | List of Elements to delete from Group. All Elements will be used if left empty. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| SelectionName | Set of Elements to delete. This selection set will be deleted from the downstream collection since it will now be empty. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-deletefleshvertices.md

# DeleteFleshVertices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteFleshVertices

> Application Version: 5.7

### Description

DeleteFleshVertices (v1)

Extract a Tetrahedral Collection from this collection based on selected vertex. Compatible attributes will be copied.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FDeleteFleshVerticesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FDeleteFleshVerticesDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

