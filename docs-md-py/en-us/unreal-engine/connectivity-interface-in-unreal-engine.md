# Connectivity Interface

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine

> Application Version: 5.7

The **Online Services** **Connectivity Interface** provides you with tools to determine whether your game is connected to your platform's backend online services.

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the Connectivity Interface:

| Function | Description |
| --- | --- |
| [GetConnectionStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IConnectivity/GetConnectionStatus?application_version=5.5) | Retrieve the connection status for the provided online service. |
| [OnConnectionStatusChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IConnectivity/OnConnectionStat-?application_version=5.5) | The event triggered when an online service connection status changes. |

### Enumerated Classes

Online service connection status is represented by the [EOnlineServicesConnectionStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EOnl-?application_version=5.5) enumerated class.

#### EOnlineServicesConnectionStatus

| Value | Description |
| --- | --- |
| `Connected` | Connected to the online services. |
| `NotConnected` | Not connected to the online services. |

## Connection Status

`GetConnectionStatus` returns the current connection status for the provided online service. Some online services consist of multiple underlying microservices. Use the name of one of these microservices as a parameter for `GetConnectionStatus` to determine the particular microservice's connection status. If you don't specify an online service parameter, `GetConnectionStatus` returns `EOnlineServicesConnectionStatus::Connected` only if all underlying microservices are connected.

You can bind `OnConnectionStatusChanged` to events to inform you when the connection status of an online service or one of its microservices changes.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The organization of an online service and the accessibility of its particular microservices varies by platform. Consult your platform's online services documentation for more information.",
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

## More Information

### Header File

Consult the `Connectivity.h` header file directly for more information as needed. The Connectivity Interface header file `Connectivity.h` is located in the directory:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Engine\\Plugins\\Online\\OnlineServices\\Source\\OnlineServicesInterface\\Public\\Online",
  "lines_of_code": 1,
  "id": 150051,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTAwNTEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMzo1MCswMDowMCJ9--b3f5476965dd7bdfed1f93ba890cd87953cf4992fd07b5986e8c847d49884c54",
  "settings": {
    "is_hidden": false
  }
}
```

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

Refer to the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.
