# MeshInfo

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshInfo

> Application Version: 5.7

### Description

MeshInfo (v1)

Collects information from the DynamicMesh and outputs it into a formatted string

Input(s) :
Mesh [Intrinsic] - DynamicMesh for the information

Output(s):
InfoString - Formatted output string

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FMeshInfoDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshInfoDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DynamicMesh for the information | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InfoString | Formatted output string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
