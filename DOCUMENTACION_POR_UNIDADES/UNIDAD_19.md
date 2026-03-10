# Unidad 19

Rango: archivos 2161 a 2280 de 3470

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeliteralbool.md

# MakeLiteralBool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralBool

> Application Version: 5.7

### Description

MakeLiteralBool (v2)

Make a bool value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Boolean |
| Type | [FMakeLiteralBoolDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeLiteralBoolDataflowNode_v2) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Bool |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeliteraldouble.md

# MakeLiteralDouble

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralDouble

> Application Version: 5.7

### Description

MakeLiteralDouble (v1)

Make a double value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Double |
| Type | [FMakeLiteralDoubleDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeLiteralDoubleDataflowNode) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Double |  | double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeliteralfloat.md

# MakeLiteralFloat

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralFloat

> Application Version: 5.7

### Description

MakeLiteralFloat (v2)

Make a float value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FMakeLiteralFloatDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeLiteralFloatDataflowNode_v2) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Float |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeliteralint.md

# MakeLiteralInt

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralInt

> Application Version: 5.7

### Description

MakeLiteralInt (v2)

Make an integer value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Int |
| Type | [FMakeLiteralIntDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeLiteralIntDataflowNode_v2) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Int |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeliteralstring.md

# MakeLiteralString

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralString

> Application Version: 5.7

### Description

MakeLiteralString (v2)

Make a literal string

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|String |
| Type | [FMakeLiteralStringDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeLiteralStringDataflowNode_v-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| String |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makemanagedarraycollectionarray.md

# MakeManagedArrayCollectionArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray

> Application Version: 5.7

### Description

MakeManagedArrayCollectionArray (v1)

Append an element to an array of ManagedArrayCollections.

Input(s) :
Array [Intrinsic] - Array to append to. If no input connection, a new array will be created
Element - The element to append.

Output(s):
Array [Passthrough] - Array to append to. If no input connection, a new array will be created

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Tags | Make Managed Array Collection |
| Type | [FDataflowMakeManagedArrayCollectionArrayNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowMakeManagedArrayCollect-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to append to. If no input connection, a new array will be created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |
| Element | The element to append. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to append to. If no input connection, a new array will be created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makematerialarray.md

# MakeMaterialArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeMaterialArray

> Application Version: 5.7

### Description

MakeMaterialArray (v1)

Make a array from a user defined list of material objects

Output(s):
MaterialArray - Material array set by the user

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Materials |
| Type | [FMakeMaterialInterfaceArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeMaterialInterfaceArrayDataf-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaterialArray | Material array set by the user | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeoutfit.md

# MakeOutfit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeOutfit

> Application Version: 5.7

### Description

MakeOutfit (v1)
Experimental

Add multiple cloth asset objects to an outfit collection.

Output(s):
Outfit - The outfit output.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Cloth Asset Make Outfit |
| Type | FChaosOutfitAssetMakeOutfitNode |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit output. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeplane.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makepoints.md

# MakePoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakePoints

> Application Version: 5.7

### Description

MakePoints (v1)

Make a points array from specified points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FMakePointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakePointsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Point |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makequaternion.md

# MakeQuaternion

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeQuaternion

> Application Version: 5.7

### Description

MakeQuaternion (v1)

Make Quaternion Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Vector |
| Type | [FMakeQuaternionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeQuaternionDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Y |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Z |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| W |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Quaternion |  | [FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makerectanglemesh.md

# MakeRectangleMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRectangleMesh

> Application Version: 5.7

### Description

MakeRectangleMesh (v1)

Make a rectangle mesh

Input(s) :
Origin - Rectangle will be translated so that center is at this point
Normal - Normal vector of all vertices will be set to this value. Default is +Z axis.

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeRectangleMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeRectangleMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Width | Width of rectangle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| Height | Height of rectangle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| WidthVertexCount | Number of vertices along Width axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |
| HeightVertexCount | Number of vertices along Height axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | Rectangle will be translated so that center is at this point | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Normal | Normal vector of all vertices will be set to this value. Default is +Z axis. | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makerootproxymesh.md

# MakeRootProxyMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRootProxyMesh

> Application Version: 5.7

### Description

MakeRootProxyMesh (v1)

Create a RootProxyMesh object
(used by geometry collection assets)

Input(s) :
Mesh - mesh to use as a proxy
Transform - transform to use for the proxy, relative to the asset it will be used for

Output(s):
RootProxyMesh - mesh to use as a proxy

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FMakeRootProxyMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeRootProxyMeshDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | mesh to use as a proxy | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| Transform | transform to use for the proxy, relative to the asset it will be used for | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| OverrideMaterials |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootProxyMesh | mesh to use as a proxy | [FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makerootproxymesharray.md

# MakeRootProxyMeshArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRootProxyMeshArray

> Application Version: 5.7

### Description

MakeRootProxyMeshArray (v1)

Create a RootProxyMesh Array
(used by geometry collection assets)

Output(s):
RootProxyMeshes - newly created array

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FMakeRootProxyMeshArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeRootProxyMeshArrayDataflowN-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootProxyMeshes | newly created array | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makerotator.md

# MakeRotator

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator

> Application Version: 5.7

### Description

MakeRotator (v1)

Make a Rotator

Input(s) :
Pitch - Rotation around the right axis (around Y axis), Looking up and down (0=Straight Ahead, +Up, -Down)
Yaw - Rotation around the up axis (around Z axis), Turning around (0=Forward, +Right, -Left)
Roll - Rotation around the forward axis (around X axis), Tilting your head, (0=Straight, +Clockwise, -CCW)

Output(s):
Rotator - Rotator output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Transform |
| Type | [FMakeRotatorDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeRotatorDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pitch | Rotation around the right axis (around Y axis), Looking up and down (0=Straight Ahead, +Up, -Down) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Yaw | Rotation around the up axis (around Z axis), Turning around (0=Forward, +Right, -Left) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Roll | Rotation around the forward axis (around X axis), Tilting your head, (0=Straight, +Clockwise, -CCW) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Rotator | Rotator output | [FRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makesizedoutfit.md

# MakeSizedOutfit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSizedOutfit

> Application Version: 5.7

### Description

MakeSizedOutfit (v1)
Experimental

Add multiple cloth asset objects to an outfit collection.

Output(s):
Outfit - The outfit output.
OutfitCollection - The outfit collection output, provided for convenience as a view into the outfit object metadata.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Cloth Asset Make Sized Outfit |
| Type | FChaosOutfitAssetMakeSizedOutfitNode |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit output. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| OutfitCollection | The outfit collection output, provided for convenience as a view into the outfit object metadata. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makesphere.md

# MakeSphere

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSphere

> Application Version: 5.7

### Description

MakeSphere (v1)

Description for this node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Sphere |
| Type | [FMakeSphereDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeSphereDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Center |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Radius |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Sphere |  | [FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makespheremesh.md

# MakeSphereMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSphereMesh

> Application Version: 5.7

### Description

MakeSphereMesh (v1)

Make a sphere mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeSphereMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeSphereMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius | Sphere Radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| NumPhi | Sphere numphi | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |
| NumTheta | Sphere numtheta | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makestairmesh.md

# MakeStairMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeStairMesh

> Application Version: 5.7

### Description

MakeStairMesh (v1)

Make a stair mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeStairMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeStairMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StairType | Type of staircase | [EDataflowStairTypeEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowStairTypeEnum) | Linear |
| NumSteps | The number of steps in this staircase. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| StepWidth | The width of each step. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 150.000000 |
| StepHeight | The height of each step. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 20.000000 |
| StepDepth | The height of each step. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 30.000000 |
| CurveAngle | Inner radius of the curved staircase | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 90.000000 |
| InnerRadius | Curve angle of the staircase (in degrees) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 150.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-maketorusmesh.md

# MakeTorusMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeTorusMesh

> Application Version: 5.7

### Description

MakeTorusMesh (v1)

Make a torus mesh

Input(s) :
Origin - Torus will be translated so that center is at this point

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeTorusMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeTorusMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius1 | Radius of the profile | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 4.000000 |
| ProfileVertexCount | Number of vertices on the profile | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |
| Radius2 | Radius of sweep curve | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| SweepVertexCount | Number of vertices on the sweep curve | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | Torus will be translated so that center is at this point | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-maketransform.md

# MakeTransform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeTransform

> Application Version: 5.7

### Description

MakeTransform (v1)

Make an FTransform
Note: Originaly this version was depricated and replaced with FMakeTransformDataflowNode\_v2 but when AnyRotationType was
introduced with the ConvertAnyRotation node FMakeTransformDataflowNode\_v2 became obsolete and this version became the current version again

Input(s) :
InTranslation - Translation
InRotation - Rotation as Euler
InScale - Scale

Output(s):
OutTransform - Result transform

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Transform |
| Type | [FMakeTransformDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeTransformDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InTranslation | Translation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| InRotation | Rotation as Euler | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| InScale | Scale | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutTransform | Result transform | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makevector2.md

# MakeVector2

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector2

> Application Version: 5.7

### Description

MakeVector2 (v1)

Make a 2D Vector

Input(s) :
X - X component
Y - Y component

Output(s):
Vector2D - 2D Vector {X, Y}

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Create Add 2D XY |
| Type | [FDataflowVectorMakeVec2Node](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorMakeVec2Node) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X | X component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Y | Y component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector2D | 2D Vector {X, Y} | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makevector3.md

# MakeVector3

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector3

> Application Version: 5.7

### Description

MakeVector3 (v1)

Make a 3D Vector

Input(s) :
X - X component
Y - Y component
Z - Z component

Output(s):
Vector3D - 3D Vector {X, Y, Z}

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Create Add 3D XYZ |
| Type | [FDataflowVectorMakeVec3Node](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorMakeVec3Node) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X | X component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Y | Y component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Z | Z component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector3D | 3D Vector {X, Y, Z} | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makevector4.md

# MakeVector4

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector4

> Application Version: 5.7

### Description

MakeVector4 (v1)

Make a 4D Vector

Input(s) :
X - X component
Y - Y component
Z - Z component
W - W component

Output(s):
Vector4D - 4D Vector {X, Y, Z, W}

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Create Add 4D XYZW |
| Type | [FDataflowVectorMakeVec4Node](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorMakeVec4Node) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X | X component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Y | Y component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Z | Z component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| W | W component | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector4D | 4D Vector {X, Y, Z, W} | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-materialinterfacetextureoverride.md

# MaterialInterfaceTextureOverride

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MaterialInterfaceTextureOverride

> Application Version: 5.7

### Description

MaterialInterfaceTextureOverride (v1)
Experimental

Duplicate the given material and replace the target texture with the override texture on the newly-created material

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Materials |
| Tags | Material Texture Override |
| Type | [FMaterialInterfaceTextureOverrideDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMaterialInterfaceTextureOverrid-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Material |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> | None |
| TargetTexture |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> | None |
| OverrideTexture |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Material |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-mathexpression.md

# MathExpression

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MathExpression

> Application Version: 5.7

### Description

MathExpression (v1)

Expression node for floats

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math |
| Type | [FMathExpressionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMathExpressionDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Expression |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| B |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| C |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| D |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-maximum.md

# Maximum

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Maximum

> Application Version: 5.7

### Description

Maximum (v2)

Maximum ( Max(A, B, C, ... ) )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Highest Larger |
| Type | [FDataflowMathMaximumNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathMaximumNode_v2) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-mergeclothcollections.md

# MergeClothCollections

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeClothCollections

> Application Version: 5.7

### Description

MergeClothCollections (v2)

Merge multiple cloth collections into a single cloth collection of multiple patterns.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Merge Collection |
| Type | [FChaosClothAssetMergeClothCollectionsNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_5) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-mergeconvexhulls.md

# MergeConvexHulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeConvexHulls

> Application Version: 5.7

### Description

MergeConvexHulls (v1)

Merge convex hulls on transforms with multiple hulls

Input(s) :
MaxConvexCount - Maximum number of convex to generate per transform. Ignored if < 0.
ErrorTolerance - Error tolerance to use to decide to merge leaf convex together.
This is in centimeters and represents the side of a cube, the volume of which will be used as threshold
to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex
OptionalSelectionFilter - Optional transform selection to compute cluster hulls on -- if not provided, all cluster hulls will be computed.
bProtectNegativeSpace - Whether to use a sphere cover to define negative space that should not be covered by convex hulls
TargetNumSamples - Approximate number of spheres to consider when covering negative space. Only applicable with the Uniform Sample Method or if Require Search Sample Coverage is disabled.
MinSampleSpacing - Minimum desired spacing between spheres; if > 0, will attempt not to place sphere centers closer than this
NegativeSpaceTolerance - Amount of space to leave between convex hulls and protected negative space
MinRadius - Spheres smaller than this are not included in the negative space

Output(s):
SphereCovering - A representation of the negative space protected by the 'protect negative space' option. If negative space is not protected, this will contain zero spheres.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FMergeConvexHullsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMergeConvexHullsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MergeProximityFilter | Filter to optionally only consider spatially close convex hulls for merges | [EConvexHullProximityFilter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/EConvexHullProximityFilter) | None |
| MergeProximityDistanceThreshold | If applying a convex hull proximity filter, the distance threshold to use for determining that two convex hulls are close enough to merge | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| bComputeNegativeSpacePerBone | Whether to compute separate negative space for each bone. Otherwise, a single negative space will be computed once and re-used for all bones. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SampleMethod | Method to use to find and sample negative space | [ENegativeSpaceSampleMethodDataflowEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ENegativeSpaceSampleMethodDatafl-) | Uniform |
| bRequireSearchSampleCoverage | Whether to require that all candidate locations identified by Voxel Search are covered by negative space samples, up to the specified Min Sample Spacing. Only applies to Voxel Search. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bOnlyConnectedToHull | When performing Voxel Search, only look for negative space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration. Only applies to Voxel Search. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SphereCoveringDebugDrawRenderSettings |  | [FDataflowNodeSphereCoveringDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeSphereCoveringDebug-) | (bDisplaySphereCovering=False,RenderType=Wireframe,bTranslucent=True,LineWidthMultiplier=0.250000,ColorMethod=Single,Color=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),ColorRandomSeed=0,ColorA=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),ColorB=(R=0.000000,G=0.000000,B=1.000000,A=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| MaxConvexCount | Maximum number of convex to generate per transform. Ignored if < 0. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| ErrorTolerance | Error tolerance to use to decide to merge leaf convex together. This is in centimeters and represents the side of a cube, the volume of which will be used as threshold to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex | double | 0.000000 |
| OptionalSelectionFilter | Optional transform selection to compute cluster hulls on -- if not provided, all cluster hulls will be computed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| bProtectNegativeSpace | Whether to use a sphere cover to define negative space that should not be covered by convex hulls | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| TargetNumSamples | Approximate number of spheres to consider when covering negative space. Only applicable with the Uniform Sample Method or if Require Search Sample Coverage is disabled. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 50 |
| MinSampleSpacing | Minimum desired spacing between spheres; if > 0, will attempt not to place sphere centers closer than this | double | 1.000000 |
| NegativeSpaceTolerance | Amount of space to leave between convex hulls and protected negative space | double | 2.000000 |
| MinRadius | Spheres smaller than this are not included in the negative space | double | 10.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SphereCovering | A representation of the negative space protected by the 'protect negative space' option. If negative space is not protected, this will contain zero spheres. | [FDataflowSphereCovering](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowSphereCovering) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-mergeincollection.md

# MergeInCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeInCollection

> Application Version: 5.7

### Description

MergeInCollection (v1)

Merges selected bones into a single bone

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to merge
TransformSelection [Intrinsic] - Transform selection for merging

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to merge

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Edit |
| Type | [FMergeInCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMergeInCollectionDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to merge | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Transform selection for merging | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to merge | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-mergeoutfits.md

# MergeOutfits

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeOutfits

> Application Version: 5.7

### Description

MergeOutfits (v1)
Experimental

Merge multiple outfits into a single outfits.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Merge Outfits |
| Type | FChaosOutfitAssetMergeOutfitsNode |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-mergeuvislands.md

# MergeUVIslands

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeUVIslands

> Application Version: 5.7

### Description

MergeUVIslands (v1)

Merge adjacent UV Islands with similar normals for a specific UV channel

Input(s) :
Collection [Intrinsic] - Target Collection
FaceSelection - Faces to auto unwrap, no selection means all faces
UVChannel - UV channel to unwrap into ( 0 by default )
AreaDistortionThreshold - Threshold for allowed area distortion from merging islands (when we use ExpMap to compute new UVs for the merged island)
MaxNormalDeviationDeg - Threshold for allowed normal deviation between merge-able islands
NormalSmoothingRounds - Amount of normal smoothing to apply when computing new UVs for merged islands. More smoothing will result in UV maps that are less sensitive to local surface shape.
NormalSmoothingAlpha - Strength of normal smoothing to apply when computing new UVs for merged islands. Stronger smoothing will result in UV maps that are less sensitive to local surface shape.

Output(s):
Collection [Passthrough] - Target Collection
UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default )

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|UV |
| Type | [FMergeUVIslandsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMergeUVIslandsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | Faces to auto unwrap, no selection means all faces | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| AreaDistortionThreshold | Threshold for allowed area distortion from merging islands (when we use ExpMap to compute new UVs for the merged island) | double | 1.500000 |
| MaxNormalDeviationDeg | Threshold for allowed normal deviation between merge-able islands | double | 45.000000 |
| NormalSmoothingRounds | Amount of normal smoothing to apply when computing new UVs for merged islands. More smoothing will result in UV maps that are less sensitive to local surface shape. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| NormalSmoothingAlpha | Strength of normal smoothing to apply when computing new UVs for merged islands. Stronger smoothing will result in UV maps that are less sensitive to local surface shape. | double | 0.250000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshappend.md

# MeshAppend

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshAppend

> Application Version: 5.7

### Description

MeshAppend (v1)

Appends two meshes

Input(s) :
Mesh1 [Intrinsic] - Mesh input
Mesh2 [Intrinsic] - Mesh input

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FMeshAppendDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshAppendDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh1 | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| Mesh2 | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshboolean.md

# MeshBoolean

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshBoolean

> Application Version: 5.7

### Description

MeshBoolean (v1)

Compute a Mesh Boolean between Mesh1 and Mesh2

Supported Boolean Operations:
Union (Mesh1 + Mesh2)
Difference (Mesh1 - Mesh2; removing what's inside of Mesh2 from Mesh1)
Intersection (Mesh1 & Mesh2; removing what's outside of Mesh2 from Mesh1)

Input(s) :
Mesh1 [Intrinsic] - Mesh input
Mesh2 [Intrinsic] - Mesh input

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryDataflowNodes) |
| Category | Mesh|Utilities |
| Type | [FMeshBooleanDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryDataflowNodes/FMeshBooleanDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Boolean operation | [EMeshBooleanOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryDataflowNodes/EMeshBooleanOperationEnum) | Dataflow\_MeshBoolean\_Intersect |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh1 | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| Mesh2 | Mesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshconstraineddeformationtestplayground.md

# MeshConstrainedDeformationTestPlayground

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground

> Application Version: 5.7

### Description

MeshConstrainedDeformationTestPlayground (v1)
Experimental

Mesh Constrained Deformation Node

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Constrained Deformation |
| Type | FMeshConstrainedDeformationNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Iterations |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| bEnableShearConstraint | Remove shear deformation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ShearConstraintStrength |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bEnableBendingConstraint |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| BendingConstraintStrength |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bEnableEdgeConstraint |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| EdgeConstraintStrength |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Gravity |  | [FVector3d](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizingMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| BaseMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| InvMass |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| EdgeConstraintWeights |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizingMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshcutter.md

# MeshCutter

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter

> Application Version: 5.7

### Description

MeshCutter (v1)

Editor Fracture Mode / Fracture / Mesh tool
Fracture using the shape of a chosen static mesh and/or array of dynamic meshes

Input(s) :
Collection [Intrinsic] - Collection to cut
BoundingBox - Boundingbox to create the cutting planes in
TransformSelection - The selected pieces to cut
Transform - Transform to apply to cut planes
CuttingDynamicMeshes - Dynamic Meshes to cut with
CuttingStaticMesh - Static Mesh to cut with
NumberToScatter - Number of meshes to random scatter
GridX - Number of meshes to add to grid in X
GridY - Number of meshes to add to grid in Y
GridZ - Number of meshes to add to grid in Z
Variability - Magnitude of random displacement to cutting meshes
MinScaleFactor - Minimum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max
MaxScaleFactor - Maximum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max
RollRange - Roll will be chosen between -Range and +Range
PitchRange - Pitch will be chosen between -Range and +Range
YawRange - Yaw will be chosen between -Range and +Range
RandomSeed - Seed for random
ChanceToFracture - Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to cut
TransformSelection [Passthrough] - The selected pieces to cut
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FMeshCutterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshCutterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseHiRes | If using a Static Mesh to cut, attempt to use the Nanite HiRes source mesh, if available and non-empty. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| LODLevel | If using a Static Mesh to cut, and not using the Nanite HiRes source mesh, use this LOD level's mesh | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| CutDistribution | How to arrange the mesh cuts in space | [EMeshCutterCutDistribution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EMeshCutterCutDistribution) | SingleCut |
| PerCutMeshSelection | When there are multiple cutting meshes, how to choose the cut mesh to apply at each location | [EMeshCutterPerCutMeshSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EMeshCutterPerCutMeshSelection) | All |
| bRandomOrientation | Whether to randomly vary the orientation of the cutting meshes | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoundingBox | Boundingbox to create the cutting planes in | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Transform | Transform to apply to cut planes | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| CuttingStaticMesh | Static Mesh to cut with | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| CuttingDynamicMeshes | Dynamic Meshes to cut with | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |
| NumberToScatter | Number of meshes to random scatter | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| GridX | Number of meshes to add to grid in X | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| GridY | Number of meshes to add to grid in Y | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| GridZ | Number of meshes to add to grid in Z | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| Variability | Magnitude of random displacement to cutting meshes | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MinScaleFactor | Minimum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| MaxScaleFactor | Maximum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.500000 |
| RollRange | Roll will be chosen between -Range and +Range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| PitchRange | Pitch will be chosen between -Range and +Range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| YawRange | Yaw will be chosen between -Range and +Range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ChanceToFracture | Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshinfo.md

# MeshInfo

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshInfo

> Application Version: 5.7

### Description

MeshInfo (v1)

Collects information from the DynamicMesh and outputs it into a formatted string

Input(s) :
Mesh [Intrinsic] - DynamicMesh for the information

Output(s):
InfoString - Formatted output string

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FMeshInfoDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshInfoDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DynamicMesh for the information | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InfoString | Formatted output string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshtocollection.md

# MeshToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshToCollection

> Application Version: 5.7

### Description

MeshToCollection (v1)

Converts a DynamicMesh to a Collection

Input(s) :
Mesh [Intrinsic] - DynamicMesh to convert
bSplitIslands - Whether to split the mesh into multiple bones based on the mesh connectivity
bAddClusterRootForSingleMesh - Whether to add a root cluster for the single mesh case. Note if the mesh is split, the root cluster will always be added.

Output(s):
Collection - Output Collection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FMeshToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshToCollectionDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bConnectIslandsByVertexOverlap | Whether to consider coincident vertices as connected even if the topology does not connect them | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ConnectVerticesThreshold | Vertices closer than this distance are considered to be overlapping | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.001000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DynamicMesh to convert | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| bSplitIslands | Whether to split the mesh into multiple bones based on the mesh connectivity | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bAddClusterRootForSingleMesh | Whether to add a root cluster for the single mesh case. Note if the mesh is split, the root cluster will always be added. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Output Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshwarp.md

# MeshWarp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWarp

> Application Version: 5.7

### Description

MeshWarp (v1)
Experimental

Mesh Warp Node

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Warp |
| Type | FMeshWarpNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Alpha |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| WarpMethod |  | EMeshResizingWarpMethod | RBFInterpolate |
| NumInterpolationPoints |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| bInterpolateNormals |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshToResize |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| SourceMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| TargetMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BlendedTargetMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| ResizedMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshwrap.md

# MeshWrap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap

> Application Version: 5.7

### Description

MeshWrap (v1)
Experimental

Dataflow node for wrapping one mesh's topology to another mesh's shape. Uses point landmarks defined by the Mesh Wrap Landmarks node to match corresponding points between the two meshes.

Input(s) :
SourceTopologyMesh - Input mesh with the desired wrapped mesh topology.
TargetShapeMesh - Input mesh with the desired wrapped mesh shape.
SourceTopologyLandmarks - Landmarks defined on SourceTopologyMesh. TargetShapeLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap.
TargetShapeLandmarks - Landmarks defined on TargetShapeMesh. SourceTopologyLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap.

Output(s):
WrappedMesh - Output wrapped mesh.
MatchedLandmarks - Landmarks matched by Identifier from SourceTopologyLandmarks and TargetShapeLandmarks.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Wrap |
| Type | [FMeshWrapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaxNumOuterIterations | Mesh Wrap is calculated with an inner and outer loop. This is the maximum number of outer loops. Each outer loop increases the Projection Stiffness by ProjectionStiffnessMultiplier. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| NumInnerIterations | Mesh Wrap is calculated with an inner and outer loop. This is the number of inner loops run before increasing the Projection Stiffness in the outer loop. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| ProjectionTolerance | Mesh Wrap will terminate early if the Projection tolerance is within this threshold. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000100 |
| LaplacianStiffness | Weight of mesh wrap to retain Source Topology mesh features. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| InitialProjectionStiffness | Initial weight of mesh wrap to match projected Target Shape. Each outer loop will multiply this stiffness by ProjectionStiffnessMultiplier. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| ProjectionStiffnessMuliplier | Each outer loop will multiply InitialProjectionStiffness by this to improve Target Shape match. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CorrespondenceStiffness | Weight of mesh wrap to match Landmark correspondences. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DefaultDisplayMaterial | Display material for Source or Target when none is supplied. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterial](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterial)> | None |
| bDisplayLandmarks | Display landmarks. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bDisplaySource | Draw source mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SourceDisplayOffset | Offset of source mesh display for side-by-side drawing. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -150.000000 |
| bDisplayTarget | Draw target mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| TargetDisplayOffset | Offset of target mesh display for side-by-side drawing. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 150.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceTopologyMesh | Input mesh with the desired wrapped mesh topology. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| TargetShapeMesh | Input mesh with the desired wrapped mesh shape. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| SourceTopologyLandmarks | Landmarks defined on SourceTopologyMesh. TargetShapeLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapLandmark](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapLandmark)> |  |
| TargetShapeLandmarks | Landmarks defined on TargetShapeMesh. SourceTopologyLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapLandmark](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapLandmark)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| WrappedMesh | Output wrapped mesh. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| MatchedLandmarks | Landmarks matched by Identifier from SourceTopologyLandmarks and TargetShapeLandmarks. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapCorrespondence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapCorrespondence)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-meshwraplandmarks.md

# MeshWrapLandmarks

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrapLandmarks

> Application Version: 5.7

### Description

MeshWrapLandmarks (v1)
Experimental

Node for defining landmarks used by MeshWrapNode. The Mesh Wrap Landmark Selection Tool allows generating these landmarks via selection.

Input(s) :
Mesh - The mesh to define landmarks on.

Output(s):
Mesh [Passthrough] - The mesh to define landmarks on.
Landmarks - The defined landmarks (identifier, vertex pair). Can be hand-input/edited or generated using the Mesh Wrap Landmark Selection Tool

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Wrap Landmarks |
| Type | [FMeshWrapLandmarksNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapLandmarksNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PointSize | Point size of displayed landmarks | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| bShowIndex | Display the landmark indices | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bShowIdentifier | Display the landmark identifier strings | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | The mesh to define landmarks on. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | The mesh to define landmarks on. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| Landmarks | The defined landmarks (identifier, vertex pair). Can be hand-input/edited or generated using the Mesh Wrap Landmark Selection Tool | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapLandmark](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapLandmark)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-minimum.md

# Minimum

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Minimum

> Application Version: 5.7

### Description

Minimum (v2)

Minimum ( Min(A, B, C, ... ) )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Lowest Smallest |
| Type | [FDataflowMathMinimumNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathMinimumNode_v2) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-multiply.md

# Multiply

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Multiply

> Application Version: 5.7

### Description

Multiply (v1)

Multiplication (A \* B)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | \* Multiplication Time |
| Type | [FDataflowMathMultiplyNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathMultiplyNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| B |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-multiplytransform.md

# MultiplyTransform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MultiplyTransform

> Application Version: 5.7

### Description

MultiplyTransform (v1)

Description for this node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Transform |
| Type | [FMultiplyTransformDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMultiplyTransformDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InLeftTransform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| InRightTransform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutTransform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-multiplyvector.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-negate.md

# Negate

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Negate

> Application Version: 5.7

### Description

Negate (v1)

Negate ( -A )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Minus Negative |
| Type | [FDataflowMathNegateNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathNegateNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-noisefield.md

# NoiseField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/NoiseField

> Application Version: 5.7

### Description

NoiseField (v1)

Noise Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FNoiseFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FNoiseFieldDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| MinRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Transform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-nonuniformpointsampling.md

# NonUniformPointSampling

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/NonUniformPointSampling

> Application Version: 5.7

### Description

NonUniformPointSampling (v1)

NonUniform Sampling on a DynamicMesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to sample points on
SamplingRadius - Desired "radius" of sample points. Spacing between samples is at least 2x this value.
MaxNumSamples - Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled
SubSampleDensity - Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results.
RandomSeed - Random Seed used to initialize sampling strategies
MaxSamplingRadius - If MaxSampleRadius > SampleRadius, then output sample radius will be in range [SampleRadius, MaxSampleRadius]
SizeDistributionPower - SizeDistributionPower is used to control how extreme the Size Distribution shift is. Valid range is [1,10]

Output(s):
SamplePoints - Sampled positions on the mesh
SampleRadii - Sampled radii
SampleTriangleIDs - Sampled triangleID
SampleBarycentricCoords - Barycentric Coordinates of each Sample Point in it's respective Triangle.
NumSamplePoints - Number of Sampled positions on the mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | [FNonUniformPointSamplingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FNonUniformPointSamplingDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SizeDistribution | SizeDistribution setting controls the distribution of sample radii | [ENonUniformSamplingDistributionMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/ENonUniformSamplingDistributionM-) | ENonUniformSamplingDistributionMode\_Uniform |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to sample points on | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SamplingRadius | Desired "radius" of sample points. Spacing between samples is at least 2x this value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MaxNumSamples | Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SubSampleDensity | Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| RandomSeed | Random Seed used to initialize sampling strategies | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MaxSamplingRadius | If MaxSampleRadius > SampleRadius, then output sample radius will be in range [SampleRadius, MaxSampleRadius] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| SizeDistributionPower | SizeDistributionPower is used to control how extreme the Size Distribution shift is. Valid range is [1,10] | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Sampled positions on the mesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleRadii | Sampled radii | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| SampleTriangleIDs | Sampled triangleID | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleBarycentricCoords | Barycentric Coordinates of each Sample Point in it's respective Triangle. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePoints | Number of Sampled positions on the mesh | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-normalizetorange.md

# NormalizeToRange

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/NormalizeToRange

> Application Version: 5.7

### Description

NormalizeToRange (v1)

Returns Float normalized to the given range

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FNormalizeToRangeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FNormalizeToRangeDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Float |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RangeMin |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RangeMax |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-normalizevector.md

# NormalizeVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/NormalizeVector

> Application Version: 5.7

### Description

NormalizeVector (v1)

Normalize a vector : Normalized = V/|V|

Input(s) :
V - Vector to normalize

Output(s):
Normalized - Normalized vector : Normalized=V/|V|

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Type | [FDataflowVectorNormalize](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorNormalize) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Vector to normalize | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |  |  |
| --- | --- | --- | --- | --- | --- |
| Normalized | Normalized vector : Normalized=V/ | V |  | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-oneminus.md

# OneMinus

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OneMinus

> Application Version: 5.7

### Description

OneMinus (v1)

One minus (1 - A)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Type | [FDataflowMathOneMinusNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathOneMinusNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-outfitassetterminal.md

# OutfitAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitAssetTerminal

> Application Version: 5.7

### Description

OutfitAssetTerminal (v1)
Experimental

Outfit terminal node to generate an outfit asset from several cloth assets.

Input(s) :
Outfit - Input outfit collection.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Terminal |
| Type | FChaosOutfitAssetTerminalNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ConvertToSkeletalMesh | Convert this outfit to a SkeletalMesh asset. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | Input outfit collection. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-outfitquery.md

# OutfitQuery

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery

> Application Version: 5.7

### Description

OutfitQuery (v1)

Query an Outfit about its properties.

Input(s) :
Outfit - Input/output collection (Output is always a passthrough)

Output(s):
Outfit [Passthrough] - Input/output collection (Output is always a passthrough)
bHasAnyValidPieces - Has this outfit any valid pieces?
bHasAnyValidBodySizes - Has this outfit any valid body sizes?

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Query |
| Type | FChaosOutfitAssetOutfitQueryNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bBodyPartMustExist | Check that body parts are present in the asset registry when checking for valid body sizes. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bMeasurementsMustExist | Check that measurements are valid when checking for valid body sizes. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bInterpolationDataMustExist | Check that some interpolation data exists when checking for valid body sizes. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | Input/output collection (Output is always a passthrough) | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | Input/output collection (Output is always a passthrough) | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| bHasAnyValidPieces | Has this outfit any valid pieces? | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasAnyValidBodySizes | Has this outfit any valid body sizes? | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-paintweightmap.md

# PaintWeightMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PaintWeightMap

> Application Version: 5.7

### Description

PaintWeightMap (v1)

Scalar vertex properties.

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Tags | Paint a weight map and save it to collection |
| Type | [FDataflowCollectionAddScalarVertexPropertyNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionAddScalarVert-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name to be set as a weight map attribute. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| TargetGroup |  | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| OverrideType | This type will define how the data are applied to the input data | [EDataflowWeightMapOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/EDataflowWeightMapOverrideType) | ReplaceAll |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey |  | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| AttributeKey |  | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-planecutter.md

# PlaneCutter

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PlaneCutter

> Application Version: 5.7

### Description

PlaneCutter (v2)

Editor Fracture Mode / Fracture / Planar tool
Fracture using a set of noised up planes.

Input(s) :
Collection [Intrinsic] - Collection to fracture
BoundingBox - Bound for plane centers
TransformSelection - Pieces to cut
Transform - Transform to bring the collection into the space of the cutting planes
CutPlanes - Cutting planes to use. The cut plane normal is aligned to the Z-up of the transform.
NumPlanes - Number of random cutting planes to add, in addition to those specified in the Cut Planes array
RandomSeed - Seed for random
ChanceToFracture - Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.
Grout - Amount of space to leave between cut pieces
Amplitude - Size of the Perlin noise displacement (in cm). If 0, no noise will be applied
Frequency - Period of the Perlin noise. Smaller values will create a smoother noise pattern
Persistence - Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor
Lacunarity - Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor
OctaveNumber - Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity
Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains
PointSpacing - Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to fracture
TransformSelection [Passthrough] - Pieces to cut
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FPlaneCutterDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FPlaneCutterDataflowNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderType |  | [EDataflowDebugDrawRenderType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/EDataflowDebugDrawRenderType) | Wireframe |
| PlaneSizeMultiplier |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.200000 |
| bTranslucent |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bRandomizeColors |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| LineWidthMultiplier |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to fracture | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoundingBox | Bound for plane centers | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| TransformSelection | Pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Transform | Transform to bring the collection into the space of the cutting planes | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| NumPlanes | Number of random cutting planes to add, in addition to those specified in the Cut Planes array | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| CutPlanes | Cutting planes to use. The cut plane normal is aligned to the Z-up of the transform. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ChanceToFracture | Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Grout | Amount of space to leave between cut pieces | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Amplitude | Size of the Perlin noise displacement (in cm). If 0, no noise will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Frequency | Period of the Perlin noise. Smaller values will create a smoother noise pattern | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| Persistence | Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Lacunarity | Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| OctaveNumber | Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| PointSpacing | Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 20.000000 |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to fracture | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Pieces to cut | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-planefallofffield.md

# PlaneFalloffField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PlaneFalloffField

> Application Version: 5.7

### Description

PlaneFalloffField (v1)

PlaneFalloff Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FPlaneFalloffFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FPlaneFalloffFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FalloffType |  | [EDataflowFieldFalloffType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowFieldFalloffType) | Dataflow\_FieldFalloffType\_Linear |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Position |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Normal |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| Distance |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Translation |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MinRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Default |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldSelectionMask |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-pointstocollection.md

# PointsToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PointsToCollection

> Application Version: 5.7

### Description

PointsToCollection (v1)

Add point cloud to a collection as vertices

Input(s) :
Collection [Intrinsic] - Collection to add the points to
Points - Points to add to the collection

Output(s):
Collection [Passthrough] - Collection to add the points to

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FPointsToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FPointsToCollectionDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to add the points to | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Points | Points to add to the collection | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to add the points to | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-pointstomesh.md

# PointsToMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PointsToMesh

> Application Version: 5.7

### Description

PointsToMesh (v1)

Converts points into a DynamicMesh

Input(s) :
Points [Intrinsic] - Points input

Output(s):
Mesh - Mesh output
TriangleCount - Mesh triangle count

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FPointsToMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FPointsToMeshDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Points input | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Mesh output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| TriangleCount | Mesh triangle count | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-pow.md

# Pow

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Pow

> Application Version: 5.7

### Description

Pow (v1)

power ( A ^ B)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Power Exponent |
| Type | [FDataflowMathPowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathPowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| B |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-print.md

# Print

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Print

> Application Version: 5.7

### Description

Print (v1)

Print value in the log
Supports any type comnvertible to a string

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Core |
| Type | [FDataflowPrintNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowPrintNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value |  | [FDataflowStringConvertibleTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowStringConvertibleTypes) | (Value="") |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-proceduralselection.md

# ProceduralSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ProceduralSelection

> Application Version: 5.7

### Description

ProceduralSelection (v1)

Procedurally generate a Cloth Selection set.

Input(s) :
ConversionInputName - Selection set to convert from when using Conversion selection type.

Output(s):
OutputName - The name to be use as a selection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Procedural Selection |
| Type | [FChaosClothAssetProceduralSelectionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetProceduralSelect-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Group | The type of element the selection refers to | [FChaosClothAssetNodeSelectionGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetNodeSelectionGro-) | (Name="") |
| SelectionType | The procedural selection method | [EChaosClothAssetProceduralSelectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetProceduralSelect-) | SelectAll |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| OutputName | The name to be use as a selection. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-proximity.md

# Proximity

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity

> Application Version: 5.7

### Description

Proximity (v1)

Update the proximity (contact) graph for the bones in a Collection

Input(s) :
DistanceThreshold - If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors
ContactThreshold - If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity
Collection [Intrinsic] - GeometryCollection to update the proximity graph on

Output(s):
Collection [Passthrough] - GeometryCollection to update the proximity graph on

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FProximityDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FProximityDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ProximityMethod | Which method to use to decide whether a given piece of geometry is in proximity with another | [EProximityMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EProximityMethodEnum) | Dataflow\_ProximityMethod\_Precise |
| FilterContactMethod | How to use the Contact Threshold (if > 0) to filter out unwanted small or corner contacts from the proximity graph. If contact threshold is zero, no filtering is applied. | [EProximityContactFilteringMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EProximityContactFilteringMethod-) | Dataflow\_ProximityContactFilteringMethod\_ProjectedBoundsOverlap |
| bUseAsConnectionGraph | Whether to automatically transform the proximity graph into a connection graph to be used for simulation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ContactAreaMethod | The method used to compute contact areas for simulation purposes (only when 'Use As Connection Graph' is enabled) | [EConnectionContactAreaMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EConnectionContactAreaMethodEnum) | Dataflow\_ConnectionContactAreaMethod\_None |
| bRecomputeConvexHulls | Whether to compute new convex hulls for proximity, or use the pre-existing hulls on the Collection, when using convex hulls to determine proximity | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color |  | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=0.000000,A=1.000000) |
| LineWidthMultiplier |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| CenterColor |  | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| CenterSize |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 12.000000 |
| bRandomizeColor | Randomize color per connection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to update the proximity graph on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DistanceThreshold | If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ContactThreshold | If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to update the proximity graph on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-proxydeformer.md

# ProxyDeformer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ProxyDeformer

> Application Version: 5.7

### Description

ProxyDeformer (v3)

Adds the proxy deformer information to this cloth collection's render data.
This version will include the render tangents when generating the proxy deformer data by default (matches the default behavior if no proxy deformer node is added).

This node is only required to selectively assign specific areas of the render mesh to the sim mesh in the proxy deformer data.
When this node isn't provided to the construction graph, default proxy deformer data are automatically generated.
This node can be used to either override or remove the default proxy deformer data.

To enable deformer areas, selection filter sets must be provided.
With no selection filter sets, the Cloth Asset is by default fully skinned.
When more selection filter sets are needed, right-click on the node and do AddOptionPin to add more sets.
Each selection filter set is composed by two selections:

* A render mesh selection (natively a RenderVertices selection, but RenderFaces selections can also be used).
* A simulation mesh selection (natively a SimFaces selection, but SimVertices3D and SimVertices2D selections can also be used).
  The render mesh selection of vertices will then only be deformed by the associated simulation mesh selection of faces.
  The Proxy Deformer node evaluations are usually slower than the equivalent default proxy deformer due to the added processing cost
  of the selection filter sets. When in use, it is therefore better to place it earlier in the graph.

A default SkinningBlend weight map is also generated by the node that masks the areas for which selection filters aren't provided.
The map can then be painted, or replaced by a smoothed transition map generated by the SkinningBlend node.
The SkinningBlend node can leverage information about the kinematic areas added by the MaxDistanceConfig node.
Unlike the default SkinningBlend weight map provided by the Proxy Deformer node, the SkinningBlend node generates areas of smooth
transition where the render mesh vertices can be simultaneously skinned and deformed by the cloth.

To sum up:

* No ProxyDeformer node -> The Cloth Asset is fully deformed.
* ProxyDeformer node without selection filters -> The Cloth Asset is fully skinned.
* ProxyDeformer node with selection filters -> the Cloth Asset is partially deformed/skinned.
* The ProxyDeformer can be slow to evaluate, always place it as early as possible in the graph to avoid costly re-evaluations.
* A SkinningBlend node placed after the MaxDistanceConfig adds smooth transitions between the skinned and proxy deformed areas.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Proxy Deformer |
| Type | [FChaosClothAssetProxyDeformerNode\_v3](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetProxyDeformerNod-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-pruneincollection.md

# PruneInCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/PruneInCollection

> Application Version: 5.7

### Description

PruneInCollection (v1)

Deletes selected bones from Collection. Empty clusters will be eliminated

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to prune
TransformSelection [Intrinsic] - Transform selection for pruning

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to prune

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Edit |
| Type | [FPruneInCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FPruneInCollectionDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to prune | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Transform selection for pruning | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to prune | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-radialfallofffield.md

# RadialFalloffField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialFalloffField

> Application Version: 5.7

### Description

RadialFalloffField (v1)

RadialFalloff Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FRadialFalloffFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRadialFalloffFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FalloffType |  | [EDataflowFieldFalloffType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowFieldFalloffType) | Dataflow\_FieldFalloffType\_Linear |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Sphere |  | [FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Center=(X=0.000000,Y=0.000000,Z=0.000000),W=0.000000) |
| Translation |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MinRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Default |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldSelectionMask |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-radialintmaskfield.md

# RadialIntMaskField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialIntMaskField

> Application Version: 5.7

### Description

RadialIntMaskField (v1)

RadialIntMask Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FRadialIntMaskFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRadialIntMaskFieldDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SetMaskConditionType |  | [EDataflowSetMaskConditionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowSetMaskConditionType) | Dataflow\_SetMaskConditionType\_Always |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Sphere |  | [FSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Center=(X=0.000000,Y=0.000000,Z=0.000000),W=0.000000) |
| Translation |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| InteriorValue |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| ExteriorValue |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldIntResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-radialscatterpoints.md

# RadialScatterPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialScatterPoints

> Application Version: 5.7

### Description

RadialScatterPoints (v2)

Radial Scatter Points Dataflow Node V 2

Input(s) :
BoundingBox - BoundingBox to generate points inside of
Center - Center of generated pattern
Normal - Normal to plane in which sites are generated
RandomSeed - Seed for random
AngularSteps - Number of angular steps
AngleOffset - Angle offset at each radial step (in degrees)
AngularNoise - Amount of global variation to apply to each angular step (in degrees)
Radius - Pattern radius (in cm)
RadialSteps - Number of radial steps
RadialStepExponent - Radial steps will follow a distribution based on this exponent, i.e., Pow(distance from center, RadialStepExponent)
RadialMinStep - Minimum radial separation between any two voronoi points (in cm)
RadialNoise - Amount of global variation to apply to each radial step (in cm)
RadialVariability - Amount to randomly displace each Voronoi site radially (in cm)
AngularVariability - Amount to randomly displace each Voronoi site in angle (in degrees)
AxialVariability - Amount to randomly displace each Voronoi site in the direction of the rotation axis (in cm)

Output(s):
Points - Generated points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FRadialScatterPointsDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRadialScatterPointsDataflowNode-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | BoundingBox to generate points inside of | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Center | Center of generated pattern | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Normal | Normal to plane in which sites are generated | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| AngularSteps | Number of angular steps | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| AngleOffset | Angle offset at each radial step (in degrees) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AngularNoise | Amount of global variation to apply to each angular step (in degrees) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Radius | Pattern radius (in cm) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |
| RadialSteps | Number of radial steps | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| RadialStepExponent | Radial steps will follow a distribution based on this exponent, i.e., Pow(distance from center, RadialStepExponent) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RadialMinStep | Minimum radial separation between any two voronoi points (in cm) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RadialNoise | Amount of global variation to apply to each radial step (in cm) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RadialVariability | Amount to randomly displace each Voronoi site radially (in cm) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AngularVariability | Amount to randomly displace each Voronoi site in angle (in degrees) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AxialVariability | Amount to randomly displace each Voronoi site in the direction of the rotation axis (in cm) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Generated points | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-radialtetrahedron.md

# RadialTetrahedron

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialTetrahedron

> Application Version: 5.7

### Description

RadialTetrahedron (v1)

@todo(deprecate), rename to FRadialTetrahedronDataflowNode

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FRadialTetrahedronDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FRadialTetrahedronDataflowNodes) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InnerRadius |  | double | 1.000000 |
| OuterRadius |  | double | 2.000000 |
| Height |  | double | 1.000000 |
| RadialSample |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| AngularSample |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| VerticalSample |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| BulgeRatio |  | double | 0.000000 |
| bDiscardInteriorTriangles |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-radialvectorfield.md

# RadialVectorField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialVectorField

> Application Version: 5.7

### Description

RadialVectorField (v1)

RadialVector Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FRadialVectorFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRadialVectorFieldDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Position |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldVectorResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-radtodeg.md

# RadToDeg

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadToDeg

> Application Version: 5.7

### Description

RadToDeg (v1)

RadToDeg(A) convert radians to degrees

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Trigonometry Circle Angle Degrees Radians Convert Unit |
| Type | [FDataflowMathRadToDegNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathRadToDegNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-randomfloat.md

# RandomFloat

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomFloat

> Application Version: 5.7

### Description

RandomFloat (v1)

Generates a random float

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Random |
| Type | [FRandomFloatDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRandomFloatDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeterministic |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RandomSeed |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -88439.585938 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-randomfloatinrange.md

# RandomFloatInRange

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomFloatInRange

> Application Version: 5.7

### Description

RandomFloatInRange (v1)

Generates a random float between Min and Max

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Random |
| Type | [FRandomFloatInRangeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRandomFloatInRangeDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeterministic |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RandomSeed |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 24063.851562 |
| Min |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Max |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-randomizefloatarray.md

# RandomizeFloatArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomizeFloatArray

> Application Version: 5.7

### Description

RandomizeFloatArray (v1)

Randomize elements in a float array (Random value will be in (RandomRangeMin, RandomRangeMax)

Input(s) :
FloatArray [Intrinsic] - Array to randomize
RandomRangeMin - Random range min
RandomRangeMax - Random range max
RandomSeed - Seed for random

Output(s):
FloatArray [Passthrough] - Array to randomize

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Type | [FRandomizeFloatArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRandomizeFloatArrayDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Array to randomize | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| RandomRangeMin | Random range min | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RandomRangeMax | Random range max | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RandomSeed | Seed for random | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Array to randomize | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-randomunitvector.md

# RandomUnitVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVector

> Application Version: 5.7

### Description

RandomUnitVector (v1)

Returns a random vector with length of 1

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Random |
| Type | [FRandomUnitVectorDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRandomUnitVectorDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeterministic |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RandomSeed |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -60588.394531 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-randomunitvectorincone.md

# RandomUnitVectorInCone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone

> Application Version: 5.7

### Description

RandomUnitVectorInCone (v1)

Returns a random vector with length of 1, within the specified cone, with uniform random distribution

Input(s) :
ConeDirection - The base "center" direction of the cone
ConeHalfAngle - The half-angle of the cone (from ConeDir to edge), in degrees

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Random |
| Type | [FRandomUnitVectorInConeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRandomUnitVectorInConeDataflowN-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeterministic |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RandomSeed |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -56694.234375 |
| ConeDirection | The base "center" direction of the cone | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| ConeHalfAngle | The half-angle of the cone (from ConeDir to edge), in degrees | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.785398 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-randomvectorfield.md

# RandomVectorField

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomVectorField

> Application Version: 5.7

### Description

RandomVectorField (v1)

RandomVector Field Dataflow node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FRandomVectorFieldDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRandomVectorFieldDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePositions |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleIndices |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| Magnitude |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldVectorResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-readskeletalmeshcurves.md

# ReadSkeletalMeshCurves

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReadSkeletalMeshCurves

> Application Version: 5.7

### Description

ReadSkeletalMeshCurves (v1)

Read Skeletal Mesh Curves Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FReadSkeletalMeshCurvesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FReadSkeletalMeshCurvesDataflowN-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ImportSKMCurveNames | Click on this button to import curve names from the skeletal mesh. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| AssignSKMCurveToMuscle | Click on this button to assign curve to muscles by name. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| CurveMuscleNameArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| GeometrySelection |  | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-recalculatenormals.md

# RecalculateNormals

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RecalculateNormals

> Application Version: 5.7

### Description

RecalculateNormals (v1)
Experimental

Recalculate the geometry's normals. Experimental, only does the render geometry.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Recalculate Simulation Render Mesh Normals |
| Type | [FChaosClothAssetRecalculateNormalsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetRecalculateNorma-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-reciprocal.md

# Reciprocal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Reciprocal

> Application Version: 5.7

### Description

Reciprocal (v1)

Reciprocal( 1 / A )
if A is equal to 0, returns Fallback

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | OneOver OneDividedBy |
| Type | [FDataflowMathReciprocalNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathReciprocalNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Fallback |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-recomputenormalsingeometrycollection.md

# RecomputeNormalsInGeometryCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RecomputeNormalsInGeometryCollection

> Application Version: 5.7

### Description

RecomputeNormalsInGeometryCollection (v1)

Editor Fracture Mode / Utilities / Normals tool
Recompute normals and tangents.

Input(s) :
Collection [Intrinsic] - Collection to use
TransformSelection - The selected pieces to use

Output(s):
Collection [Passthrough] - Collection to use

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FRecomputeNormalsInGeometryCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRecomputeNormal-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bOnlyTangents | Whether to only recompute tangents, and leave normals as they were | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bRecomputeSharpEdges | If true, update where edges are 'sharp' by comparing adjacent triangle face normals vs the Sharp Edge Angle Threshold. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SharpEdgeAngleThreshold | Threshold on angle of change in face normals across an edge, above which we create a sharp edge if bRecomputeSharpEdges is true | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 60.000000 |
| bOnlyInternalSurfaces | Whether to only change internal surface normals / tangents | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The selected pieces to use | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-referencebone.md

# ReferenceBone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReferenceBone

> Application Version: 5.7

### Description

ReferenceBone (v1)

Explicitly set the cloth Reference Bone (used when calculating SimulationVelocityScale). This will automatically computed as the bone closest to the root with weights if no valid Reference Bone is explicitly set.
Reference bones are shared by all LODs. Only the bones set for LOD0 will be used.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Reference Bone |
| Type | FChaosClothAssetReferenceBoneNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReferenceBone | Select the cloth reference bone. This will automatically computed as the bone closest to the root with weights if no valid Reference Bone is explicitly set. | FChaosClothAssetReferenceBoneSelection | (Name="") |
| CalculateDefaultReferenceBone |  | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-remesh.md

# Remesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Remesh

> Application Version: 5.7

### Description

Remesh (v2)

Remesh the cloth surface(s) to get the specified mesh resolution(s).
NOTE: Weight Maps, Skinning Data, Self Collision Spheres, and Long Range Attachment Constraints will be reconstructed on the output mesh, however all other Selections will be removed

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Remesh |
| Type | [FChaosClothAssetRemeshNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetRemeshNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bRemeshSim |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DensityMapSim | Range of target mesh resolutions, as a percentage of input triangle mesh resolution. A value of 50 on all vertices should roughly halve the total number of triangles. If a valid vertex weight map is specified, it will use vertex weights to interpolate between the Lo and Hi values. Otherwise it will use the Lo value on all vertices. | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=100.000000,High=200.000000,WeightMap="DensityMapSim",bImportFabricBounds=False,bBuildFabricMaps=False) |
| IterationsSim |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| SmoothingSim |  | double | 0.250000 |
| bRemeshRender |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RemeshMethodRender |  | [EChaosClothAssetRemeshMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetRemeshMethod) | Remesh |
| DensityMapRender | Range of target mesh resolutions when using the Remesh method, as a percentage of input triangle mesh resolution. A value of 50 on all vertices should roughly halve the total number of triangles. If a valid vertex weight map is specified, it will use vertex weights to interpolate between the Lo and Hi values. Otherwise it will use the Lo value on all vertices. | [FChaosClothAssetWeightedValueNonAnimatable](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=100.000000,High=200.000000,WeightMap="DensityMapRender",bImportFabricBounds=False,bBuildFabricMaps=False) |
| TargetPercentRender | Target mesh resolution when using the Simplify method, as a percentage of input triangle mesh resolution. A value of 50 should roughly halve the total number of triangles. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| IterationsRender |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| SmoothingRender |  | double | 0.250000 |
| bRemeshRenderSeams | If checked, attempt to find matching vertices along Render mesh boundaries and remesh these separately | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderSeamRemeshIterations | Number of remesh iterations over the Render mesh seams | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-removefloatarrayelement.md

# RemoveFloatArrayElement

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveFloatArrayElement

> Application Version: 5.7

### Description

RemoveFloatArrayElement (v1)

Removes the specified element from an array

Input(s) :
FloatArray [Intrinsic] - Array to remove the element from

Output(s):
FloatArray [Passthrough] - Array to remove the element from

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Type | [FRemoveFloatArrayElementDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRemoveFloatArrayElementDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | Element index | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bPreserveOrder | Preserve order, if order not important set it to false for faster computation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Array to remove the element from | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| Index | Element index | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Array to remove the element from | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-removeonbreak.md

# RemoveOnBreak

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak

> Application Version: 5.7

### Description

RemoveOnBreak (v1)

Remove on Break Dataflow Node

Input(s) :
Collection [Intrinsic] - Collection to set theremoval data on
TransformSelection - selection to apply the data on ( if not specified the entire collection will be set )
bEnabledRemoval - Whether or not to enable the removal on the selection
PostBreakTimer - How long after the break the removal will start ( Min / Max )
RemovalTimer - How long removal will last ( Min / Max )
bClusterCrumbling - If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect

Output(s):
Collection [Passthrough] - Collection to set theremoval data on

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FRemoveOnBreakDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRemoveOnBreakDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to set theremoval data on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | selection to apply the data on ( if not specified the entire collection will be set ) | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| bEnabledRemoval | Whether or not to enable the removal on the selection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| PostBreakTimer | How long after the break the removal will start ( Min / Max ) | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| RemovalTimer | How long removal will last ( Min / Max ) | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000) |
| bClusterCrumbling | If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to set theremoval data on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-reroutenode.md

# ReRouteNode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReRouteNode

> Application Version: 5.7

### Description

ReRouteNode (v1)

Dataflow Re Route Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Core |
| Type | [FDataflowReRouteNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowReRouteNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-resamplecurvepoints.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-resamplegeometrycollection.md

# ResampleGeometryCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ResampleGeometryCollection

> Application Version: 5.7

### Description

ResampleGeometryCollection (v1)

Editor Fracture Mode / Utilities / Resample tool
Resample to add collision particles in large flat regions that otherwise might have poor collision response.
Only useful to help improve Particle - Implicit collisions.

Input(s) :
Collection [Intrinsic] - Collection to use
TransformSelection - The selected pieces to use
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to use

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FResampleGeometryCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FResampleGeometryCollectionDataf-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The selected pieces to use | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-resampleguidespoints.md

# ResampleGuidesPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ResampleGuidesPoints

> Application Version: 5.7

### Description

ResampleGuidesPoints (v1)
Experimental

Resample the groom guides with a fixed number of points (in physics strands size)

Input(s) :
Collection - Managed array collection to be used to store datas

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Type | FResampleGuidesPointsDataflowNode |

### Inputs

| Name | Description | Type | DefaultValue |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

### Outputs

| Name | Description | Type |
| --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-reversenormals.md

# ReverseNormals

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals

> Application Version: 5.7

### Description

ReverseNormals (v1)

Reverse the geometry's normals or/and winding order of the simulation or/and render meshes stored in the cloth collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Reverse Simulation Render Mesh Normals |
| Type | [FChaosClothAssetReverseNormalsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetReverseNormalsNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimPatterns | List of sim patterns to apply the operation on. All patterns will be used if left empty. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bReverseSimMeshNormals | Whether to reverse the simulation mesh normals. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bReverseSimMeshWindingOrder | Whether to reverse the simulation mesh triangles' winding order. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderPatterns | List of render patterns to apply the operation on. All patterns will be used if left empty. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bReverseRenderMeshNormals | Whether to reverse the render mesh normals. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bReverseRenderMeshWindingOrder | Whether to reverse the render mesh triangles' winding order. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-round.md

# Round

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Round

> Application Version: 5.7

### Description

Round (v1)

Round ( 1.4 => 1.0 | 1.9 => 2.0 | -5.3 => -5.0)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Round Mid 0.5 |
| Type | [FDataflowMathRoundNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathRoundNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-scalevector.md

# ScaleVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ScaleVector

> Application Version: 5.7

### Description

ScaleVector (v1)

Scale a vector by a scalar : Scaled = (V \* Scale)

Input(s) :
V - Vector to scale
Scale - Scale factor

Output(s):
Scaled - Scaled vector : Scaled=(V \* Scale)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Scalar Float Double |
| Type | [FDataflowVectorScaleNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorScaleNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Vector to scale | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| Scale | Scale factor | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Scaled | Scaled vector : Scaled=(V \* Scale) | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-scattermeshes.md

# ScatterMeshes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ScatterMeshes

> Application Version: 5.7

### Description

ScatterMeshes (v1)

Copies the same mesh with scale onto points

Input(s) :
Points [Intrinsic] - Points to copy meshes onto
MeshToCopy [Intrinsic] - Mesh to copy onto points

Output(s):
Mesh - merged result mesh
Meshes - Result meshes as individual ones

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FMeshCopyToPointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshCopyToPointsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Scale | Scale applied to the mesh | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Points to copy meshes onto | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| MeshToCopy | Mesh to copy onto points | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | merged result mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| Meshes | Result meshes as individual ones | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-select.md

# Select

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Select

> Application Version: 5.7

### Description

Select (v1)

Dataflow Select Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | FlowControl |
| Type | [FDataflowSelectNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectedIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-selectfloatarrayindicesinrange.md

# SelectFloatArrayIndicesInRange

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectFloatArrayIndicesInRange

> Application Version: 5.7

### Description

SelectFloatArrayIndicesInRange (v1)

Selects indices of a float array by range

Input(s) :
Values - GeometryCollection for the selection

Output(s):
Indices - Indices of float Values matching the specified range

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Array |
| Type | [FSelectFloatArrayIndicesInRangeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSelectFloatArrayIndicesInRangeD-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Min | Minimum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Max | Maximum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| RangeSetting | Values for the selection has to be inside or outside [Min, Max] range | [ERangeSettingEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERangeSettingEnum) | Dataflow\_RangeSetting\_InsideRange |
| bInclusive | If true then range includes Min and Max values | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Values | GeometryCollection for the selection | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| Min | Minimum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Max | Maximum value for the selection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Indices | Indices of float Values matching the specified range | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-selection.md

# Selection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection

> Application Version: 5.7

### Description

Selection (v2)

Chaos Cloth Asset Selection Node V 2

Input(s) :
TransferCollection - The collection used to transfer sets from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Selection |
| Type | [FChaosClothAssetSelectionNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSelectionNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutputName | The name to be use as a selection. | [FChaosClothAssetConnectableOStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableOStri-) | (StringValue="") |
| InputName | The name to populate this set from and override based on Selection Override Type. Output Name will be used if Input Name is empty. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |
| SelectionOverrideType | How to apply this node's Indices onto existing sets. Changing this value will change the output set. To change how the node's stored indices are calculated, change the equivalent value on the Selection Tool context. | [EChaosClothAssetSelectionOverrideType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetSelectionOverrid-) | ReplaceAll |
| Group | The type of element the selection refers to | [FChaosClothAssetNodeSelectionGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetNodeSelectionGro-) | (Name="") |
| Indices | Selected element indices | [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | () |
| RemoveIndices | Indices to remove from the Input selection | [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | () |
| Import | Import (replace) the current selection from the input Collection's selection with the given Input Name (or Output Name if Input Name is empty). | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ImportSecondary | Import (replace) the current selection from the input Collection's secondary selection with the given Input Name (or Output Name if Input Name is empty). Secondary selections are only supported in v1 of this node. This function is provided as a migration tool to this current version. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| SimTransferType | The type of transfer used to transfer the sim mesh sets when a TransferCollection is connected. This property is disabled when no TransferCollection input has been connected. | [EChaosClothAssetWeightMapTransferType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapTransfe-) | Use2DSimMesh |
| TransferSelectionThreshold | Selections are internally converted to maps in order to do the transfer and then converted back. This value is used to do the conversion back. Decrease this value to (possibly) expand the converted selection. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.950000 |
| Transfer | Transfer the selection from the connected Transfer Collection containing a selection with Input Name (or Output Name if Input Name is empty). | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransferCollection | The collection used to transfer sets from. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| OutputName.StringValue | The value for this property. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-selectionset.md

# SelectionSet

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionSet

> Application Version: 5.7

### Description

SelectionSet (v1)

Selection Set Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Dataflow |
| Type | [FSelectionSetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FSelectionSetDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Indices |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | 1 2 3 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IndicesOut |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-selectiontointmap.md

# SelectionToIntMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToIntMap

> Application Version: 5.7

### Description

SelectionToIntMap (v1)

Convert an integer index selection to an integer map. Map type will match the selection type.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Selection To Int Map |
| Type | [FChaosClothAssetSelectionToIntMapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSelectionToIntMa-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionName | The name of the selection to convert. | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |
| IntMapName | The name of the integer map attribute that will be added to the collection. If left empty the same name as the selection name will be used instead. | [FChaosClothAssetConnectableIOStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIOStr-) | (StringValue="") |
| bKeepExistingUnselectedValues | If the IntMapName already exists, keep existing values rather than overwriting them with 'Unselected Value'. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| UnselectedValue | The value unselected elements receive. Unselected existing values can be kept by setting 'Keep Existing Unselected Values' | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SelectedValue | The value selected elements receive. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| IntMapName.StringValue | The value for this property. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-selectiontovertexlist.md

# SelectionToVertexList

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToVertexList

> Application Version: 5.7

### Description

SelectionToVertexList (v1)

Selection to Vertex List Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Selection|Utility |
| Type | [FSelectionToVertexListDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSelectionToVertexListDataflowNo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexSelection |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexList |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-selectiontoweightmap.md

# SelectionToWeightMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap

> Application Version: 5.7

### Description

SelectionToWeightMap (v1)

Convert an integer index selection to a vertex weight map where different map values can be set for selected and unselected vertices.

Input(s) :
SelectionName - The name of the selection to convert.

Output(s):
WeightMapName - The name of the weight map attribute that will be added to the collection.
If left empty the same name as the selection name will be used instead.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Selection To Weight Map |
| Type | [FChaosClothAssetSelectionToWeightMapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSelectionToWeigh-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| UnselectedValue | The value unselected vertices receive. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SelectedValue | The value selected vertices receive. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SelectionName | The name of the selection to convert. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| WeightMapName | The name of the weight map attribute that will be added to the collection. If left empty the same name as the selection name will be used instead. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setanchorstate.md

# SetAnchorState

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetAnchorState

> Application Version: 5.7

### Description

SetAnchorState (v1)

Sets the anchored state on the selected bones in a Collection

Input(s) :
Collection [Intrinsic] - GeometryCollection to set anchor state on
TransformSelection [Intrinsic] - Bone selection for setting the state on

Output(s):
Collection [Passthrough] - GeometryCollection to set anchor state on

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FSetAnchorStateDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetAnchorStateDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AnchorState | What anchor state to set on selected bones | [EAnchorStateEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EAnchorStateEnum) | Dataflow\_AnchorState\_Anchored |
| bSetNotSelectedBonesToOppositeState | If true, sets the non selected bones to opposite anchor state | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to set anchor state on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection for setting the state on | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to set anchor state on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setcollectionattributedatatyped.md

# SetCollectionAttributeDataTyped

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped

> Application Version: 5.7

### Description

SetCollectionAttributeDataTyped (v1)

Set attribute data in a Collection

Input(s) :
Collection [Intrinsic] - Collection for the custom attribute
AttributeKey - Input to drive the Attribute and Group name
BoolAttributeData - Bool type attribute data
FloatAttributeData - Float type attribute data
DoubleAttributeData - Float type attribute data
Int32AttributeData - Int type attribute data
StringAttributeData - Int type attribute data
Vector3fAttributeData - Vector3f type attribute data
Vector3dAttributeData - Vector3d type attribute data
LinearColorAttributeData - LinearColor type attribute data

Output(s):
Collection [Passthrough] - Collection for the custom attribute

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FSetCollectionAttributeDataTypedDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetCollectionAttributeDataTyped-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Standard group names | [EStandardGroupNameEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStandardGroupNameEnum) | Dataflow\_EStandardGroupNameEnum\_Transform |
| CustomGroupName | User specified group name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| AttrName | Attribute name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey | Input to drive the Attribute and Group name | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoolAttributeData | Bool type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FloatAttributeData | Float type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| DoubleAttributeData | Float type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| Int32AttributeData | Int type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| StringAttributeData | Int type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| Vector3fAttributeData | Vector3f type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Vector3dAttributeData | Vector3d type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3d](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| LinearColorAttributeData | LinearColor type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setcollidablevertices.md

# SetCollidableVertices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollidableVertices

> Application Version: 5.7

### Description

SetCollidableVertices (v1)

Set custom vertices so that only these vertices can collide with other surfaces.
Unselected vertices will not collide with unselected vertices.

Input(s) :
VertexSelection [Intrinsic] - Vertices selected to be able to collide with others. Unselected vertices will not collide with unselected vertices

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetCollidableVerticesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetCollidableVerticesDataflowNo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertices selected to be able to collide with others. Unselected vertices will not collide with unselected vertices | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setdynamicstate.md

# SetDynamicState

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetDynamicState

> Application Version: 5.7

### Description

SetDynamicState (v1)

Sets the dynamic state on the selected bones in a Collection

Input(s) :
Collection [Intrinsic] - GeometryCollection to set anchor state on
TransformSelection [Intrinsic] - Bone selection for setting the state on

Output(s):
Collection [Passthrough] - GeometryCollection to set anchor state on

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FSetDynamicStateDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetDynamicStateDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DynamicState | Dynamic state to set on selected bones | [EDataflowGeometryCollectionDynamicState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowGeometryCollectionDynam-) | Kinematic |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to set anchor state on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection for setting the state on | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to set anchor state on | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setfleshbonepositiontargetbinding.md

# SetFleshBonePositionTargetBinding

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding

> Application Version: 5.7

### Description

SetFleshBonePositionTargetBinding (v2)

Binds vertices from Collection to bone skeletal mesh surface via kinematic or weak constraints.

Input(s) :
VertexSelection - (optional) only create kinematic/weak constraints on vertices in the VertexSelection

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetFleshBonePositionTargetBindingDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetFleshBonePositionTargetBindi-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalBindingMode |  | [ESkeletalBindingMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/ESkeletalBindingMode) | Dataflow\_SkeletalBinding\_PositionTarget |
| PositionTargetStiffness |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10000.000000 |
| SearchRadius | Collection vertices are bound to their closest skeletal mesh vertices within the search radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| VertexSelection | (optional) only create kinematic/weak constraints on vertices in the VertexSelection | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setfleshdefaultproperties.md

# SetFleshDefaultProperties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties

> Application Version: 5.7

### Description

SetFleshDefaultProperties (v1)

Set Flesh Default Properties Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetFleshDefaultPropertiesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetFleshDefaultPropertiesNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Density |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| VertexStiffness |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000000.000000 |
| VertexDamping |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| VertexIncompressibility | Sets incompressibility on vertex basis. 0.6 is default behavior. 1 means absolutely incompressible. 0 means no incompressibility constraint on the material | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.600000 |
| VertexInflation | Sets inflation on vertex basis. 0.5 means no inflation/deflation. 1 means inflation to 2X volume on each dimension. 0 means the material is deflated to 0 volume. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setintomaterialsarray.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setkinematicvertexselection.md

# SetKinematicVertexSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetKinematicVertexSelection

> Application Version: 5.7

### Description

SetKinematicVertexSelection (v1)

Set VertexSelection to be kinematic. Note that kinematic particles need skin weights.

Input(s) :
VertexSelection - Vertex Selection set to be kinematic

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Tags | Set Vertex Collection to be kinematic |
| Type | [FGeometryCollectionSetKinematicVertexSelectionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| KinematicValue |  | [ESetKinematicVertexSelectionKinematicValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESetKinematicVertexSelectionKine-) | SetKinematic |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex Selection set to be kinematic | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setmuscleactivationparameter.md

# SetMuscleActivationParameter

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter

> Application Version: 5.7

### Description

SetMuscleActivationParameter (v1)

Sets per-muscle parameters for custom muscle contraction.

Input(s) :
AnimationAsset - Use minimum muscle lengths across this animation asset to infer MuscleLengthRatioThresholdForMaxActivation
SkeletalMesh - Skeletal mesh used to linear blend skin kinematic origins and insertions.
This must be the same as the one used to create TransformSource group.
Check geometry spreadsheet for more info.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetMuscleActivationParameterNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetMuscleActivationParameterNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ParameterMethod |  | [TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EParameterMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/EParameterMethod)> | Global |
| ApplyGlobalParameters | Click on this button to apply global parameters. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ContractionVolumeScale | Muscles gain volume during contraction if > 1. Volume-preserving if 1. Default: 1 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| GlobalFiberLengthRatioAtMaxActivation | How much muscle fibers shorten at max activation 1. A smaller value means more contraction in the fiber direction. Default: 0.5 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| GlobalMuscleLengthRatioThresholdForMaxActivation | Muscle length ratio (defined by origin-insertion distance) below this threshold is considered to reach max activation 1. Default: 0.75 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| GlobalInflationVolumeScale | Inflates muscle rest volume if > 1 and deflates muscle rest volume if < 1. Default: 1 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bUseLengthActivationCurve |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| GlobalLengthActivationCurve | Curve editor for muscle length-activation curve. Default: linear X-axis: normalized muscle length level from 0 (rest state) to 1 (muscle length ratio = Muscle Length Ratio Threshold For Max Activation) Y-axis: muscle activation from 0 to 1 | [FRuntimeFloatCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((),(Time=1.000000,Value=1.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |
| ThresholdScalingPercent | This percentage (usually between 0 and 100%) globally scales minimum muscle lengths computed from the animation asset. For example, if minimum muscle length = 0.5 and ThresholdScalingPercent = 80%, the final MuscleLengthRatioThresholdForMaxActivation for this muscle is 1 - (1 - 0.5) \* 80% = 0.6 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| ImportLowestMuscleLengthRatio | Click on this button to import the minimum muscle lengths across the animation asset as MuscleLengthRatioThresholdForMaxActivation | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ImportAllMuscleNames | Click on this button to import muscle bone names (in the Transform group) from the collection. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ResetToGlobalParameters | Click on this button to reset per-muscle parameters to global parameters. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ApplyCustomParameters | Click on this button to apply custom muscle parameters. | [FDataflowFunctionProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ParameterArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AnimationAsset | Use minimum muscle lengths across this animation asset to infer MuscleLengthRatioThresholdForMaxActivation | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UAnimSequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UAnimSequence)> | None |
| SkeletalMesh | Skeletal mesh used to linear blend skin kinematic origins and insertions. This must be the same as the one used to create TransformSource group. Check geometry spreadsheet for more info. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setoutfitclothcollection.md

# SetOutfitClothCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetOutfitClothCollection

> Application Version: 5.7

### Description

SetOutfitClothCollection (v1)
Experimental

Replace the ClothCollection in an Outfit with a new one.
Any data derived from the ClothCollection (e.g., Simulation Model, Render Data) will NOT be regenerated in the Outfit.

Input(s) :
Outfit - The outfit to be edited.
ClothCollection - The replacement cloth collection.
PieceIndex - The Outfit Piece to replace.
LODIndex - The Outfit LOD to replace.

Output(s):
Outfit [Passthrough] - The outfit to be edited.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Cloth Collections |
| Type | FChaosSetOutfitClothCollectionNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to be edited. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| ClothCollection | The replacement cloth collection. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| PieceIndex | The Outfit Piece to replace. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| LODIndex | The Outfit LOD to replace. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to be edited. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setphysicsasset.md

# SetPhysicsAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetPhysicsAsset

> Application Version: 5.7

### Description

SetPhysicsAsset (v1)

Replace the current physics assets to collide the simulation mesh against.

Input(s) :
PhysicsAsset - The physics asset to assign to the Cloth Collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Set Physics Asset |
| Type | [FChaosClothAssetSetPhysicsAssetNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSetPhysicsAssetN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| PhysicsAsset | The physics asset to assign to the Cloth Collection. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UPhysicsAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UPhysicsAsset)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setpivot.md

# SetPivot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetPivot

> Application Version: 5.7

### Description

SetPivot (v1)

Sets pivot for Collection

Input(s) :
Collection [Intrinsic] - Collection for the pivot change
Transform - Pivot transform

Output(s):
Collection [Passthrough] - Collection for the pivot change

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FCollectionSetPivotDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSetPivotDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the pivot change | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Transform | Pivot transform | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the pivot change | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setskinningselection.md

# SetSkinningSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetSkinningSelection

> Application Version: 5.7

### Description

SetSkinningSelection (v1)
Experimental

Set skin weights selection attributes.

Input(s) :
SelectionMapKey - Selection map key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [DataflowEditor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor) |
| Category | Collection |
| Tags | Set the skin weights selection for a future correction |
| Type | [FDataflowSetSkinningSelectionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/FDataflowSetSkinningSelectionNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionMapName | Map name to be used to select vertices to correct | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| CorrectionType | Selection map key to be used in other nodes if necessary | [ESkinWeightsCorrectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/ESkinWeightsCorrectionType) | Relax |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SelectionMapKey | Selection map key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setskinningskeletalmesh.md

# SetSkinningSkeletalMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetSkinningSkeletalMesh

> Application Version: 5.7

### Description

SetSkinningSkeletalMesh (v1)
Experimental

Set the skeletal mesh for the collection

Input(s) :
Collection - Managed array collection to be used to store datas
SkeletalMesh - Skeletal mesh binding to be stored in the collection
GeometrySelection - Geometries to set skinning skeletal mesh on

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Type | [FDataflowCollectionSetSkinningSkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionSetSkinningSk-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMesh | Skeletal mesh binding to be stored in the collection | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| GeometrySelection | Geometries to set skinning skeletal mesh on | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) | () |
| LODIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setvertexcolorfromfloatarray.md

# SetVertexColorFromFloatArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromFloatArray

> Application Version: 5.7

### Description

SetVertexColorFromFloatArray (v1)

Set the vertex color on the collection based on the normalized float array.

Input(s) :
Collection [Intrinsic] - Collection Passthrough
FloatArray [Intrinsic] - Float array to use as a scalar for the color

Output(s):
Collection [Passthrough] - Collection Passthrough

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Collection|Utilities |
| Type | [FSetVertexColorFromFloatArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetVertexColorFromFloatArrayDat-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bNormalizeInput | Enable normalization of input array | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color | Base color for the normalized float array | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection Passthrough | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FloatArray | Float array to use as a scalar for the color | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection Passthrough | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setvertexcolorfromvertexindices.md

# SetVertexColorFromVertexIndices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromVertexIndices

> Application Version: 5.7

### Description

SetVertexColorFromVertexIndices (v1)

Set the vertex color of the collection based on the selection set.

Input(s) :
Collection [Intrinsic] - Collection Passthrough
VertexIndicesIn - Vertex indices set

Output(s):
Collection [Passthrough] - Collection Passthrough

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Collection|Utilities |
| Type | [FSetVertexColorFromVertexIndicesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetVertexColorFromVertexIndices-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectedColor | Selected vertex color | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=0.000000,A=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection Passthrough | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexIndicesIn | Vertex indices set | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection Passthrough | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setvertexcolorfromvertexselection.md

# SetVertexColorFromVertexSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromVertexSelection

> Application Version: 5.7

### Description

SetVertexColorFromVertexSelection (v1)

Set the vertex color of the collection based on the selection set.

Input(s) :
Collection [Intrinsic] - Collection Passthrough
VertexSelection [Intrinsic] - Vertex selection set

Output(s):
Collection [Passthrough] - Collection Passthrough

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Collection|Utilities |
| Type | [FSetVertexColorFromVertexSelectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetVertexColorF-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectedColor | Selected vertex color | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=0.000000,A=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection Passthrough | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection set | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection Passthrough | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setvertextetrahedrapositiontargetbinding.md

# SetVertexTetrahedraPositionTargetBinding

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTetrahedraPositionTargetBinding

> Application Version: 5.7

### Description

SetVertexTetrahedraPositionTargetBinding (v1)

Set Vertex Tetrahedra Position Target Binding Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetVertexTetrahedraPositionTargetBindingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetVertexTetrahedraPositionTarg-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PositionTargetStiffness |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10000.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TargetIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| GeometryGroupGuidsIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setvertextrianglepositiontargetbinding.md

# SetVertexTrianglePositionTargetBinding

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding

> Application Version: 5.7

### Description

SetVertexTrianglePositionTargetBinding (v1)

Create point-triangle weak constraints (springs) between surface meshes of different geometries based on search radius.

Input(s) :
VertexSelection - (optional) only create weak constraints from surface vertices in VertexSelection to triangles in other geometries

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetVertexTrianglePositionTargetBindingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetVertexTrianglePositionTarget-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PositionTargetStiffness |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SearchRadius | Search radius for point-triangle pairs between geometry surfaces. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bAllowSliding | if point-triangle weak constraints created are anisotropic and allow sliding along the triangle plane | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bZeroRestLengthEditable |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bUseZeroRestLengthSprings | if point-triangle weak constraints created are zero rest-length. if true, this will cause point triangle pair to stick together, as opposed to separated by their rest state distance. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | (optional) only create weak constraints from surface vertices in VertexSelection to triangles in other geometries | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setvertexvertexpositiontargetbinding.md

# SetVertexVertexPositionTargetBinding

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexVertexPositionTargetBinding

> Application Version: 5.7

### Description

SetVertexVertexPositionTargetBinding (v1)

Set Vertex Vertex Position Target Binding Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetVertexVertexPositionTargetBindingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetVertexVertexPositionTargetBi-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RadiusRatio |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| PositionTargetStiffness |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10000.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TargetIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-setvisibilityincollection.md

# SetVisibilityInCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVisibilityInCollection

> Application Version: 5.7

### Description

SetVisibilityInCollection (v1)

Sets all selected bone's visibilty to Visible/Hidden

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to set visibility
TransformSelection [Intrinsic] - Transform selection for setting visibility
FaceSelection [Intrinsic] - Face selection for setting visibility

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to set visibility

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Edit |
| Type | [FSetVisibilityInCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetVisibilityInCollectionDatafl-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Visibility | What to set the visibility of the selected bones | [EVisibiltyOptionsEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EVisibiltyOptionsEnum) | Dataflow\_VisibilityOptions\_Invisible |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to set visibility | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Transform selection for setting visibility | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| FaceSelection | Face selection for setting visibility | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to set visibility | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

