# SketchUp Pro

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-datasmith-with-sketchup-pro-in-unreal-engine

> Application Version: 5.7

This page describes how Datasmith imports scenes from Trimble SketchUp Pro into Unreal Editor. It follows the basic process outlined in the [Datasmith Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-plugins-overview) and [About the Datasmith Import Process](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine), but adds some special translation behavior that is specific to SketchUp. If you're planning to use Datasmith to import scenes from SketchUp into Unreal Editor, reading this page can help you understand how your scene is translated, and how you can work with the results in Unreal Editor.

![SketchUp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/066f2e70-c4f9-44c7-9dfa-d69bc9ea22f4/sketchup_datasmith_compare_skp.png)

![Unreal Engine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a456687e-b213-44d6-b7b4-3ceebd9b1da2/sketchup_datasmith_compare_unreal.png)

## SketchUp Workflows

### Export Workflow

Datasmith uses an **Export Plugin** workflow for SketchUp. This means that to get your SketchUp content into Unreal using Datasmith, you need to:

1. Install a plugin for SketchUp. See the **Installation Notes** section below.
2. Export your SketchUp content to a `.udatasmith` file. See [Exporting Datasmith Content from SketchUp Pro](https://dev.epicgames.com/documentation/en-us/unreal-engine/exporting-datasmith-content-from-sketchup-pro-to-unreal-engine).
3. Enable the **Importers > Datasmith Importer** Plugin for your Project, if it's not already installed.
4. Use the **Datasmith** importer available in the Toolbar of the Unreal Editor to import your `.udatasmith` file. See [Importing Datasmith Content into Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine).

### Batch Scene Export with Ruby

You can run a Ruby script in SketchUp to batch export `.udatasmith` files. This helps automate your pipeline.

Before you can do this, you need to install the **Ruby Code Editor** extension for SketchUp. For instructions on how to do that, see the SketchUp documentation on [Managing Extensions](https://help.sketchup.com/en/extension-warehouse/managing-extensions). Once you install the Ruby Code Editor extension, you can access it from SketchUp's main menu: **Window > Ruby Code Editor**.

To export all SketchUp files from a given folder, run this code:

```
           target_dir = 'C:\temp\udatasmithExports'
           source_directory = 'E:\path\to\folder'
           Dir.foreach(source_directory) do |filename|
             ext = File.extname(filename)
             if ext == '.skp' then
                 name = File.basename(filename, ext)
                 path = File.join source_directory, filename
                 Sketchup.active_model.close true
                 Sketchup.open_file path
                 puts "Exporting '#{filename}' as '#{name}' to '#{target_dir}'"
                 EpicGames::Datasmith.export name, target_dir
           end
         end
```

You can also export a single file from code. This is the equivalent of clicking the **Export** button on the Datasmith toolbar:

```
       Sketchup.open_file 'E:\path\to\file\sketchup_file.skp'
       EpicGames::Datasmith.export "hello", 'C:\temp'
       # This creates a C:\temp\hello.udatasmith file.
```

### Direct Link Workflow

To preview changes to your SketchUp scene in Unreal Engine in real time, you can set up a Datasmith Direct Link between the two. This way, you don't need to manually re-import the entire scene into Unreal Engine every time you want to make a change. For more information, see [Using Datasmith at Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-datasmith-at-runtime-in-unreal-engine),

For Unreal Engine, Datasmith DirectLink is only supported on UE 4.27 and later versions, when using one of the following SketchUp versions:

* SketchUp 2020 (Windows and macOS)
* SketchUp 2021 (Windows and macOS)

## Installation Notes

Before you can export SketchUp content, you must download and install the **Datasmith Exporter for SketchUp** plugin from the [Datasmith Export Plugins](https://www.unrealengine.com/en-US/datasmith/plugins) page.

To see what versions of SketchUp the plugin supports, see .

The Datasmith exporter plugin currently only works with SketchUp Pro. It does not support SketchUp Free, or the discontinued SketchUp Make.



We encourage you to share the download link to the Datasmith Exporter plugins with any number of people, both inside and outside of your organization. Please note that you are not permitted to distribute the Datasmith Exporter plugins themselves.

Before you install the Datasmith Exporter for SketchUp plugin, make sure that:

* SketchUp is not running.
* You downloaded the installer for the exporter plugin that matches the Unreal Engine version you intend to use.
* You uninstalled all previous versions of the Datasmith Exporter for SketchUp plugin.

After you downloaded the installer, double-click it to open, then follow the instructions on-screen.

If you need to uninstall the Datasmith Exporter for SketchUp plugin, you can do this like you would any other application:

* Windows: Uninstall the plugin from the **Control Panel**.
* macOS: Find the plugin in **Finder** and drag it to the trash icon on your Dock, or right-click and select **Move to Trash**.

## Using the Datasmith Toolbar

Installing the Datasmith plugin adds a toolbar in SketchUp.

![Datasmith Toolbar in SketchUp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e2fdd26-94c7-420f-aecb-8e9e5df41840/datasmith-toolbar-sketchup.png "Datasmith Toolbar in SketchUp")
