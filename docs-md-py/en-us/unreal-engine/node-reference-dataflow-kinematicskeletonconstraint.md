# KinematicSkeletonConstraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicSkeletonConstraint

> Application Version: 5.7

### Description

KinematicSkeletonConstraint (v1)

Bind a animation driven skeleton hierarchy into the tetrahedron on the collection.

Input(s) :
Collection - Pass through collection to place constraints in to.
SkeletonIn - Skeleton to constraint to the tetrahedron (Must be co-located with the tetrahedron).

Output(s):
Collection [Passthrough] - Pass through collection to place constraints in to.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FKinematicSkeletonConstraintDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FKinematicSkeletonConstraintData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExclusionList | Skeleton bones to exclude from the constraint. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Pass through collection to place constraints in to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletonIn | Skeleton to constraint to the tetrahedron (Must be co-located with the tetrahedron). | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Pass through collection to place constraints in to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
