# DivideVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DivideVector

> Application Version: 5.7

### Description

DivideVector (v1)

Multiply two vectors component wise: V = (A / B)
When a component of B is zero, use the falback value as a return value for the specific component

Input(s) :
A - A Vector operand
B - B Vector operand
Fallback - Fallback Vector used when components of B are zero

Output(s):
V - Add result V=A\*B

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | / Division Over |
| Type | [FDataflowVectorDivideNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorDivideNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| Fallback | Fallback Vector used when components of B are zero | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Add result V=A\*B | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |
