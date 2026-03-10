# BuildGraph Script Types

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-types-reference-for-unreal-engine

> Application Version: 5.7

The following table contains valid data types that can be contained by **BuildGraph** attributes:

| **Type** | **Description** |
| --- | --- |
| **String** | An arbitrary string. |
| **String List** | A list of arbitrary strings separated by semicolons. |
| **Boolean** | The constant `true` or `false`. |
| **Integer** | An integer constant. |
| **Regex** | A regular expression, using [C#](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference) syntax. |
| **Name** | A named entity. Any printable character, except `^ < > : " / \ \| ? * ;`. Single spaces are allowed (except at the start and end of a name). |
| **Name List** | A list of identifiers separated by semicolons. |
| **Tag** | A label given to a list of files beginning with the # character (for example, `#My Files`). |
| **Tag List** | A list of tags separated by semicolons (for example, `#My Files;#Other Files`). |
| **Target** | A node name, aggregate name, agent name, or tag name. Indicates a sequence of nodes that need to be executed. Note that this overlaps with the meaning of `Target` as it applies to [UnrealBuildTool](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine) (which refers to a single program being built). |
| **Target list** | A list of target names separated by semicolons. |
| **File Spec** | A set of file and tag names separated by semicolons. Wildcards such as `"..."`, `"_"`, and `"?"` are permitted when referencing files (for example, `Engine/.../_.bat`). Unless otherwise specified, relative paths are resolved relative to the working root directory. |
| **File Reference** | A path to a file. Unless otherwise specified, relative paths are resolved to the working root directory. |
| **Directory Reference** | A path to a directory. Unless otherwise specified, relative paths are resolved relative to the working root directory. |
| **Unreal Target Configuration** | The configuration in which to build the target. Available configurations are: `Debug`, `DebugGame`, `Development`, `Test`, or `Shipping`. |
| **Unreal Target Platform** | A platform that Unreal Engine supports. Supported platforms can be found in [Sharing and Releasing Projects](https://dev.epicgames.com/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine). Please refer to your platform's documentation. |
| **Condition** | A [conditional expression](https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-conditions-reference-for-unreal-engine). |
