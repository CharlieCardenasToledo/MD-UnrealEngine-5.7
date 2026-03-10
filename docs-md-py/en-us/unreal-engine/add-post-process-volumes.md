# Add Post Process Volumes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/add-post-process-volumes

> Application Version: 5.7

In this tutorial, you’ll create a nighttime scene using the materials and assets from the [previous tutorial](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances) and a selection of post-process effects including **exposure**, **bloom**, **lens flare**, and **color gradin****g**. You’ll also learn how to improve the quality of lighting and reflections in your scene using **post process volumes** and [Lumen Global Illumination and Reflections](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine).

**Post process effects**non-destructively change the look and feel of a level. You can picture these effects like applying a filter to a camera, or holding a color gel in front of the lens.

![Camera with a pink filter](https://dev.epicgames.com/community/api/documentation/image/473809fa-8bf7-4227-9913-55e14186bbbc)

_A camera looking through a pink color gel._

Post process effects can be applied in realtime, without altering assets within a level. Since these effects are non-destructive, they're useful for making visual changes without disrupting Materials or complex lighting setups.

The only difference between the levels in the images below is **color grading** — a category of post processing.

| ![Room-with-amber-light](https://dev.epicgames.com/community/api/documentation/image/7aded10e-2956-40b0-b8f3-0da5ac1dbf5c) | ![Room-with-cool-tones](https://dev.epicgames.com/community/api/documentation/image/df948053-5ac2-42c0-ac99-2003e53cd1c9) |
| --- | --- |

Game developers use different types of post process effects to direct player attention, communicate gameplay information, and enhance visual storytelling. For example:

- [Color Grading](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) can mimic different times of day, change the mood of a scene, or visually communicate narrative devices such as flashbacks.
- [Reflections](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) can add realism and deepen immersion during gameplay.
- [Bloom](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) can be used in combination with [exposure](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) and [lens flares](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) to emphasize glow, reflectivity, or direct attention to an asset.

Multiple post process effects can be combined to establish a consistent visual style for a game, or used in specific gameplay situations. In the demonstration below, we used multiple effects to visually communicate when a player is underwater.

[Video: V_Mdi9TM](https://dev.epicgames.com/community/api/cms/videos/V_Mdi9TM/embed.html)

Post process effects are also used to control optimization for lighting features. If you’ve ever played a AAA video game, you may have noticed options to adjust resource-intensive effects, such as **reflection quality**. Later in this tutorial, you’ll use post process volumes to balance fidelity and performance for reflection quality in Unreal Engine.

| ![Image](https://dev.epicgames.com/community/api/documentation/image/3a577d11-cd6d-4999-acdd-62ddb8121116) | ![Image](https://dev.epicgames.com/community/api/documentation/image/42f358db-edd6-4a1f-8418-b3f6dab66c75) |
| --- | --- |

Next, let’s look at how post process effects are applied in game levels.

## The Anatomy of Post Process Volumes

Post process effects can be applied to a level by using placeable **post process volumes**. Volumes define the area that an effect applies to. These volumes are invisible to players during runtime and can be **bound** or **unbound**.

![A-Post-Process-Volume-and-its-visible-bounds.](https://dev.epicgames.com/community/api/documentation/image/8196d04e-6062-4218-9f41-01f9c341a9ff)

_A post process volume and its visible bounds._

Let’s look at an example that shows the difference between bound and unbound volumes. In the image below, we created three post process volumes that affect **Saturation**.

![1-is-unbound-2-is 25%-saturation-3-is-0%-saturation](https://dev.epicgames.com/community/api/documentation/image/2b225ce2-92dc-4480-8d8c-a74e6b719a03)

_(1) Unbound, 100% Saturation (2) Bound, 25% Saturation (3) Bound, 0% Saturation_

[Video: V_jLKUaZ](https://dev.epicgames.com/community/api/cms/videos/V_jLKUaZ/embed.html)

Notice two things in the video above. As the player walks down the hallway:

- The **unbound** volume’s saturation is unchanged even when the player is **not inside** the volume. This is because unbound volumes apply effects **globally**; to the entire level. The scale and location of the volume doesn’t matter.
- The **bound** volume’s saturation is only visible when the player is **inside** the volume. This is because bound volumes apply effects **locally**; to the area within their perimeter.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Later on, you’ll learn how to blend volumes to initiate effects as players approach their perimeter",
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

Volumes can layer hierarchically, like layers in a graphic design software. Unbound, or **global volumes**, layer over smaller, bound volumes inside a level. Similarly, you can set a layering priority for bound volumes that overlap one another.

![Image-of-a-volume-cube-within-a-volume-cube](https://dev.epicgames.com/community/api/documentation/image/2ed669cc-b0d2-4610-845c-63e1ae122e22)

Global volumes help maintain a consistent visual style throughout your game, act as a foundation for further layering, and keep your workflow organized.

For example, building up visual effects layer-by-layer can avoid unexpected results that are difficult to locate and debug. For teams that work with hundreds of effects over multiple levels, staying organized can save valuable development and debugging time.

Next, you’ll set up three post process volumes in your level and set their priority.

## Set Up Global and Local Volumes

Let’s revisit the post process volume you created in [Light a Scene](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-02-light-a-scene) and verify that it’s applying effects globally:

1. In the **Outliner**, search for the **PostProcessVolume** and select it.
2. Rename this volume `PPV_Global`.
3. In the **Details** panel, expand **Post Process Volume Settings**.
4. Verify that **Infinite Extent (Unbound)** is checked and **Priority** is set to `0`. ![Post-process-volume-settings](https://dev.epicgames.com/community/api/documentation/image/9bd49bb1-f67c-45c6-aa3d-a6370cf8e006)

Next, you’ll make two new volumes; one that surrounds Room 3 and another that surrounds the Level Transition Point within Room 3.

You’ll adjust the **Priority** of each bound volume to take precedence over the global volume when the player enters it. When setting priority, higher values take precedence over lower values.

To create new volumes, follow these steps:

1. In the Editor’s main toolbar, click **Create > Visual Effects > Post Process Volume**. Alternatively, you can search for it. Add two volumes. ![Post-process-volume-option-in-the-dropdown](https://dev.epicgames.com/community/api/documentation/image/49209897-efce-4f6c-93f2-64451363621c)
2. Name the first volume `PPV_Room3` and the second `PPV_LevelTransition`. ![PPV-volume-options](https://dev.epicgames.com/community/api/documentation/image/7b4220c4-2e32-4dee-bdbe-21ae086ff43e)
3. In the **Outliner**, select `PPV_Room3` and set its **Scale** to `8.5, 10, 5`.
4. Set its **Location** to `1600, -1050, 370`. This should roughly surround Room 3. ![Room-3-with-yellow-box-of-the-volume](https://dev.epicgames.com/community/api/documentation/image/87b2dcaa-601f-47dc-a1b8-03e6f26ae112)
5. Under **Post Process Volume Settings**, set **Priority** to `100`. ![Priority-set-to-100](https://dev.epicgames.com/community/api/documentation/image/10b00f33-d7e0-446b-b0c9-99ab3f9054cd)
6. Set the **Blend Radius** to `0` and verify that **Infinite Extent** is unchecked. ![Blend-radius-and-infinite-extent](https://dev.epicgames.com/community/api/documentation/image/2eb504e3-a413-4c17-b197-8572f449993f)
7. Select `PPV_LevelTransition` and set its **Scale** to `1.5, 1.5, 2.5`.
8. Set its **Location** to `2170, -1450, 600`. This should roughly surround the Level Transition Point. ![Arrow-to-the-transition-platform](https://dev.epicgames.com/community/api/documentation/image/23c0fc84-450a-4f42-b2f0-50eed44c9303)
9. Set its **Priority** to `200` and verify that **Infinite Exten****t** is unchecked. ![Priority-at-200](https://dev.epicgames.com/community/api/documentation/image/6e8d689b-0f43-4364-be2d-d92bcd117a25)

Your volumes for this tutorial are now set up.

## Experiment with Post Processing Presets

![Image](https://dev.epicgames.com/community/api/documentation/image/a01e2849-4ea3-4e76-819d-0f87a3a48b0f)

In this section, you’ll experiment with effects from the following post-processing categories:

- **Lens** Exposure Bloom Lens Flare
- **Color Grading** Offset Contrast

- **Global Illumination and Reflections** Lumen Scene Lighting Quality Lumen Scene Detail Reflection Quality Screen Traces Max Roughness To Trace

### Exposure

**[Exposure](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine)** controls the upper and lower limits of brightness in a level. Remember, post process volumes don't alter the properties of other actors within your level. In the demonstration below, the brightness of the **light source** isn’t changing. Instead, what’s changing is the **maximum amount of visible light** allowed into the camera lens.

In the real world, this effect is similar to how a camera’s aperture controls the amount of light it captures. Or, how your pupils dilate and constrict to adjust to different lighting conditions. This is why exposure in Unreal Engine is also called **Eye Adaptation**.

[Video: V_AuZ3BL](https://dev.epicgames.com/community/api/cms/videos/V_AuZ3BL/embed.html)

With exposure, you can mimic real-world optical effects and add realism to a game. For example, when a player moves from a dark area to a bright area, extending the duration of time it takes for the global exposure to adjust can mimic the time it takes for a human eye to adjust to brighter light.

[Video: V_zfSeel](https://dev.epicgames.com/community/api/cms/videos/V_zfSeel/embed.html)

In this section, you’ll adjust the exposure for `PPV_Global` and `PPV_Room3` to create a transition to nighttime when a player walks into Room 3.

To set exposure, follow these steps:

1. In the **Outliner**, select `PPV_Global`.
2. In the **Details** panel, under **Exposure**, check **MIN EV100** and set it to `-10`.
3. Check **MAX EV100** and set it to `20`.
4. In the **Outliner**, select `PPV_Room3`.
5. In the **Details** panel, under **Exposure**, check **MIN EV100** and set it to `-1.0`.

Test your level by right-clicking in the viewport and selecting **Play From Here**. As you move towards Room 3, the exposure should change but the change is too abrupt.

[Video: V_HYSB5i](https://dev.epicgames.com/community/api/cms/videos/V_HYSB5i/embed.html)

To extend the duration of the change, you’ll blend the global volume with the bound volume by using **Blend Radius**:

1. In the **Outliner**, select `PPV_Room3`.
2. Under the **Post Process Volume Settings**, set **Blend Radius** to `1500`.

Test your level. Now, as you move towards Room 3, the exposure should change gradually.

[Video: V_GO0SgG](https://dev.epicgames.com/community/api/cms/videos/V_GO0SgG/embed.html)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Your level may look different than ours even with the same exposure values. In the <a data-anchor-id=\"20156\" data-document-id=\"4596430\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-04-expanded-material-instances#create-an-emissive-material\">previous tutorial</a>, we changed settings in the <b>Directional Light </b>to appear more like dusk.",
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

Next, you’ll adjust the glow of the neon signs with bloom.

### Bloom

[Bloom](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) is a lighting imperfection where light appears to bleed past the boundaries of a light source or reflection.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26261113,
  "caption_left": "Bloom disabled.",
  "image_right_id": 26261114,
  "caption_right": "Bloom enabled.",
  "image_left": {
    "id": 26261113,
    "file_name": "fftbloom_disabled.png",
    "file_size": 724499,
    "content_type": "image/png",
    "created_at": "2025-11-11T22:18:18.756+00:00",
    "height": 447,
    "width": 790,
    "storage_key": "7e32c6ef-b2cd-41ce-a184-0de4abd7e5f1",
    "context": "documentation"
  },
  "image_right": {
    "id": 26261114,
    "file_name": "fftbloom_enabled.png",
    "file_size": 721932,
    "content_type": "image/png",
    "created_at": "2025-11-11T22:18:23.728+00:00",
    "height": 447,
    "width": 790,
    "storage_key": "af3b3e0c-ae2a-4c6a-927c-c7e8333e2033",
    "context": "documentation"
  },
  "image_left_storage_key": "7e32c6ef-b2cd-41ce-a184-0de4abd7e5f1",
  "image_right_storage_key": "af3b3e0c-ae2a-4c6a-927c-c7e8333e2033",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

In film, this imperfection comes from how camera sensors and lenses capture light, but the effect can be mimicked in games for artistic purposes. For example, bloom and exposure can be used to visually communicate that a player has entered a dream sequence, flashback, or is stunned after an explosion.

In Unreal Engine, you’ve already seen bloom at work in the [previous tutorial](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-04-expanded-material-instances#create-an-emissive-material) when you increased your emissive material’s **Brightness** parameter above a value of 1.

![Emissive-mask-in-blueprints](https://dev.epicgames.com/community/api/documentation/image/f890131e-8164-4723-9312-485ce9ad0a7e)

Instead of adjusting the properties of each individual asset to achieve widespread results, let’s use your post process volume to control the overall bloom in Room 3:

1. In the **Outliner**, select `PPV_Room3`.
2. In the **Details** panel, expand the **Lens** category.
3. Expand the **Bloom** category, then check **Intensity**. Set it to `0.8` or use your own values.
4. Check **Threshold** and set it to `1` or use your own values. ![Image](https://dev.epicgames.com/community/api/documentation/image/bc97d639-4bc7-4e29-9078-38025c1787d7)

**Threshold** sets the minimum value at which bloom begins to have an effect on the level. You can think of this like a clamp, as seen in the previous tutorial. **Intensity** controls how strong the bloom is, once it takes effect.

[Video: V_bzWsqJ](https://dev.epicgames.com/community/api/cms/videos/V_bzWsqJ/embed.html)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "A threshold of -1 allows all colors in a level to affect bloom.",
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

Next, you’ll add lens flare to the neons signs.

### Lens Flare

A lens flare is a lighting artifact that occurs when bright light reflects off of imperfections in a lens or internal elements of a camera.

The effect can be mimicked in games for artistic purposes. For example, lens flares can direct attention to a reflective asset, promote photorealism, or emphasize the strength of the sun when a player looks into it.

![Image-looking-through-columns-at-a-lens-flare](https://dev.epicgames.com/community/api/documentation/image/c46326d6-9d3c-4848-9c93-80b7ff50008c)

To create lens flares in your level, follow these steps:

1. In the **Outliner**, select `PPV_Room3`.
2. In the **Details** panel, expand **Lens > Lens Flares**.
3. Check **Intensity** and set it to `0.5`.
4. Check **BokehSize** and set it to `5`.
5. Check **BokehShape** and search for `DefaultBokeh`. ![Bokeh-options-in-the-menu](https://dev.epicgames.com/community/api/documentation/image/5cc35dca-4ac1-4845-8aeb-6d01886c5b87)

Test out your work by moving and back forth in front of a light source or emissive Material in your level.

[Video: V_nonoyk](https://dev.epicgames.com/community/api/cms/videos/V_nonoyk/embed.html)

Next, you’ll use color grading to communicate gameplay mechanics to players.

### Color Grading

Much like in image editing software, you can use color grading to affect a level’s **Saturation**, **Contrast**, **Gamma**, **Gain**, **Offset**, **Tint**, and more.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26261153,
  "caption_left": "Color grading disabled.",
  "image_right_id": 26261155,
  "caption_right": "Color grading enabled.",
  "image_left": {
    "id": 26261153,
    "file_name": "HighresScreenshot00006.png",
    "file_size": 2641948,
    "content_type": "image/png",
    "created_at": "2025-11-12T00:37:18.009+00:00",
    "height": 1157,
    "width": 2763,
    "storage_key": "4ba22c51-faf3-43c7-9897-f648d9fb1716",
    "context": "documentation"
  },
  "image_right": {
    "id": 26261155,
    "file_name": "HighresScreenshot00007b.png",
    "file_size": 2927312,
    "content_type": "image/png",
    "created_at": "2025-11-12T00:42:49.637+00:00",
    "height": 1157,
    "width": 2763,
    "storage_key": "9d2ee83b-32e0-4fb8-8a5e-085aae541266",
    "context": "documentation"
  },
  "image_left_storage_key": "4ba22c51-faf3-43c7-9897-f648d9fb1716",
  "image_right_storage_key": "9d2ee83b-32e0-4fb8-8a5e-085aae541266",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

With these tools, you can change the level’s perceived time of day, mood, or genre conventions. For example, sepia-tone is a style of color grading that suggests antiquity.

![Sepia-tone-color-grading-in-real-time.](https://dev.epicgames.com/community/api/documentation/image/e58d0f2f-6e31-465b-bf96-8dea9e5c818b)

_Sepia-tone color grading in realtime._

For your level, you’ll use color grading to communicate to the player when they’ve entered a Level Transition Point. The Level Transition Point is a game mechanic created in [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine) that takes players to a new level.

![Image-of-player-character-on-a-glowing-platform](https://dev.epicgames.com/community/api/documentation/image/64438711-256f-4826-ad57-b56560e744fc)

Currently, when you stand on the Level Transition Point, the Rect Light beneath you isn’t powerful enough to compete with the Directional Light and Point Lights around the room. From the player’s point of view, the change from gameplay to Level Transition could be more clearly communicated.

![Glowing-platform-with-glowing-cube](https://dev.epicgames.com/community/api/documentation/image/a4211518-0ae3-462a-bd2b-1398a8ceb552)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If presented clearly and consistently, players learn to recognize and expect visual cues that signal game mechanics in your level.",
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

To solve this problem with post-processing, follow these steps:

1. In the **Outliner**, select `PPV_LevelTransition`.
2. In the **Details** panel, expand **Color Grading > Global**, and check **Offset**.
3. Choose your own values or set **R** = `-1.0`, **G** = `-0.02`, **B** = `0.15`, and **Y** = `0.07`. ![Image](https://dev.epicgames.com/community/api/documentation/image/0c2319a0-8e4d-42a4-97dc-973b38232261) The room should now appear blue: ![Image](https://dev.epicgames.com/community/api/documentation/image/0dcd1f49-e9c1-4e8b-ac90-d46c0db3dc57)
4. To correct the white hotspot created by the Point Light, expand **Color Grading > Highlights** and check **Contrast**.
5. Set the values to **R** = `0.5`, **G** = `0.8`, **B** = `0.7`, and **Y** = `1`. ![Image](https://dev.epicgames.com/community/api/documentation/image/3312ef4d-cbfb-4a80-91e8-b2ff6cdd019e) The hotspot should be less noticeable: ![Image](https://dev.epicgames.com/community/api/documentation/image/cf7fcaf7-bf03-4cbe-9fc4-ea0a3d381bd5)

To test your work, right-click in the viewport and select **Play From Here**. When you run onto the JumpPad and land on the Level Transition Point, the screen should become blue.

[Video: V_6RDrKA](https://dev.epicgames.com/community/api/cms/videos/V_6RDrKA/embed.html)

Next, you’ll use post process volumes to control optimization for reflection quality.

### Global Illumination and Reflections

Post process volumes can control the quality and scope of visual effects. This can help you balance fidelity and performance when working with expensive rendering features such as dynamic lighting.

Remember that resource allocation often affects decisions made in development. In vast, exterior levels you can use post process volumes to conserve quality in areas far away from the player — where they won't notice. This saves resources for areas where quality matters, such as immediately around the player during gameplay or around a camera during a cinematic.

![Image](https://dev.epicgames.com/community/api/documentation/image/3470e889-9d31-43f2-be80-c5ab8793a5ef)

A volume’s **Global Illumination** and **Reflections**settings contain different lighting calculation methods suited for different development needs:

| Method | Description |
| --- | --- |
| **None** | Disables any global illumination or reflection calculations. Light sources will not create bounce light or reflections, and shadows will appear solid black. |
| **Lumen** | [Lumen Global Illumination (GI)](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine) is Unreal Engine's fully-dynamic global illumination system that works with all lighting types. |
| **ScreenSpace** | [Screen Space Global Illumination (SSGI)](https://dev.epicgames.com/documentation/en-us/unreal-engine/screen-space-global-illumination-in-unreal-engine) is a fast, dynamic lighting system that only calculates lighting for what appears within the screen view. |

When the **Lumen** method is selected in the demonstration below, notice that the orange glow from the neon arrows dynamically contributes to the scene. This is because emissive materials (which are not a light source) are calculated when using Lumen but not when using the other methods.

[Video: V_iw61oU](https://dev.epicgames.com/community/api/cms/videos/V_iw61oU/embed.html)

In addition to controlling quality, post process volumes can control how far light and reflections are able to contribute within the scene. Lvl\_Adventure is relatively small and render distance isn’t an issue. However, for larger areas (such as open-world games where large distances can cause significant resource consumption) settings like **Lumen Scene View Distance** and **Max Trace Render Distance** are useful for balancing scope and performance.

#### Adjust Reflection Quality Using Lumen GI

In this section, you’ll make adjustments to the level’s Global Illuminations and Reflections settings by solving problems in a serious of exercises. As you work, you'll learn about each setting and improve the look of reflections on the wet floor you created in the previous tutorial.

Settings you'll adjust include:

| Setting | Description |
| --- | --- |
| Global Illumination |   |
| **Lumen Scene Lighting Quality** | Calculates scene lighting fidelity. Higher values equal higher fidelity, at a performance cost. |
| **Lumen Scene Detail** | Controls the size of instances that can be represented in a scene. Higher values ensure small objects are represented, at a performance cost. |
| Reflections |   |
| **Quality** | Increases the fidelity of Lumen Reflections on surfaces. Higher values equal higher fidelity and can reduce artifacting, at a performance cost. |
| **Screen Traces** | Toggles screen space traces for Lumen Global Illumination. Turning on Screen Traces improves reflection fidelity, but it only affects what is visible on screen. |
| **Max Roughness To Trace** | Sets the maximum roughness value for which Lumen still traces reflections. |

To follow along, apply these values to `PPV_Room3`:

- **Global Illumination** **Method:** None **Lumen Scene Lighting Quality:** `0.25` **Lumen Scene Detail:** `0.25`
- **Reflections** **Method:** None **Quality:** `0.25` **Screen Traces**: Unchecked **Max Roughness to Trace:** `0.0`

![Image](https://dev.epicgames.com/community/api/documentation/image/c9e9612b-44e0-49be-b705-cd177b1b277b)

To begin the exercises, follow these steps:

1. In the viewport or **Outliner**, locate one of the emissive assets you created in the previous tutorial. Arrange it on the floor as you like. ![Image](https://dev.epicgames.com/community/api/documentation/image/da1c47a6-a886-4c9b-bfb8-dbddea1133f8)
2. In the **Outliner**, select `PPV_Room3`.
3. Navigate to the **Details** panel. To use Lumen GI, expand **Global Illumination**, check **Method**,and select **Lumen**. ![Image](https://dev.epicgames.com/community/api/documentation/image/addc9595-b994-46c7-b4dc-34092a2750e6) Your scene should now look like this: ![Image](https://dev.epicgames.com/community/api/documentation/image/1f007b77-368c-40af-a380-4f9a04acab71)
4. To use Lumen reflections, expand **Reflections**, check **Method,**and select **Lumen**. ![Image](https://dev.epicgames.com/community/api/documentation/image/86b29067-52a9-4139-ab66-16e92697b9b0) Your scene should now look like this: ![Image](https://dev.epicgames.com/community/api/documentation/image/6e1560cd-cd55-438b-b920-c4cc7987bce2)
5. Reflections are more noticeable on materials with low roughness. Since `BP_Floor`’s roughness when wet is 0 (no roughness), set **Max Roughness to Trace** to `1.0`. ![Image](https://dev.epicgames.com/community/api/documentation/image/d24876a0-7489-4c70-8066-313ca29e3cca) Your scene should now looks like this: ![Image](https://dev.epicgames.com/community/api/documentation/image/d56dec14-90c1-4212-8dde-939dfad452ae)
6. Some of the emissive power is lost on the wet floor. To solve this, check **Screen Traces**. ![Image](https://dev.epicgames.com/community/api/documentation/image/0e2307e6-66e1-4b2b-a606-ba83846005e6) Your scene should now look like this: ![Image](https://dev.epicgames.com/community/api/documentation/image/390278d8-60f2-4821-8aad-fa5b534ca5ab)
7. While the amount of reflected light is improved, the reflection itself is not crisp. To improve the clarity of the reflections, increase **Quality** to `1.0`. ![Image](https://dev.epicgames.com/community/api/documentation/image/92659d6c-a0c1-43a3-8131-dc54615bae54) Your scene should now look like this: ![Image](https://dev.epicgames.com/community/api/documentation/image/a5ba5a71-370c-449f-ab5f-9b5f6eb2868f)
8. The clarity of the reflections is improved, but there’s (subtle) visible artifacting behind the arrow. ![Image](https://dev.epicgames.com/community/api/documentation/image/26394748-2c30-4cf4-8150-b7ecc7f1a10b) To resolve the artifacting, you can increase the number of samples produced by Lumen GI. Under **Lumen Global Illumination**, check **Lumen Scene Lighting Quality** and set its value to `1.0`. ![Image](https://dev.epicgames.com/community/api/documentation/image/f0099acb-8307-4d10-bbd1-ce79d9cd45d0)
9. Check **Lumen Scene Detail** and set its value to `1.0`. ![Image](https://dev.epicgames.com/community/api/documentation/image/91f0cb6e-6fe4-429a-a425-b6a990ebdc90) Your final scene should now look like this: ![Image](https://dev.epicgames.com/community/api/documentation/image/15359066-5716-49dd-83c1-6a22857bcbd4)

With these settings, you've used Lumen Global Illuminations and Reflections to control the visual fidelity and performance of Lvl\_Adventure. Explore these settings in your own level and consider where you might want to allocate resources for quality or conserve resources to enhance performance.

## Next Up

In the next tutorial, you’ll learn how to create post-process materials and apply an on-screen effect to indicate damage.

- [Related Document](en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine.md)
