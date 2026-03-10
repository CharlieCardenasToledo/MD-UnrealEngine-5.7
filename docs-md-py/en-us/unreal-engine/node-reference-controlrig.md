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
