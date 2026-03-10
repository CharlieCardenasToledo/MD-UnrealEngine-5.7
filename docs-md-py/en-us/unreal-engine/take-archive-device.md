# Take Archive Device

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/take-archive-device

> Application Version: 5.7

The **Take Archive** device enables the ingest of arbitrary video, audio, depth, and calibration data identified using a take metadata file (`.cptake`). It can be used if you would like more control over how the data is represented or the contents of the take are not compatible with the other **Capture Manager** devices. This device is backwards compatible with takes created for use with Capture Manager and **MetaHuman Animator** in **Unreal Engine** 5.5 and earlier.

![Device Manager Take Archive Ingest](https://dev.epicgames.com/community/api/documentation/image/abea22e4-241f-45b8-9382-b698ad1f1c4a)

- **Display Name**: The name of the device as it will appear in the **Devices** list.
- **Take Directory**: the path to the root folder containing the `.cptake` metadata file. This folder can contain subfolders.

A visual example of the content expected to be found by the **Take Archive** device in the **Take Directory** is shown below:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "console_output",
  "title": "",
  "code_preview": "+-- take_1\n|   +-- top.mov\n|   |-- bot.mov\n|   \\-- metadata.cptake\n|\n|-- metadata.cptake\n\\-- take_2.mov",
  "lines_of_code": 7,
  "id": 48092,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0ODA5MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI1OjM0KzAwOjAwIn0=--22bcaa631b2689f508ef0c41811de6c12659ced4bf9acd6d9a07066a1c15efee",
  "settings": {
    "is_hidden": false
  }
}
```

## Take Metadata Files (.cptake)

Take metadata files (`.cptake`) are created by the user to describe the contents of a take. They allow Capture Manager to work with data that does not meet the expectations of the other devices or if you would like more control.

The information in a take metadata file is encoded using the JSON format, and adheres to a schema which can be found in `\Engine\Plugins\VirtualProduction\CaptureManager\CaptureManagerCore\Content\TakeMetadata\Schema`. Based on the schema, each take must have a `UniqueId` (specified as a GUID), `TakeNumber`, `Slate`, and `Device`section. Each take may optionally have an array of `Video`, `Depth`, `Audio`, or `Calibration` media content.

Below is a minimal example `.cptake` file for a mono video take:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "console_output",
  "title": "",
  "code_preview": "{\n  &quot;Version&quot;: {\n    &quot;Major&quot;: 4,\n    &quot;Minor&quot;: 2\n  },\n  &quot;UniqueId&quot;: &quot;2b42db4d-11e5-49ab-8a4d-a78212345597&quot;,\n  &quot;TakeNumber&quot;: 1,\n  &quot;Slate&quot;: &quot;MySlateName&quot;,\n  &quot;Device&quot;: {\n    &quot;Name&quot;: &quot;MyDeviceName&quot;,\n",
  "lines_of_code": 21,
  "id": 48093,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0ODA5MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI1OjM0KzAwOjAwIn0=--143f7fc9b4382ce9ea5fb63e07cf83bf3931a574edaf46ec9fbc5cbb153fb03d",
  "settings": {
    "is_hidden": false
  }
}
```

### Supported Device types

The supported device types compatible with MetaHuman Animator are:

- StereoHMC
- iPhone

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If converting a <b>Live Link Face</b> take into the <code class=\"inline-code\">.cptake</code> format, set the <code class=\"inline-code\">Model </code>to the numerical component of the <code class=\"inline-code\">deviceModel</code>found in the original <code class=\"inline-code\">take.json</code> file. For example, if the <code class=\"inline-code\">deviceModel</code>in the <code class=\"inline-code\">take.json</code> file is <code class=\"inline-code\">iPhone14</code>,<code class=\"inline-code\">3</code>, set <code class=\"inline-code\">Model</code>in the new <code class=\"inline-code\">.cptake</code> metadata file to <code class=\"inline-code\">14</code>,<code class=\"inline-code\">3</code>.",
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

### Supported Formats

The supported `Format` values for a `Video` section are:

- mov
- mp4
- png
- jpg
- jpeg

The supported `Format` values for a `Depth` section are:

- mha\_depth
- exr

The supported `Format` values for an `Audio` section are:

- wav
- mov
- mp4

The supported `Format` values for a `Calibration` section are:

- opencv
- mhaical
