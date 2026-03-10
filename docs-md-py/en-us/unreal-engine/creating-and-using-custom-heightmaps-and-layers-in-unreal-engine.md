# Creating and Using Custom Heightmaps and Target Layers

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-custom-heightmaps-and-layers-in-unreal-engine

> Application Version: 5.7

There will be times your **Landscape** will require that you use external programs to create both the **heightmap** and **target layers** that you need.
Unreal Engine accommodates this style of workflow by allowing for the import of custom heightmaps and target layers.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You use an <b>Edit Layer</b> (like a temporary paint layer) to<i> make</i> changes, and those changes are applied to a <b>Target Layer</b> (like a specific material blend) on the landscape.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Edit layers function as containers for actors (e.g. meshes, lights) to toggle them on/off or assign them to specific views or visibility sets.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "A target layer is a specific layer <i>in your material</i> (e.g. a \"grass\" or \"mud\" weightmap) that your active edit is modifying.",
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

![Image from the Electric Dreams sample project](https://dev.epicgames.com/community/api/documentation/image/f43c085c-ae21-4d99-8c69-9be7a6c15b57)

_The Electric Dreams project_

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If this is your first time using the Landscape tools, you might want to check out the <a href=\"building-virtual-worlds/landscape-outdoor-terrain/editing-landscapes\">Landscape Overview</a> first.",
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

## Importing Landscape Data from Image Files

Image files can be imported into landscape heightmaps and target layers, which can be used to customize the look and feel of your Landscape.

### Image File Formats

Image data from .PNG and .RAW files can be imported.  The native data format for heightmaps should be single-channel, grayscale, 16 bits per pixel.  The native data format for target layers should be single-channel, grayscale, 8 bits per pixel.  Standard three-channel RGB images can be used, but color information will be lost and the precision of the import process may be limited. If you are creating an image file in Photoshop to use for importing landscape data, use the following settings when creating a new document for a target layer:

![Image of Photoshop sample settings](https://dev.epicgames.com/community/api/documentation/image/afc379fd-3099-4b7c-a192-479ff7bdd18a)

Custom image file import formats can be implemented using the `ILandscapeHeightmapFileFormat` and `ILandscapeWeightmapFileFormat` interfaces.

## Using Target Layers in a Landscape Material

Importing image files that are made in an external application provides you with the flexibility to use your preferred terrain workflow, but you first need to make sure that a few things are set up in order to get everything to work smoothly.

1. First, make sure that you have created a Landscape to work with. If you have questions regarding the Landscape creation process, check out [Landscape Creation](building-virtual-worlds/landscape-outdoor-terrain/creating-landscapes).
2. Next, make a new material. For this example, you will be making a very basic material that ca be easily expanded upon if needed. The setup for your material should look something like this. ![Blueprints-showing-materials](https://dev.epicgames.com/community/api/documentation/image/a21bf0bb-1c26-4430-a206-a27fe06dad26)
3. Once the material is complete, apply it to the Landscape actor. This will turn your landscape black. ![Apply the Material to the Landscape Actor](https://dev.epicgames.com/community/api/documentation/image/5918307c-e05b-42ee-b6d2-db7497899430)
4. To fix the issue, add some Layer Info to your Landscape actor. For this example, create one Layer Info object for each of the three layers. To read more about Layer Info objects, refer to the [Layer Info Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine) page. ![Create Layer Info objects and save them](https://dev.epicgames.com/community/api/documentation/image/eaef289e-34aa-44c4-9a6b-24e048782563)
5. When completed, your Target Layers section of your Landscape panel should look something like this. ![Target Layers section with each Layer having a Layer Info](https://dev.epicgames.com/community/api/documentation/image/c4e626e7-d52b-4d8f-bc85-c3e696702aa5)
6. Now it is time to import your custom layer. In **Landscape Mode**, on the **Manage** tab, select the Import from file tab. At the **Heightmap** field, use the (**...**) button to **Browse for file**. This will prompt you to choose the .PNG or .RAW file that contains your custom layer data. Your custom layer file should be the same resolution as your Landscape actor's **Overall Resolution** that was set when you created it (the default is 505 x 505).
7. If your layers are not output at the correct size, you will see the following warning: ![error-message-about-file-size](https://dev.epicgames.com/community/api/documentation/image/131ab9fe-ca68-43b0-99f3-5ec791d79866) To fix this issue, return to your image editing software and resize your file to match the correct Landscape extent as displayed by the warning message.

## Heightmaps

Using external tools to create a base heightmap to use inside Unreal Engine can be an excellent way of speeding up the Landscape creation process. Programs such as World Machine and Terragen can quickly create the base heightmap for your Landscape. The base can then be imported, cleaned up, or modified using the editing tools inside Unreal Editor, making it a better fit with the world and the desired game play.

For more information on importing and exporting heightmaps, see [Importing and Exporting Landscape Heightmaps](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine).
