# ExtractClothSelectionSet

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet

> Application Version: 5.7

### Description

ExtractClothSelectionSet (v1)
Experimental

Extract a selection set from a Cloth Collection.

Input(s) :
Selection - Name of the selection set to be extracted. Currently only SimVertices3D and RenderVertices sets are supported.
DynamicMesh - Dynamic mesh used to reorder indices.

Output(s):
ExtractedSelectionSet - Extracted Selection Set as a Set
ExtractedSelectionArray - Extracted Selection Set as an array

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Extract Cloth Selection Set |
| Type | [FChaosClothAssetExtractSelectionSetNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetExtractSelection-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bReorderForDynamicMesh | Reorder extracted indices to match the order of a DynamicMesh that was created via ClothCollectionToDynamicMesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DynamicMesh | Dynamic mesh used to reorder indices. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExtractedSelectionSet | Extracted Selection Set as a Set | [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| ExtractedSelectionArray | Extracted Selection Set as an array | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
