# Install Unreal Engine

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine

> Application Version: 5.7

This tutorial describes how to download and install **Unreal Engine** (UE). To uninstall or make changes to Unreal Engine after you install, see [Make Changes to an Unreal Engine Installation](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#make-changes-to-an-unreal-engine-installation).

## Hardware and Software Requirements

To determine if your hardware and software are compatible with Unreal Engine and the **Epic Games Launcher**, see [Hardware and Software Specifications](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-specifications-for-unreal-engine?application_version=5.6).

### Additional Software

To install Unreal Engine, you only need the Epic Games Launcher. However, developing with Unreal Engine can require additional software depending on your development role and criteria. Additional software can include:

- Microsoft Visual Studio
- Mobile platform Software Development Kits (SDKs) for iOS and Android
- Console platform SDKs
- Third-Party Debugging Tools

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Developing and packaging for consoles requires a source code build of the Unreal Engine and cannot use the pre-compiled version obtained through the Epic Games Launcher. You can download a source code build from <a href=\"https://www.unrealengine.com/en-US/ue-on-github\">GitHub</a>, but this guide does not cover this method.",
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

## Download and Install the Epic Games Launcher

The Epic Games Launcher is where you download and manage your Unreal Engine versions. The launcher also gives you access to the [Epic Games Store](https://store.epicgames.com/en-US/), sample projects, and professional development tools such as [Fab](https://www.fab.com/), [Twinmotion](https://www.twinmotion.com/en-US), and [RealityCapture](https://www.capturingreality.com/).

To download and install the Epic Games Launcher, follow these steps:

1. Access the [Download Unreal Engine](https://www.unrealengine.com/en-US/download) page.
2. Click the **Download Launcher** button to download the installer file. Alternatively, you can click the **Download** button in the top-right corner of the page. ![Epic Games Launcher Download Page](https://dev.epicgames.com/community/api/documentation/image/8ebe4e86-a5d8-4771-a8af-214278d453f5)
3. After the download is complete, execute the **installer file** to run the Setup Wizard.
4. Once the Setup Wizard is complete, open the **Epic Games Launcher**.

### Sign In to the Epic Games Launcher

Once the Epic Games Launcher is open, you’ll be prompted to sign in using an Epic Games account. You can [sign in with an existing Epic Games account](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#sign-in-with-an-existing-epic-games-account) or [create an Epic Games account](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#create-an-epic-games-account).

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You must be signed in to download Unreal Engine. If you click <b>sign in later</b>, you cannot download the engine.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26031859,
      "caption": "",
      "alt_text": "Epic Games Launcher Sign In Later",
      "image": {
        "id": 26031859,
        "file_name": "epic-games-launcher-sign-in-later.png",
        "file_size": 15507,
        "content_type": "image/png",
        "created_at": "2025-09-02T22:08:41.359+00:00",
        "height": 170,
        "width": 600,
        "storage_key": "cb8a3f9f-a8a5-454c-bdbe-1ecde9ac8fad",
        "context": "documentation"
      },
      "storage_key": "cb8a3f9f-a8a5-454c-bdbe-1ecde9ac8fad",
      "context": "documentation",
      "width": 600,
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

#### Sign In with an Existing Epic Games Account

If you already have an Epic Games account, sign in using one of the following methods:

- Enter your email address and password into the text fields. Then, click **Sign In**. ![Epic Games Launcher Sign In With Existing Account](https://dev.epicgames.com/community/api/documentation/image/efb33e57-28b9-4e63-a8ba-fdc23c06a100)
- Select a supported third-party social media or gaming platform account. ![Epic Games Launcher Sign In With Third-Party Platform](https://dev.epicgames.com/community/api/documentation/image/658f8b51-9bdf-4fc2-92f5-5cb2e6a12164)

#### Create an Epic Games Account

If you don’t have an Epic Games account, follow these steps to create one:

1. Click **Create account**. Follow the on-screen prompts to fill in your date of birth, email, name, and other relevant information. ![Epic Games Launcher Create Account](https://dev.epicgames.com/community/api/documentation/image/3cd20c1d-2575-45bb-b569-939b74494410)
2. Once you’ve entered your information, check the box next to **Terms of Service** and the **Epic Games Store End User License Agreement** to accept these policies. Click **Continue**. ![Epic Games Launcher TOS And EULA](https://dev.epicgames.com/community/api/documentation/image/8dd4f790-456f-44ef-87bf-c9ebe91ebe82)
3. Verify your email by entering the numeric code sent to your email address. Then click **Verify email**. ![Epic Games Launcher Verify Email](https://dev.epicgames.com/community/api/documentation/image/8b8f11e6-1f1b-4957-a1b6-41f8cbef6245)
4. Review the **Epic Games Privacy Policy** and click **Continue**. ![Epic Games Launcher Privacy Policy](https://dev.epicgames.com/community/api/documentation/image/58a032f1-9423-4a6f-bc1f-da0a45b86f58) Once logged in, by default, the Epic Games Launcher lands on the **Unreal Engine** option in the left-hand navigation panel and displays the **News** tab. ![Image](https://dev.epicgames.com/community/api/documentation/image/2b1b16f5-366a-49d4-9366-50ba8ced286a)

### Install and Run Unreal Engine

To install the latest version of Unreal Engine, follow these steps:

1. In the Epic Games Launcher, click **Unreal Engine** in the left-hand navigation panel. This displays tabs relevant to Unreal Engine. ![Epic Games Launcher Unreal Engine Tabs](https://dev.epicgames.com/community/api/documentation/image/0ebeca21-3b20-4b57-a381-238697d705c6)
2. Click the **Library** tab. This is where you install and manage versions of Unreal Engine. ![Epic Games Launcher Library Tab](https://dev.epicgames.com/community/api/documentation/image/623375b1-de3c-4497-98ee-7c174e5a9066)
3. Click the **Add (+)** button next to **ENGINE VERSIONS** to add a new engine tile. This tile indicates which version of the engine will be installed. ![Epic Games Launcher Add Engine Tile](https://dev.epicgames.com/community/api/documentation/image/08db1d6d-3179-4ddd-b45a-83d591085701)
4. By default, the latest version of Unreal Engine is displayed on an engine tile. If you want to use an older version of the engine, click the version number dropdown menu and select the version you want to install from the list. ![Epic Games Launcher Engine Version Number](https://dev.epicgames.com/community/api/documentation/image/0ea5eefe-70ae-47a8-b2dd-aa34e5c2a1c8)
5. On the engine tile, click **Install**. In the new dialog, review the terms and licensing options: Read through the **Unreal Engine Pricing options**. Click **Accept** to proceed. Read through the **Unreal Engine End User License Agreement**. Check the checkbox to indicate that you’ve read and agree with the terms. Click **Accept** to proceed.
6. To choose where to install Unreal Engine on your hard drive, click **Browse** in the **Choose install location** dialog. By default, Unreal Engine uses the default installation location for your operating system. ![Epic Games Launcher Browse](https://dev.epicgames.com/community/api/documentation/image/e556c9fc-b497-4b7f-ae25-a688840adf88)
7. You can customize which Unreal Engine components to install by clicking **Options**. This opens the **Unreal Engine Installation Options** dialog. ![Epic Games Launcher Installation Options](https://dev.epicgames.com/community/api/documentation/image/fa07676d-754e-40e1-8c59-a1f8f2390ab4) Here you can choose which components suit your development needs. See the table below for descriptions of each component: After making your selection, click **Apply** to confirm.
8. In the **Choose install location** dialog, click **Install**. ![Epic Games Launcher Install](https://dev.epicgames.com/community/api/documentation/image/3dd6d23e-13d5-473a-b69c-03add938cc93)
9. After the installation is complete, run Unreal Engine by clicking **Launch** on the engine tile. Alternatively, you can use the quick launch button in the top-right corner of the Epic Games Launcher. ![Epic Games Launcher Launch Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/44f12004-90fe-4bb9-8cdf-d9a8758168ff)

#### Install Multiple Engine Versions

The Epic Games Launcher gives you access to each version of Unreal Engine dating back to Unreal Engine 4.0. This is useful because some projects or content may require specific versions of the engine.

Installing multiple versions of the engine follows the same steps as [Install and Run Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#install-and-run-unreal-engine):

1. Add a new engine tile by clicking the **Add (+)** button.
2. On the engine tile, click the version number dropdown menu and select the version you want to install from the list.
3. Click **Install** to begin the installation process.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can only have one of each engine version installed at a time.",
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

#### Install Unreal Engine Preview Builds

Prior to every major release of an Unreal Engine version, Epic Games issues a **Preview build**. Preview builds let you try out new features before they become available in major engine releases.

Because Preview builds are actively being developed, you may experience bugs or crashes while using them. For this reason, Preview builds are not intended for project development. However, they can be useful for determining if it’s worth moving development to an upcoming engine release, in order to take advantage of new features or avoid issues.

When a Preview build becomes available, it appears in the version number dropdown menu on an engine tile. Installing a Preview build follows the same steps as [Install and Run Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#install-and-run-unreal-engine).

![Epic Games Launcher Preview Builds](https://dev.epicgames.com/community/api/documentation/image/16adacad-bdb6-4708-b840-6bbfc5fa6804)

## Make Changes to an Unreal Engine Installation

The following sections describe how to verify, customize, update, and remove Unreal Engine after installation:

- [Verify an Unreal Engine Installation](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#verify-an-unreal-engine-installation)
- [Change the Components of an Unreal Engine Installation](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#change-the-components-of-an-unreal-engine-installation)
- [Apply HotFix Updates](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#apply-hot-fix-updates)
- [Install and Remove Plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#install-and-remove-plugins)
- [Uninstall Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine#uninstall-unreal-engine)

### Verify an Unreal Engine Installation

The Epic Games Launcher can “verify,” or evaluate existing engine files and plugins for corrupted or missing content.

In the Library tab of the Epic Games Launcher, the Verify option is located in the dropdown menu of each engine tile.

![Epic Games Launcher Verify](https://dev.epicgames.com/community/api/documentation/image/3f951ca6-1def-4687-be04-46a4fa86ddef)

After clicking Verify, you can see the progress of the verification by clicking **Downloads**, in the left-hand navigation panel.

![Epic Games Launcher Downloads](https://dev.epicgames.com/community/api/documentation/image/851cbc41-e4aa-402f-9a29-88ef5baaeb5b)

If any files are found to be missing or corrupted, only these files will be downloaded and installed.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The option to verify an Unreal Engine installation will not appear if a HotFix update is available but has not been downloaded and installed.",
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

### Change the Components of an Unreal Engine Installation

You can modify the components for each Unreal Engine version at any time, without redownloading the engine. This is useful if your development needs change after installation, such as requiring a different target platform or symbols for debugging.

To add or remove components from an existing version of Unreal Engine, follow these steps:

1. In the **Epic Games Launcher**, click the **Unreal Engine** tab. Then click the **Library** tab to view your installed Unreal Engine versions.
2. On the **engine tile** you want to make changes to, open the **dropdown menu**, and select **Options** to open the **Unreal Engine Installation Options** dialog. ![Epic Games Launcher Options](https://dev.epicgames.com/community/api/documentation/image/25064f12-4897-4b4e-807b-d16f474d689d)
3. In the **Unreal Engine Installation Options** dialog, check the components you want to add or remove.
4. Click **Apply** to confirm your choices.

### Apply HotFix Updates

An update for an engine version is called a **HotFix** update or release. A HotFix update is a targeted update consisting of bug and crash fixes to address critical issues. HotFix updates do not include new features for the engine.

You can identify a release that has had a HotFix update by looking at its third decimal value. In this example, 5.5.0 is the first release of this engine version, increasing by one for each new HotFix:

- 5.5.**0**
- 5.5.**1**
- 5.5.**2**

The release cadence for each HotFix update is determined by the amount of post-release issues to address and the severity of the issues.

When HotFix updates become available, the Epic Games Launcher notifies you in two ways:

- An info notification badge appears on the top-right corner of the engine tile with a HotFix.
- The engine tile’s **Launch** button is replaced with an **Update** button.

The Update button downloads the latest available updates and installs them.

![Epic Games Launcher Update](https://dev.epicgames.com/community/api/documentation/image/61752863-adb3-4744-9893-b8dc3d8b945e)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "We advise you to update your engine versions each time a HotFix becomes available. If you need to use your engine version without updating immediately, use the <b>Launch </b>button in the top-right corner of the Epic Games Launcher.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26031893,
      "caption": "",
      "alt_text": "Epic Games Launcher Quick Launch Button",
      "image": {
        "id": 26031893,
        "file_name": "epic-games-launcher-quick-launch-button.png",
        "file_size": 6027,
        "content_type": "image/png",
        "created_at": "2025-09-02T22:08:43.495+00:00",
        "height": 206,
        "width": 407,
        "storage_key": "c4f577c1-03dd-4fd2-bc65-2d9378c82644",
        "context": "documentation"
      },
      "storage_key": "c4f577c1-03dd-4fd2-bc65-2d9378c82644",
      "context": "documentation",
      "width": 300,
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

### Install and Remove Plugins

You can find and download plugins for Unreal Engine from the [Fab](http://www.fab.com/) marketplace. Plugins that are currently installed, or available to install can be found in the Epic Games Launcher by clicking **Unreal Engine > Library**, under the **Fab Library** section.

To install a plugin, follow these steps:

1. Locate the plugin you want to install in your **Fab Library**.
2. Click the **Install to Engine** button. ![Epic Games Launcher Plugins](https://dev.epicgames.com/community/api/documentation/image/932c4561-9fdc-493a-bd1e-0553f25182e5)
3. Select the Unreal Engine version to install the plugin for, if one exists. ![Epic Games Launcher Install Plugins](https://dev.epicgames.com/community/api/documentation/image/2199122e-d0c1-40bc-a0f9-e90d6a606d3f)
4. Click **Install** to queue the download.

You can check the download’s progress in the Epic Games Launcher under the Downloads category in the left-hand navigation panel.

![Epic Games Launcher Downloads](https://dev.epicgames.com/community/api/documentation/image/c02970e9-b506-4a81-b1d0-829201f8e9a0)

If there are no compatible versions of the engine installed, or if the plugin is already installed to all compatible versions, you will see the following warning dialogs:

![Epic Games Launcher Plugin Error 1](https://dev.epicgames.com/community/api/documentation/image/a268f260-be2c-4929-ac25-1e842b6addd4)

![Epic Games Launcher Plugin Error 2](https://dev.epicgames.com/community/api/documentation/image/c0c55414-022d-4b24-ba20-fdf1f9b9d1d3)

To inspect which plugins are currently installed on an engine version, click the **Installed Plugins** link under its engine tile.

![Epic Games Launcher Installed Plugins](https://dev.epicgames.com/community/api/documentation/image/d8141b38-a93c-4718-9e06-4dcc5f22dab2)

When you click Installed Plugins, the **Unreal Engine Plugins** dialog displays a list of installed plugins. To remove plugins for the selected engine version, click **Remove**.

![Epic Games Launcher Remove Plugins](https://dev.epicgames.com/community/api/documentation/image/395d377c-0c56-4bd1-b90e-18c7d9b3e89e)

### Uninstall Unreal Engine

To uninstall an existing version Unreal Engine, follow these steps:

1. In the **Epic Games Launcher**, click the **Unreal Engine** tab. Then click the **Library** tab to view your installed Unreal Engine versions.
2. On the **engine tile** you want to uninstall, open the dropdown menu, and select **Remove** to open the **Uninstall** dialog. ![Epic Games Launcher Remove Engine](https://dev.epicgames.com/community/api/documentation/image/69352b11-0162-4b3d-8c2c-25519a9771d7)
3. In the Uninstall dialog, click **Uninstall**. ![Epic Games Launcher Uninstall](https://dev.epicgames.com/community/api/documentation/image/88355f85-368c-4876-8544-8ad02a7aedf7)

## Next Up

- [Related Document](en-us/unreal-engine/install-unreal-engine.md)
