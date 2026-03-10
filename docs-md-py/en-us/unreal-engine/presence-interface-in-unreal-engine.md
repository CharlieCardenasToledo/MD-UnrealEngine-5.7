# Online Services Presence Interface

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine

> Application Version: 5.7

When logged into an online service, you may want to look for information about your friends and other users you have met online. For example, on many online services, you can see whether other users are online, what game they are currently playing, if they are available to join matches, and so on. The **Online Services Presence Interface** encompasses all functionality related to platform-specific user states across online services, including querying and updating a user's presence as well as listening for changes.

This document provides an API overview and code examples as well as tips for converting code from the [Online Subsystem Presence Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-presence-interface-in-unreal-engine).

## API Overview

### Functions

The following table provides a high-level description of the functions included in the Presence Interface.

| Function | Description |
| --- | --- |
| **Query** |   |
| [QueryPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/QueryPresence?application_version=5.5) | Fetch the presence of the user with the supplied `TargetAccountId`. |
| [BatchQueryPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/BatchQueryPresence?application_version=5.5) | Fetch the presence for every user in the supplied list of `TargetAccountIds`. |
| **Get** |   |
| [GetCachedPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/GetCachedPresence?application_version=5.5) | Retrieve the presence of the user with the supplied `TargetAccountId` cached in the interface. |
| **Update** |   |
| [UpdatePresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/UpdatePresence?application_version=5.5) | Update the presence of the user. |
| [PartialUpdatePresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/PartialUpdatePresence?application_version=5.5) | Update the presence of the user with only the specified presence settings. |
| **Event Listening** |   |
| [OnPresenceUpdated](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/OnPresenceUpdated?application_version=5.5) | Event will trigger as a result of updates to a user's presence. |

### Enumeration Classes

The Presence Interface defines three enumeration classes that represent a user's status ([EUserPresenceStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EUserPresenceStatus?application_version=5.5)), joinability ([EUserPresenceJoinability](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EUserPresenceJoinabi-?application_version=5.5)), and game status ([EUserPresenceGameStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EUserPresenceGameSta-?application_version=5.5)). These enumeration classes represent three primary members of the `FUserPresence` struct. For more information, refer to the [Primary Struct](https://dev.epicgames.com/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.5) section of this page.

#### EUserPresenceStatus

| Enumerator | Description |
| --- | --- |
| `Offline` | User is offline. |
| `Online` | User is online. |
| `Away` | User is away. |
| `ExtendedAway` | User has been away for at least two hours (may be platform dependent). |
| `DoNotDisturb` | User does not want to be disturbed. |
| `Unknown` | Default user presence status. |

#### EUserPresenceJoinability

| Enumerator | Description |
| --- | --- |
| `Public` | Anyone can discover and join this session. |
| `FriendsOnly` | Anyone trying to join must be a friend of a lobby member. |
| `InviteOnly` | Anyone trying to join must be invited first. |
| `Private` | User is not currently accepting invitations. |
| `Unknown` | Default user presence joinability status. |

#### EUserPresenceGameStatus

| Enumerator | Description |
| --- | --- |
| `PlayingThisGame` | User is playing the same game as you. |
| `PlayingOtherGame` | User is playing a different game than you. |
| `Unknown` | Default user presence game status. |

### Primary Struct

#### FUserPresence

The [FUserPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FUserPresence?application_version=5.5) struct is the primary object in the Presence interface and consists of all necessary information pertaining to a user's presence.

| Member | Type | Description |
| --- | --- | --- |
| `AccountId` | `FAccountId` | User whose presence this is. |
| `Status` | `EUserPresenceStatus` | User presence state. (Default value is `EUserPresenceStatus::Unknown`.) |
| `Joinability` | `EUserPresenceJoinability` | User session state. (Default value is `EUserPresenceJoinability::Unknown`.) |
| `GameStatus` | `EUserPresenceGameStatus` | User game state. (Default value is `EUserPresenceGameStatus::Unknown`.) |
| `StatusString` | `FString` | String representation of user presence state. |
| `RichPresenceString` | `FString` | Game-defined representation of the current game state. |
| `Properties` | `FPresenceProperties` | Session keys. |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The type <code>FPresenceProperties</code> is a typedef for <code>TMap&lt;FString, FPresenceVariant&gt;</code> where <code>FPresenceVariant</code> is an <code>FString</code>.",
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

## Examples

We now provide an example demonstrating `UpdatePresence`, `QueryPresence`, and `GetPresence`. `UserA` updates their presence with the default platform services, then `UserB` queries the presence of `UserA` after it has been updated. If the query successfully returns, then `UserB` retrieves the presence of `UserA`.

### Code

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "UserAPresence.cpp",
  "code_preview": "UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();\nUE::Online::IPresencePtr PresenceInterface = OnlineServices-&gt;GetPresenceInterface();\n\nTSharedRef&lt;UE::Online::FUserPresence&gt; Presence = MakeShared&lt;UE::Online::FUserPresence&gt;();\nPresence-&gt;AccountId = UserA;\nPresence-&gt;Status = UE::Online::EUserPresenceStatus::Online;\nPresence-&gt;Joinability = UE::Online::EUserPresenceJoinability::Public;\nPresence-&gt;RichPresenceString = TEXT(&quot;Exploring the Great Citadel&quot;);\nPresence-&gt;Properties.Add(TEXT(&quot;advanced_class&quot;), TEXT(&quot;advanced_class_assassin&quot;));\n\n",
  "lines_of_code": 26,
  "id": 150472,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NzIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NCswMDowMCJ9--b34e0ec310753f59f0098fbec5db29ae8f555e8dac7d7041799850ea2e5c8bb1",
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
  "title": "UserBPresence.cpp",
  "code_preview": "UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();\nUE::Online::IPresencePtr PresenceInterface = OnlineServices-&gt;GetPresenceInterface();\n\nPresenceInterface-&gt;QueryPresence({UserA})\n.OnComplete([](const UE::Online::TOnlineResult&lt;UE::Online::FQueryPresence&gt; Result)\n{\n\tif(Result.IsOk())\n\t{\n\t\t// we succeeded - now use GetPresence to actually view the presence object\n\n",
  "lines_of_code": 30,
  "id": 150473,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NzMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NCswMDowMCJ9--f6878617b464c71fe58096fa27ef574d901d149ee2733184dd5f9d87c2292a98",
  "settings": {
    "is_hidden": false
  }
}
```

### Walkthrough

1. Both users retrieve the default online services by calling `GetServices` with no parameters specified and access the Presence Interface:
2. `UserA` initializes an `FUserPresence` struct named `Presence`. Notice that we are using two of the aforementioned enumerations provided by the Presence Interface: `EUserPresenceStatus` and `EUserPresenceJoinability`.
3. `UserA` initializes an `FUpdatePresence::Params` struct named `Params` with the parameters that will be passed to `UpdatePresence`:
4. `UserA` calls `UpdatePresence` and processes the result with an `OnComplete` callback:
5. `UserB` queries the presence of `UserA`. Inside the queries' `OnComplete` callback, `UserB` first checks to ensure `QueryPresence` returned an "Ok" status. If it did, then `UserB` is safe to retrieve the presence of `UserA` and process the result or error of `GetPresence` accordingly:

If all function calls return without error, `UserB` now sees the updated status of `UserA` and `UserB` can choose to make decisions based on this status. For example, `UserB` could access the `GetPresenceResult` to see `UserA` is online and their joinability status is public. Upon setting this status `UserB` could decide to join `UserA` and "Explore the Great Citadel" together.

## Converting Code from Online Subsystem

The [Online Services](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-services-in-unreal-engine) plugins are an updated version of the [Online Subsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-in-unreal-engine) plugins and will exist alongside one another for the foreseeable future. The API functionality of the Online Services Presence Interface maps approximately one-to-one with the API functionality of the Online Subsystem Presence Interface. A few caveats include:

- `SetPresence` was renamed to `UpdatePresence` to better represent the function's asynchronicity.
- `UpdatePresence` and `QueryPresence` are no longer overloaded.
- We recommend using their renamed functions `PartialUpdatePresence` and `BatchQueryPresence` instead. The overloads for `UpdatePresence` and `QueryPresence` were renamed to `PartialUpdatePresence` and `BatchQueryPresence`, respectively.
- `QueryPresence` was given the `bListenToChanges` parameter. This adds a specific user to the `OnPresenceUpdated` event. The parameter is set to true by default.

## More Information

### Header File

Consult the `Presence.h` header file directly for more information as needed. The Presence Interface header file `Presence.h` is located in the directory:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Engine\\Plugins\\Online\\OnlineServices\\Source\\OnlineServicesInterface\\Public\\Online",
  "lines_of_code": 1,
  "id": 150479,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA0NzksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1NCswMDowMCJ9--e8ee9614ee298abfeae96b65fc878b3b32a7948c0ca7d11cf05a51f7bc21fef5",
  "settings": {
    "is_hidden": false
  }
}
```

For instructions on how to obtain the UE source code, refer to our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

Refer to the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.
