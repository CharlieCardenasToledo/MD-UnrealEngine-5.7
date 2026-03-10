# Capturing Data with Chaos Visual Debugger

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger

> Application Version: 5.7

In the following tutorials, you’ll use **[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**) to capture and play back recordings for targets on local or remote machines, including:

- Game clients and servers
- Packaged builds
- Play-in-editor sessions

![CVD Capture City Sample](https://dev.epicgames.com/community/api/documentation/image/97c3aa7c-65a2-4180-bdaf-3cc595369703)

## Data Channels

CVD records a considerable amount of data from several systems. The more complex a scene is, the larger the CVD file becomes — which can impact performance. To manage file size, you can opt-out of recording certain data by toggling the **data channels**.

Data channels control which simulation stages or data visualization flags that CVD records.

To toggle data channels, click **Data Channels** in the main toolbar and check the desired channels.

![Toggle Data Channels](https://dev.epicgames.com/community/api/documentation/image/3a33e243-344b-44af-9250-d54218ee1c69)

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Recording in CVD requires access to the console, such as in the <b>Test</b> or <b>Development</b> build configurations. When using the Test configuration, the CVD outliner does not display objects’ debug names. For more information on build configurations, see <a data-document-id=\"3948464\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-your-project\">Packaging Unreal Engine Projects</a>.",
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

## Session Targets

CVD describes the application or editor that you intend to record (such as a game client, game server, packaged build, or a PIE session) as a **target**. With the exception of PIE sessions, you can record one or more targets at a time, referred to as **single** or **multiple** sources.

The **Session Target** dropdown menu provides target presets to choose from when preparing to record, but you can also specify a custom target. By default, this menu is set to Local Editor — meaning that if you intend to record a local PIE session, you can leave this as is.

![Session Targets](https://dev.epicgames.com/community/api/documentation/image/0a319755-1a43-481b-bb68-6e03163c324e)

| Target | Description | Source Amount |
| --- | --- | --- |
| **Local Editor** | Records a local PIE session. | Single |
| **All Remote** | Records all instances that are not the Editor. | Multiple |
| **All Remote Servers** | Records all game servers that are not the Editor. | Multiple |
| **All Remote Clients** | Records all game clients that are not the Editor. | Multiple |
| **All** | Records all available targets. | Multiple |
| **Custom Selection** | Records a custom target or targets. | Single or Multiple |

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Recording multiple targets is useful if you are already recording a game server and game client, and need to record an additional client.",
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

## Next Up

- [Related Document](en-us/unreal-engine/recording-to-file.md)

- [Related Document](en-us/unreal-engine/live-debugging-with-chaos-visual-debugger.md)

- [Related Document](en-us/unreal-engine/playback-in-chaos-visual-debugger.md)
