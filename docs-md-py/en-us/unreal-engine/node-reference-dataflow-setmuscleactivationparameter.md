# SetMuscleActivationParameter

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter

> Application Version: 5.7

### Description

SetMuscleActivationParameter (v1)

Sets per-muscle parameters for custom muscle contraction.

Input(s) :
AnimationAsset - Use minimum muscle lengths across this animation asset to infer MuscleLengthRatioThresholdForMaxActivation
SkeletalMesh - Skeletal mesh used to linear blend skin kinematic origins and insertions.
This must be the same as the one used to create TransformSource group.
Check geometry spreadsheet for more info.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetMuscleActivationParameterNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetMuscleActivationParameterNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ParameterMethod |  | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EParameterMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/EParameterMethod)> | Global |
| ApplyGlobalParameters | Click on this button to apply global parameters. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ContractionVolumeScale | Muscles gain volume during contraction if > 1. Volume-preserving if 1. Default: 1 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| GlobalFiberLengthRatioAtMaxActivation | How much muscle fibers shorten at max activation 1. A smaller value means more contraction in the fiber direction. Default: 0.5 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| GlobalMuscleLengthRatioThresholdForMaxActivation | Muscle length ratio (defined by origin-insertion distance) below this threshold is considered to reach max activation 1. Default: 0.75 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| GlobalInflationVolumeScale | Inflates muscle rest volume if > 1 and deflates muscle rest volume if < 1. Default: 1 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bUseLengthActivationCurve |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| GlobalLengthActivationCurve | Curve editor for muscle length-activation curve. Default: linear X-axis: normalized muscle length level from 0 (rest state) to 1 (muscle length ratio = Muscle Length Ratio Threshold For Max Activation) Y-axis: muscle activation from 0 to 1 | [FRuntimeFloatCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((),(Time=1.000000,Value=1.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |
| ThresholdScalingPercent | This percentage (usually between 0 and 100%) globally scales minimum muscle lengths computed from the animation asset. For example, if minimum muscle length = 0.5 and ThresholdScalingPercent = 80%, the final MuscleLengthRatioThresholdForMaxActivation for this muscle is 1 - (1 - 0.5) \* 80% = 0.6 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| ImportLowestMuscleLengthRatio | Click on this button to import the minimum muscle lengths across the animation asset as MuscleLengthRatioThresholdForMaxActivation | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ImportAllMuscleNames | Click on this button to import muscle bone names (in the Transform group) from the collection. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ResetToGlobalParameters | Click on this button to reset per-muscle parameters to global parameters. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ApplyCustomParameters | Click on this button to apply custom muscle parameters. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ParameterArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AnimationAsset | Use minimum muscle lengths across this animation asset to infer MuscleLengthRatioThresholdForMaxActivation | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UAnimSequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UAnimSequence)> | None |
| SkeletalMesh | Skeletal mesh used to linear blend skin kinematic origins and insertions. This must be the same as the one used to create TransformSource group. Check geometry spreadsheet for more info. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
