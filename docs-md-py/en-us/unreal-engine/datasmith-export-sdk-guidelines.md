# Datasmith Export SDK Guidelines

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-export-sdk-guidelines

> Application Version: 5.7

## Target Audience for this Guide

This guide is aimed at 3D application developers who want to export scenes from third-party design applications into Unreal Engine using the Datasmith framework.

This guide makes the following assumptions:

- You are an experienced C++ programmer.
- You are familiar with the development of 3D applications.
- You are developing functionality to export models from a third-party 3D application to Unreal Engine or Twinmotion.
- You are not familiar with how Unreal Engine works, but you are willing to learn about it.

## What You Will Learn

This page outlines a series of guidelines and best practices for exporting 3D models from other design applications to Unreal Engine using the Datasmith SDK. Broadly speaking, it outlines:

- Datasmith's design philosophy.
- Data models and structures in Unreal Engine.
- UX guidelines for Datasmith exporters, with separate checklists for each major part of the export process.
- Useful API calls and code examples for different scenarios.

## Downloads and Prerequisites

This section contains:

- A list of required downloads and where to find them.
- An overview of the required Datasmith and Unreal Engine knowledge to get you started, and links to resources for further learning.

### Downloading Unreal Engine and the Datasmith SDK

If you download and build Unreal Engine from the [Unreal Engine GitHub repository](https://github.com/EpicGames/UnrealEngine), the Datasmith SDK is included with it.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To download the Unreal Engine source code from GitHub, you must first follow the steps outlined in <a href=\"https://www.unrealengine.com/en-US/ue4-on-github\">this guide</a> to request access to the repository. If you haven't been granted access, you will receive a 404 error.",
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

After you download the Unreal Engine source code, you will find the Datasmith SDK under:

`\Engine\Source\Programs\Enterprise\Datasmith\DatasmithSDK\`

The `Documentation` folder contains a sample project, as well as instructions on how to get your development environment configured.

If you download and install Unreal Engine from the [Epic Games launcher](https://www.unrealengine.com/en-US/download/ue_non_games), you must download the Datasmith SDK separately from [this folder](https://github.com/EpicGames/UnrealEngine/tree/release/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSDK) in the Unreal Engine GitHub repository.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Epic Games have developed Datasmith export plugins for a few design applications, such as Revit, SketchUp, and 3ds Max. You can refer to these plugins as examples for your own work.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can access the source code for these Datasmith export plugins in the Epic Games GitHub repository, under:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<code>\\Engine\\Source\\Programs\\Enterprise\\Datasmith\\</code>",
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

### Understanding Datasmith

Datasmith is a collection of tools and plugins that brings pre-constructed scenes created in a variety of design applications into Unreal Engine. It was designed to overcome limitations of other generic file formats, such as FBX or OBJ.

Datasmith is able to:

- Handle large meshes.
- Store data that Unreal Engine uses, such as: LODs Collision Lights Object hierarchy Metadata
- Reformat texture files (to the power of 2, into formats handled by Unreal).

To learn more about Datasmith features and functionality, refer to the [Datasmith Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-plugins-overview) page.

Exporting data happens in two steps:

1. Parse the design application and construct a **DatasmithScene** with the **DatasmithCore** API.
2. Export the scene to disk using the **DatasmithExporter** API.

To learn how to use these APIs, refer to the following documentation:

- [DatasmithCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore?application_version=5.5)
- [DatasmithExporter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Developer/DatasmithExporter?application_version=5.5)

### Unreal Engine Data Model

Before you start writing your Datasmith exporter, familiarize yourself with how Unreal Engine stores and structures information.

Unreal Engine works with projects. An Unreal project contains at least one [Level](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-in-unreal-engine), which contains one or more [Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine). Actors have a position, rotation, and scale. They can exist on different layers, be shown or hidden, have animations, and so on.

Each Actor has one or more [Components](https://dev.epicgames.com/documentation/en-us/unreal-engine/basic-components-in-unreal-engine), which can be:

- Geometric Assets, such as [Static Meshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine).
- [Lights](https://dev.epicgames.com/documentation/en-us/unreal-engine/point-lights-in-unreal-engine).
- [Cameras](https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-actors-in-unreal-engine), and so on.

Static Meshes reference [Master Materials or Material Instances](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine). In turns, Material Assets reference [Texture Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/textures-in-unreal-engine).

A single Static Mesh can be referenced by multiple Actors. This is called geometry instantiation.

![Unreal Engine data structure](https://dev.epicgames.com/community/api/documentation/image/cb8b26a5-7e3c-46af-860a-a1e3fd8eefac)

_This diagram illustrates the relationship between Actors, Components, and various types of Assets in Unreal Engine. Click the image for full size._

## Datasmith Design Principles

As a plugin developer, you should strive to ensure a consistent user experience, regardless of which software the data is being exported from. As such, it is important to understand and adhere to the Datasmith design principles outlined below. These are the principles that we (the Datasmith developer team) use when developing our own plugins.

### Datasmith Plugin Types

All Datasmith plugins use one of the following two schemes:

- Exporter / Importer combination. For example, 3ds Max, Revit, and Sketchup use: A Datasmith exporter plugin on the software side. The Datasmith File Importer plugin on the Unreal Engine side.
- Direct importer. For example, Unreal Engine can import some file formats native to Rhino, Solidworks, and Cinema4D.

![Datasmith import workflows](https://dev.epicgames.com/community/api/documentation/image/206d6e6e-f7d6-4c4a-a980-c0b3fb15a381)

_This diagram illustrates the various Datasmith import workflows available. Click the image for full size._

The choice of which workflow to use varies on a case-by-case basis.

### Export and Import Logic

One of the challenges with exchanging data between different applications is understanding where to put some of the logic. When we translate data from one application to another, we may ask ourselves:

- Should we export everything or provide options to exclude some entities?
- Should we exclude small objects when exporting? How do we define "small"?
- Should we reduce polygon count when exporting? Should we reduce texture resolutions?
- Where do we rescale entities to match units and scale?, and so on.

Generally speaking, our approach is to export everything in a granular fashion (that is, object by object), and deal with object merging, polygon reduction and other data preparation operations when the data is later imported into Unreal Engine or Twinmotion.

While there's no strict rule, our general approach is that it's best to have the least amount of options (or none at all) exposed in the Datasmith exporter, and let the Unreal Engine user make most of the decisions during the import.

With this approach, it is up to the Unreal or Twinmotion user to decide how granular their data may be, or how optimized it may be. Unreal Engine's [Dataprep](https://dev.epicgames.com/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine) is a great tool for making those decisions.

![Internal operations on the design application side are typically hidden to users. Data organization and optimization options are typically exposed.](https://dev.epicgames.com/community/api/documentation/image/52f3b65a-82d7-46dd-bb38-2ccdd1fa1f9f)

_Example division between internal and user-selected operations over the course of the Datasmith export / import process. Click the image for full size._

### Reimporting Data After Source Changes

Datasmith brings design data from a variety of source applications into Unreal Engine, typically for the purpose of building real-time visualizations and experiences around that data. Often, while you are working on building those visualizations and experiences in Unreal Engine, the scene or design data that your work incorporates needs to change in order to meet new requirements or incorporate feedback from stakeholders.

To avoid painful and costly re-work, you need to be able to incorporate those upstream changes without losing all the work you've done in the Unreal Editor. To this end, Datasmith offers a [re-import workflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-reimport-workflow-in-unreal-engine) that preserves all of your changes within the Unreal project.

From a Datasmith SDK perspective, re-importing data implies two things:

1. Entities must have a persistent unique identifier. Relying on an object's name is not a good strategy because multiple objects can have the same name.
2. Entities must be saved with a hash value that permits data re-importing at the highest possible performance. When a Datasmith entity is created, a unique number is generated based on the object's data. For example, to quickly determine if two meshes are identical, you could either compare them face-to-face using a time-consuming algorithm, or you could compute a numerical value based on the number of vertices, faces, and UVs. Comparing these two values would then be a much faster way to tell if the meshes are identical or not.

Examples are described further down on this page.

### Environment and Lighting

Although you may be tempted to perceive Unreal as a rendering engine and expect to export a model with all of its environment settings (cameras, environments, backgrounds, etc.), we find that generally, those artistic decisions are best made by Unreal Engine or Twinmotion users, after the data has been imported into the engine.

The most important aspect is to import model elements (geometry, materials, lights, metadata). Once the data has been imported into Unreal Engine or Twinmotion, users can change materials, tweak lighting, and perform other artistic tasks.

## UX Guidelines for Datasmith Exporters

If you made it to this point, you have most likely compiled Unreal and created your first Datasmith file with a small application. Congratulations!

Now it's time to look at UX considerations related to how the data should be structured for end users.

### Exporter UI

As we described in the Datasmith Design Principles section above, we want to offer the least amount of options when exporting to Datasmith. Here are some examples:

|   |   |
| --- | --- |
| ![3D export view in Revit](https://dev.epicgames.com/community/api/documentation/image/89eeef51-e7cc-4436-b6c9-2160e6005aad) | ![Datasmith export options in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/b61eb7ed-eedc-45d9-a4f6-6defc79a3b08) |
| Datasmith exporter from Revit | Export Options dialog in Unreal Engine |

#### Guidelines

- Favor WYSIWYG (What You See Is What You Get) exports by relying on the application's viewing and filtering capabilities. For example, Revit only exports what is visible in the active View, and SketchUp only exports what is visible on-screen. There is no reason to invent a whole new UX to select and filter entities to be exported.
- Favor no options at all when exporting.
- If you must expose options, keep them as simple as possible. Refer to the 3ds Max exporter above as an example.

#### To Be Avoided

Options related to data preparation and optimizations, such as geometry detail, object type filtering, UV channels, etc. These should be decisions made by the Unreal Engine user, in Unreal Engine.

### Progress Information and Error Messages

Datasmith exporters collect all entities relevant to transferring and reconstructing the scene in Unreal Engine. It is possible that some entities cannot be exported. You should inform users if one or more entities cannot be exported..

In addition, some projects are very large, which can make the export take a long time. Users should be able to see progress information.

Here are some examples. Click any image below to see it in full size.

![Progress information in 3ds Max](https://dev.epicgames.com/community/api/documentation/image/629c3a0e-7eb5-4651-9da9-9bf2f2170931)

_Progress information in 3ds Max._

![Output warnings in the Revit Datasmith Exporter.](https://dev.epicgames.com/community/api/documentation/image/6de9aae5-83ca-42b4-bac7-d333c53bcf30)

_Output warnings in the Revit Datasmith Exporter._

![Output warnings in the 3ds Max Datasmith Exporter.](https://dev.epicgames.com/community/api/documentation/image/d686598f-d620-4a38-8449-ddda9905d264)

_Output warnings in the 3ds Max Datasmith Exporter._

#### Guidelines

- Progress information needs to be presented to the user during export.
- Users need to be able to cancel the Datasmith export process.
- An error message log should be displayed to inform users about unsupported objects, missing textures, and other issues.

#### Useful to Have

Certain users often demand batch processing and scripting. For example, with SketchUp, 3ds Max or Revit, users can batch export to Datasmith using the native application scripting language.

#### To Be Avoided

Do not implement successive modal dialogs (OK / Cancel windows) that interrupt the export process each time an error or a warning occurs.

#### Useful API Calls

- [DatasmithExporter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Developer/DatasmithExporter?application_version=5.5)
- [IDatasmithProgressManager](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Developer/DatasmithExporter/IDatasmithProgressManager?application_version=5.5)
- [FDatasmithLogger](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Developer/DatasmithExporter/FDatasmithLogger?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpExporter.cpp`

### Exported Files and Folders Structure

A Datasmith "file" consists of two parts:

- A `.udatasmith` file that uses an XML data structure.
- A "sidecar folder" (an associated folder) that contains all Assets associated with the `.udatasmith` file.

![Example sidecar folder for an .udatasmith file](https://dev.epicgames.com/community/api/documentation/image/5d3b01a3-b5e5-46e5-ad98-5a0e45a3b1d8)

_Example export file with its associated folder._

#### Must Have

- A single `[filename].udatasmith` file and a single associated [filename]\_Assets folder.
- All related Assets are stored in the [filename]\_Assets folder.
- Assets are referenced in the `.udatasmith` file's XML structure using relative paths.

#### To Be Avoided

- Do not reference Assets by absolute paths.
- Do not create additional folders and subfolders that contain Assets. Here is an example of an incorrect export: ![Incorrect file structure](https://dev.epicgames.com/community/api/documentation/image/8ac013ef-18b0-4016-8209-e0778d99fca7)

### Datasmith File Header

We (Epic Games) use header information to understand where data comes from. Our telemetry only collects statistics about what types of files are imported and from which source.

Below is an example header of a Datasmith file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;DatasmithUnrealScene&gt;\n    \t&lt;Version&gt;0.24&lt;/Version&gt;\n    \t&lt;SDKVersion&gt;4.25&lt;/SDKVersion&gt;\n    \t&lt;Host&gt;Revit&lt;/Host&gt;\n    \t&lt;Application Vendor=&quot;Autodesk Inc.&quot; ProductName=&quot;Revit&quot; ProductVersion=&quot;2018&quot;/&gt;\n    \t&lt;User ID=&quot;1e8adca84ffe2d4d625d54b63fba876d&quot; OS=&quot;Windows 10 (Release 1709)&quot;/&gt;",
  "lines_of_code": 6,
  "id": 150660,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--4eb0ece280e0f765f0a87f0a09a12bd14ded64323aba61430cd23674513d9053",
  "settings": {
    "is_hidden": false
  }
}
```

#### Must Have

Datasmith information must be properly set, similar to the example above.

#### Useful API Calls

- [IDatasmithScene::SetHost](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithScene/SetHost?application_version=5.5)
- [IDatasmithScene::SetProductName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithScene/SetProductName?application_version=5.5)
- [IDatasmithScene::SetProductVersion](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithScene/SetProductVersion?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpExporter.cpp`

### Static Mesh Assets

Static Mesh Assets ([IDatasmithMeshElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMeshElement?application_version=5.5)) define actual geometry, but won't appear in the Unreal or Twinmotion viewport until they are referenced by Actors ([IDatasmithMeshActorElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMeshActorElement?application_version=5.5)). Multiple `IDatasmithMeshActorElement`s in a scene can also point to the same Static Mesh asset.

A Static Mesh Asset holds data for:

- Faces, vertices, normals and smoothing masks
- UVs
- Collisions
- LODs
- Vertex colors
- Material IDs and assignments, etc.

Below is an example data structure for a Static Mesh Asset in a `.udatasmith` file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;StaticMesh name=&quot;c96130816d3eee95f82a6c00e553f491&quot; label=&quot;Walls_Basic_Wall_Exterior_-_Insulation_on_Masonry&quot;&gt;\n      &lt;file path=&quot;rac_advanced_sample_project-3DView-{3D}_Assets/c96130816d3eee95f82a6c00e553f491.udsmesh&quot;/&gt;\n      &lt;Size a=&quot;5922000.0&quot; x=&quot;855.299927&quot; y=&quot;30.300011&quot; z=&quot;1139.999878&quot;/&gt;\n      &lt;LightmapCoordinateIndex value=&quot;-1&quot;/&gt;\n      &lt;LightmapUV value=&quot;-1&quot;/&gt;\n      &lt;Hash value=&quot;c0e8334d671cf30ef8ff8a67aa4da25b&quot;/&gt;\n      &lt;Material id=&quot;9&quot; name=&quot;e72f7720bfd15817d3789377231c9646&quot;/&gt;\n      &lt;Material id=&quot;10&quot; name=&quot;5d261e4bd619e79ebea1cfcc1d1a8d8e&quot;/&gt;\n      &lt;Material id=&quot;11&quot; name=&quot;13b3765549b7832c6bc26e8922497ced&quot;/&gt;\n    &lt;/StaticMesh&gt;",
  "lines_of_code": 10,
  "id": 150661,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--9e53c347646611de9a2344a41c0cd1f4952bbcb3dd0b8c21ddabfb8f15396e40",
  "settings": {
    "is_hidden": false
  }
}
```

#### Must Have

- Static Mesh **names** must be unique and they must not change between successive exports. This is required to track entities for subsequent re-imports. 3D applications usually provide GUIDs that are well-suited for this purpose.
- Static Mesh **labels** must be sanitized, user-readable, and representative of what that object may be.

|   |   |
| --- | --- |
| ![Unique names for mesh Assets](https://dev.epicgames.com/community/api/documentation/image/7f80b955-7434-4eb7-a04a-4ee11cc7bab3) | ![User-readable labels in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/5667faa3-e0ee-43f0-bbab-1a4919fde1eb) |
| Unique names for mesh Assets | User-readable labels in Unreal Engine |

- Static Mesh Assets (`IDatasmithMeshElement`) must be reused across Actors where applicable (they must be instanced).
- Unreal Engine uses [left-handed Z-up](https://www.evl.uic.edu/ralph/508S98/coordinates.html) coordinates and measures dimensions in centimeters, therefore: Conversion must be done on the exporter side. UV texture coordinates must be flipped vertically (on the Y axis) so we don't use a negative scale in material tiling to counteract images being flipped in Unreal Engine. Scale conversion and coordinate transformation must be baked into the Static Mesh rather than applied to the Actor transforms. *Scale is baked in the geometry, resulting in Actor transforms set to a scale of 1.0 (as opposed to 2.54 or 0.333)* Mesh pivots must be calculated in the mesh so they don't all end up at 0, 0, 0. *Left: mesh pivot aligned with object (correct). Right: pivot at 0, 0, 0 (incorrect)* Triangles must be welded so that smoothing masks and shading work correctly. *Smoothing, Normals, and similar, are correctly set on the geometry.*

#### Useful to Have

- Specify additional LODs.
- Specify collision meshes.
- Specify Lightmap UV Channel (Unwrap).

#### To Be Avoided

- Static Mesh names which aren't guaranteed to be unique and repeatable across exports. Do not use object names that are user-specified.
- Do not store units rescaling within Actor transforms.
- Do not leave pivots at 0, 0, 0.
- Do not export thousands of Static Mesh Actors that should be welded together. For example, a *Box* is typically a single mesh with 6 faces, not 6 individual meshes with a single face each.

#### Useful API Calls

- [IDatasmithMeshElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMeshElement?application_version=5.5)
- [FDatasmithMesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithMesh?application_version=5.5)
- [FDatasmithUtils::SanitizeObjectName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithUtils/SanitizeObjectName?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpExporter.cpp`

### Static Mesh Actors

Static Mesh Actors ([IDatasmithMeshActorElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMeshActorElement?application_version=5.5)) don't define the actual geometry. They point to Static Mesh Assets ([IDatasmithMeshElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMeshElement?application_version=5.5)). Note that several `IDatasmithMeshActorElement`s can reference the same Static Mesh.

Below is an example data structure of a Static Mesh Actor in a `.udatasmith` file.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;ActorMesh name=&quot;1&quot; label=&quot;Teapot001&quot; layer=&quot;0&quot;&gt;\n\t    &lt;mesh name=&quot;1&quot;/&gt;\n\t    &lt;Transform tx=&quot;16.825752&quot; ty=&quot;-18.789846&quot; tz=&quot;0.0&quot; sx=&quot;1.0&quot; sy=&quot;1.0&quot; sz=&quot;1.0&quot; qx=&quot;0.0&quot; qy=&quot;0.0&quot; qz=&quot;0.0&quot; qw=&quot;1.0&quot; qhex=&quot;0000008000000000000000800000803F&quot;/&gt;\n\t    &lt;tag value=&quot;Max.superclassof: GeometryClass&quot; /&gt;\n\t    &lt;tag value=&quot;Max.classof: Teapot&quot; /&gt;\n\t    &lt;tag value=&quot;Max.handle: 1&quot; /&gt;\n\t    &lt;tag value=&quot;Max.isGroupHead: false&quot; /&gt;\n\t    &lt;tag value=&quot;Max.isGroupMember: false&quot; /&gt;\n\t    &lt;tag value=&quot;Max.parent.handle: 0&quot; /&gt;\n    &lt;/ActorMesh&gt;\n",
  "lines_of_code": 21,
  "id": 150662,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--365959ea390fc3f9c0a393a4f7301301b54710fe15635141f71fd73c0078112f",
  "settings": {
    "is_hidden": false
  }
}
```

![Two Static Mesh Actors referencing the same Static Mesh Asset (instancing) imported from 3ds Max.](https://dev.epicgames.com/community/api/documentation/image/79b57d58-77e1-4440-afbc-e459dc701ba7)

_Two Static Mesh Actors referencing the same Static Mesh Asset (instancing) imported from 3ds Max._

#### Must Have

- Mesh Actor **names** must be unique and they must not change between successive exports. This is required to track entities for subsequent re-imports.
- Mesh Actor **labels** must be sanitized (that is, they must not contain invalid characters) and user-readable.
- Static Mesh Assets (`IDatasmithMeshElement`) must be reused across Actors where applicable (they must be instanced).
- Scale and coordinate conversions, as well as coordinate transformations, must be baked into the Static Mesh rather than applied to the Actor transforms.

#### Useful to Have

- Layer specification.
- Support for tags and metadata.

#### Useful API Calls

- [FDatasmithSceneFactory::CreateActor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithSceneFactory/CreateActor?application_version=5.5)
- [FDatasmithSceneFactory::CreateMeshActor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithSceneFactory/CreateMeshActor?application_version=5.5)
- [IDatasmithActorElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement?application_version=5.5)
- [IDatasmithMeshActorElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMeshActorElement?application_version=5.5)
- [FDatasmithUtils::SanitizeObjectName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithUtils/SanitizeObjectName?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpComponent.cpp`

### Empty Actors

Empty Actors are Actors that have no Components or Static Meshes attached to them. They are useful to hold metadata or act as a way to represent parts of a hierarchy. There are no strict rules about how or when you should use them. The guidelines below cover some common use examples.

#### Guidelines

Use empty Actors for:

- Representing null objects (for example, 3ds Max helper objects).
- Representing custom origin points (for example, Revit site locations).
- Representing other elements that make the hierarchy more readable (for example, Layers from Rhino, Block origins from Rhino, or Levels from Revit).
- Representing the head of a compound object that has no geometry of its own (for example, Revit curtain walls).

#### Examples

![3ds Max Helper objects translated as Empty Actors](https://dev.epicgames.com/community/api/documentation/image/f4439a1b-1a09-482f-ac2e-709b84137f3b)

_3ds Max Helper objects translated as Empty Actors._

![Empty Actors used to represent invisible elements from Revit](https://dev.epicgames.com/community/api/documentation/image/3db3f1c9-111f-4cdc-bc67-5c02cf7baec9)

_Empty Actors used to represent invisible elements from Revit._

#### Useful API Calls

- [FDatasmithSceneFactory::CreateActor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithSceneFactory/CreateActor?application_version=5.5)
- [FDatasmithSceneFactory::CreateMeshActor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithSceneFactory/CreateMeshActor?application_version=5.5)
- [IDatasmithActorElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement?application_version=5.5)
- [IDatasmithMeshActorElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMeshActorElement?application_version=5.5)
- [FDatasmithUtils::SanitizeObjectName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithUtils/SanitizeObjectName?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpComponent.cpp`

### Actor Hierarchy

Like many other 3D applications, Unreal Engine supports parent / child hierarchies.

Below is an example parent / child relationship in a `.udatasmith` file.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;ActorMesh name=&quot;3&quot; label=&quot;Box001&quot; layer=&quot;0&quot;&gt;\n\t\t    &lt;mesh name=&quot;3&quot;/&gt;\n\t\t    &lt;Transform .../&gt;\n\t\t    &lt;children visible=&quot;true&quot;  selector=&quot;false&quot; selection=&quot;-1&quot;&gt;\n\t\t\t    &lt;ActorMesh name=&quot;5&quot; label=&quot;Box002&quot; layer=&quot;0&quot;&gt;\n\t\t\t\t    &lt;mesh name=&quot;5&quot;/&gt;\n\t\t\t\t    &lt;Transform ...&quot;/&gt;\n\t\t\t\t    &lt;children visible=&quot;true&quot;  selector=&quot;false&quot; selection=&quot;-1&quot;&gt;",
  "lines_of_code": 8,
  "id": 150663,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--4ba0ce7f48694a32bc0979a6203cb02520c7b24b263fb0a39fff9f329da89349",
  "settings": {
    "is_hidden": false
  }
}
```

#### Guidelines

- Use Actor hierarchies to reflect the data model of your application. ![3ds Max hierarchy translated as-is to Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/d644ce89-9897-49f5-be7b-9b8056d18edf)
- Insert additional empty Actors if necessary to store information relevant to your application's data model (for example, Revit Levels are exported as an extra parent Actor). ![Revit Levels added to the hierarchy become a useful way to orient end users](https://dev.epicgames.com/community/api/documentation/image/28354b32-e0c1-4630-9bd3-3a3e36c41840)

#### To Be Avoided

To make sure your hierarchy is easy to navigate for end users, use empty Actors as parents of Static Mesh Actors only where necessary. Too many empty Actors clutter the hierarchy and make it more difficult to read and use inside both Twinmotion and Unreal Engine.

|   |   |
| --- | --- |
| ![Too many empty Actors](https://dev.epicgames.com/community/api/documentation/image/e9029a78-cb7d-4c57-8b38-a0a8c46e69b7) | ![Empty Actors used only when necessary](https://dev.epicgames.com/community/api/documentation/image/b58db296-1f33-42ef-908e-1812188911fc) |
| Too many empty Actors. | Empty Actors used only when necessary. |

#### Useful API Calls

- [IDatasmithActorElement::AddChild](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement/AddChild?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpComponent.cpp`

### Actors as Components

In applications such as Revit or Archicad, it is typical to have objects that have several sub-elements. For example, a Curtain Wall is typically built with panels and mullions and a Railing is typically built with rails and balusters:

![Curtain Walls and Railings in Revit](https://dev.epicgames.com/community/api/documentation/image/032b3a43-474f-45d2-9916-524867a2964c)

_In Revit, Curtain Walls and Railings are special objects that contain sub elements (panels, mullions, balusters, handrails)._

While it is possible to export each element as an individual Static Mesh Actor, this ends up exporting too many objects and the World Outliner in Unreal Engine becomes overly crowded, as shown below.

![Too many Actors!](https://dev.epicgames.com/community/api/documentation/image/f41356c0-e6c4-4610-a539-152af2ea8a7e)

_Curtain Wall exported as one StaticMesh Actor per panel and mullion = lots of actors in the World Outliner! Click the image for full size._

If applicable, consider exporting sub-elements as Actor Components. For example, a Curtain Wall object can be exported using the following Actor and Component hierarchy:

- Curtain Wall Object → empty Actor. Panel → Static Mesh Actor Component Panel → Static Mesh Actor Component Mullion → Static Mesh Actor Component Mullion → Static Mesh Actor Component

![A much cleaner hierarchy with Actors and Components](https://dev.epicgames.com/community/api/documentation/image/1dd3405f-41e9-4a57-a863-6aa6df88ba6f)

_Curtain Wall exported as an Empty Actor with each panel and mullion as a StaticMesh Actor Component results in considerably less clutter in the World View hierarchy. Click the image for full size._

In the `.udatasmith` file, the hierarchy looks like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;Actor name=&quot;...&quot; label=&quot;Walls_Curtain_Wall_Exterior_Curtain_Wall&quot; layer=&quot;Walls&quot;&gt;\n\t    &lt;Transform .../&gt;\n\t    &lt;children visible=&quot;true&quot;  selector=&quot;false&quot; selection=&quot;-1&quot;&gt;\n\t\t    &lt;ActorMesh name=&quot;...&quot; label=&quot;Curtain_Panels&quot; layer=&quot;Curtain Panels&quot; component=&quot;true&quot;&gt;\n\t\t\t    &lt;mesh name=&quot;...&quot;/&gt;\n\t\t\t    &lt;Transform .../&gt;\n\t\t    &lt;/ActorMesh&gt;\n\t\t    &lt;ActorMesh name=&quot;...&quot; label=&quot;Curtain_Panels&quot; layer=&quot;Curtain Panels&quot; component=&quot;true&quot;&gt;\n\t\t\t    &lt;mesh name=&quot;&gt;\n\t\t\t    &lt;Transform .../&gt;\n",
  "lines_of_code": 15,
  "id": 150664,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--9feca886e9ed000742261af63f9547af2eb9dd26ccfc757bba82e6725073bf80",
  "settings": {
    "is_hidden": false
  }
}
```

#### Guidelines

- Use Static Mesh Actor Components to represent child objects such as curtain wall panels, balusters, or similar compound objects.
- You must set both the hierarchy ([IDatasmithActorElement::AddChild](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement/AddChild?application_version=5.5)) and component flag ([IDatasmithActorElement::SetIsAComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement/SetIsAComponent?application_version=5.5)) in order for this to work correctly.

#### Useful API Calls

- [IDatasmithActorElement::AddChild](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement/AddChild?application_version=5.5)
- [IDatasmithActorElement::SetIsAComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement/SetIsAComponent?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpComponent.cpp`

### Actor Layers

Like many other 3D applications, Unreal Engine supports the concept of Layers. A Layer is an Actor property that indicates where the Actor sits in a scene's visual hierarchy.

The example below shows a possible use of layers in a `.udatasmith` file.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;ActorMesh name=&quot;2&quot; label=&quot;Sphere001&quot; layer=&quot;Layer002&quot;&gt;\n    ...\n    &lt;/ActorMesh&gt;\n    &lt;ActorMesh name=&quot;3&quot; label=&quot;Box001&quot; layer=&quot;Layer004&quot;&gt;\n    ...\n    &lt;/ActorMesh&gt;",
  "lines_of_code": 6,
  "id": 150665,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--7a462cd550505f4b1e0cbd3bafe6a3e0ceb4720a76f448b650a9d909bd15e29f",
  "settings": {
    "is_hidden": false
  }
}
```

#### Guidelines

- If your source application uses Layers, you should translate them to Layers in Unreal Engine.
- If your source application doesn't use Layers, consider if there is any other data you can translate into Unreal Engine Layers. For example, Revit doesn't use Layers, but classifies entities into Categories. ![Revit entities imported on Layers derived from Revit categories](https://dev.epicgames.com/community/api/documentation/image/e8672cf3-0d92-4f84-b14e-fd80700c9795)

#### Limitations

- Layer names must be unique.
- Unreal Engine doesn't support nested layers.

|   |   |
| --- | --- |
| ![Nested Layers in 3ds Max](https://dev.epicgames.com/community/api/documentation/image/1895ed60-2fa5-420d-9282-5dff95adade0) | ![The same layers imported in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/39230467-9cf1-4442-b251-1f83dd436c37) |
| Nested Layers in 3ds Max. | The same layers imported in Unreal Engine. Observe the flat Layer hierarchy. |

#### Useful API Calls

- [IDatasmithActorElement::SetLayer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement/SetLayer?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/Private/DatasmithMaxSceneExporter.cpp`

### Actor Tags

Unreal Engine supports user-defined tags for Actors. Datasmith uses Actor Tags to hold technical information that describes how data is structured in the source application. Unreal Engine users can then use these Actor tags to perform scripting operations, for example with Python, Blueprint Utilities, or Visual Dataprep.

Below is an example use of tags on Static Mesh Actors in a `.udatasmith` file exported from 3ds Max:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;ActorMesh ...&gt;\n\t    &lt;mesh name=&quot;a8f655367fcc240a8c9eb8d847d58463&quot;/&gt;\n\t    &lt;Transform .../&gt;\n\t    &lt;tag value=&quot;Revit.Element.Id.186551&quot; /&gt;\n\t    &lt;tag value=&quot;Revit.Element.UniqueId.07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b7&quot; /&gt;\n\t    &lt;tag value=&quot;Revit.DB.FamilyInstance.Mirrored.True&quot; /&gt;\n\t    &lt;tag value=&quot;Revit.DB.FamilyInstance.HandFlipped.False&quot; /&gt;\n\t    &lt;tag value=&quot;Revit.DB.FamilyInstance.FaceFlipped.True&quot; /&gt;\n\t    &lt;tag value=&quot;Revit.Host.Id.156316&quot; /&gt;\n\t    &lt;tag value=&quot;Revit.Host.UniqueId.9e597f98-694d-4ada-b8ef-0e7459e0b930-0002629c&quot; /&gt;\n",
  "lines_of_code": 21,
  "id": 150666,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--bb5d4c3d251ebaff52cf25f749087179def0df4a6c6d4b1edee90a2bbb946934",
  "settings": {
    "is_hidden": false
  }
}
```

Although there aren't strict rules as to what to put in an Actor's tags, we adopted the methodology of using tags for holding information that is specific to the source application.

For example, in the case of 3ds Max, we decided to use the tags to hold information about the type of object (in 3ds Max), whether or not it's part of a group, and so on.

For Revit, we have adopted a similar approach where we store information that describes the internal structure of Revit entities.

|   |   |
| --- | --- |
| ![Actor Tags on Actor Components from Revit](https://dev.epicgames.com/community/api/documentation/image/acb7d8ca-0ec2-4363-b7fc-b77abda392c7) | ![Actor Tags from 3ds Max](https://dev.epicgames.com/community/api/documentation/image/ffda5114-188d-4b4f-89c6-b31bf6ad8347) |
| Actor Tags on Actor Components from Revit. | The same layers imported in Unreal Engine. Observe the flat Layer hierarchy. |

#### Guidelines

- Prefix your tags with the name of the application you're importing from (for example: Revit.TagName or Max.TagName).
- Use tags to represent technical information about how data is structured in the source application. To store other user-defined data, use metadata instead.

#### Useful API Calls

- [IDatasmithActorElement::AddTag](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement/AddTag?application_version=5.5)
- [IDatasmithActorElement::SetIsAComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement/SetIsAComponent?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpComponent.cpp`

### Metadata

Datasmith carries Key / Value pairs that can be used to store BIM information (or any other custom data) on entities.

![3ds Max metadata translated into Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/f28fc52f-eadb-4173-b56a-c312b1ecb0f6)

_Metadata from 3ds Max (left) translated into Unreal Engine (right)._

#### Limitations

- Key / Value pairs can only carry strings. This means that floats, units, etc. will need to be contained ("baked") into the string (for example, "10 mm").
- Hierarchical properties are not supported, so you'll need to flatten the hierarchy using an underscore ( \_ ) separator. Refer to the Revit example below where **Element** and **Type** properties are handled by concatenating text strings to keep things grouped.

![A simulated flattened hierarchy using metadata from Revit](https://dev.epicgames.com/community/api/documentation/image/fb098c05-9097-492c-bc55-dcb1e40f2b57)

_A simulated flattened hierarchy using metadata from Revit._

#### Useful API Calls

- [IDatasmithMetaDataElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMetaDataElement?application_version=5.5)
- [IDatasmithMetaDataElement::SetAssociatedElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithMetaDataElement/SetAssociatedElement?application_version=5.5)
- [FDatasmithSceneFactory::CreateKeyValueProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithSceneFactory/CreateKeyValueProperty?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/Private/DatasmithMaxSceneExporter.cpp`

### Camera Actors

Datasmith can create Cameras in Unreal Engine, but, depending on your use case, you may or may not want to export cameras from the 3D application. Sometimes, users set cameras explicitly (for example, 3ds Max Physical Cameras). Other times, Cameras are derived from other application concepts (for example, Views from Revit, or Bookmarks from SketchUp).

One key element to consider with regards to Unreal Engine Cameras is that they have physically based characteristics that you will need to set at export time, such as:

- Sensor width
- Aspect ratio
- Exposure value
- White point
- Depth of Field, and so on.

Below is an example implementation of a Camera with tags and characteristics in a `.udatasmith` file.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;Camera name=&quot;1856&quot; label=&quot;PhysCamera001&quot; layer=&quot;0&quot;&gt;\n\t\t    &lt;LookAt Actor=&quot;1857&quot;/&gt;\n\t\t    &lt;Transform tx=&quot;706.201538&quot; ty=&quot;468.560883&quot; tz=&quot;0.0&quot; sx=&quot;1.0&quot; sy=&quot;1.0&quot; sz=&quot;1.0&quot; qx=&quot;0.0&quot;     qy=&quot;0.0&quot; qz=&quot;-0.758784&quot; qw=&quot;0.651344&quot; qhex=&quot;0000000000000000A33F42BF79BE263F&quot;/&gt;\n\t\t    &lt;SensorWidth value=&quot;36.0&quot;/&gt;\n\t\t    &lt;SensorAspectRatio value=&quot;1.333333&quot;/&gt;\n\t\t    &lt;DepthOfField enabled=&quot;0&quot;/&gt;\n\t\t    &lt;FocusDistance value=&quot;850.27594&quot;/&gt;\n\t\t    &lt;FStop value=&quot;8.0&quot;/&gt;\n\t\t    &lt;FocalLength value=&quot;40.0&quot;/&gt;\n\t\t    &lt;LookAtRollAllowed enabled=&quot;0&quot;/&gt;\n",
  "lines_of_code": 23,
  "id": 150667,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--e82b875ee6b20b5a54db8c8fc0a9726dd9a8c0111c4d00988a6ebfe3f0c79032",
  "settings": {
    "is_hidden": false
  }
}
```

![Unreal Engine CineCameraActor](https://dev.epicgames.com/community/api/documentation/image/342fc607-d882-4605-896e-b84c9d4039ce)

_Unreal Engine CineCameraActor._

#### Guidelines

Depth of Field, Exposure, and other photographic effects defined by post-processing settings are also optional. These require a close relationship between lighting and cameras in the source application which may not be defined in the context of your own Datasmith export.

#### Limitations

- Unreal Engine Cameras don't support skewed cameras (2-point perspective). For example, Revit can have "cropped" views that will shift the Camera perspective, but Datasmith (and, by extension, Unreal Engine) doesn't support this type of Camera transformation.

#### Useful API Calls

- [IDatasmithActorElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithActorElement?application_version=5.5)
- [IDatasmithCameraActorElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithCameraActorElement?application_version=5.5)
- [IDatasmithCameraActorElement::SetPostProcess](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithCameraActorElement/SetPostProcess?application_version=5.5)
- [IDatasmithPostProcessElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithPostProcessElement?application_version=5.5)

#### Code Example

For an example implementation, refer to the following files in the Unreal Engine repository:

- `/Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/Private/DatasmithMaxCameraExporter.cpp`
- `/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpCamera.cpp`

### Texture Assets

In Unreal Engine, textures represent more than just color information. In order to be sampled and affect lighting and shading correctly, you must indicate the intended use for the texture (texturemode). Possible uses include:

- Diffuse
- Specular
- Normal
- NormalGreenInv
- Displace
- Other
- Bump
- Ies

We also need to specify its color space (typically Gamma correction or sRGB) as this has a direct impact on how light will work with materials (sRGB and RGB curve).

Below is an example implementation of a texture Asset in a `.udatasmith` file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;Texture name=&quot;sitework_planting_gravel_mixed_0&quot; texturemode=&quot;0&quot; texturefilter=&quot;3&quot; textureaddressx=&quot;0&quot; textureaddressy=&quot;0&quot; rgbcurve=&quot;-1.000000&quot; srgb=&quot;0&quot; file=&quot;rac_advanced_sample_project-3DView-{3D}_Assets/sitework.planting.gravel.mixed.png&quot;&gt;\n\n\t\t    &lt;Hash value=&quot;b10e41741cfee286a5fcf3b288de78f5&quot;/&gt;\n\n    &lt;/Texture&gt;",
  "lines_of_code": 5,
  "id": 150668,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--94e4f2c074ea8a862797163cd599e6955028e392c941f5f5661e289c51e8c1df",
  "settings": {
    "is_hidden": false
  }
}
```

#### Guidelines

- You must set your color space (Gamma / sRGB) correctly, based on the texture's intended use: sRGB color space is typically used for Albedo textures. Linear color space is typically used for normal, height, or bump maps.
- The texture's name (not filename) must be [sanitized](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithUtils/SanitizeName?application_version=5.5) (that is, it must not include any invalid characters).
- You must place textures in the same folder as the rest of the Assets. ![Textures should be exported in the same folder as the other Assets](https://dev.epicgames.com/community/api/documentation/image/cfd4cbd6-c079-40f5-9614-e2692e5bfa53)

#### To Be Avoided

- Do not use absolute paths.
- Do not place textures in a different folder than the rest of the Assets.
- While exporting, you don't need to transform textures. The Datasmith importer will handle transforms. There is no need to convert textures to `.uasset` files with the DatasmithCore API. There is no need to reformat, resize, or convert textures to different formats.

![Incorrect placement of texture files](https://dev.epicgames.com/community/api/documentation/image/e7b77c02-1c8f-44dd-9aa8-30729633eab1)

_This image shows an incorrect use of .uasset files to represent textures._

#### Useful API Calls

- [IDatasmithTextureElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithTextureElement?application_version=5.5)
- [EDatasmithTextureFilter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/EDatasmithTextureFilter?application_version=5.5)
- [EDatasmithTextureMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/EDatasmithTextureMode?application_version=5.5)
- [IDatasmithTextureElement::SetRGBCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithTextureElement/SetRGBCurve?application_version=5.5)
- [FDatasmithUtils::SanitizeName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/FDatasmithUtils/SanitizeName?application_version=5.5)

#### Code Example

For an example implementation, refer to the following file in the Unreal Engine repository:

`/Engine/Source/Programs/Enterprise/Datasmith/DatasmithSketchUpRubyExporter/Private/DatasmithSketchUpMaterial.cpp`

### Materials

#### Simple PBR Export

The following example demonstrates how textures can be exported to a Datasmith file to create a basic PBR material containing an albedo map and a height map.

##### Original Material in Rhino

This example uses the following Material in Rhino:

![A material in Rhino](https://dev.epicgames.com/community/api/documentation/image/58aedf39-e2bb-4d83-9bda-7dd9c52c42dc)

The Material's settings are as follows:

|   |   |
| --- | --- |
| ![Albedo map](https://dev.epicgames.com/community/api/documentation/image/2c95fd17-11d4-4844-bb8e-90a3220c3a80) | ![Height map](https://dev.epicgames.com/community/api/documentation/image/f5a93062-684f-4122-900b-abc5300f1a8a) |
| Albedo map | Height map |

##### Resulting Datasmith file

The resulting Datasmith file will look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;Texture name=&quot;c02622dee4b6e6e08265ed1a8ed947e3&quot; label=&quot;ColorChecker_sRGB_from_Lab_D50&quot; **texturemode=&quot;0&quot;** texturefilter=&quot;3&quot; textureaddressx=&quot;0&quot; textureaddressy=&quot;0&quot; rgbcurve=&quot;1.000000&quot; **srgb=&quot;1&quot;** file=&quot;rhino_diffuse_and_bump_Assets/ColorChecker_sRGB_from_Lab_D50.bmp&quot;&gt;\n\t\t    &lt;Hash value=&quot;2eac7dc7c873963f39791a4c7e9a6f74&quot;/&gt;\n    &lt;/Texture&gt;\n    &lt;Texture name=&quot;82c22916309f2f098d35b2856b2caf5c&quot; label=&quot;Heightmap_normal&quot; **texturemode=&quot;6&quot;** texturefilter=&quot;3&quot; textureaddressx=&quot;0&quot; textureaddressy=&quot;0&quot; rgbcurve=&quot;1.000000&quot; **srgb=&quot;0&quot;** file=&quot;rhino_diffuse_and_bump_Assets/Heightmap.png&quot;&gt;\n\t\t    &lt;Hash value=&quot;cafca7197e3f5a46480b09f329f9eabd&quot;/&gt;\n    &lt;/Texture&gt;\n\n    &lt;UEPbrMaterial name=&quot;90589c47f06eb971d548591f23c285af&quot; label=&quot;Custom&quot;&gt;\n    \t\t&lt;Expressions&gt;\n\t\t\t    &lt;Texture Name=&quot;Diffuse_Map&quot; PathName=&quot;c02622dee4b6e6e08265ed1a8ed947e3&quot;&gt;\n",
  "lines_of_code": 18,
  "id": 150669,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2NjksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1Njo0NyswMDowMCJ9--dceeb91bbef949b3f481ab0085f27632c5b9413c2d9ad53ea5996b7d6db2c3dd",
  "settings": {
    "is_hidden": false
  }
}
```

Observe that the two Textures above have different values for `texturemode` and `srgb`:

- `texturemode="0"` and `srgb="1"` for the first Texture
- `texturemode="6"` and `srgb="0"` for the second Texture

##### Imported in Unreal Editor

In Unreal Engine, the importer Material's PBR graph will look like this:

![Imported Material's PBR graph](https://dev.epicgames.com/community/api/documentation/image/f53653e8-e0af-4a7c-8493-d2f3be0888ef)

_Click the image for full size._

Note that the albedo map is set to `SRGB=1` and the sampler type is set to `Color`. This is automatically set up by the Datasmith importer and is the result of setting the exported albedo map as:

`texturemode="0" srgb="1"`

The height map, which was greyscale in Rhino, has been converted to a normal map by the Datasmith importer, which is the result of setting the texture as:

`texturemode="6" srgb="0"`

##### Useful API Calls

- [IDatasmithUEPbrMaterialElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithUEPbrMaterialElement?application_version=5.5)
- [IDatasmithTextureElement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/IDatasmithTextureElement?application_version=5.5): SetSRGB - [EDatasmithColorSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/EDatasmithColorSpace?application_version=5.5) SetTextureMode - [EDatasmithTextureMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DatasmithCore/EDatasmithTextureMode?application_version=5.5)
