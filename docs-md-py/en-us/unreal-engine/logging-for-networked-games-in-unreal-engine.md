# Logging

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/logging-for-networked-games-in-unreal-engine

> Application Version: 5.7

## Logging for Networked Games

**Client** and **Server** logs are important for identifying and debugging networking issues. While many networking logs fall into the **LogNet** category, we recommend checking log categories that are more closely related to specific systems to provide greater insight into any issues.

These categories are not enabled by default and have varying amounts of verbosity that you may need to adjust to gain information about the behavior you're experiencing. The list below provides some recommended categories:

| Category | Description |
| --- | --- |
| **LogNetTraffic** | Logs all network traffic when this log variable is set to VeryVerbose. |
| **LogNetPackageMap** | Logs information related to how NetGUIDs are Sent, Received, and Acknowledged. |
| **LogNetVersion** **LogNetFastTArray** **LogNetDormancy** **LogRep** **LogRepTraffic** | Logs information related to Property Replication and RepNotify functions that are used by FRepLayout and FObjectReplicator. |
| **LogRepProperties** | Logs information related to the sending and receiving of replicated properties. |
| **PacketHandlerLog** | Logs information on the packet handler and its components. These components have their own sub-categories. For example, LogDTLSHandler, OodleNetworkHandlerComponentLog, and LogHandshake. |
| **LogDemo** | Logs information on recording and playing back replays. Each replay streamer has a related log category: LogLocalFileReplay, LogSaveGameReplay, LogNullReplay, and LogMemoryReplay. |

You can enable these log categories and adjust their verbosity by the following methods:

### Command-Line Argument

Pass the `LogCmds` command line argument:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "-LogCmds=&quot;&lt;LOG_CATEGORY&gt; &lt;LOG_VERBOSITY&gt;&quot;",
  "lines_of_code": 1,
  "id": 59777,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1OTc3NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjIxKzAwOjAwIn0=--785b109ed8aac878703dcc6f15b6dda7e9b0ce869a21905a9dc3c4bbb7dbb4e0",
  "settings": {
    "is_hidden": false
  }
}
```

For example, to set `LogNetTraffic` to `VeryVerbose`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "-LogCmds=&quot;LogNetTraffic VeryVerbose&quot;",
  "lines_of_code": 1,
  "id": 59778,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1OTc3OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjIxKzAwOjAwIn0=--b5687815df8df7bb5edf33a213673ea3b131d8a0e20315c893a9558d5206a9f4",
  "settings": {
    "is_hidden": false
  }
}
```

### Console Command

Use the `Log` console command:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Log &lt;LOG_CATEGORY&gt; &lt;LOG_VERBOSITY&gt;",
  "lines_of_code": 1,
  "id": 59779,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1OTc3OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjIxKzAwOjAwIn0=--5d153ca077a2f7aef7fd016903b11212b316ff61991d40a345be0c27e48bdcae",
  "settings": {
    "is_hidden": false
  }
}
```

For example, to set `LogNetTraffic` to `Verbose`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Log LogNetTraffic Verbose",
  "lines_of_code": 1,
  "id": 59780,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1OTc4MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjIxKzAwOjAwIn0=--34bf27d8039c57fb7abb3e02048a9a2ee30d17e6accee5759dfea3443cfa38d0",
  "settings": {
    "is_hidden": false
  }
}
```

### Engine Configuration

Set them in your project's `DefaultEngine.ini.`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[Core.Log]\n&lt;LOG_CATEGORY1&gt;=&lt;LOG_VERBOSITY1&gt;\n&lt;LOG_CATEGORY2&gt;=&lt;LOG_VERBOSITY2&gt;\n...",
  "lines_of_code": 4,
  "id": 59781,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1OTc4MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjIxKzAwOjAwIn0=--c493090993b2d9431c9fca991c64b10202ed7520461f9c02ba22ed58b19c9d51",
  "settings": {
    "is_hidden": false
  }
}
```

For example, to set multiple categories to different verbosities:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[Core.Log]\nLogNetPackageMap=Log\nLogNetTraffic=Verbose\nLogRep=VeryVerbose",
  "lines_of_code": 4,
  "id": 59782,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1OTc4MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjIxKzAwOjAwIn0=--7f105f6ee0c7941b47c0e6dc51898adb0ff6c7a6d21d672384ee111a0a231955",
  "settings": {
    "is_hidden": false
  }
}
```

## Helpful Errors

When reading logs, the following list can be useful for determining what kind of error occurred.

| **UEngine::BroadcastNetworkFailure** | Printed when a net driver encounters some major error. The log line will include the failure type, the error string, and the description of the net driver that encountered the error. You can see a list of the possible network failures with brief descriptions in the ENetworkFailure enum in EngineBaseTypes.h. |
| --- | --- |
| **UNetConnection::Close** | A description of the connection being closed. |
| **UActorChannel::Close** | A LogNetTraffic category that will include the channel index, the Actor for that channel, and the reason it was closed. Checking the logs around these lines can help provide some indication as to why a connection or Actor channel was closed. |

The command-line argument `-LogTrace=<PARTIAL_LOG_LINE>` performs stack traces from partial log message strings. For example: `-LogTrace=UNetConnection::Close` will produce a stack trace whenever `UNetConnection::Close` is printed to the logs. The command-line argument `-DumpRPCs` provides the capability to dump RPCs and their parameters, which can be useful for tracking what RPCs are being sent and their parameters.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "LogTrace and DumpRPCs both require <strong>NetcodeUnitTest</strong> to be enabled.",
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
