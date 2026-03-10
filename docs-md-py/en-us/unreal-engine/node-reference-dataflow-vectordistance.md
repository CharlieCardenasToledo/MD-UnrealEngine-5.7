# VectorDistance

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorDistance

> Application Version: 5.7

### Description

VectorDistance (v1)

Compute the distance between two vectors : Distance = |B-A|

Input(s) :
A - A Vector operand
B - B Vector operand

Output(s):
Distance - Distance between A and B : Distance=|B-A|

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Type | [FDataflowVectorDistanceNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorDistanceNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |  |  |
| --- | --- | --- | --- | --- | --- |
| Distance | Distance between A and B : Distance= | B-A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |
