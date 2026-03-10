# Stereo Video Device

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/stereo-video-device

> Application Version: 5.7

The **Stereo Video** device enables the ingest of pairs of videos as stereo takes. An audio file (`.wav`) may also be provided alongside the video.

![Device Details Stereo](https://dev.epicgames.com/community/api/documentation/image/ce6dd3b6-75d8-4c51-8d37-a3e4c3261ce8)

- **Display Name**: The name of the device as it will appear in the **Devices** list.
- **Take Directory**: The path to the root folder containing pairs of video files. This folder can contain subfolders.
- **Video Discovery Expression**: [Tokens](https://dev.epicgames.com/documentation/en-us/unreal-engine/stereo-video-device?application_version=5.6#discovery-expression-tokens) that can be extracted from the folder and file name of the video to identify the take.
- **Audio Discovery Expression**: [Tokens](https://dev.epicgames.com/documentation/en-us/unreal-engine/stereo-video-device?application_version=5.6#discovery-expression-tokens) that can be extracted from the folder and file name of the audio file to identify the take.

A visual example of the content expected to be found by the Stereo Video device in the **Take Directory** is shown below:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "console_output",
  "title": "",
  "code_preview": "+-- take_1\n|   +-- top.mov\n|   \\-- bot.mov\n|\n+-- take_2\n|   +-- audio.wav\n|   |-- top.mov\n|   \\-- bot.mov\n|\n+-- take_3\n",
  "lines_of_code": 24,
  "id": 137688,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzc2ODgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNTozNCswMDowMCJ9--1533d20384fedd41b772380652e71c8b4ec4b58f008707fbc4c2740b99f1a1ae",
  "settings": {
    "is_hidden": false
  }
}
```

## Discovery Expression Tokens

The **Video Discovery Expression** and **Audio Discovery Expression** are used to define the naming convention for video and audio files in your takes. The available tokens are:

| `<Slate>` | The slate name. |
| --- | --- |
| `<Name>` | The identifier for the camera in the stereo pair. |
| `<Take>` | The take number. |
| `<Any>` | Any valid string. |
| `<Auto>` | Used without any other tokens to automatically identify takes based on the directory structure. |

Tokens can be separated using the following delimiters: `_-.\`

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When not using the <code class=\"inline-code\">&lt;Auto&gt;</code> token, both <code class=\"inline-code\">&lt;Slate&gt;</code> and <code class=\"inline-code\">&lt;Name&gt;</code> must be present.",
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

For example, consider the following take: `MyTakeFolder/MySlate_MyName_SomeString-005.mov`. If the Video Discovery Expression is set to the default value of `<Auto>`, the following tokens will be identified:

| **Slate** | `MyTakeFolder` |
| --- | --- |
| Name | `MySlate_MyName_SomeString-005` |
| **Take** | `1`(the default value) |

However, if the Video Discovery Expression is set to `<Slate>_<Name>_<Any>-<Take>` the following tokens will be extracted instead:

| **Slate** | `MySlate` |
| --- | --- |
| **Name** | `MyName` |
| Take | `5` |
| **Any** | `SomeString` |

In both cases, the extension `.mov` is ignored.

The same applies for audio files, where any audio extension (such as `.wav`) is ignored.
