# Post Process Effects

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine

> Application Version: 5.7

Post-processing effects enable artists and designers to define the overall look and feel of the scene through a combined selection of properties and features that affect coloring, tonemapping, lighting, and more. A special type of volume, called a **Post Process Volume**, can be added to a Level to access these features. Multiple volumes can be placed to define the look of a specific area, or it can be set to affect the entire scene.

## Using Post Process Volumes

You can add a **Post Process Volume** into your Level using the **Place Actors** panel.

Click image for full size.

Once placed in the Level, use the **Details** panel to access all the available properties and features. You'll find that they are broken up into categories for the type of feature they are and what they affect.

Click image for full size.

The **Post Process Volume Settings** are specific settings for this placed volume and how it interacts with the scene and with any other Post Process Volumes it may overlap with. For example, you can toggle the **Infinite Extent** property to make this Post Process Volume affect everywhere in the scene, or leave it unchecked to have it affect only a certain area. When Volumes overlap, you can control how they interact with one another to blend from one to another, which is useful when you have radically different looks between them.

| Property | Description |
| --- | --- |
| **Priority** | Specifies the priority of this volume. In the case of overlapping volumes, the one with the highest priority overrides the lower priority ones. The order is undefined if two or more overlapping volumes have the same priority. |
| **Blend Radius** | Sets the radius (in world units) around the volume that is used for blending. For example, when walking into a volume, the look can be different than that outside of the volume. The blend radius creates a transitional area around the volume. |
| **Blend Weight** | The amount of influence the volume's properties have. A value of 1 has full effect, while a value of 0 has no effect. |
| **Enabled** | Whether this volume affects post processing or not. If enabled, the volume's settings are used for blending. |
| **Infinite Extent (Unbound)** | Whether the bounds of the volume are taken into account. If enabled, the volume affects the entire scene, regardless of its volume's bounds. When not enabled, the volume only has an effect within its bounds. |

## Post Process Features and Properties

Access a Post Process Volume's properties and settings by selecting one placed in the Level. The **Details** panel will list the available categories and their available properties.

Unreal Engine uses some default post processing settings, even if you don't have a placed Post Process Volume in your Level. These default post process settings can be found and configured in the **Project Settings** in the **Rendering > Default Settings** section.

Configuring these options can be useful for Level Editing to stabilize auto exposure or bloom before you start working on defining the look of the scene.

## Lens

The **Lens** category contains properties and settings that simulate common real-world effects from a camera lens.

### Depth of Field

Similar to what happens with real-world cameras, **Depth of Field** applies a blur to a scene based on the distance in front of, or behind, a focal point. The effect is used to draw the viewer's attention to a specific subject in the shot based on depth. It also adds an aesthetic which makes the rendered image appear more like a photograph, or film.

![Depth of Field Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ddbff770-3014-4665-bbef-f23359ab1c38/dof_cine_disabled.png)

![Cinematic Depth of Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b1fd02a-7cff-48cc-af40-27c0f75c6a7f/dof_cine_enabled.png)

There are two depth of field options available:

* [Cinematic Depth of Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-depth-of-field-in-unreal-engine) is used for desktop and console platforms. It provides a filmic look with properties that align with those found on real-world cameras. The Post Process Volume provides some settings, but primarily the camera properties found on a [Cinematic Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine) should be used to control depth of field.
* [Mobile Depth of Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-depth-of-field-in-unreal-engine) is an optimized, low-cost option that works for mobile platforms. It uses gaussian blurring to set a focal region with near and far transition areas.

For more information, see [Depth of Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine)

### Bloom

**Bloom** is a lighting artifact of real-world cameras that also adds to the perceived realism of the rendered image by reproducing glow around lights and reflective surfaces. Bloom is an effect that works with other effects, like lens flares and dirt masks, but those are not covered by the general bloom properties.

![Convolution for Bloom: Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09687b5d-42de-4b64-a2f3-68e0494bd9ee/fftbloom_enabled.png)

![Convolution for Bloom: Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6a15cc3-f3a6-46a2-84d6-20af5f3e447f/fftbloom_disabled.png)

For more information, see [Bloom](https://dev.epicgames.com/documentation/en-us/unreal-engine/bloom-in-unreal-engine)

### Exposure and Local Exposure

The engine automatically controls exposure — though it's sometimes called eye adaptation — which adjusts how bright, or dark, the scene becomes for the current view based on current scene luminance. This effect recreates the experience of human eyes adjusting to different lighting conditions, like when walking from a dimly lit interior to a brightly lit exterior, or the other way around.

The **Exposure** category contains properties to select the type of exposure method to use and to specify how bright or dark it should allow the scene to become over a given time.

There is an additional control for exposure called **Local Exposure** that has its own category or properties. These properties apply local adjustments to exposure (within artist-controlled parameters) using edge-aware data structure while preserving luminance detail. This makes it particularly useful in challenging high contrast scenes, such as indoor scenes with very bright outdoors that are visible through doors and windows.

For more information, see [Exposure](https://dev.epicgames.com/documentation/en-us/unreal-engine/auto-exposure-in-unreal-engine)

### Chromatic Aberration

**Chromatic Aberration** is an effect that simulates the color shifts in real-world camera lenses. It's a phenomena where light rays enter a lens at different points causing separation of RGB colors.

![Without Chromatic Aberration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c3c2365-c13c-4078-a3bb-5d48d14c3ddb/scenefringe_0.png)

![With Chromatic Aberration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e72ba27-18f0-4c16-bdde-2e30051bdbe8/scenefringe_2.png)

| Property | Description |
| --- | --- |
| **Intensity** | The amount of aberration/camera fringe, or camera imperfection, to simulate an artifact that happens in real-world camera lenses. |
| **Start Offset** | A normalized distance to the center of the framebuffer where the effect takes place. |

### Dirt Mask

The **Dirt Mask** is a texture-driven effect that brightens up the [Bloom](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine#bloom) in defined areas of the screen. It can be useful to create a specific look of a camera lens and its imperfections, or something like dirt and dust that has gotten on the lens.

![Dirt Mask Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95beae32-942d-4beb-998a-f2e7af1920f4/dirtmaskenabled.png)

![Dirt Mask Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a14f3dd-1da2-4565-9735-892281f8a5f1/dirtmaskdisabled.png)

| Property | Description |
| --- | --- |
| **Dirt Mask Texture** | Texture that defines the dirt on the camera lens where the light of very bright objects is scattered. |
| **Dirt Mask Intensity** | The intensity of the dirt mask. |
| **Dirt Mask Tint** | Apply an RGB color value to the dirt mask texture. |

### Camera

A set of properties controlling the camera shutter and cinematic depth of field.

Full properties and physically based properties of the camera should be set on the [Cinematic Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine).

| Property | Description |
| --- | --- |
| **Shutter Speed (1/s)** | The camera shutter speed in seconds. |
| **ISO** | The camera sensor sensitivity to light. |
| **Aperture (F-stop)** | Defines the opening of the camera lens. Aperture is 1/f-stop. Typical lenses go down to f/1.2 (a large opening). Small numbers have a larger aperture opening, blurring more of the foreground and background. Larger values have a smaller aperture, blurring less of the foreground and background. |
| **Maximum Aperture (min F-stop)** | Defines the maximum opening of the camera lens to control the curvature of blades of the diaphragm. set it to 0 to get straight blades. |
| **Number of diaphragm blades** | Defines the number of blades of the diaphragm within the lens (between 4 and 16). This defines the shape of the bokeh. |

### Lens Flare

The **Lens Flare** effect is an image-based technique that simulates the scattering of light when viewing bright objects due to imperfections in the camera lens.

![lens flare](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/139ebc0b-6c9a-4c01-977a-20786bdeeee9/lens-flare.png)
