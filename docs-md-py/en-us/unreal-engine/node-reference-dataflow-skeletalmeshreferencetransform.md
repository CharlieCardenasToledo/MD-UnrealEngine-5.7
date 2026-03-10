# SkeletalMeshReferenceTransform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshReferenceTransform

> Application Version: 5.7

### Description

SkeletalMeshReferenceTransform (v1)

Skeletal Mesh Reference Transform Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | General |
| Tags | Skeletal Mesh |
| Type | [FSkeletalMeshReferenceTransformDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FSkeletalMeshReferenceTransformD-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| BoneIndexIn |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformOut |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
