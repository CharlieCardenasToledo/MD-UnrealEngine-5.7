# Using UI Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-ui-metadata-in-unreal-engine

> Application Version: 5.7

You can use the following document to learn about how to use UI Metadata with Mutable Characters.

## UI Metadata

All parameter and state nodes have a **UI** section section of properties in the **Details** panel. In this section, you can specify extra information for each parameter and parameter option. This information is available in-game. UI metadata is commonly used to help generate the in-game UI.

![UI section of details panel of parameter nodes in mutable character blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16bd4d2d-5aba-4d00-8ade-a798cc129938/image_0.png)

Here you can reference a list of the properties found in this section, with a description of their functionality:

| Property | Description |
| --- | --- |
| **Minimum & Maximum Values** | In these properties you can set two numerical scalar values that can be used as the minimum and maximum values for the node. |
| **Editor Gameplay Tags** | This is an **Editor Only** variable, which means that it is not available in-game.  Using this property you can add tags to parameters and parameter options. Then, from the **Preview Instance** tab, you can filter parameter options that contain any or all the specified tags. gameplay tag filter property |
| **Object Friendly & UI Section Names** | Here you can set object friendly and UI Section names. |
| **UI Order** | Here you can set an order for the UI element using an integer value. |
| **UI Thumbnail** | Here you can set a UI Thumbnail image. |
| **Editor UIThumbnail Object** | This is an **Editor Only** variable, which means that it is not available in-game.  You can use this property to set a thumbnail for a parameter option in the **Instance Properties** tab when the `UI Thumbnails` property is also enabled. You can set any type of asset that has a UE thumbnail. ui thumbnails property |
| **Extra Information** | This option is a Map that you can use to add extra String information with a specifier. extra information property |
| **Extra Assets** | This option is similar to the **Extra Information** property that you can use to add extra asset information with a specifier. extra information property |

## UI Metadata API

The UI Metadata is stored inside the CO, which you can access using the following methods:

* **GetParameterUIMetadata**: This method returns the UI Metadata of the specified parameter.
* **GetIntParameterOptionUIMetadata**: This method returns the UI Metadata of the specified parameter option.
* **GetStateUIMetadata**: This method returns the UI Metadata of the specified state.

![ui metadata api methods](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64908def-282b-46f5-9df7-60ff52f75e88/image_5.png)
