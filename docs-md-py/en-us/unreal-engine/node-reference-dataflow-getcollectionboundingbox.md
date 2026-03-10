# GetCollectionBoundingBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionBoundingBox

> Application Version: 5.7

### Description

GetCollectionBoundingBox (v1)

Get the geometric bounding box a collection in collection space

Input(s) :
Collection - Collection to compute the bouning box from

Output(s):
BoundingBox - Geometric bounding box of the input collection
Center - Center of the resulting bounding box
Dimensions - Dimensions of the resulting bounding box in centimers

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Box |
| Tags | Collection Bounds Size Dimensions Extents Center |
| Type | [FBoundingBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoundingBoxDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to compute the bouning box from | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | Geometric bounding box of the input collection | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center | Center of the resulting bounding box | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Dimensions | Dimensions of the resulting bounding box in centimers | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
