# Creating Gameplay in Unreal Engine

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-gameplay-in-unreal-engine-for-unity-developers

> Application Version: 5.7

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This page explains Unreal Engine (UE) gameplay programming concepts for Unity users. The explanations below assume you are familiar with Unity C# and want to learn UE C++ and Blueprint.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

The examples below cover some common gameplay programming use cases in Unity C# and how to implement the same functionality in UE.

## Instantiating GameObject / Spawning Actor

In Unity, you use the `Instantiate` function to create new instances of objects. This function takes any `UnityEngine.Object` type (GameObject, MonoBehaviour, etc.), and makes a copy of it.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "public GameObject EnemyPrefab;\npublic Vector3 SpawnPosition;\npublic Quaternion SpawnRotation;\n\nvoid Start()\n{\n\tGameObject NewGO = (GameObject)Instantiate(EnemyPrefab, SpawnPosition, SpawnRotation);\n\tNewGO.name = &quot;MyNewGameObject&quot;;\n}",
  "lines_of_code": 9,
  "id": 35986,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTk4NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--da4325935ca82f657a204d79e3f26f0a9e771b024307548a2247613f42cf43cb",
  "settings": {
    "is_hidden": false
  }
}
```

UE has two different functions to instantiate objects:

- `NewObject` creates new `UObject` types.
- `SpawnActor` spawns `AActor` types.

### UObjects and NewObject

Subclassing `UObject` in UE is similar to subclassing `ScriptableObject` in Unity. These are useful for gameplay classes that do not need to spawn into the world or have attached components as Actors do.

In Unity, if you created a subclass of `ScriptableObject`, you can instantiate it like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "MyScriptableObject NewSO = ScriptableObject.CreateInstance&lt;MyScriptableObject&gt;();",
  "lines_of_code": 1,
  "id": 35987,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTk4NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--a51d17941c42c0f1e181191020bde491df031fc52381742069a082ee4d02d212",
  "settings": {
    "is_hidden": false
  }
}
```

In UE, if you create a subclass of `UObject`, you can instantiate it like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UMyObject* NewObj = NewObject&lt;UMyObject&gt;();",
  "lines_of_code": 1,
  "id": 35988,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTk4OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--7079a0d74541f859ef9634b25b13726328f7ad3d79748f6d229452ccf49afd49",
  "settings": {
    "is_hidden": false
  }
}
```

### AActors and SpawnActor

You can spawn Actors using the `SpawnActor` method on a World (`UWorld` in C++) object. Some UObjects and all Actors provide a `GetWorld` method to get the World object.

In the example below, we use those methods with an existing Actor's spawn parameters to emulate the functionality of Unity's `Instantiate` method.

#### Example

Below is the example AActor subclass, `AMyActor`. The default constructor initializes the `int32` and `USphereComponent*`.

Note the use of the `CreateDefaultSubobject` function. This function creates Components and assigns default properties to them. Sub-objects created with this function act as a default template, so you can modify them in a subclass or Blueprint.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UCLASS()\nclass AMyActor : public AActor\n{\n\tGENERATED_BODY()\n\n\tUPROPERTY()\n\tint32 MyIntProp;\n\n\tUPROPERTY()\n\tUSphereComponent* MyCollisionComp;\n",
  "lines_of_code": 20,
  "id": 35989,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTk4OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--4470401627f57df5b58ba49cf5f21df1b3428c95138a5dd82f6965257d7d5eec",
  "settings": {
    "is_hidden": false
  }
}
```

This creates a clone of a `AMyActor`, including all member variables, UPROPERTYs, and Components.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "AMyActor* CreateCloneOfMyActor(AMyActor* ExistingActor, FVector SpawnLocation, FRotator SpawnRotation)\n{\n\tUWorld* World = ExistingActor-&gt;GetWorld();\n\tFActorSpawnParameters SpawnParams;\n\tSpawnParams.Template = ExistingActor;\n\tWorld-&gt;SpawnActor&lt;AMyActor&gt;(ExistingActor-&gt;GetClass(), SpawnLocation, SpawnRotation, SpawnParams);\n}",
  "lines_of_code": 7,
  "id": 35990,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTk5MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--d3444db01fd17f983d5dd7291e6e0cd3be0a113146ae01c01272308fef67524c",
  "settings": {
    "is_hidden": false
  }
}
```

## Casting from One Type to Another

In this case, we get a component we know we have, then cast it to a specific type and conditionally do something.

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "Collider collider = gameObject.GetComponent&lt;Collider&gt;;\nSphereCollider sphereCollider = collider as SphereCollider;\nif (sphereCollider != null)\n{\n\t\t// ...\n}",
  "lines_of_code": 6,
  "id": 35991,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTk5MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--12df60f49b815fb484888a32f65784b3258be06208e351918e26d73d48497fae",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UPrimitiveComponent* Primitive = MyActor-&gt;GetComponentByClass(UPrimitiveComponent::StaticClass());\nUSphereComponent* SphereCollider = Cast&lt;USphereComponent&gt;(Primitive);\nif (SphereCollider != nullptr)\n{\n\t\t// ...\n}",
  "lines_of_code": 6,
  "id": 35992,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTk5MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--be793606f5f4df70886162daec47ba4afb63836d786462b261ae46238f11ea3c",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

You can cast in Blueprint by using a **Cast to** node. For more detailed information, see [Casting Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/casting-quick-start-guide-in-unreal-engine).

## Destroying GameObject / Actor

| **Unity C#** | **UE C++** | **Blueprint** ![Image](https://dev.epicgames.com/community/api/documentation/image/fb7488ae-917d-4d70-815c-670b453f3aa1) |
| --- | --- | --- |

## Destroying GameObject / Actor (with 1-Second Delay)

| **Unity C#** | **UE C++** | **Blueprint** ![Image](https://dev.epicgames.com/community/api/documentation/image/01009987-7e14-4e3c-aeb8-9b7b6440cd81) |
| --- | --- | --- |

## Disabling GameObjects / Actors

| **Unity C#** | **UE C++** | **Blueprint** ![Image](https://dev.epicgames.com/community/api/documentation/image/689707f7-b239-4c44-b508-176cc366d5ba) |
| --- | --- | --- |

## Accessing the GameObject / Actor from a Component

| **Unity C#** | **UE C++** | **Blueprint** ![Image](https://dev.epicgames.com/community/api/documentation/image/71a31ef3-bbac-4c45-a80c-47e6dd51d0da) |
| --- | --- | --- |

## Accessing a Component from the GameObject / Actor

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "MyComponent MyComp = gameObject.GetComponent&lt;MyComponent&gt;();",
  "lines_of_code": 1,
  "id": 36001,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--aa065b680dc320a7608faf92b0c81f8aacfc41ae161bb65953d4173810a3663f",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UMyComponent* MyComp = MyActor-&gt;FindComponentByClass&lt;UMyComponent&gt;();",
  "lines_of_code": 1,
  "id": 36002,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--66ee1fcf2deec3acfe4862853aa522ba52964bc4e36a39ba67726a5b368c1f31",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/c5db4405-f52e-4d87-ac7c-042b50f408b7)

## Finding GameObjects / Actors

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "// Find GameObject by name\nGameObject MyGO = GameObject.Find(&quot;MyNamedGameObject&quot;);\n\n// Find Objects by type\nMyComponent[] Components = Object.FindObjectsOfType(typeof(MyComponent)) as MyComponent[];\nforeach (MyComponent Component in Components)\n{\n\t\t// ...\n}\n\n",
  "lines_of_code": 16,
  "id": 36003,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--60a82fed869d4a733a527bb155fcc12572dc1af3a3206780621afc1783e9c41b",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Find UObjects by type\nfor (TObjectIterator&lt;UMyObject&gt; It; It; ++it)\n{\n\tUMyObject* MyObject = *It;\n\t// ...\n}\n\n// Find Actor by name (also works on UObjects)\nAActor* MyActor = FindObject&lt;AActor&gt;(nullptr, TEXT(&quot;MyNamedActor&quot;));\n\n",
  "lines_of_code": 26,
  "id": 36004,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--8a753d60dcf57a658576a8b17ec4249d90f3a2dcb71997587a5f1637e50e907d",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/68b9a54e-e28e-493a-9752-459ccf84a1f8)

![Image](https://dev.epicgames.com/community/api/documentation/image/9b61fae8-2c7b-44ee-b8f4-177ec88d94b1)

## Adding Tags to GameObjects / Actors

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "MyGameObject.tag = &quot;MyTag&quot;;",
  "lines_of_code": 1,
  "id": 36005,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--6ca1d2f18661f8832e9aa2873a278dafc40c7bb8d6b34504354d8ccb5c926eaa",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Actors can have multiple tags\nMyActor.Tags.AddUnique(TEXT(&quot;MyTag&quot;));",
  "lines_of_code": 2,
  "id": 36006,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--15b419be4f7c539abe45af85550277d2fcce6ecb1d3cb834d41c8320e91d03ae",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/26918efc-0d14-4aec-b8df-d9958cb268c3)

## Adding Tags to MonoBehaviours / ActorComponents

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "// This changes the tag on the GameObject it is attached to\nMyComponent.tag = &quot;MyTag&quot;;",
  "lines_of_code": 2,
  "id": 36007,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--12f6e7381b92e23e9d64626a50c57b763589a8e5421ff0b7bec54bb3fb64b565",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Components have their own array of tags\nMyComponent.ComponentTags.AddUnique(TEXT(&quot;MyTag&quot;));",
  "lines_of_code": 2,
  "id": 36008,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--e42b327b92218461954c38ea258284ff6a531361050ee7ea05974a019682fe3f",
  "settings": {
    "is_hidden": false
  }
}
```

## Comparing Tags on GameObjects / Actors and MonoBehaviours / ActorComponents

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "if (MyGameObject.CompareTag(&quot;MyTag&quot;))\n{\n\t// ...\n}\n\n// Checks the tag on the GameObject it is attached to\nif (MyComponent.CompareTag(&quot;MyTag&quot;))\n{\n\t// ...\n}",
  "lines_of_code": 10,
  "id": 36009,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAwOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--697bf2006b7d99655f9d7304f34caef4623f7c3d6ca864bcf5182a3b5a82e200",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Checks if an Actor has this tag\nif (MyActor-&gt;ActorHasTag(FName(TEXT(&quot;MyTag&quot;))))\n{\n\t// ...\n}",
  "lines_of_code": 5,
  "id": 36010,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--bb3be0992e94789f862026421be5346b48bb98e4391c30e9ff1a6c59ca720fec",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/4384de8d-5bc9-4875-80df-4ff4d3911c1a)

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Checks if an ActorComponent has this tag\nif (MyComponent-&gt;ComponentHasTag(FName(TEXT(&quot;MyTag&quot;))))\n{\n\t// ...\n}",
  "lines_of_code": 5,
  "id": 36011,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--0ffd4b4b6e0b7c73f6cf1947a6cdbddd041a35fe5d644baa2e59b3707095efd9",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/0c722b70-f411-4419-8998-660157690933)

## Physics: RigidBody vs. Primitive Component

In Unity, to give a GameObject physics characteristics, you attach a RigidBody component.

In UE, any Primitive Component (`UPrimitiveComponent` in C++) can represent a physical object. Some common Primitive Components are:

- Shape Components (`USphereComponent`, `UCapsuleComponent`, etc.)
- Static Mesh Components
- Skeletal Mesh Components

Unlike Unity, which separates the responsibilities of collision and visualizations into separate components, UE combines the concepts of "potentially physical" and "potentially visible" into a single Primitive Component. Any Component with geometry in the world that can be rendered or physically interacted with is a subclass of `UPrimitiveComponent`.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Collision Channels are the UE equivalent of layers in Unity. To learn more, refer to <a href=\"https://www.unrealengine.com/en-US/blog/collision-filtering\">Collision Filtering</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

### RayCast vs. RayTrace

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "GameObject FindGOCameraIsLookingAt()\n{\n\tVector3 Start = Camera.main.transform.position;\n\tVector3 Direction = Camera.main.transform.forward;\n\tfloat Distance = 100.0f;\n\tint LayerBitMask = 1 &lt;&lt; LayerMask.NameToLayer(&quot;Pawn&quot;);\n\n\tRaycastHit Hit;\n\tbool bHit = Physics.Raycast(Start, Direction, out Hit, Distance, LayerBitMask);\n\n",
  "lines_of_code": 17,
  "id": 36012,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--ea11b01df8891504dba2951dca8e9699c163d0432df567064f74bbc59eaf62ca",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "APawn* AMyPlayerController::FindPawnCameraIsLookingAt()\n{\n\t// You can use this to customize various properties about the trace\n\tFCollisionQueryParams Params;\n\t// Ignore the player&#39;s pawn\n\tParams.AddIgnoredActor(GetPawn());\n\n\t// The hit result gets populated by the line trace\n\tFHitResult Hit;\n\n",
  "lines_of_code": 23,
  "id": 36013,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--882b646fa0fc4a00516541b0b510b6e88fe7ae81832b3b25f34423ad65589b43",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/c5c26aa0-10b0-4e48-8220-5c29bd8b5d11)

_Click the image for full size._

### Trigger Volumes

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "public class MyComponent : MonoBehaviour\n{\n\tvoid Start()\n\t{\n\t\tcollider.isTrigger = true;\n\t}\n\tvoid OnTriggerEnter(Collider Other)\n\t{\n\t\t// ...\n\t}\n",
  "lines_of_code": 15,
  "id": 36014,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--1f7642935f72dfb6c65c0b8a17f7faf8e5e8a6f8e95c553e35ef59c00b9915f1",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UCLASS()\nclass AMyActor : public AActor\n{\n\tGENERATED_BODY()\n\n\t// My trigger component\n\tUPROPERTY()\n\tUPrimitiveComponent* Trigger;\n\n\tAMyActor()\n",
  "lines_of_code": 25,
  "id": 36015,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--ad2c43cdf74675ede6c0ad3573d8302d5b8b54376421709ee3cb49529c7f8d52",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/b9ddaf52-9b15-48d4-bc8b-3670d4e31452)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To learn more about setting up collision responses, see <a data-document-id=\"3229680\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-in-unreal-engine\">Collision</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

### Kinematic Rigidbodies

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "public class MyComponent : MonoBehaviour\n{\n\tvoid Start()\n\t{\n\t\trigidbody.isKinematic = true;\n\t\trigidbody.velocity = transform.forward * 10.0f;\n\t}\n}",
  "lines_of_code": 8,
  "id": 36016,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--7d24cfa1d15dd3f22c41a502a4c0473f9b93124484ce95cf0a86f6793f93ae44",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UCLASS()\nclass AMyActor : public AActor\n{\n\tGENERATED_BODY()\n\n\tUPROPERTY()\n\tUPrimitiveComponent* PhysicalComp;\n\n\tAMyActor()\n\t{\n",
  "lines_of_code": 15,
  "id": 36017,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--76687fe10485f4bf0ce5200a90d277d5c3bf3c1a14b3613d53f8ad5ee0f731e3",
  "settings": {
    "is_hidden": false
  }
}
```

## Input Events

#### Unity

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "public class MyPlayerController : MonoBehaviour\n{\n\tvoid Update()\n\t{\n\t\tif (Input.GetButtonDown(&quot;Fire&quot;))\n\t\t{\n\t\t\t// ...\n\t\t}\n\t\tfloat Horiz = Input.GetAxis(&quot;Horizontal&quot;);\n\t\tfloat Vert = Input.GetAxis(&quot;Vertical&quot;);\n",
  "lines_of_code": 13,
  "id": 36018,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--e723926478c2eced2630db40d72feb049cbf2f5d95d669ea3b6abbe75293ff9e",
  "settings": {
    "is_hidden": false
  }
}
```

#### UE C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UCLASS()\nclass AMyPlayerController : public APlayerController\n{\n\tGENERATED_BODY()\n\n\tvoid SetupInputComponent()\n\t{\n\t\tSuper::SetupInputComponent();\n\n\t\tInputComponent-&gt;BindAction(&quot;Fire&quot;, IE_Pressed, this, &amp;AMyPlayerController::HandleFireInputEvent);\n",
  "lines_of_code": 18,
  "id": 36019,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNjAxOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE0OjA4KzAwOjAwIn0=--e041a77672fc621bf549bf2cb53613ab0b2b03474f24e64f07c6c2bb4b067804",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/15504e00-984c-41e9-9db8-d1c5414b03d1)

This is what your input properties in your Project Settings might look like:

![Input settings in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/7b31af9c-d644-47ba-94d0-a6fa414d6d49)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To learn more about how to set up input for your UE project, see <a data-document-id=\"3229155\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine\">Input</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Further Reading

For more information related to the concepts above, we recommend that you review the following sections:

- [Gameplay Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) - Covers core game systems such as game mode, player state, controllers, pawns, cameras, and more.
- [Gameplay Architecture](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-cpp-in-unreal-engine) - Reference for creating and implementing gameplay classes.
- [Gameplay Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-tutorials-for-unreal-engine) - Tutorials for recreating common gameplay elements.
