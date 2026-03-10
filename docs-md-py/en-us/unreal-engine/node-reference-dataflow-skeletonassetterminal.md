# SkeletonAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletonAssetTerminal

> Application Version: 5.7

### Description

SkeletonAssetTerminal (v1)

* Dataflow terminal node to save a skeleton asset

Input(s) :
SourceSkeleton - Source Skeleton used to override the skeleton asset
SkeletonAsset - Skeleton Asset to be saved

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Terminal |
| Type | [FSkeletonAssetTerminalNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FSkeletonAssetTerminalNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceSkeleton | Source Skeleton used to override the skeleton asset | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |
| SkeletonAsset | Skeleton Asset to be saved | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |
