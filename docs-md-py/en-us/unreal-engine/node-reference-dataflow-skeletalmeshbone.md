# SkeletalMeshBone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshBone

> Application Version: 5.7

### Description

SkeletalMeshBone (v1)

Skeletal Mesh Bone Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | General |
| Tags | Skeletal Mesh |
| Type | [FSkeletalMeshBoneDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FSkeletalMeshBoneDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| PropertyName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Overrides |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndexOut |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
