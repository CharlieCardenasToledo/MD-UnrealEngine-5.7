# Revit

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-datasmith-with-revit-in-unreal-engine

> Application Version: 5.7

This page describes how Datasmith imports scenes from Autodesk Revit into Unreal Editor. It follows the basic process outlined in the [Datasmith Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-plugins-overview) and [About the Datasmith Import Process](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine), but adds some special behavior that is specific to Revit. If you're planning to use Datasmith to import scenes from Revit into Unreal Editor, reading this page can help you understand how your scene is translated, and how you can work with the results in Unreal Editor.

![Revit](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69db2c76-7c81-401d-9bfe-3db1edd94686/datasmith-revit-compare-revit.png)

![Unreal Engine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a487e1d-e343-4f05-97be-df10f94ded34/datasmith-revit-compare-unreal.png)

## Revit Workflow

Datasmith uses an Export Plugin workflow for Revit. This means that to get your Revit content into the Unreal Engine using Datasmith, you need to:

1. Install a plugin for Revit. See the **Installation Notes** section below.
2. Export your Revit content to a `*.udatasmith` file. See [Exporting Datasmith Content from Revit](https://dev.epicgames.com/documentation/en-us/unreal-engine/exporting-datasmith-content-from-revit-to-unreal-engine). Alternatively, you can [use Dynamo](https://dev.epicgames.com/documentation/en-us/unreal-engine/batch-exporting-revit-views-with-dynamo-to-a-datasmith-scene) to batch export Revit views.
3. Enable the **Importers > Datasmith Importer** Plugin for your Project, if it's not already enabled.
4. Use the **Datasmith** importer in the Toolbar of the Unreal Editor to import your`.udatasmith` file. See [Importing Datasmith Content into Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine).

## Installation Notes

Before you can export Revit content, you must download and install the **Datasmith Exporter for Revit** plugin from the [Datasmith Export Plugins](https://www.unrealengine.com/en-US/datasmith/plugins) page.

To see what versions of Revit the plugin supports, see .

We encourage you to share the download link to the Datasmith Exporter plugins with any number of people, both inside and outside of your organization. Please note that you are not permitted to distribute the Datasmith Exporter plugins themselves.

Before you install the Datasmith Exporter for Revit plugin, make sure that:

* Revit is not running.
* You downloaded the installer for the exporter plugin that matches Unreal Engine version you intend to use.
* You uninstalled all previous versions of the Datasmith Exporter for Revit plugin.

After you downloaded the installer, double-click it to open, then follow the instructions on-screen.

When you launch Revit after you installed the exporter plugin, you might see the following warning: "The publisher of this add-in could not be verified. What do you want to do?" Click **Always Load** to confirm that you want the Datasmith Exporter plugin to be available each time you launch Revit.

If you need to uninstall the Datasmith Exporter for Revit plugin, you can do this from the **Control Panel**, like any other Windows application.

## Controlling What Gets Exported

You always need to have a 3D View selected and active in Revit in order to export your scene using the Datasmith Exporter plugin. The visibility settings of that 3D View define what elements from the Revit file get included in the exported `.udatasmith` file.

You can use any 3D View that you already have in your Revit file. However, to take full control over the objects that you bring in to Unreal Engine, we recommend that you set up a new 3D View in Revit, and set up that view so that it shows only the objects that you need in your realtime visualization.

Revit offers many tools and techniques for controlling the visibility of objects inside a 3D View. For example:

* You can use the **Graphics > Visibility/Graphics Overrides** to control the visibility of the different objects and object categories in your Level.
* You can use a [Section Box](http://help.autodesk.com/view/RVT/2019/ENU/?guid=GUID-C9EA51CB-3214-4BD8-AD55-3BEB1CCD15B6) to cut the geometry you export. Only the objects inside your Section Box are exported to Unreal Engine. Note that when an object crosses the boundaries of the Section Box, such as the walls, floor and furniture in the images below, its geometry is truncated. Inside Unreal Engine, the Static Mesh Assets that represent the exported objects only contain the geometry that lies inside the Section Box.
* **Temporary Hide and Isolate** settings in Revit are respected.
* Only geometric objects visible in the current 3D View are exported. Non-geometric objects are ignored.

The Datasmith Exporter respects your choice of which objects are shown and which are hidden, but it does not take into account other settings that control the way the 3D View is drawn in the Revit viewport. For example, it does not take into account the **Graphics > Graphic Display Options** set for the 3D View (Realistic vs. Shaded Model Display, Cast Shadows, and so on) or the **Camera > Rendering Settings** (Draft vs. High Quality settings, Lighting schemes, and so on).

For more information about controlling visibility in a Revit 3D View, see also [Visibility and Graphic Display in Project Views](http://help.autodesk.com/view/RVT/2019/ENU/?guid=GUID-A2FC119B-51D7-4C2E-84ED-CD51983EC532) in the Revit Help.

## Geometry

In general, each element that you can select individually in the Revit scene is translated to Unreal as a separate Static Mesh Asset. Some elements, such as railings, may be broken down further into smaller Static Meshes when they are made up of smaller parts.

In all cases, the geometry of each Static Mesh Asset is set to match the dimensions of the Revit object at the time you export the file. Parametric settings and constraints are not carried over into Unreal Engine. So, for example, if you move a floor up or down in the Unreal Editor, the height of the walls will not stretch or shrink to match the new location as it would in Revit.

### Instancing

If two objects belong to the same family, and if they have exactly the same parameter values, then both objects are represented in the Datasmith Scene as instances of the same Static Mesh Asset.

### Tessellation

Datasmith relies on Revit's built-in tessellation services to create triangular meshes from your scene geometry. In most cases, this produces adequate geometry for use in Unreal Engine. However, if you find these surfaces to be a problem in your Projects, you can try tools offered by the Unreal Editor for reducing the complexity of these meshes, such as the [Proxy Geometry tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/proxy-geometry-tool-in-unreal-engine).

You can also manually specify the level of tessellation for meshes that Revit creates from the **Datasmith Export Settings** panel. These levels are defined by the [Revit API](https://www.revitapidocs.com/2019/d98987f3-27a6-1893-3b7d-fc28e8ed5322.htm).

![Level of Tessellation setting in the Datasmith Export Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b0321d0b-f624-4336-b005-38e9b4c8e4bc/export-settings-tessellation.png)
