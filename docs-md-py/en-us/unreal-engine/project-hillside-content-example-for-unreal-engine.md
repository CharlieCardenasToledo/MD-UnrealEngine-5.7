# Project Hillside

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/project-hillside-content-example-for-unreal-engine

> Application Version: 5.7

Unreal Engine has been used for years in the production of real-time and offline architectural renderings, but new features like Nanite and Lumen, released in Unreal Engine 5, have tremendously increased the scale and quality of what is possible. Hillside is an architectural visualization sample scene developed in collaboration with Neoscape to showcase the original design of Safdie Architects' **Habitat '67** community in Montréal, Canada. This document gives a brief tour of the project and covers the most important settings and considerations that went into building and rendering such a large ArchViz project.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Like most Architectural visualization projects, Project Hillside is very graphically intensive. To achieve stable frame rates and render the final movie, it is recommended to have a RTX A6000 or at least a RTX 3080 graphics card.",
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

## Setup

To create a project with the Hillside sample, follow these steps:

1. Access the [Hillside sample](https://fab.com/s/c40a1c83a173) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

## Architecture Template

Project Hillside was created using the **Archvis** template in UE5. This template serves as a good starting point for architecture projects because it comes with Datasmith, Movie Render Queue, and other commonly used plugins already enabled, as well as hardware-accelerated raytracing.

## Project Organization

The full Hillside project consists of four different Main Levels and their corresponding Level Sequences. These Levels and sequences were used to create an animation, as well as still imagery, as it would typically be done in the Architectural Visualization world. The goal was to make it as simple as possible with as few custom elements and settings needed.

The four Main Levels are located in the **Content > Hillside > Maps** folder:

- **[1]LV\_Teaser** is an abstract concept animation that demonstrates the use of UE for Motion Graphics using the same elements and tools for traditional visualization animations.
- **[2]LV\_Exterior** contains the original proposal master plan designed for Expo 67, Project Hillside.
- **[3]LV\_Interior** contains Moshe Safdie's interior unit in Habitat 67 as well as a simple photogrammetry mesh of the built Habitat.
- **[4]LV\_Credits** contains logo animations and credits.

The four Main sequences are located in **Content > Hillside > Movies**:

- **[1]LS\_Teaser** is a one-camera animation with choreographed moving meshes, lights, wind, particle systems, and post process effects
- **[2]LS\_Exterior** is a collection of exterior shots, from close-up details to wide vistas of the building in the context of Montreal City. Using Sequencer, we control lighting, mood, set dressing, and lights visibility. This sequence demonstrates the use of Nanite and VSMs for highly detailed, large-scale architecture exteriors.
- **[3]LS\_Interior** is a collection of interior shots demonstrating Lumen's capability to handle complex-geometry interiors and lighting conditions.
- **[4]LS\_Credits** consists of a simple Motion Graphics animation imported into UE using Datasmith.

### Scene Organization

Each shot has its own sequence. This allowed us to control camera animation and settings like aperture depth of field, material functions, specific object visibility, as well as lighting settings per shot when needed. Most post process settings are controlled by one Level-wide post-process volume. However, some shots require a few custom adjustments that are controlled in the camera post-process effects and then override the main post-process volume. For example, the shot below needed the Lumen Scene Distance to be pushed back a little more than the default to make sure the global illumination was visible all the way back into the scene. This way, we only adjusted settings that may have impacted performance or art direction on a per-shot basis.

![Image](https://dev.epicgames.com/community/api/documentation/image/ce1f1fd2-9392-4b6c-8a4a-a7cf7cfe0850)

_Example sequence inside Sequencer. Click the image for full size._

All shot sequences were then compiled into a **Camera Cut** master sequence where we grouped shots by season: summer, spring, and fall. This allowed us to have a simple, clean structure for editing and for managing VFX like rain, people, and vehicle visibility per shot or groups of shots.

## Rendering the Sequences with Movie Render Queue

The final Hillside video and still images were rendered out of Sequencer using **Movie Render Queue** (MRQ), which offered us a single place to manage and produce all of our linear content creation.

To load sequences in Movie Render Queue, follow these steps:

1. Enable the Movie Render Queue plugin. If you need additional help to complete this task, see [Working with Plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine).
2. Once the plugin is enabled, open it from the main menu by navigating to **Window > Cinematics > Movie Render Queue**.
3. Load any sequence by clicking the **+Render** button and selecting the sequence to load. ![Image](https://dev.epicgames.com/community/api/documentation/image/bd19b130-f733-4579-9578-05ea9ed46bf9)

Once your sequences are loaded into MRQ, you can assign predefined render settings to each sequence. You can also load a previously saved Render Queue. This way, you can modify your default render settings per shot or sequence and retain the custom settings without having to save multiple render settings each time you want to render.

In our example, we saved our default settings to **MRQ\_Hillside\_BaseConfigPreset**, located in **Content > Cinematics**. Just like using one primary post-process volume as a starting point for all look development inside the scene, this base configuration works for 95% of all shots in Hillside. Then, we saved a Render Queue named according to what we wanted to render. For example, if we only wanted to render Stills in Raster mode, we would save that MRQ configuration with a few customization like additional CVars or specific image sizes.

**LV\_Teaser** needs to use more memory resources for virtual shadows because of the complexity of the scene, so we added the CVar `r.Shadow.Virtual.MaxPhysicalPages 12000`. By default, UE uses a value of 4000 for this setting; higher values are contingent on the GPU you have and its available memory.

The project contains saved presets for the Animation, Stills Raster and Stills Path Traced, but these are just starting points for you to see what we did in one location. Using presets lets you easily iterate on settings for different scenes and quality levels (such as Test, Draft, and Final renders).

![Project Hillside cvars](https://dev.epicgames.com/community/api/documentation/image/0f1fb091-a9f8-4072-a4c6-7a87b799bd34)

_List of CVars we used for the base configuration preset in MRQ._

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To learn more about Movie Render Queue and how to use it, refer to the <a href=\"animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue\">Movie Render Queue</a> section of the Unreal Engine documentation.",
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

To render a sequence, once everything is loaded, use one of the following options in the **Movie Render Queue** window:

![Image](https://dev.epicgames.com/community/api/documentation/image/e1cb721d-fc68-4662-8583-a73a5ab57a75)

- Click **Render (Local)**, if you want to render while the engine is running
- Click **Render (Remote)** if you want to open a headless instance of the engine to run the rendering job. This option can be useful when using a GPU that may not have enough VRAM to handle the engine being open at the same time.

## Rendering the Stills with MRQ

All still camera level sequences were created with the [Still Image](https://dev.epicgames.com/documentation/en-us/unreal-engine/render-multiple-camera-angle-stills-in-unreal-engine), which is located in **Engine > Plugins > MovieRender Queue Content > Editor > Stills**. Once you have your cameras placed, you can run this widget and it will automatically generate the appropriate sequences for you to batch-render images. For each sequence, you can also customize visibility of Actors for set dressing, change lighting, edit environment characteristics like fog and post-process settings, and so on.

![Image](https://dev.epicgames.com/community/api/documentation/image/96951482-d227-4778-ac61-cb5c7a7ef995)

Just like with animation sequences, all you have to do is load these into the MRQ, make sure you are using the correct render presets located in **Content > Cinematics** for either Raster or Path Tracer, and click **Render**. You can find all the still sequences we rendered in **Content > Hillside > Renders**.

For very high-resolution images, you can use the [High Resolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-render-settings-and-formats-in-unreal-engine#settings) feature in MRQ, which divides the image in smaller chunks to save memory. Our **MRQ\_Hillside\_Ext\_StillRaster** preset uses 2 tiles to safely accommodate a 6000x6000 render without running out of VRAM on our target GPU.

## Lumen vs. PathTracer

One of the great advantages of Lumen is speed and accuracy. We included a few path-traced images in the project where all materials, lighting and camera settings are the same, but we switched rendering from Raster to PathTraced in MRQ to see the difference. You must decide how you render your images, as this is heavily dependent on hardware and scene complexity. We chose raster rendering for the entirety of this project because it allows for much faster rendering and still reaches a very high fidelity.

Below, you can see an outdoor shot rendered with Path Tracer and Lumen:

```json
{
  "type": "comparison_slider",
  "image_left_id": 26056004,
  "caption_left": "Path Tracer",
  "image_right_id": 26056005,
  "caption_right": "Lumen",
  "image_left": {
    "id": 26056004,
    "file_name": "ext-path-tracer.jpeg",
    "file_size": 4032424,
    "content_type": "image/jpeg",
    "created_at": "2025-09-11T18:41:20.909+00:00",
    "height": 4000,
    "width": 4000,
    "storage_key": "0e1efb4d-7375-4037-8c8e-cb640b8e6d88",
    "context": "documentation"
  },
  "image_right": {
    "id": 26056005,
    "file_name": "ext-lumen.jpeg",
    "file_size": 6696414,
    "content_type": "image/jpeg",
    "created_at": "2025-09-11T18:41:21.300+00:00",
    "height": 6000,
    "width": 6000,
    "storage_key": "3da37314-c9ff-41df-9219-cd6cd3b8132a",
    "context": "documentation"
  },
  "image_left_storage_key": "0e1efb4d-7375-4037-8c8e-cb640b8e6d88",
  "image_right_storage_key": "3da37314-c9ff-41df-9219-cd6cd3b8132a",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

Here's a comparison between indoor shots rendered with Path Tracer and Lumen as well:

```json
{
  "type": "comparison_slider",
  "image_left_id": 26056006,
  "caption_left": "Path Tracer",
  "image_right_id": 26056007,
  "caption_right": "Lumen",
  "image_left": {
    "id": 26056006,
    "file_name": "int-path-tracer.jpeg",
    "file_size": 1270645,
    "content_type": "image/jpeg",
    "created_at": "2025-09-11T18:41:21.626+00:00",
    "height": 3000,
    "width": 2400,
    "storage_key": "8be626b8-be03-4678-983b-44b4690ebcc3",
    "context": "documentation"
  },
  "image_right": {
    "id": 26056007,
    "file_name": "int-lumen.jpeg",
    "file_size": 1613267,
    "content_type": "image/jpeg",
    "created_at": "2025-09-11T18:41:21.894+00:00",
    "height": 3735,
    "width": 2992,
    "storage_key": "36a4c72e-3ba0-4a04-888b-143279c1563d",
    "context": "documentation"
  },
  "image_left_storage_key": "8be626b8-be03-4678-983b-44b4690ebcc3",
  "image_right_storage_key": "36a4c72e-3ba0-4a04-888b-143279c1563d",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

## Lighting and Level Management

### Sublevels

The Hillside video includes several different lighting and weather scenarios through various seasons and times of day. To better control these conditions and toggle between them, we created a simple default lighting Level that contains a [Sun and Sky](https://dev.epicgames.com/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine), [Volumetric Clouds](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-fog-in-unreal-engine), and [Exponential Height Fog](https://dev.epicgames.com/documentation/en-us/unreal-engine/exponential-height-fog-in-unreal-engine). From this default Level, we created copies with different times of day, color, intensities, cloud, and fog variations that could be loaded and controlled in the main Level.

All the lighting sublevels are present in the **LV\_Exterior** persistent Level, but only one is made visible at any time via the Levels panel or in Sequencer. Theoretically, you could manage all the lighting and lookdev on the individual Actors directly inside Sequencer, but using sublevels lets you reuse conditions multiple times instead of recreating them per-shot.

![Image](https://dev.epicgames.com/community/api/documentation/image/0af07946-8ab8-40d8-9561-799abf731946)

_Lighting Levels visibility. Note that only one is visible, and the other ones are hidden. Click the image for full size._

Lumen only supports 256 lights at once (unlike the Path Tracer), and we had a large number of artificial light sources like street lamps visible in the night shots. To overcome that limitation, we divided all artificial lighting into localized groups that could be loaded from Sequencer per-shot, in the same way we loaded and unloaded different environment lighting conditions.

![Image](https://dev.epicgames.com/community/api/documentation/image/ce4ff46d-b0fd-498c-916e-9f42a3ed56c9)

_Night lights visibility. Click the image for full size._

### Level Instances

We made heavy use of [Level Instances](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-instancing-in-unreal-engine) to separate the project into its different components. This allowed for multiple artists to work on their respective models or tasks without blocking source control access to the Main Level, where the look development was being worked on.

Below is an example of the structure of all of these Level instances and how we grouped them.

Another advantage of this workflow is that you can quickly modify or adjust your Level instances by clicking the **Edit** button, or directly go to the Level and open it to adjust without dealing with the visual noise of the Main Level.

Each Level contains ISMs and / or HISMs, as outlined below, that minimize the draw calls and increase performance.

```json
{
  "type": "sequence_slider",
  "caption": "Use the slider to navigate between images.",
  "images": [
    {
      "image_id": 26056012,
      "storage_key": "b90b701d-a955-4d88-9bcd-4bf718e4ce82",
      "context": "documentation",
      "image": {
        "id": 26056012,
        "file_name": "ue5_2-level-instancing-1.png",
        "file_size": 2821749,
        "content_type": "image/png",
        "created_at": "2025-09-11T18:41:22.950+00:00",
        "height": 1022,
        "width": 2048,
        "storage_key": "b90b701d-a955-4d88-9bcd-4bf718e4ce82",
        "context": "documentation"
      }
    },
    {
      "image_id": 26056013,
      "storage_key": "cb9d8c3d-d9f4-46ff-8462-ed2d49cdd808",
      "context": "documentation",
      "image": {
        "id": 26056013,
        "file_name": "ue5_2-level-instancing-2.png",
        "file_size": 1662515,
        "content_type": "image/png",
        "created_at": "2025-09-11T18:41:23.264+00:00",
        "height": 1028,
        "width": 2048,
        "storage_key": "cb9d8c3d-d9f4-46ff-8462-ed2d49cdd808",
        "context": "documentation"
      }
    },
    {
      "image_id": 26056014,
      "storage_key": "a80bf19d-0529-4007-af0c-330ccebd1002",
      "context": "documentation",
      "image": {
        "id": 26056014,
        "file_name": "ue5_2-level-instancing-3.png",
        "file_size": 848759,
        "content_type": "image/png",
        "created_at": "2025-09-11T18:41:23.459+00:00",
        "height": 1020,
        "width": 2048,
        "storage_key": "a80bf19d-0529-4007-af0c-330ccebd1002",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Working with CAD Data

### Creating and Importing the Model

Safdie Architects designed the Hillside model in Rhino and made efforts to keep grouping, naming, and metadata clean and organized. This allowed for maximum utility and flexibility later down the line, when it came to cleaning up the scene and automating any optimizations or data prep for the final render.

The model was exported from Rhino and imported into Unreal Engine using [Datasmith](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-plugins-for-unreal-engine?application_version=5.5), which kept the whole scene hierarchy intact and brought over all the basic materials and metadata.

The default scene worked fine, but its modular design was composed of tens of thousands of small pieces, like the thousands of windows, each one consisting of several meshes.

To optimize performance, we aimed to reduce the number of draw calls. We built a custom set of scripts that collapsed and condensed the building model into larger chunks that ultimately kept our Content Browser cleaner, the Outliner leaner, and the draw calls reasonably low. The modular pieces we ended up with were further optimized by being converted with another script into Instanced Static Meshes and Hierarchical Instanced Static Meshes to streamline the rendering process as much as possible. Nanite improved things significantly when it comes to draw calls and the cost of rendering meshes. Another benefit of organizing the models this way is optimizing performance for platforms and devices that can only render the fallback meshes.

To push visual fidelity higher, we also did some extra modeling work after optimization was complete. The modular pieces were exported out of the editor and had extra chamfers and details added in 3ds Max that wouldn't be as essential in the original CAD drawings. Modified elements were then reimported in-place.

![Image](https://dev.epicgames.com/community/api/documentation/image/81b84717-aaf2-4641-b249-0305719ecc41)

_The optimization process outlined above reduced this component of the building from 579 Static Meshes to 18. Click the image for full size._

### Editor Scripts

#### Merging and Managing Hierarchy

![Image](https://dev.epicgames.com/community/api/documentation/image/a7cbd816-4147-4bbe-90ab-10f3e9eeffba)

_Hillside Utilities widget_

The **Hillside \_Utilities\_v5** [Editor Utility Widget](https://dev.epicgames.com/documentation/en-us/unreal-engine/editor-utility-widgets-in-unreal-engine), located in **Content > Hillside > Blueprints**, is a custom toolkit developed to speed up the optimization of imported geometry. This tool was designed to work with the Rhino model's "block" paradigm, which uses many nested meshes for every modular piece of the structure. Using this tool improved Outliner organization, as well as performance, by easily collapsing groups and re-instancing the new meshes throughout the scene.

#### HISMs

![Image](https://dev.epicgames.com/community/api/documentation/image/1c0de4ad-f77e-467c-9937-dd0bc2949ad3)

_Mesh to HISM tool_

The **Mesh to HISM** tool is a multi-purpose custom Editor Utility Widget created to manage large amounts of Static Mesh Instances in Hillside. A selection of Static Meshes can be automatically compacted into instance components (ISM or HISM) to reduce Editor overhead and increase rendering performance.

We used the SubObject Data Subsystem to handle dynamically creating and modifying Actor components in-editor. On top of the Instancing tool, we added a couple of handy buttons to fix negative scaling on all selected Actors, and to randomly set rotation and scale as necessary to add a natural look and variation to foliage and set dressing. Additionally, we added functionality to split Static Mesh assets for Nanite by separating triangles with Opaque or Masked materials from triangles with Translucent materials, which are not supported by Nanite.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26056008,
  "caption_left": "Before using the Mesh to HISM tool",
  "image_right_id": 26056009,
  "caption_right": "After using the Mesh to HISM tool",
  "image_left": {
    "id": 26056008,
    "file_name": "uw5_2-mesh-to-hism-1.png",
    "file_size": 1301602,
    "content_type": "image/png",
    "created_at": "2025-09-11T18:41:22.116+00:00",
    "height": 604,
    "width": 2048,
    "storage_key": "78f77f7d-9a11-432b-81d7-1f0fef4a7eb0",
    "context": "documentation"
  },
  "image_right": {
    "id": 26056009,
    "file_name": "ue5_2-mesh-to-hism-2.png",
    "file_size": 1312936,
    "content_type": "image/png",
    "created_at": "2025-09-11T18:41:22.309+00:00",
    "height": 628,
    "width": 2048,
    "storage_key": "c60eea4d-4aad-4aba-85d9-bcbb9ffa0a4f",
    "context": "documentation"
  },
  "image_left_storage_key": "78f77f7d-9a11-432b-81d7-1f0fef4a7eb0",
  "image_right_storage_key": "c60eea4d-4aad-4aba-85d9-bcbb9ffa0a4f",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

## Rendering Optimization

### Nanite Optimizations

Every eligible Static Mesh in the project had Nanite enabled except Water Bodies, the Landscape, and surfaces with translucent materials. Even if individual Assets didn't have a high poly count or number of materials, Nanite's clustered rendering approach and its tight support for Virtual Shadow Maps and Lumen improved performance across the board.

![Image](https://dev.epicgames.com/community/api/documentation/image/c7f434dd-58c7-45fb-b4e5-fa1019eca603)

_View Mode for Inspection - Nanite Visualization | Mask; Green = Nanite, Red = Non-Nanite_

### Nanite + World Position Offset (WPO)

The foliage Assets throughout Hillside use WPO in their materials in order to blow in the wind and give life to the scene. To optimize performance for both Nanite and VSMs, careful attention was given to the way WPO was used in the scene.

The console variable `r.OptimizedWPO=1` was enabled and stored inside the `DefaultEngine.ini` config file. This allowed us to shut off WPO evaluation for Nanite meshes that didn't have the Evaluate World Position Offset option enabled in their Details panel. The foliage had this turned off to save performance in the editor.

For the final movie render, the `OptimizedWPO` variable was disabled in Movie Render Queue to let the windy WPO effect show up in the foliage. Additionally, the foliage Assets were given reasonable culling distances for their WPO evaluation using `World Position Offset Disable Distance` so that only those closest to the camera would use this effect.

![Image](https://dev.epicgames.com/community/api/documentation/image/8f4513dc-aa6f-40f2-b763-799973fece1b)

_View Mode for Inspection - Nanite Visualization | Evaluate WPO ; Red = WPO Off | Green = WPO On_

### Actor Mobility and VSM

All Static Mesh Actors had their mobility carefully set based on their function in the project to avoid [VSM Invalidation](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine?application_version=5.5#caching). Virtually everything was set to Static.

#### Scalability Settings

Like any project, achieving maximum quality and solid performance was a balancing act in Hillside. The targeted output was primarily a linear video, but developers still needed to comfortably navigate the scene. Carefully controlling the render settings also opened up new possibilities for alternative outputs.

Below are some of the tweaks we made to the DefaultScalability.ini file for the project that helped us achieve up to 30 FPS on our target machines.

**Foliage Cull Distance** (`foliage.CullDistanceScale)` acts as a multiplier upon the Min/Max Culling Distances set on Foliage Type assets. We had quite a lot of grass and foliage in the project that was only worth fully rendering during the final cinematic, so we adjusted this variable as needed:

- Low - `foliage.CullDistanceScale=0.05`
- Medium - `foliage.CullDistanceScale=0.2`
- High - `foliage.CullDistanceScale=0.3`
- Epic - `foliage.CullDistanceScale=0.5`
- Cinematic - `foliage.CullDistanceScale=1.0`

These foliage instances also incurred a high cost on Shadow Depths, so we decreased the **Virtual Shadow Map Resolution** on the Epic scalability level:

- Original: `r.Shadow.Virtual.ResolutionLodBiasDirectional=-1.5`
- Hillside: `r.Shadow.Virtual.ResolutionLodBiasDirectional=-0.5`

The cost of rendering each frame depended heavily on the screen resolution, especially when it came to Lumen GI and Lumen Reflections. To optimize performance, we decided to reduce the default screen percentage values and rely on [Temporal Super Resolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine) to make up for any loss in image quality.

- Original - `PerfIndexValues_ResolutionQuality="50 71 87 100 100"` Low - 50% Medium - 71% High - 87% Epic - 100% Cinematic - 100%
- Hillside - `PerfIndexValues_ResolutionQuality="50 60 68 75 100"` Low - 50% Medium - 60% High - 68% Epic - 75% Cinematic - 100%

We also added Material Quality Switches in all the main materials, disabling expensive features based on the chosen scalability level.

![Image](https://dev.epicgames.com/community/api/documentation/image/d044afa5-15ec-43d2-b996-273f78bdaf4d)

## Advanced Material Techniques

#### Volumetric Clouds

To create beautiful and believable skies for the huge variety of different seasons, times-of-day, and camera angles, we made major improvements to the standard material used in the [Volumetric Clouds](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine). No HDRIs were used for the sky.

![Image](https://dev.epicgames.com/community/api/documentation/image/7d811497-695f-40ae-ba0f-b638ad914b1d)

The custom Volumetric Cloud material provides easily art-directable settings for 4 different layers of clouds through a packed texture map (R = Stratocumulus, G = Altostratus, B = Cirrostratus, and A = Nimbostratus). There are simple parameters for **WindVector**, **Stormy**, and many other options for rotating the whole sky, masking out areas, and fine-tuning coverage. You can even enable lightning in the clouds for stormy weather. It also leverages the **Hillside\_MaterialParameters** 0[Material Parameter Collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-material-parameter-collections-in-unreal-engine), which allows the sky and other materials to be globally modified together across different shots.

This material can be migrated to your own project and customized. You can find it under **Content** > **Hillside** > **Effects** > **Clouds** > **Materials** > **M\_VolumetricCloud\_Hillside**.

[Video: V_siJN9O](https://dev.epicgames.com/community/api/cms/videos/V_siJN9O/embed.html)

*Easily set the overall scale of the layout texture in world units.*

[Video: V_rbjaNw](https://dev.epicgames.com/community/api/cms/videos/V_rbjaNw/embed.html)

*Coverage and density affecting the volume shader.*

#### Wooden deck flooring with Parallax Occlusion Mapping

The material used for the outdoor decks creates natural variations in all the wooden planks with a pseudorandom mask generation technique and a random value per instanced static mesh. Using both alleviates the tiling repetition when used to drive tinting, hue shift, saturation, and other effects per plank and per instance.

[Video: V_e09ZfJ](https://dev.epicgames.com/community/api/cms/videos/V_e09ZfJ/embed.html)

It also uses Parallax Occlusion Mapping (POM) to give extra depth and occlusion between planks. Layers of dirt, grime, puddles, and leaves help finalize the desired look.

![Image](https://dev.epicgames.com/community/api/documentation/image/7036aa10-ed81-4c02-8376-970fc1a8c65e)

#### Concrete

Habitat 67 is made of a lot of concrete, so we made special efforts to create a versatile concrete shader. We used triplanarUVs and a custom texture bombing material function to project from all angles and control tilling. Per Instance Random was used to inject variation in color and roughness, and the project contains a multitude of features that can be enabled to get the desired look, depending on the circumstances. Walls can have drips and dirt, wetness and algae can appear near shorelines, pebbles can be added on top of balconies, there are cracks, micro details, fallen leaves, etc.

![Image](https://dev.epicgames.com/community/api/documentation/image/e3b73171-bb59-4cca-9126-0417e22fe8d4)

![Image](https://dev.epicgames.com/community/api/documentation/image/05af813c-1d52-4e05-a6b7-0788f243915a)

_Shoreline feature which add algae, drips and cracks around water line. Click the image for full size._

#### Grass

To support large fields of grass, we used a texture bombing technique to avoid tiling. Micro and macro variation, along with debris and fallen leaves, adds richness and further breaks down tilling. Careful variation in specular and roughness also adds realism, and the roughness maps leverage texture compositing to modulate their intensity over distance. We also used a fuzz technique to attenuate contrast at grazing angles.

![Image](https://dev.epicgames.com/community/api/documentation/image/222ce6c5-3f23-4fa3-94ad-f54cc407b983)

To blend grass with tree mulches, we used a height blend technique which carefully blends between blades of grass and dirt. We created a mask using distance fields which drives the final blend and adds variation for each mulch. Adding leaves on top completes the illusion.

![Image](https://dev.epicgames.com/community/api/documentation/image/112d5318-a1cd-4f21-b0c2-7db4ee3f8edc)

#### Weather Manager System

![Image](https://dev.epicgames.com/community/api/documentation/image/7112822b-f7f0-4676-b705-463876a3ff40)

The weather and seasonal effects in Hillside are spread across many different materials and systems, so we created a custom [Editor Utility](https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints) to manage it all from one place. To open this utility, double-click the **WeatherControl\_Editor** Blueprint in **Content > Hillside > WeatherManager**.

To use this Blueprint, you need to add it to the **LV\_Exterior** Level. Parameters can be edited directly from its **Details** panel in the editor, or you can preview settings in play-in-Editor (PIE) with a custom widget that it creates.

The WeatherControl\_Editor Blueprint uses the following parameters:

- **Autumn scale**: Update the colors and add falling leaves particle systems on the nearest leafy trees (PIE-only for the falling leaves particle system).
- **Cloud Parameters**: Update the visual aspects of the cloud with multiple controls.
- **Wet Surface Scale**: Update the wetness on some surfaces (Asphalt, Concrete).
- **Sun Sky (time of day)**: Update time of day, month, day, solar time.
- **Interior Mapping**: Toggle Windows Interior Mapping.
- **Enable Wind**: Toggle wind in foliage materials (can affect real-time performance).

#### Rain on Windows

For the rain, we used a technique that procedurally generates rain trickles and water drops in a render target for use inside the glass material. This allowed us to tweak the rain as we saw fit, with more or fewer rain trickles and merging droplets of water. We added refraction on water drops, which creates an upside-down effect to achieve a more believable look.

![Image](https://dev.epicgames.com/community/api/documentation/image/edcc47f7-0c17-497f-b205-d3f07a1f1782)

#### Water Pond and Pools

Using the [Single Layer Water](https://dev.epicgames.com/documentation/en-us/unreal-engine/single-layer-water-shading-model-in-unreal-engine) shading model hides the complexity of calculating absorption, scattering and anisotropy, so we could easily create photorealistic water. Along with absorption and scattering, our material supports wind gusts, refraction, floating leaves, and caustics.

![Image](https://dev.epicgames.com/community/api/documentation/image/51e23563-f57d-4b9b-9a18-ea844fdfb58d)

Since UE5.1, the Single Layer Water shading model supports path tracing.

![Image](https://dev.epicgames.com/community/api/documentation/image/ef091d95-300d-47fd-9844-25f088a624c0)

#### River

We used the [Water plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/water-system-in-unreal-engine) to create the St. Lawrence River. Starting from a river material as a base, we made a custom shader with a small set of Gerstner waves and several artist-friendly parameters. One big spline-based Water Body defined the main river area and general flow, and additional spline-based Water Bodies were placed around the island to define different flow directions, flow speed, and material variations where required.

![Image](https://dev.epicgames.com/community/api/documentation/image/ff0d83dc-7b49-44ff-a91f-cf8b14fef0bb)

##### Affecting flow with splines

We used a small [Runtime Virtual Texture](https://dev.epicgames.com/documentation/en-us/unreal-engine/runtime-virtual-texturing-in-unreal-engine) to capture the depth of the water bodies so we could quickly iterate on the map to drive wave amplitudes, using primitives to fake depth without affecting the actual depth of the landscape. This creates the illusion of calmer water around piers and more windy or upset water in the center of the river. Foam around the shoreline was also added using Distance Field techniques.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To render water with WPO in path tracing, you need to enable Water on Ray Tracing by setting <code>r.RayTracing.Geometry.Water 1</code>.",
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

#### Rocks and Shoreline

To give the illusion of wetness on the shoreline, we created a wet rock material with a world space blend which supports three states: dry, wet, and algae. We could then specify a shoreline height and blend falloff to get the desired look.

![Image](https://dev.epicgames.com/community/api/documentation/image/1c4dc903-f81a-4ca8-8468-7287330c1702)

#### Fake Interiors

We took the cubemap interior material from the [City Sample buildings](https://www.fab.com/listings/008fe959-5511-428e-93bd-f99b1179f6d5) and simplified it just enough for Hillside's needs. In order to have the necessary interior rooms and furniture style fit for Hillside, we used a custom system made with Blueprints to capture cubemaps of individual 3D rooms, then added the color and depth of the furnishings as an extra layer. We used assets and materials [migrated from Twinmotion](https://www.fab.com/listings/47cd28b9-3a16-43c7-9592-ee51ce48d0dd).

[Video: V_cJvx4N](https://dev.epicgames.com/community/api/cms/videos/V_cJvx4N/embed.html)

The resulting maps were added to a texture array file, and rooms and furnishings were mixed randomly in the window material by the use of the **Per Instance Random** node. This allowed us to add more variants to the array and a huge variety of randomness across all parameters, like lighting accents, blinds, curtains, light intensity, temperature and more.

Even the 90-degree corner windows were fake interiors. This was achieved by taking black and white masks captured using the cubemap capture tool, and setting them up in a separate material instance affecting only the room cubemaps, but not the prop maps.

![Image](https://dev.epicgames.com/community/api/documentation/image/83ee395a-9f46-43da-acb7-dc83e1f58aa8)

## Bringing Life to the Scene

#### High Quality Translucent Reflections

There is plenty of glass and water in Hillside, so getting good looking reflections on those surfaces was imperative. In the PostProcessVolume, we enabled **High Quality Translucent Reflections** in the Lumen settings.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26056010,
  "caption_left": "Default Reflections",
  "image_right_id": 26056011,
  "caption_right": "High Quality Translucent Reflections",
  "image_left": {
    "id": 26056010,
    "file_name": "reflections-lumen-off.png",
    "file_size": 2188676,
    "content_type": "image/png",
    "created_at": "2025-09-11T18:41:22.528+00:00",
    "height": 653,
    "width": 1283,
    "storage_key": "96d4ffbe-a2b6-4177-a06e-f10f7a552bad",
    "context": "documentation"
  },
  "image_right": {
    "id": 26056011,
    "file_name": "reflections-lumen-on.png",
    "file_size": 2196963,
    "content_type": "image/png",
    "created_at": "2025-09-11T18:41:22.749+00:00",
    "height": 652,
    "width": 1281,
    "storage_key": "2589ed59-a886-45e6-9e23-3b3f64b8233f",
    "context": "documentation"
  },
  "image_left_storage_key": "96d4ffbe-a2b6-4177-a06e-f10f7a552bad",
  "image_right_storage_key": "2589ed59-a886-45e6-9e23-3b3f64b8233f",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

#### Trees and Props

We used existing content from across the Epic ecosystem to populate the world as much as possible. Tree assets were mostly migrated from [Twinmotion](https://www.fab.com/listings/47cd28b9-3a16-43c7-9592-ee51ce48d0dd) and imported from [Quixel](https://quixel.com/blog/2022/10/17/megascans-trees-european-hornbeam-now-available-on-the-unreal-engine-marketplace), various props for interior and exterior scenes were brought over from Twinmotion, and some VFX and all the vehicles were migrated from the [City Sample](https://www.fab.com/listings/4898e707-7855-404b-af0e-a505ee690e68). These assets are organized under the **Content > ExternalAssets** folder.

![Image](https://dev.epicgames.com/community/api/documentation/image/a78750fd-4c7d-43dd-8676-45bbcc85eb36)

Some of the Twinmotion trees were exported from Unreal Engine to 3ds Max to be processed with [Pivot Painter](https://dev.epicgames.com/documentation/en-us/unreal-engine/pivot-painter-tool-2.0-in-unreal-engine), which enabled higher fidelity wind simulations across the hierarchy of tree branches.

![Image](https://dev.epicgames.com/community/api/documentation/image/20ccf231-b097-4288-b066-25e28fd0063e)

![Image](https://dev.epicgames.com/community/api/documentation/image/26ab4455-cb45-45c8-801c-07e7b9e746e3)

#### Niagara VFX

Tech artists added an additional level of realism and cinematic appeal to Hillside by creating various special effects in [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-in-niagara-effects-for-unreal-engine). All the Niagara Systems and accompanying Assets are grouped under **Content > Hillside > Effects**. We've showcased some examples below.

![Image](https://dev.epicgames.com/community/api/documentation/image/833cc4fe-09e4-4ba1-bb2b-7c83f8cb748b)

_Falling Cherry Blossoms made from mesh particles in Niagara._

![Image](https://dev.epicgames.com/community/api/documentation/image/7218cff0-e2c1-47ed-bf13-b4216bec1cdb)

_Coffee Steam real-time fluid sim that uses our Niagara Fluids plugin._

![Image](https://dev.epicgames.com/community/api/documentation/image/9f1c311e-0697-42ad-8bea-5c3f06913b50)

_Bubbler water feature that was simulated in Houdini and imported as a Geometry Cache from an Alembic file._

#### Vehicles

The animated background vehicles throughout the sequence were migrated from the [City Sample](https://www.fab.com/listings/2909157b-ddfa-4cef-a925-69dc2467021f) project and reduced to simpler Blueprints and fewer meshes. To populate the roads and have the vehicles drive automatically, a custom Blueprint called **BP\_SimpleTrafficGenerator** was created that spawns vehicle Actors along a given spline at a given density. The vehicles drive along the spline during Play or Simulate with a custom Actor component called **FollowSplineComponent**.

![Image](https://dev.epicgames.com/community/api/documentation/image/e036a7b8-9d14-440a-83c7-5e0b6bba208a)

Because the vehicles only drive themselves during Play, it wasn't easy to preview or fine-tune their animations inside Sequencer. To bake out an animation sequence that could be scrubbed and manipulated easily shot-by-shot, we used [Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine) to capture about 20 seconds of driving gameplay for the ~100 vehicles and embed it as a [Subsequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-subscequences-track-in-unreal-engine).

![Image](https://dev.epicgames.com/community/api/documentation/image/c1974438-10ae-4383-b8b6-3aa50bb4bfe4)

#### Far Distance Effects

For additional atmosphere and lighting controls, we used a simple card to fake distant fog and the glow of city lights.

![Image](https://dev.epicgames.com/community/api/documentation/image/a8b0bcf4-bcfd-4084-886e-d4be2978a9fb)

The window lighting on distant buildings at night time is a material migrated from the City Sample.

In order to make sure that reflections of distant objects remained accurate and distant parts of the buildings received high quality shadows, we added `r.RayTracing.Culling.Radius 80000` to the `DefaultEngine.ini` file, which increases the reflection distance from the default of 30,000 cm.

## Learn More

- [Exploring Hillside: a virtual Habitat 67](https://www.unrealengine.com/en-US/hillside)
- [Unpacked: Hillside](https://dev.epicgames.com/community/learning/courses/ZMz/unreal-engine-hillside-sample-project-unpacked/lEKe/unreal-engine-hillside-sample-project-unpacked-overview)
