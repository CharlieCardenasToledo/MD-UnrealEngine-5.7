# SetFleshBonePositionTargetBinding

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding

> Application Version: 5.7

### Description

SetFleshBonePositionTargetBinding (v2)

Binds vertices from Collection to bone skeletal mesh surface via kinematic or weak constraints.

Input(s) :
VertexSelection - (optional) only create kinematic/weak constraints on vertices in the VertexSelection

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetFleshBonePositionTargetBindingDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetFleshBonePositionTargetBindi-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalBindingMode |  | [ESkeletalBindingMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/ESkeletalBindingMode) | Dataflow\_SkeletalBinding\_PositionTarget |
| PositionTargetStiffness |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10000.000000 |
| SearchRadius | Collection vertices are bound to their closest skeletal mesh vertices within the search radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| VertexSelection | (optional) only create kinematic/weak constraints on vertices in the VertexSelection | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
