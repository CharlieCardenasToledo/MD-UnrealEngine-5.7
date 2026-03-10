# Unidad 16

Rango: archivos 1801 a 1920 de 3470

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setshapelibraryfromuserdata.md

# Set Shape Library from User Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeLibraryfromUserData

> Application Version: 5.7

### Description

Allows to set / add a shape library on the running control rig from user data

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Tags | Shape,Gizmo,Library |
| Type | [FRigUnit\_SetupShapeLibraryFromUserData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetupShapeLibraryFromUs-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NameSpace | The name space of the user data to look the shape library up within | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Path | The path within the user data for the shape library | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| LibraryName | Optionally provide the namespace of the shape library to use.  *This is only useful if you have multiple shape libraries and you*  want to override a specific one. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| LogShapeLibraries | If this is checked we'll output the resulting shape libraries to the log for debugging. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setshapesettings.md

# Set Shape Settings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeSettings

> Application Version: 5.7

### Description

Changes the shape settings of a control
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,Control |
| Type | [FRigUnit\_HierarchySetShapeSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchySetShapeSettin-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to change | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Settings | The shape settings for the control | [Rig Unit Hierarchy Add Control Shape Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControl_Sha-) | (bVisible=True,Name="Default",Color=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),Transform=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setshapetransform.md

# Set Shape Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeTransform

> Application Version: 5.7

### Description

SetShapeTransform is used to perform a change in the hierarchy by setting a single control's shape transform.
This is typically only used during the Construction Event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlShapeTransform,Gizmo,GizmoTransform,MeshTransform |
| Type | [FRigUnit\_SetShapeTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetShapeTransform) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Transform | The shape transform to set for the control | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setsplinepoints.md

# Set Spline Points

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetSplinePoints

> Application Version: 5.7

### Description

Set the points of a spline, given a spline and an array of positions

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_SetSplinePoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_SetSplinePoints) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to be updated | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | The points to set on the spline. The assumption is that the number of points provided matches the points on the spline. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-setsplinetransforms.md

# Set Spline Transforms

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetSplineTransforms

> Application Version: 5.7

### Description

Set the points of a spline, given a spline and an array of transforms

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_SetSplineTransforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_SetSplineTransforms) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to be updated | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | The transforms interpreted as positions to set on the spline. The assumption is that the number of transforms provided matches the points on the spline. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-settransform.md

# Set Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetTransform

> Application Version: 5.7

### Description

SetTransform is used to set a single transform on hierarchy.

Note: For Controls when setting the initial transform this node
actually sets the Control's offset transform and resets the local
values to (0, 0, 0).
SetTranslation is used to set a single translation on hierarchy.
SetRotation is used to set a single rotation on hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | Set Transform,SetBoneTransform,SetControlTransform,SetInitialTransform,SetSpaceTransform,Set Translation,SetBoneTranslation,SetControlTranslation,SetInitialTranslation,SetSpaceTranslation,SetBoneLocation,SetControlLocation,SetInitialLocation,SetSpaceLocation,SetBonePosition,SetControlPosition,SetInitialPosition,SetSpacePosition,SetTranslation,SetLocation,SetPosition,Set Rotation,SetBoneRotation,SetControlRotation,SetInitialRotation,SetSpaceRotation,SetBoneOrientation,SetControlOrientation,SetInitialOrientation,SetSpaceOrientation,SetRotation,SetOrientation |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to set the transform for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Space | Defines if the transform should be set in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| bInitial | Defines if the transform should be set as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Value | The new transform of the given item | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Weight | Defines how much the change will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true children of affected items in the hierarchy will follow the transform change - otherwise only the parent will move. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-settransformarray.md

# Set Transform Array

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetTransformArray

> Application Version: 5.7

### Description

SetTransformArray is used to set an array of transforms on the hierarchy.

Note: For Controls when setting the initial transform this node
actually sets the Control's offset transform and resets the local
values to (0, 0, 0).

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | SetBoneTransform,SetControlTransform,SetInitialTransform,SetSpaceTransform |
| Type | [FRigUnit\_SetTransformItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetTransformItemArray) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The item to set the transform for | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Space | Defines if the transform should be set in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| bInitial | Defines if the transform should be set as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Transforms | The new transform of the given item | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| Weight | Defines how much the change will be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true children of affected items in the hierarchy will follow the transform change - otherwise only the parent will move. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-shapeexists.md

# Shape Exists

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ShapeExists

> Application Version: 5.7

### Description

Checks whether or not a shape is available in the rig's shape libraries

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Tags | Shape,Gizmo,Library,Exists,Contains |
| Type | [FRigUnit\_ShapeExists](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ShapeExists) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ShapeName | The name of the shape to search for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the shape name exists in any of the shape libraries | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-shiftbox.md

# Shift Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ShiftBox

> Application Version: 5.7

### Description

Move the box by a certain amount

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,Translate,Move,BoundingBox |
| Type | [FRigVMFunction\_MathBoxShift](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxShift) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | the box to move | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Amount | the amount / vector to shift the box by | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting moved box | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-sign.md

# Sign

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Sign

> Application Version: 5.7

### Description

Returns the sign of the value (+1 for >= 0.0, -1 for < 0.0)
Returns the sign of the value (+1 for >= 0.f, -1 for < 0.f)
Returns the sign of the value (+1 for >= 0, -1 for < 0)
Returns the sign of the value (+1 for >= FVector(0.f, 0.f, 0.f), -1 for < 0.f) for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Sign |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-sin.md

# Sin

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Sin

> Application Version: 5.7

### Description

Returns the sinus value of the given value (in radians)

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Sin |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-slidechain.md

# Slide Chain

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SlideChain

> Application Version: 5.7

### Description

Slides an existing chain along itself with control over extrapolation.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Fit,Refit |
| Type | [FRigUnit\_SlideChainItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SlideChainItemArray) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to slide | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| SlideAmount | The amount of sliding. This unit is multiple of the chain length. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnanimationchannel.md

# SpawnAnimationChannel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnAnimationChannel

> Application Version: 5.7

### Description

Adds a new animation channel to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | SpawnAnimationChannel,Spawn Bool Animation Channel,Construction,Create,New,AddAnimationChannel,NewAnimationChannel,CreateAnimationChannel,AddChannel,NewChannel,CreateChannel,SpawnChannel,Spawn Float Animation Channel,Spawn Vector2D Animation Channel,Spawn Vector Animation Channel,Spawn Rotator Animation Channel |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InitialValue | The initial value of the new animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MinimumValue | The minimum value of the new animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaximumValue | The maximum value for the animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| LimitsEnabled | The enable settings for the limits | [Rig Unit Hierarchy Add Animation Channel Empty Limit Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_2)   [Rig Unit Hierarchy Add Animation Channel Single Limit Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_9)   [FRigUnit\_HierarchyAddAnimationChannel2DLimitSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-)   [FRigUnit\_HierarchyAddAnimationChannelVectorLimitSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_12)   [FRigUnit\_HierarchyAddAnimationChannelRotatorLimitSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_6) | () |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewChannel |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnbone.md

# Spawn Bone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnBone

> Application Version: 5.7

### Description

Adds a new bone to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,Joint,Skeleton |
| Type | [FRigUnit\_HierarchyAddBone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddBone) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The initial transform of the new element | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Space | Defines if the transform should be interpreted in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewBone |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawncomponent.md

# Spawn Component

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnComponent

> Application Version: 5.7

### Description

Adds a component under an element in the hierarchy

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_SpawnComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_SpawnComponent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Execute | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item for this component | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the component (can be empty) | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Component | The actual component | [FRigPhysicsBodyComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsBodyComponent),[FRigPhysicsControlComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsControlComponent),[FRigPhysicsJointComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointComponent),[FRigPhysicsSolverComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSolverComponent) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Key | The key of the component | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |
| Success | Returns true if the operation was successful. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawncontrol.md

# SpawnControl

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnControl

> Application Version: 5.7

### Description

Adds a new control to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | SpawnControl,Spawn Float Control,Construction,Create,New,AddControl,NewControl,CreateControl,Spawn Integer Control,Spawn Vector2D Control,Spawn Vector Control,Spawn Rotator Control,Rotation,Spawn Transform Control |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InitialValue | The initial value of the new control | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Settings | The settings for the control | [Rig Unit Hierarchy Add Control Float Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlFloa-_2)   [FRigUnit\_HierarchyAddControlInteger\_Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlInte-_2)   [FRigUnit\_HierarchyAddControlVector2D\_Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlVect-_3)   [FRigUnit\_HierarchyAddControlVector\_Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlVect-_5)   [FRigUnit\_HierarchyAddControlRotator\_Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlRota-_2)   [FRigUnit\_HierarchyAddControlTransform\_Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlTran-_2) | (PrimaryAxis=X,bIsScale=False,Limits=(Limit=(bMinimum=True,bMaximum=True),MinValue=0.000000,MaxValue=100.000000,bDrawLimits=True),Shape=(bVisible=True,Name="Default",Color=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),Transform=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))),Proxy=(bIsProxy=False,DrivenControls=,ShapeVisibility=BasedOnSelection),DisplayName="",bSelectable=True) |
| OffsetTransform | The offset transform of the new control | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| OffsetSpace | The space the offset is in | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewControl |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnintegeranimationchannel.md

# Spawn Integer Animation Channel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel

> Application Version: 5.7

### Description

Adds a new animation channel to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,AddAnimationChannel,NewAnimationChannel,CreateAnimationChannel,AddChannel,NewChannel,CreateChannel,SpawnChannel |
| Type | [FRigUnit\_HierarchyAddAnimationChannelInteger](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_4) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InitialValue | The initial value of the new animation channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MinimumValue | The minimum value of the new animation channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MaximumValue | The maximum value for the animation channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| LimitsEnabled | The enable settings for the limits | [Rig Unit Hierarchy Add Animation Channel Single Limit Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_9) | (Enabled=(bMinimum=True,bMaximum=True)) |
| ControlEnum | The enum to use to find valid values | Enum | None |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewChannel |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnnull.md

# Spawn Null

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnNull

> Application Version: 5.7

### Description

Adds a new null to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,Locator,Group |
| Type | [FRigUnit\_HierarchyAddNull](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddNull) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The initial transform of the new element | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Space | Defines if the transform should be interpreted in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewNull |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnphysicsbody.md

# Spawn Physics Body

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody

> Application Version: 5.7

### Description

Adds a new physics body as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_AddPhysicsBody](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsBody) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Solver | The solver to relate this new physics body should be added to | [Rig Physics Body Solver Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsBodySolverSettings) | (PhysicsSolverComponentKey=(ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver"),bUseAutomaticSolver=True,SourceBone=(Type=None,Name=""),TargetBone=(Type=None,Name=""),bIncludeInChecksForReset=True) |
| Dynamics | The dynamics properties of the new physics element | [Rig Physics Dynamics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDynamics) | (Density=1.000000,MassOverride=1.000000,bOverrideCentreOfMass=False,CentreOfMassOverride=(X=0.000000,Y=0.000000,Z=0.000000),CentreOfMassNudge=(X=0.000000,Y=0.000000,Z=0.000000),bOverrideMomentsOfInertia=False,MomentsOfInertiaOverride=(X=1.000000,Y=1.000000,Z=1.000000),LinearDamping=0.000000,AngularDamping=0.000000) |
| Collision | The collision properties of the new physics element | [Rig Physics Collision](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsCollision) | (Boxes=,Spheres=,Capsules=,Material=(Friction=1.000000,Restitution=0.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply)) |
| BodyData | The runtime modifiable data | [Physics Control Modifier Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlModifierData) | (MovementType=Simulated,CollisionType=QueryAndPhysics,KinematicTargetSpace=OffsetInBoneSpace,GravityMultiplier=1.000000,PhysicsBlendWeight=1.000000,bUpdateKinematicFromSimulation=True) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body component key that was created | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnphysicscomponents.md

# Spawn Physics Components

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsComponents

> Application Version: 5.7

### Description

Adds a set of physics components including the body, joint and controls

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Body,Joint,Control |
| Type | [FRigUnit\_AddPhysicsComponents](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsComponents) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bAddJoint | Whether to add a Physics Joint | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bAddSimSpaceControl | Whether to add a simulation-space Physics Control | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bAddParentSpaceControl | Whether to add a parent-space Physics Control | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Solver | The solver to relate this new physics element to | [Rig Physics Body Solver Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsBodySolverSettings) | (PhysicsSolverComponentKey=(ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver"),bUseAutomaticSolver=True,SourceBone=(Type=None,Name=""),TargetBone=(Type=None,Name=""),bIncludeInChecksForReset=True) |
| Dynamics | The dynamics properties of the new physics body | [Rig Physics Dynamics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDynamics) | (Density=1.000000,MassOverride=1.000000,bOverrideCentreOfMass=False,CentreOfMassOverride=(X=0.000000,Y=0.000000,Z=0.000000),CentreOfMassNudge=(X=0.000000,Y=0.000000,Z=0.000000),bOverrideMomentsOfInertia=False,MomentsOfInertiaOverride=(X=1.000000,Y=1.000000,Z=1.000000),LinearDamping=0.000000,AngularDamping=0.000000) |
| Collision | The collision properties of the new physics body | [Rig Physics Collision](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsCollision) | (Boxes=,Spheres=,Capsules=,Material=(Friction=1.000000,Restitution=0.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply)) |
| BodyData | The runtime modifiable data of the new physics body | [Physics Control Modifier Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlModifierData) | (MovementType=Simulated,CollisionType=QueryAndPhysics,KinematicTargetSpace=OffsetInBoneSpace,GravityMultiplier=1.000000,PhysicsBlendWeight=1.000000,bUpdateKinematicFromSimulation=True) |
| JointData | The properties of the joint | [Rig Physics Joint Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) | (bEnabled=True,bAutoCalculateParentOffset=True,ExtraParentOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),bAutoCalculateChildOffset=True,ExtraChildOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),LinearConstraint=(Limit=0.000000,XMotion=LCM\_Locked,YMotion=LCM\_Locked,ZMotion=LCM\_Locked,Stiffness=0.000000,Damping=0.000000,Restitution=0.000000,ContactDistance=5.000000,bSoftConstraint=False),ConeConstraint=(Swing1LimitDegrees=45.000000,Swing2LimitDegrees=45.000000,Swing1Motion=ACM\_Free,Swing2Motion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),TwistConstraint=(TwistLimitDegrees=45.000000,TwistMotion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),bDisableCollision=True,LinearProjectionAmount=0.500000,AngularProjectionAmount=0.000000,ParentInverseMassScale=1.000000) |
| DriveData | Optional motor/drive associated with the physics joint | [Rig Physics Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) | (LinearDriveConstraint=(PositionTarget=(X=0.000000,Y=0.000000,Z=0.000000),VelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),XDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),YDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),ZDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),bAccelerationMode=True),AngularDriveConstraint=(TwistDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SwingDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SlerpDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),OrientationTarget=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000),AngularVelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),AngularDriveMode=SLERP,bAccelerationMode=True),bUseSkeletalAnimation=True,SkeletalAnimationVelocityMultiplier=1.000000) |
| SimSpaceControlData | Data for the simulation space control | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |
| ParentSpaceControlData | Data for the parent space control | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The component key of the Physics Body | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |
| PhysicsJointComponentKey | The component key of the Physics Joint, if created | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |
| SimSpaceControlComponentKey | The component key of the simulation-space Physics Control, if created | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |
| ParentSpaceControlComponentKey | The component key of the parent-space Physics Control, if created | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnphysicscontrol.md

# Spawn Physics Control

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsControl

> Application Version: 5.7

### Description

Adds a new physics control as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Control |
| Type | [FRigUnit\_AddPhysicsControl](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsControl) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| ParentBodyComponentKey | The optional body that "does" the controlling - though if it is dynamic then it can move too | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| bUseParentBodyAsDefault | Whether or not to use the parent body (if one exists) as the Physics Control parent | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ChildBodyComponentKey | The body that is controlled | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| ControlData | Describes the initial strength etc of the new control | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |
| ControlMultiplier | Fine control over the control strengths etc | [Physics Control Multiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlMultiplier) | (LinearStrengthMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),LinearDampingRatioMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),LinearExtraDampingMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),MaxForceMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),AngularStrengthMultiplier=1.000000,AngularDampingRatioMultiplier=1.000000,AngularExtraDampingMultiplier=1.000000,MaxTorqueMultiplier=1.000000) |
| ControlTarget | The initial target for the new control | [Physics Control Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlTarget) | (TargetPosition=(X=0.000000,Y=0.000000,Z=0.000000),TargetVelocity=(X=0.000000,Y=0.000000,Z=0.000000),TargetOrientation=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000),TargetAngularVelocity=(X=0.000000,Y=0.000000,Z=0.000000),bApplyControlPointToTarget=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ControlComponentKey | The Physics Control component key that was created | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnphysicsjoint.md

# Spawn Physics Joint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsJoint

> Application Version: 5.7

### Description

Adds a new Physics Joint as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Joint,Articulation,Constraint,Skeleton |
| Type | [FRigUnit\_AddPhysicsJoint](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsJoint) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| ParentBodyComponentKey | The parent body of the joint. If unset, then the system will try to find a suitable body by looking for a parent that contains a body that is in the same solver as the child body. | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| ChildBodyComponentKey | The child body of the joint. If unset, then the system will try to find a suitable body | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| JointData | The properties of the joint | [Rig Physics Joint Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) | (bEnabled=True,bAutoCalculateParentOffset=True,ExtraParentOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),bAutoCalculateChildOffset=True,ExtraChildOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),LinearConstraint=(Limit=0.000000,XMotion=LCM\_Locked,YMotion=LCM\_Locked,ZMotion=LCM\_Locked,Stiffness=0.000000,Damping=0.000000,Restitution=0.000000,ContactDistance=5.000000,bSoftConstraint=False),ConeConstraint=(Swing1LimitDegrees=45.000000,Swing2LimitDegrees=45.000000,Swing1Motion=ACM\_Free,Swing2Motion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),TwistConstraint=(TwistLimitDegrees=45.000000,TwistMotion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),bDisableCollision=True,LinearProjectionAmount=0.500000,AngularProjectionAmount=0.000000,ParentInverseMassScale=1.000000) |
| DriveData | Optional motor/drive associated with the physics joint | [Rig Physics Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) | (LinearDriveConstraint=(PositionTarget=(X=0.000000,Y=0.000000,Z=0.000000),VelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),XDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),YDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),ZDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),bAccelerationMode=True),AngularDriveConstraint=(TwistDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SwingDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SlerpDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),OrientationTarget=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000),AngularVelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),AngularDriveMode=SLERP,bAccelerationMode=True),bUseSkeletalAnimation=True,SkeletalAnimationVelocityMultiplier=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint component key that was created | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnphysicssolver.md

# Spawn Physics Solver

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsSolver

> Application Version: 5.7

### Description

Adds a new physics solver as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Simulation |
| Type | [FRigUnit\_AddPhysicsSolver](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsSolver) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| SolverSettings | Settings for the physics solver that will be added | [Rig Physics Solver Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSolverSettings) | (bAutomaticallyAddPhysicsComponents=True,SimulationSpace=Component,CollisionSpace=Component,SpaceBone=(Type=None,Name=""),Collision=(Boxes=,Spheres=,Capsules=,Material=(Friction=1.000000,Restitution=1.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply)),Gravity=(X=0.000000,Y=0.000000,Z=-981.000000),WorldCollisionType=None,WorldCollisionExpiryFrames=3,WorldCollisionBoundsExpansion=1.100000,PositionIterations=8,VelocityIterations=4,ProjectionIterations=1,MaxNumRollingAverageStepTimes=1,CollisionBoundsExpansion=2.000000,BoundsVelocityMultiplier=1.000000,MaxVelocityBoundsExpansion=25.000000,MaxDepenetrationVelocity=0.000000,FixedTimeStep=0.020000,MaxTimeSteps=10,MaxDeltaTime=0.020000,bUseLinearJointSolver=True,bSolveJointPositionsLast=True,bUseManifolds=True,PositionThresholdForReset=0.000000,KinematicSpeedThresholdForReset=5000.000000,KinematicAccelerationThresholdForReset=0.000000) |
| SimulationSpaceSettings | Settings for the solver that apply to when it uses a simulation space other than "world". These typically relate to the movement of the simulation space itself, and how that is used by the solver. | [Rig Physics Simulation Space Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSimulationSpaceSettin-) | (SpaceMovementAmount=1.000000,VelocityScaleZ=1.000000,bClampLinearVelocity=False,MaxLinearVelocity=10000.000000,bClampAngularVelocity=False,MaxAngularVelocity=10000.000000,bClampLinearAcceleration=False,MaxLinearAcceleration=10000.000000,bClampAngularAcceleration=False,MaxAngularAcceleration=10000.000000,LinearAccelerationThresholdForTeleport=100000.000000,AngularAccelerationThresholdForTeleport=100000.000000,PositionChangeThresholdForTeleport=100.000000,OrientationChangeThresholdForTeleport=30.000000,LinearDragMultiplier=1.000000,AngularDragMultiplier=1.000000,ExternalLinearDrag=(X=0.000000,Y=0.000000,Z=0.000000),ExternalLinearVelocity=(X=0.000000,Y=0.000000,Z=0.000000),ExternalAngularVelocity=(X=0.000000,Y=0.000000,Z=0.000000),ExternalTurbulenceVelocity=(X=0.000000,Y=0.000000,Z=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The component key of the solver that has been added | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnscaleanimationchannel.md

# SpawnScaleAnimationChannel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnScaleAnimationChannel

> Application Version: 5.7

### Description

Adds a new animation channel to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | SpawnScaleAnimationChannel,Spawn Scale Float Animation Channel,Construction,Create,New,AddAnimationChannel,NewAnimationChannel,CreateAnimationChannel,AddChannel,NewChannel,CreateChannel,SpawnChannel,Spawn Scale Animation Channel |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InitialValue | The initial value of the new animation channel | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| MinimumValue | The minimum value of the new animation channel | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| MaximumValue | The maximum value for the animation channel | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10.000000 |
| LimitsEnabled | The enable settings for the limits | [Rig Unit Hierarchy Add Animation Channel Single Limit Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_9)   [FRigUnit\_HierarchyAddAnimationChannelVectorLimitSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_12) | (Enabled=(bMinimum=True,bMaximum=True)) |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewChannel |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spawnsocket.md

# Spawn Socket

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnSocket

> Application Version: 5.7

### Description

Adds a new socket to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,Locator,Group |
| Type | [FRigUnit\_HierarchyAddSocket](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddSocket) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The initial transform of the new element | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Space | Defines if the transform should be interpreted in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| Color | The color of the socket | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| Description | The (optional) description of the socket | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Parent | The parent of the new element to add | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewSocket |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spheretracebyobjecttypes.md

# Sphere Trace By Object Types

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByObjectTypes

> Application Version: 5.7

### Description

Sweeps a sphere against the world and return the first blocking hit. The trace is filtered by object types only, the collision response settings are ignored.
You can create custom object types in Project Setting - Collision

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Collision |
| Tags | Sweep,Raytrace,Collision,Collide,Trace |
| Type | [FRigUnit\_SphereTraceByObjectTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SphereTraceByObjectType-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | Start of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | End of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ObjectTypes | The types of objects that this trace can hit | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EObjectTypeQuery](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/EObjectTypeQuery)>> | () |
| Radius | Radius of the sphere to use for sweeping / tracing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bHit | Returns true if there was a hit | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitLocation | Hit location in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitNormal | Hit normal in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-spheretracebytracechannel.md

# Sphere Trace By Trace Channel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByTraceChannel

> Application Version: 5.7

### Description

Sweeps a sphere against the world and return the first blocking hit using a specific channel. Target objects can have different object types, but they need to have the same trace channel set to "block" in their collision response settings.
You can create custom trace channels in Project Setting - Collision.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Collision |
| Tags | Sweep,Raytrace,Collision,Collide,Trace |
| Type | [FRigUnit\_SphereTraceByTraceChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SphereTraceByTraceChann-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | Start of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | End of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| TraceChannel | The 'channel' that this trace is in, used to determine which components to hit | [Trace Type Query](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/ETraceTypeQuery) | TraceTypeQuery1 |
| Radius | Radius of the sphere to use for sweeping / tracing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bHit | Returns true if there was a hit | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitLocation | Hit location in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitNormal | Hit normal in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-sphericalposereader.md

# Spherical Pose Reader

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphericalPoseReader

> Application Version: 5.7

### Description

Outputs a float value between 0-1 based off of the driver item's rotation in a specified region.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Pose Reader, SPR |
| Type | [FRigUnit\_SphericalPoseReader](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SphericalPoseReader) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DriverItem | The bone that will drive the output parameter when rotated into the active regions of this pose reader. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| DriverAxis | The axis of the driver transform that is compared against the falloff regions. Typically the axis that is pointing at the child; usually X by convention. Default is X-axis (1,0,0). | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| RotationOffset | Rotate the entire falloff region to align with the desired area of effect. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=90.000000,Y=0.000000,Z=0.000000) |
| ActiveRegionSize | The size of the active region (green) that outputs the full value (1.0). Range is 0-1. Default is 0.1. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| ActiveRegionScaleFactors | The directional scaling parameters for the active region (green). | [Region Scale Factors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRegionScaleFactors) | (PositiveWidth=1.000000,NegativeWidth=1.000000,PositiveHeight=1.000000,NegativeHeight=1.000000) |
| FalloffSize | The size of the falloff region (yellow) that defines the start of the output range. A value of 1 wraps the entire sphere with falloff. Range is 0-1. Default is 0.2. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.200000 |
| FalloffRegionScaleFactors | The directional scaling parameters for the falloff region (yellow). | [Region Scale Factors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRegionScaleFactors) | (PositiveWidth=1.000000,NegativeWidth=1.000000,PositiveHeight=1.000000,NegativeHeight=1.000000) |
| FlipWidthScaling | Flip the positive / negative directions of the width scale factors. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| FlipHeightScaling | Flip the positive / negative directions of the height scale factors. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| OptionalParentItem | An optional parent to use as a stable frame of reference for the active regions (defaults to DriverItem's parent if unset). | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Debug | The debug settings | [Spherical Pose Reader Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FSphericalPoseReaderDebugSetting-) | (bDrawDebug=True,bDraw2D=False,bDrawLocalAxes=False,DebugScale=25.000000,DebugSegments=20,DebugThickness=0.250000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutputParam | The normalized output parameter; ranges from 0 (when outside yellow region) to 1 (in the green region) and smoothly blends from 0-1 in the yellow region. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-splineconstraint.md

# Spline Constraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineConstraint

> Application Version: 5.7

### Description

Fits a given chain to a spline curve.
Additionally provides rotational control matching the features of the Distribute Rotation node.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Fit,Resample,Spline |
| Type | [FRigUnit\_SplineConstraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_SplineConstraint) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to align | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Spline | The curve to align to | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| Alignment | Specifies how to align the chain on the curve | [Control Rig Curve Alignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigCurveAlignment) | Stretched |
| Minimum | The minimum U value to use on the curve | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | The maximum U value to use on the curve | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| PrimaryAxis | The primary axis to use when building transforms | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The secondary axis to use when building transforms | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-splinefrompoints.md

# Spline From Points

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromPoints

> Application Version: 5.7

### Description

Creates a Spline curve from an array of positions

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Spline From Positions |
| Type | [FRigUnit\_ControlRigSplineFromPoints](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_ControlRigSplineFromPoi-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | The input points to form the spline | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| SplineMode | The mode to use for the spline | [Spline Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/ESplineType) | Hermite |
| bClosed | If True the spline will be closed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SamplesPerSegment | Specifies the detail per segment of the spline | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| Compression | The amount of compression to apply | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Stretch | The amount of stretch to allow for the spline | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The resulting spline | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-splinefromtransforms.md

# Spline From Transforms

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromTransforms

> Application Version: 5.7

### Description

Creates a Spline curve from an array of transforms

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Spline From Transforms |
| Type | [FRigUnit\_ControlRigSplineFromTransforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_ControlRigSplineFromTra-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | The input transforms to build the spline from | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| SplineMode | The mode to use for the spline | [Spline Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/ESplineType) | Hermite |
| bClosed | If True the spline will be closed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SamplesPerSegment | Specifies the detail per segment of the spline | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| Compression | The amount of compression to apply | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Stretch | The amount of stretch to allow for the spline | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The resulting spline | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-split.md

# Split

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Split

> Application Version: 5.7

### Description

Splits a string into multiple sections given a separator

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Type | [FRigVMFunction\_StringSplit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringSplit) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to split up | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Separator | The separator to use to split up the input string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The array of split up parts of the input string | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-springik.md

# Spring IK

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringIK

> Application Version: 5.7

### Description

The Spring IK solver uses a verlet integrator to perform an IK solve.
It support custom constraints including distance, length etc.
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | IK |
| Type | [FRigUnit\_SpringIK](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SpringIK) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StartBone | The name of the first bone to solve | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| EndBone | The name of the second bone to solve | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| HierarchyStrength | Sets the coefficient of the springs along the hierarchy. Values between 1 and 2048 are common. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 256.000000 |
| EffectorStrength | Sets the coefficient of the springs towards the effector. Values between 1 and 2048 are common. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 64.000000 |
| EffectorRatio | Defines the equilibrium of the effector springs. This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| RootStrength | Sets the coefficient of the springs towards the root. Values between 1 and 2048 are common. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 64.000000 |
| RootRatio | Defines the equilibrium of the root springs. This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Damping | The higher the value to more quickly the simulation calms down. Values between 0.0001 and 0.75 are common. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.400000 |
| PoleVector | The polevector to use for the IK solver This can be a location or direction. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| bFlipPolePlane | If set to true the pole plane will be flipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| PoleVectorKind | The kind of pole vector this is representing - can be a direction or a location | [Control Rig Vector Kind](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigVectorKind) | Direction |
| PoleVectorSpace | The space in which the pole vector is expressed | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| PrimaryAxis | The major axis being aligned - along the bone | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The minor axis being aligned - towards the pole vector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=0.000000) |
| bLiveSimulation | If set to true simulation will continue for all intermediate bones over time. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Iterations | Drives how precise the solver operates. Values between 4 and 24 are common. This is only used if the simulation is not live (bLiveSimulation setting). | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| bLimitLocalPosition | If set to true bones are placed within the original distance of the previous local transform. This can be used to avoid stretch. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugSettings | The debug setting for the node | [Rig Unit Spring IK Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SpringIK_DebugSettings) | (bEnabled=False,Scale=1.000000,Color=(R=0.000000,G=0.000000,B=1.000000,A=1.000000),WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-springinterp.md

# SpringInterp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterp

> Application Version: 5.7

### Description

Uses a simple spring model to interpolate a float from Current to Target.
Uses a simple spring model to interpolate a vector from Current to Target.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Simulation|Springs |
| Tags | SpringInterp,Spring Interpolate,Alpha,SpringInterpolate,Verlet |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | Rest/target position of the spring. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Strength | The spring strength determines how hard it will pull towards the target. The value is the frequency at which it will oscillate when there is no damping. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 4.000000 |
| CriticalDamping | The amount of damping in the spring. Set it smaller than 1 to make the spring oscillate before stabilizing on the target. Set it equal to 1 to reach the target without overshooting. Set it higher than one to make the spring take longer to reach the target. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Force | Extra force to apply (since the mass is 1, this is also the acceleration). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| bUseCurrentInput | If true, then the Current input will be used to initialize the state, and is required to be a variable that holds the current state. If false then the Target value will be used to initialize the state and the Current input will be ignored/unnecessary as a state will be maintained by this node. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Current | Current position of the spring. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| TargetVelocityAmount | The amount that the velocity should be passed through to the spring. A value of 1 will result in more responsive output, but if the input is noisy or has step changes, these discontinuities will be passed through to the output much more than if a smaller value such as 0 is used. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bInitializeFromTarget | If true, then the initial value will be taken from the target value, and not from the current value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | New position of the spring after delta time. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Velocity | The resulting velocity of this spring | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-springinterpolate.md

# Spring Interpolate

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterpolate

> Application Version: 5.7

### Description

Uses a simple spring model to interpolate a quaternion from Current to Target.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Simulation|Springs |
| Tags | Alpha,SpringInterpolate,Verlet |
| Type | [FRigUnit\_SpringInterpQuaternionV2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SpringInterpQuaternionV-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | Rest/target position of the spring. | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| Strength | The spring strength determines how hard it will pull towards the target. The value is the frequency at which it will oscillate when there is no damping. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 4.000000 |
| CriticalDamping | The amount of damping in the spring. Set it smaller than 1 to make the spring oscillate before stabilizing on the target. Set it equal to 1 to reach the target without overshooting. Set it higher than one to make the spring take longer to reach the target. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Torque | Extra torque to apply (since the moment of inertia is 1, this is also the angular acceleration). | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bUseCurrentInput | If true, then the Current input will be used to initialize the state, and is required to be a variable that holds the current state. If false then the Target value will be used to initialize the state and the Current input will be ignored/unnecessary as a state will be maintained by this node. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Current | Current position of the spring. | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| TargetVelocityAmount | The amount that the velocity should be passed through to the spring. A value of 1 will result in more responsive output, but if the input is noisy or has step changes, these discontinuities will be passed through to the output much more than if a smaller value such as 0 is used. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bInitializeFromTarget | If true, then the initial value will be taken from the target value, and not from the current value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | New position of the spring after delta time. | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| AngularVelocity | Angular velocity | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-sqrt.md

# Sqrt

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Sqrt

> Application Version: 5.7

### Description

Returns the square root of the given value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Sqrt,Root,Square |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-startprofilingtimer.md

# Start Profiling Timer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StartProfilingTimer

> Application Version: 5.7

### Description

Starts a profiling timer for debugging, used in conjunction with End Profiling Timer

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Debug |
| Tags | Measure,BeginProfiling,Profile |
| Type | [FRigUnit\_StartProfilingTimer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_StartProfilingTimer) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-startswith.md

# StartsWith

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StartsWith

> Application Version: 5.7

### Description

Tests whether this name starts with given name
Tests whether this string starts with given string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | StartsWith,Starts With,Left |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to search within | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| Start | The start name to look for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the given input name starts with the given start string | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-stepphysicssolver.md

# Step Physics Solver

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StepPhysicsSolver

> Application Version: 5.7

### Description

Steps the specified physics solver

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Simulate |
| Type | [FRigUnit\_StepPhysicsSolver](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_StepPhysicsSolver) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The physics solver that should be stepped | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| DeltaTimeOverride | If this is zero, then the execute context time will be used. If this is positive then it will override the delta time. A negative value will prevent the solver from stepping, but there will still be update costs associated with the node. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SimulationSpaceDeltaTimeOverride | If this is zero, then the simulation delta time will be used for evaluating movement of the simulation space. If this is positive then it will override. This may be needed if the component movement is being done in parallel, in which case you might need to pass in the previous time delta here. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Alpha | How much of the simulation is combined with the input bone. This currently happens in component space. Note that the simulation will continue to run, even if alpha = 0 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| VisualizationSettings | Settings that specify how the solver state should be visualized during/after the step | [Rig Physics Visualization Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsVisualizationSettings) | (bEnableVisualization=True,LineThickness=1.000000,ShapeSize=1,ShapeDetail=16,bShowBodies=True,bShowCentreOfMass=False,bShowJoints=True,bShowControls=False,bShowWorldObjects=True,bShowWorldOverlapBox=False,bShowActiveContacts=True,bShowInactiveContacts=False) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-subtract.md

# Subtract

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Subtract

> Application Version: 5.7

### Description

Returns the difference of the two values

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Subtract,- |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first color for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |
| B | The second color for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting color | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-switch.md

# Switch

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Switch

> Application Version: 5.7

### Description

Run a branch based on an integer index

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | Case |
| Type | [FRigVMDispatch\_SwitchInt32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_SwitchInt32) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Index | The index of the case to switch to | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Cases | The Cases execute argument. | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Completed | The Completed execute argument. | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-switchparent.md

# Switch Parent

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SwitchParent

> Application Version: 5.7

### Description

Switches an element to a new parent.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Children,Parent,Constraint,Space,Switch |
| Type | [FRigUnit\_SwitchParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SwitchParent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mode | Depending on this the child will switch to the world, \* back to its default or to the item provided by the Parent pin | [Rig Switch Parent Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigSwitchParentMode) | ParentItem |
| Child | The child to switch to a new parent | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Parent | The optional parent to switch to. This is only used if the mode is set to 'Parent Item' | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| bMaintainGlobal | If set to true the item will maintain its global transform, \* otherwise it will maintain local | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-tan.md

# Tan

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Tan

> Application Version: 5.7

### Description

Returns the tangens value of the given value (in radians)

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Tan |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-tangentfromspline.md

# Tangent From Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TangentFromSpline

> Application Version: 5.7

### Description

Retrieves the tangent from a given Spline and U value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_TangentFromControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_TangentFromControlRigSp-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| U | The U value along the spline to evaluate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Tangent | The tangent at the evaluated location on the spline | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-timeloop.md

# Time Loop

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeLoop

> Application Version: 5.7

### Description

Simulates a time value - and outputs loop information

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | Playback,Pause,Timeline |
| Type | [FRigVMFunction\_TimeLoop](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_TimeLoop) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Speed | The speed to play-back the time at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Duration | the duration of a single loop in seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Normalize | if set to true the output relative and flipflop will be normalized over the duration. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Absolute | the overall time in seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Relative | the relative time in seconds (within the loop) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| FlipFlop | the relative time in seconds (within the loop), going from 0 to duration and then back from duration to 0, or 0 to 1 and 1 to 0 if Normalize is turned on | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Even | true if the iteration of the loop is even | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-timeoffset.md

# TimeOffset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeOffset

> Application Version: 5.7

### Description

Records a value over time and can access the value from the past

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Time |
| Tags | TimeOffset,Value Over Time (Float),Buffer,Delta,History,Previous,Delay,Value Over Time (Vector),Value Over Time (Transform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to record | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SecondsAgo | Seconds of time in the past you want to query the value for | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| BufferSize | The sampling precision of the buffer. The higher the more precise - the more memory usage. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| TimeRange | The maximum time required for offsetting in seconds. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting offset value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-toaxisandangle.md

# To Axis And Angle

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToAxisAndAngle

> Application Version: 5.7

### Description

Retrieves the axis and angle of a quaternion in radians

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct,GetAxis,GetAngle |
| Type | [FRigVMFunction\_MathQuaternionToAxisAndAngle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionToA-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Axis | The axis of the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Angle | The angle in radians of the quaternion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-toeuler.md

# To Euler

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToEuler

> Application Version: 5.7

### Description

Retrieves the euler angles in degrees

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathQuaternionToEuler](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionToE-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| RotationOrder | The rotation order to use when encoding the euler angles | [Euler Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | ZYX |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The euler angles in degrees representing the quaternion in the given rotation order | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-toggled.md

# Toggled

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Toggled

> Application Version: 5.7

### Description

Returns true if the value has changed from the last run

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Tags | Changed,Different |
| Type | [FRigVMFunction\_MathBoolToggled](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolToggled) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to check / compare | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Toggled | True if the input value has been toggled | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-tointeger.md

# To Integer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToInteger

> Application Version: 5.7

### Description

Converts a string to an integer

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | ToInt,Number |
| Type | [FRigVMFunction\_StringToInteger](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringToInteger) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to convert to integer | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| ChopLeft | chops non-digit characters from the left of the string | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ChopRight | chops non-digit characters from the right of the string | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting integer number (or INDEX\_NONE) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Success | True if the string was successfully converted to integer | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-tolowercase.md

# To Lowercase

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToLowercase

> Application Version: 5.7

### Description

Converts the string to lower case

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Type | [FRigVMFunction\_StringToLowercase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringToLowercase) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to convert to lowercase | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting lowercased string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-tostring.md

# To String

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToString

> Application Version: 5.7

### Description

Converts any value to string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Type | [FRigDispatch\_ToString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigDispatch_ToString) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to convert to a string | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting string representation of the value | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-toswing-twist.md

# To Swing & Twist

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToSwing&Twist

> Application Version: 5.7

### Description

Computes the swing and twist components of a quaternion

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Type | [FRigVMFunction\_MathQuaternionSwingTwist](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionSwi-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Input | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| TwistAxis | The axis to treat as the twist axis | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Swing | The resulting swing quaternion of the input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Twist | The resulting twist quaternion of the input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-touppercase.md

# To Uppercase

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToUppercase

> Application Version: 5.7

### Description

Converts the string to upper case

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Type | [FRigVMFunction\_StringToUppercase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringToUppercase) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to convert to uppercase | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting uppercased string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-tovectors.md

# To Vectors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors

> Application Version: 5.7

## To Vectors (FRigVMFunction\_MathMatrixToVectors)

Converts the matrix to its vectors

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Matrix |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathMatrixToVectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathMatrixToVecto-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The matrix to split up to vectors | [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (XPlane=(W=0.000000,X=1.000000,Y=0.000000,Z=0.000000),YPlane=(W=0.000000,X=0.000000,Y=1.000000,Z=0.000000),ZPlane=(W=0.000000,X=0.000000,Y=0.000000,Z=1.000000),WPlane=(W=1.000000,X=0.000000,Y=0.000000,Z=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | The resulting origin | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| X | The resulting X component | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Y | The resulting Y component | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Z | The resulting Z component | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## To Vectors ()

Retrieves the forward, right and up vectors of a quaternion
Retrieves the forward, right and up vectors of a transform's quaternion

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | ToVectors,To Vectors,Forward,Right,Up |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Forward | The forward axis of the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Right | The right axis of the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Up | The up axis of the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-toworld.md

# To World

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToWorld

> Application Version: 5.7

### Description

Converts a transform from rig (global) space to world space
Converts a position / location from rig (global) space to world space
Converts a rotation from rig (global) space to world space

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | To World,Global,Local,World,Actor,ComponentSpace,FromRig |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input transform in global / rig space | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| World | The result transform in world space | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-trackinputpose.md

# Track Input Pose

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TrackInputPose

> Application Version: 5.7

### Description

Forces tracking of the input animation (on all physics bodies) for the next N frames

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Reset,Simulate |
| Type | [FRigUnit\_TrackInputPose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_TrackInputPose) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The solver to relate this new physics element to | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| NumberOfFrames | The number of frames to track the input pose for | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| bForceNumberOfFrames | If true, then the number will be forced, potentially reducing the number. If false, then the NumberOfFrames will only be used to increase the number of frames remaining. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-transformarraytosrt.md

# Transform Array to SRT

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformArraytoSRT

> Application Version: 5.7

### Description

Decomposes a Transform Array to its components.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | EulerTransform,Scale,Rotation,Orientation,Translation,Location |
| Type | [FRigVMFunction\_MathTransformArrayToSRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformArra-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | The input transform array to decompose | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Translations | The array of translations - one for each input transform | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Rotations | The array of rotation - one for each input transform | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Scales | The array of scale values - one for each input transform | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-transformbox.md

# Transform Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformBox

> Application Version: 5.7

### Description

Transforms the box by a given transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,BoundingBox |
| Type | [FRigVMFunction\_MathBoxTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | the box to transform | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Transform | the transform to apply to the box | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | the resulting transformed box | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-transformfromspline.md

# Transform From Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSpline

> Application Version: 5.7

### Description

Retrieves the transform from a given Spline and U value based on the given primary and secondary axis

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_TransformFromControlRigSpline2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_TransformFromControlRig-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| U | The U value along the spline to evaluate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| PrimaryAxis | The primary axis to use when building the transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The secondary axis to use when building the transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The resulting composed transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-transformfromsplinewithupvector.md

# Transform From Spline (with UpVector)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSplinewithUpVector

> Application Version: 5.7

### Description

Retrieves the transform from a given Spline and U value based on the given Up Vector and Roll

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_TransformFromControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_TransformFromControlRig-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| UpVector | The up-vector to use to build the transform's rotation | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| Roll | The roll to apply to the resulting rotation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| U | The U value along the spline to evaluate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The resulting composed transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-transformfromsrt.md

# Transform from SRT

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformfromSRT

> Application Version: 5.7

### Description

Composes a Transform (and Euler Transform) from its components.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | EulerTransform,Scale,Rotation,Orientation,Translation,Location |
| Type | [FRigVMFunction\_MathTransformFromSRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformFrom-_2) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Location | The location for the desired transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Rotation | The euler angles in degrees for the desired transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RotationOrder | The rotation order to interpret the euler angles by | [Euler Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | XYZ |
| Scale | The scale for the desired transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The result as a transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| EulerTransform | The result as a euler transform | [Euler Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-transformlocation.md

# Transform Location

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformLocation

> Application Version: 5.7

### Description

Multiplies a given vector (location) by the transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | Multiply |
| Type | [FRigVMFunction\_MathTransformTransformVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformTran-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The input transform to transform the input vector by | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Location | The input vector to transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting transformed vector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-transformray.md

# Transform Ray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformRay

> Application Version: 5.7

### Description

Transforms a ray

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Ray |
| Tags | Multiply,Project |
| Type | [FRigVMFunction\_MathRayTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathRayTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Ray | The ray to transform | [Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |
| Transform | The transform to apply to the ray | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting transformed ray | [Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-trimwhitespace.md

# Trim Whitespace

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TrimWhitespace

> Application Version: 5.7

### Description

Trims the whitespace from a string (start and end)

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | Space,WhiteSpace,Remove,Truncate |
| Type | [FRigVMFunction\_StringTrimWhitespace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringTrimWhitesp-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to trim | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting trimmed string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-true.md

# True

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/True

> Application Version: 5.7

### Description

Returns true

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Tags | Yes |
| Type | [FRigVMFunction\_MathBoolConstTrue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolConstTrue) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value of the constant | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-twopi.md

# TwoPi

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TwoPi

> Application Version: 5.7

### Description

Returns PI \* 2.0

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | TwoPi,Two Pi,Tau |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value of the constant | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 6.283185 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-union.md

# Union

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Union

> Application Version: 5.7

### Description

Merges two arrays while ensuring unique elements.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayUnion](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayUnion) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to merge the other array with. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Other | The second array to merge to the first one. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-unit.md

# Unit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Unit

> Application Version: 5.7

### Description

Returns the normalized quaternion
Returns the normalized value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Unit,Normalize |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-unsetcurvevalue.md

# Unset Curve Value

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UnsetCurveValue

> Application Version: 5.7

### Description

UnsetCurveValue is used to perform a change in the curve container by invalidating a single Curve value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Curve |
| Tags | UnsetCurveValue |
| Type | [FRigUnit\_UnsetCurveValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_UnsetCurveValue) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Curve | The name of the Curve to set the Value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-updatephysicscontroltarget.md

# Update Physics Control Target

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UpdatePhysicsControlTarget

> Application Version: 5.7

### Description

Sets the target for a physics control and updates the target velocities based on the previews
targets (which will be overwritten)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyUpdateControlTarget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyUpdateControlT-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |
| TargetPosition | The target position of the child body, relative to the parent body | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| TargetOrientation | The target orientation of the child body, relative to the parent body | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Pitch=0.000000,Yaw=0.000000,Roll=0.000000) |
| DeltaTime | The delta time used to calculate the target velocity | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-userdefinedevent.md

# User Defined Event

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UserDefinedEvent

> Application Version: 5.7

### Description

User Defined Event for running custom logic

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Events |
| Tags | Event,Entry,MyEvent |
| Type | [FRigVMFunction\_UserDefinedEvent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_UserDefinedEvent) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| EventName | The name of the event. Given this name the event can be invoked using the run event node. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | My Event |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-verletvector.md

# Verlet (Vector)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VerletVector

> Application Version: 5.7

### Description

Simulates a single position over time using Verlet integration. It is recommended to use SpringInterp instead as it
is more accurate and stable, and has more meaningful parameters.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Springs |
| Tags | Simulate,Integrate |
| Type | [FRigVMFunction\_VerletIntegrateVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VerletIntegrateVe-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | The target value to interpolate / integrate towards | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Strength | The strength of the verlet spring | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 64.000000 |
| Damp | The amount of damping to apply ( 0.0 to 1.0, but usually really low like 0.005 ) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| Blend | The amount of blending to apply per second | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| Force | The force feeding into the solver. Can be used for gravity. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Position | The resulting simulated position | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Velocity | The resulting simulated velocity | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Acceleration | The resulting simulated acceleration | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visualdebug.md

# VisualDebug

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebug

> Application Version: 5.7

### Description

Debug draw parameters for an Axis given a quaternion
Debug draw parameters for an Axis given a transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | VisualDebug,Visual Debug Quat,Draw,Rotation,Visual Debug Transform,Axes |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The pass through rotation to draw | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Thickness | The line thickness to use for the drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Scale | The scale to apply to the axes drawn | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visualdebugvector.md

# Visual Debug Vector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebugVector

> Application Version: 5.7

### Description

Debug draw parameters for a Point or Vector given a vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,Point |
| Type | [FRigVMFunction\_VisualDebugVectorNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualDebugVector-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The pass through vector to draw | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Mode | The mode to draw the vector with | [Rig Unit Visual Debug Point Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigUnitVisualDebugPointMode) | Point |
| Color | The color to use for the debug draw | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use for the drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Scale | The scale to apply to the vector when drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogarrow.md

# Visual Log Arrow

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogArrow

> Application Version: 5.7

### Description

Logs arrow - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String,Direction |
| Type | [FRigVMFunction\_VisualLogArrow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogArrow) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SegmentStart | The start of the arrow | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| SegmentEnd | The end of the arrow | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ArrowHeadSize | The size of the arrow head | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 8.000000 |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogbox.md

# Visual Log Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogBox

> Application Version: 5.7

### Description

Logs box shape - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogBox) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to draw | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| bWireframe | Whether to display as wireframe | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogcapsule.md

# Visual Log Capsule

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogCapsule

> Application Version: 5.7

### Description

Logs capsule shape - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogCapsule](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogCapsule) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Base | The base or origin of the capsule | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| HalfHeight | Half the height of the capsule | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Radius | The radius of the capsule | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Rotation | The orientation of the capsule | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| bWireframe | Whether to display as wireframe | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogcircle.md

# Visual Log Circle

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogCircle

> Application Version: 5.7

### Description

Logs circle - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String,Disc |
| Type | [FRigVMFunction\_VisualLogCircle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogCircle) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Center | The center of the circle | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| UpAxis | The up axis/normal of the circle's plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| Radius | The radius of the circle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Thickness | The thickness of the circle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bWireframe | Whether to display as wireframe | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogcone.md

# Visual Log Cone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogCone

> Application Version: 5.7

### Description

Logs cone shape - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogCone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogCone) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | The origin of the cone | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Direction | The direction of the cone | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| Length | The length of the cone | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Angle | The angle of the cone | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| bWireframe | Whether to display as wireframe | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogcylinder.md

# Visual Log Cylinder

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogCylinder

> Application Version: 5.7

### Description

Logs cylinder shape - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogCylinder](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogCylinder) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | The start of the line segment forming the cylinder | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | The end of the line segment forming the cylinder | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Radius | The radius of the cylinder | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| bWireframe | Whether to display as wireframe | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visualloglocation.md

# Visual Log Location

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogLocation

> Application Version: 5.7

### Description

Logs location as sphere with given radius - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String,Sphere |
| Type | [FRigVMFunction\_VisualLogLocation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogLocation) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Location | The location to log | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Radius | The radius of the sphere to log the location with | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogorientedbox.md

# Visual Log Oriented Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogOrientedBox

> Application Version: 5.7

### Description

Logs oriented box shape - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogOrientedBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogOriented-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to draw | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Transform | The transform of the box | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bWireframe | Whether to display as wireframe | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogsegment.md

# Visual Log Segment

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogSegment

> Application Version: 5.7

### Description

Logs segment - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String,Line |
| Type | [FRigVMFunction\_VisualLogSegment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogSegment) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SegmentStart | The start of the line segment | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| SegmentEnd | The end of the line segment | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Thickness | The thickness of the segment | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogsphere.md

# Visual Log Sphere

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogSphere

> Application Version: 5.7

### Description

Logs sphere shape - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogSphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogSphere) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Center | The centre of the sphere | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Radius | The radius of the sphere | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| bWireframe | Whether to display as wireframe | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-visuallogtext.md

# Visual Log Text

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogText

> Application Version: 5.7

### Description

Logs simple text string with Visual Logger - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogText) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Text | The text to log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig.md

# ControlRig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig

> Application Version: 5.7

### Animation

| Node | Description |
| --- | --- |
| [Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Curve) | Provides a constant curve to be used for multiple curve evaluations |
| [Delta Time](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DeltaTime) | Returns the time gone by from the previous evaluation |
| [Ease](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Ease) | Returns the eased version of the input value |
| [EaseType](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EaseType) | A constant value of an easing type |
| [Evaluate Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateCurve) | Evaluates the provided curve. Values are normalized between 0 and 1 |
| [Frames to Seconds](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FramestoSeconds) | Converts frames to seconds based on the current frame rate |
| [Now](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Now) | Returns the current time (year, month, day, hour, minute) |
| [Seconds to Frames](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SecondstoFrames) | Converts seconds to frames based on the current frame rate |

### Animation Attribute

| Node | Description |
| --- | --- |
| [Get Animation Attribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAnimationAttribute) | Get the value of an animation attribute from the skeletal mesh |
| [Set Animation Attribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute) | Modify an animation attribute if one is found, otherwise add a new animation attribute |

### Array

| Node | Description |
| --- | --- |
| [Add](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Add) | Adds an element to an array and returns the new element's index. Modifies the input array. |
| [Append](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Append) | Appends the another array to the main one. Modifies the input array. |
| [At](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/At) | Returns an element of an array by index. |
| [Clone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Clone) | Clones an array and returns a duplicate. |
| [Difference](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Difference) | Creates a new array containing the difference between the two input arrays. |
| [Find](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Find) | Searchs a potential element in an array and returns its index. |
| [For Each](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEach) | Loops over the elements in an array. |
| [Init](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Init) | Sets the size of the array, initializing all elements to the given value. Modifies the input array. |
| [Insert](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Insert) | Inserts an element into an array at a given index. Modifies the input array. |
| [Intersection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Intersection) | Creates a new array containing the intersection between the two input arrays. |
| [IsEmpty](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsEmpty) | Returns true if the array is empty |
| [Make Array](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArray) | Creates a new array from its elements. |
| [Num](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Num) | Returns the number of elements of an array |
| [Remove](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Remove) | Removes an element from an array by index. Modifies the input array. |
| [Reset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Reset) | Removes all elements from an array. Modifies the input array. |
| [Reverse](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Reverse) | Reverses the order of the elements of an array. Modifies the input array. |
| [Set At](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAt) | Sets an element of an array by index. Modifies the input array. |
| [Set Num](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetNum) | Sets the numbers of elements of an array. Modifies the input array. |
| [Union](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Union) | Merges two arrays while ensuring unique elements. Modifies the input array. |

### Collision

| Node | Description |
| --- | --- |
| [Line Trace By Object Types](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByObjectTypes) | Performs a line trace against the world and return the first blocking hit. |
| [Line Trace By Trace Channel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByTraceChannel) | Performs a line trace against the world and return the first blocking hit using a specific channel. |
| [Sphere Trace By Object Types](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByObjectTypes) | Sweeps a sphere against the world and return the first blocking hit. |
| [Sphere Trace By Trace Channel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByTraceChannel) | Sweeps a sphere against the world and return the first blocking hit using a specific channel. |

### Constraints

| Node | Description |
| --- | --- |
| [Aim Constraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AimConstraint) | Orients an item such that its aim axis points towards a global target. |
| [Parent Constraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraint) | Constrains an item's transform to multiple items' transforms |
| [Parent Constraint Math](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraintMath) | Computes the output transform by constraining the input transform to multiple parents |
| [Position Constraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PositionConstraint) | Constrains an item's position to multiple items' positions |
| [Rotation Constraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RotationConstraint) | Constrains an item's rotation to multiple items' rotations |
| [Scale Constraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ScaleConstraint) | Constrains an item's scale to multiple items' scales |

### Controls

| Node | Description |
| --- | --- |
| [Get Control Bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlBool) | GetControlBool is used to retrieve a single Bool from a hierarchy. |
| [Get Control Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlColor) | GetControlColor is used to retrieve the color of control |
| [Get Control Float](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlFloat) | GetControlFloat is used to retrieve a single Float from a hierarchy. |
| [Get Control Integer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlInteger) | GetControlInteger is used to retrieve a single Integer from a hierarchy. |
| [Get Control Offset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlOffset) | GetControlOffset returns the offset transform of a given control. |
| [Get Control Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlRotator) | GetControlRotator is used to retrieve a single Rotator from a hierarchy. |
| [Get Control Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlTransform) | GetControlTransform is used to retrieve a single transform from a hierarchy. |
| [Get Control Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlVector) | GetControlVector is used to retrieve a single Vector from a hierarchy, can be used for Controls of type "Position" or "Scale". |
| [Get Control Vector2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlVector2D) | GetControlVector2D is used to retrieve a single Vector2D from a hierarchy. |
| [Get Control Visibility](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlVisibility) | GetControlVisibility is used to retrieve the visibility of a control |
| [Get Driven Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetDrivenControls) | GetControlDrivenList is used to retrieve the list of affected controls of an indirect control |
| [Get Shape Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetShapeTransform) | GetShapeTransform is used to retrieve single control's shape transform. |
| [GetAnimationChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAnimationChannel) | Get Bool Channel is used to retrieve a control's animation channel value Get Float Channel is used to retrieve a control's animation channel value Get Int Channel is used to retrieve a control's animation channel value Get Vector2D Channel is used to retrieve a control's animation channel value Get Vector Channel is used to retrieve a control's animation channel value Get Rotator Channel is used to retrieve a control's animation channel value Get Transform Channel is used to retrieve a control's animation channel value |
| [GetAnimationChannelFromItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAnimationChannelFromItem) | Get Bool Channel is used to retrieve a control's animation channel value Get Float Channel is used to retrieve a control's animation channel value Get Int Channel is used to retrieve a control's animation channel value Get Vector2D Channel is used to retrieve a control's animation channel value Get Vector Channel is used to retrieve a control's animation channel value Get Rotator Channel is used to retrieve a control's animation channel value Get Transform Channel is used to retrieve a control's animation channel value |
| [Set Control Bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlBool) | SetControlBool is used to perform a change in the hierarchy by setting a single control's bool value. |
| [Set Control Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlColor) | SetControlColor is used to change the control's color |
| [Set Control Float](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlFloat) | SetControlFloat is used to perform a change in the hierarchy by setting a single control's float value. |
| [Set Control Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlRotator) | SetControlRotator is used to perform a change in the hierarchy by setting a single control's Rotator value. |
| [Set Control Scale Offset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlScaleOffset) | SetControlScaleOffset is used to perform a change in the hierarchy by setting a single control's scale offset. |
| [Set Control Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector) | SetControlVector is used to perform a change in the hierarchy by setting a single control's Vector value. |
| [Set Control Vector2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector2D) | SetControlVector2D is used to perform a change in the hierarchy by setting a single control's Vector2D value. |
| [Set Control Visibility](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVisibility) | SetControlVisibility is used to change the visibility on a control at runtime |
| [Set Driven Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetDrivenControls) | SetControlDrivenList is used to change the list of affected controls of an indirect control |
| [Set Multiple Controls Bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultipleControlsBool) | SetMultiControlBool is used to perform a change in the hierarchy by setting multiple controls' bool value. |
| [Set Shape Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeTransform) | SetShapeTransform is used to perform a change in the hierarchy by setting a single control's shape transform. |
| [SetAnimationChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannel) | Set Bool Channel is used to set a control's animation channel value Set Float Channel is used to set a control's animation channel value Set Int Channel is used to set a control's animation channel value Set Vector2D Channel is used to set a control's animation channel value Set Vector Channel is used to set a control's animation channel value Set Rotator Channel is used to set a control's animation channel value Set Transform Channel is used to set a control's animation channel value |
| [SetAnimationChannelFromItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannelFromItem) | Set Bool Channel is used to set a control's animation channel value Set Float Channel is used to set a control's animation channel value Set Int Channel is used to set a control's animation channel value Set Vector2D Channel is used to set a control's animation channel value Set Vector Channel is used to set a control's animation channel value Set Rotator Channel is used to set a control's animation channel value Set Transform Channel is used to set a control's animation channel value |
| [SetControlOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlOffset) | SetControlOffset is used to perform a change in the hierarchy by setting a single control's transform. |
| [SetMultiControlValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultiControlValue) | SetMultiControlFloat is used to perform a change in the hierarchy by setting multiple controls' float value. |

### Core

| Node | Description |
| --- | --- |
| [Break](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Break) | Decomposes a struct into its elements |
| [Chop](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Chop) | Returns the left or right most characters from the name chopping the given number of characters from the start or the end Returns the left or right most characters from the string chopping the given number of characters from the start or the end |
| [Concat](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Concat) | Concatenates two names together to make a new name Concatenates two strings together to make a new string |
| [Constant](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Constant) | Provides a constant value to the graph |
| [Contains](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Contains) | Returns true or false if a given name exists in another given name |
| [EndsWith](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EndsWith) | Tests whether this name ends with given name Tests whether this string ends with given string |
| [Equals](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Equals) | Compares any two values and return true if they are identical |
| [Make](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Make) | Composes a struct out of its elements |
| [Not Equals](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/NotEquals) | Compares any two values and return true if they are not identical |
| [Replace](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Replace) | Replace all occurrences of a subname in this name Replace all occurrences of a substring in this string |
| [StartsWith](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StartsWith) | Tests whether this name starts with given name Tests whether this string starts with given string |

### Core|Name

| Node | Description |
| --- | --- |
| [Get Numeric Suffix](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetNumericSuffix) | Tests whether this name ends with a numeric suffix |
| [Is None](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsNone) | Returns true if this name is none |
| [Is Valid](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsValid) | Returns true if this name is valid / is not none |

### Core|String

| Node | Description |
| --- | --- |
| [Find](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Find) | Finds a string within another string |
| [Join](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Join) | Joins a string into multiple sections given a separator |
| [Left](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Left) | Returns the left most characters of a string |
| [Length](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Length) | Returns the length of a string |
| [Middle](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Middle) | Returns the middle section of a string |
| [Pad Integer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PadInteger) | Converts an integer number to a string with padding |
| [Reverse](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Reverse) | Returns the reverse of the input string |
| [Right](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Right) | Returns the right most characters of a string |
| [Split](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Split) | Splits a string into multiple sections given a separator |
| [To Integer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToInteger) | Converts a string to an integer |
| [To Lowercase](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToLowercase) | Converts the string to lower case |
| [To Uppercase](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToUppercase) | Converts the string to upper case |
| [Trim Whitespace](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TrimWhitespace) | Trims the whitespace from a string (start and end) |

### Curve

| Node | Description |
| --- | --- |
| [Curve Exists](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CurveExists) | CurveExists is used to check whether a curve exists or not. |
| [Get Curve Value](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetCurveValue) | GetCurveValue is used to retrieve a single float from a Curve |
| [Set Curve Value](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetCurveValue) | SetCurveValue is used to perform a change in the curve container by setting a single Curve value. |
| [Unset Curve Value](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UnsetCurveValue) | UnsetCurveValue is used to perform a change in the curve container by invalidating a single Curve value. |

### Debug

| Node | Description |
| --- | --- |
| [Draw Arc](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawArc) | Draws an arc in the viewport, can take in different min and max degrees |
| [Draw Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawBox) | Draws a box in the viewport |
| [Draw Hierarchy](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawHierarchy) | Draws vectors on each bone in the viewport across the entire hierarchy |
| [Draw Line](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawLine) | Draws a line in the viewport given a start and end vector |
| [Draw Line Strip](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawLineStrip) | Draws a line strip in the viewport given any number of points |
| [Draw Pose Cache](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawPoseCache) | Draws vectors on each bone in the viewport across the entire pose |
| [Draw Rectangle](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawRectangle) | Draws a rectangle in the viewport given a transform |
| [Draw Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawTransform) | Given a transform, will draw a point, axis, or a box in the viewport |
| [Draw Transform Array](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawTransformArray) | Given a transform array, will draw a point, axis, or a box in the viewport |
| [End Profiling Timer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EndProfilingTimer) | Ends an existing profiling timer for debugging, used in conjunction with Start Profiling Timer |
| [Start Profiling Timer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StartProfilingTimer) | Starts a profiling timer for debugging, used in conjunction with End Profiling Timer |
| [Visual Debug Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebugVector) | Debug draw parameters for a Point or Vector given a vector |
| [Visual Log Arrow](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogArrow) | Logs arrow - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogBox) | Logs box shape - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Capsule](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogCapsule) | Logs capsule shape - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Circle](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogCircle) | Logs circle - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Cone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogCone) | Logs cone shape - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Cylinder](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogCylinder) | Logs cylinder shape - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Location](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogLocation) | Logs location as sphere with given radius - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Oriented Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogOrientedBox) | Logs oriented box shape - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Segment](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogSegment) | Logs segment - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Sphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogSphere) | Logs sphere shape - recording for Visual Logs has to be enabled to record this data |
| [Visual Log Text](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogText) | Logs simple text string with Visual Logger - recording for Visual Logs has to be enabled to record this data |
| [VisualDebug](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebug) | Debug draw parameters for an Axis given a quaternion Debug draw parameters for an Axis given a transform |

### Deformer Graph

| Node | Description |
| --- | --- |
| [Add Deformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddDeformer) | Adds a deformer to the Skeletal Mesh Component |

### DynamicHierarchy

| Node | Description |
| --- | --- |
| [Add Spaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddSpaces) | Adds available spaces for a given control. This is used for the space switching widget. |
| [Create Parent Relationship](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CreateParentRelationship) | Adds a new parent to an element. |
| [Get Parent Weights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentWeights) | Returns the item's parents' weights |
| [Get Shape Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetShapeSettings) | Retrieves the shape settings of a control |
| [Import Skeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportSkeleton) | Imports all bones (and curves) from the currently assigned skeleton. |
| [Remove Item](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveItem) | Removes an element from the hierarchy Note: This node only runs as part of the construction event. |
| [Reset Hierarchy](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ResetHierarchy) | Removes all elements from the hierarchy Note: This node only runs as part of the construction event. |
| [Set Channel Hosts](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetChannelHosts) | Allows an animation channel to be hosted by multiple controls |
| [Set Default Parent](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetDefaultParent) | Changes the default parent for an item - this removes all other current parents. |
| [Set Parent Weights](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetParentWeights) | Sets the item's parents' weights |
| [Set Shape Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeSettings) | Changes the shape settings of a control Note: This node only runs as part of the construction event. |
| [Spawn Bone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnBone) | Adds a new bone to the hierarchy Note: This node only runs as part of the construction event. |
| [Spawn Integer Animation Channel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel) | Adds a new animation channel to the hierarchy Note: This node only runs as part of the construction event. |
| [Spawn Null](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnNull) | Adds a new null to the hierarchy Note: This node only runs as part of the construction event. |
| [Spawn Socket](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnSocket) | Adds a new socket to the hierarchy Note: This node only runs as part of the construction event. |
| [SpawnAnimationChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnAnimationChannel) | Adds a new animation channel to the hierarchy Note: This node only runs as part of the construction event. |
| [SpawnControl](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnControl) | Adds a new control to the hierarchy Note: This node only runs as part of the construction event. |
| [SpawnScaleAnimationChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnScaleAnimationChannel) | Adds a new animation channel to the hierarchy Note: This node only runs as part of the construction event. |
| [Switch Parent](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SwitchParent) | Switches an element to a new parent. |

### Enum

| Node | Description |
| --- | --- |
| [Cast](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast) | Casts from enum to int |
| [Cast](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast) | Casts from int to enum |

### Events

| Node | Description |
| --- | --- |
| [Backwards Solve](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BackwardsSolve) | Event for driving elements based off the skeleton hierarchy |
| [Connector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Connector) | Event for filtering connection candidates |
| [Construction Event](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ConstructionEvent) | Event to create / configure elements before any other event |
| [Forwards Solve](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForwardsSolve) | Event for driving the skeleton hierarchy with variables and rig elements |
| [Interaction](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Interaction) | Event for executing logic during an interaction |
| [Post Construction](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PostConstruction) | Event to further configure elements. Runs after the Construction Event |
| [Post Forwards Solve](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PostForwardsSolve) | Event always executed after the forward solve |
| [Pre Forwards Solve](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PreForwardsSolve) | Event always executed before the forward solve |
| [User Defined Event](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UserDefinedEvent) | User Defined Event for running custom logic |

### Execution

| Node | Description |
| --- | --- |
| [Branch](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Branch) | Executes either the True or False branch based on the condition |
| [For Loop](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForLoop) | Given a count, execute iteratively until the count is up |
| [Get Interaction](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetInteraction) | Returns true if the Control Rig is being interacted |
| [If](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/If) | Chooses between two values based on a condition |
| [Is Asset Editor Open](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsAssetEditorOpen) | Returns true if a graph is run with its asset editor open. |
| [Select](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Select) | Pick from a list of values based on an integer index |
| [Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Sequence) | Allows for a single execution pulse to trigger a series of events in order. |
| [Switch](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Switch) | Run a branch based on an integer index |

### Hierarchy

| Node | Description |
| --- | --- |
| [Add Multiple Tags](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddMultipleTags) | Sets multiple tags on an item |
| [Add Tag](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddTag) | Sets a single tag on an item |
| [Aim](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Aim) | Aligns the rotation of a primary and secondary axis of an item to a global target. |
| [Aim Math](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AimMath) | Outputs an aligned transform of a primary and secondary axis of an input transform to a world target. |
| [Basic FABRIK](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicFABRIK) | The FABRIK solver can solve N-Bone chains using the Forward and Backward Reaching Inverse Kinematics algorithm. |
| [Basic IK](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIK) | Solves the two bone IK given two bones. Note: This node operates in world space! |
| [Basic IK Positions](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions) | Solves the two bone IK given positions Note: This node operates in world space! |
| [Basic IK Transforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKTransforms) | Solves the two bone IK given transforms Note: This node operates in world space! |
| [CCDIK](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CCDIK) | The CCID solver can solve N-Bone chains using the Cyclic Coordinate Descent Inverse Kinematics algorithm. |
| [Chain Info](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainInfo) | Retrieves various pieces of info about an interpolated transform hierarchy from an rig element item list |
| [Distribute Rotation](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DistributeRotation) | Distributes rotations provided across a array of items. |
| [Filter Items by Tags](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FilterItemsbyTags) | Filters an item array by a list of tags |
| [Find Closest Item](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FindClosestItem) | Returns the item with the closest distance to the provided point in global space. |
| [Find Items with Metadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FindItemswithMetadata) | Returns all items containing a specific set of metadata |
| [Find Items with multiple Tags](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FindItemswithmultipleTags) | Returns all items with a specific set of tags |
| [Find Items with Tag](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FindItemswithTag) | Returns all items with a specific tag |
| [From World](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromWorld) | Converts a transform from world space to rig (global) space Converts a position / location from world space to rig (global) space Converts a rotation from world space to rig (global) space |
| [Full Body IK](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FullBodyIK) | Based on a Position Based solver at core, this node can solve multi chains within a root using multi effectors |
| [Get All](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAll) | Creates an item array for all elements given the filter. |
| [Get Chain](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChain) | Returns a chain between two items |
| [Get Children](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChildren) | Creates an item array based on the direct or recursive children of a provided parent item. |
| [Get Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetComponent) | Gets the component |
| [Get Metadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetMetadata) | Gets some metadata for the provided item |
| [Get Module Metadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleMetadata) | Returns some metadata on a given module |
| [Get Parent](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParent) | Returns the item's parent |
| [Get Parents](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParents) | Returns the item's parents |
| [Get Siblings](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetSiblings) | Returns the item's siblings |
| [Get Tags](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTags) | Returns the metadata tags on an item |
| [Has Metadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMetadata) | Returns true if a given item in the hierarchy has a specific set of metadata |
| [Has Multiple Tags](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMultipleTags) | Returns true if a given item in the hierarchy has all of the provided tags |
| [Has Tag](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HasTag) | Returns true if a given item in the hierarchy has a specific tag stored in the metadata |
| [IK Rig](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IKRig) | Supply an IK Rig asset and provide goal transforms to run IK on the skeleton. |
| [Item](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Item) | The Item node is used to share a specific item across the graph |
| [Multi Effector FABRIK](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MultiEffectorFABRIK) | The FABRIK solver can solve multi chains within a root using multi effectors the Forward and Backward Reaching Inverse Kinematics algorithm. |
| [Project to new Parent](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ProjecttonewParent) | Gets the relative offset between the child and the old parent, then multiplies by new parent's transform. |
| [Remove All Metadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveAllMetadata) | Removes an existing metadata filed from an item |
| [Remove Metadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveMetadata) | Removes an existing metadata filed from an item |
| [Remove Tag](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveTag) | Removes a tag from an item |
| [Send Event](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SendEvent) | SendEvent is used to notify the engine / editor of a change that happend within the Control Rig. |
| [Set Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetComponent) | Set the content of a component |
| [Set Metadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMetadata) | Sets some metadata for the provided item |
| [Set Module Metadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetModuleMetadata) | Sets metadata on the module |
| [Slide Chain](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SlideChain) | Slides an existing chain along itself with control over extrapolation. |
| [Spawn Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnComponent) | Adds a component under an element in the hierarchy |
| [Spherical Pose Reader](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphericalPoseReader) | Outputs a float value between 0-1 based off of the driver item's rotation in a specified region. |
| [Spring IK](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringIK) | The Spring IK solver uses a verlet integrator to perform an IK solve. |
| [To World](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToWorld) | Converts a transform from rig (global) space to world space Converts a position / location from rig (global) space to world space Converts a rotation from rig (global) space to world space |

### Items

| Node | Description |
| --- | --- |
| [Get Parent Indices](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentIndices) | Returns an array of relative parent indices for each item. |
| [Item Exists](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemExists) | Returns true or false if a given item exists |
| [Item Name Search](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemNameSearch) | Creates an item array based on a name search. The name search is case sensitive. |
| [Item Replace](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemReplace) | Replaces the text within the name of the item |
| [Item Type Equals](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemTypeEquals) | Returns true if the two items' types are equal |
| [Item Type Not Equals](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemTypeNotEquals) | Returns true if the two items's types are not equal |
| [Replace Items](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ReplaceItems) | Replaces all names within the item array |

### Items|Collections

| Node | Description |
| --- | --- |
| [Collection from Items](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CollectionfromItems) | Returns a collection provided a specific array of items. |
| [Get Items from Collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetItemsfromCollection) | Returns an array of items provided a collection |

### Live Link

| Node | Description |
| --- | --- |
| [Evaluate Live Link Frame (Animation)](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameAnimation) | Evaluate current Live Link Animation associated with supplied subject |
| [Evaluate Live Link Frame (Transform)](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameTransform) | Evaluate current Live Link Transform associated with supplied subject |
| [Get Basic LiveLink Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBasicLiveLinkData) | Evaluate current Live Link Basic float property data associated with supplied subject |
| [Get Live Link Input Device Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetLiveLinkInputDeviceData) | A node to evaluate a live link input device value |
| [Get Parameter Value By Name](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParameterValueByName) | Get the parameter value with supplied subject frame |
| [Get Transform By Name](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransformByName) | Get the transform value with supplied subject frame |

### Math

| Node | Description |
| --- | --- |
| [Absolute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Absolute) | Returns the absolute (positive) value |
| [Acos](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Acos) | Returns the inverse cosinus value (in radians) of the given value |
| [Add](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Add) | Returns the sum of the two values |
| [ArrayAverage](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ArrayAverage) | Returns the average of the given array |
| [ArraySum](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ArraySum) | Returns the sum of the given array |
| [Asin](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Asin) | Returns the inverse sinus value (in radians) of the given value |
| [Atan](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Atan) | Returns the inverse tangens value (in radians) of the given value |
| [Atan2](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Atan2) | Returns the arctangent of the specified A and B coordinates. |
| [Ceiling](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Ceiling) | Returns the closest higher full number (integer) of the value |
| [Clamp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Clamp) | Clamps the given value within the range provided by minimum and maximum Clamps the given value within the range provided by minimum and maximum for each component |
| [ClampSpatially](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampSpatially) | Clamps a transform's position using a plane collision, cylindric collision or spherical collision. |
| [Cos](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cos) | Returns the cosinus value of the given value (in radians) |
| [Degrees](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Degrees) | Returns the degrees of a given value in radians |
| [Divide](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Divide) | Returns the division of the two values |
| [E](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/E) | Returns E |
| [Exponential](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Exponential) | Computes the base-e exponential of the given value |
| [Floor](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Floor) | Returns the closest lower full number (integer) of the value |
| [Greater](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Greater) | Returns true if the value A is greater than B |
| [GreaterEqual](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GreaterEqual) | Returns true if the value A is greater than or equal to B |
| [HalfPi](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HalfPi) | Returns PI \* 0.5 |
| [Interpolate](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Interpolate) | Linearly interpolates between A and B using the ratio T Performs a spherical interpolation of the quaternions A and B based on the blend value T. |
| [Inverse](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Inverse) | Returns the inverse value Returns the negative value Returns the inverted transform of the input |
| [IsNearlyEqual](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsNearlyEqual) | Returns true if the value A is almost equal to B Returns true if value A is almost equal to B |
| [IsNearlyZero](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsNearlyZero) | Returns true if the value is nearly zero |
| [LawOfCosine](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LawOfCosine) | Computes the angles alpha, beta and gamma (in radians) between the three sides A, B and C |
| [Less](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Less) | Returns true if the value A is less than B |
| [LessEqual](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LessEqual) | Returns true if the value A is less than or equal to B |
| [Make Absolute](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeAbsolute) | Returns the absolute global rotation within a parent's rotation Returns the absolute global transform within a parent's transform Returns the absolute global vector within a parent's vector |
| [Make Relative](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeRelative) | Returns the relative local rotation within a parent's rotation Returns the relative local transform within a parent's transform Returns the relative local vector within a parent's vector |
| [Maximum](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Maximum) | Returns the larger of the two values Returns the larger of the two values each component |
| [Minimum](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Minimum) | Returns the smaller of the two values Returns the smaller of the two values for each component |
| [Mirror](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Mirror) | Mirror a rotation about a central transform. |
| [Modulo](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Modulo) | Returns the modulo of the two values |
| [Multiply](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Multiply) | Returns the product of the two values |
| [Negate](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Negate) | Returns the negative value |
| [Pi](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Pi) | Returns PI |
| [Power](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Power) | Returns the value of A raised to the power of B. |
| [Radians](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Radians) | Returns the radians of a given value in degrees |
| [Remap](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Remap) | Remaps the given value from a source range to a target range. |
| [Rotate Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RotateVector) | Rotates a given vector by the quaternion Rotates a given vector (direction) by the transform |
| [Round](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Round) | Returns the rounded value of the given double number Returns the rounded value of the given float number |
| [Scale](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Scale) | Scales a quaternion's angle Returns the product of the the vector and the float value |
| [Sign](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Sign) | Returns the sign of the value (+1 for >= 0.0, -1 for < 0.0) Returns the sign of the value (+1 for >= 0.f, -1 for < 0.f) Returns the sign of the value (+1 for >= 0, -1 for < 0) Returns the sign of the value (+1 for >= FVector(0.f, 0.f, 0.f), -1 for < 0.f) for each component |
| [Sin](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Sin) | Returns the sinus value of the given value (in radians) |
| [Sqrt](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Sqrt) | Returns the square root of the given value |
| [Subtract](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Subtract) | Returns the difference of the two values |
| [Tan](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Tan) | Returns the tangens value of the given value (in radians) |
| [ToVectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors) | Retrieves the forward, right and up vectors of a quaternion Retrieves the forward, right and up vectors of a transform's quaternion |
| [TwoPi](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TwoPi) | Returns PI \* 2.0 |
| [Unit](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Unit) | Returns the normalized quaternion Returns the normalized value |

### Math|Boolean

| Node | Description |
| --- | --- |
| [And](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/And) | Returns true if both conditions are true |
| [False](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/False) | Returns false |
| [FlipFlop](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FlipFlop) | Returns true and false as a sequence. |
| [Nand](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Nand) | Returns false if both conditions are true |
| [Not](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Not) | Returns true if the condition is false |
| [Once](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Once) | Returns true once the first time this node is hit |
| [Or](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Or) | Returns true if one of the conditions is true |
| [Toggled](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Toggled) | Returns true if the value has changed from the last run |
| [True](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/True) | Returns true |

### Math|Box

| Node | Description |
| --- | --- |
| [Box from Array](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BoxfromArray) | Returns bounding box of the given array of positions |
| [Expand Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ExpandBox) | Expands the size of the box by a given amount |
| [Get Box Center](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBoxCenter) | Returns the center of a bounding box |
| [Get Box Size](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBoxSize) | Returns the size of a bounding box |
| [Get Box Volume](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBoxVolume) | Returns the volume of a given box |
| [Get Distance to Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetDistancetoBox) | Returns the distance to a given box |
| [Is Box Valid](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsBoxValid) | Returns true if the box has any content / is valid |
| [Is Inside Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsInsideBox) | Returns true if a point is inside a given box |
| [Move Box To](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MoveBoxTo) | Moves the center of the box to a new location |
| [Shift Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ShiftBox) | Move the box by a certain amount |
| [Transform Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformBox) | Transforms the box by a given transform |

### Math|Damp|Experimental

| Node | Description |
| --- | --- |
| [Critical Spring Damp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CriticalSpringDamp) | Damps a float using a spring damper Damps a vector using a spring damper Damps a quaternion using a spring damper |
| [Damp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Damp) | Damps a float value using exponential decay damping Damps a vector value using exponential decay damping Damps a quaternion value using exponential decay damping |

### Math|Int

| Node | Description |
| --- | --- |
| [Int to Name](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/InttoName) | Converts an integer to a string Converts an integer to a name |

### Math|Matrix

| Node | Description |
| --- | --- |
| [From Vectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromVectors) | Makes a matrix from its vectors |
| [To Vectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors) | Converts the matrix to its vectors |

### Math|Noise

| Node | Description |
| --- | --- |
| [Noise](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Noise) | Generates a float through a noise fluctuation process between a min and a max through speed Generates a double through a noise fluctuation process between a min and a max through speed Generates a vector through a noise fluctuation process between a min and a max through speed |

### Math|Quaternion

| Node | Description |
| --- | --- |
| [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Axis) | Extracts an axis from a quaternion rotation |
| [Dot](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Dot) | Returns the dot product between two quaternions |
| [From Axis And Angle](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromAxisAndAngle) | Makes a quaternion from an axis and an angle in radians |
| [From Euler](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromEuler) | Makes a quaternion from euler values in degrees |
| [From Two Vectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromTwoVectors) | Makes a quaternion from two vectors, representing the shortest rotation between the two vectors. |
| [Make Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeQuat) | Makes a quaternion from its components |
| [Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RotationOrder) | Enum of possible rotation orders |
| [To Axis And Angle](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToAxisAndAngle) | Retrieves the axis and angle of a quaternion in radians |
| [To Euler](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToEuler) | Retrieves the euler angles in degrees |
| [To Swing & Twist](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToSwing&Twist) | Computes the swing and twist components of a quaternion |

### Math|Random

| Node | Description |
| --- | --- |
| [Random](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Random) | Generates a random float between a min and a max Generates a random vector between a min and a max |

### Math|Ray

| Node | Description |
| --- | --- |
| [GetAt](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAt) | Returns the position on a ray |
| [Intersect Plane](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane) | Returns the closest point intersection of a ray with a plane |
| [Intersect Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectRay) | Returns the closest point intersection of a ray with another ray |
| [Transform Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformRay) | Transforms a ray |

### Math|RBF Interpolation

| Node | Description |
| --- | --- |
| [RBF Quaternion](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFQuaternion) | A RBF interpolator from quaternion to float A RBF interpolator from quaternion to vector A RBF interpolator from quaternion to color A RBF interpolator from quaternion to quaternion A RBF interpolator from quaternion to transform |
| [RBF Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFVector) | A RBF interpolator from vector to float A RBF interpolator from vector to vector A RBF interpolator from vector to color A RBF interpolator from vector to quaternion A RBF interpolator from vector to transform |

### Math|Transform

| Node | Description |
| --- | --- |
| [Make Transform Array Relative](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeTransformArrayRelative) | Treats the provided transforms as a chain with global / local transforms, and projects each transform into the target space. |
| [Transform Array to SRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformArraytoSRT) | Decomposes a Transform Array to its components. |
| [Transform from SRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformfromSRT) | Composes a Transform (and Euler Transform) from its components. |
| [Transform Location](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformLocation) | Multiplies a given vector (location) by the transform |

### Math|Vector

| Node | Description |
| --- | --- |
| [Angle Between](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AngleBetween) | Returns the angle between two vectors in radians |
| [Ceiling](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Ceiling) | Returns the closest higher full number (integer) of the value for each component |
| [ClampLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampLength) | Clamps the length of a given vector between a minimum and maximum |
| [Cross](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cross) | Returns the cross product between two vectors |
| [Distance Between](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DistanceBetween) | Returns the distance from A to B |
| [Distance To Plane](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DistanceToPlane) | Find the point on the plane that is closest to the given point and the distance between them. |
| [Dot](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Dot) | Returns the dot product between two vectors |
| [Floor](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Floor) | Returns the closest lower full number (integer) of the value for each component |
| [Intersect Plane](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane) | Intersects a plane with a vector given a start and direction |
| [Length](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Length) | Returns the length of the vector |
| [Length Squared](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LengthSquared) | Returns the squared length of the vector |
| [Mirror on Normal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MirroronNormal) | Mirror a vector about a normal vector. |
| [Orthogonal](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Orthogonal) | Returns true if the two vectors are orthogonal |
| [Parallel](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Parallel) | Returns true if the two vectors are parallel |
| [Round](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Round) | Returns the closest full number (integer) of the value for each component |
| [SetLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetLength) | Sets the length of a given vector |

### Modules

| Node | Description |
| --- | --- |
| [Discard Matches](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DiscardMatches) | Discards matches during a connector event |
| [Get Array Connection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetArrayConnection) | Returns the resolved array of items of the connector. |
| [Get Candidates](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetCandidates) | Returns the connection candidates for one connector |
| [Get Connection](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetConnection) | Returns the resolved item of the connector. |
| [Get Item Module](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetItemModule) | Returns the namespace of a given item. |
| [Get Items In Module](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetItemsInModule) | Returns all items (based on a filter) in the current module. |
| [Get Module Name](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleName) | Returns the name of the current module instance. |
| [Is In Current Module](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsInCurrentModule) | Returns true if the given item has been created by this module. |
| [Set Default Match](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetDefaultMatch) | Set default match during a connector event |

### Object

| Node | Description |
| --- | --- |
| [Cast](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast) | Casts between object types |

### Pose Cache

| Node | Description |
| --- | --- |
| [Apply Pose Cache](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ApplyPoseCache) | Sets the hierarchy's pose |
| [Create Pose Cache](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CreatePoseCache) | Creates the hierarchy's pose |
| [For Each Pose Cache Element](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEachPoseCacheElement) | Given a pose, execute iteratively across all items in the pose |
| [Get Pose Cache](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCache) | Returns the hierarchy's pose |
| [Get Pose Cache Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheCurve) | Returns the hierarchy's pose curve value |
| [Get Pose Cache Delta](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheDelta) | Compares two pose caches and compares their values. |
| [Get Pose Cache Items](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheItems) | Returns the items in the hierarchy pose |
| [Get Pose Cache Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransform) | Returns the hierarchy's pose transform |
| [Get Pose Cache Transform Array](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransformArray) | Returns an array of transforms from a given hierarchy pose |
| [Is Pose Cache Empty](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsPoseCacheEmpty) | Returns true if the hierarchy pose is empty (has no items) |

### RigLogic

| Node | Description |
| --- | --- |
| [RigLogic](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RigLogic) | RigLogic is used to translate control input curves into bone transforms and values for blend shape and animated map multiplier curves |

### RigPhysics

| Node | Description |
| --- | --- |
| [Calculate Physics Collision](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CalculatePhysicsCollision) | Discards any existing collision data and replaces it with a box based on the joint positions. |
| [Disable Collision Between](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DisableCollisionBetween) | Disables collision between two bodies |
| [Get Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsControlData) | Gets the control data for a physics control |
| [Get Physics Joint Drive Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsJointDriveProperties) | Gets the joint drive for a physics joint component |
| [Get Physics Joint Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsJointProperties) | Gets the joint data for a physics joint component |
| [Get Physics Solver Space Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsSolverSpaceData) | Retrieves the simulation space data that were generated during the simulation step, so the values returned will relate to the previous update if the solver has not yet been stepped. |
| [Import Collision From Physics Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset) | Imports/creates bones from the physics asset and creates collision for them. |
| [Instantiate From Physics Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/InstantiateFromPhysicsAsset) | Creates multiple physics components based on the supplied physics asset. |
| [Instantiate physics](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Instantiatephysics) | Instantiates all the objects in the physics world. |
| [Make Articulation Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationDriveData) | Helper to simplify creation of drive data for a typical articulation (i.e. no linear drive, but with an angular drive) |
| [Make Articulation Joint Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationJointData) | Helper to simplify creation of joint data for a typical articulation (i.e. locked linear motion, but with an angular limit) |
| [Make Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeDriveData) | Helper to simplify creation of drive data |
| [Set Physics Body Collision Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyCollisionMode) | Sets what collision mode is used for this body |
| [Set Physics Body Collision Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyCollisionProperties) | Sets the collision for a physics component body |
| [Set Physics Body Damping](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyDamping) | Sets the linear and angular damping on the body. |
| [Set Physics Body Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyData) | Sets all the data on a body - but in a sparse way so you can decide which parameters get applied. |
| [Set Physics Body Dynamics Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyDynamicsProperties) | Sets the mass etc for a physics component body |
| [Set Physics Body Gravity Multiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyGravityMultiplier) | Sets the multiplier on gravity that should be applied to the body. |
| [Set Physics Body Include In Checks For Reset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyIncludeInChecksForReset) | Sets whether this body should be included in checks for resetting physics on the whole rig |
| [Set Physics Body Kinematic Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyKinematicTarget) | Sets the kinematic target for a body - note that this won't actually make the body kinematic |
| [Set Physics Body Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMaterial) | Applies the material settings to all the collision shapes |
| [Set Physics Body Movement Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMovementMode) | Sets the movement mode for this body. |
| [Set Physics Body Physics Blend Weight](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyPhysicsBlendWeight) | Controls the amount that the simulation is blended back into the target bones. |
| [Set Physics Body Source Bone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodySourceBone) | Sets what bone is used as a source transform for the physics body. |
| [Set Physics Body Target Bone](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyTargetBone) | Sets what bone is targeted by the simulation - i.e. where the simulation output is written to. |
| [Set Physics Body Update Kinematic From Simulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyUpdateKinematicFromSimulation) | If true, then kinematic objects will be written back from simulation to the bones. |
| [Set Physics Control Angular Damping Ratio](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlAngularDampingRatio) | Sets the Angular Damping Ratio of a Physics Control |
| [Set Physics Control Angular Strength](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlAngularStrength) | Sets the Angular Strength of a Physics Control |
| [Set Physics Control Custom Control Point](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlCustomControlPoint) | Sets the custom control point on a control |
| [Set Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlData) | Sets the control data for a physics control |
| [Set Physics Control Data And Multiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlDataAndMultiplier) | Sets the control data and multiplier for a physics control |
| [Set Physics Control Enabled](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlEnabled) | Sets whether a control is enabled |
| [Set Physics Control Linear Damping Ratio](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlLinearDampingRatio) | Sets the Linear Damping Ratio of a Physics Control |
| [Set Physics Control Linear Strength](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlLinearStrength) | Sets the Linear Strength of a Physics Control |
| [Set Physics Control Multiplier](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlMultiplier) | Sets the multipliers for a physics control |
| [Set Physics Control Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsControlTarget) | Sets the target for a physics control |
| [Set Physics Joint Drive Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointDriveProperties) | Sets the joint drive for a physics component body |
| [Set Physics Joint Drive Use Skeletal Animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointDriveUseSkeletalAnimation) | Sets the joint drive for a physics component body |
| [Set Physics Joint Enabled](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointEnabled) | Specifies whether a Physics Joint should be enabled or not |
| [Set Physics Joint Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointProperties) | Sets the joint data for a physics joint component |
| [Set Physics Solver External Velocity](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsSolverExternalVelocity) | Sets the external velocity of the simulation - used for adding wind effects |
| [Set Physics Solver Simulation Space Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsSolverSimulationSpaceSettings) | Sets the solver's simulation space settings |
| [Spawn Physics Body](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody) | Adds a new physics body as a component on the owner element. |
| [Spawn Physics Components](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsComponents) | Adds a set of physics components including the body, joint and controls |
| [Spawn Physics Control](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsControl) | Adds a new physics control as a component on the owner element. |
| [Spawn Physics Joint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsJoint) | Adds a new Physics Joint as a component on the owner element. |
| [Spawn Physics Solver](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsSolver) | Adds a new physics solver as a component on the owner element. |
| [Step Physics Solver](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StepPhysicsSolver) | Steps the specified physics solver |
| [Track Input Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TrackInputPose) | Forces tracking of the input animation (on all physics bodies) for the next N frames |
| [Update Physics Control Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/UpdatePhysicsControlTarget) | Sets the target for a physics control and updates the target velocities based on the previews targets (which will be overwritten) |

### Simulation

| Node | Description |
| --- | --- |
| [Chain Harmonics](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainHarmonics) | Given a root will drive all items underneath in a chain based harmonics spectrum |
| [Harmonics](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Harmonics) | Drives an array of items through a harmonics spectrum |

### Simulation|Accumulate

| Node | Description |
| --- | --- |
| [AccumulateAdd](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateAdd) | Adds a value over time over and over again Adds a vector over time over and over again |
| [Accumulated Time](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulatedTime) | Simulates a time value - can act as a timeline playing back |
| [AccumulateLerp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateLerp) | Interpolates two values over time over and over again Interpolates two vectors over time over and over again Interpolates two quaternions over time over and over again Interpolates two transforms over time over and over again |
| [AccumulateMul](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul) | Multiplies a value over time over and over again Multiplies a vector over time over and over again |
| [AccumulateMul](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul) | Multiplies a quaternion over time over and over again Multiplies a transform over time over and over again |
| [AccumulateRange](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateRange) | Accumulates the min and max values over time |
| [Time Loop](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeLoop) | Simulates a time value - and outputs loop information |

### Simulation|Springs

| Node | Description |
| --- | --- |
| [Spring Interpolate](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterpolate) | Uses a simple spring model to interpolate a quaternion from Current to Target. |
| [SpringInterp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterp) | Uses a simple spring model to interpolate a float from Current to Target. |
| [Verlet (Vector)](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VerletVector) | Simulates a single position over time using Verlet integration. |

### Simulation|Time

| Node | Description |
| --- | --- |
| [AlphaInterp](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AlphaInterp) | Takes in a float value and outputs an accumulated value with a customized scale and clamp Takes in a vector value and outputs an accumulated value with a customized scale and clamp Takes in a quaternion value and outputs an accumulated value with a customized scale and clamp |
| [DeltaFromPrevious](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DeltaFromPrevious) | Computes the difference from the previous value going through the node |
| [KalmanFilter](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/KalmanFilter) | Averages a value over time. |
| [TimeOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeOffset) | Records a value over time and can access the value from the past |

### Splines

| Node | Description |
| --- | --- |
| [Closest Parameter From Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClosestParameterFromSpline) | Retrieves the closest U value from a given Spline and a position |
| [Draw Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawSpline) | Draws the given spline in the viewport |
| [Fit Chain on Spline Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FitChainonSplineCurve) | Fits a given chain to a spline curve. |
| [Fit Spline Curve on Chain](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FitSplineCurveonChain) | Fits a given spline curve to a chain. |
| [Get Length At Param Of Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetLengthAtParamOfSpline) | Retrieves the length from a given Spline |
| [Get Length Of Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetLengthOfSpline) | Retrieves the length from a given Spline |
| [Parameter At Length Percentage](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParameterAtLengthPercentage) | Returns the U parameter of a spline given a length percentage (0.0 - 1.0) |
| [Position From Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/PositionFromSpline) | Retrieves the position from a given Spline and U value |
| [Set Spline Points](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetSplinePoints) | Set the points of a spline, given a spline and an array of positions |
| [Set Spline Transforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetSplineTransforms) | Set the points of a spline, given a spline and an array of transforms |
| [Spline Constraint](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineConstraint) | Fits a given chain to a spline curve. |
| [Spline From Points](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromPoints) | Creates a Spline curve from an array of positions |
| [Spline From Transforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromTransforms) | Creates a Spline curve from an array of transforms |
| [Tangent From Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TangentFromSpline) | Retrieves the tangent from a given Spline and U value |
| [Transform From Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSpline) | Retrieves the transform from a given Spline and U value based on the given primary and secondary axis |
| [Transform From Spline (with UpVector)](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSplinewithUpVector) | Retrieves the transform from a given Spline and U value based on the given Up Vector and Roll |

### Transforms

| Node | Description |
| --- | --- |
| [Get Relative Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetRelativeTransform) | GetRelativeTransform is used to retrieve a single transform from a hierarchy in the space of another transform |
| [Get Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransform) | GetTransform is used to retrieve a single transform from a hierarchy. |
| [Get Transform Array](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransformArray) | GetTransformArray is used to retrieve an array of transforms from the hierarchy. |
| [Modify Transforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ModifyTransforms) | Modify Transforms is used to perform a change in the hierarchy by setting one or more bones' transforms |
| [Offset Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/OffsetTransform) | Offset Transform is used to add an offset to an existing transform in the hierarchy. |
| [Set Relative Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetRelativeTransform) | SetRelativeTransform is used to set a single transform from a hierarchy in the space of another item SetRelativeTranslation is used to set a single translation from a hierarchy in the space of another item SetRelativeRotation is used to set a single rotation from a hierarchy in the space of another item |
| [Set Scale](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetScale) | SetScale is used to set a single scale on hierarchy. |
| [Set Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetTransform) | SetTransform is used to set a single transform on hierarchy. |
| [Set Transform Array](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetTransformArray) | SetTransformArray is used to set an array of transforms on the hierarchy. |

### Uncategorized

| Node | Description |
| --- | --- |
| [Cast](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast) | Turns the given bool into a float value Turns the given bool into an integer value Makes a color from a single float Makes a color from a single double Returns the double cast to an int (this uses floor) Returns the double cast to a float Returns the float cast to an int (this uses floor) Returns the float cast to a double Returns the int cast to a float Returns the int cast to a double Makes a transform from a matrix Makes a matrix from a transform Makes a quaternion from a rotator Retrieves the rotator Makes a quaternion based transform from a euler based transform Retrieves a euler based transform from a quaternion based transform Makes a vector from a single float Makes a vector from a single double Casts the provided item key to its name |
| [From String](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromString) | Converts a string into any value |
| [Get User Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetUserData) | Retrieves a value from a namespaces user data |
| [Print](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Print) | Prints any value to the log |
| [Set Shape Library from User Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeLibraryfromUserData) | Allows to set / add a shape library on the running control rig from user data |
| [Shape Exists](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ShapeExists) | Checks whether or not a shape is available in the rig's shape libraries |
| [To String](https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToString) | Converts any value to string |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-abs.md

# Abs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Abs

> Application Version: 5.7

### Description

Abs (v1)

Absolute value ( |A| )

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | Absolute Positive |
| Type | [FDataflowMathAbsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathAbsNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-add.md

# Add

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Add

> Application Version: 5.7

### Description

Add (v1)

Addition (A + B)

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Scalar |
| Tags | + Addition Plus |
| Type | [FDataflowMathAddNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathAddNode) |

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

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-addcustomcollectionattribute.md

# AddCustomCollectionAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddCustomCollectionAttribute

> Application Version: 5.7

### Description

AddCustomCollectionAttribute (v1)

Adds custom attribute to Collection

Input(s) :
Collection [Intrinsic] - Collection for the custom attribute

Output(s):
Collection [Passthrough] - Collection for the custom attribute

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FAddCustomCollectionAttributeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAddCustomCollectionAttributeDat-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Standard group names | [EStandardGroupNameEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStandardGroupNameEnum) | Dataflow\_EStandardGroupNameEnum\_Transform |
| CustomGroupName | User specified group name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| AttrName | Attribute name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| CustomAttributeType | Attribute type | [ECustomAttributeTypeEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECustomAttributeTypeEnum) | Dataflow\_CustomAttributeType\_Float |
| NumElements | Number of elements for the attribute | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| NumElements | Number of elements for the attribute | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-addkinematicparticles.md

# AddKinematicParticles

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddKinematicParticles

> Application Version: 5.7

### Description

AddKinematicParticles (v1)

Add Kinematic Particles Dataflow Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAddKinematicParticlesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAddKinematicParticlesDataflowNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| SkeletalSelectionMode |  | [ESkeletalSeletionMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/ESkeletalSeletionMode) | Dataflow\_SkeletalSelection\_Single |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMeshIn |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| VertexIndicesIn |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| BoneIndexIn |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TargetIndicesOut |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-addrootproxymeshtoarray.md

# AddRootProxyMeshToArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray

> Application Version: 5.7

### Description

AddRootProxyMeshToArray (v1)

* Add a root proxy object to an array of root proxy mesh
* + (used by geometry collection assets)

Input(s) :
RootProxyMeshes - Root proxy array to add the mesh to

Output(s):
RootProxyMeshes [Passthrough] - Root proxy array to add the mesh to

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FAddRootProxyMeshToArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAddRootProxyMeshToArrayDataflow-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootProxyMeshes | Root proxy array to add the mesh to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |
| RootProxyMesh |  | [FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh) | (Mesh=None,Transform=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),OverrideMaterials=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootProxyMeshes | Root proxy array to add the mesh to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-addsolverdeformer.md

# AddSolverDeformer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer

> Application Version: 5.7

### Description

AddSolverDeformer (v1)

Add a graph deformer to the groom simulation

Input(s) :
PhysicsSolvers - Physics solvers to advance in time
SimulationTime - Delta time to use to advance the solver

Output(s):
PhysicsSolvers [Passthrough] - Physics solvers to advance in time

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsSolver](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsSolver) |
| Category | Physics|Solver |
| Tags | DataflowSimulationTag |
| Type | [FAddSolverDeformerDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsSolver/FAddSolverDeformerDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshDeformer | Graph deformer solver the component is using | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UOptimusDeformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OptimusCore/UOptimusDeformer)> | None |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationTime | Delta time to use to advance the solver | [FDataflowSimulationTime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationTime) | () |
| PhysicsSolvers | Physics solvers to advance in time | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolvers | Physics solvers to advance in time | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-addstitch.md

# AddStitch

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddStitch

> Application Version: 5.7

### Description

AddStitch (v1)

Chaos Cloth Asset Add Stitch Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Add Stitch |
| Type | [FChaosClothAssetAddStitchNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetAddStitchNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MergeToSingleVertexSelection | Set of vertices to stitch together. Can be 2D or 3D vertices. A seam will be created by making a chain of stitches (all vertices will merge to a single 3D vertex). | [FChaosClothAssetConnectableIStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-addtomaterialarray.md

# AddToMaterialArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddToMaterialArray

> Application Version: 5.7

### Description

AddToMaterialArray (v1)

Add material(s) to an array

Input(s) :
MaterialArray - Material array to add to

Output(s):
MaterialArray [Passthrough] - Material array to add to

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Materials |
| Type | [FAddToMaterialInterfaceArrayDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAddToMaterialInterfaceArrayData-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaterialArray | Material array to add to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaterialArray | Material array to add to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-adduvchannel.md

# AddUVChannel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddUVChannel

> Application Version: 5.7

### Description

AddUVChannel (v1)

* Add a new UV channel to the collection
* note that there's a maximum of 8 channels that can be handled by a collection

Input(s) :
Collection [Intrinsic] - Target Collection

Output(s):
Collection [Passthrough] - Target Collection
UVChannel - Index of the added UV channel

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|UV |
| Type | [FAddUVChannelDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAddUVChannelDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DefaultValue | Value to initialize the UV with | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | Index of the added UV channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-addvector.md

# AddVector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddVector

> Application Version: 5.7

### Description

AddVector (v1)

Add two vectors component wise : V = (A + B)

Input(s) :
A - A Vector operand
B - B Vector operand

Output(s):
V - Add result V=A+B

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | + Plus Addition |
| Type | [FDataflowVectorAddNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorAddNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Add result V=A+B | [FDataflowVectorTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-advancephysicssolvers.md

# AdvancePhysicsSolvers

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AdvancePhysicsSolvers

> Application Version: 5.7

### Description

AdvancePhysicsSolvers (v1)

Advance the simulation physics solver in time

Input(s) :
SimulationTime - Delta time to use to advance the solver
PhysicsSolvers - Physics solvers to advance in time

Output(s):
PhysicsSolvers [Passthrough] - Physics solvers to advance in time

### Information

|  |  |
| --- | --- |
| Module | [DataflowSimulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation) |
| Category | Physics|Solver |
| Tags | DataflowSimulationTag |
| Type | [FAdvancePhysicsSolversDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FAdvancePhysicsSolversDataflowNo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationTime | Delta time to use to advance the solver | [FDataflowSimulationTime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationTime) | () |
| PhysicsSolvers | Physics solvers to advance in time | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolvers | Physics solvers to advance in time | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-alignuvmeshnode.md

# AlignUVMeshNode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AlignUVMeshNode

> Application Version: 5.7

### Description

AlignUVMeshNode (v1)
Experimental

Align UVMesh Node

Input(s) :
BaseUVChannelIndex - Base UV channel index in case it differs from the ResizingMesh UV channel index, or -1 to use the same channel.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Align UV Mesh |
| Type | FAlignUVMeshNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bScale |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizingMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| BaseMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| UVChannelIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| BaseUVChannelIndex | Base UV channel index in case it differs from the ResizingMesh UV channel index, or -1 to use the same channel. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizingMesh |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| UVChannelIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-appendcollections.md

# AppendCollections

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendCollections

> Application Version: 5.7

### Description

AppendCollections (v1)

Description for this node

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FAppendCollectionAssetsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAppendCollectionAssetsDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection1 |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Collection2 |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection1 |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| GeometryGroupGuidsOut1 |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| GeometryGroupGuidsOut2 |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-appendmeshestocollection.md

# AppendMeshesToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendMeshesToCollection

> Application Version: 5.7

### Description

AppendMeshesToCollection (v1)

Append Array of Meshes to Collection

Input(s) :
Collection [Intrinsic] - Meshes will be appended to this collection
Meshes - Dynamic Meshes to append
ParentIndex - Index of parent bone for appended meshes. If invalid, meshes will be appended to a root node.

Output(s):
Collection [Passthrough] - Meshes will be appended to this collection
AddedSelection - Selection of added transforms

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FAppendMeshesToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAppendMeshesToCollectionDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Meshes will be appended to this collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Meshes | Dynamic Meshes to append | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |
| ParentIndex | Index of parent bone for appended meshes. If invalid, meshes will be appended to a root node. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Meshes will be appended to this collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| AddedSelection | Selection of added transforms | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-appendpoints.md

# AppendPoints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendPoints

> Application Version: 5.7

### Description

AppendPoints (v1)

Combine two arrays of points into one

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FAppendPointsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAppendPointsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PointsA |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| PointsB |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-appendtetrahedralcollection.md

# AppendTetrahedralCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection

> Application Version: 5.7

### Description

AppendTetrahedralCollection (v2)

Append another Tetrahedral Collection to this collection. All attributes will be appended to the end.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAppendTetrahedralCollectionDataflowNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAppendTetrahedralCollectionData-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bMergeTransform | If checked, non-geometry transforms from CollectionToAppend are merged into Collection by matching transform names. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CollectionToAppend |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| CollectionGeometrySelection |  | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
| CollectionToAppendGeometrySelection |  | [FDataflowGeometrySelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
| CollectionGeometryGroupGuids |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| CollectionToAppendGeometryGroupGuids |  | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-appendtocollectiontransformattribute.md

# AppendToCollectionTransformAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendToCollectionTransformAttribute

> Application Version: 5.7

### Description

AppendToCollectionTransformAttribute (v1)

@todo(deprecate), move to GeometryCollection as AppendCollectionTransformDataflowNode

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAppendToCollectionTransformAttributeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAppendToCollectionTransformAttr-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | ComponentTransform |
| GroupName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | ComponentTransformGroup |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformIn |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-applygeometryscripttocollection.md

# ApplyGeometryScriptToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyGeometryScriptToCollection

> Application Version: 5.7

### Description

ApplyGeometryScriptToCollection (v1)

Apply a Geometry Script Mesh Processors to the geometry of selected transforms in a geometry collection

Input(s) :
Collection [Intrinsic] - Input/Output mesh
TransformSelection - Selected bones will have geometry script processing applied (if they have geometry). If not connected, all geometry will be processed.

Output(s):
Collection [Passthrough] - Input/Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FApplyMeshProcessorToGeometryCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FApplyMeshProces-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bWeldVertices | Whether the processed mesh will have edges at normal/UV/color seams welded so they are treated as one edge during processing. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bPreserveIsolatedVertices | Whether to preserve isolated vertices which aren't used by any triangles. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/Output mesh | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Selected bones will have geometry script processing applied (if they have geometry). If not connected, all geometry will be processed. | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/Output mesh | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-applygeometryscripttomesh.md

# ApplyGeometryScriptToMesh

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyGeometryScriptToMesh

> Application Version: 5.7

### Description

ApplyGeometryScriptToMesh (v1)

Apply a Geometry Script Mesh Processors to an input UDynamicMesh

Input(s) :
Mesh [Intrinsic] - Input/Output mesh

Output(s):
Mesh [Passthrough] - Input/Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FApplyMeshProcessorToMeshDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FApplyMeshProcessorToMeshDataflo-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Input/Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Input/Output mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-applyproxydeformer.md

# ApplyProxyDeformer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyProxyDeformer

> Application Version: 5.7

### Description

ApplyProxyDeformer (v1)

Update the Render Mesh by applying any existing proxy deformer data.
This node can be used to deform the render mesh after the sim mesh has changed after the proxy deformer data was calculated.
It has no effect if there is no existing proxy deformer data, or if the sim or render mesh have not deformed since that data was calculated.

Input(s) :
Collection - Input/output collection

Output(s):
Collection [Passthrough] - Input/output collection

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Apply Proxy Deformer |
| Type | [FChaosClothAssetApplyProxyDeformerNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetApplyProxyDeform-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bIgnoreSkinningBlendWeights | Ignore Skinning Blend Weights (apply proxy deformer to all points) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-applyrbfresizing.md

# ApplyRBFResizing

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing

> Application Version: 5.7

### Description

ApplyRBFResizing (v1)
Experimental

Apply the interpolation data calculated by GenerateRBFResizingWeights to resize a mesh.

Input(s) :
MeshToResize - The mesh being resized
TargetSkeletalMesh - The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh
TargetMesh - The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh
InterpolationData - The pre-calculated base RBF interpolation data.

Output(s):
ResizedMesh - The resulting resized mesh

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Apply RBF Resizing |
| Type | FApplyRBFResizingNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseSkeletalMeshTarget | Use a skeletal mesh for the target mesh (instead of a dynamic mesh) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bInterpolateNormals | Whether or not to interpolate the normals as well as the positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshToResize | The mesh being resized | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| TargetSkeletalMesh | The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| TargetSkeletalMeshLODIndex |  | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| TargetMesh | The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| InterpolationData | The pre-calculated base RBF interpolation data. | [FMeshResizingRBFInterpolationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) | (SampleIndices=,SampleRestPositions=,InterpolationWeights=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizedMesh | The resulting resized mesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-applyresizing.md

# ApplyResizing

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing

> Application Version: 5.7

### Description

ApplyResizing (v1)
Experimental

Apply resizing for a given Target Mesh.

Input(s) :
TargetSkeletalMesh - The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh
SkeletalMeshLODIndex - Source and Target mesh LOD.
InterpolationData - The pre-calculated base RBF interpolation data.
bForceApplyToRenderMesh - Force apply to the render mesh. Otherwise, the sim mesh will be resized if it exists, only resizing the render mesh if no sim mesh data exists.
SourceSkeletalMesh - The source mesh. Used for CustomResizingRegions. Must have matching vertices with TargetMesh
bSkipCustomRegionResizing - Skip applying Custom Region Resizing data.
bSavePreResizedSimPosition3D - Save pre-resized sim 3d vertices for scaling 2D rest length in XPBD anisotropic stretch constraints.
IMPORTANT: Using Save Pre-Resized Sim Position 3D requires the following settings in SimulationStretchConfig node:
Stretch Use 3d Rest Lengths: false
Solver Type: XPBD
Distribution Type: Anisotropic

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Apply Cloth Outfit Resizing |
| Type | [FChaosClothAssetApplyResizingNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetApplyResizingNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TargetSkeletalMesh | The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| InterpolationData | The pre-calculated base RBF interpolation data. | [FMeshResizingRBFInterpolationData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) | (SampleIndices=,SampleRestPositions=,InterpolationWeights=) |
| SkeletalMeshLODIndex | Source and Target mesh LOD. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bForceApplyToRenderMesh | Force apply to the render mesh. Otherwise, the sim mesh will be resized if it exists, only resizing the render mesh if no sim mesh data exists. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SourceSkeletalMesh | The source mesh. Used for CustomResizingRegions. Must have matching vertices with TargetMesh | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| bSkipCustomRegionResizing | Skip applying Custom Region Resizing data. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bSavePreResizedSimPosition3D | Save pre-resized sim 3d vertices for scaling 2D rest length in XPBD anisotropic stretch constraints. IMPORTANT: Using Save Pre-Resized Sim Position 3D requires the following settings in SimulationStretchConfig node: Stretch Use 3d Rest Lengths: false Solver Type: XPBD Distribution Type: Anisotropic | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-arccos.md

# ArcCos

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcCos

> Application Version: 5.7

### Description

ArcCos (v1)

ArcCos(A) returns a value in radians

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Cosine Trigonometry Circle Angle Degrees Radians |
| Type | [FDataflowMathArcCosNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathArcCosNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-arcsin.md

# ArcSin

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcSin

> Application Version: 5.7

### Description

ArcSin (v1)

ArcSin(A) returns a value in radians

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Sine Trigonometry Circle Angle Degrees Radians |
| Type | [FDataflowMathArcSinNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathArcSinNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-arctan.md

# ArcTan

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcTan

> Application Version: 5.7

### Description

ArcTan (v1)

ArcTan(A) returns a value in radians

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Tangent Trigonometry Circle Angle Degrees Radians |
| Type | [FDataflowMathArcTanNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathArcTanNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) | (Value=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowNumericTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-arctan2.md

# ArcTan2

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcTan2

> Application Version: 5.7

### Description

ArcTan2 (v1)

ArcTan2(A, B) returns a value in radians

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Trig |
| Tags | Tangent Trigonometry Circle Angle Degrees Radians |
| Type | [FDataflowMathArcTan2Node](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMathArcTan2Node) |

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

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-assignmaterialtocollection.md

# AssignMaterialToCollection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection

> Application Version: 5.7

### Description

AssignMaterialToCollection (v1)

Assign material to a set of face in a geometry collection

Input(s) :
Collection [Intrinsic] - Collection to assign material to
FaceSelection - Faces that will be set with this material index, if no selection is connected , all faces will be set
MaterialArray [Intrinsic] - Array holding the materials objects
Material - Material to assign to the selection

Output(s):
Collection [Passthrough] - Collection to assign material to
MaterialArray [Passthrough] - Array holding the materials objects
MaterialIndex - Index where the material was set in the array

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Materials |
| Type | [FAssignMaterialInterfaceToCollectionDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAssignMaterialI-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bMergeDuplicateMaterials | If true, detect duplicate in the material array and only add the material in the array if it does not yet exists | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to assign material to | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | Faces that will be set with this material index, if no selection is connected , all faces will be set | [FDataflowFaceSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| MaterialArray | Array holding the materials objects | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| Material | Material to assign to the selection | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to assign material to | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| MaterialArray | Array holding the materials objects | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| MaterialIndex | Index where the material was set in the array | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-attachcurveroots.md

# AttachCurveRoots

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AttachCurveRoots

> Application Version: 5.7

### Description

AttachCurveRoots (v1)
Experimental

Attach the curve roots by setting their kinematic weights to 1.0f

Input(s) :
Collection - Managed array collection to be used to store datas
CurveSelection - Curve selection to focus the geometry transfer spatially

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
KinematicWeightsKey - Vertex kinematic weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FAttachCurveRootsDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FAttachCurveRootsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the geometry transfer spatially | [FDataflowCurveSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| KinematicWeightsKey | Vertex kinematic weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-attachguidesroots.md

# AttachGuidesRoots

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AttachGuidesRoots

> Application Version: 5.7

### Description

AttachGuidesRoots (v1)
Experimental

Attach the guides roots by setting their kinematic weights to 1.0f

Input(s) :
Collection - Managed array collection to be used to store datas

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
KinematicWeightsKey - Point Kinematic weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Type | FAttachGuidesRootsDataflowNode |

### Inputs

| Name | Description | Type | DefaultValue |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

### Outputs

| Name | Description | Type |
| --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |
| KinematicWeightsKey | Point Kinematic weights key to be used in other nodes if necessary | [FCollectionAttributeKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-attribute.md

# Attribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute

> Application Version: 5.7

### Description

Attribute (v2)
Experimental

Create a new attribute for the specified group.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Attribute |
| Type | [FChaosClothAssetAttributeNode\_v2](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetAttributeNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the attribute to create. | [FChaosClothAssetConnectableIOStringValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIOStr-) | (StringValue="") |
| Group | The attribute group. | [FChaosClothAssetNodeAttributeGroup](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetNodeAttributeGro-) | (Name="") |
| Type | The attribute type. | [EChaosClothAssetNodeAttributeType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetNodeAttributeTyp-) | Integer |
| IntValue | Default integer value. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| FloatValue | Default float value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| VectorValue | Default vector value. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Name.StringValue | The value for this property. | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-authorscenecollisioncandidates.md

# AuthorSceneCollisionCandidates

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates

> Application Version: 5.7

### Description

AuthorSceneCollisionCandidates (v1)

Marks mesh vertices as candidates for scene collision raycasts. Each vertex has an associated
bone index to use as the origin of the raycast. The runtime distance between the vertex and the
bone designates the range of the scene query depth.

Input(s) :
VertexIndices - ! Indices to use with environment collisions. If this input is not connected, then all
! indicies are used.
OriginBoneIndex - ! Bone index to use as the world raycast origin. -1 denotes the component transform.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAuthorSceneCollisionCandidates](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAuthorSceneCollisionCandidates) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSurfaceVerticesOnly | ! Restricts vertices to only ones on the surface. All vertices otherwise. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexIndices | ! Indices to use with environment collisions. If this input is not connected, then all ! indicies are used. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| OriginBoneIndex | ! Bone index to use as the world raycast origin. -1 denotes the component transform. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-authortetmetrics.md

# AuthorTetMetrics

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorTetMetrics

> Application Version: 5.7

### Description

AuthorTetMetrics (v1)

Generate quality metrics

Input(s) :
Collection - Passthrough geometry collection. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.

Output(s):
Collection [Passthrough] - Passthrough geometry collection. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCalculateTetMetrics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCalculateTetMetrics) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Passthrough geometry collection. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Passthrough geometry collection. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-dataflow-autocluster.md

# AutoCluster

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster

> Application Version: 5.7

### Description

AutoCluster (v1)

Automatically group pieces of a fractured Collection into a specified number of clusters

Input(s) :
ClusterSites - Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries
ClusterFraction - Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process
SiteSize - Choose the Edge-Size of the cube used to groups bones under a cluster (in cm).
ClusterGridWidth - Choose the number of cluster sites to distribute along the X axis
ClusterGridDepth - Choose the number of cluster sites to distribute along the Y axis
ClusterGridHeight - Choose the number of cluster sites to distribute along the Z axis
MinimumSize - If a cluster has volume less than this value (in cm) cubed, then the auto-cluster process will attempt to merge it into a neighboring cluster.
Collection [Intrinsic] - Fractured GeometryCollection to cluster
TransformSelection [Intrinsic] - Bone selection for the clustering

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FAutoClusterDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAutoClusterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClusterSizeMethod | How to choose the size of the clusters to create | [EClusterSizeMethodEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EClusterSizeMethodEnum) | Dataflow\_ClusterSizeMethod\_ByNumber |
| DriftIterations | For a grid distribution, optionally iteratively recenter the grid points to the center of the cluster geometry (technically: applying K-Means iterations) to balance the shape and distribution of the clusters | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bPreferConvexity | Whether to favor clusters that have a convex shape. (Note: Does not support ByGrid clustering.) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ConcavityTolerance | If > 0, cube root of maximum concave volume to add per cluster (ignoring concavity of individual parts) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AutoCluster | If true, bones will only be added to the same cluster if they are physically connected (either directly, or via other bones in the same cluster) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| EnforceSiteParameters | If true, make sure the site parameters are matched as close as possible ( bEnforceConnectivity can make the number of site larger than the requested input may produce without it ) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AvoidIsolated | If true, prevent the creation of clusters with only a single child. Either by merging into a neighboring cluster, or not creating the cluster. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color |  | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=0.000000,A=1.000000) |
| LineWidthMultiplier |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| CenterColor |  | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| CenterSize |  | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 12.000000 |
| bRandomizeColor | Randomize color per connection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ColorRandomSeed | Random seed | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection for the clustering | [FDataflowTransformSelection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| ClusterSites | Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| ClusterFraction | Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.250000 |
| SiteSize | Choose the Edge-Size of the cube used to groups bones under a cluster (in cm). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ClusterGridWidth | Choose the number of cluster sites to distribute along the X axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ClusterGridDepth | Choose the number of cluster sites to distribute along the Y axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ClusterGridHeight | Choose the number of cluster sites to distribute along the Z axis | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| MinimumSize | If a cluster has volume less than this value (in cm) cubed, then the auto-cluster process will attempt to merge it into a neighboring cluster. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bPreferConvexity | Whether to favor clusters that have a convex shape. (Note: Does not support ByGrid clustering.) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ConcavityTolerance | If > 0, cube root of maximum concave volume to add per cluster (ignoring concavity of individual parts) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to cluster | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

