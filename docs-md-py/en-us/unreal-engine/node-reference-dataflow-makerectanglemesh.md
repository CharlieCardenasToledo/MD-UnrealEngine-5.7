# MakeRectangleMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRectangleMesh

> Application Version: 5.7

### Description

MakeRectangleMesh (v1)

Make a rectangle mesh

Input(s) :
Origin - Rectangle will be translated so that center is at this point
Normal - Normal vector of all vertices will be set to this value. Default is +Z axis.

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeRectangleMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeRectangleMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Width | Width of rectangle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| Height | Height of rectangle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| WidthVertexCount | Number of vertices along Width axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |
| HeightVertexCount | Number of vertices along Height axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | Rectangle will be translated so that center is at this point | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Normal | Normal vector of all vertices will be set to this value. Default is +Z axis. | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
