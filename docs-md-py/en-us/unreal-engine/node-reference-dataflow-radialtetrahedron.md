# RadialTetrahedron

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialTetrahedron

> Application Version: 5.7

### Description

RadialTetrahedron (v1)

@todo(deprecate), rename to FRadialTetrahedronDataflowNode

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FRadialTetrahedronDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FRadialTetrahedronDataflowNodes) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InnerRadius |  | double | 1.000000 |
| OuterRadius |  | double | 2.000000 |
| Height |  | double | 1.000000 |
| RadialSample |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| AngularSample |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| VerticalSample |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| BulgeRatio |  | double | 0.000000 |
| bDiscardInteriorTriangles |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
