# VisualizeFiberField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFiberField

> Application Version: 5.7

### Description

VisualizeFiberField (v1)

Visualizes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FVisualizeFiberFieldNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FVisualizeFiberFieldNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VectorScale |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VectorField |  | [FFieldCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FFieldCollection) |  |
