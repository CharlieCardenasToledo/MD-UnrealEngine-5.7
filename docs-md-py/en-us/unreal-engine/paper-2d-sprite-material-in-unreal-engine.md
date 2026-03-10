# Paper 2D Sprite Material

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-sprite-material-in-unreal-engine

> Application Version: 5.7

**Sprite Materials** are assignable [Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials) assets that influence the Sprites appearance in levels, such as sharpening pixels, smoothing edges, and how translucent they are.

![select sprite material property](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1426e6e5-b095-4fed-9a01-c207f76a37e2/material.png)

Materials can also affect how the Sprites interact with the environment lighting and can even emit its own lighting.

![sprite material render comparison](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a963125b-e598-435b-ba84-d251d834c2d5/emit.png)

## Sprite Material Reference

Here you can reference a list of the materials included with the Paper2D plugin that you can use when working with Sprites in Unreal Engine.

| Material | Example Image | Description |
| --- | --- | --- |
| **DefaultLitSpriteMaterial** | default lit sprite material | This material uses the **Default Sprite Texture Settings** as the material settings. Using this material, will also enable the sprite's appearance to be influenced by lights within the level. |
| **DefaultSpriteMaterial** | default sprite material | This material will use the **Default Sprite Texture Settings** as the material settings. Using this material, will also prevent the sprite's appearance from being influenced by lights within the level.  There are two DefaultSpriteMaterials found in the engine content, one is designed for the Paper 2D system while the other is designed for the [Niagara particle system](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine). You can delineate the two by hovering over the material, and ensuring the **Path** lists the `/Paper2d` file path. |
| **MaskedLitSpriteMaterial** | masked lit sprite material | This material will **mask** the sprite from its background and the level, creating a hard cutoff between the sprite and the background. When using a mask material, no gradient transparency values can be used. Using this material, will also enable the sprite's appearance to be influenced by lights within the level. |
| **MaskedUnlitSpriteMaterial** | masked unlit sprite material | This material will **mask** the sprite from its background and the level, creating a hard cutoff between the sprite and the background. When using a mask-material, no gradient transparency values can be used. Using this material will also prevent the sprite's appearance from being influenced by lights within the level. |
| **OpaqueLitSpriteMaterial** | opaque lit sprite material | This material will use a solid layer for the entire sprite object. This material does not allow for any transparency or gradient of transparency in the sprite's pixels. If the sprite contains a transparent background, this material will fill the background in with a solid black. Using this material will enable the sprite's appearance to be influenced by lights within the level. |
| **OpaqueUnlitSpriteMaterial** | opaque unlit sprite material | This material will use a solid layer for the entire sprite object. This material does not allow for any transparency or gradient of transparency in the sprite's pixels. If the sprite contains a transparent background, this material will fill the background in with a solid black. Using this material will prevent the sprite's appearance from being influenced by lights within the level. |
| **TranslucentLitSpriteMaterial** | translucent lit sprite material | This material will allow for transparency and transparency gradients to occur on the sprite. This material can be helpful for creating see-through materials such as windows or water. Using this material will also enable the sprite's appearance to be influenced by lights within the level.  Transparency materials are the most performance intensive, so it is important to use these materials sparingly in your project. |
| **TranlucentUnlitSpriteMaterial** | translucent unlit sprite material | Using this material, will allow for transparency and transparency gradients to occur on the sprite. This material can be helpful for creating see-through materials such as windows or water. This material is the most performance intensive so it is important to use this mode sparingly. Using this material, will prevent the sprite's appearance from being influenced by lights within the level.  Transparency materials are the most performance intensive, so it is important to use these materials sparingly in your project. |

## Custom Sprite Materials

You can edit existing Sprite Material assets or create custom Material assets that you can use to render your Sprites in your project.

For more information about creating material assets, see the [Material Editor Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide) documentation.
