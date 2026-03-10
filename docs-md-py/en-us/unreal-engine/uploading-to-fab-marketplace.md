# Uploading to Fab Marketplace

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/uploading-to-fab-marketplace

> Application Version: 5.7

If you are converting an asset from an existing **Fab** listing, keep your existing listing and add an additional **MetaHuman** format to your existing listing. There is no need to create a new listing, and this way, buyers who have purchased your items previously will automatically have access to the new MetaHuman format version of your asset. If this item is not already on Fab, you can create a new listing.

## Create a New Listing on Fab

1. Add a MetaHuman Format to the listing. ![MetaHuman Tag](https://dev.epicgames.com/community/api/documentation/image/8442df07-3216-4f0c-9896-abce1b025829) ![Choose MetaHuman Format](https://dev.epicgames.com/community/api/documentation/image/584521cc-49dd-40a0-97a5-9c918bb1dc5f) ![Upload File To Fab](https://dev.epicgames.com/community/api/documentation/image/5569fe65-d1d6-42a9-a1e5-e81a8c2bac21)
2. When filling out your listing, add the `parametric` tag for your item. Optionally, you can add other formats (such as Maya source files) or additional files (such as DNA files or other file types not specifically offered as options) if you want to include them in the listing. MetaHuman Manager will only package items in your folder which your main asset has dependencies on. If you want to include other items (such as alternate textures or materials), you must manually zip them and upload them as **Format > Other > Additional Files**.
3. Once you feel good about your listing, **Publish** it. Once it goes through the standard moderation process, it will be listed on Fab and be added to the Fab MetaHuman Channel.

## Next Step

- [Related Document](en-us/unreal-engine/painting-weight-maps.md)
