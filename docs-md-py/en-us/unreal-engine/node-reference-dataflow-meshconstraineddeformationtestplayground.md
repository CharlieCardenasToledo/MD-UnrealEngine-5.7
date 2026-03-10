# MeshConstrainedDeformationTestPlayground

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground

> Application Version: 5.7

### Description

MeshConstrainedDeformationTestPlayground (v1)
Experimental

Mesh Constrained Deformation Node

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Constrained Deformation |
| Type | FMeshConstrainedDeformationNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Iterations |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| bEnableShearConstraint | Remove shear deformation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ShearConstraintStrength |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bEnableBendingConstraint |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| BendingConstraintStrength |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bEnableEdgeConstraint |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| EdgeConstraintStrength |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Gravity |  | [FVector3d](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizingMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| BaseMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| InvMass |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| EdgeConstraintWeights |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizingMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
