# TransferVertexAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexAttribute

> Application Version: 5.7

### Description

TransferVertexAttribute (v1)

Transfer float properties from a source collection to a target collection.
Component Transfer is used when all geometries from the source collection have matched names with the target collection.
Otherwise, Global Transfer is used.
Geometries are matched when the geometry's BoneName can be found as the start of the BoneName of a geometry in the target collection.
Use TransformNameSuffix to add extra string to the source geometry's BoneName to avoid multiple matched names.
For example, source geometry has name SK\_10 and target geometry has name SK\_10\_tet1
For all names, Check BoneName attribute in Transform group in the collection.

Input(s) :
Collection - Target collection to transfer vertex attribute to.
FromCollection - Source collection to transfer vertex attribute from.
AttributeKey - The name of the vertex attribute to generate indices from.

Output(s):
Collection [Passthrough] - Target collection to transfer vertex attribute to.
AttributeKey [Passthrough] - The name of the vertex attribute to generate indices from.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Tags | Transfer a named vertex attribute from the Source Collection to the Target Collection |
| Type | [FGeometryCollectionTransferVertexAttributeNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-_2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransferMethod | Transfer method [default: Paired Geometry Transfer] | [EDataflowTransferVertexAttributeNodeTransferMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-_2) | Global |
| BoundingVolumeType | Bounding volume type for source assets[default: Triangle] | [EDataflowTransferVertexAttributeNodeBoundingVolume](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-_1) | Triangle |
| SourceScale | Bounding volume hierarchy cell size for neighboring vertices to transfer into[default: Asset] | [EDataflowTransferVertexAttributeNodeSourceScale](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-) | Asset\_Bound |
| Falloff | Falloff of source value based on distance from source triangle[default: Squared] | [EDataflowTransferVertexAttributeNodeFalloff](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransferVertexAttribute-) | None |
| FalloffThreshold | Threshold based on distance from source triangle.Values past the threshold will falloff.[Defaults to 1 percent of triangle size(0.01)] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| EdgeMultiplier | Edge multiplier for the Bounding Volume Hierarchy(BVH) target's particle search radius. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| BoundMultiplier | Max bound multiplier for the Bounding Volume Hierarchy(BVH) target's particle search radius. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| TransformNameSuffix | Suffix of transform names added to the source geometry's BoneName for geometry matching during transfer[default: \_Tet]. In CreateTetrahedron node we add \_Tet to tetrahedral geometries. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | \_Tet |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target collection to transfer vertex attribute to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FromCollection | Source collection to transfer vertex attribute from. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey | The name of the vertex attribute to generate indices from. | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="Vertices") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target collection to transfer vertex attribute to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| AttributeKey | The name of the vertex attribute to generate indices from. | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
