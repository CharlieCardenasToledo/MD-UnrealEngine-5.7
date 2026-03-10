# WaveScalarField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/WaveScalarField

> Application Version: 5.7

### Description

WaveScalarField (v1)

WaveScalar Field Dataflow node v2

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FWaveScalarFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FWaveScalarFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FunctionType |  | [EDataflowWaveFunctionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowWaveFunctionType) | Dataflow\_WaveFunctionType\_Cosine |
| FalloffType |  | [EDataflowFieldFalloffType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowFieldFalloffType) | Dataflow\_FieldFalloffType\_Linear |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Position |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Translation |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Wavelength |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| Period |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
