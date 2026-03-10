# EditSkeletonBones

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones

> Application Version: 5.7

### Description

EditSkeletonBones (v1)
Experimental

Edit skeleton bones properties.

Input(s) :
Skeleton - Skeleton to be edited

Output(s):
Skeleton [Passthrough] - Skeleton to be edited

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Tags | Edit skeleton bones |
| Type | [FDataflowCollectionEditSkeletonBonesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionEditSkeletonB-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Skeleton | Skeleton to be edited | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Skeleton | Skeleton to be edited | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> |  |
