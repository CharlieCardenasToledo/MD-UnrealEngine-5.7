# MakePlane

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakePlane

> Application Version: 5.7

### Description

MakePlane (v1)

Make a plane

Input(s) :
BasePoint - Base point
Normal - Normal vector

Output(s):
Plane - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Plane |
| Type | [FMakePlaneDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakePlaneDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DebugDrawRenderSettings | DebugDraw settings | [FDataflowNodeDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.500000,G=0.500000,B=0.500000,A=1.000000),LineWidthMultiplier=1.000000) |
| PlaneSizeMultiplier |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BasePoint | Base point | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Normal | Normal vector | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Plane | Output mesh | [FPlane](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
