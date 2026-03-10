# USDImport

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport

> Application Version: 5.7

### Description

USDImport (v2)

Import a USD file from a third party garment construction software.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth USD Import |
| Type | [FChaosClothAssetUSDImportNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetUSDImportNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bImportSimMesh | Only import the simulation mesh data from the USD file. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportRenderMesh | Only import the render mesh data from the USD file. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportWithOpacity | Importing the render mesh with opacity requires transluscency to be enable in the project settings. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| UsdFile | Path of the USD file to import. | [FChaosClothAssetImportFilePath](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportFilePath) | (FilePath="",bForceReimport=False) |
| ReimportUsdFile | Click on this button to reimport the specified USD file and regenerate the intermediary assets. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ReloadSimStaticMesh | The USD import process generates an intermediary simulation static mesh. Click on this button to reimport it without reimporting the USD file. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ReloadRenderStaticMesh | The USD import process generates an intermediary render static mesh. Click on this button to reimport it without reimporting the USD file. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| PackagePath | Content folder where all the USD assets are imported. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| ImportedSimStaticMesh | The static mesh created from the USD import process used as simulation mesh. Note that this property can still be empty after successfully importing a simulation mesh depending on whether the simulation mesh is imported from an older version of USD cloth schema. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| ImportedUVScale | The UV scale used to import the patterns from the imported static mesh UV coordinates. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| ImportedRenderStaticMesh | The static mesh created from the USD import process used as render mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| ImportedSimAssets | List of all the simulation static mesh's dependent assets. This does not include any Engine, or Engine plugin content. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| ImportedRenderAssets | List of all the render static mesh's dependent assets. This does not include any Engine, or Engine plugin content. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
