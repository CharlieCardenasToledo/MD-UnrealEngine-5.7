# Taking Screenshots

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/taking-screenshots-in-unreal-engine

> Application Version: 5.7

Unreal Engine 5 (UE5) offers a multitude of different ways of taking in-game screenshots of your project.
This document describes which tools are available for taking screenshots in UE5 and how you can use them.

## Default Save Location

By default any screenshots will be saved to the following location in your project folder.

**Saved\Screenshots\Windows**

When you do take a screenshot, the following message will be displayed in the lower right-hand corner of the screen.

![Showing the save location of your high resolution screenshot](https://dev.epicgames.com/community/api/documentation/image/860d6a7c-279f-43b0-88b1-28cc183b75f3)

Clicking on the message will display the folder containing your screenshots.

## Standard Screenshot

The standard screenshot feature is available via the console command **Shot** (default key binding is **F9**).
It can generate screenshots at the size of the screen resolution (or window resolution if the game is running in windowed mode).

## High Resolution Screenshot

The high resolution screenshot console command is a great cross-platform tool for taking very high resolution screenshots.
It is capable of generating screenshots of any size that are based off of the screen resolution (or window resolution if the game is running in window mode).
The high resolution screenshot console command does this by rendering the game frame multiple times, one tile at a time at full resolution, and concatenating all tiles into a single image file.

The default behavior is to take a screenshot with a resolution 4 times greater than the game resolution and create an image file in the Screenshot folder.

When running the game through the editor (PIE) or as standalone, open the command console by hitting **~** (*tilde*) and type:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "HighResShot",
  "lines_of_code": 1,
  "id": 75160,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3NTE2MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjM3OjUyKzAwOjAwIn0=--824943c12d0f92e20d1237bb024d62bd85c3283e42dcdaabe8f05150904d0206",
  "settings": {
    "is_hidden": false
  }
}
```

### Parameters

The HighResShot console command takes a number of optional parameters that can control how the screenshot is taken:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "HighResShot filename=PATH (XxY OR Multiplier) CaptureX CaptureY CaptureW CaptureH bMaskUsingCustomDepth bDumpBufferVisualizationTargets bCaptureHDR bDateTimeAsFilename",
  "lines_of_code": 1,
  "id": 75161,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3NTE2MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjM3OjUyKzAwOjAwIn0=--04edc580f8d4b3d02f082d4ac9906b64083de8beb71982161673174ab20fd0a6",
  "settings": {
    "is_hidden": false
  }
}
```

| Parameter | Description |
| --- | --- |
| XxY | Specifies the size of the image (width x height). |
| Multiplier | Multiplies the size of the screenshot by a value. |
| CaptureX CaptureY CaptureW CaptureH | Uses integers to define a region of the viewport to use for the screenshot. |
| bMaskUsingCustomDepth | Uses a boolean value (0 or 1) to toggle using the Custom Depth buffer as a mask for the capture. See [#customdepthmask) |
| bDumpBufferVisualizationTargets | Uses a boolean value (0 or 1) to toggle capturing each pass in the G Buffer as an image that gets exported. |
| bCaptureHDR | Uses a boolean value (0 or 1) to toggle the use of the .EXR file format to capture an HDR image. |
| bDateTimeAsFilename | Uses a boolean value (0 or 1) to toggle the use of a timestamp in the generated filename. |

Typing the following will take a screenshot that is twice as big as the screen resolution:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "HighResShot 2",
  "lines_of_code": 1,
  "id": 75162,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3NTE2MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjM3OjUyKzAwOjAwIn0=--f8d112100b36e87b73298d9f23c6764b3eaa6ca15f2ab7bbbe6213b967011aed",
  "settings": {
    "is_hidden": false
  }
}
```

Similarly, the command below will take a screenshot at 3840 wide by 2160 high:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "HighResShot 3840x2160",
  "lines_of_code": 1,
  "id": 75163,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3NTE2MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjM3OjUyKzAwOjAwIn0=--65cdefb4d58193b069ee8d872de0cf2a63ff754056c9b9f19b70357c5e85cded",
  "settings": {
    "is_hidden": false
  }
}
```

## High Resolution Screenshot Tool

![The High Resolution Screenshot Tool](https://dev.epicgames.com/community/api/documentation/image/09e09110-2740-4fcc-89f3-53a8fc141d7b)

With the High Resolution Screenshot Tool (HRSST) you can specify a specific region of your viewport to use when you take a screenshot. You can also adjust the size of the screenshot and output the results of the GBuffer.

### Accessing the High Resolution Screenshot Tool

You can access the HRSST by first clicking on the **Viewport Options** and then selecting the **High Resolution Screenshot** option.

![Opening the High Resolution Screenshot Tool](https://dev.epicgames.com/community/api/documentation/image/28c20439-3fab-4c57-93c6-29f743d478a5)

Once you have selected the **High Resolution Screenshot**, the HRSST will be displayed on screen.

![Numbered explanation of the HRSST window](https://dev.epicgames.com/community/api/documentation/image/144376a2-dfa2-49ed-b229-809d4b697484)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can move the HRSST anywhere inside of UE5. However, be aware of its position as sometime the HRSST can become hidden by other floating windows like the <strong>Content Browser</strong>.",
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

| Number | Description |
| --- | --- |
| 1 | A multiplier that sets the size of the screenshot. |
| 2 | Includes the Date and Timestamp in the image name. |
| 3 | Tells the tool to include each pass in the GBuffer as an image that gets exported. |
| 4 | Writes all exported images into .EXR format and enables full 16 bit color depth (HDR) export of all of available intermediate rendering stages. |
| 5 | Forces full 128bpp rendering. |
| 6 | Captures certain objects in the scene. See [Custom Depth Mask](https://dev.epicgames.com/documentation/en-us/unreal-engine/taking-screenshots-in-unreal-engine) |
| 7 | Specifies a region within the viewport that you wish to capture. You define a region by first clicking on the tool and selecting a region to capture. Do this by holding down the **Left Mouse Button** and dragging in the Editor viewport. |
| 8 | Clears any previous capture regions that you might have created. This button will only be visible when you have a region selected. |
| 9 | Expands the capture region to the entire editor window. This button will only be visible when you have a region selected. |
| 10 | Click this to take the screenshot. |

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Due to the high system requirements of a high resolution screenshot, very large multipliers might cause the graphics driver to become unresponsive and possibly crash. In these circumstances, please try using a lower number.",
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

### Using the High Resolution Screenshot Tool

To take a high resoloution screenshot:

1. Enable the HRSST. To do this, click on the **Viewport Options**, then select the **High Resolution Screenshot** option. [Video: 1_sb17w0u7](https://dev.epicgames.com/community/api/cms/videos/1_sb17w0u7/embed.html)
2. Once the tool has been enabled, press the **Specify Region** button to select a region of the editor viewport that you want to capture. [Video: 1_phe8xef7](https://dev.epicgames.com/community/api/cms/videos/1_phe8xef7/embed.html)
3. Adjust the **Screenshot Size Multiplier** to set the final size of the image file, then press the Camera icon to take the screenshot. Screenshots will be saved to **Saved\Screenshots\Windows** folder. [Video: 1_gwf6airo](https://dev.epicgames.com/community/api/cms/videos/1_gwf6airo/embed.html)

### Buffer Visualizations

The HRSST can render each of the following buffers in the G-Buffer:

- **BaseColor**
- **LightingModel**
- **Metallic**
- **Opacity**
- **PostTonerMapHDRColor**
- **PreTonerMapHDRColor**
- **Roughness**
- **SceneColor**
- **SceneDepth**
- **SceneDepthWorldUnits**
- **SeparateTranslucencyA**
- **SeparateTranslucencyRGB**
- **Specular**
- **SubsurfaceColor**
- **WorldNormal**

To enable the HRSST to export out the G-Buffer as images, first enable **Include Buffer Visualization Targets**, then press the capture button. The capture folder will now contain a screenshot for each of the G-Buffers listed above.

### OpenEXR Image Support

The HRSST supports exporting images in the OpenEXR image format.
This enables full 16 bit color depth (HDR) export of all available intermediate rendering stages.
After you click the capture button, the HRSST writes out the following buffers to the OpenEXR image format.

- **BaseColor**
- **LightingModel**
- **Metallic**
- **Opacity**
- **PostTonerMapHDRColor**
- **PreTonerMapHDRColor**
- **Roughness**
- **SceneColor**
- **SceneDepth**
- **SceneDepthWorldUnits**
- **SeparateTranslucencyA**
- **SeparateTranslucencyRGB**
- **Specular**
- **SubsurfaceColor**
- **WorldNormal**

To use OpenEXR image support, enable **Write HDR format visualization targets**, then press the capture button. The capture folder will now contain a screenshot for each of the G-Buffers listed above.

[Video: 1_6gym3bu7](https://dev.epicgames.com/community/api/cms/videos/1_6gym3bu7/embed.html)

### Custom Depth Mask

During the course of development, you might need the ability to capture certain objects in the game world for promotional material.
However, having to manually cut out objects from the background can be both time consuming and frustrating.
To help speed this process up the HRSST has an option called **Use custom depth as mask**, which can separate objects in the world from one another.
Setting up and using this part of the tool is done by following these steps:

1. Select the objects that you want to capture. Then, in the **Details** panel, enable the **Render CustomDepth Pass** option. [Video: 1_wctyxpis](https://dev.epicgames.com/community/api/cms/videos/1_wctyxpis/embed.html)
2. Open the HRSST and select the region you want to capture. Make sure that the region you are trying to capture includes the meshes that have **Render CustomDepth Pass** enabled.
3. Enable the **Use custom depth as mask** option.
4. Take the screenshot by pressing the capture button.
5. View the screenshot by clicking on message that is displayed in the lower right hand corner of the screen. [Video: 1_5qs900a7](https://dev.epicgames.com/community/api/cms/videos/1_5qs900a7/embed.html)
