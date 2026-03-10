# Unreal Engine Editor Preferences

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-editor-preferences

> Application Version: 5.7

## General Settings

The settings in **Unreal Engine** are set in the [Editor Preferences](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-editor-preferences), accessed from the **Edit > Editor Preferences** window, and navigating to the **Plugins > Capture Manager** section.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "These settings are not available in UEFN.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24641195,
      "caption": "",
      "alt_text": "Editor Preferences Plugins Capture Settings",
      "image": {
        "id": 24641195,
        "file_name": "editor-preferences-plugins-capture-manager.png",
        "file_size": 518951,
        "content_type": "image/png",
        "created_at": "2025-05-27T22:32:33.486+00:00",
        "height": 1600,
        "width": 1593,
        "storage_key": "da696636-6ed6-416c-85f2-f42cb9dffb42",
        "context": "documentation"
      },
      "storage_key": "da696636-6ed6-416c-85f2-f42cb9dffb42",
      "context": "documentation",
      "width": 600,
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

- **Media Directory**: Location on the Unreal Engine client machine where raw media data (for example, images sequences, and audio files) will be stored.
- **Import Directory**: Location within the project where ingested assets will be created.
- **Auto Save Assets**: Whether assets should be saved automatically after creation.
- **Capture Data Asset Name**: Naming convention for the Capture Data asset created during ingest.
- **Launch Ingest Server on Live Link Hub Connection**: Launches the ingest server on detection of a connection to Live Link Hub.
- **Video / Audio / Calibration Asset Name**: Naming convention for the Video, Audio, and Calibration assets created during ingest.

Naming tokens can be used to automatically populate parts of the **Media Directory**, **Import Directory**, and **Capture Data** and **Video / Audio / Calibration** asset names.
