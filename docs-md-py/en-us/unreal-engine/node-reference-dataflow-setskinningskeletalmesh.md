# SetSkinningSkeletalMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetSkinningSkeletalMesh

> Application Version: 5.7

### Description

SetSkinningSkeletalMesh (v1)
Experimental

Set the skeletal mesh for the collection

Input(s) :
Collection - Managed array collection to be used to store datas
SkeletalMesh - Skeletal mesh binding to be stored in the collection
GeometrySelection - Geometries to set skinning skeletal mesh on

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Type | [FDataflowCollectionSetSkinningSkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionSetSkinningSk-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMesh | Skeletal mesh binding to be stored in the collection | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| GeometrySelection | Geometries to set skinning skeletal mesh on | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) | () |
| LODIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
