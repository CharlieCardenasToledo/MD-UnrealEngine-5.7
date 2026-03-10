# Unidad 18

Rango: archivos 2041 a 2160 de 3470

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-deletevertextrianglepositiontargetbinding.md

# DeleteVertexTrianglePositionTargetBinding

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteVertexTrianglePositionTargetBinding

> Application Version: 5.7

### Description

DeleteVertexTrianglePositionTargetBinding (v1)

Delete vertex-triangle weak constraints (zero rest length springs) between VertexSelection1 and VertexSelection2.

Input(s) :
VertexSelection1 [Intrinsic] - This node deletes springs between VertexSelection1 and VertexSelection2.
VertexSelection2 [Intrinsic] - This node deletes springs between VertexSelection1 and VertexSelection2.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FDeleteVertexTrianglePositionTargetBindingDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FDeleteVertexTri-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection1 | This node deletes springs between VertexSelection1 and VertexSelection2. | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| VertexSelection2 | This node deletes springs between VertexSelection1 and VertexSelection2. | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-divide.md

# Divide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Divide

> Application Version: 5.7

### Description

Divide (v1)

Division (A / B)
if B is equal to 0, 0 is returned Fallback value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | / Division |
| Type | [FDataflowMathDivideNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathDivideNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| B |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Fallback |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-dividevector.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-divisionwholeandremainder.md

# Division (Whole and Remainder)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DivisionWholeandRemainder

> Application Version: 5.7

### Description

Division (Whole and Remainder) (v1)

Division Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FDivisionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDivisionDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Dividend |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Divisor |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Remainder |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| ReturnValue |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-duplicatemeshuvchannelnode.md

# DuplicateMeshUVChannelNode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode

> Application Version: 5.7

### Description

DuplicateMeshUVChannelNode (v1)

Create a new UV layer/channel in a UDataflowMesh

Input(s) :
Mesh [Intrinsic] - DataflowMesh input/output

Output(s):
Mesh [Passthrough] - DataflowMesh input/output
NewUVChannel - Index of the added UV channel

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Tags | Mesh UV DataflowMesh |
| Type | [FDuplicateMeshUVChannelNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDuplicateMeshUVChannelNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceUVChannel | Index of the source UV channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DataflowMesh input/output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DataflowMesh input/output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| NewUVChannel | Index of the added UV channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-editskeletonbones.md

# EditSkeletonBones

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones

> Application Version: 5.7

### Description

EditSkeletonBones (v1)
Experimental

Edit skeleton bones properties.

Input(s) :
Skeleton - Skeleton to be edited

Output(s):
Skeleton [Passthrough] - Skeleton to be edited

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Tags | Edit skeleton bones |
| Type | [FDataflowCollectionEditSkeletonBonesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionEditSkeletonB-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Skeleton | Skeleton to be edited | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Skeleton | Skeleton to be edited | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-editskinweights.md

# EditSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights

> Application Version: 5.7

### Description

EditSkinWeights (v1)
Experimental

Edit skin weights vertex properties.

Input(s) :
BoneIndicesKey - Bone indices key to be used in other nodes if necessary
BoneWeightsKey - Bone weights key to be used in other nodes if necessary
SkeletalMesh - Skeletal mesh to extract the skeleton from for the skinning

Output(s):
BoneIndicesKey [Passthrough] - Bone indices key to be used in other nodes if necessary
BoneWeightsKey [Passthrough] - Bone weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Tags | Edit skin weights and save it to collection |
| Type | [FDataflowCollectionEditSkinWeightsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionEditSkinWeigh-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndicesName | The name to be set as a weight map attribute. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| BoneWeightsName | The name to be set as a weight map attribute. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| bCompressSkinWeights | Boolean to use a compressed format (FVector4f, FIntVector) to store the skin weights | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SkeletalMesh | Skeletal mesh to extract the skeleton from for the skinning | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-efit.md

# EFit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EFit

> Application Version: 5.7

### Description

EFit (v1)

Fits a value from one range to another

Takes the value num from the range (oldmin, oldmax) and shifts it to the corresponding value in the new range (newmin, newmax). Unlike fit, this function does not clamp values in the given range.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FEFitDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FEFitDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Float |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| OldMin |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| OldMax |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| NewMin |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| NewMax |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-enableuvresizing.md

# EnableUVResizing

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EnableUVResizing

> Application Version: 5.7

### Description

EnableUVResizing (v1)
Experimental

Node for enabling UV Resizing used by the ChaosOutfitAsset's Resizeable Outfit.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Enable UV Resizing |
| Type | [FChaosClothAssetEnableUVResizingNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetEnableUVResizing-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-exp.md

# Exp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Exp

> Application Version: 5.7

### Description

Exp (v1)

Exponential ( Exp(A) )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Exponential |
| Type | [FDataflowMathExpNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathExpNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-explodedview.md

# ExplodedView

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView

> Application Version: 5.7

### Description

ExplodedView (v1)

"Explodes" the pieces from the Collection for better visualization

Input(s) :
Collection [Intrinsic] - Collection to explode
UniformScale - Scale amount to expand the pieces uniformly in all directions
Scale - Scale amounts to expand the pieces in all 3 directions
Offset - Translate collection for exploded view

Output(s):
Collection [Passthrough] - Collection to explode

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FExplodedViewDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FExplodedViewDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to explode | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| UniformScale | Scale amount to expand the pieces uniformly in all directions | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Scale | Scale amounts to expand the pieces in all 3 directions | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Offset | Translate collection for exploded view | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to explode | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-extractbodypartsarrayfrombodysizeparts.md

# ExtractBodyPartsArrayFromBodySizeParts

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractBodyPartsArrayFromBodySizeParts

> Application Version: 5.7

### Description

ExtractBodyPartsArrayFromBodySizeParts (v1)
Experimental

Extract the array of BodyParts from a FChaosOutfitBodySizeBodyParts

Input(s) :
BodySizeParts - The source outfit.

Output(s):
BodyParts - The outfit body parts grouped by BodySize.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Extract Outfit Body Parts Skeletal Mesh |
| Type | FChaosExtractBodyPartsArrayFromBodySizePartsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BodySizeParts | The source outfit. | FChaosOutfitBodySizeBodyParts | (BodyParts=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BodyParts | The outfit body parts grouped by BodySize. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-extractclothselectionset.md

# ExtractClothSelectionSet

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet

> Application Version: 5.7

### Description

ExtractClothSelectionSet (v1)
Experimental

Extract a selection set from a Cloth Collection.

Input(s) :
Selection - Name of the selection set to be extracted. Currently only SimVertices3D and RenderVertices sets are supported.
DynamicMesh - Dynamic mesh used to reorder indices.

Output(s):
ExtractedSelectionSet - Extracted Selection Set as a Set
ExtractedSelectionArray - Extracted Selection Set as an array

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Extract Cloth Selection Set |
| Type | [FChaosClothAssetExtractSelectionSetNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetExtractSelection-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bReorderForDynamicMesh | Reorder extracted indices to match the order of a DynamicMesh that was created via ClothCollectionToDynamicMesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DynamicMesh | Dynamic mesh used to reorder indices. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExtractedSelectionSet | Extracted Selection Set as a Set | [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| ExtractedSelectionArray | Extracted Selection Set as an array | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-extractclothweightmap.md

# ExtractClothWeightMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothWeightMap

> Application Version: 5.7

### Description

ExtractClothWeightMap (v1)
Experimental

Extract a weight map from a Cloth Collection.

Input(s) :
WeightMap - Name of the weight map to be extracted
DynamicMesh - Dynamic mesh used to reorder weights.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Extract Cloth Weight Map |
| Type | [FChaosClothAssetExtractWeightMapNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetExtractWeightMap-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshTarget | Type of the weight map to be extracted | [EChaosClothAssetWeightMapMeshTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapMeshTar-) | Simulation |
| bReorderForDynamicMesh | Reorder extracted weights to match the order of a DynamicMesh that was created via ClothCollectionToDynamicMesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DynamicMesh | Dynamic mesh used to reorder weights. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExtractedWeightMap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-fieldmakedensefloatarray.md

# FieldMakeDenseFloatArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray

> Application Version: 5.7

### Description

FieldMakeDenseFloatArray (v1)

Converts a sparse FloatArray (a selected subset of the whole incoming array) into a dense FloatArray
(same number of elements as the incoming array using NumSamplePositions) using the Remap input
NumSamplePositions controls the size of the output array, only indices smaller than l to than NumSamplePositions
will be processed

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FFieldMakeDenseFloatArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFieldMakeDenseFloatArrayDataflo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Default |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatInput |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-filterpointswithmesh.md

# FilterPointsWithMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh

> Application Version: 5.7

### Description

FilterPointsWithMesh (v1)

Filter a point set to only the points inside or outside of a given mesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to use to filter point set
bKeepInside - Whether to keep the points inside or (if false) outside the mesh, when filtering by Winding Number.
WindingThreshold - The winding number threshold to use for determining whether a point is inside or outside of the mesh, if corresponding Filter Method is set
MinDistance - The min distance to surface to keep, if corresponding Filter Method is set
MaxDistance - The max distance to surface to keep, if corresponding Filter Method is set
bUseSignedDistance - Whether to use signed distances for the Min and Max Distance thresholds. Otherwise, unsigned distance is used.
Note: Signs are computed via the Winding Number. The sign is negative if the point's Winding Number is below the Winding Threshold.
SamplePoints - Points to filter

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | FFilterPointSetWithMeshDataflowNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FilterMethod |  | [uint8](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to use to filter point set | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SamplePoints | Points to filter | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| bKeepInside | Whether to keep the points inside or (if false) outside the mesh, when filtering by Winding Number. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| WindingThreshold | The winding number threshold to use for determining whether a point is inside or outside of the mesh, if corresponding Filter Method is set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| MinDistance | The min distance to surface to keep, if corresponding Filter Method is set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxDistance | The max distance to surface to keep, if corresponding Filter Method is set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| bUseSignedDistance | Whether to use signed distances for the Min and Max Distance thresholds. Otherwise, unsigned distance is used. Note: Signs are computed via the Winding Number. The sign is negative if the point's Winding Number is below the Winding Threshold. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Points to filter | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-filtersimulationproxies.md

# FilterSimulationProxies

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies

> Application Version: 5.7

### Description

FilterSimulationProxies (v1)

Filter simulation proxies from context

Input(s) :
SimulationProxies - Simulation proxies coming from the context and filtered with the groups

Output(s):
FilteredProxies - Simulation proxies coming from the context and filtered with the groups

### Information

|  |  |
| --- | --- |
| Module | [DataflowSimulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation) |
| Category | Physics|Proxy |
| Tags | DataflowSimulationTag |
| Type | [FFilterSimulationProxiesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FFilterSimulationProxiesDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationGroups | Simulation groups to filter the output solvers properties | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationProxies | Simulation proxies coming from the context and filtered with the groups | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FilteredProxies | Simulation proxies coming from the context and filtered with the groups | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-filtersizedoutfit.md

# FilterSizedOutfit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit

> Application Version: 5.7

### Description

FilterSizedOutfit (v1)
Experimental

Select a single size for the passed Outfit and filter out all non matching sizes.

Input(s) :
Outfit - The outfit to filter.
SizeName - The name of the body size to use to filter.
If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements.
TargetBody - The target body skeletal mesh containing the measurements to select the required size to use to filter.
The target body is unused if Size Name is a valid name.

Output(s):
Outfit [Passthrough] - The outfit to filter.
OutfitCollection - The outfit collection output, provided for convenience as a view into the outfit object metadata.
SizeName [Passthrough] - The name of the body size to use to filter.
If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Filter Sized Outfit |
| Type | FChaosOutfitAssetFilterSizedOutfitNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to filter. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| SizeName | The name of the body size to use to filter. If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| TargetBody | The target body skeletal mesh containing the measurements to select the required size to use to filter. The target body is unused if Size Name is a valid name. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to filter. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| SizeName | The name of the body size to use to filter. If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OutfitCollection | The outfit collection output, provided for convenience as a view into the outfit object metadata. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-fit.md

# Fit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Fit

> Application Version: 5.7

### Description

Fit (v1)

Fits a value from one range to another
Returns a number between newmin and newmax that is relative to num in the range between oldmin and oldmax.
If the value is outside the old range, it will be clamped to the new range.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FFitDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFitDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Float |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| OldMin |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| OldMax |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| NewMin |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| NewMax |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-fixtinygeo.md

# FixTinyGeo

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo

> Application Version: 5.7

### Description

FixTinyGeo (v1)

Editor Fracture Mode / Utilities / TinyGeo tool
Merge pieces of geometry onto their neighbors -- use it to, for example, clean up too small pieces of geometry.

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
| Type | [FFixTinyGeoDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFixTinyGeoDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MergeType | Whether to merge small geometry, or small clusters | [EFixTinyGeoMergeType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoMergeType) | MergeGeometry |
| bOnFractureLevel | Only consider bones at the current Fracture Level | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bOnlyClusters | Only auto-consider clusters for merging. Note that leaf nodes can still be consider if manually selected. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bOnlySameParent | Only merge clusters to neighbors with the same parent in the hierarchy | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bGeometryOnlySameParent | Only merge geometry to neighbors with the same parent in the hierarchy | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| NeighborSelection |  | [EFixTinyGeoNeighborSelectionMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoNeighborSelectionMeth-) | LargestNeighbor |
| bOnlyToConnected | Only merge pieces that are connected in the proximity graph.If unchecked, connected pieces will still be favored, but if none are available the closest disconnected piece can be merged. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseCollectionProximityForConnections | Whether to use the Proximity (as computed by the Proximity node) to determine which bones are connected, and thus can be considered for merging. Otherwise will compute and use a reasonable default connectivity. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| UseBoneSelection | Options for using the current bone selection | [EFixTinyGeoUseBoneSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoUseBoneSelection) | NoEffect |
| SelectionMethod |  | [EFixTinyGeoGeometrySelectionMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoGeometrySelectionMeth-) | RelativeVolume |
| MinVolumeCubeRoot | If size (cube root of volume) is less than this value, geometry should be merged into neighbors -- i.e. a value of 2 merges geometry smaller than a 2x2x2 cube | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RelativeVolume | If cube root of volume relative to the overall shape's cube root of volume is less than this, the geometry should be merged into its neighbors. (Note: This is a bit different from the histogram viewer's "Relative Size," which instead shows values relative to the largest rigid bone.) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
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

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-flatten.md

# Flatten

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Flatten

> Application Version: 5.7

### Description

Flatten (v1)

Flattens selected bones. If no selection is provided, flattens all bones to level 1

Input(s) :
Collection [Intrinsic] - Fractured GeometryCollection to flatten
OptionalTransformSelection - If connected, clusters under the selected bones will be flattened. If no selection is provided, all bones will be flattened to level 1.

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to flatten

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterFlattenDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterFlattenDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to flatten | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OptionalTransformSelection | If connected, clusters under the selected bones will be flattened. If no selection is provided, all bones will be flattened to level 1. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to flatten | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-fleshassetterminal.md

# FleshAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FleshAssetTerminal

> Application Version: 5.7

### Description

FleshAssetTerminal (v1)

Flesh Asset Terminal Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Terminal |
| Type | [FFleshAssetTerminalDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FFleshAssetTerminalDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FleshAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UFleshAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshEngine/UFleshAsset)> | None |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-floatarraycomputestatistics.md

# FloatArrayComputeStatistics

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics

> Application Version: 5.7

### Description

FloatArrayComputeStatistics (v1)

Computes statistics of a float array

Input(s) :
FloatArray [Intrinsic] - Array to compute values from
TransformSelection - TransformSelection describes which values to use, if not connected all the elements will be used

Output(s):
Value - Computed value
Indices - Indices of elements with the computed value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Type | [FFloatArrayComputeStatisticsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayComputeStatisticsData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OperationName | Statistics Operation | [EStatisticsOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStatisticsOperationEnum) | Dataflow\_EStatisticsOperationEnum\_Min |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Array to compute values from | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| TransformSelection | TransformSelection describes which values to use, if not connected all the elements will be used | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | Computed value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Indices | Indices of elements with the computed value | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-floatarraynormalize.md

# FloatArrayNormalize

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize

> Application Version: 5.7

### Description

FloatArrayNormalize (v1)

Normalize the selected float data in a FloatArray

Input(s) :
InFloatArray [Intrinsic] - Input VectorArray
Selection - Selection for the operation

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FFloatArrayNormalizeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayNormalizeDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InFloatArray | Input VectorArray | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| Selection | Selection for the operation | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| MinRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutFloatArray |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-floatarraytointarray.md

# FloatArrayToIntArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray

> Application Version: 5.7

### Description

FloatArrayToIntArray (v1)

Converts a Float array to Int array using the specified method.

Input(s) :
FloatArray - Float array value to convert

Output(s):
IntArray - Int array output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Conversions |
| Type | [FFloatArrayToIntArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayToIntArrayDataflowNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Function | Conversion method: Floor takes the floor of each input float value - 1.1 turns into 1. Ceil takes the ceil - 1.1 turns into 2. Round rounds to the nearest integer - 1.1 turns into 1. Tuncate trucates like a type cast - 1.1 turns into 1. Non-zero to Index appends the index of all non-zero values to the output array. Zero to Index appends the index of all zero values to the output array. | [EFloatArrayToIntArrayFunctionEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EFloatArrayToIntArrayFunctionEnu-) | Dataflow\_FloatToInt\_NonZeroToIndex |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Float array value to convert | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IntArray | Int array output | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-floatarraytovertexselection.md

# FloatArrayToVertexSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToVertexSelection

> Application Version: 5.7

### Description

FloatArrayToVertexSelection (v1)

Converts a TArray to a FDataflowVertexSelection

Input(s) :
FloatArray [Intrinsic] - TArray array

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Type | [FFloatArrayToVertexSelectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayToVertexSelectionData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Comparison operation | [ECompareOperation1Enum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECompareOperation1Enum) | Dataflow\_Compare\_Greater |
| Threshold |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | TArray array | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexSelection |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-floatmathexpression.md

# FloatMathExpression

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatMathExpression

> Application Version: 5.7

### Description

FloatMathExpression (v1)

Expression node for floats

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FFloatMathExpressionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatMathExpressionDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Expression |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| B |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| C |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| D |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-floatoverride.md

# FloatOverride

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatOverride

> Application Version: 5.7

### Description

FloatOverride (v1)

Float Override Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Dataflow |
| Type | [FFloatOverrideDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FFloatOverrideDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PropertyName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Overrides |
| KeyName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | FloatAttr |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ValueOut |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-floor.md

# Floor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Floor

> Application Version: 5.7

### Description

Floor (v1)

Floor ( 1.4 => 1.0 | 1.9 => 1.0 | -5.3 => -6.0 )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Round Lowest Integer |
| Type | [FDataflowMathFloorNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathFloorNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-forcedependency.md

# ForceDependency

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency

> Application Version: 5.7

### Description

ForceDependency (v1)

Force an evaluation dependency between two values

Input(s) :
Value - Evaluating Value will force an evaluation of DependentValue
DependentValue - Evaluating Value will force an evaluation of DependentValue

Output(s):
Value [Passthrough] - Evaluating Value will force an evaluation of DependentValue

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | FlowControl |
| Type | [FDataflowForceDependencyNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowForceDependencyNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DependentValue | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |
| Value | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-frac.md

# Frac

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Frac

> Application Version: 5.7

### Description

Frac (v1)

Frac ( 1.4 => 0.4 | 1.9 => 0.9 | -5.3 => 0.3 )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Fractional Decimal Point |
| Type | [FDataflowMathFracNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathFracNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generateclusterconvexhullsfromchildrenhulls.md

# GenerateClusterConvexHullsFromChildrenHulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromChildrenHulls

> Application Version: 5.7

### Description

GenerateClusterConvexHullsFromChildrenHulls (v1)

Generates cluster convex hulls for children hulls

Input(s) :
ConvexCount - Maximum number of convex to generate for a specific cluster. Will be ignored if error tolerance is used instead
ErrorTolerance - Error tolerance to use to decide to merge leaf convex together.
This is in centimeters and represents the side of a cube, the volume of which will be used as threshold
to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex
OptionalSelectionFilter - Optional transform selection to compute cluster hulls on -- if not provided, all cluster hulls will be computed.
bAllowMergingLeafHulls - Also allow the same hull merging process to run on leaf hulls (merging hulls on leaves in the selection)
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
| Type | [FGenerateClusterConvexHullsFromChildrenHullsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGenerateCluster-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bPreferExternalCollisionShapes | Whether to prefer available External (imported) collision shapes instead of the computed convex hulls on the Collection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| MergeProximityFilter | Filter to optionally only consider spatially close convex hulls for merges | [EConvexHullProximityFilter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/EConvexHullProximityFilter) | None |
| MergeProximityDistanceThreshold | If applying a convex hull proximity filter, the distance threshold to use for determining that two convex hulls are close enough to merge | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
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
| ConvexCount | Maximum number of convex to generate for a specific cluster. Will be ignored if error tolerance is used instead | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ErrorTolerance | Error tolerance to use to decide to merge leaf convex together. This is in centimeters and represents the side of a cube, the volume of which will be used as threshold to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex | double | 0.000000 |
| OptionalSelectionFilter | Optional transform selection to compute cluster hulls on -- if not provided, all cluster hulls will be computed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| bAllowMergingLeafHulls | Also allow the same hull merging process to run on leaf hulls (merging hulls on leaves in the selection) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
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

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generateclusterconvexhullsfromleafhulls.md

# GenerateClusterConvexHullsFromLeafHulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls

> Application Version: 5.7

### Description

GenerateClusterConvexHullsFromLeafHulls (v1)

Generates cluster convex hulls for leafs hulls

Input(s) :
ConvexCount - Maximum number of convex to generate for a specific cluster. Will be ignored if error tolerance is used instead
ErrorTolerance - Error tolerance to use to decide to merge leaf convex together.
This is in centimeters and represents the side of a cube, the volume of which will be used as threshold
to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex
OptionalSelectionFilter - Optional transform selection to compute cluster hulls on -- if not provided, all cluster hulls will be computed.
bAllowMergingLeafHulls - Also allow the same hull merging process to run on leaf hulls (merging hulls on leaves in the selection)
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
| Type | [FGenerateClusterConvexHullsFromLeafHullsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGenerateCluster-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bPreferExternalCollisionShapes | Whether to prefer available External (imported) collision shapes instead of the computed convex hulls on the Collection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AllowMerges | Method to determine if the convex hulls from two separate bones can potentially be merged | [EAllowConvexMergeMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/EAllowConvexMergeMethod) | ByProximity |
| MergeProximityFilter | Filter to optionally only consider spatially close convex hulls for merges | [EConvexHullProximityFilter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/EConvexHullProximityFilter) | None |
| MergeProximityDistanceThreshold | If applying a convex hull proximity filter, the distance threshold to use for determining that two convex hulls are close enough to merge | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
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
| ConvexCount | Maximum number of convex to generate for a specific cluster. Will be ignored if error tolerance is used instead | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ErrorTolerance | Error tolerance to use to decide to merge leaf convex together. This is in centimeters and represents the side of a cube, the volume of which will be used as threshold to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex | double | 0.000000 |
| OptionalSelectionFilter | Optional transform selection to compute cluster hulls on -- if not provided, all cluster hulls will be computed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| bAllowMergingLeafHulls | Also allow the same hull merging process to run on leaf hulls (merging hulls on leaves in the selection) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
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

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generatecurvegeometry.md

# GenerateCurveGeometry

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry

> Application Version: 5.7

### Description

GenerateCurveGeometry (v1)
Experimental

Build the curve geometry from a collection containing curves

Input(s) :
Collection - Managed array collection to be used to store datas
SourceCurves - Managed array collection to be used to store datas
CurveSelection - Curve selection to focus the curves generation spatially
CurveCount - Max number of guides

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGenerateCurveGeometryDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGenerateCurveGeometryDataflowNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bMergeCurves | Flag to check if we can merge guides or not | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SourceCurves | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the curves generation spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |
| CurveCount | Max number of guides | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generateguidescurves.md

# GenerateGuidesCurves

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateGuidesCurves

> Application Version: 5.7

### Description

GenerateGuidesCurves (v1)
Experimental

Build the guides curves from the strands

Input(s) :
Collection - Managed array collection to be used to store datas

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Type | FGenerateGuidesCurvesDataflowNode |

### Inputs

| Name | Description | Type | DefaultValue |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

### Outputs

| Name | Description | Type |
| --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generateinterpolatedproxy.md

# GenerateInterpolatedProxy

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy

> Application Version: 5.7

### Description

GenerateInterpolatedProxy (v1)
Experimental

Generate a pair of Dynamic Meshes with the same topology that can be interpolated.

Currently, this node relies on the vertex mapping data existing on the input source and target meshes,
and that the mapped vertices on both meshes match.

Input(s) :
SourceMesh - Source mesh
SourceMaterialArray - Source materials.
TargetMesh - Target mesh

Output(s):
ProxyMesh - Output proxy mesh
ProxyMaterialArray - Proxy materials.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Type | FGenerateInterpolatedProxyDataflowNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BlendAlpha | Alpha between source (0) and target (1) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceMesh | Source mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SourceMaterialArray | Source materials. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| TargetMesh | Target mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ProxyMesh | Output proxy mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| ProxyMaterialArray | Proxy materials. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generateorigininsertion.md

# GenerateOriginInsertion

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateOriginInsertion

> Application Version: 5.7

### Description

GenerateOriginInsertion (v1)

Given two sets of vertex indices, generate two sets of vertex indices for origins and insertions that are within X distance away.

Input(s) :
Collection - typedef FManagedArrayCollection DataType;

Output(s):
Collection [Passthrough] - typedef FManagedArrayCollection DataType;

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FGenerateOriginInsertionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FGenerateOriginInsertionNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OriginIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InsertionIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| OriginIndicesOut |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InsertionIndicesOut |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generaterbfresizingweights.md

# GenerateRBFResizingWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights

> Application Version: 5.7

### Description

GenerateRBFResizingWeights (v1)
Experimental

Sample points and generate RBF Interpolation data for a given Source mesh.

Input(s) :
MeshToResize - The mesh to resize. This is currently unused but may be used to improve point sampling in the future.
SourceMesh - The source mesh to be sampled.
NumInterpolationPoints - The number of interpolation points to be sampled.

Output(s):
InterpolationData - The calculated interpolation points and RBF weights

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Generate RBF Resizing Weights |
| Type | FGenerateRBFResizingWeightsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceMesh | The source mesh to be sampled. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| NumInterpolationPoints | The number of interpolation points to be sampled. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1500 |
| MeshToResize | The mesh to resize. This is currently unused but may be used to improve point sampling in the future. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InterpolationData | The calculated interpolation points and RBF weights | [FMeshResizingRBFInterpolationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generateresizableproxy.md

# GenerateResizableProxy

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateResizableProxy

> Application Version: 5.7

### Description

GenerateResizableProxy (v1)
Experimental

Generate a pair of Dynamic Meshes with the same topology that can be interpolated.

Currently, this node relies on the vertex mapping data existing on the input source and target meshes,
and that the mapped vertices on both meshes match.

Input(s) :
SourceMesh - Source mesh
SourceMaterialArray - Source materials.
TargetMesh - Target mesh

Output(s):
SourceProxyMesh - Output source proxy mesh
TargetProxyMesh - Output source proxy mesh
ProxyMaterialArray - Target materials.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Type | FGenerateResizableProxyDataflowNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceMappingData | Source vertex mapping data. TODO: only have two choices that work currently. Make this an enum or something | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | ImportedVertexVIDsAttr |
| TargetMappingData | Target vertex mapping data. TODO: only have two choices that work currently. Make this an enum or something | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | ImportedVertexVIDsAttr |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceMesh | Source mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SourceMaterialArray | Source materials. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| TargetMesh | Target mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceProxyMesh | Output source proxy mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| TargetProxyMesh | Output source proxy mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| ProxyMaterialArray | Target materials. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generatesimmorphtarget.md

# GenerateSimMorphTarget

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget

> Application Version: 5.7

### Description

GenerateSimMorphTarget (v1)

Generate a Sim Morph target from a cloth collection sim mesh (with matching topology).

Input(s) :
Collection - Input/output collection
MorphTargetCollection - Collection to generate the morph target from.

Output(s):
Collection [Passthrough] - Input/output collection
MorphTargetName - Morph target name

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Generate Sim Morph Target |
| Type | [FChaosClothAssetGenerateSimMorphTargetNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_3) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bGenerateNormalDeltas | Whether or not to generate normal deltas | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| MorphTargetCollection | Collection to generate the morph target from. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| MorphTargetName | Morph target name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generateskeletalbindings.md

# GenerateSkeletalBindings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSkeletalBindings

> Application Version: 5.7

### Description

GenerateSkeletalBindings (v1)

Generate barycentric bindings (used by the FleshDeformer deformer graph) of a render surface to a tetrahedral mesh.

Input(s) :
Collection - Passthrough geometry collection. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.
SkeletalMeshIn - The input mesh, whose render surface is used to generate bindings.

Output(s):
Collection [Passthrough] - Passthrough geometry collection. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FGenerateSkeletalBindings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FGenerateSkeletalBindings) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Passthrough geometry collection. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndexIn |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SkeletalMeshIn | The input mesh, whose render surface is used to generate bindings. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Passthrough geometry collection. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-generatesurfacebindings.md

# GenerateSurfaceBindings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings

> Application Version: 5.7

### Description

GenerateSurfaceBindings (v1)

Generate barycentric bindings (used by the FleshDeformer deformer graph and Geometry Cache generation) of a render surface to a tetrahedral mesh and its surface.

* If a point is outside of the tetrahedral mesh, find surface embedding within SurfaceProjectionSearchRadius.
  Embeddings of LOD 0 are color coded in the render view:
  green: embedded on in a tetrahedron
  blue: embedded on a surface triangle
  red: orphan (cannot be embedded)
  yellow: orphan reparented to a tetrahedron from a node neighbor

Input(s) :
Collection - Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.
StaticMeshIn - The input mesh, whose render surface is used to generate bindings.
SkeletalMeshIn - The input mesh, whose render surface is used to generate bindings.
TransformSelection - Render mesh will only bind to geometries whose transforms are in TransformSelection.
GeometryGroupGuidsIn - Render mesh will only bind to geometries whose GeometryGroupGuids match here.

Output(s):
Collection [Passthrough] - Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.
SKMDynamicMesh - Converted from embedded skeletal/static mesh

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FGenerateSurfaceBindings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FGenerateSurfaceBindings) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMeshLODList | Select skeletal mesh LODs to embed. Default empty list selects all LODs. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bDoSurfaceProjection | Enable binding to the exterior hull of the tetrahedron mesh. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SurfaceProjectionSearchRadius | The search radius when looking for surface triangles to bind to. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bDoOrphanReparenting | When nodes aren't contained in tetrahedra and surface projection fails, try to find suitable bindings by looking to neighboring parents. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| StaticMeshIn | The input mesh, whose render surface is used to generate bindings. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| SkeletalMeshIn | The input mesh, whose render surface is used to generate bindings. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| TransformSelection | Render mesh will only bind to geometries whose transforms are in TransformSelection. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| GeometryGroupGuidsIn | Render mesh will only bind to geometries whose GeometryGroupGuids match here. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SKMDynamicMesh | Converted from embedded skeletal/static mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-geometrycollectionterminal.md

# GeometryCollectionTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionTerminal

> Application Version: 5.7

### Description

GeometryCollectionTerminal (v2)

* Geometry Collection asset terminal node

Input(s) :
Materials - Materials to set on this asset
InstancedMeshes - array of instanced meshes

Output(s):
Materials [Passthrough] - Materials to set on this asset
InstancedMeshes [Passthrough] - array of instanced meshes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Terminal |
| Type | [FGeometryCollectionTerminalDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollectionTerminalDataf-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Materials | Materials to set on this asset | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | array of instanced meshes | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |
| RootProxyMeshes |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Materials | Materials to set on this asset | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | array of instanced meshes | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-geometrycollectiontocollection.md

# GeometryCollectionToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionToCollection

> Application Version: 5.7

### Description

GeometryCollectionToCollection (v2)

Converts a UGeometryCollection asset to an FManagedArrayCollection

Output(s):
Collection - Geometry collection newly created
Materials - Material instances array from the static mesh
InstancedMeshes - Array of instanced meshes
RootProxyMeshes - corresponding source proxies

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FGeometryCollectionToCollectionDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GeometryCollection | Asset input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGeometryCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/UGeometryCollection)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Geometry collection newly created | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Materials | Material instances array from the static mesh | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | Array of instanced meshes | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |
| RootProxyMeshes | corresponding source proxies | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-geometryselectiontovertexselection.md

# GeometrySelectionToVertexSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometrySelectionToVertexSelection

> Application Version: 5.7

### Description

GeometrySelectionToVertexSelection (v1)

Converts GeometrySelection to VertexSelection

Input(s) :
Collection - GeometryCollection
GeometrySelection - Input geometry selection

Output(s):
VertexSelection - Vertex selection output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|All |
| Type | [FGeometrySelectionToVertexSelectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometrySelecti-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GeometryIndices | Space separated list of geometry indices to specify the selection when GeometrySelection is not connected | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| GeometrySelection | Input geometry selection | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexSelection | Vertex selection output | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getarrayelement.md

# GetArrayElement

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetArrayElement

> Application Version: 5.7

### Description

GetArrayElement (v1)

Get an element from an array

Input(s) :
Array [Intrinsic] - Array to get the element from
Index - Index to get the element at

Output(s):
Array [Passthrough] - Array to get the element from
Element - Element from the array at the specified index

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Tags | Index At |
| Type | [FDataflowGetArrayElementNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowGetArrayElementNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to get the element from | [FDataflowArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowArrayTypes) | () |
| Index | Index to get the element at | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to get the element from | [FDataflowArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowArrayTypes) |  |
| Element | Element from the array at the specified index | [FDataflowAllTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAllTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getarraysize.md

# GetArraySize

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetArraySize

> Application Version: 5.7

### Description

GetArraySize (v1)

Get size of an array

Input(s) :
Array [Intrinsic] - Array to get size from

Output(s):
Size - Computed value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Tags | Count Length Num |
| Type | [FDataflowGetArraySizeNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowGetArraySizeNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to get size from | [FDataflowArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowArrayTypes) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Size | Computed value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getbooloverridefromasset.md

# GetBoolOverrideFromAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoolOverrideFromAsset

> Application Version: 5.7

### Description

GetBoolOverrideFromAsset (v1)

Get Bool Override from Asset Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Overrides |
| Type | [FGetBoolOverrideFromAssetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetBoolOverrideFromAssetDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Key |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Key |
| Default |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IsOverriden |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Bool |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| BoolDefault |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getboundingboxesfromcollection.md

# GetBoundingBoxesFromCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoundingBoxesFromCollection

> Application Version: 5.7

### Description

GetBoundingBoxesFromCollection (v1)

Gets BoundingBoxes of pieces from a Collection

Input(s) :
Collection - Input Collection
TransformSelection - The BoundingBoxes will be output for the bones selected in the TransformSelection

Output(s):
BoundingBoxes - Output BoundingBoxes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetBoundingBoxesFromCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetBoundingBoxesFromCollectionD-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The BoundingBoxes will be output for the bones selected in the TransformSelection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBoxes | Output BoundingBoxes | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getboxlengths.md

# GetBoxLengths

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoxLengths

> Application Version: 5.7

### Description

GetBoxLengths (v1)

Create an array of lengths of bounding boxes (measured along an axis, diagonal, or the max/min axes) from an array of bounding boxes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Box |
| Type | [FGetBoxLengthsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetBoxLengthsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeasurementMethod |  | [EBoxLengthMeasurementMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EBoxLengthMeasurementMethod) | Diagonal |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Boxes |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Lengths |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getcentroidsfromcollection.md

# GetCentroidsFromCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection

> Application Version: 5.7

### Description

GetCentroidsFromCollection (v1)

Gets centroids of pieces from a Collection

Input(s) :
Collection - Input Collection
TransformSelection - The centroids will be output for the bones selected in the TransformSelection

Output(s):
Centroids - Output centroids
Levels - Hidden output to store computed level values for centroids

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetCentroidsFromCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetCentroidsFromCollectionDataf-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bColorByLevel | Control point color by level or setting | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color | Point color | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| bSizeByLevel | Control the point size by level or setting | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Size | Point size | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 8.000000 |
| PointSize | Float curve to control point size by level | [FRuntimeFloatCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((Value=12.000000),(Time=1.000000,Value=6.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The centroids will be output for the bones selected in the TransformSelection | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Centroids | Output centroids | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Levels | Hidden output to store computed level values for centroids | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getclothasset.md

# GetClothAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetClothAsset

> Application Version: 5.7

### Description

GetClothAsset (v1)
Experimental

Get a cloth asset object into the graph.

Output(s):
ClothAsset - The Cloth Asset to import into a collection.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Get Cloth Asset |
| Type | FChaosGetClothAssetNode |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClothAsset | The Cloth Asset to import into a collection. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosClothAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetEngine/UChaosClothAsset)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getcollectionattributedatatyped.md

# GetCollectionAttributeDataTyped

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionAttributeDataTyped

> Application Version: 5.7

### Description

GetCollectionAttributeDataTyped (v1)

Get attribute data from a Collection

Input(s) :
Collection [Intrinsic] - Collection for the custom attribute
AttributeKey - Input to drive the Attribute and Group name

Output(s):
BoolAttributeData - Bool type attribute data
FloatAttributeData - Float type attribute data
DoubleAttributeData - Float type attribute data
Int32AttributeData - Int type attribute data
StringAttributeData - Int type attribute data
Vector3fAttributeData - Vector3f type attribute data
Vector3dAttributeData - Vector3d type attribute data
LinearColorAttributeData - Vector3d type attribute data

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetCollectionAttributeDataTypedDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetCollectionAttributeDataTyped-) |

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

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoolAttributeData | Bool type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FloatAttributeData | Float type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| DoubleAttributeData | Float type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| Int32AttributeData | Int type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| StringAttributeData | Int type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| Vector3fAttributeData | Vector3f type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Vector3dAttributeData | Vector3d type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3d](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| LinearColorAttributeData | Vector3d type attribute data | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getcollectionboundingbox.md

# GetCollectionBoundingBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionBoundingBox

> Application Version: 5.7

### Description

GetCollectionBoundingBox (v1)

Get the geometric bounding box a collection in collection space

Input(s) :
Collection - Collection to compute the bouning box from

Output(s):
BoundingBox - Geometric bounding box of the input collection
Center - Center of the resulting bounding box
Dimensions - Dimensions of the resulting bounding box in centimers

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Box |
| Tags | Collection Bounds Size Dimensions Extents Center |
| Type | [FBoundingBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoundingBoxDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to compute the bouning box from | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | Geometric bounding box of the input collection | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center | Center of the resulting bounding box | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Dimensions | Dimensions of the resulting bounding box in centimers | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getcollectionfromasset.md

# GetCollectionFromAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionFromAsset

> Application Version: 5.7

### Description

GetCollectionFromAsset (v1)

Description for this node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FGetCollectionFromAssetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetCollectionFromAssetDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CollectionAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGeometryCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/UGeometryCollection)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getconvexhullvolume.md

# GetConvexHullVolume

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume

> Application Version: 5.7

### Description

GetConvexHullVolume (v1)

Get the sum of volumes of the convex hulls on the selected nodes

Input(s) :
TransformSelection [Intrinsic] - The transforms to consider

Output(s):
Volume - Sum of convex hull volumes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetConvexHullVolumeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetConvexHullVolumeDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSumChildrenForClustersWithoutHulls | For any cluster transform that has no convex hulls, whether to fall back to the convex hulls of the cluster's children. Otherwise, the cluster will not add to the total volume sum. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bVolumeOfUnion | Whether to take the volume of the union of selected hulls, rather than the sum of each hull volume separately. This is more expensive but more accurate when hulls overlap. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The transforms to consider | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Volume | Sum of convex hull volumes | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getcurrentindex.md

# GetCurrentIndex

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCurrentIndex

> Application Version: 5.7

### Description

GetCurrentIndex (v1)

Get the current index in a subgraph
This is to be used in subgraph when iterating over an array

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | SubGraph |
| Type | [FDataflowSubGraphGetCurrentIndexNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowSubGraphGetCurrentIndex-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getcurveattributes.md

# GetCurveAttributes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCurveAttributes

> Application Version: 5.7

### Description

GetCurveAttributes (v1)
Experimental

Get the kinematic weights attributes names

Output(s):
AttributeKey - Attribute key to build

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGetCurveAttributesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGetCurveAttributesDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeType | Type of attribute to use | [EGroomAttributeType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/EGroomAttributeType) | KinematicWeights |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeKey | Attribute key to build | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getfleshasset.md

# GetFleshAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetFleshAsset

> Application Version: 5.7

### Description

GetFleshAsset (v1)

Get Flesh Asset Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FGetFleshAssetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FGetFleshAssetDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FleshAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UFleshAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshEngine/UFleshAsset)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getfloatoverridefromasset.md

# GetFloatOverrideFromAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetFloatOverrideFromAsset

> Application Version: 5.7

### Description

GetFloatOverrideFromAsset (v1)

Get Float Override from Asset Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Overrides |
| Type | [FGetFloatOverrideFromAssetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetFloatOverrideFromAssetDatafl-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Key |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Key |
| Default |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IsOverriden |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Float |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| FloatDefault |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getgeometrycollectionasset.md

# GetGeometryCollectionAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionAsset

> Application Version: 5.7

### Description

GetGeometryCollectionAsset (v1)

Get Current geometry collection asset
Note : Use with caution as this may get replaced in a near future for a more generic getAsset node

Output(s):
Asset - Asset this data flow graph instance is assigned to

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FGetGeometryCollectionAssetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetGeometryCollectionAssetDataf-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Asset | Asset this data flow graph instance is assigned to | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGeometryCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/UGeometryCollection)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getgeometrycollectionsources.md

# GetGeometryCollectionSources

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources

> Application Version: 5.7

### Description

GetGeometryCollectionSources (v1)

Get the list of the original mesh information used to create a specific geometryc collection asset
each entry contains a mesh, a transform and a list of override materials

Input(s) :
Asset - Asset to get geometry sources from

Output(s):
Sources - array of geometry sources

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FGetGeometryCollectionSourcesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetGeometryCollectionSourcesDat-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Asset | Asset to get geometry sources from | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGeometryCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/UGeometryCollection)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Sources | array of geometry sources | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionSource](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionSource)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getgroomasset.md

# GetGroomAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGroomAsset

> Application Version: 5.7

### Description

GetGroomAsset (v2)
Experimental

Get the groom asset

Output(s):
GroomAsset - Groom asset that will be used in the dataflow graph

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGetGroomAssetDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGetGroomAssetDataflowNode_v2) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroomAsset | Groom asset that will be used in the dataflow graph | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGroomAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsCore/UGroomAsset)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getgroomattributes.md

# GetGroomAttributes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGroomAttributes

> Application Version: 5.7

### Description

GetGroomAttributes (v1)
Experimental

Get the kinematic weights attributes names

Output(s):
AttributeKey - Attribute key to build

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Type | FGetGroomAttributesDataflowNode |

### Outputs

| Name | Description | Type |
| --- | --- | --- |
| AttributeKey | Attribute key to build | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getintoverridefromasset.md

# GetIntOverrideFromAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetIntOverrideFromAsset

> Application Version: 5.7

### Description

GetIntOverrideFromAsset (v1)

Get Int Override from Asset Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Overrides |
| Type | [FGetIntOverrideFromAssetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetIntOverrideFromAssetDataflow-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Key |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Key |
| Default |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IsOverriden |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Int |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| IntDefault |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getmaterialasset.md

# GetMaterialAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMaterialAsset

> Application Version: 5.7

### Description

GetMaterialAsset (v1)

Get a material interface from an existing asset

Output(s):
Material - Material asset to get

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Materials |
| Type | [FGetMaterialInterfaceAssetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetMaterialInterfaceAssetDatafl-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Material | Material asset to get | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getmeshboundingbox.md

# GetMeshBoundingBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox

> Application Version: 5.7

### Description

GetMeshBoundingBox (v1)

Get the local geometric bounding box a dynamic mesh

Input(s) :
Mesh - dynamic mesh to compute the bouning box from

Output(s):
BoundingBox - Geometric bounding box of the input dynamic mesh
Center - Center of the resulting bounding box
Dimensions - Dimensions of the resulting bounding box in centimers

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh |
| Tags | Bounds Size Dimensions Extents Center |
| Type | [FGetMeshBoundingBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetMeshBoundingBoxDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | dynamic mesh to compute the bouning box from | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | Geometric bounding box of the input dynamic mesh | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center | Center of the resulting bounding box | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Dimensions | Dimensions of the resulting bounding box in centimers | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getmeshdata.md

# GetMeshData

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshData

> Application Version: 5.7

### Description

GetMeshData (v1)

Outputs Mesh data

Input(s) :
Mesh [Intrinsic] - Mesh for the data

Output(s):
VertexCount - Number of vertices
EdgeCount - Number of edges
TriangleCount - Number of triangles

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FGetMeshDataDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetMeshDataDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Mesh for the data | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexCount | Number of vertices | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| EdgeCount | Number of edges | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| TriangleCount | Number of triangles | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getnumelementsincollectiongroup.md

# GetNumElementsInCollectionGroup

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup

> Application Version: 5.7

### Description

GetNumElementsInCollectionGroup (v1)

Returns number of elements in a group in a Collection

Input(s) :
Collection [Intrinsic] - Collection for the custom attribute

Output(s):
NumElements - Number of elements for the attribute

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetNumElementsInCollectionGroupDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetNumElementsInCollectionGroup-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Standard group names | [EStandardGroupNameEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStandardGroupNameEnum) | Dataflow\_EStandardGroupNameEnum\_Transform |
| CustomGroupName | User specified group name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumElements | Number of elements for the attribute | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getormakeoutfitfromasset.md

# GetOrMakeOutfitFromAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOrMakeOutfitFromAsset

> Application Version: 5.7

### Description

GetOrMakeOutfitFromAsset (v1)
Experimental

Extract the Outfit from an Outfit Asset.
If the Outfit does not exist (e.g., this OutfitAsset has been cooked),
recreate a new one.

Input(s) :
OutfitAsset - The outfit asset input.

Output(s):
Outfit - The outfit output.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Get Make Outfit |
| Type | FChaosOutfitAssetGetOrMakeOutfitFromAssetNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutfitAsset | The outfit asset input. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfitAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfitAsset)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit output. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getoutfitasset.md

# GetOutfitAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitAsset

> Application Version: 5.7

### Description

GetOutfitAsset (v1)
Experimental

Get an outfit asset object into the graph.

Output(s):
OutfitAsset - The Outfit Asset to import into a collection.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Get Outfit Asset |
| Type | FChaosGetOutfitAssetNode |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutfitAsset | The Outfit Asset to import into a collection. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfitAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfitAsset)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getoutfitbodyparts.md

# GetOutfitBodyParts

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitBodyParts

> Application Version: 5.7

### Description

GetOutfitBodyParts (v1)
Experimental

Extract the Body Part Skeletal Meshes from an Outfit.

Input(s) :
Outfit - The source outfit.

Output(s):
Outfit [Passthrough] - The source outfit.
BodySizeParts - The outfit body parts grouped by BodySize.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Body Parts Skeletal Mesh |
| Type | FChaosGetOutfitBodyPartsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| BodySizeParts | The outfit body parts grouped by BodySize. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getoutfitclothcollections.md

# GetOutfitClothCollections

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections

> Application Version: 5.7

### Description

GetOutfitClothCollections (v1)
Experimental

Extract the cloth collections contained into the specified source outfit.

Input(s) :
Outfit - The source outfit.
LodIndex - The LOD to output in the cloth collections array. Set to -1 to output all LODs

Output(s):
Outfit [Passthrough] - The source outfit.
ClothCollections - The outfit cloth collections array in group of consecutives LODs for each of the outfit pieces.
NumLods - The number of LODs output in the cloth collections array.
NumPieces - The number of cloth pieces output in the cloth collections array.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Cloth Collections |
| Type | FChaosGetOutfitClothCollectionsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| LodIndex | The LOD to output in the cloth collections array. Set to -1 to output all LODs | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| ClothCollections | The outfit cloth collections array in group of consecutives LODs for each of the outfit pieces. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |
| NumLods | The number of LODs output in the cloth collections array. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| NumPieces | The number of cloth pieces output in the cloth collections array. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getoutfitrbfinterpolationdata.md

# GetOutfitRBFInterpolationData

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData

> Application Version: 5.7

### Description

GetOutfitRBFInterpolationData (v1)
Experimental

Extract the Body Part RBF Interpolation Data from an outfit.

Input(s) :
Outfit - The source outfit.
BodySizeIndex - The body size index.
BodyPartIndex - The body part (sub) index.

Output(s):
Outfit [Passthrough] - The source outfit.
InterpolationData - The interpolation data.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit RBF Interpolation Data |
| Type | FChaosGetOutfitRBFInterpolationDataNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| BodySizeIndex | The body size index. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| BodyPartIndex | The body part (sub) index. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| InterpolationData | The interpolation data. | [FMeshResizingRBFInterpolationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getphysicsassetfromskeletalmesh.md

# GetPhysicsAssetFromSkeletalMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetPhysicsAssetFromSkeletalMesh

> Application Version: 5.7

### Description

GetPhysicsAssetFromSkeletalMesh (v1)

Get the physics assets from input skeletal mesh.

Input(s) :
SkeletalMesh - Input skeletal mesh

Output(s):
PhysicsAsset - Output physics asset

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | General |
| Tags | Get Physics Asset Skeletal Mesh |
| Type | [FGetPhysicsAssetFromSkeletalMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FGetPhysicsAssetFromSkeletalMesh-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh | Input skeletal mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsAsset | Output physics asset | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UPhysicsAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UPhysicsAsset)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getphysicssolvers.md

# GetPhysicsSolvers

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetPhysicsSolvers

> Application Version: 5.7

### Description

GetPhysicsSolvers (v1)

Get physics solvers from context

Output(s):
PhysicsSolvers - Physics solvers coming from the context and filtered with the groups

### Information

|  |  |
| --- | --- |
| Module | [DataflowSimulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation) |
| Category | Physics|Solver |
| Tags | DataflowSimulationTag |
| Type | [FGetPhysicsSolversDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FGetPhysicsSolversDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationGroups | Simulation groups to filter the output solvers properties | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolvers | Physics solvers coming from the context and filtered with the groups | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getrootindexfromcollection.md

# GetRootIndexFromCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetRootIndexFromCollection

> Application Version: 5.7

### Description

GetRootIndexFromCollection (v1)

Get the root node index

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetRootIndexFromCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetRootIndexFromCollectionDataf-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getschema.md

# GetSchema

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSchema

> Application Version: 5.7

### Description

GetSchema (v1)

Collects group and attribute information from the Collection and outputs it into a formatted string

Input(s) :
Collection - GeometryCollection for the information

Output(s):
String - Formatted string containing the groups and attributes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetSchemaDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetSchemaDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the information | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| String | Formatted string containing the groups and attributes | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getsimulationtime.md

# GetSimulationTime

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSimulationTime

> Application Version: 5.7

### Description

GetSimulationTime (v1)

Get the context simulation time

Output(s):
SimulationTime - Simulation time property coming from the context

### Information

|  |  |
| --- | --- |
| Module | [DataflowSimulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation) |
| Category | Physics|Common |
| Tags | DataflowSimulationTag |
| Type | [FGetSimulationTimeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FGetSimulationTimeDataflowNode) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationTime | Simulation time property coming from the context | [FDataflowSimulationTime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationTime) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getskinningselection.md

# GetSkinningSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSkinningSelection

> Application Version: 5.7

### Description

GetSkinningSelection (v1)
Experimental

Get skin weights selection attributes.

Output(s):
SelectionMapKey - Selection map key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [DataflowEditor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor) |
| Category | Collection |
| Tags | Get the skin weights selection for a future correction |
| Type | [FDataflowGetSkinningSelectionNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/FDataflowGetSkinningSelectionNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| CorrectionType | Selection map key to be used in other nodes if necessary | [ESkinWeightsCorrectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/ESkinWeightsCorrectionType) | Relax |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SelectionMapKey | Selection map key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getspherecoveringspherecount.md

# Get Sphere Covering Sphere Count

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSphereCoveringSphereCount

> Application Version: 5.7

### Description

Get Sphere Covering Sphere Count (v1)

Report the number of spheres in a sphere covering

Input(s) :
SphereCovering [Intrinsic] - The sphere covering to evaluate

Output(s):
NumSpheres - Number of spheres in the sphere covering

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | SphereCovering |
| Type | [FSphereCoveringCountSpheresNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSphereCoveringCountSpheresNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SphereCovering | The sphere covering to evaluate | [FDataflowSphereCovering](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowSphereCovering) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumSpheres | Number of spheres in the sphere covering | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getstaticmeshboundingbox.md

# GetStaticMeshBoundingBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetStaticMeshBoundingBox

> Application Version: 5.7

### Description

GetStaticMeshBoundingBox (v1)

Get the local geometric bounding box a static mesh

Input(s) :
StaticMesh - Static Mesh to compute the bouning box from

Output(s):
BoundingBox - Geometric bounding box of the input Static Mesh
Center - Center of the resulting bounding box
Dimensions - Dimensions of the resulting bounding box in centimers

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Static Mesh |
| Tags | Bounds Size Dimensions Extents Center |
| Type | [FGetStaticMeshBoundingBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FGetStaticMeshBoundingBoxDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StaticMesh | Static Mesh to compute the bouning box from | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | Geometric bounding box of the input Static Mesh | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center | Center of the resulting bounding box | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Dimensions | Dimensions of the resulting bounding box in centimers | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getstringoverridefromasset.md

# GetStringOverrideFromAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetStringOverrideFromAsset

> Application Version: 5.7

### Description

GetStringOverrideFromAsset (v1)

Get String Override from Asset Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Overrides |
| Type | [FGetStringOverrideFromAssetDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetStringOverrideFromAssetDataf-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Key |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Key |
| Default |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IsOverriden |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| String |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| StringDefault |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getsurfaceindices.md

# GetSurfaceIndices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSurfaceIndices

> Application Version: 5.7

### Description

GetSurfaceIndices (v1)

Get Surface Indices Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FGetSurfaceIndicesNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FGetSurfaceIndicesNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| GeometryGroupGuidsIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SurfaceVertexSelection |  | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-getvariable.md

# GetVariable

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetVariable

> Application Version: 5.7

### Description

GetVariable (v1)

Get Dataflow Variable Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | Dataflow |
| Type | [FGetDataflowVariableNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FGetDataflowVariableNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VariablePropertyBag |  | [FInstancedPropertyBag](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FInstancedPropertyBag) | (Value=None) |
| VariableName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-gridscatterpoints.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-groomassetterminal.md

# GroomAssetTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetTerminal

> Application Version: 5.7

### Description

GroomAssetTerminal (v2)
Experimental

Groom Asset Terminal Dataflow Node V 2

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGroomAssetTerminalDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGroomAssetTerminalDataflowNode_-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeNames | Attributes names used for the keys | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GuidesCollection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| StrandsCollection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-groomassettocollection.md

# GroomAssetToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection

> Application Version: 5.7

### Description

GroomAssetToCollection (v1)
Experimental

Transform a groom asset to a collection

Input(s) :
GroomAsset - Input asset to read the guides from
CurvesType - Type of curves to use to fill the groom collection (guides/strands)
CurvesThickness - Curves thickness for geometry generation

Output(s):
Collection - Managed array collection used to store the curves

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGroomAssetToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGroomAssetToCollectionDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroomAsset | Input asset to read the guides from | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGroomAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsCore/UGroomAsset)> | None |
| CurvesThickness | Curves thickness for geometry generation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| CurvesType | Type of curves to use to fill the groom collection (guides/strands) | [EGroomCollectionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/EGroomCollectionType) | Guides |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection used to store the curves | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-growtileregion.md

# GrowTileRegion

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion

> Application Version: 5.7

### Description

GrowTileRegion (v1)
Experimental

Finds a square tile within a specified image region and duplicates it over the whole image.
The image region to search is determined by the UV coordinates in ValidRegionMesh -- only texels inside a 2D UV mesh triangle are considered when searching for a tile.
Note this node does not try to detect any repeating patterns, it just grabs the first square tile of the specified size that is entirely inside the UV mesh.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Grow Tile |
| Type | FMeshResizingGrowTileRegionNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshUVLayer |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| TileWidth |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| ValidRegionMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
| MeshMask |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-hashstring.md

# HashString

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/HashString

> Application Version: 5.7

### Description

HashString (v1)

Generates a hash value from a string

Input(s) :
String - String to hash

Output(s):
Hash - Generated hash value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|String |
| Type | [FHashStringDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FHashStringDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| String | String to hash | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Hash | Generated hash value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-hashvector.md

# HashVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/HashVector

> Application Version: 5.7

### Description

HashVector (v1)

Generates a hash value from a vector

Input(s) :
Vector - Vector to hash

Output(s):
Hash - Generated hash value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Vector |
| Type | [FHashVectorDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FHashVectorDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector | Vector to hash | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Hash | Generated hash value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-imagecombinechannels.md

# ImageCombineChannels

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels

> Application Version: 5.7

### Description

ImageCombineChannels (v1)

Combine channels into a single RGBA image
Outputs are single channel images

Input(s) :
Red - Red channel - if not connected, use black color
Green - Green channel - if not connected, use black color
Blue - Blue channel - if not connected, use black color
Alpha - Alpha channel - if not connected, use black color

Output(s):
Image - Output image recombined from input channels

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Image |
| Type | [FDataflowImageCombineChannelsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImageCombineChannelsNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResolutionOptions | resolution option | [EDataflowImageCombineResolutionOption](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageCombineResolutionO-) | Highest |
| Resolution | resolution of the output image if the resolution option is set to user defined | [EDataflowImageResolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageResolution) | Resolution512 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Red | Red channel - if not connected, use black color | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Green | Green channel - if not connected, use black color | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Blue | Blue channel - if not connected, use black color | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Alpha | Alpha channel - if not connected, use black color | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image | Output image recombined from input channels | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-imagefromcolor.md

# ImageFromColor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor

> Application Version: 5.7

### Description

ImageFromColor (v1)

Create a RGBA image from a single color at a specific resolution
Outputs are single channel images

Input(s) :
FillColor - color to fill the image with
Resolution - resolution of the output image

Output(s):
Image - Output image

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Image |
| Type | [FDataflowImageFromColorNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImageFromColorNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FillColor | color to fill the image with | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |
| Resolution | resolution of the output image | [EDataflowImageResolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageResolution) | Resolution16 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image | Output image | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-imagesplitchannels.md

# ImageSplitChannels

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageSplitChannels

> Application Version: 5.7

### Description

ImageSplitChannels (v1)

Split a image in individual channels
Outputs are single channel images

Input(s) :
Image - Input image to split per channel

Output(s):
Red - Red channel
Green - Green channel
Blue - Blue channel
Alpha - Alpha channel

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Image |
| Type | [FDataflowImageSplitChannelsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImageSplitChannelsNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image | Input image to split per channel | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Red | Red channel | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
| Green | Green channel | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
| Blue | Blue channel | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
| Alpha | Alpha channel | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-imagetotexture.md

# ImageToTexture

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageToTexture

> Application Version: 5.7

### Description

ImageToTexture (v1)

Create a transient texture asset from an image

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | Image |
| Tags | Image Texture |
| Type | [FDataflowImageToTextureNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowImageToTextureNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| TextureName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransientTexture |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-importsimulationcache.md

# ImportSimulationCache

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache

> Application Version: 5.7

### Description

ImportSimulationCache (v1)
Experimental

Set vertex values from a simulation cache. The topology of the Collection will remain the same.

Input(s) :
Collection - Input/output collection
ImportedCache - Cache to import in.

Output(s):
Collection [Passthrough] - Input/output collection

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Import Cache |
| Type | [FChaosClothAssetImportSimulationCacheNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_4) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CacheIndex | Cache index to read | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| CacheTime | Cache time to read | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Transform | Transform cache data. | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| ParticleOffset | Particle cache offset. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bUpdateSimulationMesh | Update simulation mesh from cache. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bRecalculateNormals | Recalculate simulation normals based on imported positions. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUpdateRenderMesh | Update render mesh from cache via proxy deformer data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| ImportedCache | Cache to import in. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosCacheCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosCaching/UChaosCacheCollection)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-inversesquareroot.md

# InverseSquareRoot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/InverseSquareRoot

> Application Version: 5.7

### Description

InverseSquareRoot (v1)

Inverse Square Root ( 1 / sqrt(A) )
if A is equal to 0, returns Fallback

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | OneOverSquareRoot |
| Type | [FDataflowMathInverseSquareRootNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathInverseSquareRootNo-) |

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

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-inverttransform.md

# InvertTransform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/InvertTransform

> Application Version: 5.7

### Description

InvertTransform (v1)

Invert a transform.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Transform |
| Type | [FInvertTransformDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FInvertTransformDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InTransform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutTransform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-isnearlyzero.md

# IsNearlyZero

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/IsNearlyZero

> Application Version: 5.7

### Description

IsNearlyZero (v1)

Is Nearly Zero Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Utilities |
| Type | [FIsNearlyZeroDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FIsNearlyZeroDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Float |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-isolatecomponent.md

# IsolateComponent

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/IsolateComponent

> Application Version: 5.7

### Description

IsolateComponent (v1)

Isolate Component Node

Input(s) :
Collection - typedef FManagedArrayCollection DataType;

Output(s):
Collection [Passthrough] - typedef FManagedArrayCollection DataType;

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FIsolateComponentNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FIsolateComponentNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeleteHiddenFaces |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| TargetGeometryIndex |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-kinematicbodysetupinitialization.md

# KinematicBodySetupInitialization

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicBodySetupInitialization

> Application Version: 5.7

### Description

KinematicBodySetupInitialization (v1)

@todo(deprecate), rename to FCollisionBodyConstraintDataflowNode

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FKinematicBodySetupInitializationDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FKinematicBodySetupInitializatio-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-kinematicinitialization.md

# KinematicInitialization

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicInitialization

> Application Version: 5.7

### Description

KinematicInitialization (v1)

@todo(deprecate), rename to FKinematicConstraintDataflowNode

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FKinematicInitializationDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FKinematicInitializationDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 40.000000 |
| SkeletalSelectionMode |  | [ESkeletalSeletionMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/ESkeletalSeletionMode) | Dataflow\_SkeletalSelection\_Single |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| VertexIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| BoneIndexIn |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-kinematicmuscleattachments.md

# KinematicMuscleAttachments

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicMuscleAttachments

> Application Version: 5.7

### Description

KinematicMuscleAttachments (v1)

Kinematic Muscle Attachments Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FKinematicMuscleAttachmentsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FKinematicMuscleAttachmentsDataf-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OriginVertexIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InsertionVertexIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-kinematicskeletalmeshinitialization.md

# KinematicSkeletalMeshInitialization

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicSkeletalMeshInitialization

> Application Version: 5.7

### Description

KinematicSkeletalMeshInitialization (v1)

@todo(deprecate), rename to FSkeletalMeshConstraintDataflowNode

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FKinematicSkeletalMeshInitializationDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FKinematicSkeletalMeshInitializa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| IndicesOut |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-kinematicskeletonconstraint.md

# KinematicSkeletonConstraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicSkeletonConstraint

> Application Version: 5.7

### Description

KinematicSkeletonConstraint (v1)

Bind a animation driven skeleton hierarchy into the tetrahedron on the collection.

Input(s) :
Collection - Pass through collection to place constraints in to.
SkeletonIn - Skeleton to constraint to the tetrahedron (Must be co-located with the tetrahedron).

Output(s):
Collection [Passthrough] - Pass through collection to place constraints in to.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FKinematicSkeletonConstraintDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FKinematicSkeletonConstraintData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExclusionList | Skeleton bones to exclude from the constraint. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Pass through collection to place constraints in to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletonIn | Skeleton to constraint to the tetrahedron (Must be co-located with the tetrahedron). | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Pass through collection to place constraints in to. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-lerp.md

# Lerp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Lerp

> Application Version: 5.7

### Description

Lerp (v1)

Linearly interpolates between A and B based on Alpha. (100% of A when Alpha = 0.0 and 100% of B when Alpha = 1.0)

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FLerpDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FLerpDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| B |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Alpha |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-lineartosplineskinweights.md

# LinearToSplineSkinWeights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/LinearToSplineSkinWeights

> Application Version: 5.7

### Description

LinearToSplineSkinWeights (v1)
Experimental

Convert linear skinning data to spline skinning data

Input(s) :
Collection - Managed array collection to be used to store datas
VertexSelection - Vertex selection to process vertices subset

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
SplineParamKey - Spline skinning parameter key
SplineBonesKey - Spline bones key. Used for storing root and end spline bone for each vertex.

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FLinearToSplineSkinWeightsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FLinearToSplineSkinWeightsDatafl-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection to process vertices subset | [FDataflowVertexSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SplineParamKey | Spline skinning parameter key | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| SplineBonesKey | Spline bones key. Used for storing root and end spline bone for each vertex. | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-log.md

# Log

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Log

> Application Version: 5.7

### Description

Log (v1)

Natural log ( Log(A) )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Logarithm |
| Type | [FDataflowMathLogNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathLogNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-logx.md

# LogX

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/LogX

> Application Version: 5.7

### Description

LogX (v1)

Log for a specific base ( Log[Base](A) )
If base is negative or zero returns 0

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Logarithm |
| Type | [FDataflowMathLogXNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathLogXNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |
| Base |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=10.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeattributekey.md

# MakeAttributeKey

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeAttributeKey

> Application Version: 5.7

### Description

MakeAttributeKey (v1)

Make Attribute Key Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | GeometryCollection |
| Type | [FMakeAttributeKeyDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FMakeAttributeKeyDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupIn |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| AttributeIn |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeKeyOut |  | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makebox.md

# MakeBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeBox

> Application Version: 5.7

### Description

MakeBox (v1)

Make a box

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Box |
| Type | [FMakeBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeBoxDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DataType |  | [EMakeBoxDataTypeEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EMakeBoxDataTypeEnum) | Dataflow\_MakeBox\_DataType\_MinMax |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Min |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Max |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=10.000000,Y=10.000000,Z=10.000000) |
| Center |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Size |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=10.000000,Y=10.000000,Z=10.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box |  | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeboxmesh.md

# MakeBoxMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeBoxMesh

> Application Version: 5.7

### Description

MakeBoxMesh (v1)

Make a box mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeBoxMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeBoxMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Center |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Size |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=5.000000,Y=5.000000,Z=5.000000) |
| SubdivisionsX |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |
| SubdivisionsY |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |
| SubdivisionsZ |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 3 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makecapsulemesh.md

# MakeCapsuleMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCapsuleMesh

> Application Version: 5.7

### Description

MakeCapsuleMesh (v1)

Make a capsule mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeCapsuleMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeCapsuleMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius | Radius of capsule | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SegmentLength | Length of capsule line segment, so total height is SegmentLength + 2\*Radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| NumHemisphereArcSteps | Number of vertices along the 90-degree arc from the pole to edge of spherical cap. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| NumCircleSteps | Number of vertices along each circle | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 6 |
| NumSegmentSteps | Number of subdivisions lengthwise along the cylindrical section | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeclothasset.md

# MakeClothAsset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeClothAsset

> Application Version: 5.7

### Description

MakeClothAsset (v1)
Experimental

Cloth terminal node to generate a cloth asset from a cloth collection.

Input(s) :
CollectionLodsArray - Input cloth collections for this LOD -- Array connection. Individual CollectionLods will be ignored if there is a CollectionLodsArray connection.

Output(s):
ClothAsset - The cloth asset output.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Make Cloth Asset |
| Type | FChaosClothAssetMakeClothAssetNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CollectionLodsArray | Input cloth collections for this LOD -- Array connection. Individual CollectionLods will be ignored if there is a CollectionLodsArray connection. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClothAsset | The cloth asset output. | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosClothAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetEngine/UChaosClothAsset)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makecollection.md

# MakeCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCollection

> Application Version: 5.7

### Description

MakeCollection (v1)

Make an empty ManagedArrayCollection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Collection |
| Type | [FMakeCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeCollectionDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAddRootTransform | if true, create a root transform | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makeconvexdecompositionsettings.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makecylindermesh.md

# MakeCylinderMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCylinderMesh

> Application Version: 5.7

### Description

MakeCylinderMesh (v1)

Make a cylinder mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeCylinderMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeCylinderMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius1 | Radius1 of cylinder | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Radius2 | Radius2 of cylinder | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Height | Height of cylinder | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| LengthSamples | LengthSamples of cylinder | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| AngleSamples | AngleSamples of cylinder | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makedataflowmesh.md

# MakeDataflowMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeDataflowMesh

> Application Version: 5.7

### Description

MakeDataflowMesh (v1)

Create a UDataflow mesh from an input UDynamicMesh and material array

Input(s) :
InMesh [Intrinsic] - DynamicMesh input
InMaterials [Intrinsic] - Materials input

Output(s):
Mesh - DataflowMesh output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FMakeDataflowMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeDataflowMeshDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InMesh | DynamicMesh input | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| InMaterials | Materials input | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DataflowMesh output | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makediscmesh.md

# MakeDiscMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeDiscMesh

> Application Version: 5.7

### Description

MakeDiscMesh (v1)

Make a disc mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeDiscMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeDiscMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius | Radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Normal | Normal vector of all vertices will be set to this value. Default is +Z axis. | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| AngleSamples | Number of vertices around circumference | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |
| RadialSamples | Number of vertices along radial spokes | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| StartAngle | Start of angle range spanned by disc, in degrees | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| EndAngle | End of angle range spanned by disc, in degrees | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 360.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-makefloatarray.md

# MakeFloatArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeFloatArray

> Application Version: 5.7

### Description

MakeFloatArray (v1)

M

Input(s) :
NumElements - Number of elements of the array
Value - Value to initialize the array with

Output(s):
FloatArray - Output float array

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FMakeFloatArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeFloatArrayDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumElements | Number of elements of the array | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| Value | Value to initialize the array with | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Output float array | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

