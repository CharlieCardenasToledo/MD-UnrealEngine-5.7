# AddRootProxyMeshToArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray

> Application Version: 5.7

### Description

AddRootProxyMeshToArray (v1)

* Add a root proxy object to an array of root proxy mesh
* + (used by geometry collection assets)

Input(s) :
RootProxyMeshes - Root proxy array to add the mesh to

Output(s):
RootProxyMeshes [Passthrough] - Root proxy array to add the mesh to

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FAddRootProxyMeshToArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAddRootProxyMeshToArrayDataflow-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootProxyMeshes | Root proxy array to add the mesh to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |
| RootProxyMesh |  | [FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh) | (Mesh=None,Transform=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),OverrideMaterials=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootProxyMeshes | Root proxy array to add the mesh to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |
