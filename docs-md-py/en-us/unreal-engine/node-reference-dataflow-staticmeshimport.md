# StaticMeshImport

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport

> Application Version: 5.7

### Description

StaticMeshImport (v2)

Import a static mesh asset into the cloth collection simulation and/or render mesh containers.

Input(s) :
StaticMesh - The Static Mesh to import from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Static Mesh Import |
| Type | [FChaosClothAssetStaticMeshImportNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetStaticMeshImport-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reimport | Reimport the imported static mesh asset. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| LODIndex | Which static mesh Lod to import. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSimMesh | Import static mesh data as a simulation mesh data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SimMeshSection | Material section to import as sim mesh data. Use -1 to import all sections. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| UVChannel | UV channel of the static mesh to import the 2D simulation mesh patterns from. If set to -1, or the specified UVChannel doesn't exist then the import will unwrap the 3D simulation mesh into 2D simulation mesh patterns. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| UVScale | Apply this scale to the UVs when populating Sim Mesh positions. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| bImportRenderMesh | Import static mesh data as render mesh data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| RenderMeshSection | Material section to import as render mesh data. Use -1 to import all sections. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StaticMesh | The Static Mesh to import from. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
