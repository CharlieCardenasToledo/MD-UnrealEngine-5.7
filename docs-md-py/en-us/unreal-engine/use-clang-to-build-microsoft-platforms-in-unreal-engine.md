# Use Clang to Build Microsoft Platforms

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine

> Application Version: 5.7

**Unreal Engine (UE)** supports using the **Clang** compiler on Windows to build [supported Microsoft platforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine). You can enable Clang with:

- [Build Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine)
- [Command-Line Arguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine)
- [Engine Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine)

This page also includes a table of additional options, such as specifying:

- Clang linker
- Clang version
- MSVC version
- Toolchain version

For more information, see the [Additional Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine) section below. As of UE 5.3, the latest supported version of Clang is [Clang 16](https://releases.llvm.org/16.0.0/tools/clang/docs/index.html).

## What is Clang

Clang is a front-end compiler that compiles C, C++, Objective-C, and Objective-C++ into machine code. Clang is an alternative to the MSVC (Microsoft Visual C++) compiler.

## Install Clang

You can install Clang through [Visual Studio](https://learn.microsoft.com/en-us/cpp/build/clang-support-msbuild?view=msvc-170) or directly from the [LLVM Downloads](https://releases.llvm.org/download.html) page.

## Enable Clang

Once you have installed Clang, follow any one of the methods below to enable Clang in your Unreal project.

### Build Configuration

To enable Clang in [Build Configuration](setting-up-your-production-pipeline/unreal-build-system/unreal-build-tool/build-configuration), navigate to an engine `BuildConfiguration.xml` file, and add the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; ?&gt;\n&lt;Configuration xmlns=&quot;https://www.unrealengine.com/BuildConfiguration&quot;&gt;\n\t...\n\t&lt;WindowsPlatform&gt;\n      \t\t&lt;Compiler&gt;Clang&lt;/Compiler&gt;\n\t&lt;/WindowsPlatform&gt;\n...\n&lt;/Configuration&gt;",
  "lines_of_code": 8,
  "id": 163119,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMxMTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyODozNiswMDowMCJ9--321ef1d0d79d9bfbfe254b6b090ecc94bf0eaa696e4b92dba98d023949becee1",
  "settings": {
    "is_hidden": false
  }
}
```

### Command-Line Arguments

To enable Clang with [Command-Line Arguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine), pass the `-Compiler=Clang` option.

### Engine Configuration

To enable Clang in [Engine Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/configuration-files-in-unreal-engine), navigate to an engine configuration file, such as `DefaultEngine.ini`, and add the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[/Script/WindowsTargetPlatform.WindowsTargetSettings]\n-Compiler=Clang",
  "lines_of_code": 2,
  "id": 163120,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMxMjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyODozNiswMDowMCJ9--d9ca335bfb6e3dc8959191efce7375fb056368fdc0c6a386a8873bfa923a6614",
  "settings": {
    "is_hidden": false
  }
}
```

## Additional Options

The following options assume that:

- Build Configuration options are added inside the `<WindowsPlatform>...</WindowsPlatform>` section of `BuildConfiguration.xml`.
- Engine Configuration options are added to the `[/Script/WindowsTargetPlatform.WindowsTargetSettings]` section of an engine configuration file, such as `DefaultEngine.ini`.

| Option | Build Configuration | Command-Line Argument | Engine Configuration |
| --- | --- | --- | --- |
| Clang linker | `<bAllowClangLinker>true</bAllowClangLinker>` | `-ClangLinker` | `bAllowClangLinker=true` |
| Clang Compiler Version | `<CompilerVersion>Latest</CompilerVersion>` | `-CompilerVersion=Latest` | `CompilerVersion=Latest` |
| MSVC Version | `<Toolchain>VisualStudio2022</VisualStudio>` | `-VCToolchain=VisualStudio2022` | `Toolchain=VisualStudio2022` |
| Toolchain Version | `<ToolchainVersion>Latest</ToolchainVersion>` | `-VCToolchainVersion=Latest` | `ToolchainVersion=Latest` |

### Clang Linker

The Clang Linker is a boolean option that determines whether the Clang Linker is used when compiling with Clang.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Epic does not use the Clang linker for Microsoft platforms and it is not currently tested.",
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

### Clang Compiler Version

The Clang compiler version is a string option that determines which version of the specified compiler is used. The options include:

- Specific version number: Use the exact version specified, for example, "16.0.0".
- Latest: Use the newest installed version.

### MSVC Version

The MSVC Toolchain is a string option that determines which toolchain is used. The options include:

- VisualStudio2022

### Toolchain Version

The Toolchain version is a string option that determines which version of the MSVC toolchain is used. The options include:

- Specific version number: Use the exact version specified, for example, "14.37.32822".
- Latest: Use the newest installed version.
- Preview: Use the newest installed preview version.

## More Information

Follow these links for information about:

- [Windows Platform](setting-up-your-production-pipeline/unreal-build-system/unreal-build-tool/build-configuration/#windowsplatform) section of [Build Configuration](setting-up-your-production-pipeline/unreal-build-system/unreal-build-tool/build-configuration)
- [Command-Line Arguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine)
- [Engine Configuration Files](https://dev.epicgames.com/documentation/en-us/unreal-engine/configuration-files-in-unreal-engine)
