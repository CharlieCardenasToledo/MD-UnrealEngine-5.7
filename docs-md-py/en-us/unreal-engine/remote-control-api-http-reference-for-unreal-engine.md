# Remote Control API HTTP Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-api-http-reference-for-unreal-engine

> Application Version: 5.7

This page describes the HTTP endpoints offered by the Remote Control API, and details the format of the message body you need to include when you call each endpoint.

## GET remote/info

Use this endpoint to see all the HTTP routes available in the Remote Control API. The call returns a JSON payload with all the available HTTP routes and their descriptions.

### Example

Send the request with an empty request body. A successful request returns a 200 status with the following response body:

```
	{
		"HttpRoutes": [
			{
				"Path": "/remote/info",
				"Verb": "Get",
				"Description": "Get information about different routes available on this API."
			},
			{
				"Path": "/remote",
				"Verb": "Options",
				"Description": "Allows cross-origin http requests to the API."
			},
			{
				"Path": "/remote/batch",
				"Verb": "Put",
				"Description": "Allows batching multiple calls into one request."
			}
			...
		]
	}
```

## PUT remote/object/call

Use this endpoint to call a function exposed by a specified `UObject` that is currently in memory in the Editor: typically an Actor in the current Level or an Asset in your Project.

You can call any function that is callable from Blueprint. This includes any function defined in C++ with the `BlueprintCallable` specifier, or any function that is defined and implemented entirely in Blueprint.

When you call this endpoint, you must pass a JSON payload with the following properties:

| Property | Description |
| --- | --- |
| `objectPath` | The path that uniquely identifies the `UObject` you want to interact with. For more information on finding this path, see [About UObject Paths](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-api-http-reference-for-unreal-engine#aboutuobjectpaths) below. |
| `functionName` | The name of the function you want to call from the specified `UObject`. If your function is defined in C++, its original name may not match the display name shown in Blueprint. In this case, use the function name defined in C++. |
| `parameters` | An object that defines the parameters you want to pass to the function.   * The name of each property in this object should be the name of a parameter accepted by the function you call.  ``` 	If your function is defined in C++, the original parameter name may not match the value you see in the Blueprint Editor. In this case, use the paramter name defined in C++. For example, in the code below, the second parameter needs to be specified as `bSweep` to match its C++ definition, although it is exposed in the equivalent Blueprint node as **Sweep**. ```  * The value of the property may be any simple value such as a number or a Boolean value. Or, if the function requires you to pass an object, you can provide a JSON object that encapsulates the properties of that object. The Remote Control system will use the values you provide to attempt to create a new object of the necessary type. For example, in the code below, the `NewLocation` is automatically used to create a new Vector.   You don't have to include a property in this object for every parameter the function accepts. For any parameter that you omit, the Web Remote Control system will construct a default object of the appropriate type. |
| `generateTransaction` | Defines whether or not the Editor should record this function call in the Project's transaction history. Setting this property to `true` has the following effects:   * Any changes made by the function will be undoable. The Editor records an entry in the Project's **Undo History** panel for this function call. A user working in the Unreal Editor can then roll back the effect of the change. This entry is always under the name **Remote Call Transaction Wrap**, regardless of the function you call: Remote transactions listed in the Undo History * If you're in a [Multi-User Editing](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine) session, the change will be replicated to other connected users. |

The call returns a JSON payload that contains the return value of the function called, along with any other output parameters specified in the function's definition.

### Example

Request body:

```
	{
		"objectPath" : "/Game/ThirdPersonBP/Maps/ThirdPersonExampleMap.ThirdPersonExampleMap:PersistentLevel.CubeMesh_5",
		"functionName" : "SetActorLocation",
		"parameters" : {
			"NewLocation" : {"X" : 100, "Y" : 0, "Z" : 30},   // These values are used to create a new Vector
			"bSweep" : true
		},
		"generateTransaction" : true
	}
```

A successful request gives a `200` status with the following response body:

```
	{
		"SweepHitResult":{
			"bBlockingHit":true,
			"bStartPenetrating":false,
			"FaceIndex":-1,
			"Time":0.338644,
			"Distance":170.822,
			"Location":{ "X":100, "Y":0, "Z":429.178 },
			"ImpactPoint":{ "X":169, "Y":30, "Z":354 },
			"Normal":{ "X":-1.51964e-11, "Y":4.01851e-8, "Z":1 },
			"ImpactNormal":{ "X":-1.51964e-11, "Y":4.01851e-8, "Z":1 },
			"TraceStart":{ "X":100, "Y":0, "Z":600 },
			"TraceEnd":{ "X":100, "Y":0, "Z":100 },
			"PenetrationDepth":0,
			"Item":-1,
			"PhysMaterial":"",
			"Actor":"/Game/ThirdPersonBP/Maps/ThirdPersonExampleMap.ThirdPersonExampleMap:PersistentLevel.Bump_StaticMesh",
			"Component":"/Game/ThirdPersonBP/Maps/ThirdPersonExampleMap.ThirdPersonExampleMap:PersistentLevel.Bump_StaticMesh.StaticMeshComponent0",
			"BoneName":"None",
			"MyBoneName":"None"
		},
		"ReturnValue":true
	}
```

In this case, the `SweepHitResult` is included in the return value because the original definition of the `SetActorLocation()` function in the `Engine/Source/Runtime/Engine/Classes/GameFramework/Actor.h` file defines it as an output parameter: that is, a non-const reference to a data value that is produced by the function call.

## PUT remote/object/property

Use this endpoint to access property values exposed by a specified UObject currently in memory in the Editor: typically an Actor or an Asset.

If the UObject you are accessing is an instance of a C++ class, this includes any class members defined in C++ as properties that are accessible to Blueprint, subject to the restrictions below.

If the UObject you are accessing is an instance of a Blueprint class, this includes any Blueprint variables owned by that class, subject to the restrictions below.

This endpoint can only access properties that meet certain criteria:

* The property must be defined as `public`. It may not be `private` or `protected`.
* It must not have any `BlueprintGetter` or `BlueprintSetter` functions defined. If it does, you must use those functions with the `remote/object/call` endpoint described above instead of trying to read or write the values directly using the `remote/object/property` endpoint.
* If you are accessing the object in the Editor, the property must be set as `EditAnywhere`. In order to modify the value, the property must not be set as `EditConst`.
* If you are accessing an object in `-game` mode or Play In Editor (PIE) mode, the property must be set as `BlueprintVisible`. In order to modify the value, the property must not be set as `BlueprintReadOnly`.

Depending on the way you construct your request message, you can:

* Request all available properties exposed by the object, along with their current values.
* Request the value of any property that offers at least read access.
* Set the value of any properties that offer write access.

When you call this endpoint, you must pass a JSON payload with the following properties:

| Property | Description |
| --- | --- |
| `objectPath` | The path that uniquely identifies the `UObject` you want to interact with. For more information on finding this path, see [About UObject Paths](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-api-http-reference-for-unreal-engine#aboutuobjectpaths) below. |
| `propertyName` | The name of the property you want to read or modify. If you omit this property in a call with `READ_ACCESS`, the response will list all readable properties available on the specified `UObject`. |
| `access` | Defines the kind of access request you are making for the property. This can be any of the following values:   * `READ_ACCESS` specifies that you are making a request for the current value of a property, or for all properties on the specified `UObject`. * `WRITE_ACCESS` specifies that you want to set a new value for one or more properties, which you define in the `propertyValue` object. * `WRITE_TRANSACTION_ACCESS` is the same as `WRITE_ACCESS`, but records the property value change in the Project's transaction history. This is similar to the `generateTransaction` property of the `remote/object/call` endpoint. It has the following effects:   + The Editor handles the property modification exactly as if it had been done in the **Details** panel of the Unreal Editor. This may invoke additional code inside the Editor to handle pre-change and post-change events linked to that property.   + If you're in a [Multi-User Editing](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine) session, the change will be replicated to other connected users.   + This option makes the change undoable. If you set this property to `true`, the Editor records an entry in the Project's **Undo History** panel for this property change. A user working in the Unreal Editor can then roll back the effect of the change. This entry is always under the name **Remote Set Object Property**: Remote Set Object Property |
| `propertyValue` | When you make a request with `WRITE_ACCESS` or `WRITE_TRANSACTION_ACCESS`, you use this object to specify the properties you want to modify, and the new value you want to set for each of those properties.  This must be a JSON object in which the name of each field matches the name of a writeable property on the specified `UObject`, and the value of each field is the new value that you want to set for that property. |

The call returns a JSON payload that contains the information you requested, or the result of your write request.

### Examples

#### Reading all Properties

Request body:

```
	{
		"objectPath" : "/Game/ThirdPersonBP/Maps/ThirdPersonExampleMap.ThirdPersonExampleMap:PersistentLevel.CubeMesh_5",
		"access" : "READ_ACCESS"
	}
```

A successful request gives a `200` status with the following response body:

```
	{
		"bStaticMeshReplicateMovement": false,
		"NavigationGeometryGatheringMode": "Default",
		"PrimaryActorTick": {
			"TickGroup": "TG_PrePhysics",
			"EndTickGroup": "TG_PrePhysics",
			"bTickEvenWhenPaused": false,
			"bCanEverTick": false,
			"bStartWithTickEnabled": true,
			"bAllowTickOnDedicatedServer": true,
			"TickInterval": 0
		},
		"bHidden": false,
		"bOnlyRelevantToOwner": false,
		"bAlwaysRelevant": false,
		"bReplicateMovement": false,
		"bNetLoadOnClient": true,
		"bNetUseOwnerRelevancy": false,
		"bRelevantForLevelBounds": true,
		"bReplayRewindable": false,
		"bAllowTickBeforeBeginPlay": false,
		"bBlockInput": false,
		"bCanBeDamaged": false,
		"bFindCameraComponentWhenViewTarget": true,
		"bGenerateOverlapEventsDuringLevelStreaming": false,
		"bIgnoresOriginShifting": false,
		"bEnableAutoLODGeneration": true,
		"bIsEditorOnlyActor": false,
		"ReplicatedMovement": {
			"LinearVelocity": { "X": 0, "Y": 0, "Z": 0 },
			"AngularVelocity": { "X": 0, "Y": 0, "Z": 0 },
			"Location": { "X": 0, "Y": 0, "Z": 0 },
			"Rotation": { "Pitch": 0, "Yaw": 0, "Roll": 0 },
			"bSimulatedPhysicSleep": false,
			"bRepPhysics": false,
			"LocationQuantizationLevel": "RoundWholeNumber",
			"VelocityQuantizationLevel": "RoundWholeNumber",
			"RotationQuantizationLevel": "ByteComponents"
		},
		"InitialLifeSpan": 0,
		"NetDormancy": "DORM_Awake",
		"SpawnCollisionHandlingMethod": "AlwaysSpawn",
		"AutoReceiveInput": "Disabled",
		"InputPriority": 0,
		"NetCullDistanceSquared": 2.25e+08,
		"NetUpdateFrequency": 100,
		"MinNetUpdateFrequency": 2,
		"NetPriority": 1,
		"SpriteScale": 1,
		"Tags": []
	}
```

#### Reading a Single Property

Request body:

```
	{
		"objectPath" : "/Game/ThirdPersonBP/Maps/ThirdPersonExampleMap.ThirdPersonExampleMap:PersistentLevel.CubeMesh_5.StaticMeshComponent0",
		"propertyName" : "StreamingDistanceMultiplier",
		"access" : "READ_ACCESS",
	}
```

A successful request gives a `200` status with the following response body:

```
	{
		"StreamingDistanceMultiplier": 1
	}
```

#### Writing Properties

Request body:

```
	{
		"objectPath" : "/Game/ThirdPersonBP/Maps/ThirdPersonExampleMap.ThirdPersonExampleMap:PersistentLevel.CubeMesh_5.StaticMeshComponent0",
		"access" : "WRITE_ACCESS",
		"propertyName" : "StreamingDistanceMultiplier",
		"propertyValue" : {
			"StreamingDistanceMultiplier" : 2
		}
	}
```

A successful request gives a `200` status with an empty response body.

## PUT remote/object/thumbnail

Use this endpoint to retrieve the thumbnail image of an Asset in the **Content Browser**. The call returns a JSON payload that contains the thumbnail.

### Example

Request body:

```
	{
		"objectPath" : "/Game/Mannequin/Animations/ThirdPersonJump_Start.ThirdPersonJump_Start"
	}
```

A successful request returns a 200 status with the thumbnail image in the response body:

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dd24a586-0ac4-4e03-8e20-d83cee03b97c/image_0.png)
