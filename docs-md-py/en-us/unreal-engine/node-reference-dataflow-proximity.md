# Proximity

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity

> Application Version: 5.7

### Description

Proximity (v1)

Update the proximity (contact) graph for the bones in a Collection

Input(s) :
DistanceThreshold - If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors
ContactThreshold - If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity
Collection [Intrinsic] - GeometryCollection to update the proximity graph on

Output(s):
Collection [Passthrough] - GeometryCollection to update the proximity graph on

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FProximityDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FProximityDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ProximityMethod | Which method to use to decide whether a given piece of geometry is in proximity with another | [EProximityMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EProximityMethodEnum) | Dataflow\_ProximityMethod\_Precise |
| FilterContactMethod | How to use the Contact Threshold (if > 0) to filter out unwanted small or corner contacts from the proximity graph. If contact threshold is zero, no filtering is applied. | [EProximityContactFilteringMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EProximityContactFilteringMethod-) | Dataflow\_ProximityContactFilteringMethod\_ProjectedBoundsOverlap |
| bUseAsConnectionGraph | Whether to automatically transform the proximity graph into a connection graph to be used for simulation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ContactAreaMethod | The method used to compute contact areas for simulation purposes (only when 'Use As Connection Graph' is enabled) | [EConnectionContactAreaMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EConnectionContactAreaMethodEnum) | Dataflow\_ConnectionContactAreaMethod\_None |
| bRecomputeConvexHulls | Whether to compute new convex hulls for proximity, or use the pre-existing hulls on the Collection, when using convex hulls to determine proximity | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color |  | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=0.000000,A=1.000000) |
| LineWidthMultiplier |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| CenterColor |  | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| CenterSize |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 12.000000 |
| bRandomizeColor | Randomize color per connection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to update the proximity graph on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DistanceThreshold | If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ContactThreshold | If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to update the proximity graph on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
