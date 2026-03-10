# CreateColorArrayFromFloatArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray

> Application Version: 5.7

### Description

CreateColorArrayFromFloatArray (v1)

Set the vertex color on the collection based on the normalized float array.

Input(s) :
FloatArray - Float array to use as a scalar for the color

Output(s):
ColorArray - Color array output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Collection|Utilities |
| Type | [FCreateColorArrayFromFloatArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateColorArrayFromFloatArrayD-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bNormalizeInput | Enable normalization of input array | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color | Base color for the normalized float array | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Float array to use as a scalar for the color | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ColorArray | Color array output | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)> |  |
