# Unidad 15

Rango: archivos 1681 a 1800 de 3470

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-maximum.md

# Maximum

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Maximum

> Application Version: 5.7

### Description

Returns the larger of the two values
Returns the larger of the two values each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Maximum |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-middle.md

# Middle

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Middle

> Application Version: 5.7

### Description

Returns the middle section of a string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | Within,Center |
| Type | [FRigVMFunction\_StringMiddle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringMiddle) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to retrieve a section of | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Start | the index of the first character | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Count | if count is set to -1 all character from Start will be returned | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting section of the input string given start and count | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-minimum.md

# Minimum

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Minimum

> Application Version: 5.7

### Description

Returns the smaller of the two values
Returns the smaller of the two values for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Minimum |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-mirror.md

# Mirror

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Mirror

> Application Version: 5.7

### Description

Mirror a rotation about a central transform.
Mirror a transform about a central transform.
Mirror a vector about a central transform.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Mirror |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| MirrorAxis | the axis to mirror against | [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | X |
| AxisToFlip | the axis to flip for rotations | [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | Z |
| CentralTransform | The transform about which to mirror | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting mirrored rotation | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-mirroronnormal.md

# Mirror on Normal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MirroronNormal

> Application Version: 5.7

### Description

Mirror a vector about a normal vector.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Type | [FRigVMFunction\_MathVectorMirror](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorMirror) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input vector to mirror | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Normal | The normal to mirror the vector by | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting mirrored vector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-modifytransforms.md

# Modify Transforms

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ModifyTransforms

> Application Version: 5.7

### Description

Modify Transforms is used to perform a change in the hierarchy by setting one or more bones' transforms

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | ModifyBone |
| Type | [FRigUnit\_ModifyTransforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ModifyTransforms) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ItemToModify | The items to modify. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_ModifyTransforms\_PerItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ModifyTransforms_PerIte-)> | (()) |
| Weight | At 1 this sets the transform, between 0 and 1 the transform is blended with previous results. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| WeightMinimum | The minimum of the weight - defaults to 0.0 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WeightMaximum | The maximum of the weight - defaults to 1.0 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Mode | Defines if the bone's transform should be set in local or global space, additive or override. | [Control Rig Modify Bone Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigModifyBoneMode) | AdditiveLocal |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-modulo.md

# Modulo

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Modulo

> Application Version: 5.7

### Description

Returns the modulo of the two values

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Modulo,%,fmod |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-moveboxto.md

# Move Box To

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MoveBoxTo

> Application Version: 5.7

### Description

Moves the center of the box to a new location

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,Translate,Move,BoundingBox |
| Type | [FRigVMFunction\_MathBoxMoveTo](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxMoveTo) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | the box to move | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Center | the new center for the box | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting moved box | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-multieffectorfabrik.md

# Multi Effector FABRIK

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MultiEffectorFABRIK

> Application Version: 5.7

### Description

The FABRIK solver can solve multi chains within a root using multi effectors
the Forward and Backward Reaching Inverse Kinematics algorithm.
For now this node supports single effector chains only.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Multi, Effector, N-Chain,IK |
| Type | [FRigUnit\_MultiFABRIK](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_MultiFABRIK) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootBone | The first bone in the chain to solve | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Effectors | The list of effectors to use for the solver | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_MultiFABRIK\_EndEffector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_MultiFABRIK_EndEffector)> | () |
| Precision | The precision to use for the fabrik solver | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| MaxIterations | The maximum number of iterations. Values between 4 and 16 are common. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-multiply.md

# Multiply

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Multiply

> Application Version: 5.7

### Description

Returns the product of the two values

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Multiply,Product,\*,Global |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first color for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| B | The second color for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting color | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-nand.md

# Nand

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Nand

> Application Version: 5.7

### Description

Returns false if both conditions are true

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Type | [FRigVMFunction\_MathBoolNand2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolNand2) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value for the operation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| B | The second value for the operation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-negate.md

# Negate

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Negate

> Application Version: 5.7

### Description

Returns the negative value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Negate,-,Abs |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-noise.md

# Noise

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Noise

> Application Version: 5.7

### Description

Generates a float through a noise fluctuation process between a min and a max through speed
Generates a double through a noise fluctuation process between a min and a max through speed
Generates a vector through a noise fluctuation process between a min and a max through speed

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Noise |
| Tags | Noise,Noise (Float),Noise (Double),Noise (Vector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to retrieve the noise for | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Speed | The speed of the noise field | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.100000 |
| Frequency | The frequency of the noise field | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| Minimum | The minimum range of the noise | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |
| Maximum | The maximum range of the noise | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value in the noise field | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-not.md

# Not

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Not

> Application Version: 5.7

### Description

Returns true if the condition is false

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Tags | ! |
| Type | [FRigVMFunction\_MathBoolNot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolNot) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-notequals.md

# Not Equals

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/NotEquals

> Application Version: 5.7

### Description

Compares any two values and return true if they are not identical

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Different,!=,Xor |
| Type | [FRigVMDispatch\_CoreNotEquals](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CoreNotEquals) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value to compare | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| B | The second value to compare | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The boolean result of the comparison | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-now.md

# Now

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Now

> Application Version: 5.7

### Description

Returns the current time (year, month, day, hour, minute)

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Tags | Time,Clock |
| Type | [FRigVMFunction\_GetWorldTime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_GetWorldTime) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Year | The Year of the world time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Month | The Month of the world time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Day | The Day of the world time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| WeekDay | The WeekDay of the world time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Hours | The Hours of the world time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Minutes | The Minutes of the world time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Seconds | The Seconds of the world time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| OverallSeconds | The OverallSeconds of the world time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-num.md

# Num

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Num

> Application Version: 5.7

### Description

Returns the number of elements of an array

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayGetNum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayGetNum) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array to retrieve the size for. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Num | The size of the input array. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-offsettransform.md

# Offset Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/OffsetTransform

> Application Version: 5.7

### Description

Offset Transform is used to add an offset to an existing transform in the hierarchy. The offset is post multiplied.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | Offset,Relative,AddBoneTransform |
| Type | [FRigUnit\_OffsetTransformForItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_OffsetTransformForItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to offset the transform for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| OffsetTransform | The transform of the item relative to its previous transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Weight | Defines how much the change will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true children of affected items in the hierarchy will follow the transform change - otherwise only the parent will move. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-once.md

# Once

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Once

> Application Version: 5.7

### Description

Returns true once the first time this node is hit

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Tags | FlipFlop,Toggle,Changed,Different |
| Type | [FRigVMFunction\_MathBoolOnce](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolOnce) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Duration | The duration in seconds at which the result is true Use 0 for a different result every time. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value - true once the first time this node is hit | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-or.md

# Or

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Or

> Application Version: 5.7

### Description

Returns true if one of the conditions is true

### Information

|  |  |  |  |
| --- | --- | --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |  |  |
| Category | Math|Boolean |  |  |
| Tags |  |  |  |
| Type | [FRigVMFunction\_MathBoolOr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolOr) |  |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value for the operation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| B | The second value for the operation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-orthogonal.md

# Orthogonal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Orthogonal

> Application Version: 5.7

### Description

Returns true if the two vectors are orthogonal

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Type | [FRigVMFunction\_MathVectorOrthogonal](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorOrthogo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first vector to compare | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| B | The second vector to compare | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the two vectors A and B are orthogonal | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-padinteger.md

# Pad Integer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PadInteger

> Application Version: 5.7

### Description

Converts an integer number to a string with padding

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | FromInt,Number,LeadingZeroes |
| Type | [FRigVMFunction\_StringPadInteger](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringPadInteger) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input number to convert to a string (for example 4) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Digits | The number of digits in total to use (for example 3) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting string representing the padded integer (for example '004') | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-parallel.md

# Parallel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Parallel

> Application Version: 5.7

### Description

Returns true if the two vectors are parallel

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Type | [FRigVMFunction\_MathVectorParallel](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorParalle-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first vector to compare | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| B | The second vector to compare | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the two vectors A and B are parallel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-parameteratlengthpercentage.md

# Parameter At Length Percentage

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParameterAtLengthPercentage

> Application Version: 5.7

### Description

Returns the U parameter of a spline given a length percentage (0.0 - 1.0)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_ParameterAtPercentage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_ParameterAtPercentage) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| Percentage | The percentage (0.0 - 1.0) to evaluate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| U | The U value on the spline for the given percentage | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-parentconstraint.md

# Parent Constraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraint

> Application Version: 5.7

### Description

Constrains an item's transform to multiple items' transforms

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent,Orient,Scale |
| Type | [FRigUnit\_ParentConstraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraint) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to constrain | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bMaintainOffset | If True the offset will be computed based on the current delta between each child and parent | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | The filter to apply on the transform | [Transform Filter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FTransformFilter) | (TranslationFilter=(bX=True,bY=True,bZ=True),RotationFilter=(bX=True,bY=True,bZ=True),ScaleFilter=(bX=True,bY=True,bZ=True)) |
| Parents | The array of parents to constrain the child to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings of the constraint operation | [Rig Unit Parent Constraint Advanced Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraint_Advanc-) | (InterpolationType=Average,RotationOrderForFilter=XZY) |
| Weight | The weight to use when applying the resulting transform to the child | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-parentconstraintmath.md

# Parent Constraint Math

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraintMath

> Application Version: 5.7

### Description

Computes the output transform by constraining the input transform to multiple parents

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent,Orient,Scale |
| Type | [FRigUnit\_ParentConstraintMath](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraintMath) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Input | Input is used to calculate offsets from parents' initial transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Parents | The array of parents to compute the constrained transform for | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings to use for the constraint compute | [Rig Unit Parent Constraint Math Advanced Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraintMath_Ad-) | (InterpolationType=Average) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output | The resulting constrained transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-pi.md

# Pi

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Pi

> Application Version: 5.7

### Description

Returns PI

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Pi |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value of the constant | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 3.141593 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-positionconstraint.md

# Position Constraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PositionConstraint

> Application Version: 5.7

### Description

Constrains an item's position to multiple items' positions

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent,Translation |
| Type | [FRigUnit\_PositionConstraintLocalSpaceOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PositionConstraintLocal-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to constrain | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bMaintainOffset | If True the offset will be computed based on the current delta between each child and parent | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | The filter to apply on the transform | [Filter Option Per Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FFilterOptionPerAxis) | (bX=True,bY=True,bZ=True) |
| Parents | The array of parents to constrain the child to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| Weight | The weight to use when applying the resulting transform to the child | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-positionfromspline.md

# Position From Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PositionFromSpline

> Application Version: 5.7

### Description

Retrieves the position from a given Spline and U value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Point From Spline |
| Type | [FRigUnit\_PositionFromControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_PositionFromControlRigS-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| U | The U value along the spline to evaluate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Position | The resulting position on the spline | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-postconstruction.md

# Post Construction

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PostConstruction

> Application Version: 5.7

### Description

Event to further configure elements. Runs after the Construction Event

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Events |
| Tags | Create,Build,Spawn,Setup,Init,Fit |
| Type | [FRigUnit\_PostPrepareForExecution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PostPrepareForExecution) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-postforwardssolve.md

# Post Forwards Solve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PostForwardsSolve

> Application Version: 5.7

### Description

Event always executed after the forward solve

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Events |
| Tags | Begin,Update,Tick,PostForward,Event |
| Type | [FRigUnit\_PostBeginExecution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PostBeginExecution) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-power.md

# Power

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Power

> Application Version: 5.7

### Description

Returns the value of A raised to the power of B.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Power |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| B | The second number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-preforwardssolve.md

# Pre Forwards Solve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PreForwardsSolve

> Application Version: 5.7

### Description

Event always executed before the forward solve

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Events |
| Tags | Begin,Update,Tick,PreForward,Event |
| Type | [FRigUnit\_PreBeginExecution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PreBeginExecution) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-print.md

# Print

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Print

> Application Version: 5.7

### Description

Prints any value to the log

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Type | [FRigVMDispatch\_Print](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_Print) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Prefix | The prefix to place at the start of the printed out message | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Value | The value to print | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| Enabled | If False the printing of the message will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ScreenDuration | The duration of the printed message to appear on the screen | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.050000 |
| ScreenColor | The color of the message on the screen | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-projecttonewparent.md

# Project to new Parent

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ProjecttonewParent

> Application Version: 5.7

### Description

Gets the relative offset between the child and the old parent, then multiplies by new parent's transform.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | ProjectTransformToNewParent,Relative,Reparent,Offset |
| Type | [FRigUnit\_ProjectTransformToNewParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ProjectTransformToNewPa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The element to project between parents | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bChildInitial | If set to true the child will be retrieved in its initial transform | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| OldParent | The original parent of the child. Can be an actual parent in the hierarchy or any other item you want to use to compute to offset against. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bOldParentInitial | If set to true the old parent will be retrieved in its initial transform | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| NewParent | The new parent of the child. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bNewParentInitial | If set to true the new parent will be retrieved in its initial transform | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The resulting transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-radians.md

# Radians

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Radians

> Application Version: 5.7

### Description

Returns the radians of a given value in degrees

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Radians |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-random.md

# Random

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Random

> Application Version: 5.7

### Description

Generates a random float between a min and a max
Generates a random vector between a min and a max

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Random |
| Tags | Random,Random (Float),Random (Vector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Seed | The seed for the random number generator | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 217 |
| Minimum | The minimum value for the random number range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | The maximum value for the random number range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Duration | The duration at which the number won't change. Use 0 for a different number every time. A negative number (for ex: -1) results in an infinite duration. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting random number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-rbfquaternion.md

# RBF Quaternion

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFQuaternion

> Application Version: 5.7

### Description

A RBF interpolator from quaternion to float
A RBF interpolator from quaternion to vector
A RBF interpolator from quaternion to color
A RBF interpolator from quaternion to quaternion
A RBF interpolator from quaternion to transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|RBF Interpolation |
| Tags | RBF Quaternion,RBF Quaternion to Float,RBF,Interpolate,Quaternion,RBF Quaternion to Vector,RBF Quaternion to Color,RBF Quaternion to Quaternion,RBF Quaternion to Transform |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Targets | The array of targets to interpolate within | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatFloat\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatFloat_Tar-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatVector\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatVector_Ta-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatColor\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatColor_Tar-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatQuat\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatQuat_Targ-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateQuatXform\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateQuatXform_Tar-)> | () |
| Input | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| DistanceFunction | The distance function to use | [RBFQuat Distance Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFQuatDistanceType) | ArcLength |
| SmoothingFunction | The smoothing function to use | [RBFKernel Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFKernelType) | Gaussian |
| SmoothingAngle | The smoothing angle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 45.000000 |
| bNormalizeOutput | If true the resulting output will be normalized | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| TwistAxis | The twist axis of the input quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output | The interpolated result | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-rbfvector.md

# RBF Vector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFVector

> Application Version: 5.7

### Description

A RBF interpolator from vector to float
A RBF interpolator from vector to vector
A RBF interpolator from vector to color
A RBF interpolator from vector to quaternion
A RBF interpolator from vector to transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|RBF Interpolation |
| Tags | RBF Vector,RBF Vector to Float,RBF,Interpolate,Vector,RBF Vector to Vector,RBF Vector to Color,RBF Vector to Quat,RBF Vector to Transform |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Targets | The array of targets to interpolate within | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorFloat\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorFloat_T-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorVector\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorVector_-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorColor\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorColor_T-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorQuat\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorQuat_Ta-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorXform\_Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorXform_T-)> | () |
| Input | The input vector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| DistanceFunction | The distance function to use | [RBFVector Distance Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFVectorDistanceType) | Euclidean |
| SmoothingFunction | The smoothing function to use | [RBFKernel Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFKernelType) | Gaussian |
| SmoothingRadius | The radius to apply for the smoothing function | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| bNormalizeOutput | If true the resulting output will be normalized | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output | The interpolated result | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-remap.md

# Remap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Remap

> Application Version: 5.7

### Description

Remaps the given value from a source range to a target range.
Remaps the given value from a source range to a target range for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Remap,Rescale,Scale |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to remap | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SourceMinimum | The minimum of the range of the input / source value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SourceMaximum | The maximum of the range of the input / source value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| TargetMinimum | The minimum of the range of the output / target value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| TargetMaximum | The maximum of the range of the output / target value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| bClamp | If set to true the result is clamped to the target range | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting remapped value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-remove.md

# Remove

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Remove

> Application Version: 5.7

### Description

Removes an element from an array by index.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayRemove](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayRemove) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to remove an element from. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index at which to remove the element. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-removeallmetadata.md

# Remove All Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveAllMetadata

> Application Version: 5.7

### Description

Removes an existing metadata filed from an item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | DeleteMetadata |
| Type | [FRigUnit\_RemoveAllMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_RemoveAllMetadata) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to remove the metadata from | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Removed | True if any metadata has been removed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-removeitem.md

# Remove Item

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveItem

> Application Version: 5.7

### Description

Removes an element from the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Delete,Erase,Joint,Skeleton |
| Type | [FRigUnit\_HierarchyRemoveElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyRemoveElement) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to remove | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSuccess | True if the element has been removed successfuly | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-removemetadata.md

# Remove Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveMetadata

> Application Version: 5.7

### Description

Removes an existing metadata filed from an item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | DeleteMetadata |
| Type | [FRigUnit\_RemoveMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_RemoveMetadata) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to remove the metadata from | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the metadata to remove | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Removed | True if the metadata has been removed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-removetag.md

# Remove Tag

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveTag

> Application Version: 5.7

### Description

Removes a tag from an item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | DeleteTag |
| Type | [FRigUnit\_RemoveMetadataTag](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_RemoveMetadataTag) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to set the metadata for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Tag | The name of the tag to set | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Removed | Returns true if the removal was successful | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-replace.md

# Replace

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Replace

> Application Version: 5.7

### Description

Replace all occurrences of a subname in this name
Replace all occurrences of a substring in this string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Replace,Search,Emplace,Find |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to search within | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| Old | The old name to search for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| New | The new name to replace the old name with | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting replaced name | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-replaceitems.md

# Replace Items

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ReplaceItems

> Application Version: 5.7

### Description

Replaces all names within the item array

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Tags | Replace,Find,Collection |
| Type | [FRigUnit\_CollectionReplaceItemsArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionReplaceItemsA-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The input array of items to replace | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Old | The old name to look for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| New | The new name to replace the old name with | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| RemoveInvalidItems | If True items that don't exist (after the replace operation) will be removed from the list of results | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bAllowDuplicates | If True the list may contain duplicates | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting array of items | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-reset.md

# Reset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Reset

> Application Version: 5.7

### Description

Removes all elements from an array.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayReset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayReset) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to be cleared. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-resethierarchy.md

# Reset Hierarchy

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ResetHierarchy

> Application Version: 5.7

### Description

Removes all elements from the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Delete,Erase,Clear,Empty,RemoveAll |
| Type | [FRigUnit\_HierarchyReset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyReset) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-reverse.md

# Reverse

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Reverse

> Application Version: 5.7

## Reverse (FRigVMFunction\_StringReverse)

Returns the reverse of the input string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Type | [FRigVMFunction\_StringReverse](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringReverse) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to reverse | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reverse | The resulting reversed string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

## Reverse (FRigVMDispatch\_ArrayReverse)

Reverses the order of the elements of an array.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayReverse](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayReverse) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to reverse. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-right.md

# Right

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Right

> Application Version: 5.7

### Description

Returns the right most characters of a string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | End |
| Type | [FRigVMFunction\_StringRight](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringRight) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to retrieve the right most characters of | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Count | The number of characters to retrieve | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting right most characters of the input string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-riglogic.md

# RigLogic

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RigLogic

> Application Version: 5.7

### Description

RigLogic is used to translate control input curves into bone transforms and values for blend shape and
animated map multiplier curves

### Information

|  |  |
| --- | --- |
| Module | [RigLogicModule](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigLogicModule) |
| Category | RigLogic |
| Tags | Rig,RigLogic |
| Type | [FRigUnit\_RigLogic](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigLogicModule/FRigUnit_RigLogic) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-rotatevector.md

# Rotate Vector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RotateVector

> Application Version: 5.7

### Description

Rotates a given vector by the quaternion
Rotates a given vector (direction) by the transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Rotate Vector,Transform,Multiply,Direction,TransformDirection |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The input quaternion to rotate the input vector by | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| Vector | The input vector to rotate | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting rotated vector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-rotationconstraint.md

# Rotation Constraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RotationConstraint

> Application Version: 5.7

### Description

Constrains an item's rotation to multiple items' rotations

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent,Orientation,Orient,Rotate |
| Type | [FRigUnit\_RotationConstraintLocalSpaceOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_RotationConstraintLocal-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to constrain | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bMaintainOffset | If True the offset will be computed based on the current delta between each child and parent | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | The filter to apply on the transform | [Filter Option Per Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FFilterOptionPerAxis) | (bX=True,bY=True,bZ=True) |
| Parents | The array of parents to constrain the child to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings of the constraint operation | [Rig Unit Rotation Constraint Advanced Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_RotationConstraint_Adva-) | (InterpolationType=Average,RotationOrderForFilter=XZY) |
| Weight | The weight to use when applying the resulting transform to the child | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-rotationorder.md

# Rotation Order

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RotationOrder

> Application Version: 5.7

### Description

Enum of possible rotation orders

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Type | [FRigVMFunction\_MathQuaternionRotationOrder](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionRot-_1) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RotationOrder | The constant rotation order | [Euler Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | ZYX |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-round.md

# Round

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Round

> Application Version: 5.7

## Round ()

Returns the rounded value of the given double number
Returns the rounded value of the given float number

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Round |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to round | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The rounded value of the given double number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| Int | The result as an integer | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## Round (FRigVMFunction\_MathVectorRound)

Returns the closest full number (integer) of the value for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Type | [FRigVMFunction\_MathVectorRound](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorRound) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-scale.md

# Scale

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Scale

> Application Version: 5.7

### Description

Scales a quaternion's angle
Returns the product of the the vector and the float value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Scale,Multiply,Angle,Product,\*,ByScalar,ByFloat |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| Factor | The scale factor to scale the input by | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting scaled quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-scaleconstraint.md

# Scale Constraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ScaleConstraint

> Application Version: 5.7

### Description

Constrains an item's scale to multiple items' scales

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent, Size |
| Type | [FRigUnit\_ScaleConstraintLocalSpaceOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ScaleConstraintLocalSpa-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to constrain | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bMaintainOffset | If True the offset will be computed based on the current delta between each child and parent | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | The filter to apply on the transform | [Filter Option Per Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FFilterOptionPerAxis) | (bX=True,bY=True,bZ=True) |
| Parents | The array of parents to constrain the child to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| Weight | The weight to use when applying the resulting transform to the child | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-secondstoframes.md

# Seconds to Frames

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SecondstoFrames

> Application Version: 5.7

### Description

Converts seconds to frames based on the current frame rate

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Type | [FRigVMFunction\_SecondsToFrames](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_SecondsToFrames) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Seconds | The input time as seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Frames | The resulting number of frames | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-select.md

# Select

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Select

> Application Version: 5.7

### Description

Pick from a list of values based on an integer index

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | Switch,Case |
| Type | [FRigVMDispatch\_SelectInt32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_SelectInt32) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index of the value to select | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Values | The fixed array of values to select from | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting selected value from the values array based on the index | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-sendevent.md

# Send Event

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SendEvent

> Application Version: 5.7

### Description

SendEvent is used to notify the engine / editor of a change that happend within the Control Rig.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Event,Notify,Notification |
| Type | [FRigUnit\_SendEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SendEvent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Event | The event to send to the engine | [Rig Event](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigEvent) | RequestAutoKey |
| Item | The item to send the event for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| OffsetInSeconds | The time offset to use for the send event | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bEnable | The event will be sent if this is checked | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bOnlyDuringInteraction | The event will be sent if this only during an interaction | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-sequence.md

# Sequence

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Sequence

> Application Version: 5.7

### Description

Allows for a single execution pulse to trigger a series of events in order.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Type | [FRigVMFunction\_Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_Sequence) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | The execution input | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The execution result A | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| B | The execution result B | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setanimationattribute.md

# Set Animation Attribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute

> Application Version: 5.7

### Description

Modify an animation attribute if one is found, otherwise add a new animation attribute

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Animation Attribute |
| Type | [FRigDispatch\_SetAnimAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_SetAnimAttribute) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the animation attribute | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| BoneName | The name of the bone that stores the attribute, default to root bone if set to none | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Value | The value to get / set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore),[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString),[FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),User Defined Structs,[FPoseHistoryAnimationAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PoseSearch/FPoseHistoryAnimationAttribute) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Success | Returns true if the animation attribute was successfully stored | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setanimationchannel.md

# SetAnimationChannel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannel

> Application Version: 5.7

### Description

Set Bool Channel is used to set a control's animation channel value
Set Float Channel is used to set a control's animation channel value
Set Int Channel is used to set a control's animation channel value
Set Vector2D Channel is used to set a control's animation channel value
Set Vector Channel is used to set a control's animation channel value
Set Rotator Channel is used to set a control's animation channel value
Set Transform Channel is used to set a control's animation channel value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetAnimationChannel,Set Bool Channel,Animation,Channel,Set Float Channel,Set Int Channel,Set Vector2D Channel,Set Vector Channel,Set Rotator Channel,Set Transform Channel |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The new value of the animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Control | The name of the Control to retrieve the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Channel | The name of the animation channel to retrieve the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bInitial | If set to true the initial value will be returned | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setanimationchannelfromitem.md

# SetAnimationChannelFromItem

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannelFromItem

> Application Version: 5.7

### Description

Set Bool Channel is used to set a control's animation channel value
Set Float Channel is used to set a control's animation channel value
Set Int Channel is used to set a control's animation channel value
Set Vector2D Channel is used to set a control's animation channel value
Set Vector Channel is used to set a control's animation channel value
Set Rotator Channel is used to set a control's animation channel value
Set Transform Channel is used to set a control's animation channel value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetAnimationChannelFromItem,Set Bool Channel,Animation,Channel,Set Float Channel,Set Int Channel,Set Vector2D Channel,Set Vector Channel,Set Rotator Channel,Set Transform Channel |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The new value of the animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Item | The item representing the channel | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| bInitial | If set to true the initial value will be returned | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setat.md

# Set At

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAt

> Application Version: 5.7

### Description

Sets an element of an array by index.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArraySetAtIndex](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArraySetAtIndex) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to set an element for. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index of the element to set. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Element | The new value for element to set. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setchannelhosts.md

# Set Channel Hosts

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetChannelHosts

> Application Version: 5.7

### Description

Allows an animation channel to be hosted by multiple controls

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Children,Parent,Constraint,Space,SetParent,AddParent,Channel |
| Type | [FRigUnit\_SetChannelHosts](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetChannelHosts) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Channel | The channel to receive more hosts | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Hosts | The hosts to add to the channel | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcomponent.md

# Set Component

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetComponent

> Application Version: 5.7

### Description

Set the content of a component

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_SetComponentContent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_SetComponentContent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Execute | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Key | The key of the component | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | () |
| Component | The actual component | [FRigPhysicsBodyComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsBodyComponent),[FRigPhysicsControlComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsControlComponent),[FRigPhysicsJointComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointComponent),[FRigPhysicsSolverComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSolverComponent) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Success | Returns true if the operation was successful. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontrolbool.md

# Set Control Bool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlBool

> Application Version: 5.7

### Description

SetControlBool is used to perform a change in the hierarchy by setting a single control's bool value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlBool,SetGizmoBool |
| Type | [FRigUnit\_SetControlBool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlBool) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoolValue | The bool value to get / set for the given Control. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the bool for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontrolcolor.md

# Set Control Color

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlColor

> Application Version: 5.7

### Description

SetControlColor is used to change the control's color

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlColor,SetGizmoColor |
| Type | [FRigUnit\_SetControlColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlColor) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the color for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Color | The color to set for the control | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontrolfloat.md

# Set Control Float

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlFloat

> Application Version: 5.7

### Description

SetControlFloat is used to perform a change in the hierarchy by setting a single control's float value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlFloat,SetGizmoFloat |
| Type | [FRigUnit\_SetControlFloat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlFloat) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatValue | The float value to get / set for the given Control. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontroloffset.md

# SetControlOffset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlOffset

> Application Version: 5.7

### Description

SetControlOffset is used to perform a change in the hierarchy by setting a single control's transform.
This is typically only used during the Construction Event.
SetControlTranslationOffset is used to perform a change in the hierarchy by setting a single control's translation offset.
This is typically only used during the Construction Event.
SetControlRotationOffset is used to perform a change in the hierarchy by setting a single control's rotation offset.
This is typically only used during the Construction Event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlOffset,Set Control Offset,Initial,InitialTransform,SetInitialTransform,SetInitialControlTransform,Set Control Translation Offset,SetControlTranslationOffset,SetInitialTranslation,SetInitialLocation,Set Control Rotation Offset,SetControlRotationOffset,SetInitialRotation |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Offset | The offset transform to set on the control | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the control's transform should be set in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontrolrotator.md

# Set Control Rotator

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlRotator

> Application Version: 5.7

### Description

SetControlRotator is used to perform a change in the hierarchy by setting a single control's Rotator value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlRotator,SetGizmoRotator |
| Type | [FRigUnit\_SetControlRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlRotator) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Rotator | The vector value to get / set for the given Control. | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Pitch=0.000000,Yaw=0.000000,Roll=0.000000) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Space | Defines if the bone's transform should be set in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontrolscaleoffset.md

# Set Control Scale Offset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlScaleOffset

> Application Version: 5.7

### Description

SetControlScaleOffset is used to perform a change in the hierarchy by setting a single control's scale offset.
This is typically only used during the Construction Event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlOffset,Initial,InitialTransform,SetInitialTransform,SetInitialControlTransform,SetControlScaleOffset,SetInitialScale,SetInitialScale |
| Type | [FRigUnit\_SetControlScaleOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlScaleOffset) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Scale | The new scale offset to set on the control | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the control's transform should be set in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontrolvector.md

# Set Control Vector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector

> Application Version: 5.7

### Description

SetControlVector is used to perform a change in the hierarchy by setting a single control's Vector value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlVector,SetGizmoVector |
| Type | [FRigUnit\_SetControlVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlVector) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector | The vector value to get / set for the given Control. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Space | Defines if the bone's transform should be set in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontrolvector2d.md

# Set Control Vector2D

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector2D

> Application Version: 5.7

### Description

SetControlVector2D is used to perform a change in the hierarchy by setting a single control's Vector2D value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlVector2D,SetGizmoVector2D |
| Type | [FRigUnit\_SetControlVector2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlVector2D) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector | The 2d vector value to get / set for the given Control. | [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcontrolvisibility.md

# Set Control Visibility

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVisibility

> Application Version: 5.7

### Description

SetControlVisibility is used to change the visibility on a control at runtime

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlVisibility,Visibility,Hide,Show,Hidden,Visible,SetGizmoVisibility |
| Type | [FRigUnit\_SetControlVisibility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlVisibility) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The name of the Control to set the visibility for. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Pattern | If the ControlName is set to None this can be used to look for a series of Controls | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| bVisible | The visibility to set for the control | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setcurvevalue.md

# Set Curve Value

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetCurveValue

> Application Version: 5.7

### Description

SetCurveValue is used to perform a change in the curve container by setting a single Curve value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Curve |
| Tags | SetCurveValue |
| Type | [FRigUnit\_SetCurveValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetCurveValue) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Curve | The name of the Curve to set the Value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Value | The value to set for the given Curve. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setdefaultmatch.md

# Set Default Match

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetDefaultMatch

> Application Version: 5.7

### Description

Set default match during a connector event

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | Connection,Resolve,Match,Default |
| Type | [FRigUnit\_SetDefaultMatch](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetDefaultMatch) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Default | The items being interacted on | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setdefaultparent.md

# Set Default Parent

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetDefaultParent

> Application Version: 5.7

### Description

Changes the default parent for an item - this removes all other current parents.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Children,Parent,Constraint,Space,SetParent,AddParent |
| Type | [FRigUnit\_SetDefaultParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetDefaultParent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to be parented under the new default parent | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Parent | The default parent to be used for the child | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setdrivencontrols.md

# Set Driven Controls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetDrivenControls

> Application Version: 5.7

### Description

SetControlDrivenList is used to change the list of affected controls of an indirect control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlDrivenList,Interaction,Indirect |
| Type | [FRigUnit\_SetControlDrivenList](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlDrivenList) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the list for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Driven | The list of affected controls | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setlength.md

# SetLength

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetLength

> Application Version: 5.7

### Description

Sets the length of a given vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Unit,Normalize,Scale |
| Type | [FRigVMFunction\_MathVectorSetLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorSetLeng-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input vector to set the length of | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| Length | The desired length of the vector | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting scaled input vector \* (or 0,0,0 in case the input was also 0,0,0) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setmetadata.md

# Set Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMetadata

> Application Version: 5.7

### Description

Sets some metadata for the provided item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_SetMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_SetMetadata) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item storing the metadata | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the metadata | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |
| Value | The value to get / set | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Success | Returns true if the metadata was successfully stored | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setmodulemetadata.md

# Set Module Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetModuleMetadata

> Application Version: 5.7

### Description

Sets metadata on the module

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_SetModuleMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_SetModuleMetadata) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the metadata | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |
| Value | The value to get / set | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Success | Returns true if the metadata was successfully stored | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setmulticontrolvalue.md

# SetMultiControlValue

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultiControlValue

> Application Version: 5.7

### Description

SetMultiControlFloat is used to perform a change in the hierarchy by setting multiple controls' float value.
SetMultiControlInteger is used to perform a change in the hierarchy by setting multiple controls' integer value.
SetMultiControlVector2D is used to perform a change in the hierarchy by setting multiple controls' vector2D value.
SetMultiControlRotator is used to perform a change in the hierarchy by setting multiple controls' rotator value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetMultiControlValue,Set Multiple Controls Float,SetMultipleControlsFloat,SetControlFloat,SetGizmoFloat,Set Multiple Controls Integer,SetMultipleControlsInteger,SetControlInteger,SetGizmoInteger,Set Multiple Controls Vector2D,SetMultipleControlsVector2D,SetControlVector2D,SetGizmoVector2D,Set Multiple Controls Rotator,SetMultipleControlsRotator,SetControlRotator,SetGizmoRotator |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Entries | The array of control-float pairs to be processed | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlFloat\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlFloat_En-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlInteger\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlInteger_-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlVector2D\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlVector2D-)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlRotator\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlRotator_-)> | (()) |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setmultiplecontrolsbool.md

# Set Multiple Controls Bool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultipleControlsBool

> Application Version: 5.7

### Description

SetMultiControlBool is used to perform a change in the hierarchy by setting multiple controls' bool value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetMultipleControlsBool,SetControlBool,SetGizmoBool |
| Type | [FRigUnit\_SetMultiControlBool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlBool) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Entries | The array of control-Bool pairs to be processed | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlBool\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlBool_Ent-)> | (()) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setnum.md

# Set Num

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetNum

> Application Version: 5.7

### Description

Sets the numbers of elements of an array.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArraySetNum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArraySetNum) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to set the size for. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Num | The new size of the array. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setparentweights.md

# Set Parent Weights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetParentWeights

> Application Version: 5.7

### Description

Sets the item's parents' weights

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Chain,Parents,Hierarchy |
| Type | [FRigUnit\_HierarchySetParentWeights](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchySetParentWeigh-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to set the parents' weights for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Weights | The weights to set for the child's parents. \* The number of weights needs to match the current number of parents. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementWeight](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementWeight)> | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodycollisionmode.md

# Set Physics Body Collision Mode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyCollisionMode

> Application Version: 5.7

### Description

Sets what collision mode is used for this body

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyCollisionType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| CollisionType | What type of collision to use for the Physics Body | [Collision Enabled](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/ECollisionEnabled__Type) | QueryAndPhysics |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodycollisionproperties.md

# Set Physics Body Collision Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyCollisionProperties

> Application Version: 5.7

### Description

Sets the collision for a physics component body

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetCollision](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetCollision) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| Collision | Specifies the collision associated with the Physics Body | [Rig Physics Collision](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsCollision) | (Boxes=,Spheres=,Capsules=,Material=(Friction=1.000000,Restitution=0.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply)) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodydamping.md

# Set Physics Body Damping

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyDamping

> Application Version: 5.7

### Description

Sets the linear and angular damping on the body. This will reduce the velocity, to make the
body start tracking the simulation space.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyDamping](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_1) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| LinearDamping | The desired linear damping | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AngularDamping | The desired angular damping | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodydata.md

# Set Physics Body Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyData

> Application Version: 5.7

### Description

Sets all the data on a body - but in a sparse way so you can decide which parameters get applied.
Note that the sparse data does not get displayed correctly (the flags that enable/disable all end up getting
reset if the user attempts to change them) so this should be used with caution until this is fixed.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodySparseData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_8) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| Data | Sparse data to be set on the Physics Body | [Physics Control Modifier Sparse Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlModifierSparseDat-) | (MovementType=Simulated,CollisionType=QueryAndPhysics,GravityMultiplier=1.000000,PhysicsBlendWeight=1.000000,KinematicTargetSpace=OffsetInBoneSpace,bUpdateKinematicFromSimulation=True,bEnableMovementType=True,bEnableCollisionType=True,bEnableGravityMultiplier=True,bEnablePhysicsBlendWeight=True,bEnableKinematicTargetSpace=True,bEnablebUpdateKinematicFromSimulation=True) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodydynamicsproperties.md

# Set Physics Body Dynamics Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyDynamicsProperties

> Application Version: 5.7

### Description

Sets the mass etc for a physics component body

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetDynamics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetDynamics) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| Dynamics | Sets the properties describing the dynamics properties of the Physics Body | [Rig Physics Dynamics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDynamics) | (Density=1.000000,MassOverride=1.000000,bOverrideCentreOfMass=False,CentreOfMassOverride=(X=0.000000,Y=0.000000,Z=0.000000),CentreOfMassNudge=(X=0.000000,Y=0.000000,Z=0.000000),bOverrideMomentsOfInertia=False,MomentsOfInertiaOverride=(X=1.000000,Y=1.000000,Z=1.000000),LinearDamping=0.000000,AngularDamping=0.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodygravitymultiplier.md

# Set Physics Body Gravity Multiplier

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyGravityMultiplier

> Application Version: 5.7

### Description

Sets the multiplier on gravity that should be applied to the body.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyGravityMultiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_2) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| GravityMultiplier | How much the Physics Body should respond to the gravity set in the Physics Solver | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodyincludeinchecksforreset.md

# Set Physics Body Include In Checks For Reset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyIncludeInChecksForReset

> Application Version: 5.7

### Description

Sets whether this body should be included in checks for resetting physics on the whole rig

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyIncludeInChecksForReset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_Hierarc-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| bInclude | WHether the Physics Body should be included when checking to see if the simulation should be reset. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodykinematictarget.md

# Set Physics Body Kinematic Target

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyKinematicTarget

> Application Version: 5.7

### Description

Sets the kinematic target for a body - note that this won't actually make the body kinematic

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyKinematicTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_3) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| KinematicTarget | Kinematic target for the Physics Body. This will be combined with the animation pose, depending on the Kinematic Target Space. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodymaterial.md

# Set Physics Body Material

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMaterial

> Application Version: 5.7

### Description

Applies the material settings to all the collision shapes

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyMaterial](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_4) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| Material | The physics material to be used for collision on the Physics Body | [Rig Physics Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsMaterial) | (Friction=1.000000,Restitution=0.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodymovementmode.md

# Set Physics Body Movement Mode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMovementMode

> Application Version: 5.7

### Description

Sets the movement mode for this body.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyMovementType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_5) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| MovementType | How the Physics Body should move when the Physics Solver is stepped. | [Physics Movement Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/EPhysicsMovementType) | Simulated |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodyphysicsblendweight.md

# Set Physics Body Physics Blend Weight

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyPhysicsBlendWeight

> Application Version: 5.7

### Description

Controls the amount that the simulation is blended back into the target bones.
Note that this feature is not yet fully implemented.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyPhysicsBlendWeight](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_6) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| PhysicsBlendWeight | A per-body "alpha" on how much of the physics movement to apply to the target bone. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodysourcebone.md

# Set Physics Body Source Bone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodySourceBone

> Application Version: 5.7

### Description

Sets what bone is used as a source transform for the physics body. This is used as a kinematic target, and when
initializing the simulation.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodySourceBone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_7) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| SourceBone | The bone to use as a source transform (kinematic target, and initialization) for the Physics Body. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodytargetbone.md

# Set Physics Body Target Bone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyTargetBone

> Application Version: 5.7

### Description

Sets what bone is targeted by the simulation - i.e. where the simulation output is written to.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyTargetBone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_9) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| TargetBone | The bone to use as a target for the Physics Body - i.e. where its transforms should be written to. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsbodyupdatekinematicfromsimulation.md

# Set Physics Body Update Kinematic From Simulation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyUpdateKinematicFromSimulation

> Application Version: 5.7

### Description

If true, then kinematic objects will be written back from simulation to the bones. This only
necessary when either kinematic targets are being used, or when the target bone differs from the source bone.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyUpdateKinematicFromSimulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_Hierarc-_2) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| bUpdateKinematicFromSimulation | When bodies are written back from simulation, if this is set to false, there is a small performance benefit to skipping bodies that are known to be kinematic, and when they are set to just track the input animation. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontrolangulardampingratio.md

# Set Physics Control Angular Damping Ratio

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlAngularDampingRatio

> Application Version: 5.7

### Description

Sets the Angular Damping Ratio of a Physics Control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlAngularDampingRatio](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlAngu-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| DampingRatio | The angular damping ratio for the control. When this is 1, there is just enough damping to stop the control from oscillating about its target, due to the control strength (in the absence of any other influences). Values above this will add more damping, and values below will make the system tend to oscillate, as it will be under-ramped. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontrolangularstrength.md

# Set Physics Control Angular Strength

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlAngularStrength

> Application Version: 5.7

### Description

Sets the Angular Strength of a Physics Control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlAngularStrength](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlAngu-_1) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| Strength | The angular strength of the control. In the absence of any other influences, this is the frequency of oscillation when there is zero damping. For example, a strength of 2 would make the target oscillate twice per second (when there is no damping). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontrolcustomcontrolpoint.md

# Set Physics Control Custom Control Point

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlCustomControlPoint

> Application Version: 5.7

### Description

Sets the custom control point on a control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlCustomControlPoint](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlCust-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| CustomControlPoint | The position of the control point relative to the child mesh, when using a custom control point. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bUseCustomControlPoint | Whether or not to use the custom control point position | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontroldata.md

# Set Physics Control Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlData

> Application Version: 5.7

### Description

Sets the control data for a physics control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlData) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| ControlData | The data (strengths etc) that should be set on the Physics Control | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontroldataandmultiplier.md

# Set Physics Control Data And Multiplier

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlDataAndMultiplier

> Application Version: 5.7

### Description

Sets the control data and multiplier for a physics control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlDataAndMultiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlData-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| ControlData | The control data (strengths etc) to use | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |
| ControlMultiplier | Detail/per-direction multipliers on the control data | [Physics Control Multiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlMultiplier) | (LinearStrengthMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),LinearDampingRatioMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),LinearExtraDampingMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),MaxForceMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),AngularStrengthMultiplier=1.000000,AngularDampingRatioMultiplier=1.000000,AngularExtraDampingMultiplier=1.000000,MaxTorqueMultiplier=1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontrolenabled.md

# Set Physics Control Enabled

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlEnabled

> Application Version: 5.7

### Description

Sets whether a control is enabled

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlEnabled](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlEnab-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control that should be enabled or disabled | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| bEnabled | Whether or not the Physics Control should be enabled | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontrollineardampingratio.md

# Set Physics Control Linear Damping Ratio

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlLinearDampingRatio

> Application Version: 5.7

### Description

Sets the Linear Damping Ratio of a Physics Control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlLinearDampingRatio](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlLine-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| DampingRatio | The linear damping ratio for the control. When this is 1, there is just enough damping to stop the control from oscillating about its target, due to the control strength (in the absence of any other influences). Values above this will add more damping, and values below will make the system tend to oscillate, as it will be under-ramped. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontrollinearstrength.md

# Set Physics Control Linear Strength

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlLinearStrength

> Application Version: 5.7

### Description

Sets the Linear Strength of a Physics Control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlLinearStrength](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlLine-_1) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| Strength | The linear strength of the control. In the absence of any other influences, this is the frequency of oscillation when there is zero damping. For example, a strength of 2 would make the target oscillate twice per second (when there is no damping). Note that parent-space controls should this set to zero when they are controlling two bodies that are connected with a physics joint. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontrolmultiplier.md

# Set Physics Control Multiplier

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlMultiplier

> Application Version: 5.7

### Description

Sets the multipliers for a physics control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlMultiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlMult-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| ControlMultiplier | The multipliers to use on the control. These allow fine-grained control over the strengths (etc) in different directions. | [Physics Control Multiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlMultiplier) | (LinearStrengthMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),LinearDampingRatioMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),LinearExtraDampingMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),MaxForceMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),AngularStrengthMultiplier=1.000000,AngularDampingRatioMultiplier=1.000000,AngularExtraDampingMultiplier=1.000000,MaxTorqueMultiplier=1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicscontroltarget.md

# Set Physics Control Target

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlTarget

> Application Version: 5.7

### Description

Sets the target for a physics control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetControlTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetControlTarg-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| ControlTarget | The target transform (etc) for the control | [Physics Control Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlTarget) | (TargetPosition=(X=0.000000,Y=0.000000,Z=0.000000),TargetVelocity=(X=0.000000,Y=0.000000,Z=0.000000),TargetOrientation=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000),TargetAngularVelocity=(X=0.000000,Y=0.000000,Z=0.000000),bApplyControlPointToTarget=False) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsjointdriveproperties.md

# Set Physics Joint Drive Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointDriveProperties

> Application Version: 5.7

### Description

Sets the joint drive for a physics component body

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetJointDriveData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetJointDriveD-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsJoint") |
| DriveData | The Physics Joint drive data that should be used | [Rig Physics Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) | (LinearDriveConstraint=(PositionTarget=(X=0.000000,Y=0.000000,Z=0.000000),VelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),XDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),YDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),ZDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),bAccelerationMode=True),AngularDriveConstraint=(TwistDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SwingDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SlerpDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),OrientationTarget=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000),AngularVelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),AngularDriveMode=SLERP,bAccelerationMode=True),bUseSkeletalAnimation=True,SkeletalAnimationVelocityMultiplier=1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsjointdriveuseskeletalanimation.md

# Set Physics Joint Drive Use Skeletal Animation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointDriveUseSkeletalAnimation

> Application Version: 5.7

### Description

Sets the joint drive for a physics component body

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetJointDriveUseSkeletalAnimation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetJointDriveU-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsJoint") |
| bUseSkeletalAnimation | Whether the drive targets should be relative to the incoming animation pose. If set to true (and the drive targets are zero), then the drives will track the target animation. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsjointenabled.md

# Set Physics Joint Enabled

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointEnabled

> Application Version: 5.7

### Description

Specifies whether a Physics Joint should be enabled or not

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetJointEnabled](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetJointEnable-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsJoint") |
| bEnabled | Whether or not the joint should be enabled. Disabling the joint will disable any limits and drives | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicsjointproperties.md

# Set Physics Joint Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointProperties

> Application Version: 5.7

### Description

Sets the joint data for a physics joint component

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetJointData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetJointData) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsJoint") |
| JointData | The physics joint data (limit and drive properties) to be used | [Rig Physics Joint Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) | (bEnabled=True,bAutoCalculateParentOffset=True,ExtraParentOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),bAutoCalculateChildOffset=True,ExtraChildOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),LinearConstraint=(Limit=0.000000,XMotion=LCM\_Locked,YMotion=LCM\_Locked,ZMotion=LCM\_Locked,Stiffness=0.000000,Damping=0.000000,Restitution=0.000000,ContactDistance=5.000000,bSoftConstraint=False),ConeConstraint=(Swing1LimitDegrees=45.000000,Swing2LimitDegrees=45.000000,Swing1Motion=ACM\_Free,Swing2Motion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),TwistConstraint=(TwistLimitDegrees=45.000000,TwistMotion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),bDisableCollision=True,LinearProjectionAmount=0.500000,AngularProjectionAmount=0.000000,ParentInverseMassScale=1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicssolverexternalvelocity.md

# Set Physics Solver External Velocity

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsSolverExternalVelocity

> Application Version: 5.7

### Description

Sets the external velocity of the simulation - used for adding wind effects

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_SetPhysicsSolverExternalVelocity](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_SetPhysicsSolverExterna-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The physics solver | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| ExternalLinearVelocity | Additional velocity that is added to the component velocity so the simulation acts as if the actor is moving at speed, even when stationary. The vector is in world space. This could be used for wind effects etc. Typical values are similar to the velocity of the object or effect, and usually around or less than 1000 for characters/wind. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ExternalAngularVelocity | Additional angular velocity that is added to the component angular velocity. This can be used to make the simulation act as if the actor is rotating even when it is not. E.g., to apply physics to a character on a podium as the camera rotates around it, to emulate the podium itself rotating. Vector is in world space. Units are deg/s. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ExternalTurbulenceVelocity | This will treat the external velocity like a wind field and add turbulence to it. Units are the same as velocity, so this is the approximate magnitude of the turbulence. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setphysicssolversimulationspacesettings.md

# Set Physics Solver Simulation Space Settings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsSolverSimulationSpaceSettings

> Application Version: 5.7

### Description

Sets the solver's simulation space settings

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_SetPhysicsSolverSimulationSpaceSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_SetPhysicsSolverSimulat-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The physics solver | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| SimulationSpaceSettings | The new simulation space settings | [Rig Physics Simulation Space Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSimulationSpaceSettin-) | (SpaceMovementAmount=1.000000,VelocityScaleZ=1.000000,bClampLinearVelocity=False,MaxLinearVelocity=10000.000000,bClampAngularVelocity=False,MaxAngularVelocity=10000.000000,bClampLinearAcceleration=False,MaxLinearAcceleration=10000.000000,bClampAngularAcceleration=False,MaxAngularAcceleration=10000.000000,LinearAccelerationThresholdForTeleport=100000.000000,AngularAccelerationThresholdForTeleport=100000.000000,PositionChangeThresholdForTeleport=100.000000,OrientationChangeThresholdForTeleport=30.000000,LinearDragMultiplier=1.000000,AngularDragMultiplier=1.000000,ExternalLinearDrag=(X=0.000000,Y=0.000000,Z=0.000000),ExternalLinearVelocity=(X=0.000000,Y=0.000000,Z=0.000000),ExternalAngularVelocity=(X=0.000000,Y=0.000000,Z=0.000000),ExternalTurbulenceVelocity=(X=0.000000,Y=0.000000,Z=0.000000)) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setrelativetransform.md

# Set Relative Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetRelativeTransform

> Application Version: 5.7

### Description

SetRelativeTransform is used to set a single transform from a hierarchy in the space of another item
SetRelativeTranslation is used to set a single translation from a hierarchy in the space of another item
SetRelativeRotation is used to set a single rotation from a hierarchy in the space of another item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | Set Relative Transform,Offset,Local,Set Relative Translation,Set Relative Rotation |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child item to set the transform for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Parent | The parent item to use. The child transform will be set in the space of the parent. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bParentInitial | Defines if the parent's transform should be determined as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Value | The transform of the child item relative to the provided parent | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Weight | Defines how much the change will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true children of affected items in the hierarchy will follow the transform change - otherwise only the parent will move. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setscale.md

# Set Scale

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetScale

> Application Version: 5.7

### Description

SetScale is used to set a single scale on hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | SetBoneScale,SetControlScale,SetInitialScale,SetSpaceScale,SetScale |
| Type | [FRigUnit\_SetScale](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetScale) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to set the scale for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Space | Defines if the scale should be set in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| bInitial | Defines if the transform should be set as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Scale | The new scale of the given item | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Weight | Defines how much the change will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true children of affected items in the hierarchy will follow the transform change - otherwise only the parent will move. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

