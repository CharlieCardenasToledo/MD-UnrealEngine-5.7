# Convert Mesh to OBJ String

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString

> Application Version: 5.7

### Description

Convert Mesh to OBJ String (v1)

Convert a mesh to a string formatted as an OBJ file, which can be read by many external mesh viewers

Input(s) :
bInvertFaces - Whether to flip the orientation of the triangles in the OBJ output

Output(s):
StringOBJ - A string representing the input mesh in the OBJ file format

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Development |
| Type | [FMeshToOBJStringDebugDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshToOBJStringDebugDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| bInvertFaces | Whether to flip the orientation of the triangles in the OBJ output | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StringOBJ | A string representing the input mesh in the OBJ file format | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
