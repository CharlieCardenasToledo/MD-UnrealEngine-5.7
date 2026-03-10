# Leaderboards Interface

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine

> Application Version: 5.7

A **leaderboard** is a list of players ranked by an in-game statistic. Leaderboards encourage competition between players, their friends, and the rest of the world, for the top score in your game. Games can feature multiple modes that award scores. Each of these modes can have its own leaderboard or leaderboards.

Leaderboards can rank entries in the following ways:

- **Ascending**: Lower scores are ranked better than higher scores. The Fortnite wins leaderboard is organized in descending order since more wins is desirable.
- **Descending**: Higher scores are ranked better than lower scores. Lap time leaderboards in racing games are organized in ascending order since faster lap times are more desirable.

The **Online Services Leaderboards Interface** provides developers with tools to display and update leaderboards from within their games. Leaderboard data can be very large since each leaderboard your game supports could have an entry for every user account that has played your game. For this reason, the leaderboards interface retrieves data in chunks. Games that implement the leaderboards interface can request chunks of the leaderboard in different ways as described below in the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5#functions) section and, in more detail, in the [Read Leaderboard Entries](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5) section.

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the leaderboards interface:

| Function | Description |
| --- | --- |
| [ReadEntriesForUsers](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ILeaderboards/ReadEntriesForUsers?application_version=5.5) | Read leaderboard entries for specific users. |
| [ReadEntriesAroundRank](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ILeaderboards/ReadEntriesAroundRank?application_version=5.5) | Read leaderboard entries around a specified rank index. |
| [ReadEntriesAroundUser](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ILeaderboards/ReadEntriesAroundUser?application_version=5.5) | Read leaderboard entries around the specified user. |

### Primary Struct

The leaderboards interface's functionality is primarily communicated through the [FLeaderboardEntry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FLeaderboardEntry?application_version=5.5) struct:

| Member | Type | Description |
| --- | --- | --- |
| `AccountId` | `FAccountId` | Account ID of this leaderboard entry. |
| `Rank` | `int32` | Rank of this account in this leaderboard. |
| `Score` | `int64` | Score of this account in this leaderboard. |

## Configuration

To update a leaderboard score using stats, you must configure the leaderboards interface in the engine configuration files, such as `DefaultEngine.ini`. The leaderboards interface works in conjunction with the [Stats Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5) to track stats for leaderboard rankings.

### General Syntax

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "DefaultEngine.ini",
  "code_preview": "[OnlineServices.Leaderboards]\nbIsTitleManaged=true\n!LeaderboardDefinitions=ClearDefinitions\n+LeaderboardDefinitions=(Name=&lt;StatName0&gt;, Id=&lt;Id0&gt;, UpdateMethod=[KeepBest | Force], OrderMethod=[Ascending | Descending])\n+LeaderboardDefinitions=(Name=&lt;StatName1&gt;, Id=&lt;Id1&gt;, UpdateMethod=[KeepBest | Force], OrderMethod=[Ascending | Descending])\n...",
  "lines_of_code": 6,
  "id": 150460,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1MiswMDowMCJ9--c07eab63e4892f653e26ca897fa2bbf2dd862075623d9d1b7e1af3cc36e97aa3",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "In order for leaderboards to update based on stats changes, you must set the <code>bIsTitleManaged</code> flag to <code>true</code>. This flag configures the client to listen for the Online Services Stats Interface's <code>FStatsUpdated</code> event to automatically update leaderboards in response to stats changes. The <code>bIsTitleManaged</code> flag's default value is <code>false</code>. If you do not set this flag to <code>true</code>, leaderboards will not automatically update based on stat changes configured in the leaderboard definitions in <code>DefaultEngine.ini</code>.",
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

The following [Leaderboard Definition](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5) table explains the syntax for adding a leaderboard definition to an engine configuration file.

#### Leaderboard Definition

| Field | Type | Description |
| --- | --- | --- |
| `Name` | `String` | Name of the stat that determines ranking. This must be the same as the name of a stat configured with the stats interface. |
| `Id` | `int` | ID number to associate with this leaderboard. This is not related to the stats ID from the stats interface. |
| `UpdateMethod` | `KeepBest` or `Force` | The method used to update this leaderboard entry. `KeepBest` keeps the best value for this stat that has been achieved. `Force` updates the leaderboard entry to the latest stat value, regardless of how it changes a player's rank. |
| `OrderMethod` | `Ascending` or `Descending` | Determines whether a lower or higher stat value gives a better ranking. `Ascending` means a lower stat value gives a higher rank. `Descending` means a higher stat value gives a higher rank. |

### Configuration Example

Suppose that you have a simple game with a single leaderboard titled "Total Game Points" tracked by a statistic of the same name configured with the stats interface:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "DefaultEngine.ini",
  "code_preview": "[OnlineServices.Stats]\n!StatDefinitions=ClearDefinitions\n+StatDefinitions=(Name=Total_Game_Points, Id=0, ModifyMethod=Sum)\n\n[OnlineServices.Leaderboards]\nbIsTitleManaged=true\n!LeaderboardDefinitions=ClearDefinitions\n+LeaderboardDefinitions=(Name=Total_Game_Points, Id=0, UpdateMethod=KeepBest, OrderMethod=Descending)",
  "lines_of_code": 8,
  "id": 150461,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1MiswMDowMCJ9--f67163116aeadc0fed10705f7785062d8284df61ff0b9c487adaa610716dd5a9",
  "settings": {
    "is_hidden": false
  }
}
```

In this configuration, the leaderboard:

- keeps the best score for the `Total_Game_Points` statistic for each player, and
- is organized in descending order, since higher point totals are more desirable.

## Read Leaderboard Entries

There are three different ways to read leaderboard entries with the leaderboards interface. Leaderboard entries can be read in the following ways:

- [For specific users](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5)
- [Around a particular rank](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5)
- [Around a given user](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5)

Below we show a visual representation of what each of these methods retrieves with the "Total Game Points" leaderboard configured in the [configuration example](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5) above.

### For Specific Users

Use the `ReadEntriesForUsers` function to retrieve leaderboard entries for specific users. This function takes in a list of user IDs for the individual users whose rank you wish to query.

#### Example

Suppose that you have the leaderboard below titled "Total Game Points" and call `ReadEntriesForUsers` with the following parameters:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UE::Online::FReadEntriesForUsers::Params Params;\nParams.LocalAccountId = &quot;LLV54WB-3C678QQ&quot;;\nParams.AccountIds = {&quot;9P8H4GQ-HNO5GA4&quot;, &quot;3CN9H8E-VNO3G3C&quot;, &quot;OHB8RA2-OHSEBSE&quot;};\nParams.BoardName = TEXT(&quot;Total Game Points&quot;);",
  "lines_of_code": 4,
  "id": 150462,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1MiswMDowMCJ9--927580ad996b36cf2dc2f1c7262226abf850622aa50f9cf27c4f7bd57be67942",
  "settings": {
    "is_hidden": false
  }
}
```

If the call returns successfully, you can access the columns marked as retrieved in the returned `TOnlineResult`:

| Total Game Points |   |   |   |
| --- | --- | --- | --- |
| **Account ID** | **Rank** | **Score** | **Retrieved?** |
| 3CN9H8E-VNO3G3C | 1 | 1,901 | Y |
| LLV54WB-3C678QQ | 2 | 151 |   |
| OHB8RA2-OHSEBSE | 3 | 17 | Y |
| 9P8H4GQ-HNO5GA4 | 4 | 3 | Y |
| 9HQGQER-ILASDFH | 5 | 1 |   |

### Around a Particular Rank

Use the `ReadEntriesAroundRank` function to retrieve leaderboard entries around a particular leaderboard rank. This function takes in:

- a rank at which you want to start reading leaderboard entries, and
- a limit for the number of entries to read.

#### Example

Suppose that you have the leaderboard below titled Total Game Points and call `ReadEntriesAroundRank` with the following parameters:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UE::Online::FReadEntriesAroundRank::Params Params;\nParams.LocalAccountId = &quot;LLV54WB-3C678QQ&quot;;\nParams.Rank = 2;\nParams.Limit = 2;\nParams.BoardName = TEXT(&quot;Total Game Points&quot;);",
  "lines_of_code": 5,
  "id": 150463,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NjMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1MiswMDowMCJ9--a819f37eabd71f0da7c5ef360191d305c5240fa9ade897e96163a29c6dc25ed5",
  "settings": {
    "is_hidden": false
  }
}
```

If the call returns successfully, you can access the columns marked as retrieved in the returned `TOnlineResult`:

| Total Game Points |   |   |   |
| --- | --- | --- | --- |
| **Account ID** | **Rank** | **Score** | **Retrieved?** |
| 3CN9H8E-VNO3G3C | 1 | 1,901 |   |
| LLV54WB-3C678QQ | 2 | 151 |   |
| OHB8RA2-OHSEBSE | 3 | 17 | Y |
| 9P8H4GQ-HNO5GA4 | 4 | 3 | Y |
| 9HQGQER-ILASDFH | 5 | 1 |   |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "From a programming perspective, the rank of the top of a leaderboard is 0, not 1. As a result of this, to retrieve the entry in third place, <code>ReadEntriesAroundRank</code> needs to be called with <code>Params.Rank = 2</code>.",
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

### Around a Given User

Use the `ReadEntriesAroundUser` function to retrieve leaderboard entries around a particular user. This function takes in:

- the user around which you want to read entries,
- an offset to indicate where to start reading entries, and
- a limit for the total number of entries to read.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The offset can exceed the limit. In this case, the provided user will not be present in the returned array of leaderboard entries. This can be useful when organizing leaderboard entries into pages for viewing.",
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

#### Example

Suppose that you have the leaderboard below titled Total Game Points and call `ReadEntriesAroundUser` with the following parameters:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UE::Online::FReadEntriesAroundUser::Params Params;\nParams.LocalAccountId = &quot;LLV54WB-3C678QQ&quot;;\nParams.Offset = -1;\nParams.Limit = 3;\nParams.BoardName = TEXT(&quot;Total Game Points&quot;);",
  "lines_of_code": 5,
  "id": 150464,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NjQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1MiswMDowMCJ9--779f13cfc43c22104248a2f9db2e2eca9dd8b7c4ffd994757ec6a59c95958252",
  "settings": {
    "is_hidden": false
  }
}
```

If the call returns successfully, you can access the columns marked as retrieved in the returned `TOnlineResult`:

| Total Game Points |   |   |   |
| --- | --- | --- | --- |
| **Account ID** | **Rank** | **Score** | **Retrieved?** |
| 3CN9H8E-VNO3G3C | 1 | 1,901 | Y |
| LLV54WB-3C678QQ | 2 | 151 | Y |
| OHB8RA2-OHSEBSE | 3 | 17 | Y |
| 9P8H4GQ-HNO5GA4 | 4 | 3 |   |
| 9HQGQER-ILASDFH | 5 | 1 |   |

## More Information

### Header File

Consult the `Leaderboards.h` header file directly for more information as needed. The Leaderboards Interface header file `Leaderboards.h` is located in the directory:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UNREAL_ENGINE_ROOT\\Engine\\Plugins\\Online\\OnlineServices\\Source\\OnlineServicesInterface\\Public\\Online",
  "lines_of_code": 1,
  "id": 150465,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NjUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1MiswMDowMCJ9--07e25e88fa24e3d68db6779ea160eeb9f5485a1c79371cf4915d9447a781a85e",
  "settings": {
    "is_hidden": false
  }
}
```

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

See the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.
