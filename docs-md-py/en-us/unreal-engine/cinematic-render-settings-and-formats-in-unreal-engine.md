# Render Settings and Formats

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-render-settings-and-formats-in-unreal-engine

> Application Version: 5.7

The Render Settings in Movie Render Queue are used to customize how your sequences are rendered. These include additional rendering processes such as anti-aliasing, custom console commands, output format, rendering mode, and more.

This guide covers the settings interface, the list of settings that can be added, and the ability to save your settings as presets.

#### Prerequisites

- You have completed the prerequisite steps from the **[Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine)** section of the Movie Render Pipeline page.

## Opening Render Settings

You can open the Render Settings window by clicking the **Settings** entry for your job.

![render settings window](https://dev.epicgames.com/community/api/documentation/image/a16e57de-dfdd-4b3e-8065-c7dc9de790b1)

## Interface Overview

There are three main areas of the Render Settings window:

![render settings interface](https://dev.epicgames.com/community/api/documentation/image/890bc8ca-55a4-4d8a-be30-7c03e28cc7d6)

1. **Toolbar**: The toolbar contains a menu for adding additional settings and loading or saving the current setting list to a preset.
2. **Settings List**: The Settings List shows the current settings to apply to the job, and includes toggles to enable or disable them. Each setting is categorized into either **Exports**, **Rendering**, or **Settings**.
3. **Settings Details**: Shows the properties for the selected setting from the **Settings List**.

## Settings List

Clicking the **+ Setting** button will reveal the list of different settings you can add to your job. They are categorized into three groups; **Settings**, **Exports**, and **Rendering**.

![render settings list](https://dev.epicgames.com/community/api/documentation/image/ccbdf2b0-40e6-4a88-a1e5-2efc9dab7018)

### Settings

The Settings category contains options for render quality options, console variables, and miscellaneous render options.

```json
{
  "type": "include",
  "excerpt_id": 1549,
  "excerpt_assignment_id": 1340,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Name",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">Output</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The Output setting controls your output file's directory, file name, frame rate, and output resolution. Your file name and directory path can be customized using <code>{token}</code> format strings. Output is a required setting and cannot be deleted from the settings window.",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">Anti-Aliasing</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Anti-aliasing controls the number of samples used to produce the final render. There are two types of sampling that produce the render: <strong>Spatial</strong> and <strong>Temporal</strong>.",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">Burn In</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Burn In enables adding custom watermarks to your render, which contain information about the render and shot. You can choose whether the Burn In is added to the final image, or is rendered to a separate layer.",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">Camera</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The Camera setting contains settings for the shutter timing and you can specify an overscan percentage to render extra pixels around the edges of your images.",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">Color Output</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The Color Output setting overrides Unreal's default color space settings with a custom <strong><a data-document-id=\"3233941\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine\">OpenColorIO (OCIO)</a></strong> configuration. You can also use it to disable the <strong>Tone Curve</strong> portion of post-processing even if not using an OCIO-based workflow.",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">Console Variables</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Console Variables enables console commands to be designated when the render begins. This is useful when trying to apply quality settings that are too computationally expensive for real-time preview in the Editor. The variables will be reverted upon the render completing.",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">Debug Options</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Debug Options contain options for debugging certain render behaviors. Typically you do not need to use these options unless you're troubleshooting issues within your renders.",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">Game Overrides</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Game Overrides change several common game-related settings, such as Game Mode and Cinematic Quality settings. This is useful if the game's normal mode displays UI elements or loading screens that you do not want to capture.",
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
              "content": "<a data-document-id=\"3940566\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine\">High Resolution</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The High Resolution settings enable the use of tiled renders to produce larger images without being constrained by maximum texture sizes or memory limits on GPUs.",
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
  "excerpt_hash_id": "q05",
  "settings": {
    "is_hidden": false
  }
}
```

Visit **[Image Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine)** for a more comprehensive look at these options.

- [Related Document](en-us/unreal-engine/cinematic-render-settings-and-formats-in-unreal-engine.md)

### Exports

The Exports category controls what image, audio, and video format you want to output your sequence to.

```json
{
  "type": "include",
  "excerpt_id": 1550,
  "excerpt_assignment_id": 1341,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Name",
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
              "content": "<a data-document-id=\"3940564\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-export-formats-in-unreal-engine\">Command Line Encoder</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The Command Line Encoder can be used to create your own output format from third party software, such as FFmpeg. This setting requires an encoder executable and settings to be enabled in your Project Settings.",
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
              "content": "<a data-document-id=\"3940564\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-export-formats-in-unreal-engine\">Final Cut Pro XML</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The Final Cut Pro XML format will output an XML file that can be read by Final Cut Pro and other video editing software that support this format. This is not supported in shipping builds.",
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
              "content": "<strong>.bmp Sequence [8bit]</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the movie as a sequence of .bmp images. Pixel values are clamped in the [0-1] range, meaning that no HDR values are preserved. This applies sRGB encoding curve.",
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
              "content": "<a data-document-id=\"3940564\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-export-formats-in-unreal-engine\">EXR Sequence</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the movie as a sequence of .exr images. HDR values are preserved but if the Tone Curve is enabled, linear values are scaled to approximately the [0-1] range with only the brightest highlights going above one. Disabling the Tone Curve writes linear values in the [0-100] range or more depending on the intensity of lights and other bright objects. No sRGB encoding curve is applied to .exr targets.",
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
              "content": "<strong>.jpg Sequence [8bit]</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the movie as a sequence of .jpg images. Applies sRGB encoding curve.",
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
              "content": "<strong>.png Sequence [8bit]</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the movie as a sequence of .png images. Applies sRGB encoding curve. Transparency is supported by enabling Enable Alpha Channel Support in Post Processing project setting.",
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
              "content": "<a data-document-id=\"3940564\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-export-formats-in-unreal-engine\">WAV Audio</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs a .wav audio file alongside any other output formats you have selected.",
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
              "content": "<a data-document-id=\"3940564\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-export-formats-in-unreal-engine\">Apple ProRes Video Codecs</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs a .mov file using Apple ProRes, which is Apple's high-quality, lossy video compression codec. This requires the Apple ProRes Media plugin to be enabled.",
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
              "content": "<a data-document-id=\"3940564\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-export-formats-in-unreal-engine\">Avid DNx Video Codecs</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs a movie file using Avid DNx, which is a high-definition lossy video codec. This requires the Avid DNxHR/DNxMXF Media plugin to be enabled.",
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
              "content": "<strong>Prestreaming Recorder</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The Prestreaming Recorder is used to create render caches for cinematics using <strong>Virtual Textures</strong> or <strong>Nanite</strong>.",
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
  "excerpt_hash_id": "RJ5",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "More than one export item can be specified for any given sequence. For example, you may choose to export your sequence as both a <strong>.jpg image sequence</strong> and <strong>.wav audio file</strong> to combine in your video editing software.",
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

Visit the **[Export Formats](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-export-formats-in-unreal-engine)** page for a more comprehensive look at these options.

- [Related Document](en-us/unreal-engine/cinematic-render-settings-and-formats-in-unreal-engine.md)

### Rendering

The Rendering category contains options for outputting different view-mode images and render passes.

| Name | Description |
| --- | --- |
| **Deferred Rendering** | Outputs the final image for the sequence, matching what you see in the viewport. |
| **Deferred Rendering (Detail Lighting)** | Outputs using a special shader variation which only displays lighting combined with normal maps. Can be useful to show off the geometry of a Level. |
| **Deferred Rendering (Lighting Only)** | Similar to Detail Lighting but without normal maps affecting the lighting. |
| **Path Tracer** | Displays path-tracing data as it is calculated for each frame. Not all rendering features are supported by the Path Tracer at this time. |
| **Deferred Rendering (Reflections Only)** | Outputs using a special shader variation which makes everything in the world reflective. |
| **Deferred Rendering (Unlit)** | Outputs using a special shader variation which displays only base color, with no lighting information. |
| **UI Renderer** | Includes any UMG widgets that have been added to the viewport in the output render. This is an experimental feature. |
| **Object Ids (Limited)** | The Object Ids render pass outputs an image where components in the scene are assigned an ID. IDs can be grouped individually, or based on other factors such as material, folder, or Actor name. This requires the Movie Render Queue Additional Passes plugin to be enabled. Object Ids are not supported in shipping builds. |

Visit the **[Render Passes](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-render-passes-in-unreal-engine)** Page for a more comprehensive look at these options.

- [Related Document](en-us/unreal-engine/cinematic-render-passes-in-unreal-engine.md)

## Presets

By default, render settings are temporarily set for your editor session and will be lost once the session is closed. You can save your settings as **Presets** to allow for project-wide sharing or for different settings to be used for different sequences.

There are two types of presets that can be saved and reused: **Master** and **Shot**.

### Master

Master presets are meant to be applied to the top-level job in order to propagate their settings to the camera cuts beneath them.

To save your current settings as a master config, click **Load/Save Preset** and select **Save As Preset**. You will then be prompted to save a **Movie Pipeline Master Config Asset**.

![save render job preset](https://dev.epicgames.com/community/api/documentation/image/97e74b97-43f5-44b0-922a-efdfa32922d1)

You can then apply this preset to a job in your queue by clicking the dropdown menu in the settings field and selecting the saved **Movie Pipeline Master Config Asset**.

![apply render job preset](https://dev.epicgames.com/community/api/documentation/image/132f51db-6e0b-4c81-b0c3-ec905a637440)

### Shot

Shot presets allow for overriding render settings per camera in your render. These may be useful if certain shots in your cinematic sequence require different settings from those that are being applied from the Master.

To save and use Shot presets, expand a job in your render queue to view its child cameras. Each camera has its own settings field that can be overwritten. Click one of the **Edit** fields to open the settings window for that camera.

![shot render settings](https://dev.epicgames.com/community/api/documentation/image/bf9977b8-ff65-4f78-8321-c2dab2c452e2)

You can add settings by clicking the **+ Setting** button and selecting a setting from the list.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You cannot add <strong>Export </strong>category settings or change the output directory for shot settings, as settings at this level cannot conflict with required settings from the Master.",
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

To save your current settings as a shot preset, click **Load/Save Preset** and select **Save As Preset**. You will then be prompted to save a **Movie Pipeline Shot Config Asset**.

![save render shot preset](https://dev.epicgames.com/community/api/documentation/image/378bcbcd-a85e-420a-9042-9d6e36286788)

Similar to applying a Master preset, you can apply this preset to a specific shot in your queue by clicking the dropdown menu in the settings field and selecting the saved **Movie Pipeline Shot Config Asset**.

![render config preset](https://dev.epicgames.com/community/api/documentation/image/5bc91a30-d1bf-4794-b19b-c44821444a1b)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Master and Shot Config Assets are different asset types and cannot be used interchangeably.",
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

### Editing Presets

When you have assigned a preset in the Settings column, it will change to match that preset's name. If you click a preset you will be taken to the configuration editor where you can edit the configuration. **These edits do not change the preset asset**, they are only modifying a temporary copy of that preset.

If you would like to modify the presets directly, you have two options:

- You can open the editor through the Movie Render Queue UI and choose **Save as Preset** and overwrite the preset that already exists.
- You can open and edit them directly by double-clicking them in the Content Browser. This will bring up an editor from which you can add settings, edit their values and save the changes using the asset's **Save** buttons.
