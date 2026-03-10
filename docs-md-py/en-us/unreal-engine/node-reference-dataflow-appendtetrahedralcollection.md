# AppendTetrahedralCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection

> Application Version: 5.7

### Description

AppendTetrahedralCollection (v2)

Append another Tetrahedral Collection to this collection. All attributes will be appended to the end.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAppendTetrahedralCollectionDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAppendTetrahedralCollectionData-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bMergeTransform | If checked, non-geometry transforms from CollectionToAppend are merged into Collection by matching transform names. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CollectionToAppend |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| CollectionGeometrySelection |  | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
| CollectionToAppendGeometrySelection |  | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
| CollectionGeometryGroupGuids |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| CollectionToAppendGeometryGroupGuids |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
