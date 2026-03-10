# MakeConvexDecompositionSettings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeConvexDecompositionSettings

> Application Version: 5.7

### Description

MakeConvexDecompositionSettings (v1)

Provide settings for running convex decomposition of geometry

Input(s) :
MinSizeToDecompose - If greater than zero, the minimum geometry size (cube root of volume) to consider for convex decomposition
MaxGeoToHullVolumeRatioToDecompose - If the geo volume / hull volume ratio is greater than this, do not consider convex decomposition
ErrorTolerance - Stop splitting when hulls have error less than this (expressed in cm; will be cubed for volumetric error).
Note: Decomposition will only be performed if: bProtectNegativeSpace is true, ErrorTolerance is > 0, or MaxHullsPerGeometry > 1
MaxHullsPerGeometry - If greater than zero, maximum number of convex hulls to use in each convex decomposition.
Note: Decomposition will only be performed if: bProtectNegativeSpace is true, ErrorTolerance is > 0, or MaxHullsPerGeometry > 1
MinThicknessTolerance - Optionally specify a minimum thickness (in cm) for convex parts; parts below this thickness will always be merged away. Overrides NumOutputHulls and ErrorTolerance when needed.
NumAdditionalSplits - Control the search effort spent per convex decomposition: larger values will require more computation but may find better convex decompositions
bProtectNegativeSpace - Whether to drive decomposition by finding a negative space that should not be covered by convex hulls. If enabled, ErrorTolerance and NumAdditionalSplits will not be used.
bOnlyConnectedToHull - When protecting negative space, only look for space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration.
NegativeSpaceTolerance - Amount of space to leave between convex hulls and protected negative space
NegativeSpaceMinRadius - Spheres smaller than this are not included in the negative space

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FMakeDataflowConvexDecompositionSettingsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeDataflowConvexDecomposition-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MinSizeToDecompose | If greater than zero, the minimum geometry size (cube root of volume) to consider for convex decomposition | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxGeoToHullVolumeRatioToDecompose | If the geo volume / hull volume ratio is greater than this, do not consider convex decomposition | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ErrorTolerance | Stop splitting when hulls have error less than this (expressed in cm; will be cubed for volumetric error). Note: Decomposition will only be performed if: bProtectNegativeSpace is true, ErrorTolerance is > 0, or MaxHullsPerGeometry > 1 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxHullsPerGeometry | If greater than zero, maximum number of convex hulls to use in each convex decomposition. Note: Decomposition will only be performed if: bProtectNegativeSpace is true, ErrorTolerance is > 0, or MaxHullsPerGeometry > 1 | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| MinThicknessTolerance | Optionally specify a minimum thickness (in cm) for convex parts; parts below this thickness will always be merged away. Overrides NumOutputHulls and ErrorTolerance when needed. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| NumAdditionalSplits | Control the search effort spent per convex decomposition: larger values will require more computation but may find better convex decompositions | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| bProtectNegativeSpace | Whether to drive decomposition by finding a negative space that should not be covered by convex hulls. If enabled, ErrorTolerance and NumAdditionalSplits will not be used. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bOnlyConnectedToHull | When protecting negative space, only look for space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| NegativeSpaceTolerance | Amount of space to leave between convex hulls and protected negative space | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| NegativeSpaceMinRadius | Spheres smaller than this are not included in the negative space | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DecompositionSettings |  | [FDataflowConvexDecompositionSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowConvexDecompositionSett-) |  |
