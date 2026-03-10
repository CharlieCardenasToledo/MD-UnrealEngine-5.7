# VisualizeFracture

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture

> Application Version: 5.7

### Description

VisualizeFracture (v1)

Visualizing fracture/cluster info in fractured collection

Input(s) :
Collection [Intrinsic] - Collection to visualize
RandomSeed - Seed for random
ExplodeAmount - Scale amount to expand the pieces uniformly in all directions
Scale - Scale amounts to expand the pieces in all 3 directions
Offset - Translate collection for exploded view

Output(s):
Collection [Passthrough] - Collection to visualize

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FVisualizeFractureDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVisualizeFractureDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bApplyExplodedView | Use cluster level for coloring and explode | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bApplyColor |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColoringType |  | [EDataflowVisualizeFractureColoringType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowVisualizeFractureColori-) | ColorByLevel |
| RandomColorRangeMin |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 40 |
| RandomColorRangeMax |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 190 |
| Attribute |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Min |  | [FMinSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMinSettings) | (MinAttrValue=0.000000,MinColor=(R=0.000000,G=1.000000,B=0.000000,A=1.000000)) |
| Max |  | [FMaxSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMaxSettings) | (MaxAttrValue=1.000000,MaxColor=(R=1.000000,G=0.000000,B=0.000000,A=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to visualize | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Level |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ExplodeAmount | Scale amount to expand the pieces uniformly in all directions | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Scale | Scale amounts to expand the pieces in all 3 directions | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Offset | Translate collection for exploded view | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to visualize | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
