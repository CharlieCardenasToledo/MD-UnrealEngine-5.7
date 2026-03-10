# Visual Studio Tips and Tricks

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine

> Application Version: 5.7

## Immediate Window

| Command | Description |
| --- | --- |
| `{,,UnrealEditor-Core}::PrintScriptCallstack()` | Blueprint callstack |
| `{,,UnrealEditor-Core}::GFrameNumber` | Current frame number (also works as breakpoint condition) |
| `{,,UnrealEditor-Core}::GPlayInEditorID` | PIE ID (useful for multiplayer, also works as breakpoint condition) |
| `UnrealEditor-Engine!GPlayInEditorContextString` | PIE window name (useful for multiplayer) |

## Quick Reference

### Disabling/Enabling Optimizations

The following macros will disable and enable compiler optimization for the file you add them to:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UE_DISABLE_OPTIMIZATION\n\tUE_ENABLE_OPTIMIZATION",
  "lines_of_code": 2,
  "id": 137624,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2MjQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyMjoyMyswMDowMCJ9--deae644c1a82dc17116d8805d4a8e2ba69727b872b885d75924f93c678c2a8ed",
  "settings": {
    "is_hidden": false
  }
}
```

When optimization is disabled, code will execute exactly as you wrote it without removing temporary or debugging variables you would need during traces or step-by-step debug sessions. This is useful when you want to selectively debug files without using a full Debug build.

### Debug Lines

**Debug lines** refer to lines drawn in the viewport, usually to show the path of line traces or paths. To use them, you need to include `DrawDebugHelpers.h`. The following code illustrates how to use `DrawDebugLine`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#include &quot;DrawDebugHelpers.h&quot;\n\tDrawDebugLine(GetWorld(), START, END, FColor::Green);",
  "lines_of_code": 2,
  "id": 137625,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2MjUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyMjoyMyswMDowMCJ9--3da1f75a499d6324dab4eece27774f4ff288fbbd9c707f6f6100c4587753b4b6",
  "settings": {
    "is_hidden": false
  }
}
```

`DrawDebugHelpers` has numerous debug drawers in addition to standard debug lines. These include:

**Primitive Shapes**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "+ DrawDebugBox\n\t+ DrawDebugSphere\n\t+ DrawDebugCapsule\n\t+ DrawDebugCylinder\n\t+ DrawDebugPlane\n\t+ DrawDebugCone\n\t+ DrawDebugPoint",
  "lines_of_code": 7,
  "id": 137626,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2MjYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyMjoyMyswMDowMCJ9--bd8a20bb276e7d2f8fe133ed23e49981651a2a36c1649e46cd3ec139f1cef779",
  "settings": {
    "is_hidden": false
  }
}
```

**Solid Shapes**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "+ DrawDebugSolidBox\n\t+ DrawDebugSolidPlane",
  "lines_of_code": 2,
  "id": 137627,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2MjcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyMjoyMyswMDowMCJ9--573ae1b097172d2915a22982bde419635f583d23a8d7331234a1475a07e82ef3",
  "settings": {
    "is_hidden": false
  }
}
```

**Other Common Shapes**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "+ DrawDebugFrustrum\n\t+ DrawDebugCamera\n\t+ DrawDebugCrosshairs",
  "lines_of_code": 3,
  "id": 137628,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2MjgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyMjoyMyswMDowMCJ9--7bd8be6c9f4e12f412532ce094cd33eb8e344332c62d55c737284816757c3db1",
  "settings": {
    "is_hidden": false
  }
}
```

**Meshes**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "+ DrawDebugMesh",
  "lines_of_code": 1,
  "id": 137629,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2MjksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyMjoyMyswMDowMCJ9--938b5a6e8342f4ab4e02176b7dfa8be9f5f4f5246fb095f5d439af6a7e38d7a9",
  "settings": {
    "is_hidden": false
  }
}
```

### Debug Text

The following code provides an example of how to write debug text to the screen. This mirrors the functionality in the **Print String** Blueprint node.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#include &quot;Engine/Engine.h&quot;\n\tFString MyDebugString = FString::Printf(TEXT(&quot;MyVelocity(%s)&quot;), *MyVelocity.ToCompactString());\n\tGEngine-&gt;AddOnScreenDebugMessage(INDEX_NONE, 0.f, FColor::Yellow, MyDebugString, false, FVector2D::UnitVector * 1.2f);",
  "lines_of_code": 3,
  "id": 137630,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2MzAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyMjoyMyswMDowMCJ9--5570693b9dbf7b701dcebaa4328f2944f6621338ce4d07d18a033f2e695d2ae6",
  "settings": {
    "is_hidden": false
  }
}
```

The `FString::Printf` function can take string format parameters, providing a way to quickly compose strings that include variables. You need to include `Engine.h` to gain access to `GEngine` so you can call `AddOnScreenDebugMessage`. For more information on how to use string formatting, refer to [String Handling in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/string-handling-in-unreal-engine).

### Enum to String

Enums can be converted to strings by calling `GetNameStringByValue` from a static `UEnum` and providing it with the value you want to get the name of. You must initialize the `UEnum` with a `StaticEnum` of the same type as the enum whose value you are passing in.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "EMyEnum::Type MyVariable;\n\tstatic const UEnum* Enum = StaticEnum&lt;EMyEnum::Type&gt;();\n\tEnum-&gt;GetNameStringByValue(MyVariable);",
  "lines_of_code": 3,
  "id": 137631,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2MzEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyMjoyMyswMDowMCJ9--c363df2675ba915548046c6b2c396bfe29e5923313c64e1b945d390edfabf2a3",
  "settings": {
    "is_hidden": false
  }
}
```

## Fixing the Configuration Combobox Width

The default solution configuration combobox is too small to see the full name of the option currently selected. To fix that, right-click on the **toolbar**, select **Customize**, select the **Commands** tab, select the **radio Toolbar > Standard**, scroll down to the **Solution Configurations**, click on **Modify Selection**, and put in the width you would like. A width of 200 is typically useful.

![Fixing the configuration combobox](https://dev.epicgames.com/community/api/documentation/image/69237c88-b481-4002-8e77-1786741b503d)

## Speeding up Visual Studio 2019

Visual Studio 2019 can be slow when working with Unreal projects. The following are a few strategies that might improve performance for you:

### Debugging Is Slow

Try disabling the following settings in **Option > Debugging > General**:

- Uncheck **Enable Diagnostic Tools** while debugging.
- Uncheck **Show elapsed time PerfTip** while debugging.

### Perforce Visual Studio history Shows Above Every Method

![Showing P4VS history](https://dev.epicgames.com/community/api/documentation/image/243dbcf8-4d1f-434a-9b2b-3a1a19874fe5)

To stop the Perforce Visual Studio history from showing above every method, uncheck **Tools > Options > Text Editor\All Languages\CodeLens > Enable CodeLens**.

### Visual Studio Is Slow when Opening Solutions or Debugging

If you are using another plugin for symbol searching, such as Visual Assist, you can disable the Intellisense database to prevent it from parsing the solution. This can be done from:
**Tools** > **Options** > **Text Editor** > **C/C++** > **Advanced** > Set **Disable Database = true**.
