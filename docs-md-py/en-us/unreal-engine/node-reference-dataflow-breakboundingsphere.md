# BreakBoundingSphere

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakBoundingSphere

> Application Version: 5.7

### Description

BreakBoundingSphere (v1)

Expands data of FSphere

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Sphere |
| Tags | Expand Radius Center Volume |
| Type | [FExpandBoundingSphereDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FExpandBoundingSphereDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingSphere |  | [FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Center=(X=0.000000,Y=0.000000,Z=0.000000),W=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Center |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Radius |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Volume |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
