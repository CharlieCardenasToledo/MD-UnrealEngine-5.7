# SetIntoMaterialsArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetIntoMaterialsArray

> Application Version: 5.7

### Description

SetIntoMaterialsArray (v1)

Set an element into a material array at a specific index
(if the index does not match the range of the array, the array will remain unchanged)

Input(s) :
MaterialArray [Intrinsic] - Material array to modify
Material - Material to set at the specific index into the array
Index - Index Set the material at (if the index does not match the range of the array, the array will remain unchanged)

Output(s):
MaterialArray [Passthrough] - Material array to modify

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Materials |
| Type | [FSetIntoMaterialInterfaceArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetIntoMaterialInterfaceArrayDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaterialArray | Material array to modify | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| Material | Material to set at the specific index into the array | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> | None |
| Index | Index Set the material at (if the index does not match the range of the array, the array will remain unchanged) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaterialArray | Material array to modify | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
