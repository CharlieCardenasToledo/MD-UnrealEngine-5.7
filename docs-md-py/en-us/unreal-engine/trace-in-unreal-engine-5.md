# Trace

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/trace-in-unreal-engine-5

> Application Version: 5.7

**Trace** is a structured logging framework for tracing instrumentation events from a running process. The modules **TraceLog** and **TraceAnalysis** are the principal modules that constitute the framework.
The **Unreal Trace Server** runs in the background as a single server instance and can be shared between multiple projects or branches. It is an optimized program that has minimal impact on performance and does not include a user interface.

The Trace Server launches automatically by a separate server process, `UnrealTraceServer.exe`, which is located in the `Engine/Binaries/Win64` directory folder.

![insights-major-components-diagram](https://dev.epicgames.com/community/api/documentation/image/68c9bfb7-53a6-4103-812b-4b800ddc3aee)

The Trace Server has two components:

- The **Trace Recorder** listens on port 1981 for incoming trace connections and records the live trace stream.
- The **Trace Store** stores the recorded traces as files in a folder. It watches this folder for changes and exposes the list of available traces to Unreal Insights UI.

An example of the path to the trace folder is:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "C:/Users/&lt;user&gt;/AppData/Local/UnrealEngine/Common/UnrealTrace/Store/001/",
  "lines_of_code": 1,
  "id": 109853,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDk4NTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyOTozMyswMDowMCJ9--5e6acb5d526699f5f9c7ad3e6cfd054bc9967229126646757146ffb80b9de761",
  "settings": {
    "is_hidden": false
  }
}
```

## Unreal Trace Server

Unreal Editor builds automatically launch the `UnrealTraceServer.exe`, when you make a connection from the Unreal Trace session browser. The Unreal Trace Server runs in the background as a single server instance and can be shared between multiple projects and branches.

![trace-executable](https://dev.epicgames.com/community/api/documentation/image/35d0f92b-b520-4f70-a0fa-b723afe91304)

You can shut down Unreal Trace Server by accessing your system's Task Manager, and navigating to the Processes tab.

![task-manager](https://dev.epicgames.com/community/api/documentation/image/cb96addd-1279-4cd7-a410-bdc3524e1bc2)

Unreal Trace Server runs in the background as a single instance that does not need to be terminated in order to launch a new version. It can receive and record data from multiple sources simultaneously.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Currently, we only support Unreal Trace Server for one user per machine. If multiple users are logged in simultaneously, then traces will be stored in the first user's trace directory, therefore leaving them inaccessible to other users.",
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

## Trace Insights Widget

The **Trace Insights Widget** provides a way to control and manage your **Trace Data** using an Editor interface. You can access the **Trace Insights Widget** from the Editorby navigating to the bottom toolbar and clicking the **Trace** button.

![Trace Button](https://dev.epicgames.com/community/api/documentation/image/7052ff6c-a02f-46e9-a6eb-7c27e1ee3905)

The follows sections describe settings within each category of the Trace menu.

### Trace Data

The **Trace Data** category contains settings on data channels, Trace bookmarks, Trace screenshots, and more.

![Trace Data](https://dev.epicgames.com/community/api/documentation/image/d356fef9-0e03-4efe-aca4-087411ae0e4a)

#### Channels

Trace is capable of recording large amounts of data. You can choose which type of data to record by using **Trace Channels**.

Channels control the data rate when tracing. Each event type is tied to one or more channels. If the required channels are not enabled then the event will not be emitted to the trace stream.

![Trace Channels](https://dev.epicgames.com/community/api/documentation/image/ebb6e42a-ac35-4b6d-b6a6-a20ee3595a4b)

**Channel presets** group channels together to provide scenario-based entry points.

```json
{
  "type": "include",
  "excerpt_id": 2511,
  "excerpt_assignment_id": 1868,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Channel",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Description",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Animation</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Animation Insights Plugin.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>AssetLoadTime</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Contains named CPU timers for <code class=\"inline-code\">UObject::Serialize</code>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>AssetMetadata</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Asset Names and Class Names as metadata for memory allocations. Requires <strong>Metadata</strong> channel. Used by <strong>Memalloc</strong> channel.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Audio</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Audio Insights Plugin.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>AudioMixer</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "AudioMixer Insights Plugin.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Bookmark</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Low-frequency markers to signify important transitions. Bookmarks provide a quick overview of features such as level loading or engine boot phases.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Callstack</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Callstack descriptions. Allows allocations to be associated with callstacks.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>ContextSwitch</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Trace context switch events. On Windows, game or editor runtime should be run as administrator.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Cook</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Displays named CPU timers specific to cooking. This requires the CPU channel to be enabled. Cook will add the both the <code>CookByTheBook</code> and <code>SaveCookedPackage</code> CPU timing events.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Counters</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Generic counters. Traces float and integer values over time. Counters Trace API. It enables the CSV Profiler Trace.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Cpu</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Named CPU timers. Additional timers can be added by enabling the Stat Named Events channel from the Insights Widget or using the <code>-statnamedevents</code> command line argument.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>File</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "File I/O trace channel that contains Open, ReOpen, Read, Write, Close events.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Frame</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Game and Rendering frames.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Gpu</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Named GPU timers. Based on GpuProfiler data.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>LoadTime</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Asset Loading Insights trace channel. Only works for runtime loading from the pak/iostore.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Log</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Logs Messages.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>MemAlloc</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Memory allocations. Uses Module and Callstack.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>MemTag</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Memory tag statistics. Traces snapshots of memory usage per tag at regular rate. Relies on LLM subsystem for tracing. Implies \"-llm\". Available after <code>Init()</code>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Messaging</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "UDP Messaging plugin.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Metadata</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Support for generic metadata scopes.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Module</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Module loading information.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Net</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Networking trace channel.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Niagara</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Niagara Plugin.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Object</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "GameplayInsights/RewindDebugger plugin. <code>UObject</code> classes, worlds, instances, and events.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Physics</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<a data-document-id=\"3229676\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine\">Chaos Visual Debugger</a>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>RDG</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "RDG Insights Plugin.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>RHICommands</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "CPU or GPU named timers for RHI commands.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>RenderCommands</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "CPU or GPU named timers for commands executed on the rendering thread.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>SaveTime</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Named CPU timers specific to package saving.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Screenshot</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Captures screenshots triggered with <code>Trace.Screenshot</code> console command or using the  <code>TRACE_SCREENSHOT()</code> API.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Slate</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Slate Insights Plugin.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>StackSampling</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Trace stack sampling events based on Event Tracing for Windows (ETW).",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Stats</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Stats counters. Based on the Stats system.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Task</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Task Graph trace channel.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>VisualLogger</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Visual Logger starts recording to file.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "n3oX",
  "settings": {
    "is_hidden": false
  }
}
```

The following channels are enabled by default:

- Bookmark
- Cpu
- Frame
- Gpu
- Log
- Region
- Screenshot

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The MemAlloc, MemTag, and Module channels are grey because they must be run from the command the prompt. See <a data-document-id=\"3234851\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/trace-in-unreal-engine-5\">From the Command Prompt</a>",
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

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can define your own presets using config files added to the <code>[Trace.ChannelPresets]</code> category. See the <a data-document-id=\"3234852\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/developer-guide-to-tracing-in-unreal-engine\">Trace Developer Guide</a> for documentation.",
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

#### Trace Screenshot

**Trace Screenshot** takes a picture of your project's viewport during that frame and sends it to the trace. By default, Trace Screenshot is enabled from the channel panel.   
  
You can take a Trace Screenshot in two ways:

- In the bottom toolbar, click **Trace >** **Trace Screenshot**. ![Trace Screenshot](https://dev.epicgames.com/community/api/documentation/image/d2c1826d-cca4-4cc2-977a-0587338564e6)
- In the console, enter the command `trace.screenshot`.

When using Trace Screenshot, the Timing Insights timeline displays a vertical line that contains a name generated based on the current timestamp, using the date and time of your screenshot.

![trace-screenshot](https://dev.epicgames.com/community/api/documentation/image/5b655993-9594-4ce6-acce-5e770b771b75)

#### Trace Bookmark

**Trace Bookmark** emits a `TRACE_BOOKMARK()` event with the given string name. When used from the Editor, both the screenshot and bookmark events will generate a name based on the current timestamp using the format of date and time.  
  
You can set a Trace Bookmark in two ways:

- In the bottom toolbar, click **Trace > Trace Bookmark**. ![Trace Bookmark](https://dev.epicgames.com/community/api/documentation/image/70347ac8-262b-475c-bea4-382ae874b6b7)
- In the console, enter the command `trace.bookmark`.

Bookmarks and screenshots are visible in the **Timing Insights** tab. You can find them in the **markers track** docked on the top toolbar, underneath the **ruler track**. Bookmarks are available in the **Log** view.

![trace-bookmark](https://dev.epicgames.com/community/api/documentation/image/647f856e-a772-423c-b370-02003b8e6e50)

![log-window](https://dev.epicgames.com/community/api/documentation/image/d5d9d94e-7914-466b-814b-9509336a11db)

#### Stat Named Events

**Stat Named Events** provide additional profiling metrics. You can enable or disable them by clicking the **State Named Events** checkbox.

![stat-named-events](https://dev.epicgames.com/community/api/documentation/image/4958e11a-6525-4ee0-9998-31863e02fe25)

### Trace Destination

In the **Trace Destination** category, you can choose where to store your trace data.

![Trace Destination](https://dev.epicgames.com/community/api/documentation/image/3fb02c95-b3b8-47ae-88c2-cb30a1110a15)

| Option | Description |
| --- | --- |
| **Trace Store** | Writes the trace data to a file in its managed trace store directory. |
| **File** | Writes trace data directly to the specified file. |

### Tracing

The **Tracing** category contains settings for starting and stopping a recording, and saving Trace Snapshots.

![Tracing](https://dev.epicgames.com/community/api/documentation/image/54bb62f6-da4f-4733-87b0-43c5eff7d186)

#### Start and Stop Recording

| Option | Description |
| --- | --- |
| **Start Trace** | Starts a trace to the selected trace destination. You can start a trace from the Trace Insights widget by clicking the **Start Trace** button. |
| **Stop Trace** | When a Trace is started, the Start Trace UI icon displays in red. You can stop the trace from recording by clicking the **Stop Trace** button. |

#### Save Trace Snapshot

There are two ways to save a **Trace Snapshot**:

- In the bottom toolbar, click the **Save Trace Snapshot** button. ![save-snapshot-button](https://dev.epicgames.com/community/api/documentation/image/2c6f9238-64b1-4c57-85e2-13d8ad0564dc)
- In the bottom toolbar, click **Trace** **>** **Save Trace Snapshot**. ![Save Trace Snapshot](https://dev.epicgames.com/community/api/documentation/image/63e6e88d-6842-452b-bbb9-e9204099fcdc)

### Options

The **Options** category controls automation, such as automatically opening Unreal Insights or destination folders.

![Options](https://dev.epicgames.com/community/api/documentation/image/87bf2244-a899-42e4-9648-37b63d6d6d5a)

| Option | Description |
| --- | --- |
| **Open Live Session on Trace Start** | When tracing is started, the live session automatically opens in Unreal Insights. |
| **Open Insights after Trace** | When tracing is stopped or a snapshot is saved, the recorded session automatically opens in Unreal Insights. |
| **Shown in Explorer after Trace** | When tracing is stopped or a snapshot is saved, the folder containing the recorded session automatically opens. |

### Locations

The **Locations** category controls where traces (saved to File and the Trace Server) are stored.

![Locations](https://dev.epicgames.com/community/api/documentation/image/ce94db35-eb28-4816-8eb2-6bdded63f6a3)

| Option | Description |
| --- | --- |
| **Open Trace Store Directory** | The location where traces saved to the Trace Server are stored. |
| **Open Profiling Directory** | Opens the profiling directory of the current project. This is the location where traces to the file are stored. |

### Insights

The **Insights** category contains settings that open Unreal Insights, live sessions, and recorded files.

![Insights](https://dev.epicgames.com/community/api/documentation/image/a6cce4c3-2da2-461c-bb6d-4b559d2b00e6)

| Option | Description |
| --- | --- |
| **Unreal Insights**(**Session Browser**) | Launches the Unreal Insights Session Browser. |
| **Open Live Session** | Opens the current live session. This is only possible when tracing to the store. |
| **Recent Traces** | Opens the latest traces recorded to the trace store or as a file. |

## Trace Status

You can check information about your **Connection**, **Memory Used**, **Important Events cache**, **Sent** data, **Enabled** and **Available** Trace channels by using the console command `Trace.Status`.

![trace-status](https://dev.epicgames.com/community/api/documentation/image/9ad1cc36-29b9-4107-80d7-fe51d1d1b675)

## Run Insights From the Command Prompt

To run Unreal Insights from the Command Prompt, follow these steps:

1. Navigate to your `Engine\Binaries\Win64` folder and double-click `UnrealInsights.exe`. ![unreal-insights-executable-in-binaries-folder](https://dev.epicgames.com/community/api/documentation/image/5b618536-1e69-4eed-9a40-f358b21347ee)
2. Launch the **Command Prompt** from your operating system and run your project. In the following example, replace the installation path and project name with your own:

## Tail Tracing

**Tail Tracing** tracks events over the last few seconds (depending on the buffer size). Therefore, any machines that may be able to display a lead-up.

The default size of the buffer is 4MB, however if you wish to modify or deactivate it, you can do so by entering using the console command `-tracetailmb=X`.

Setting **X** to **0 MB** will deactivate it and other values will change the buffer size accordingly.

## Late Connect

**Important events** are cached on the Unreal Engine client side, then sent to late-connecting machines during connection. Therefore, one-time events (Important Events) won't be missed before you can make a connection.

Insights can instruct remote running Unreal Engine instances to connect to the remote trace servers from its local UI instance without needing to involve the local machine.

Late connect can be initiated by navigating to **Unreal Insights** **>** **Connect**, or from the Editor console by entering any of the following commands or arguments:

- `"trace.send [ip]" / "trace.start [filename]"`
- `-trace.start [file] [channelSet] -tracehost=[ip]`
- `-tracefile = [filepath]`

Unreal Insights has a file-based caching system that makes it possible for the application to attach additional information to a trace. This can be used to retrieve previously calculated results faster, or store data that would otherwise be lost such as symbols. The cache is stored in a `.ucache` file next to the trace file.

## Trace User Guide

You can use different workflows to run traces in Unreal Insights. See the [Trace User Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine) for documentation.

## Trace Developer Guide

You can develop your own traces in Unreal Insights. See the [Trace Developer Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/developer-guide-to-tracing-in-unreal-engine) for documentation.
