# Recording to File

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/recording-to-file

> Application Version: 5.7

In this tutorial, you’ll learn how to record visualizations in **[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**) and save them as a `.utrace` file for later debugging. Recording to file is useful if you don't want the performance overhead of live playback.

For information on recording visualizations in real time, see [Recording a Live Session](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger).

## Start a Recording Using the UI

In this section you’ll learn how to record a PIE session using the Local Editor target preset, and the process to record all other target types.

### Local Editor

To record and play back a local PIE session, follow these steps:

1. In CVD, in the **Data Channels** menu, toggle the data channels you want to record. ![Toggle Data Channels](https://dev.epicgames.com/community/api/documentation/image/bc2cf5fe-e987-4a7a-ac67-39347b46adae)
2. In Unreal Editor, click the **Play** button in the main toolbar to begin a PIE session. You can choose to begin the PIE session before or after beginning a recording in CVD. ![Play Button](https://dev.epicgames.com/community/api/documentation/image/f4cb85af-8905-4e9c-b67c-edb24153b158)
3. Since the target Local Editor is already selected by default, you can begin the recording by clicking **Record to File**. While recording, this button turns into a red recording icon. ![Record To File](https://dev.epicgames.com/community/api/documentation/image/12c32f5b-191a-43bb-8da8-44503acccc1b)
4. To stop recording, hover over the recording icon and click the red square icon. ![Stop Recording](https://dev.epicgames.com/community/api/documentation/image/e56dec23-b75a-457e-ab8d-a4163192be23)
5. This process outputs a single `.utrace` file that you can load immediately after recording by clicking **Yes** in the dialog box. ![Save To File](https://dev.epicgames.com/community/api/documentation/image/b6f8a7c0-229f-472a-a121-a5073e8d0e4a)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": " If you are currently recording, you can quit an existing PIE session and begin a new one — CVD automatically connects to it.",
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

### All Other Targets

To record all other target types, follow these steps:

1. Verify that your target application or applications are running.
2. In CVD, toggle the data channels you want to record. ![Toggle Data Channels](https://dev.epicgames.com/community/api/documentation/image/0bf212ea-cc5b-4d3b-b924-398d4a886ece)
3. To select a target to record, click the **Session Target** dropdown menu in CVD’s main toolbar and choose a preset or custom target(s). ![Session Targets](https://dev.epicgames.com/community/api/documentation/image/6b4bd0cd-551a-4017-9599-1902c947d5b0)
4. To begin a recording, in CVD’s main toolbar, click the **Record to File**. While recording, this button turns into a red recording icon. ![Record To File](https://dev.epicgames.com/community/api/documentation/image/9a6bc666-28cb-4bfc-b363-3f290f8425dd)
5. To stop recording, highlight the recording icon and click the red square icon. ![Stop Recording](https://dev.epicgames.com/community/api/documentation/image/d2685b90-fc91-4c3f-8dcf-3b066306f827)

Depending on whether you record a single or multiple targets, this process outputs one or more `.utrace` files. If you record multiple targets, the dialog that prompts you to load the recording does not appear.

## (Legacy) Record to File Using the Command Line Interface

We recommend using CVD’s UI to start and end recordings, however, you can use the command line to record PIE sessions, game clients and servers, and packaged builds.

### Enable a Data Channel

1. To modify data channels, open the command line in the target application. In a packaged build, press **Backtick** (`).
2. Enter the following console command, replacing `[newstate]` with true or false and `[channelname]` with the desired data channel: `p.Chaos.VD.SetCVDDataChannelEnabled [newstate] [channelname]` For example: ![Legacy Record To File](https://dev.epicgames.com/community/api/documentation/image/949645b0-043d-4887-99bd-3504f084d049)
3. Press **Enter** to execute the command.

### Enable Multiple Data Channels

To enable or disable multiple channels by listing them, separated by commas. The following example enables the **PostIntegrate** and **Scene Queries** channels:

`p.Chaos.VD.SetCVDDataChannelEnabled true SceneQueries,PostIntegrate`

![Legacy Multiple Channels](https://dev.epicgames.com/community/api/documentation/image/87ba0151-f50c-4c17-a17e-bb168c44a1df)

### Enable Predefined Data Channels

To launch a game client or server with a predefined set of enabled channels, add the following command line argument:

`CVDDataChannelsOverride=[ChannelName1,ChannelName2]`

The following example enables the Integrate and Scene Queries channels:

`CVDDataChannelsOverride=SceneQueries,PostIntegrate`

### Start a Recording Using the Command Line

1. To start a recording, open the command line in the target application. If you’re running a packaged build, you can press **Backtick** (`).
2. Type the following command and press **Enter** to execute it: `p.Chaos.StartVDRecording` ![Start Recording (Console)](https://dev.epicgames.com/community/api/documentation/image/20efb315-46b5-49c3-873c-f492541a17ac) ![Start Recording (Legacy)](https://dev.epicgames.com/community/api/documentation/image/31fbb471-fcf9-4ffb-a2eb-0da0ba36bce3) When the recording begins, the string Chaos Visual Debugger recording in progress… displays on screen. ![Recording In Progress String](https://dev.epicgames.com/community/api/documentation/image/f6b46843-d1ad-40f8-aecc-d065de2dc635)
3. To stop a recording, open the command line, type the following command, and press Enter to execute it. `p.Chaos.StopVDRecording` ![Stop Recording (Console)](https://dev.epicgames.com/community/api/documentation/image/44bed7d0-7887-45b2-8ad8-1604d3459b72)

## Next Up

In the next tutorial, you’ll learn how to locate your `.utrace` files and play back your recordings.

- [Related Document](en-us/unreal-engine/live-debugging-with-chaos-visual-debugger.md)

- [Related Document](en-us/unreal-engine/playback-in-chaos-visual-debugger.md)
