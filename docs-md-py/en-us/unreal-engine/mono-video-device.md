# Mono Video Device

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mono-video-device

> Application Version: 5.7

The **Mono Video** device enables the ingest of individual video files as mono takes. If the video contains an audio track it will also be extracted during ingest.

![Capture Manager Device Details](https://dev.epicgames.com/community/api/documentation/image/61ca965e-501c-4439-856e-5d3c73de3d6c)

- **Display Name**: The name of the device as it will appear in the **Devices** list.
- **Take Directory**: The path to the root folder containing video files. This folder can contain subfolders.
- **Video Discovery Expression**: [Tokens](https://dev.epicgames.com/documentation/en-us/unreal-engine/mono-video-device#discovery-expression-tokens) that can be extracted from the folder and file name to identify the take.

A visual example of the content expected to be found by the **Mono Video** device in the **Take Directory** is shown below:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "console_output",
  "title": "",
  "code_preview": "+-- takes\n|   +-- take_1.mov\n|   \\-- take_2.mov\n|\n\\-- take_3.mov",
  "lines_of_code": 5,
  "id": 47840,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0Nzg0MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI1OjMzKzAwOjAwIn0=--54d4270d6148acec076401918da13c20867a981f5c38758ac3d46e00adc827e3",
  "settings": {
    "is_hidden": false
  }
}
```

## Discovery Expression Tokens

The **Video Discovery Expression** is used to define the naming convention for video files in your takes. The available tokens are:

| `<Slate>` | The slate name. |
| --- | --- |
| **`<Name>`** | The identifier for the camera. |
| **`<Take>`** | The take number. |
| **`<Any>`** | Any valid string. |
| `<Auto>` | Used without any other tokens to automatically identify takes based on the directory structure. |

Tokens can be separated using the following delimiters: `_-.\`

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When not using the <code class=\"inline-code\">&lt;Auto&gt;</code> token, both <code class=\"inline-code\">&lt;Slate&gt;</code> and <code class=\"inline-code\">&lt;Name&gt;</code> must be present.",
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

| **Slate** | `MySlate_MyName_SomeString` |
| --- | --- |
| **Name** | `video` (the default value) |
| **Take** | `1` (the default value) |

However, if the Video Discovery Expression is set to `<Slate>_<Name>_<Any>-<Take>` the following tokens will be extracted instead:

| **Slate** | `MySlate` |
| --- | --- |
| **Name** | `MyName` |
| **Take** | `5` |
| **Any** | `SomeString` |

In both cases, the extension `.mov` is ignored.
