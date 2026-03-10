# ExplodedView

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView

> Application Version: 5.7

### Description

ExplodedView (v1)

"Explodes" the pieces from the Collection for better visualization

Input(s) :
Collection [Intrinsic] - Collection to explode
UniformScale - Scale amount to expand the pieces uniformly in all directions
Scale - Scale amounts to expand the pieces in all 3 directions
Offset - Translate collection for exploded view

Output(s):
Collection [Passthrough] - Collection to explode

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FExplodedViewDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FExplodedViewDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to explode | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| UniformScale | Scale amount to expand the pieces uniformly in all directions | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Scale | Scale amounts to expand the pieces in all 3 directions | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Offset | Translate collection for exploded view | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to explode | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
