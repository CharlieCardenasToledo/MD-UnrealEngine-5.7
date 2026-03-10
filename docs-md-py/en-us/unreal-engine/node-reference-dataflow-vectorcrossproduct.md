# VectorCrossProduct

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorCrossProduct

> Application Version: 5.7

### Description

VectorCrossProduct (v1)

Compute the cross product of two vectors : CrossProduct = B^A
This node only operates in 3 dimensions, inputs will be converted to a 3D vector internally and result will be a vector with a zero W component

Input(s) :
A - A Vector operand
B - B Vector operand

Output(s):
CrossProduct - Resulting cross product of A and B : CrossProduct=B^A

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Type | [FDataflowVectorCrossProductNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorCrossProductNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CrossProduct | Resulting cross product of A and B : CrossProduct=B^A | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |
