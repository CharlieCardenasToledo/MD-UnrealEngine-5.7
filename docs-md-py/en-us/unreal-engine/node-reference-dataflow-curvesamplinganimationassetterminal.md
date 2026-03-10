# CurveSamplingAnimationAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal

> Application Version: 5.7

### Description

CurveSamplingAnimationAssetTerminal (v1)

* terminal node to create an animation asset for muscle activation MLD training.
* The animation remains in the rest pose with the curves spiking from 0 to 1 to 0 in each block of frames (Number of frames per muscle)
* Curves will stay at value 0 most of the time. Only one curve is active at a time.
* Total animation frames = Frame Rate \* Number of frames per muscle

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Terminal |
| Type | [FCurveSamplingAnimationAssetTerminalNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCurveSamplingAnimationAssetTerm-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FrameRate | Frame rate of the animation | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 30 |
| NumFramesPerMuscle | Number of frames created for each curve. Within this window of frames, curve value will go from 0 to 1 to 0. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMeshAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| AnimationAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UAnimSequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UAnimSequence)> | None |
