# ResampleCurvePoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ResampleCurvePoints

> Application Version: 5.7

### Description

ResampleCurvePoints (v1)
Experimental

Resample the curves with a fixed number of points

Input(s) :
Collection - Managed array collection to be used to store datas
CurveSelection - Curve selection to focus the guides generation spatially
NumPoints - Max number of points (to be able to plug into a variable since enum is not supported in dataflow)

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FResampleCurvePointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FResampleCurvePointsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PointsCount | Max number of points | [EGroomNumPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/EGroomNumPoints) | Size16 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the guides generation spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |
| NumPoints | Max number of points (to be able to plug into a variable since enum is not supported in dataflow) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
