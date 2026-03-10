# Upgrading Niagara Tags

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/upgrading-niagara-tags-in-unreal-engine

> Application Version: 5.7

![The Tagged Asset Browser](https://dev.epicgames.com/community/api/documentation/image/ab1ed11d-63d7-45cc-b7be-7568ec3f57ff)

![Comparing tags in an asset to tags in the Asset Browser](https://dev.epicgames.com/community/api/documentation/image/560b9418-f8ca-42e5-b6bc-61c09573bd9b)

The update of the **Niagara Asset Browser** with the release of Unreal Engine 5.7 means you need to upgrade existing Niagara systems and emitters that use Niagara asset tags to use the new **Tagged Asset Browser Configuration** assets.

For projects that make use of Niagara Asset Tags, we advise resaving existing Niagara systems and emitters. Tags will automatically transfer to the new User Asset Tag system once loaded.

If you defined your own tags in a now-deprecated **Niagara Asset Tag Definition** asset, we added a new context action. This action finds all Niagara assets containing the tags defined inside, and asks you to resave them.

![New context action to migrate tagged assets to user asset tags.](https://dev.epicgames.com/community/api/documentation/image/09f784d2-96bc-4949-9835-bf65bef77354)

For internal tags defined in C++, you can navigate to the folders with the assets you want to update, and use the console command `fx.Niagara.MigrateInternalTagsToUserAssetTags`.
