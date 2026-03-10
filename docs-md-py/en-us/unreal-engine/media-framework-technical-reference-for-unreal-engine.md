# Media Framework Technical Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/media-framework-technical-reference-for-unreal-engine

> Application Version: 5.7

This page outlines the currently supported file extensions, URLs, and capture devices, as well as pointing out some troubleshooting tips on how to enable Media Framework with different platforms.
There are some known platform-specific issues and limitations which we are currently investigating and trying to resolve, each of which has been identified in the Troubleshooting and Known Issues sections.

## Supported Files, URLs and Capture Devices

The table below indicates the supported file extensions based on each media player platform.

Click the [link here](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/26794c66-2da5-4afa-9716-201fc3ae425a/supportedextentions.xlsx) to download a `.xlsx` version of the supported files and URLs spreadsheets.

![Supported file extensions based on each media player platform](https://dev.epicgames.com/community/api/documentation/image/482c9de9-84e2-47a6-94b4-02ca3c0cdfd3)

The table below shows the supported URLs based on media player platform.

![Supported URLs based on media player platform](https://dev.epicgames.com/community/api/documentation/image/a6a2950a-ecd3-4770-b9e2-88d735eac906)

The list of supported file formats above is ongoing, and support for additional file extensions will come online in future engine updates. These have been updated for the **Electra Media Player**.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For the best compatibility and performance, it is recommended to use <strong>H.264</strong> encoded <strong>MP4 (.mp4)</strong> container files.",
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

### Capture Devices

Media Framework supports audio/video capture hardware on Windows (WmfMedia) and Android (AndroidCamera). Consoles are not yet supported.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Please see the <a data-document-id=\"3233306\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/playing-live-video-captures-in-unreal-engine\">Playing Live Video Captures</a> page for an example guide on working with capture devices.",
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

## WMF Media Configuration

The following sections describe the configuration options that you can set for the WMF Media Plugin in your Project Settings.

### Custom Codecs

Windows Media Foundation (WMF) handles standard audio/video playback and recording on the Windows Platform; however, WMF is also extensible.
By default, WMF supports a number of different formats, encoding, and file containers, but it can also be extended with the use of optional codec packs that can be downloaded and installed from the Internet.
What this means, however, is that certain users may not have a particular codec needed to decode and playback a media file.

In the past, Unreal Engine only supported default codecs that were supplied with WMF to ensure that everyone could handle and process media the same way.
There may be times when you want to use a different method of encoding your media or your own proprietary media encoder that you want to ship your game with (for example, you ship your game with an installer that provides the needed encoder).

You can now enable and allow non-standard codecs for **WMF Media** from the **Plugins** section of **Project Settings**.

![Project Settings - WMF Media Plugin](https://dev.epicgames.com/community/api/documentation/image/f92021de-e1e1-4dc0-8435-7432ffa502f9)

_Click image for full size._

By default, the player plugin attempts to detect audio and video codecs that are not supported by the operating system (OS), requiring the user to install additional codec packs.
If the player plugin detects an unsupported format when accessing the media, a warning message is provided in the **Output Log**.

Additionally, you can see media asset information inside a **Media Player** asset in the **Info** panel.

When enabling **Allow non-supported codecs**, the Plugin player will skip the check and allow the usage of non-standard codecs.

### Playback Optimization

The WMF Media Plugin offers some options that you can use to customize the way it decodes and plays back your media. If the Plugin doesn't play your media with the responsiveness, smoothness, or performance that you need, you can try enabling these options.

![Playback optimization settings](https://dev.epicgames.com/community/api/documentation/image/8a521cba-1935-4924-90b9-0d328176da3a)

_Click image for full size._

| Setting | Description |
| --- | --- |
| **Low Latency** | This setting minimizes delays, or latency, in media playback. If your video playback tends to lag, this setting may help you achieve a faster response from the WMF Media Plugin. However, enabling this setting may adversely affect the quality of the video and/or audio. Only works on Windows 8 or later. |
| **Hardware Accelerated Video Decoding (Experimental)** | Uses the GPU instead of the CPU to decode video streams. If your CPU is a bottleneck on your video performance, this setting may improve the smoothness of your video playback. It may also enable you to use more media at the same time, with larger resolutions. Only works on Windows platforms, rendering with DirectX 11. |

## HAP Codec Playback Support

HAP Codec Playback allows you to produce high quality media with low CPU/GPU processing requirements.

In UE5, you can play **1x 4K 60 FPS** movie or **2x 4K 30 FPS** movie, which can be stretched to **2x 4K 60 FPS** movies.

| Specification | Supported Setting |
| --- | --- |
| **Format** | HAP, HAP Alpha, HAP Q, HAP Q Alpha |
| **Frame Rates** | 10, 15, 23.976, 24, 25, 29.97, 30, 50, 59.94, 60 |
| **Resolutions** | Up to 4K 3840x2160 |
| **Bit Depth** | 8bit (4:4:4:) |
| **Pixel Aspect Ratio** | Aspect Ratio Independent |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "As of 4.23, HAP playback does not support embedded audio or timecodes.",
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

### Benchmarking Test Case

Below is the benchmark test case the UE5 team used to determine these settings. You can use this test case as a comparison for your own project.

The current benchmarking process is meant to give a rough idea of system performance. We tested playback of the same movie file in 3 different softwares: Unreal Engine, Ventuz, and VLC.
For each test, we monitored and logged CPU, GPU, and Disk usage with Windows Task Manager.

The movie file was an **11 second 4K 60 FPS movie** from an 8K 60 FPS source that we recompressed in 4K, 8K, and 16K using HAP. We discovered issues with WMF that cause anything above **4K 60 FPS** to fail on all three softwares.
We also found that using two SSDs is significantly faster than using one SSD.

Here are some additional notes:

- We were unable to properly assess disk usage for Unreal and Ventuz applications.
- Note that a 60 FPS video clip is the equivalent of two 30 FPS video clips to decode.
- At this point, this is not a PRO Video Playback solution so there is no guarantee on synchronous playback in between files or machines.

#### Test System Description

- Xeon 3.39 Ghz
- 96 GB
- Samsung MZVKW512HMJP-000L7 (C:)
- ATA Samsung SSD 860 SCSI Disk (D:)

## Troubleshooting

Most player Plugins have had extensive logging added, and will provide detailed logging of potential problems.

To enable logging, add the following to your project's **Engine.ini** file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[Core.Log]\n\tLogMedia=VeryVerbose\n\tLogMediaAssets=VeryVerbose\n\tLogAndroidMedia=VeryVerbose\n\tLogAvfMedia=VeryVerbose\n\tLogMfMedia=VeryVerbose\n\tLogPS4Media=VeryVerbose\n\tLogWmfMedia=VeryVerbose",
  "lines_of_code": 8,
  "id": 161307,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjEzMDcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNzo0MiswMDowMCJ9--28bc6c9a91ce815063ba535ca76f966d36435b0afd2b5a489884fa7249401d55",
  "settings": {
    "is_hidden": false
  }
}
```

If a media source fails to open or play, check the **Output Log** for additional details.

You can also check information about a Media Source inside the Media Player asset and **Info** tab.

![Info Window](https://dev.epicgames.com/community/api/documentation/image/692ed9e8-7310-459a-bfd1-12821d358aea)

This will show what options are available for the media source, as well as the different Audio and Video streams and information about each stream.

### Windows

The Windows Media Foundation (WMF) player Plugin WmfMedia has a number of limitations for MP4 containers.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "See Microsoft's <a href=\"https://msdn.microsoft.com/en-us/library/windows/desktop/dd757766%28v=vs.85%29.aspx\">MPEG-4 File Source</a> page for more information.",
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

## Known Issues and Limitations

**Media Framework** is still in development, and there are some known issues and limitations, as outlined below:

- **Android** Audio currently plays via the OS and cannot be piped through UE5's Sound System.
- **Editor** The Playlist UI inside the Media Player always has a playlist created internally. Playlists can be saved from the Media Player; however, there is no way currently to edit the playlist in the Media Player. Workaround: Save a Playlist from the Media Player then open and edit the Media Playlist asset.
- **Sequencer** Media Playback will not render out properly when recording cinematics from Sequencer. We have this scheduled to release in the near future as we know this is important. The ImgMedia Plugin will be synced with Sequencer.
- **Windows** QuickTime movie (.mov) support on Windows 7 and later is currently unreliable. Workaround: This format is currently not recommended for use.
- **Linux** Currently, the WebM Media Player is the only available media player on Linux.
