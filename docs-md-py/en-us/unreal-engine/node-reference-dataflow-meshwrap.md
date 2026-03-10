# MeshWrap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap

> Application Version: 5.7

### Description

MeshWrap (v1)
Experimental

Dataflow node for wrapping one mesh's topology to another mesh's shape. Uses point landmarks defined by the Mesh Wrap Landmarks node to match corresponding points between the two meshes.

Input(s) :
SourceTopologyMesh - Input mesh with the desired wrapped mesh topology.
TargetShapeMesh - Input mesh with the desired wrapped mesh shape.
SourceTopologyLandmarks - Landmarks defined on SourceTopologyMesh. TargetShapeLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap.
TargetShapeLandmarks - Landmarks defined on TargetShapeMesh. SourceTopologyLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap.

Output(s):
WrappedMesh - Output wrapped mesh.
MatchedLandmarks - Landmarks matched by Identifier from SourceTopologyLandmarks and TargetShapeLandmarks.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Wrap |
| Type | [FMeshWrapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaxNumOuterIterations | Mesh Wrap is calculated with an inner and outer loop. This is the maximum number of outer loops. Each outer loop increases the Projection Stiffness by ProjectionStiffnessMultiplier. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| NumInnerIterations | Mesh Wrap is calculated with an inner and outer loop. This is the number of inner loops run before increasing the Projection Stiffness in the outer loop. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| ProjectionTolerance | Mesh Wrap will terminate early if the Projection tolerance is within this threshold. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000100 |
| LaplacianStiffness | Weight of mesh wrap to retain Source Topology mesh features. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| InitialProjectionStiffness | Initial weight of mesh wrap to match projected Target Shape. Each outer loop will multiply this stiffness by ProjectionStiffnessMultiplier. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| ProjectionStiffnessMuliplier | Each outer loop will multiply InitialProjectionStiffness by this to improve Target Shape match. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CorrespondenceStiffness | Weight of mesh wrap to match Landmark correspondences. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DefaultDisplayMaterial | Display material for Source or Target when none is supplied. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterial](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterial)> | None |
| bDisplayLandmarks | Display landmarks. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bDisplaySource | Draw source mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SourceDisplayOffset | Offset of source mesh display for side-by-side drawing. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -150.000000 |
| bDisplayTarget | Draw target mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| TargetDisplayOffset | Offset of target mesh display for side-by-side drawing. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 150.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceTopologyMesh | Input mesh with the desired wrapped mesh topology. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| TargetShapeMesh | Input mesh with the desired wrapped mesh shape. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| SourceTopologyLandmarks | Landmarks defined on SourceTopologyMesh. TargetShapeLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapLandmark](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapLandmark)> |  |
| TargetShapeLandmarks | Landmarks defined on TargetShapeMesh. SourceTopologyLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapLandmark](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapLandmark)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| WrappedMesh | Output wrapped mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| MatchedLandmarks | Landmarks matched by Identifier from SourceTopologyLandmarks and TargetShapeLandmarks. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapCorrespondence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapCorrespondence)> |  |
