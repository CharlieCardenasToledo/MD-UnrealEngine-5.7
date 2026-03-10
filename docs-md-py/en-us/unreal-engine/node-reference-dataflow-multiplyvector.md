# MultiplyVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MultiplyVector

> Application Version: 5.7

### Description

MultiplyVector (v1)

Multiply two vectors component wise: V = (A \* B)

Input(s) :
A - A Vector operand
B - B Vector operand

Output(s):
V - Add result V=A\*B

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | \* Multiplication Times |
| Type | [FDataflowVectorMultiplyNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorMultiplyNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Add result V=A\*B | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |
