# Packaging Your Outfit Asset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-your-outfit-asset

> Application Version: 5.7

The **MetaHuman Manager** is a UI that verifies if assets are MetaHuman compatible, and generates `.mhpkg` files. Mhpkg is the format we use to upload and sell MetaHuman compatible assets on FAB. Mhpkgs from MetaHuman Manager are the only file type that is accepted by FAB when creating a listing in the new MetaHuman format. Packages can then be imported into **Unreal Engine** (UE) using the standard FAB import procedure.

## Packaging Your Outfit

1. To package your outfit, in the Unreal Editor, navigate to **Window > MetaHuman** **Manager**. ![UE MetaHuman Manager](https://dev.epicgames.com/community/api/documentation/image/e2824719-2135-446e-889b-bf079afb399a) MetaHuman Manager will scan the folders that are in the settings of MetaHuman Packaging Paths, and look for valid assets.
2. Your outfit should show up in the **Clothing (Outfit)** section. Click **Verify** at the bottom of the window. ![MetaHuman Manager](https://dev.epicgames.com/community/api/documentation/image/99c09eaf-706e-46f6-aba2-b30dcd10966d) Errors and warnings may appear. If an asset has errors, you will not be able to package it. If it has warnings, you will be able to package it, but it may not be an optimal asset. It is recommended to fix them and re-verify.
3. Once you’ve passed verification, you will be able to use the **Package** button next to it. Click **Package**, select where you’d like to save that package, and make note of that location.
4. To test your asset, create a blank project in Unreal Editor. Your outfit asset must be placed inside a folder structure identical to the one it was created in. For this tutorial, create the following structure: `Content/Outfits/techwearOutfit`
5. Drag-and-drop your packaged file into the techwearOutfit folder. You can now test your outfit asset.

## Next Step

- [Related Document](en-us/unreal-engine/uploading-to-fab-marketplace.md)
