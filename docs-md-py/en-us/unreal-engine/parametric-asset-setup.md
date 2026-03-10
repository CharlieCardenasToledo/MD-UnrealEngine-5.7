# Parametric Asset Setup

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/parametric-asset-setup

> Application Version: 5.7

Before we get started with asset creation, there are a few things we need to do. First, enable both **MetaHuman** and **Chaos Cloth** Plugins:

1. In **Unreal Engine** (UE) 5.6 or later, click **Edit > Plugins** in the menu bar.
2. Under the **Built-In** section of the **All Plugins** list: Click **MetaHuman**, and enable the **MetaHuman Creator** plugin. ![Image](https://dev.epicgames.com/community/api/documentation/image/ac68fbd6-c6d6-4163-8af0-a4035c78dec4) Click **Physics**, and enable **Chaos Cloth Asset** and **Chaos Cloth Asset Editor**. ![Image](https://dev.epicgames.com/community/api/documentation/image/98feabc2-7748-49c1-8ef3-ba3bf242b0c4) You must restart UE to apply this change.
3. In the **Epic Games Launcher**, in the **Library** tab, click on the dropdown menu on the **Launch** button of the engine version you wish to use. Select **Options**. ![Epic Games Launcher Options](https://dev.epicgames.com/community/api/documentation/image/68f558d2-0804-4eb8-9f09-9cd9d28be98e)
4. Check the box next to **MetaHuman Creator Core Data** and click **Apply**. This will download essential content for MetaHuman Creator.
5. In UE, click **Edit > Project Settings**. In the left-hand menu of the Project Settings window, scroll to the **Plugins** section, and click **MetaHuman SDK**. In these settings, are **MetaHuman Packaging Paths**. ![MetaHuman Packaging Paths](https://dev.epicgames.com/community/api/documentation/image/093d258e-a40a-4533-a8bc-2cbdb1271637) Take note of the location for Outfits. As a default, this is `/Game/Outfits` which shows up in your Content Browser as **All > Content > Outfits**. For this example, we will use the default directory, **Outfits**, and be creating an asset called “techwearOutfit” (which you can download from [FAB](https://www.fab.com/listings/9e04c752-1979-4723-b78f-6d24afc532bc)).
6. In the Content Browser, inside of the Outfits folder, create a folder with the same name as your asset. In this case “techwearOutfit.” Then, create and nest a second folder inside the first, with the same name. You should end up with a folder structure that looks like this: ![Outfit Path](https://dev.epicgames.com/community/api/documentation/image/af033243-cd0d-462d-b4a7-7ff3fcee0e86) Within this working folder, you can arrange things in any way you want; you can create subfolders for different types of assets, such as meshes, cloth assets, materials and textures, or you can keep them all within this folder.

### Next Step

- [Related Document](en-us/unreal-engine/creating-your-metahuman-in-unreal-engine.md)
