# ReadSkeletalMeshCurves

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReadSkeletalMeshCurves

> Application Version: 5.7

### Description

ReadSkeletalMeshCurves (v1)

Read Skeletal Mesh Curves Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FReadSkeletalMeshCurvesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FReadSkeletalMeshCurvesDataflowN-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ImportSKMCurveNames | Click on this button to import curve names from the skeletal mesh. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| AssignSKMCurveToMuscle | Click on this button to assign curve to muscles by name. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| CurveMuscleNameArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| GeometrySelection |  | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
