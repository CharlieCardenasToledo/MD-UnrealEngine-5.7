# AssignMaterialToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection

> Application Version: 5.7

### Description

AssignMaterialToCollection (v1)

Assign material to a set of face in a geometry collection

Input(s) :
Collection [Intrinsic] - Collection to assign material to
FaceSelection - Faces that will be set with this material index, if no selection is connected , all faces will be set
MaterialArray [Intrinsic] - Array holding the materials objects
Material - Material to assign to the selection

Output(s):
Collection [Passthrough] - Collection to assign material to
MaterialArray [Passthrough] - Array holding the materials objects
MaterialIndex - Index where the material was set in the array

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Materials |
| Type | [FAssignMaterialInterfaceToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAssignMaterialI-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bMergeDuplicateMaterials | If true, detect duplicate in the material array and only add the material in the array if it does not yet exists | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to assign material to | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | Faces that will be set with this material index, if no selection is connected , all faces will be set | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| MaterialArray | Array holding the materials objects | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| Material | Material to assign to the selection | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to assign material to | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| MaterialArray | Array holding the materials objects | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| MaterialIndex | Index where the material was set in the array | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
