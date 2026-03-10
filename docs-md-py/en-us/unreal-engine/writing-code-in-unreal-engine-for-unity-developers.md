# Writing Code in Unreal Engine

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers

> Application Version: 5.7

## Setup

### C++

To write C++ code in Unreal Engine (UE), download [Visual Studio](https://visualstudio.microsoft.com/downloads/) on Windows, or [install Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12) on macOS. When you create a new C++ project, UE will automatically create Visual Studio project files for you.

There are two ways to access Visual Studio from your UE project:

- In the **Content Browser**, **double-click** a C++ class to open it in Visual Studio.
- From the main menu, go to **Tools** **>** **Open Visual Studio**. This option only appears if your project contains at least one C++ class.

A critical difference in UE: You will sometimes have to manually refresh your Visual Studio project files (for example, after downloading a new version of UE, or when manually making changes to source file locations on disk.) You can do this in two ways:

- From UE's main menu, go to **Tools > Refresh Visual Studio Project**.
- **Right-click** the **.uproject** file in your project's directory and select **Generate Visual Studio project files**.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "See <a data-document-id=\"3228543\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-your-development-environment-for-cplusplus-in-unreal-engine\">Development Setup</a> for more detailed information.",
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

### Blueprint

You only need UE to use Blueprint scripting. All the features you need are built into Unreal Editor.

## Writing Event Functions

If you previously worked with MonoBehaviors, you are familiar with the `Start`, `Update`, and `OnDestroy` methods. Below is a comparison between a Unity behavior and its equivalent for UE: Actors and Components.

In Unity, you might have a simple component that looks like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "c_sharp",
  "title": "",
  "code_preview": "public class MyComponent : MonoBehaviour\n{\n\tvoid Start() {}\n\tvoid OnDestroy() {}\n\tvoid Update() {}\n}",
  "lines_of_code": 6,
  "id": 70931,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3MDkzMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjIyOjU0KzAwOjAwIn0=--8e7dfee697dc3acf9d2b51ea6b7cce5114556463ccf8e132add7ff8a4b35150c",
  "settings": {
    "is_hidden": false
  }
}
```

### AActor

In UE, you can write code on the Actor itself rather than only coding new component types.

Additionally, Actors have similar methods to Unity's `Start`, `OnDestroy`, and `Update` methods.

#### C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UCLASS()\nclass AMyActor : public AActor\n{\n\tGENERATED_BODY()\n\n\t// Called at start of game.\n\tvoid BeginPlay();\n\n\t// Called when destroyed.\n\tvoid EndPlay(const EEndPlayReason::Type EndPlayReason);\n",
  "lines_of_code": 14,
  "id": 70932,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3MDkzMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjIyOjU0KzAwOjAwIn0=--b9197e1cca65de4843f39a1bde2e1d20830c7ae568ae4d35bae8085a7910382f",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/90216cf5-0993-428e-b4d0-80903e1899f3)

### UActorComponent

Components in UE are conceptually similar to MonoBehaviors but contain different methods.

#### C++

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UCLASS()\nclass UMyComponent : public UActorComponent\n{\n\tGENERATED_BODY()\n\n\t// Called after the owning Actor was created\n\tvoid InitializeComponent();\n\n\t// Called when the component or the owning Actor is being destroyed\n\tvoid UninitializeComponent();\n",
  "lines_of_code": 14,
  "id": 70933,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3MDkzMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjIyOjU0KzAwOjAwIn0=--5431de3dd742814afaca9fe9a802c7aef5499ba46cd4f5de78f955e1bad98da5",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint

![Image](https://dev.epicgames.com/community/api/documentation/image/9d35c8a7-d6fe-4bb5-bd1c-dc74d3f1fab2)

## Additional Notes

- In UE, you must explicitly call the parent's method within a child's method. For example, in Unity C# this would be `base.Update()`, but in UE C++ you will use `Super::Tick()` for Actors or `Super::TickComponent()` for Components.
- In UE C++, classes use various prefixes, such as `U` for `UObject` subclasses and `A` for Actor subclasses. See [Coding Standard](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine) for more detailed information.
- For gameplay coding examples, see [Creating Gameplay in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-gameplay-in-unreal-engine-for-unity-developers).
