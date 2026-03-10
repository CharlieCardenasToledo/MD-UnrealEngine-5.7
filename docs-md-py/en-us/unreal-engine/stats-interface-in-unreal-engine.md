# Stats Interface

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine

> Application Version: 5.7

The **Online Services Stats Interface** is used to upload stats and data to online services and complete stats queries. Stats Interface functionality is also used by other interfaces that rely on user gameplay statistics such as the Online Services' Achievements and Leaderboards Interfaces.

## API Overview

The following table provides a high-level description of the functions included in the Stats Interface.

| Function | Description |
| --- | --- |
| **Update** |   |
| [UpdateStats](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/UpdateStats?application_version=5.5) | Upload stats to the platform |
| **Query** |   |
| [QueryStats](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/QueryStats?application_version=5.5) | Query the stats of a user and cache the result in the interface. |
| [BatchQueryStats](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/BatchQueryStats?application_version=5.5) | Query the stats of a group of users and cache the results in the interface. |
| **Get** |   |
| [GetCachedStats](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/GetCachedStats?application_version=5.5) | Retrieve the cached user stats stored after a call to QueryStats or BatchQueryStats. |
| **Event Listening** |   |
| [OnStatsUpdated](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/OnStatsUpdated?application_version=5.5) | An event will fire as a result of changes to user stats. |

## Configuration

You can use the Stats Interface with either a corresponding platform backend or a `StatsNull` implementation. To use the Stats Interface, you must first configure the Stats Interface in your `DefaultEngine.ini` file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "DefaultEngine.ini",
  "code_preview": "[OnlineServices.Stats]\n+StatDefinitions=(Name=&lt;STAT_NAME&gt;, Id=&lt;ID_NUMBER&gt;, ModifyMethod=&lt;METHOD&gt;, DefaultValue=&quot;&lt;TYPE&gt;:&lt;DEFAULT_VALUE&gt;&quot;)",
  "lines_of_code": 2,
  "id": 150517,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1MTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NyswMDowMCJ9--091334697819e3091e5394e0375449e7304f4f6d0b0c117b141f8407502cf210",
  "settings": {
    "is_hidden": false
  }
}
```

**Stat Definitions** consist of the following fields:

- `Name`: The name of the stat. This is the name that will be used to update and query stats with `UpdateStats` and `QueryStats` respectively.
- `Id`: The ID of the stat. This is the corresponding configured stat ID in the platform portal.
- `ModifyMethod`: Method prescribing how the stat will be updated. For non-`StatsNull` implementations, the Modify Method is configured in the platform portal. The Modify Method is used by the Achievements Interface on all implementations when using Title Managed achievements to determine whether an achievement meets the prescribed unlock rules.
- `DefaultValue`: The type and default value of the stat. This prescribes the initial value of the stat.

To unlock achievements and update leaderboards with stats, you must specify corresponding stats in the Achievements and Leaderboards config sections of `DefaultEngine.ini`.

### Configuration Example

Here is a configuration example for the Online Services Stats interface:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "DefaultEngine.ini",
  "code_preview": "[OnlineServices.Stats]\n+StatDefinitions=(Name=Stat_Use_Largest, Id=0, ModifyMethod=Largest, DefaultValue=&quot;Int64:0&quot;)\n+StatDefinitions=(Name=Stat_Use_Smallest, Id=1, ModifyMethod=Smallest, DefaultValue=&quot;Int64:999&quot;)\n+StatDefinitions=(Name=Stat_Use_Set, Id=2, ModifyMethod=Set, DefaultValue=&quot;Int64:0&quot;)\n+StatDefinitions=(Name=Stat_Use_Sum, Id=3, ModifyMethod=Sum, DefaultValue=&quot;Int64:0&quot;)\n+StatDefinitions=(Name=Stat_Type_Bool, Id=4, ModifyMethod=Set, DefaultValue=&quot;Bool:True&quot;)\n+StatDefinitions=(Name=Stat_Type_Double, Id=5, ModifyMethod=Smallest, DefaultValue=&quot;Double:9999.999&quot;)",
  "lines_of_code": 7,
  "id": 150518,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1MTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NyswMDowMCJ9--8be19c3e07cf48457dfc40c778cc56c5f6bfbb23ea7c7a1bad438d5ddaa929dd",
  "settings": {
    "is_hidden": false
  }
}
```

## Examples

This section contains a variety of code examples that guide you on how to:

- [Query Stats](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5)
- [Get Cached Stats](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5)
- [Listen for an event](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5)
- [Execute a Console Command](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5)

### Query Stats

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();\nUE::Online::IStatsPtr Stats = OnlineServices-&gt;GetStatsInterface();\n\nUE::Online::FQueryStats::Params Params;\nParams.LocalAccountId = LocalAccountId;\nParams.TargetAccountId = TargetAccountId;\nParams.StatNames = {&quot;StatA&quot;, &quot;StatB&quot;};\n\n// See Note below Walkthrough for more information about this OnComplete call\nStats-&gt;QueryStats(MoveTemp(Params)).OnComplete([](const UE::Online::TOnlineResult&lt;FQueryStats&gt;&amp; Result)\n",
  "lines_of_code": 20,
  "id": 150519,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1MTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NyswMDowMCJ9--c8e2e5c5ee64a0f39d5b0536babac681d30647db6801f8a423ee09aceb4e1724",
  "settings": {
    "is_hidden": false
  }
}
```

#### Walkthrough

1. Use the default online services by calling `GetServices` with no parameters specified:
2. Access the Stats Interface for the default online services:
3. Instantiate the parameters necessary to query the `StatNames` of the `TargetAccountId`:
4. Handle the `QueryStats.OnComplete` callback by processing the error or the queried stats:

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To bind to a member function, always prefer to use a UObject-derived class or a class that inherits from <code>TSharedFromThis</code> and use",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "code_snippet",
      "description": "",
      "snippet_type": "cpp_programming",
      "title": "",
      "code_preview": ".OnComplete(this, &amp;MyClass::OnQueryStatsComplete)",
      "lines_of_code": 1,
      "id": 150524,
      "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1MjQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NyswMDowMCJ9--a969b90c41dfa6c0dc70c6e3ca348ce9a42355f083da73f4b9d8462213231362",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This automatically selects <code>CreateUObject</code>, <code>CreateThreadSafeSP</code>, or <code>CreateSP</code>. The safest delegate creation call will be used. For more information, refer to the <a href=\"programming-and-scripting/online/online-services/overview#CallbackFormat\">Callback Format</a> section of the Online Services Overview page.",
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

### Get Cached Stats

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();\nUE::Online::IStatsPtr Stats = OnlineServices-&gt;GetStatsInterface();\n\nUE::Online::TOnlineResult&lt;FGetCachedStats&gt; CachedStats = Stats-&gt;GetCachedStats({});\nif (CachedStats.IsError())\n{\n\tUE::Online::FOnlineError OnlineError = CachedStats.GetErrorValue();\n\t// Process OnlineError\n\treturn;\n}\n",
  "lines_of_code": 13,
  "id": 150525,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1MjUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NyswMDowMCJ9--a728dda4e934eb9e4a4e487dbbc6d5052cff2535ec4b310a6a5c798d2d93bbfc",
  "settings": {
    "is_hidden": false
  }
}
```

#### Walkthrough

1. Use the default online services by calling `GetServices` with no parameters specified and access the Stats Interface:
2. Retrieve the cached stats through the Stats Interface with `Stats->GetCachedStats`:
3. Handle the `CachedStats` by processing the error or the cached stats data:

### Listen for an Event

Event listening is handled differently than synchronous and asynchronous functions. An `FOnlineEventDelegateHandle` is created to handle the result of the `OnStatsUpdated` event, then `Unbind` must be called in your shutdown code to ensure proper destruction.

#### Walkthrough

1. Declare an event handle in your class for the Stat interface.
2. In your init code, initialize the default online services, access the Stats interface, and process the stats when an event happens.
3. Ensure that you unbind the event handler in your shutdown code.

### Execute a Console Command

For the general command-line syntax to run an async interface with a console command, refer to the [Online Services Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5) documentation.

#### Example

To run the `QueryStats` function, execute the following console command:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "OnlineServices Index=0 Stats QueryStats 0 0 [&quot;StatA&quot;, &quot;StatB&quot;]",
  "lines_of_code": 1,
  "id": 150532,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1MzIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NyswMDowMCJ9--527781a4e144c7c49ee0afe9d2246ae89f39d6b6b63744c11cfbcad8c43084ee",
  "settings": {
    "is_hidden": false
  }
}
```

This command calls `QueryStats` from the Stats Interface with the default online services for the zeroth local user. In particular, the above command queries the default online services for `StatA` and `StatB` of this user.

## Reset Stats Data

During development and testing, the `ResetStats` function resets all provided player stats for the current title. Although policies vary across online services, you should not expect this function to work outside a testing environment. Be sure to remove any code that uses `ResetStats` from shipping builds, or use compile-time logic to mask the code like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if !UE_BUILD_SHIPPING\n// Code block with call to ResetStats\n#endif",
  "lines_of_code": 3,
  "id": 150533,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1MzMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NyswMDowMCJ9--2be3eeac49c5032eec8bbbc224f649a2e4af26ede5c9970c048be5e547bd1c23",
  "settings": {
    "is_hidden": false
  }
}
```

## More Information

### Header File

Consult the `Stats.h` header file directly for more information as needed. The Stats Interface header file `Stats.h` is located in the directory:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Engine\\Plugins\\Online\\OnlineServices\\Source\\OnlineServicesInterface\\Public\\Online",
  "lines_of_code": 1,
  "id": 150534,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1MzQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NyswMDowMCJ9--55630a6541dd25a8440c336d21596d98b92bfb95bed6c69f28480dc1184d8752",
  "settings": {
    "is_hidden": false
  }
}
```

For instructions on how to obtain the UE source code, refer to our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

Refer to the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.
