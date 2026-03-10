# Recording a Live Session

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger

> Application Version: 5.7

In this tutorial, you’ll learn how to record and play back an application in real time using **[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**). Unlike [recording to file](https://dev.epicgames.com/documentation/en-us/unreal-engine/recording-to-file), recording a live session can be done **locally** (on your machine) or **remotely** (over a network). This is useful for live debugging on the fly but also saves the recording as a `.utrace` file for you to review and share later on.

![Recording a Live Session](https://dev.epicgames.com/community/api/documentation/image/ae8844cb-a23d-480c-9cb5-8d6933123a5e)

## Record Live Sessions

In this section you’ll learn how to record a PIE session using the Local Editor target preset, and the process to record all other target types.

### Local Editor

To record and play back a live PIE session on a local or a remote machine, follow these steps:

1. In CVD, toggle the data channels you want to record. ![Toggle Data Channels](https://dev.epicgames.com/community/api/documentation/image/d7f37ce6-fe06-4924-aacb-574b3b8917ac)
2. In Unreal Editor, click the **Play** button in the main toolbar to begin a PIE session. You can start the PIE session before or after beginning a recording in CVD ![Play Button](https://dev.epicgames.com/community/api/documentation/image/47e06c72-8aec-4e57-891b-46dc007a8d12)
3. Since the Local Editor target is already selected by default, you can begin the recording by clicking **Record Live Session**. While recording, this button turns into a red recording icon. ![Record Live Session](https://dev.epicgames.com/community/api/documentation/image/0ea42f7e-95d0-41ab-a5d6-5c08bc12020c)
4. To stop recording, highlight the recording icon and click the red square icon. This process outputs a single `.utrace` file. ![Stop Recording](https://dev.epicgames.com/community/api/documentation/image/d48c70cd-0587-4d4c-9a8d-3c47edbeab78) [Video: V_RcyXCr](https://dev.epicgames.com/community/api/cms/videos/V_RcyXCr/embed.html)

### All Other Targets

To record and playback a game client, server, or packaged build on a local or remote machine, follow these steps:

1. Verify that your target application or applications are running.
2. Toggle the data channels you want to record. ![Toggle Data Channels](https://dev.epicgames.com/community/api/documentation/image/6c39ebe0-b317-4bdd-9cb3-3acdcbf4fd58)
3. To select a target to record, in CVD’s main toolbar, click the **Session Target** dropdown menu and choose your target. ![Session Target](https://dev.epicgames.com/community/api/documentation/image/38cc5554-1c75-47a9-b590-6a2960e1edcb)
4. To begin a recording, in CVD’s main toolbar, click **Record Live Session**. While recording, this button turns into a red recording icon. ![Record Live Session](https://dev.epicgames.com/community/api/documentation/image/f0edea29-2309-44de-8563-feddcd89175d)
5. To stop recording, highlight the recording icon and click the red square icon. This process outputs one or more `.utrace` files. ![Stop Recording](https://dev.epicgames.com/community/api/documentation/image/96245b53-8d1a-4d82-9bba-627ab9f65758)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The game client and CVD compete for GPU resources. If the playback in CVD is struggling, you can limit the game client’s framerate or reduce the graphics quality.",
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

## (Legacy) Record a Live Session with the Command Line Interface

We recommend using CVD’s UI to start and end recordings, however, you can use the command line to record PIE sessions, game clients and servers, and packaged builds. The session can be local (on the same workstation or even in the same PIE instance) or over the network.

### Enable a Data Channel

1. To modify data channels, open the command line in the target application. In a packaged build, press **Backtick** (`).
2. Enter the following console command, making sure to replace `[newstate]` with true or false and `[channelname]` with the desired data channel: `p.Chaos.VD.SetCVDDataChannelEnabled [newstate] [channelname]` For example: ![Recording Live (Console)](https://dev.epicgames.com/community/api/documentation/image/d3dd8bf8-4769-4ae8-acc8-7a521da337fc)
3. Press **Enter** to execute the command.

### Enable Multiple Data Channels

You can enable or disable multiple channels by listing them, separated by commas. The following example enables the **PostIntegrate** and **Scene Queries** channels:

`p.Chaos.VD.SetCVDDataChannelEnabled true SceneQueries,PostIntegrate`

![Recording Live Multiple Channels (Console)](https://dev.epicgames.com/community/api/documentation/image/ca30d14b-75c4-4112-aa9f-1765412a5e64)

### Enable Predefined Data Channels

If you want to launch a game client or server with a predefined set of enabled channels, add the following command line argument:

`CVDDataChannelsOverride=[ChannelName1,ChannelName2]`

The following example enables the Integrate and Scene Queries channels:

`CVDDataChannelsOverride=SceneQueries,PostIntegrate`

### Start a Recording Using the Command Line

1. To start a recording, open the command line.
2. If you are working on a local machine, type the following command and press **Enter** to execute it: `p.Chaos.StartVDRecording Server` ![Start Recording Server (Console)](https://dev.epicgames.com/community/api/documentation/image/b5c6027a-54dd-4282-8999-ad07469861cc) If you are working on a remote machine, type the following command and press **Enter** to execute it: `p.Chaos.StartVDRecording Server [YOURWORKSTATIONIP]`
3. In CVD’s main toolbar, click **Connect To Session**. In the **Live Session Browser**, next to **Selected Live Session**, select the available live session running on the local trace store.
4. (Optional) If you’re connecting to multiple targets, from the **Connection Mode** dropdown menu, select **Multi Source**. ![Multi Source Connection Mode](https://dev.epicgames.com/community/api/documentation/image/fc5ebfbc-59f0-4621-a850-b48061297719)
5. Click **Connect to Session** (in the **Live Session Browser** dialog). When the recording begins, the string **Chaos Visual Debugger recording in progress…** displays on screen. ![Recording String](https://dev.epicgames.com/community/api/documentation/image/97f55263-0aac-49c6-8130-a95cb7e9b689)
6. To stop a recording, open the command line. If you’re working on a local machine, type the following command and press **Enter**: `p.Chaos.StopVDRecording Server` ![Stop Recording Server (Console)](https://dev.epicgames.com/community/api/documentation/image/8c6a9ebb-0b1a-4be7-9eaa-86d6699c825b) If you’re working on a remote machine, type: `p.Chaos.StopVDRecording Server [YOURWORKSTATIONIP]`

## Next Up

In the next tutorial, you’ll learn how to locate your `.utrace` files and play back your recordings.

- [Related Document](en-us/unreal-engine/playback-in-chaos-visual-debugger.md)
