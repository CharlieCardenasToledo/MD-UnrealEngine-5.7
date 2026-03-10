# Slate Postbuffers

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-slate-postbuffers-in-unreal-engine

> Application Version: 5.7

[Video: V_TmACwT](https://dev.epicgames.com/community/api/cms/videos/V_TmACwT/embed.html)

**Slate postbuffers** sample the game scene for use in UI materials, similar to how SceneColor is used in postprocess materials. This makes it possible for you to create visual effects that apply to both your game world and your user interface. Slate postbuffers can also potentially apply a **Slate postprocess** class to handle a broad postprocess such as a blur effect.

Some example use cases for Slate postbuffers include the following:

- Blurring the scene behind a transparent popup message.
- A vignetting effect to show damage or darkness.
- A screen-wide blur that selectively obscures widgets as well as the game world.
- A distortion filter that looks similar to a worn VHS tape.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Each of the above examples is available in the <strong>UI_SlatePostBuffer</strong> level in the <a href=\"samples-and-tutorials/content-examples\">Content Examples</a> project.",
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

This page provides:

- An overview of the workflow for using Slate postbuffers.
- Technical information about how Slate postbuffers function and their limitations.
- Instructions for how to do the following: Enable Slate postbuffers. Configure your Slate postbuffers. Create a new Slate Post Processor class. Integrate a Slate postbuffer into a material and apply it to a UI element.

## Overview

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Slate postbuffers and postprocessor classes are global resources, so you should communicate with your entire team about how your project uses them.",
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

Unreal Engine supports up to 5 Slate postbuffers, which each sample the game scene for use in UI materials. You can set a Slate postprocessor class for each postbuffer to apply a broad postprocess to that buffer before you use it in a UI material. If there is no postprocessor, it will just sample a copy of the game scene.

![The Slate RHI Settings in Project Settings](https://dev.epicgames.com/community/api/documentation/image/11c4e28c-e003-4dd5-baaa-1fb40ab3bffe)

To populate a postbuffer, you must add a **Post Buffer Update** widget to your UI. The bounding box of the widget dictates the area of the buffer that will be filled in with post-processed pixels. The postbuffer also contains the likeness of  widgets positioned below the update widget in terms of Z-order. Parts of the buffer not covered by an update widget retain their contents from the previous frame, or stay black.

A UI material can sample a postbuffer using the **GetSlatePost** functions. For example, `GetSlatePost0` samples Slate Postbuffer 0, while `GetSlatePost4` samples Slate Postbuffer 4. UI materials can use Slate postbuffers similarly to how post-process materials sample a scene with SceneColor.

![Example of the GetSlatePost node in use](https://dev.epicgames.com/community/api/documentation/image/15da24ce-ce43-4cbc-981e-f1a5641bcaf1)

When you apply your UI material to a widget, it will use the widget to apply the material’s postprocess to the portion of the screen behind it. The following example uses inverted Y axis UV coordinates to flip the portion of the viewport within a square widget upside-down.

![Example of a picture-in-picture with inverted UV coordinates from the Content Samples project](https://dev.epicgames.com/community/api/documentation/image/faba4b8e-5782-4f0b-98d3-2bb83d170158)

As a more complex example, the following screenshot shows a widget distorting the screen to look like a worn VHS tape. The widget applying the VHS distortion material takes up the entire screen and is layered on top of other widgets within the UI. This makes it possible for UE to process the UI and game scene together, so you can control elements like the date and timecode with text widgets in the UMG Blueprint.

![Example of a Slate postbuffer creating a VHS blur](https://dev.epicgames.com/community/api/documentation/image/e330e559-c5d7-4630-b419-4ef6a7dd8fc4)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "By default, the GetPostBuffer nodes sample directly behind your UI widgets. To learn how to override them, see the section below on Tips for Using Postbuffers in UI Materials.",
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

## Enable Slate Postbuffers

To enable Slate postbuffers, add the following CVar to your project’s `*Engine.ini` file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "DefaultEngine.ini",
  "code_preview": "[ConsoleVariables]\n\tSlate.CopyBackbufferToSlatePostRenderTargets=1",
  "lines_of_code": 2,
  "id": 148916,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNDg5MTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNjo1MCswMDowMCJ9--709179943efdf363741f612bffd2de2d190e5cf48d28dd5b2f73286d7ca2c855",
  "settings": {
    "is_hidden": false
  }
}
```

Alternatively, you can use the following console command to enable this CVar:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "command_line",
  "title": "",
  "code_preview": "-dpcvars=Slate.CopyBackbufferToSlatePostRenderTargets=1",
  "lines_of_code": 1,
  "id": 148917,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNDg5MTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNjo1MCswMDowMCJ9--8f6ee538b0d79d98929a6111c573fefcf425c8aafbd748552a975949de11982b",
  "settings": {
    "is_hidden": false
  }
}
```

## Configure Slate Postbuffers in Your Project Settings

To configure your postbuffers:

1. Open your **Project Settings**.
2. Navigate to **Game** > **Slate RHIRenderer Settings** > **Post Processing**.
3. Unfold the drop-down for buffers that you want to configure. You can enable or disable each buffer as needed. ![Enable the postbuffer in your project settings.](https://dev.epicgames.com/community/api/documentation/image/c73a76d1-c935-49b1-99df-755a891e7eb3)
4. If you want to add a specific postprocess to a Slate postbuffer, select a **Post Processor Class** for it. ![Set the post processor class alongside your postbuffer settings.](https://dev.epicgames.com/community/api/documentation/image/8f98e28f-d091-4b21-8bf3-bfd8b90f0b30)
5. If you want to improve performance or save video memory, you can set the postbuffer to only be half the resolution of the game window (one quarter by area). If you are only using the buffer for blur, and the blur strength is always higher than 3.2, then this won’t have any effect on quality. Stronger blurs are always computed at half or lower resolution. ![Setting the postbuffer resolution to half.](https://dev.epicgames.com/community/api/documentation/image/106953af-119f-49f0-a31c-449eb35cab5a)

## Create and Use a Slate Post Processor Class

To create a new Slate postprocessor class:

1. Create a **new Blueprint Class** derived from **USlateRHIPostBufferProcessor** or one of its child classes. This tutorial uses USlatePostBufferBlur as an example. ![Use the Slate postbuffer blur class as the base for a new Blueprint](https://dev.epicgames.com/community/api/documentation/image/4516ea34-c592-4983-8d06-99f5a327e8e7)
2. Open the Blueprint for your new postprocessor, then edit the class defaults. Change the default setting for **Gaussian Blur Strength** to something other than the default value inherited from the parent class. In this example, the Gaussian Blur Strength is set to 10.0. ![Set the blur strength for the derived postbuffer blur class.](https://dev.epicgames.com/community/api/documentation/image/1b003f8a-85f3-4d87-bf00-9e8511fb3223)
3. Open **Project Settings** > **Slate Renderer Settings** > **Post Processing**, unfold the dropdown for one of your postbuffers, and set the **Post Processor Class** to your new postprocessor. ![Set the blur postprocessor on one of the postbuffers.](https://dev.epicgames.com/community/api/documentation/image/b397fdfd-2d02-48f5-bd8e-1ba5eef26fad)

UE now uses your postprocessor to process the backbuffer before widgets copy it. In this case, it adds a gaussian blur.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You also can implement your own postprocessor by deriving a new C++ class from <code>USlateRHIPostBufferProcessor</code>.",
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

### Modify a Slate Post Processor at Runtime

You can modify your Slate postprocessors’ values at runtime using the **Slate FX Subsystem**.

1. Create a **Slate FX Subsystem** node.
2. Call **Get Slate Post Processor** to get a postprocessor from one of your postbuffers.
3. Cast the postprocessor to the appropriate class.
4. Access the postprocessor’s parameters from the casted postprocessor object. ![Modifying a blur postprocessor at runtime in Blueprint.](https://dev.epicgames.com/community/api/documentation/image/e9f8c7ec-8707-4a01-a3b9-a967e9ee1a01) *The above image is only an example of how modifying a postprocessor at runtime looks. We do not recommend performing this operation on tick as depicted.*

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Because Slate postbuffers and postprocessors are global resources, if you modify a Slate Post Processor’s value as in the example above, it will change the value globally. Every instance of a Slate widget or UI material that uses this postprocess will therefore reflect that change. Use caution and communicate with your entire team before modifying Slate postprocess values at runtime.",
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

## Use the Postbuffer in a UI Material

To create a UI material that samples the postbuffer:

1. Create a new **Material**.
2. Set the Material’s **Material Domain** to **User Interface**. ![Set the material's domain to User Interface](https://dev.epicgames.com/community/api/documentation/image/bee1b621-cebe-4ba4-92a2-66af8a5bb699)
3. To sample a buffer, call the **GetSlatePost** function corresponding to the postbuffer you want to use. For example, `GetSlatePost0` gets Slate Postbuffer 0. ![Use a GetSlatePost node to get a postbuffer.](https://dev.epicgames.com/community/api/documentation/image/09371047-8e2d-45fb-a974-520b01e8795e)

### Tips for Using Postbuffers in UI Materials

The following are some tips for using postbuffers in UI materials:

- By default, GetSlatePost nodes only sample pixels behind the current widget, but you can modify this using the **UVs** input.
- Use **LinearRGB** to get a gamma-correct sampling of the backbuffer.
- **RGB** is useful for effects such as correct color inversion.

The following graph is an example of a material that uses a postbuffer to create a rotating UE logo that inverts the colors of the world behind it. The UE logo texture feeds into the Opacity output, while the Final Color inverts the RGB output of GetSlatePost0.

![A material that inverts and blurs portions of the buffer.](https://dev.epicgames.com/community/api/documentation/image/f68fe608-a889-4f8a-9206-fa4a0b6d3fb4)

This material is used in the image below. Note that the material samples the scene directly behind the widget despite having no UV input to `GetSlatePost0`.

![The previous material in use on UE logos in frame.](https://dev.epicgames.com/community/api/documentation/image/71dc0445-aeae-4144-8e9f-e38b63474b73)

To only capture the game scene, place the widget at the bottom of the hierarchy.

If you want the widget to also contain the UI, then capture the UI in your postbuffer by following these steps:

1. Find the **Post Buffer Update Widget** in the Palette in UMG Designer. ![The Post buffer update widget in the palette.](https://dev.epicgames.com/community/api/documentation/image/92f76ad6-a158-4577-aa9c-f55b972d5c56)
2. Add the Widget wherever you want a current UI update. The Slate postbuffer will update wherever this widget is placed. ![An example of the update widget placed in the hierarchy.](https://dev.epicgames.com/community/api/documentation/image/309a9654-e38f-443b-802b-e5dbbf7a1fa6)
3. Configure the Post Buffer Update Widget in the Details panel. ![Configuring the details of the post buffer update widget.](https://dev.epicgames.com/community/api/documentation/image/c5ecc785-530f-46c3-8511-1da18f21a23e)

The **Post Buffer Update Widget** has the following parameters:

| Parameter | Description |
| --- | --- |
| **Perform Default Post Buffer Update** | If true, the default scene-only copy / slate postprocess occurs. If false, the default copy / process does not occur. If no postbuffer updates have been "drawn" and this setting is off, when a widget attempts to sample the slate postbuffers, the behavior is undefined. The result could be the last frame or black and white, which should be avoided. |
| **Buffers to Update** | Deprecated. Use **Update Buffer Infos** instead. |
| Update Buffer Infos | An array of the Buffers that this widget will trigger a capture for, as well as the Post Processor properties for each. |

After you configure your Post Buffer Update Widget, other widgets can freely sample both the Scene and UI with any applied post FX for the buffers you select to update.

### Postbuffer and Draw Order

For postbuffer updates to function correctly, Slate must draw all the UI elements the postbuffer will sample *before* the postbuffer can sample them. Putting the postbuffer in an overlay within a vertical / horizontal / grid box might not guarantee this due to drawing out-of-order. As a guideline:

- The bottom layer of your hierarchy should be widgets you want to show postbuffer-affected visuals.
- The middle layer should contain the postbuffer widget.
- The top layer should be a material that samples the postbuffer and applies the effect to the bottom layer.

The following image demonstrates an effective draw order:

![An example hierarchy.](https://dev.epicgames.com/community/api/documentation/image/ac4929f8-11f9-438d-86b3-68c7fc026265)

The following images demonstrate the material applied to the images in the horizontal box:

![An example material that blurs the inside of a horizontal box.](https://dev.epicgames.com/community/api/documentation/image/7ce30701-7d0c-4ee6-9268-cf1249a44ce2)

## Technical Information and Limitations

The following are some technical insights and limitations on how Slate postbuffers behave.

### Sampling

GetSlatePost nodes sample the current state of the given postbuffer for widgets to sample. These buffers are global, so you need team planning to use them.

### Performance and Blur Postprocesses

When using postbuffers, an optimized version of the multi-step Kawase Dual Filter is used to approximate a Gaussian blur with high precision. Depending on the used blur strength, which corresponds to the Gaussian “sigma” value, the blur can be computed on a downscaled version of the image.

With increasing blur strength, the number of intermediate render passes also increases. However, using a higher blur strength will not result in a higher performance cost. In fact, using weaker blur strength might have a higher performance cost before the downscaling kicks in.

#### Multiple Post Processors

When you use multiple postbuffers with postprocesses on them, you only pay the performance cost for the postprocesses actually visible onscreen. For example, if you have two postbuffers that each use a blur postprocess with a different value:

- If only one of them is visible, you only pay for that one.
- If both are visible, then you pay for both of them.

### Minimizing Buffer Usage

Each buffer is only copied/populated if a widget is drawn that uses the buffer. When a buffer is not used for two frames, it is resized on the GPU to 1x1.

### HDR Support

Slate postbuffers support **HDR**. However, when using HDR, materials should **sample from RGB** instead of LinearRGB. Additionally, HDR support only works immediately with HDR Composite off. If you want to use HDR composite you may need to correct gamma values during use.

### Cached Buffer Usage

Widget materials cache postbuffer usage on material/texture creation and on resource update, but does not update this cached value per draw.

Because of this caching, if you run with the global CVar Slate.CopyBackbufferToSlatePostRenderTargets turned off, you may get stuck with materials showing no usage. In this scenario, materials attempting to use the postbuffers may only sample black / white. If this happens, you may need to restart if you want to clear the usage cache and get correct results. We encourage enabling Slate.CopyBackbufferToSlatePostRenderTargets in your \*Engine.ini or early on when testing.

When resizing in PIE with Post Buffer Update Widgets, sampling results may be black/white temporarily during the resize. This issue occurs because we are more conservative on postbuffer update widgets when it comes to size checking. This only occurs in PIE since PIE is more active about drawing during resizes due to drawing the editor. This does not occur in Standalone or Shipping builds.
