# GrowTileRegion

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion

> Application Version: 5.7

### Description

GrowTileRegion (v1)
Experimental

Finds a square tile within a specified image region and duplicates it over the whole image.
The image region to search is determined by the UV coordinates in ValidRegionMesh -- only texels inside a 2D UV mesh triangle are considered when searching for a tile.
Note this node does not try to detect any repeating patterns, it just grabs the first square tile of the specified size that is entirely inside the UV mesh.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Grow Tile |
| Type | FMeshResizingGrowTileRegionNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshUVLayer |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| TileWidth |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| ValidRegionMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
| MeshMask |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
