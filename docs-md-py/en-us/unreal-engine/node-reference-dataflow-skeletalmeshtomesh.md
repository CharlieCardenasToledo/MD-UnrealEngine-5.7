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
