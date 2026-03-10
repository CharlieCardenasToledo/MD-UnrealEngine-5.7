# Set Up and Compile Your Project

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine

> Application Version: 5.7

## Before You Begin

Ensure you've done the following:

- [Installed Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine) and set up [Visual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.5) for Unreal Engine
- Learned about Projects and Actors and how to navigate Unreal Editor
- Read [Code a First-Person Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

## Start From a Template

This tutorial starts you off with a Blueprint-based project containing sample assets. You'll gradually add code that replicates and expands on the existing Blueprint functionality. This way, you can learn to build new classes in a fresh C++ project while also having the equivalent Blueprints available as a reference.

To create a new game project from a template, follow these steps:

1. Open Unreal Engine. In the **Unreal Project Browser**, go to the **Games** project category, and select the **First Person** template. ![Image](https://dev.epicgames.com/community/api/documentation/image/73b65128-97f9-4d0e-9660-bdbc27ab951d)
2. In the **Project Defaults**, keep the project type set to **Blueprint**. This means Unreal Engine creates a project with Blueprint-type default assets instead of C++ assets.
3. For the **Variant**, select **Arena Shooter**.
4. Name your project. This tutorial uses `AdventureGame` as the project name.
5. Click **Create** to open your new project in the editor.

## Verify Enhanced Input

With the **Enhanced Input system**, you can control character movement by building custom Input Actions that define the actions your character can do, such as jumping or crouching. Each Input Action exists as a data asset that you can reference in code to communicate between your code and your character.

Later in this tutorial, you’ll combine Input Actions and code to enable your character to move and look around.

The Enhanced Input system should already be enabled in your project. To verify this, follow these steps:

1. In Unreal Editor’s main menu, go to the **Edit** menu, and select **Plugins**.
2. Search for **Enhanced Input**. You should see the plugin installed and enabled. ![Image](https://dev.epicgames.com/community/api/documentation/image/05b4ce2b-0bb0-494f-8008-f9ab40d5325e)

To learn more about the Enhanced Input system and Input Actions, see [Enhanced Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine).

## Create a C++ Game Mode Class

Your Blueprint-based project doesn’t have any C++ files or a Visual Studio (VS) project to work with. Next, you'll create your first C++ class, which tells Unreal Engine to generate the Visual Studio project and files you need to get coding.

You'll start with a Game Mode class. **Game Mode** assets define a game's rules, win conditions, and what characters are used. The Game Mode also sets the default gameplay framework classes your project uses, including the Pawn, PlayerController, and HUD. Later in this tutorial, you’ll use your Game Mode to change the default player character.

To create a new Game Mode C++ class, follow these steps:

1. In Unreal Editor’s main menu, go to **Tools > New C++ Class**.
2. In the **Choose Parent Class** window, find and select **Game Mode Base**, and click **Next**. ![Image](https://dev.epicgames.com/community/api/documentation/image/f25d4a94-1509-47ab-b79b-90a88bdeddd1) This means your custom class is derived from the parent `AGameModeBase` class.
3. In the **Name Your New Game Mode Base** step, next to **Class Type**, click **Public**, which places the class header in your game module's Public folder so it can be included by other code.
4. Enter a name for the new class, then click **Create Class**. This tutorial uses `AdventureGameMode`. ![Image](https://dev.epicgames.com/community/api/documentation/image/b3473dbe-5429-487b-a954-72245b6d562a)
5. Adding code to your project may take a minute or two. During this process, two warning prompts appear, stating that you’ll need to build or compile your project from VS at least once before the C++ classes appear in the Content Browser. Click **OK**, and then click **Yes** on the second warning to open your code.

## Build Your Project

Before you start adding code, finish preparing your environment by building your project in VS and refreshing Unreal Editor.

### Open the Project in Visual Studio

If the engine didn’t automatically prompt you to open your project in VS after you created the Game Mode class, in Unreal Editor’s main menu, go to **Tools** and select **Open Visual Studio**.

You can also find your project’s `.sln` file in `/Documents/Unreal Projects/[ProjectName]` by default.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Unreal Engine tracks changes you make to your project, like adding new classes, modules, plugins, or modifying build settings. However, the VS project files may not automatically reflect these updates. Use <b>Refresh Visual Studio Project </b>(also in the <b>Tools </b>menu) to regenerate the solution and project files based on the current project state so everything is up-to-date.",
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

When you open Visual Studio, you'll see your project files organized in the **Solution Explorer**.

![Image](https://dev.epicgames.com/community/api/documentation/image/0889e6d1-2a98-4897-89f5-9a08439920c4)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When you open your first Unreal Engine C++ project in VS, you might see a warning about missing components in the <b>Solution Explorer</b>. Click <b>Install </b>to allow VS to install any additional components that may be necessary for your project.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26399771,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 26399771,
        "file_name": "ue5_3-visual-studio-missing-components.png",
        "file_size": 28011,
        "content_type": "image/png",
        "created_at": "2026-01-20T21:59:43.725+00:00",
        "height": 207,
        "width": 324,
        "storage_key": "55a7a504-66a6-44fc-b992-31a946018e96",
        "context": "documentation"
      },
      "storage_key": "55a7a504-66a6-44fc-b992-31a946018e96",
      "context": "documentation",
      "width": 330,
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

In the **Solution Explorer**, expand **Games > [*ProjectName*] > Source > [*ProjectName*]**. This is where the main files for your game are located, including two files corresponding to your new Game Mode, `[GameModeName].cpp` and `[GameModeName].h`.

![Image](https://dev.epicgames.com/community/api/documentation/image/28254003-0850-4232-ad9a-3feca7532b5c)

### Build the Project and Refresh Unreal Editor

To make Unreal Editor recognize your code project and include your C++ classes in the Content Browser, build your project from VS and restart the editor.

To build your project so its classes appear in Unreal Editor, follow these steps:

1. In the **Solution Explorer**, under the **Games** folder, right-click your project, and select **Build**. ![Image](https://dev.epicgames.com/community/api/documentation/image/0498c05c-f716-4ee8-8785-4927fd7d841f)
2. When the build is complete, go back to Unreal Editor and check if the **Compile**button has appeared in the bottom toolbar and if a new C++ Classes folder has appeared in the Content Browser. ![Image](https://dev.epicgames.com/community/api/documentation/image/5a2bbed7-4c2a-472c-afba-dfb4f2f6e072)
3. If they haven’t appeared, close the editor and open your project again. Opening the editor recompiles your project, telling UE that your C++ classes exist. If Unreal Engine asks to rebuild your project, click **Yes**.

### Disable Live Coding

Before compiling your code again, turn off **Live Coding** in Unreal Editor. With Live Coding, you can change and rebuild C++ code in implementation (`.cpp`) files while the engine is running; however, it follows a different compilation workflow and may produce errors when editing header (`.h`) files or trying to compile from Visual Studio. Live Coding is useful when iterating on a developed code base, but we recommend disabling it when starting a new project.

To turn off Live Coding, in the editor’s bottom toolbar, click the three dots next to the **Compile** button and disable **Enable Live Coding**.

![Image](https://dev.epicgames.com/community/api/documentation/image/651891b3-d23b-4c51-9803-27220f146152)

## Extend a C++ Class to Blueprints

Now that you've made your own custom Game Mode, extend it to Blueprints to expose its properties to the editor, then set that new Blueprint as your project’s default Game Mode.

Extending your Game Mode class to Blueprints exposes class values directly to the editor instead of doing everything through code. The Blueprint acts as a child of the C++ class, inheriting all functionality of the class.

To derive a Blueprint asset from your GameMode class, follow these steps:

1. In the **Content Browser** asset tree, go to **C++ Classes > [*ProjectName*]** **> Public** to find the C++ classes you’ve created.
2. Right-click your **Game Mode Base** class and select **Create Blueprint class based on [*GameModeBaseName*]**. ![Image](https://dev.epicgames.com/community/api/documentation/image/db1b8c6e-bf40-47d9-b0a1-a646905ff32d)
3. In the **Add Blueprint Class** window, name your Blueprint with a `BP_` prefix so you can identify it later. This tutorial uses `BP_AdventureGameMode`.
4. For the **Path**, select **All** > **Content** > **FirstPerson** > **Blueprints,** and click **Create Class**. ![Image](https://dev.epicgames.com/community/api/documentation/image/4ffd1c6f-39c1-43da-a829-cd32cf930018) Unreal Engine automatically opens the Blueprint in a new Blueprint Editor window.
5. In the Game Mode Blueprint's tab, click **Save**.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can dock the new window within the main editor window by dragging the Blueprint’s tab next to the map tab (<b>Lvl_FirstPerson</b>) in the main editor window. ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26399778,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 26399778,
        "file_name": "ue5-dockingawindow.gif",
        "file_size": 1541829,
        "content_type": "image/gif",
        "created_at": "2026-01-20T21:59:44.452+00:00",
        "height": 720,
        "width": 1280,
        "storage_key": "72e879e9-d48a-49bf-b967-f03082f5419b",
        "context": "documentation"
      },
      "storage_key": "72e879e9-d48a-49bf-b967-f03082f5419b",
      "context": "documentation",
      "width": 450,
      "autoplay": true,
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

## Change the Project’s Game Mode

By default, new Unreal Engine projects use a sample Game Mode. To change this to your custom Game Mode, edit your project’s settings.

To change the default Game Mode, follow these steps:

1. In the editor’s main menu, go to **Edit > Project Settings**.
2. In the **Project** section in the left panel, select **Maps & Modes**.
3. At the top of the settings table, change the **Default GameMode** to your Game Mode Blueprint. ![Image](https://dev.epicgames.com/community/api/documentation/image/49737a24-0a00-45dd-9141-c65a05bf3e1c)
4. Close **Project Settings**.
5. Return to the level editor tab. Next to the **Details** panel tab, click the **World Settings** tab. The **World Settings** panel contains settings control how the current level behaves.
6. In the **Game Mode** section, set **GameMode Override** to your new Game Mode Blueprint (ensure the asset you select has the `BP_` prefix). Or, click the arrow icon to remove the override so the level uses the default Game Mode set in the project settings. ![Image](https://dev.epicgames.com/community/api/documentation/image/20f5b7c2-ca49-432a-ae2a-311d9b8a1973)
7. In the level editor, click **Save**.

## Add an On-Screen Debug Message

A great way to start adding code to your project is by adding a “Hello World!” message on screen.

Add a debug message to verify that you are using your new Game Mode rather than the default Game Mode provided by Unreal Engine. Log messages and debug messages are useful for verifying and debugging code during development.

### Override the Default StartPlay() Function

`AGameModeBase` includes a `StartPlay()` function that UE calls when the game is ready to start gameplay. You'll typically override this function in your custom GameMode classes to add global game start logic. Here, you'll override it to make a debug message appear when the game starts.

To override `StartPlay()` in your custom GameMode class, follow these steps:

1. In VS, open your Game Mode class’ `.h` header file. The code samples in this tutorial use a class named `AdventureGameMode.` The default code should look like this: `GENERATED_BODY()` is a macro used by Unreal Header Tool that automatically generates code required for this class and other UObjects to work with Unreal Engine. To learn more about Unreal Header Tool, see the [UHT documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine). The `AAdventureGameMode` class exposes different Game Mode states to your code, such as a game starting or ending, entering a map, or a game being in progress. When each state is triggered, it runs an associated function such as `StartPlay()` or `ResetLevel()`.
2. Add an override declaration for the `StartPlay()` function to your `AAdventureGameModeBase` class. Place this override after the `GENERATED_BODY()` line.
3. Save the `.h` file.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Unreal Engine classes and functions have prefixes tell the Unreal Header Tool about the class type. For example, an <code class=\"inline-code\">A</code> prefix for Actors, <code class=\"inline-code\">U</code> for UObjects, and <code class=\"inline-code\">F</code> for Structs. To learn more about Unreal Engine C++ Class Prefixes, see <a data-document-id=\"3227315\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine\">Epic C++ Coding Standards: Naming Conventions</a>.  ",
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

### Add a Debug Message to StartPlay()

Implement your `StartPlay()` override with some custom code that prints a debug message.

To print a debug message on screen when gameplay starts, follow these steps:

1. Open your Game Mode’s `.cpp` file to implement the function you just declared.
2. Add a new function definition for `StartPlay()`. This function is declared in `AAdventureGameMode`, so define it using `AAdventureGameMode::StartPlay()`. Place this code after the `#include` line.
3. Inside `AMyGameModeBase::StartPlay()`, add `Super::StartPlay()` to call the `StartPlay()` function from the `AAdventureGameMode` parent class. This is necessary to handle the other logic that should run when the game starts.
4. After `Super::StartPlay()`, add a `check` for `GEngine != nullptr` to ensure the global engine pointer is valid. This is a pointer to the UEngine class that Unreal Engine itself uses, and checking that it's valid ensures your game is running properly before your code continues. If the global engine pointer isn’t valid, your game will crash.
5. Use `GEngine` to access UEngine's `AddOnScreenDebugMessage()` member function, which prints a message on-screen when the game is running. This function takes four values: A unique int key that identifies the message and prevents the same message from being added multiple times. Use `-1` if the uniqueness doesn’t matter. A float number of seconds to display the message. An `FColor` that sets the text color. An `FString` message to print. Calling this function with the following values displays a “Hello World!” message in yellow text on the screen for five seconds when the game begins: Place this code after the `check` line.
6. Save the `.cpp` file.

Now, `AAdventureGameMode::StartPlay()` should look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#include &quot;AdventureGameMode.h&quot;\n\nvoid AAdventureGameMode::StartPlay()\n{\n\tSuper::StartPlay();\n\n\tcheck(GEngine != nullptr);\n\n\tGEngine-&gt;AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT(&quot;Hello World!&quot;));\n}",
  "lines_of_code": 10,
  "id": 160833,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MzMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODowMyswMDowMCJ9--6f9d1baec712f7260646980858cf7cf72edae5bc1450632e5ca858064b39f5e3",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">UE_LOG</code> is another helpful function for printing debug messages. Instead of printing a message on-screen, it logs messages to Unreal Engine’s output log or console during runtime. It’s useful for logging or tracking detailed information about what’s happening in your game. You can categorize logs into different channels and define the message type (such as informational, error, or warning messages). For example:<br><br><code class=\"inline-code\">UE_LOG(LogTemp, Warning, TEXT(\"This is a warning message!\"));</code>",
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

## Compile and Test Your Code

You can click the **Compile** button in Unreal Editor to rebuild your project; however, we recommend rebuilding from VS. Once compiled, you can see your code changes reflected in the editor and in-game.

To see your changes in game, click **Play** in the main toolbar to start **Play in Editor** (**PIE**) mode. Your debug message appears in the top-left corner.

![Image](https://dev.epicgames.com/community/api/documentation/image/bf9d8417-1a6c-4f0c-8190-b3ba349a7b1d)

![Image](https://dev.epicgames.com/community/api/documentation/image/6ab7bb86-c2ab-445e-ad58-58399b633cfd)

To exit PIE mode, press **Shift + Escape** or click **Stop** in the Level Editor toolbar.

## Next Up

Now that you have a basic project with a new Game Mode, you can start creating your player character! In the next section, you’ll build a new Character class and learn how to use Input Actions to add movement controls to your character.

- [Related Document](en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus.md)

## Complete Code

Here is the complete code built in this section:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "AdventureGameMode.h",
  "code_preview": "#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/GameModeBase.h&quot;\n#include &quot;AdventureGameMode.generated.h&quot;\n\nUCLASS()\nclass ADVENTUREGAME_API AAdventureGameMode : public AGameModeBase\n{\n\tGENERATED_BODY()\n",
  "lines_of_code": 13,
  "id": 160834,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MzQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODowMyswMDowMCJ9--42f9b164d3afd5fb13ea008562363bd7773bc7805b3a1141590066f02e6864e9",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "AdventureGameMode.cpp",
  "code_preview": "#include &quot;AdventureGameMode.h&quot;\n\nvoid AAdventureGameMode::StartPlay()\n{\n\tSuper::StartPlay();\n\n\tcheck(GEngine != nullptr);\n\n\tGEngine-&gt;AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT(&quot;Hello World!&quot;));\n}",
  "lines_of_code": 10,
  "id": 160835,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MzUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODowMyswMDowMCJ9--ca0f681e4f45202ca42e0d0788559bfe938a2ff3b8f97f720f532f18dbbbefe9",
  "settings": {
    "is_hidden": false
  }
}
```
