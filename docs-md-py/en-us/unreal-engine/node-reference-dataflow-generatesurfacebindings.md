# GenerateSurfaceBindings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings

> Application Version: 5.7

### Description

GenerateSurfaceBindings (v1)

Generate barycentric bindings (used by the FleshDeformer deformer graph and Geometry Cache generation) of a render surface to a tetrahedral mesh and its surface.

* If a point is outside of the tetrahedral mesh, find surface embedding within SurfaceProjectionSearchRadius.
  Embeddings of LOD 0 are color coded in the render view:
  green: embedded on in a tetrahedron
  blue: embedded on a surface triangle
  red: orphan (cannot be embedded)
  yellow: orphan reparented to a tetrahedron from a node neighbor

Input(s) :
Collection - Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.
StaticMeshIn - The input mesh, whose render surface is used to generate bindings.
SkeletalMeshIn - The input mesh, whose render surface is used to generate bindings.
TransformSelection - Render mesh will only bind to geometries whose transforms are in TransformSelection.
GeometryGroupGuidsIn - Render mesh will only bind to geometries whose GeometryGroupGuids match here.

Output(s):
Collection [Passthrough] - Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.
SKMDynamicMesh - Converted from embedded skeletal/static mesh

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FGenerateSurfaceBindings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FGenerateSurfaceBindings) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMeshLODList | Select skeletal mesh LODs to embed. Default empty list selects all LODs. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bDoSurfaceProjection | Enable binding to the exterior hull of the tetrahedron mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SurfaceProjectionSearchRadius | The search radius when looking for surface triangles to bind to. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bDoOrphanReparenting | When nodes aren't contained in tetrahedra and surface projection fails, try to find suitable bindings by looking to neighboring parents. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| StaticMeshIn | The input mesh, whose render surface is used to generate bindings. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| SkeletalMeshIn | The input mesh, whose render surface is used to generate bindings. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| TransformSelection | Render mesh will only bind to geometries whose transforms are in TransformSelection. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| GeometryGroupGuidsIn | Render mesh will only bind to geometries whose GeometryGroupGuids match here. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SKMDynamicMesh | Converted from embedded skeletal/static mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
