# DeleteVertexTrianglePositionTargetBinding

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteVertexTrianglePositionTargetBinding

> Application Version: 5.7

### Description

DeleteVertexTrianglePositionTargetBinding (v1)

Delete vertex-triangle weak constraints (zero rest length springs) between VertexSelection1 and VertexSelection2.

Input(s) :
VertexSelection1 [Intrinsic] - This node deletes springs between VertexSelection1 and VertexSelection2.
VertexSelection2 [Intrinsic] - This node deletes springs between VertexSelection1 and VertexSelection2.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FDeleteVertexTrianglePositionTargetBindingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FDeleteVertexTri-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection1 | This node deletes springs between VertexSelection1 and VertexSelection2. | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| VertexSelection2 | This node deletes springs between VertexSelection1 and VertexSelection2. | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
