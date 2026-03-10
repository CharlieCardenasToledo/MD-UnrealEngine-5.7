# SkeletalMeshImport

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport

> Application Version: 5.7

### Description

SkeletalMeshImport (v2)

Import a skeletal mesh asset into the cloth collection simulation and/or render mesh containers.

Input(s) :
SkeletalMesh - The skeletal mesh to import.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Skeletal Mesh Import |
| Type | [FChaosClothAssetSkeletalMeshImportNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_42) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reimport | Reimport the imported skeletal mesh asset. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| LODIndex | The skeletal mesh LOD to import. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSingleSection | Enable single import section mode. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SectionIndex | The skeletal mesh LOD section to import. If not enabled, then all sections will be imported. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSimMesh | Whether to import the simulation mesh from the specified skeletal mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportRenderMesh | Whether to import the render mesh from the specified skeletal mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| UVChannel | UV channel of the skeletal mesh to import the 2D simulation mesh patterns from. If set to -1, or the specified UVChannel doesn't exist then the import will unwrap the 3D simulation mesh into 2D simulation mesh patterns. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| UVScale | Apply this scale to the UVs when populating Sim Mesh positions. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| bSetPhysicsAsset | Set the same physics asset as the one used by the imported skeletal mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bImportSimMorphTargets | Import morph targets as Sim Mesh Morph Targets | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh | The skeletal mesh to import. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
