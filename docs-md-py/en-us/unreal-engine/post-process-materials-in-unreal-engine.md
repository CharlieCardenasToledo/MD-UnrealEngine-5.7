# Post Process Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine

> Application Version: 5.7

Post Process Materials enable you to set up materials that can be used with your post process to create visual screen effects for damage, area type effects, or overall look for your game
that can only be achieved via Post Process Materials.

In the following sections, you'll learn about setting up Post Process Materials, the available settings you can use, along with some examples of how to setup some of your own Post Process
Materials using different buffers, blending between Post Process Materials, and more.

## Post Processing Graph

```json
{
  "type": "include",
  "excerpt_id": 1928,
  "excerpt_assignment_id": 1498,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The engine already features complex post processing based on a graph of post processing nodes. The <strong>Post Processing Materials</strong>\ncan be additionally inserted in some specific position. See <a data-anchor-id=\"17831\" data-document-id=\"3225817\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine#faq\">Frequently Asked Questions section</a> for <strong>r.CompositionGraphDebug</strong> to get a dump of the full graph.\nThe graph is actually not only doing post processing but also some parts of the lighting.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "EGl",
  "settings": {
    "is_hidden": false
  }
}
```

Most of the time the graph is automatically creating intermediate render targets. This means if you want to blend with the former
color, you need to do the blending in the shader (using the input from PostProcessInput0).

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can create your own intermediate render targets with <a data-document-id=\"3940494\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-material-user-scene-textures-in-unreal-engine\">User Scene Textures</a>.",
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

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Post Process Materials should be used sparingly and only when you really need them. Whenever possible, such as for color correction or adjustments, bloom, depth of field, and various other effects, you should use the settings inherent to the Post Process Volume, which have been optimized and are more efficient.",
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

## Using a Post Process Material

Through post process settings (usually defined with post process volumes or camera settings) it is possible to blend (so called) blendable assets.
At the moment, only **Materials** and **Material Instances** are blendable assets. The engine provides a few post process materials but with this feature
you can create your own **custom post processing** without any programmer help.

Simply assign one or more post process materials to a post process volume in the **Blendables** section. First press the **+** to add
new slots, select a material in the **Content Browser**, and press the left arrow to assign it. Materials with equal Blendable Location and Blendable Priority (see below) are processed in order, and unused slots are simply ignored.

![Image](https://dev.epicgames.com/community/api/documentation/image/73b91818-d5b5-4e79-b8e0-f1e037bf8062)

## Critical Settings for Post Process Materials

A post processing material needs to specify the material domain **post process**:

![Image](https://dev.epicgames.com/community/api/documentation/image/37345ab4-085a-4268-bb41-a0225a080d0e)

The material should only use **Emissive Color** to output the new color. Additionally, you can define where during the post processing this pass should be applied
and, if there are multiple, in which order they should be processed (Blendable Priority):

![Image](https://dev.epicgames.com/community/api/documentation/image/272211e4-7709-48d6-b347-64c77483c184)

| Blendable Location | Description |
| --- | --- |
| **Before Tonemapping** | All lighting is provided in HDR with scene color when Scene Texture expression's Post Process Input 0 is used. It fixes issues with temporal anti-aliasing (TAA) and GBuffer lookups. For example, issues that can happen when using depth and normals. |
| **After Tonemapping** | This option indicates that post processing will take place after tonemapping and color grading has been completed. It is the preferred location for performance since the color is LDR and requires less precision and bandwidth. When this option is selected, the SceneTexture expression's Post Process Inputs 2 and 3 are used to control where Scene Color is in the pipeline. Input 2 applies scene color before tonemapping. Input 3 applies scene color after tonemapping. |
| **Before Translucency** | This is even earlier in the pipeline than 'Before Tonemapping' before translucency was combined with the scene color. Note that SeparateTranslucency is composited later than normal translucency. |
| **Replacing the Tonemapper** | PostProcessInput0 provides the HDR scene color, PostProcessInput1 has the SeparateTranslucency (Alpha is mask), PostprocessInput2 has the low resolution bloom input. |

The typical postprocess input comes from the pass before. That color can be accessed through the SceneTexture material expression when using **PostProcessInput0**. Using SceneColor might not give you the right results.

## Blending Between Different Material Instances

[Using A Post Process Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine)

With postprocess volumes, it is easy to setup soft transitions between multiple postprocess materials. Here we use one volume that is marked unbound and one volume that has larger blend radius (e.g. 1000):

|   |   |
| --- | --- |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/60e62b32-d868-4ffa-a7d6-174ef86d65c9) | ![Image](https://dev.epicgames.com/community/api/documentation/image/7f697ef1-e15c-4362-b24c-73363a3fe381) |
| Post Process Set to Unbound | Post Process Bound Volume |

The Priority on the Post Process Volume affects the *order of blending* for multiple instances of the same blendable material, in comparison to the Blendable Priority on the material, which affects the *order of rendering* between different blendable materials. Blending can be disabled by setting **Is Blendable** to **false** in the material properties, which causes each instance of the material to render independently (this can be potentially costly). Materials that write to a [User Scene Texture](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-material-user-scene-textures-in-unreal-engine) aren't blended.

Each volume we specify a different material instance of the same material. The color is specified as a material parameter which allows different settings for the two material instances.

![Image](https://dev.epicgames.com/community/api/documentation/image/fa93e6a3-eb07-4e21-b3ac-5eca9aaffaad)

| ![Image](https://dev.epicgames.com/community/api/documentation/image/c82910d3-7d9b-4b1f-ad87-d0d874c5761e) | ![Image](https://dev.epicgames.com/community/api/documentation/image/7ef4a188-7317-439f-b925-132fcf999835) |
| --- | --- |
| Material Instance RED | Material Instance GREEN |

Depending on the camera position the setting of one volume is used and blended when within the Blend Radius' range:

| ![Image](https://dev.epicgames.com/community/api/documentation/image/2673c953-b8dd-47b0-a260-3bb956167c11) | ![Image](https://dev.epicgames.com/community/api/documentation/image/8a193641-99b5-4dc5-b693-993520c71d65) | ![Image](https://dev.epicgames.com/community/api/documentation/image/f0ba8919-1da2-4ccf-8e6c-9d8c665bbbb5) |
| --- | --- | --- |
| Unbound Post Process Volume Material Instance (RED) set to 0.75 | Blend Radius of 1000 | Post Process Volume Material Instance (GREEN) set to 0.75 |

With camera movement, you can perceive soft linear transition between the two effects setting.

The following shows a top down view of a level that has how two volumes. The large unbound volume has a red material instance and the small volume has a green material instance specified as blendable.
The smaller volume has a higher priority. The material params are getting blended depending on the camera position.
The fuzzy borders are defined by the Blend Radius property specified in the volumes and extend the volume shape.

With the correct setup all blending happens as expected.

```json
{
  "type": "comparison_slider",
  "image_left_id": 25777805,
  "caption_left": "Bad Setup",
  "image_right_id": 25777806,
  "caption_right": "Good Setup",
  "image_left": {
    "id": 25777805,
    "file_name": "VolumeBlendBad.png",
    "file_size": 28137,
    "content_type": "image/png",
    "created_at": "2025-07-03T18:27:03.732+00:00",
    "height": 289,
    "width": 404,
    "storage_key": "21f11bc7-df33-4e24-95f8-fa4929a2a3e3",
    "context": "documentation"
  },
  "image_right": {
    "id": 25777806,
    "file_name": "VolumeBlendGood.png",
    "file_size": 34260,
    "content_type": "image/png",
    "created_at": "2025-07-03T18:27:03.827+00:00",
    "height": 289,
    "width": 404,
    "storage_key": "24ee3cfd-f44a-4a25-b871-fb4b1eedb3a6",
    "context": "documentation"
  },
  "image_left_storage_key": "21f11bc7-df33-4e24-95f8-fa4929a2a3e3",
  "image_right_storage_key": "24ee3cfd-f44a-4a25-b871-fb4b1eedb3a6",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

The difference between the both setup is the default value specified on the material (scalar or vector) parameters.
The good setup has values that make the pass appear to not have any effect (e.g. multiply with white or lerp with 0).

**In both setup we see this:** When the camera is outside the influence of either volume the postprocess pass is not getting rendered (visualize by the grey grid).
If we are fully inside either of the volumes we also see the correct blending.

**The bad setup :** When the camera enters the influence radius we see a hard transition but because is uses the wrongly specified default parameters.

**The good setup :** The transition of entering the camera the influence radius is well hidden and we see a smooth transition to the volume colors.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "All material instances properties are blended, no matter if the property checkbox is checked or not (in that case it blends the\nproperty from the parent). This is different from the post processing settings where an unchecked property is not having any effect.\nThis means if you blend a material instance, all properties are getting blended.",
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

## The Material Expression "SceneTexture"

You can add the **SceneTexture** material expression into your material and choose which texture you want to reference in the expression properties:

![Image](https://dev.epicgames.com/community/api/documentation/image/f8655a82-878a-4016-815a-8ee5923fbf74)

The node has an optional input and multiple outputs:

![Image](https://dev.epicgames.com/community/api/documentation/image/bae9719d-a259-4d97-ae43-8a0d955b53c3)

The **UV** input allows you to specify where you want to make a texture lookup (only used for the Color output).
The color output is a 4 channel output (actual channel assignment depends on the scene texture id). **Size** is a 2 component vector with the
width and height of the texture. The inverse of that (1/width, 1/height) is available in the **InvSize** output. It is handy when referencing
neighbor samples like in the example below:

![Image](https://dev.epicgames.com/community/api/documentation/image/509077a2-aaec-4596-a28e-49db5ae82024)

The material expression computes the depth difference of the current pixel to a neighbor pixel (e.g. In = 0,1 to return the delta to the pixel below).

## Using GBuffer Properties

A GBuffer consists of multiple textures that store material (e.g. subsurface/specular color, roughness, ...) and object attributes (e.g. normal, depth)
without lighting to compute shading (how light interacts with a material). In a deferred renderer, we first render the GBuffer and then compute all lighting (deferred)
with the GBuffer attributes. If using the deferred shading path (e.g. DirectX 11 or high end OpenGL), we can get access to those buffers during post processing.

Anti-Aliasing generally makes this a bit more difficult as a GBuffer pixel/texel is no longer 1:1 associated with an output pixel (see section below).

## CustomDepth

This separate feature enables masking of certain objects by rendering them into another depth buffer (called custom depth buffer).
This adds extra draw calls but no more materials. The rendering is fairly cheap as we only output depth. The feature can be activated on the mesh
(e.g. Static Mesh Properties / Render Custom Depth):

![Image](https://dev.epicgames.com/community/api/documentation/image/af9ca3ef-caff-4f10-b68f-7d302e04250d)

In this scene, we activated the feature on two objects but without a post processing pass visualizing the content, this feature remains invisible:

![Image](https://dev.epicgames.com/community/api/documentation/image/e54d2929-d4fa-4976-ac5c-2634c2a80bda)

Here we can see how a visualization of the Custom Depth looks like:

![Image](https://dev.epicgames.com/community/api/documentation/image/73630f06-5575-48d6-9b30-40f79d8f8712)

This is the material we used to visualize it:

![Image](https://dev.epicgames.com/community/api/documentation/image/838db62e-6a37-463f-8112-6304d6cf246b)

## CustomDepth Stencil

Custom Depth Stencil is an extension of Custom Depth where you can use a stencil, or cutout, of your rendered object to then do visually interesting things like the example below that enables you to
visualize occlude objects, draw object outlines, or only be visible from certain viewing angles. There is a lot of potential with what you can do by having access to the stencil of an Actor in your
scene. Using the following settings to enable and assign a stencil value.

![Image](https://dev.epicgames.com/community/api/documentation/image/266c5e91-9a82-4e87-b47f-09568c87f241)

In this scene, Custom Depth is enabled on three objects and a **Custom Depth Stencil Value** is set for each, but without any post processing pass to visualize the content, this feature remains invisible.

![Image](https://dev.epicgames.com/community/api/documentation/image/71cb8b93-bd72-4bc8-a172-446769448fb4)

Once you've setup your Post Process Material you will be able to visualize how the Custom Depth Stencil looks, The occluded objects render with a randomly assigned color based on the **Custom Depth Stencil Value** used.

![Image](https://dev.epicgames.com/community/api/documentation/image/5a4cdd84-9f4d-4661-86d9-d09c6445e027)

This is a setup of the Material we used to visualize it:

![Image](https://dev.epicgames.com/community/api/documentation/image/8d2cbadd-d9d9-4256-be21-ac4d9b90580d)

_Click image for full size._

This is by no means, the only way to use Custom Depth Stencil and in this particular Material setup the stencil is being divided so that it uses values between 1 and 255, a mask is being used
for any value that is between these values, a random color is being created for these values as well so as the Custom Depth Stencil Value changes so does the color, and finally the mask that is
created is being used in a way that only colors the stencil if the object is occluded.

## Temporal Anti-Aliasing or Why the GBuffer Jitters

Temporal anti-aliasing is a unique Unreal Engine feature that greatly improves image quality with a very moderate performance cost.

By default, a post process material is inserted in the end of the post processing graph (after tone mapper). This means you get the final LDR color after tone mapping, color grading and after the temporal anti-aliasing
was applied. This is the best spot for many simple post processing effects - for performance and ease of use.

Here you can see how we used the custom depth input to visualize a silhouette around specific objects:

![Image](https://dev.epicgames.com/community/api/documentation/image/a51af53b-bd76-4bd4-aec5-1d0e0dac68ab)

Notice that the former image has no anti-aliasing on the silhouette but in motion you also would see the silhouette jittering around 1 pixel.
This is because temporal anti-aliasing moves the rendering of the whole scene by a sub pixel each frame. Multiple frames together are getting combined to produce the final anti-aliased image.
We can however move the material to an earlier spot in the post processing graph to fix this issue.

This is the result:

![Image](https://dev.epicgames.com/community/api/documentation/image/2bd5b6f8-becf-4c25-8489-af6f3567ac2f)

We get a stable and anti-aliased image. In motion we might see some artifacts with the temporal anti-aliasing. This feature is using the depth buffer to replace old images. With the border rendered inside the object
it works well enough, but outside the object we would also need to adjust the depth buffer (not done yet, costs extra performance), ideally this should not be.

## UV and ScreenPosition

With post process materials you can look up into screen aligned buffers, but you need to know the right UVs.
The **ScreenPosition** material expression with the mapping option set to **ViewportUV** outputs the UV with 0,0 at the left top of the viewport and 1,1 at the bottom right.
In contrast, using the **SceneTextureUV** mapping in this material expression might give you different results. This is because the actual texture (more correctly it is a render target) is potentially larger than the viewport.
It can be larger in editor because we share this texture for multiple viewports and the largest extent is used for all viewports.
Even in game it can be larger in some cases (e.g. SceneCaptureActors might have a smaller viewport, Matinee black borders, Splitscreen, VR, ...).

The **SceneTextureUV** option gives you the UV for this larger texture. If you only need a relative offset (e.g. pixel sized edge detection) you need to scale with the right size.
The **SceneTexture** material expression has outputs for the size and the inverse of the size (efficient and useful for pixel offsets).
To test all that, you can use the console variable **r.ViewPortTest** which allows you to test various viewport configurations.

## Filtered texture lookups

The SceneTexture material expression has a checkbox to get [bilinear] filtered lookups. Using this option can result in a slower rendering so it should be only used if needed.
Many of the screen space textures do not support filtering (e.g. GBuffer). Not exposing this property allows the engine to compress the data if needed (packing prevents filtering).

## Replacing the Tonemapper

It is possible to override the in engine tonemapper with your own one by using the "Replacing the Tonemapper" blendable location. This is a work in progress feature meaning it will likely change and it does not have all the functionality yet.

![Image](https://dev.epicgames.com/community/api/documentation/image/761e790e-2ada-456e-b96a-ef8ee3978851)

We started exposing some Post process setting parameters to the tonemapper but that part is likely to change quite a bit.
The values are exposed as material parameters and need to have the exact name.

Vector parameter:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Engine.FilmWhitePoint",
  "lines_of_code": 1,
  "id": 73797,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3Mzc5NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU1OjU3KzAwOjAwIn0=--d1e0ac7caabf924aea6523a6b24739d064a0fde020717c3d0781123ef9b9c67c",
  "settings": {
    "is_hidden": false
  }
}
```

Scalar parameter:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Engine.FilmSaturation\n\tEngine.FilmContrast",
  "lines_of_code": 2,
  "id": 73798,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3Mzc5OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU1OjU3KzAwOjAwIn0=--19f3ecd359c847096b4b6858a60179a47008fcc0cbac293589f38d96f9610c39",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "In order to get the parameters you need to create a material instance from the post process material.",
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

You still can use your own parameters and get them blended like other post process material settings.

## Known Issues

- **Material expression SceneTexture** Separate Translucency does not work Certain lookups do not work in certain passes Material Functions may report an error but can still be used in a Material with the Post Process domain.
- **Material** UV in the Post Process Material might not be in the 0-1 range (for example, in the editor when reducing the viewport size), which aligns with the lookup but makes it hard to implement something like a vignette effect. Outputting alpha is not yet supported. Use Opacity instead. Using World Position with [Temporal Anti-Aliasing Upsampling](https://dev.epicgames.com/documentation/en-us/unreal-engine/screen-percentage-with-temporal-upscale-in-unreal-engine) requires sampling the depth buffer after temporal upscaling (TAAU, DLSS, and Temporal Super Resolution) that will cause aliasing in the output since the use of it can not be anti-aliased. For this reason, we recommend making the effect take place before temporal upscaling.
- **Blending** When blending two post process volumes with a Blend Radius, it is possible to see a non-soft transition. This can be avoided by using an unbound volume with a material instance setting that represents the default.

## FAQ

- **Can I have the "Lighting only mode" texture as input?** No, we do not have this data available as an intermediate step. For this view mode, we generate it by ignoring the material colors. To make this a fast option, it would require restructuring a large part of the rendering code.
- **Why a SceneColor lookup shows banding but when using PostProcessInput0, I do not see that?** When SceneColor is used we create a lower quality copy of the scene to allow a lookup into a texture that we currently write to (General case is rendering any mesh where this is not possible). In Post Processing, you should use PostProcessInput0.
- **How much memory do I pay for a post process?** Memory cost depends on screen resolution. Before tone mapping we use HDR (8bytes per pixel), after we use LDR (4 bytes per pixel).
- **How can I lower the render cost for post processing?** Measure on the target platform, keep the texture lookup count low, do less math operations and reduce dependent texture lookups, avoid randomized texture lookup (can be slower due to texture cache misses).
- **How many passes I can use?** Each pass adds to the performance cost. Try to combine passes and activate passes only if needed. General game features e.g. noise could be added to the engine passes for better performance.
- **How much CPU performance do I pay per post process and for blending?** Blending materials is very cheap. All material instances properties are getting blended and only one post process material pass with those settings gets rendered.
- **I need to use "Before Tonemapper" to get proper TemporalAA. When I use a color, it is tone mapped and therefore looks different. How can I prevent that?** There is no easy solution. You would need to do an inverse tonemaping operation (expensive). The color also might appear different depending on eye adaptation. You could expose the EyeAdaptation level to the SceneTextures to compensate for that.
- **How can I get a full dump of the post processing graph?** **r.CompositionGraphDebug** can log the graph into the console. Example:
