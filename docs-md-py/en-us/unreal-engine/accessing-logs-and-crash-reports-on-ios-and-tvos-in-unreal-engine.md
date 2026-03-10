# Accessing Logs and Crash Reports on iOS and tvOS

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine

> Application Version: 5.7

### Accessing iOS and tvOS Logs and Crash Reports

iOS applications built with Unreal Engine produce crash logs that developers can use to debug their projects and fix code issues. However, for security reasons, the debug symbols are not available with the crash logs themselves. You will see keys and numbers, but to see names of functions or information about variables in a human-readable format, you need to match your logs to a database of symbols for your project.

There are several processes for re-symbolicating your logs and reading them, depending on how you delivered your debug builds to devices. **TestFlight** is Apple's application for delivering test builds to a large number of possible devices, and it provides logs from those builds to developers. You can also obtain logs directly through USB debugging.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You need a Mac and Xcode to read logs for iOS projects. Other operating systems and IDEs will not work with the workflows on this page.",
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

## 1. Accessing Logs Directly from Device

If you are debugging directly through USB or Ethernet, follow these steps to view a symbolicated crash log:

1. In Xcode, from the main menu, select **Window** > **Devices and Simulators**.
2. Click the iPhone you want to obtain crash data from, then click **View Device Logs**.
3. Control-click the log you want to read, then click **Re-Symbolicate and export Log**.

This will provide a human-readable log with debug symbols.

## 2. Accessing Logs from TestFlight

When an application delivered through TestFlight crashes, it produces an **XCrashPoint** file containing crash information. To read these files, you need a `.dSYM` file with debug symbols for your project, then you need to extract the crash report and re-symbolicate it.

For specific information about deploying applications through TestFlight and accessing logs, refer to [Apple's documentation on TestFlight](https://developer.apple.com/testflight/). This section will provide information about how to symbolicate them once you have obtained them.

### Generating a .dSYM File During Packaging

To generate a `.dSYM` file when you package your project, follow these steps:

1. Open **Unreal Editor**.
2. Open your **Project Settings**, then navigate to **Platforms** > **iOS** > **Build**.
3. Enable **Generate dSYM file for code debugging and profiling**. ![Check the Generate dySM file option](https://dev.epicgames.com/community/api/documentation/image/5501bf54-d2fa-4d31-a78a-7adc2502402d)
4. Package your project.

The `.dSYM` file for your project will appear in your project folder, under `/Binaries/iOS`.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code>.dSYM</code> files have a timestamp showing when they were packaged. Take note of this information so you can match <code>.dSYM</code> files to the correct build.",
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

### Generating a .dSYSM File From a Command Line

To generate .dSYM file using UAT, execute the RunUAT script in a command line with the **GenerateDYSM** command. Specify the following parameters:

| Parameter | Optional | Valid Values | Description |
| --- | --- | --- | --- |
| -Platform=[Target Platform] | Yes | IOS, TVOS, Mac | Specifies target platform. Defaults to current platform if unspecified. |
| -Target=[Project Name] | Yes | The name of your project. | Specifies which project you want to use. Defaults to current project if unspecified. |
| -Config=[Build Configuration] | Yes | Debug, DebugGame, Development, Test, Shipping | Target build configuration. Defaults to Development if unspecified. |
| -Architecture=[Architecture Type] | No | x64, arm64, x64+arm64] | Target device architecture. |
| -flat | Yes | Does not take inputs. | If specified, the .dSYMs will be flat files that are easier to copy between computers or servers. |

For example, the following command will generate .dSYM files for iOS devices using the arm64 architecture:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "```RunUAT.command GenerateDYSM -project=MyProject -platform=Mac -target=EngineTestEditor -config=Test -architecutre=arm64```",
  "lines_of_code": 1,
  "id": 60599,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDU5OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjM2KzAwOjAwIn0=--a2ab78eabb34bd7a4cf87d565d85c1bb842fe42f2850672a162e0073838f61b4",
  "settings": {
    "is_hidden": false
  }
}
```

### Extracting the Crash Report and Re-Symbolicating

To obtain your crash report and re-symbolicate it so that you can read it, follow these steps:

1. Obtain an `XCrashPoint`file from TestFlight. You can use the following command line input to do this.
2. Control-click on the `.XCrashPoint` file, then click **Extract `.crash` file**. You can also export this information using the following command line input:
3. Open XCode, then look at the **terminal**. Use it to navigate to your Xcode `.package`.
4. Use the symbolicatecrash tool by running the following command line:

The above instructions use default directories. Use the locations of your `.crash` and `.dSYM` files when you run these command lines.

Xcode will then provide a crash log with function names and variables visible.
