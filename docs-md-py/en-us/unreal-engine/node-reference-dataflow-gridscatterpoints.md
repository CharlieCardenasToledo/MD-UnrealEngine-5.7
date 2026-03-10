# GridScatterPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GridScatterPoints

> Application Version: 5.7

### Description

GridScatterPoints (v1)

Grid Scatter Points Dataflow Node

Input(s) :
NumberOfPointsInX - Number of points in X direction
NumberOfPointsInY - Number of points in Y direction
NumberOfPointsInZ - Number of points in Z direction
RandomSeed - Seed for random
MaxRandomDisplacementX - Random displacement in X direction will be in the range (-MaxRandomDisplacementX, MaxRandomDisplacementX)
MaxRandomDisplacementY - Random displacement in Y direction will be in the range (-MaxRandomDisplacementY, MaxRandomDisplacementY)
MaxRandomDisplacementZ - Random displacement in Z direction will be in the range (-MaxRandomDisplacementZ, MaxRandomDisplacementZ)
BoundingBox - BoundingBox to generate points inside of

Output(s):
Points - Generated points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FGridScatterPointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGridScatterPointsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | BoundingBox to generate points inside of | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| NumberOfPointsInX | Number of points in X direction | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| NumberOfPointsInY | Number of points in Y direction | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| NumberOfPointsInZ | Number of points in Z direction | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MaxRandomDisplacementX | Random displacement in X direction will be in the range (-MaxRandomDisplacementX, MaxRandomDisplacementX) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRandomDisplacementY | Random displacement in Y direction will be in the range (-MaxRandomDisplacementY, MaxRandomDisplacementY) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRandomDisplacementZ | Random displacement in Z direction will be in the range (-MaxRandomDisplacementZ, MaxRandomDisplacementZ) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Generated points | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
