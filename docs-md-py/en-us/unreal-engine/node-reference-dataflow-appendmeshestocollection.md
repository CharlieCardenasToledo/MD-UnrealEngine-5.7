# AppendMeshesToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendMeshesToCollection

> Application Version: 5.7

### Description

AppendMeshesToCollection (v1)

Append Array of Meshes to Collection

Input(s) :
Collection [Intrinsic] - Meshes will be appended to this collection
Meshes - Dynamic Meshes to append
ParentIndex - Index of parent bone for appended meshes. If invalid, meshes will be appended to a root node.

Output(s):
Collection [Passthrough] - Meshes will be appended to this collection
AddedSelection - Selection of added transforms

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FAppendMeshesToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAppendMeshesToCollectionDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Meshes will be appended to this collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Meshes | Dynamic Meshes to append | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |
| ParentIndex | Index of parent bone for appended meshes. If invalid, meshes will be appended to a root node. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Meshes will be appended to this collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| AddedSelection | Selection of added transforms | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
