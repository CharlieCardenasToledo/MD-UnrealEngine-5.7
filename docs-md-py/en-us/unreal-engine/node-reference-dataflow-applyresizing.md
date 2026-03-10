# ApplyResizing

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing

> Application Version: 5.7

### Description

ApplyResizing (v1)
Experimental

Apply resizing for a given Target Mesh.

Input(s) :
TargetSkeletalMesh - The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh
SkeletalMeshLODIndex - Source and Target mesh LOD.
InterpolationData - The pre-calculated base RBF interpolation data.
bForceApplyToRenderMesh - Force apply to the render mesh. Otherwise, the sim mesh will be resized if it exists, only resizing the render mesh if no sim mesh data exists.
SourceSkeletalMesh - The source mesh. Used for CustomResizingRegions. Must have matching vertices with TargetMesh
bSkipCustomRegionResizing - Skip applying Custom Region Resizing data.
bSavePreResizedSimPosition3D - Save pre-resized sim 3d vertices for scaling 2D rest length in XPBD anisotropic stretch constraints.
IMPORTANT: Using Save Pre-Resized Sim Position 3D requires the following settings in SimulationStretchConfig node:
Stretch Use 3d Rest Lengths: false
Solver Type: XPBD
Distribution Type: Anisotropic

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Apply Cloth Outfit Resizing |
| Type | [FChaosClothAssetApplyResizingNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetApplyResizingNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TargetSkeletalMesh | The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| InterpolationData | The pre-calculated base RBF interpolation data. | [FMeshResizingRBFInterpolationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) | (SampleIndices=,SampleRestPositions=,InterpolationWeights=) |
| SkeletalMeshLODIndex | Source and Target mesh LOD. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bForceApplyToRenderMesh | Force apply to the render mesh. Otherwise, the sim mesh will be resized if it exists, only resizing the render mesh if no sim mesh data exists. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SourceSkeletalMesh | The source mesh. Used for CustomResizingRegions. Must have matching vertices with TargetMesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| bSkipCustomRegionResizing | Skip applying Custom Region Resizing data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bSavePreResizedSimPosition3D | Save pre-resized sim 3d vertices for scaling 2D rest length in XPBD anisotropic stretch constraints. IMPORTANT: Using Save Pre-Resized Sim Position 3D requires the following settings in SimulationStretchConfig node: Stretch Use 3d Rest Lengths: false Solver Type: XPBD Distribution Type: Anisotropic | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
