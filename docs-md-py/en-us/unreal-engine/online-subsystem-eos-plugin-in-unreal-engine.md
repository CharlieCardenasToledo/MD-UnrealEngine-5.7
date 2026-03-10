# The Online Subsystem EOS Plugin

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "include",
  "excerpt_id": 61,
  "excerpt_assignment_id": 38,
  "blocks": [
    {
      "type": "callout",
      "callout_type": "note",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Google has informed developers of a vulnerability in versions (earlier than M102) of WebRTC. Impacts, workarounds, and updates can be found <a href=\"https://eoshelp.epicgames.com/s/news/eos-news-article-MCVDBTZSVM7VAJHF4ZGJVXZM52I4?language=en_US\">here</a>.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "WYq",
  "settings": {
    "is_hidden": false
  }
}
```

**Epic Online Services (EOS)** is an engine-agnostic system that provides a range of cross-platform online features, including:

- Player-centric features, such as: Achievements Leaderboards
- Commercial features, such as: In-game purchases
- Social features, such as: Voice communication Friends lists

You can use EOS in your Unreal Engine project with the Online Subsystem Epic Online Services (OSS EOS) plugin. The **Online Subsystem Epic Online Services** plugin helps you interact with Epic Online Services in your game without writing code for interacting with the EOS SDK directly. To use this feature, you must register and configure your product or products with the **EOS Developer Portal**, then enable and configure a few plugins to expose EOS functionality through the OSS interface.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For more information about Epic Online Services including information about registering and configuring your products, see the <a href=\"https://dev.epicgames.com/docs/services/index.html\">Epic Online Services Developer Documentation</a>.",
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

## Overview of EOS Plugins

The OSS EOS plugin builds upon the **Online Subsystem (OSS)** plugin. The [Online Subsystem plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-in-unreal-engine) is a general-purpose plugin that provides a common interface to access a variety of online services. The OSS EOS plugin extends the OSS plugin by implementing specific functionality available through Epic Online Services by integrating communication with the EOS SDK into the plugin. This page discusses the following features of the OSS EOS plugin:

- [Product Registration](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine)
- [Enabling the Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine)
- [Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine)
- [Login](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine#login)
- [Supported Interfaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine)

Optionally, you can extend the OSS EOS plugin with the **OSS EOS Plus** plugin. EOS Plus stands for "EOS + Base Platform," which combines EOS and another platform (such as Steam, console platform, etc.). Combining EOS with another platform provides additional features, such as automatic session mirroring. You can use EOS Plus with or without [Epic Account Services (EAS)](https://dev.epicgames.com/docs/epic-account-services).

### When to Use EOS Plus

If you ship your game on the Epic Games Store, you want to use the OSS EOS plugin; additionally, there is no need to use EOS Plus. If you ship your game on another platform, use the OSS EOS Plus plugin in addition to the OSS EOS plugin. There might be exceptions to this guidance. Continue reading this page to determine the best combination of plugins for your project.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Online Subsystem EOS Plus is a temporary solution to implement certain platform mirroring functionality while that functionality does not exist in the EOS SDK. EOS Plus functionality will be replaced with native EOS SDK support as it becomes available. EOS Plus is a Beta feature with limited feature coverage.",
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

### How to Use OSS EOS

The [OSS EOS Plugin Course](https://dev.epicgames.com/community/learning/courses/1px/unreal-engine-the-eos-online-subsystem-oss-plugin/Lnjn/unreal-engine-introduction) on the [Epic Developer Community](https://dev.epicgames.com/community/unreal-engine) guides you through the process of using OSS EOS in an Unreal Engine project.

## Setup

### Register Your Product with Epic Online Services

The [Epic Developer Resources Documentation](https://dev.epicgames.com/docs) provides you with resources for the Epic Games Store (EGS), Epic Online Services, Kids Web Services (KWS), and their associated tools. To take advantage of the OSS EOS plugin, you must first have a product registered with Epic Online Services. To register your product with EOS, navigate to the [Epic Developer Portal](https://dev.epicgames.com/portal/) and follow the steps to [Get Started](https://dev.epicgames.com/docs/services/GameServices/QuickStart/index.html). In particular, this guide outlines product registration in [Step 1 of the Get Started Steps](https://dev.epicgames.com/docs/epic-online-services/eos-get-started/services-quick-start#step-1---set-up-an-epic-games-account-and-organization). The information provided when you register your product is required later to configure the OSS EOS plugin within Unreal Engine.

Unreal Engine is distributed with a copy of the EOS SDK, so you do not need to download the EOS SDK separately if you want to use the EOS SDK version included with Unreal Engine. To use a different version of the EOS SDK, download your desired version of the EOS SDK by following the instructions in [Step 2 of the Get Started Steps](https://dev.epicgames.com/docs/epic-online-services/eos-get-started/services-quick-start#step-2---download-the-eos-sdk). After you download your desired version of the EOS SDK, follow the instructions on our [Upgrading the EOS SDK](https://dev.epicgames.com/documentation/en-us/unreal-engine/upgrading-the-eos-sdk-in-unreal-engine) documentation for more information about how to upgrade the EOS SDK used by Unreal Engine.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you upgrade the EOS SDK, we recommend you consult the <a href=\"https://dev.epicgames.com/docs/epic-online-services/release-notes\">EOS SDK Release Notes</a> for any necessary updates your upgrade requires.",
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

### Enable the OSS EOS Plugins

To use EOS in your project, you must enable the OSS EOS plugin in Unreal Engine. To enable the OSS EOS plugin, follow these steps:

1. Navigate to **Edit > Plugins**. This opens the **Plugin Browser** where you can search for the plugins you want to enable.
2. Within the **Plugin Browser**, locate and enable the **Online Subsystem EOS** plugin.

Online Subsystem EOS implements the Online Subsystem plugin for Epic Online Services. The following additional plugins are enabled by default when you enable the OSS EOS plugin:

- **EOS Plus** Combines EOS with another platform.
- **EOS Shared** Responsible for initialization and shutdown of the EOS SDK. Enabled by default as a dependency of OSS EOS.
- **EOS Voice Chat** Voice chat support through EOS.

After enabling your desired plugins, you need to configure them for use in your project. Some of the following configuration steps require product-related settings or identifiers received after registering your product with EOS. These are available in your [Epic Developer Portal](https://dev.epicgames.com/portal/).

### Configure the OSS EOS Plugins

In order to proceed, ensure that you have:

1. [Registered your product with Epic Online Services](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine).
2. [Enabled the OSS EOS plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine).

To configure the OSS EOS plugins, follow these steps:

1. From the toolbar, click **Edit > Project Settings**.
2. Navigate to **Plugins > Online Subsystem EOS**.

![Plugins Online Subsystem EOS](https://dev.epicgames.com/community/api/documentation/image/eeec8267-0bb8-4d11-bb04-5c17fc43dc39)

_Edit OSS EOS Plugins_

*Click image to expand.*

#### EOS Settings

These settings relate to EOS' platform-specific configuration. For more information, see the [EOS API Reference](https://dev.epicgames.com/docs/services/API/index.html) page about the [EOS\_Platform\_Options](https://dev.epicgames.com/docs/en-US/api-ref/structs/eos-platform-options) data structure. The following table describes each of the EOS settings:

| Setting | Description |
| --- | --- |
| Cache Dir | Directory for storing temporary EOS data. The default location on Windows is `C:/Users/<USERNAME>/Documents/CacheDir`. |
| Default Artifact Name | This artifact name is used if no artifact is passed via command-line arguments. If you are not passing an artifact name through the command-line, ensure that this matches the **Artifact Name** defined below. |
| Tick Budget in Milliseconds | This setting prevents EOS operations from blocking the game by causing [EOS\_Platform\_Tick](https://dev.epicgames.com/docs/en-US/api-ref/functions/eos-platform-tick) to return. See the Epic Online Services documentation about [EOS\_Platform\_Create](https://dev.epicgames.com/docs/en-US/api-ref/functions/eos-platform-create) for more information. |
| Enable Overlay | Use this to enable or disable overlays. Some overlays may be platform-specific, such as the e-commerce overlay, which is only valid for titles shipping on the Epic Games Store. |
| Enable Social Overlay | The social overlay shows information about friends, achievements, and extra authentication steps. You can disable this overlay individually while leaving other overlays enabled. This setting has no effect if **Enable Overlay** is turned off. |
| Enable Editor Overlay | Use this to enable or disable overlays while in the Unreal Editor. |
| Title Storage Tags | Use when querying multiple files in title data storage. For more information, see the Epic Online Services documentation about [Querying Multiple Files By Tag](https://dev.epicgames.com/docs/game-services/title-storage#querying-multiple-files-by-tag) in the [Title Storage Interface](https://dev.epicgames.com/docs/game-services/title-storage). |
| Title Storage Read Chunk Length | Set the maximum amount of data (bytes) to read in a single callback of [EOS\_TitleStorage\_OnReadFileDataCallback](https://dev.epicgames.com/docs/en-US/api-ref/callbacks/eos-title-storage-on-read-file-data-callback). For more information, see the Epic Online Services documentation about [Accessing Files](https://dev.epicgames.com/docs/game-services/title-storage#accessing-files) in the [Title Storage Interface](https://dev.epicgames.com/docs/game-services/title-storage). |
| Artifacts | The Epic Games Store supports multiple artifacts for a single product. For example, your product can have separate internal artifacts for development, testing, and the released version your customers use. This array contains settings for each named artifact. There must be at least one artifact in the array, and the **Default Artifact Name** value must match the name of one of the array elements. See [Artifact Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine) section below for more information about these settings. |

##### Artifact Settings

Artifact settings include settings for your product that you have registered in the EOS Developer Portal. The settings you configure here should match the settings for your registered product in the EOS Developer Portal. You can find [settings for your products](https://dev.epicgames.com/portal/epic-games/products/your_product/settings) on the EOS Developer Portal.

To edit the **Artifact Settings**, follow these steps:

1. Click the **Add Element** button next to **Artifacts** in the **EOS Settings** section. This creates a new element in the **EOS Settings' Artifact** array.
2. To customize the settings of this new Artifact, click the arrow next to your newly created array element. If this is the first element in the array, the name is **Index[0]**.

The following table describes the available Artifact settings:

| Setting | Description |
| --- | --- |
| Artifact Name | If you are launching on the Epic Games Store, this should match the Artifact ID in the store settings located in your [Developer Portal](https://dev.epicgames.com/portal). If you are not launching on the Epic Games Store, this can be any string. This should also match the artifact passed via the `-epicapp` command-line argument or the Default Artifact Name. |
| Client ID | The Client Id for your product. This Id starts with `xyz` as the first 3 characters. |
| Client Secret | The client secret used to verify your **Client ID**. |
| Product ID | The EOS SDK uses this ID to identify your product. |
| Sandbox ID | The artifact belongs to the sandbox with this ID value. |
| Deployment ID | The Deployment ID you are targeting. Deployment IDs differ for each artifact. For example, if you have `MyGameStaging` and `MyGameRelease` artifacts, they will each have their own Deployment IDs. By default, you have one deployment per sandbox. |
| Client Encryption Key | A 64-byte hexadecimal string that encrypts data when uploaded to an EOS service. Unlike other settings, EOS does not manage this encryption key and it is not stored in your product settings. The key is unique to your game and not known to Epic Games to protect users' data privacy. It is used to encrypt data for Player and Title data storage. |

#### EOS Plus Settings

To use this plugin, first register and configure [your product](https://dev.epicgames.com/portal/epic-games/products/your_product) in the Developer Portal for each [platform](https://dev.epicgames.com/docs/services/Platforms/index.html) you want to support. The platform-specific versions of EOS SDK contain detailed instructions for using the features of the platform each version supports.

Before using the EOS Plus plugin, you must configure EOS Plus Login Settings and Crossplay Settings.

##### EOS Plus Login Settings

The following table describes the EOS Plus Login settings:

| Setting | Description |
| --- | --- |
| Use Epic Account for EOS login (requires account linking) | If this option is enabled, the OSS EOS plugin uses the platform-specific authentication token to sign the user into their Epic Account automatically. |
| Use EOS Connect APIs to create and link Product User IDs (PUIDs), and use EOS Game Services | If this option is enabled, use EOS Connect APIs to link accounts for crossplay. |

##### Crossplay Settings

The following table describes the Crossplay settings:

| Setting | Description |
| --- | --- |
| Mirror Stats to EOS | If this option is enabled, EOS Plus sends a duplicate of all [Stats](https://dev.epicgames.com/docs/services/API/Interfaces/Stats/index.html) information to the OSS EOS plugin. |
| Mirror Achievements to EOS | If this option is activated, EOS Plus sends a duplicate of all [Achievement](https://dev.epicgames.com/docs/services/API/Interfaces/Achievements/index.html) data to the OSS EOS plugin. |
| Use Crossplay Sessions | This setting is required to play cross-platform network games. It also makes the EOS [Sessions Interface](https://dev.epicgames.com/docs/services/API/Interfaces/Sessions/index.html) the primary session interface. |
| Mirror Presence to EAS | This option determines whether the EOS Plus plugin will also send [Presence](https://dev.epicgames.com/docs/services/API/Interfaces/Presence/index.html) data to the OSS EOS plugin. Presence data is only available when using Epic Account Services. |

#### Engine Configuration for the EOS Plugins

Once you have set up your product on the Developer Portal and configured the plugins, there are a few settings you need to configure. You can configure these plugins in the engine configuration hierarchy, such as `DefaultEngine.ini`.

##### OSS EOS Configuration Settings

Add the following configuration settings to your project's `DefaultEngine.ini` file:

1. Check that the Online Subsystem EOS plugin is enabled for use in your project.
2. Set EOS as the default platform for your project's online services.
3. Specify the net drivers.
4. Use EOS' peer-to-peer socket functionality for player hosted matches. This setting is optional.

The following is all the configuration settings described above for OSS EOS:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[OnlineSubsystemEOS]\n\tbEnabled=true\n\n\t[OnlineSubsystem]\n\tDefaultPlatformService=EOS\n\n\t[/Script/Engine.Engine]\n\t!NetDriverDefinitions=ClearArray\n\t+NetDriverDefinitions=(DefName=&quot;GameNetDriver&quot;,DriverClassName=&quot;/Script/SocketSubsystemEOS.NetDriverEOSBase&quot;,DriverClassNameFallback=&quot;/Script/OnlineSubsystemUtils.IpNetDriver&quot;)\n\t+NetDriverDefinitions=(DefName=&quot;DemoNetDriver&quot;,DriverClassName=&quot;/Script/Engine.DemoNetDriver&quot;,DriverClassNameFallback=&quot;/Script/Engine.DemoNetDriver&quot;)\n",
  "lines_of_code": 13,
  "id": 35001,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTAwMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjAyKzAwOjAwIn0=--67e1a2b65ff3b1f7690f0475cf5d92e11ed2d18e0205c0b85412defb243df739",
  "settings": {
    "is_hidden": false
  }
}
```

###### Launching a Title from the Epic Games Launcher

If you are launching your title from the Epic Games Launcher, you need to add configuration entries in the Engine configuration file hierarchy for all Epic App and Epic Sandbox pairs that the Epic Games Store (EGS) launches. Ensure the **Default Artifact Name** and the **Artifact Name** in your project settings or engine configuration matches the Artifact Name in your Epic Online Services Developer Portal.

When you ship a title on EGS, the Default Artifact Name is ignored. EGS always passes an `-epicapp` command-line argument that it uses instead. The Default Artifact Name is useful when shipping on other storefronts where `-epicapp` is not passed.

##### EOS Plus Configuration Settings

If you want to configure your project to implement crossplay between EOS and another online platform, add the following configuration settings to your project's `DefaultEngine.ini` file:

1. Check that the Online Subsystem EOS Plus plugin is enabled for use in your project. Recall that the EOS Plus plugin lets you use EOS in conjunction with a different online service.
2. Change your default platform online services to EOS Plus. This tells the engine that you are using EOS in conjunction with a different platform service. Also, add the additional native platform online services you want to use. In this example, it is set to Steam, but it can be any online service, including console online services.
3. Communicate what Net ID types are compatible with the default OSS. This only needs to be set when EOS/EOS Plus is the default OSS.
4. Support communication between both EOS and EOS Plus clients. For example, consider the scenario where you have an EOS Plus player logged in with another online platform, such as Steam, hosting an EOS Session and an EOS (not EOS Plus) client joins the former's EOS Session. The pure EOS client needs this mapping so that EOS Plus Net Ids are correctly routed to EOS and deserialized as EOS Net Ids. This `MappedUniqueNetIdTypes` configuration is added to the same configuration section as the configuration from the previous step.

The following is all the configuration settings described above for EOS Plus:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[OnlineSubsystemEOSPlus]\n\tbEnabled=true\n\n\t[OnlineSubsystem]\n\tDefaultPlatformService=EOSPlus\n\tNativePlatformService=Steam\n\n\t[/Script/OnlineSubsystemUtils.OnlineEngineInterfaceImpl]\n\t+CompatibleUniqueNetIdTypes=EOS\n\t+CompatibleUniqueNetIdTypes=EOSPlus\n",
  "lines_of_code": 11,
  "id": 35006,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTAwNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjAyKzAwOjAwIn0=--630fac4392f165bd000592085ec074b649ad5a11573b207b2abcbbc8aab10987",
  "settings": {
    "is_hidden": false
  }
}
```

## How OSS EOS Finds Artifacts

To choose the particular artifact to use for OSS EOS at startup, you can specify a number of settings through the Unreal Engine command-line to find an artifact specified in engine configuration or default to a particular artifact. As of UE 5.5, whatever is passed on the command-line as the Sandbox ID and Deployment ID (passed via `-epicsandboxid` and `-epicdeploymentid` arguments) are always used. Previously, these values were only used to look up matching entries in the Artifacts configuration array. No matter what Artifact entry is found in the configuration array, the command-line Sandbox and Deployment IDs are always used.

This behavior is outline in the following sequence of steps:

1. In descending order of preference, define `ArtifactName` as the value of: `-EOSArtifactNameOverride=<...>` `-EpicApp=<...>` `DefaultArtifactName` from engine configuration
2. In descending order of preference, define `SandboxId` as the value of: `-EpicSandboxIdOverride=<...>` `-EpicSandboxId=<...>` Not specified
3. In descending order of preference, define `DeploymentId` as the value of: `-EpicDeploymentIdOverride=<...>` `-EpicDeploymentId=<...>` Not specified
4. If `SandboxId` and `DeploymentId` are specified, search for an artifact that matches all of `ArtifactName`, `SandboxId`, and `DeploymentId`.
5. If Step 4 fails or is not run, but `SandboxId` is specified, search for an artifact that matches `ArtifactName` and `SandboxId`.
6. If Step 5 fails or is not run, search for an artifact that matches `ArtifactName`.
7. If Step 6 fails, search for an artifact with an empty `ArtifactName`.
8. If Step 7 fails, report an error as no artifact is found.
9. Once an artifact is found: In descending order of preference, use the following for `SandboxId`: If specified, the value from Step 2. The value from the artifact entry found from one of Steps 4-7. In descending order of preference, use the following for `DeploymentId`: If specified, the value from Step 3. The value from the artifact entry found from one of Steps 4-7.

You can provide specific artifact entries in the configuration artifacts array for specific combinations of `ArtifactName`, `SandboxId`, and `DeploymentId`. This is useful if you want to vary the `ClientId` and/or `EncryptionKey` for each combination. On the other hand, if you want to set a `ClientId` that you always want to use, you can provide a single artifact entry in the configuration artifacts array with an empty `ArtifactName`. This forces the behavior above to always use the artifact with the empty artifact name.

## Login

There are two methods to start the login process in the Online Identity Interface:

- **Auto Login**: Requires you to pass a local user number.
- **Login**: Requires you to use an `FOnlineAccountCredentials` object.

The next section describes how to log a user in using either Auto Login or Login in OSS EOS.

### Login with OSS EOS

In addition to providing a valid local user number, the Login method requires you to pass a `FOnlineAccountCredentials` object. This class has three fields:

- Type
- Id
- Token

#### Login Methods

These three fields indicate which method of authentication the OSS EOS should use, depending on their values. The following sections provide examples of how to set up each of the different types of authentication available:

- Account Portal
- Developer
- Exchange Code

##### Account Portal

- Type: `AccountPortal`
- Id:
- Token:

Account Portal is the most general-purpose method for login as it does not require the **EOS Developer Authentication Tool (Dev Auth Tool)**, nor does it require your application to be launched from the Epic Games Launcher.

With this method, if you are using EOS SDK version 1.15 or later, a game overlay UI appears when the Login call is made. If the game overlay is not enabled, a browser window opens. The user needs to enter their Epic Account information when prompted. If the user is already logged in to Epic Games, the user must accept the access scopes for the product in question.

Since credentials are provided by the user either in the game overlay UI or in the browser, you do not need to provide an Id or Token.

##### Developer

- Type: `Developer`
- Id: `localhost:<PORT>` `PORT` is the port specified in Dev Auth Tool
- Token: `<CREDENTIALS_NAME>` `CREDENTIALS_NAME` is specified in Dev Auth Tool

Developer is the recommended method for development with OSS EOS on desktop platforms. This method requires the Dev Auth Tool to be running. See the following documentation on the Epic Online Services site for more information about the [Developer Authentication Tool.](https://dev.epicgames.com/docs/services/en-US/EpicAccountServices/DeveloperAuthenticationTool/index.html)

After you set up the Dev Auth Tool, remember which Port and Credentials Name you use since they are required to fill the `Id` and `Token` fields of the `FOnlineAccountCredentials` object as indicated above. This login method opens when the Login call is made, and the user is asked to input their Epic Games account information. If the user is already logged in to Epic Games, the user must accept the access scopes for the product in question. This step only occurs the first time a user logs in.

##### Exchange Code

- Type: `ExchangeCode`
- Id:
- Token: `<EXCHANGE_CODE>` `<EXCHANGE_CODE>` is provided by the Epic Games Launcher

You should only use the Exchange Code method if your application is launched from the Epic Games Launcher, as it requires the exchange code provided by the Launcher. This method does not require Dev Auth Tool to be running and is what you should use with the shipping version of your game.

Since the Epic Games Launcher provides an exchange code token, you do not need to provide an Id or Token.

#### Login Success

If any of these methods are completed successfully, the login process ends by registering all necessary EOS notification services (login status, friends, presence updates, and auth refresh) and triggering the following registered delegates:

- `OnLoginComplete`: parameters include whether the login was successful and the `UniqueNetId` of the newly authenticated user.
- `OnLoginStatusChanged`: parameters correspond with the previous and current login status and the `UniqueNetId` of the newly authenticated user.

### Auto Login with OSS EOS

To use Auto Login with Online Subsystem EOS, you must pass additional command-line arguments to your game's executable upon startup. These arguments correspond to the three fields in the `FOnlineAccountCredentials` object otherwise passed to the Login method.

The parameters from the login above correspond to command-line arguments as follows:

| FOnlineAccountCredentials Variable | Command-Line Argument |
| --- | --- |
| `Type` | `AUTH_TYPE` |
| `Id` | `AUTH_LOGIN` |
| `Token` | `AUTH_PASSWORD` |

#### Login Methods

This section contains examples of the parameters needed for all three login methods as explained in the previous section.

##### Account Portal

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "-AUTH_TYPE=&quot;accountportal&quot;",
  "lines_of_code": 1,
  "id": 35007,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTAwNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjAyKzAwOjAwIn0=--f3d20b23374c393473d50aba5ec7334001c323082cae289bf685095728ed753d",
  "settings": {
    "is_hidden": false
  }
}
```

##### Developer

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "-AUTH_TYPE=&quot;developer&quot; -AUTH_LOGIN=&quot;localhost:&lt;PORT&gt;&quot; -AUTH_PASSWORD=&quot;&lt;NAME_IN_DEV_AUTH_TOOL&gt;&quot;",
  "lines_of_code": 1,
  "id": 35008,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTAwOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjAyKzAwOjAwIn0=--9c6dad99b033b104bcea23814709ce6531decdeb562c5692eaa99881c72f0f57",
  "settings": {
    "is_hidden": false
  }
}
```

The arguments in this command are:

- `<PORT>` is the port you configured in the Dev Auth Tool.
- `<NAME_IN_DEV_AUTH_TOOL>` is the credentials name you chose in the Dev Auth Tool.

##### Exchange Code

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "-AUTH_TYPE=&quot;exchangecode&quot; -AUTH_PASSWORD=&quot;&lt;EXCHANGE_CODE_FROM_LAUNCHER&gt;&quot;",
  "lines_of_code": 1,
  "id": 35009,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTAwOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjAyKzAwOjAwIn0=--c30e77c92dbb34ce07904e894b1b933c5c8a57c50179703dd2d808e568ef8afc",
  "settings": {
    "is_hidden": false
  }
}
```

The arguments in this command are::

- `<EXCHANGE_CODE_FROM_LAUNCHER>` is the exchange code from the Epic Games Launcher.

### Login Flow with External Account Credentials

This section describes the login flow for OSS EOS with an external account. You must enable EOS Plus to log in with an external account.

If Epic Account Services and the Connect Interface (`EOS_Connect`) are both enabled, `EOS_Auth_Login` is called with the external account credentials for the non-EOS platform, such as Steam. If this login fails with an invalid user error (`EOS_InvalidUser`), `EOS_Auth_LinkAccount` is called. This call prompts the user to log in to their Epic Games account through a web browser or user interface overlay. This login links the user's Epic Games account to their external, non-EOS account.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "See <a data-document-id=\"3228276\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine\">Known Issues</a> below for more information about the account linking process.",
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

If Epic Account Services is not enabled, but the Connect Interface is enabled, `EOS_Connect_Login` is called with the external account credentials.

Identity Provider configuration is required for both the Auth Interface (`EOS_Auth`) and Connect Interface. To use your desired external platform, add it to the Identity Providers list in the EOS Project Developer Portal. If you have properly configured your platforms in the Identity Provider, EOS authentication should complete successfully and unlock access to all EOS game features. For more information, see the Epic Developer Resources documentation about [Identity Provider Management](https://dev.epicgames.com/docs/dev-portal/identity-provider-management).

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "EOS Plus must be enabled in order to use external account login.",
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

#### Using Epic Account Services

If this setting is enabled, the login process continues as if Using Cross Platform User IDs were enabled too. The external authentication token is added to the set of credentials needed for the login method, and EOS attempts to authenticate by calling the `EOS_Auth_Login` method.

## Interfaces

This section provides additional information about the interfaces implemented in the Online Subsystem EOS plugin. For more detailed information about each of these interfaces, see the Online Subsystem documentation. The OSS EOS plugin supports the following EOS SDK interfaces:

### Supported Interfaces

| OSS EOS Interface | EOS SDK Interface | Description |
| --- | --- | --- |
| [Achievements](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-achievements-interface-in-unreal-engine) | [Achievements](https://dev.epicgames.com/docs/game-services/achievements) | Unlock and check the status of user achievements. |
| [Store](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-store-interface-in-unreal-engine?application_version=5.5), [Purchase](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-purchase-interface-in-unreal-engine) | [Ecom](https://dev.epicgames.com/docs/epic-games-store/services/ecom/ecom-overview) | Purchase items and verify ownership of those items. |
| [External UI](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-external-ui-interface-in-unreal-engine) | [UI](https://dev.epicgames.com/docs/epic-account-services/eosui-interface) | Display user interface overlay. |
| [Identity](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-identity-interface-in-unreal-engine?application_version=5.5) | [Auth](https://dev.epicgames.com/docs/epic-account-services/auth/auth-interface) | Verify user accounts, including login and logout. |
| [Leaderboards](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-leaderboard-interface-in-unreal-engine) | [Leaderboards](https://dev.epicgames.com/docs/game-services/leaderboards) | Create and retrieve leaderboards. |
| [Presence](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-presence-interface-in-unreal-engine) | [Presence](https://dev.epicgames.com/docs/epic-account-services/eos-presence-interface) | Inform friends of current activities. |
| [Sessions](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-session-interface-in-unreal-engine) | [Sessions](https://dev.epicgames.com/docs/game-services/sessions) | Manage session-based matchmaking. |
| [Friends](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-friends-interface-in-unreal-engine?application_version=5.5) | [Friends](https://dev.epicgames.com/docs/epic-account-services/eos-friends-interface) | Add or remove players from friends list. Retrieve friends list. |
| Stats | [Stats](https://dev.epicgames.com/docs/game-services/eos-stats-interface) | Ingest and query user stats. |
| Title File | [Title Storage](https://dev.epicgames.com/docs/game-services/title-storage) | Download encrypted title data from the cloud. |
| [User Cloud](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-user-interface-in-unreal-engine) | [User Info](https://dev.epicgames.com/docs/epic-account-services/eos-user-info-interface) | Access user display information. |

#### Sessions

##### Bucket Id

In OSS EOS Sessions, `BucketId` is top-level, game-specific filtering information for session searches. For more information about the Sessions `BucketId`, see the EOS documentation about [Sessions](https://dev.epicgames.com/docs/game-services/sessions).

`BucketId` can be set to anything your project needs by using a custom attribute added to `FOnlineSessionSettings::Settings`. To do this, add the following to your project code:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "SessionSettings.Settings.Add(OSSEOS_BUCKET_ID_ATTRIBUTE_KEY, FOnlineSessionSetting(FString(TEXT(&quot;BUCKET_ID_PLACEHOLDER&quot;)), EOnlineDataAdvertisementType::ViaOnlineService));",
  "lines_of_code": 1,
  "id": 35010,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTAxMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjAyKzAwOjAwIn0=--3fac4051a3ff719e5a3370be93a7ba0e0edc8405fe353e3dddd6cacc547f9459",
  "settings": {
    "is_hidden": false
  }
}
```

where:

- `BUCKET_ID_PLACEHOLDER` is the Bucket Id you want to use.

This custom `BucketId` also needs to be added to any session search parameters in a similar way.

#### Stats

##### Stat Names

OSS EOS converts all stat names to uppercase before passing them to EOS. When you configure your project in the EOS Developer Portal, make sure to configure stat names as uppercase names to ensure compatibility with OSS EOS.

## Known Issues

### Account Linking

At the moment, account linking during the login process is only available in the Steam platform, and attempting login on any other platform results in the following authentication error appearing in the log:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "LogEOSSDK: Warning: LogEOS: Error response received from backend. ServiceName=[OAuth], OperationName=[TokenGrant], Url=[&lt;Redacted&gt;], HttpStatus=[400], ErrorCode=[errors.com.epicgames.account.oauth.authorization_pending], NumericErrorCode=[1012], ErrorMessage=[The authorization server request is still pending as the end user has yet to visit and enter the verification code.], CorrId=[...]",
  "lines_of_code": 1,
  "id": 35011,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTAxMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjAyKzAwOjAwIn0=--f080ae3d0d7c7164a9867674de53158da3b2c13aa06d202b78b1c4b1643088b3",
  "settings": {
    "is_hidden": false
  }
}
```

This functionality will be available in other platforms in future releases. In the meantime, manual account linking can be done via the Accounts tab in the Connections section of the Epic Games [Account Settings.](https://www.epicgames.com/account/connections)

The Epic account used in the linking process needs to accept the application access scopes (as described in the section [Login with OSS EOS](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-eos-plugin-in-unreal-engine)), or this other error appears in the log:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "LogEOSSDK: Warning: LogEOS: Error response received from backend. ServiceName=[OAuth], OperationName=[TokenGrant], Url=[&lt;Redacted&gt;], HttpStatus=[400], ErrorCode=[errors.com.epicgames.oauth.scope_consent_required], NumericErrorCode=[58005], ErrorMessage=[The user has not consented to required scopes.], CorrId=[...]",
  "lines_of_code": 1,
  "id": 35012,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTAxMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjAyKzAwOjAwIn0=--f19090ce1a9d7c2e6a2e11cd53fb2c577a0f4f80aaafd4e9437a1ed25c63e1c9",
  "settings": {
    "is_hidden": false
  }
}
```

Once the account is linked, the access scopes are accepted, and, if the EOS authentication configuration is correct, login will complete successfully and the application will be able to use all of EAS' additional features.
