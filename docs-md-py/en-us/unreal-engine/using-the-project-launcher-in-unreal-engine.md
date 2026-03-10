# Project Launcher

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-project-launcher-in-unreal-engine

> Application Version: 5.7

The Project Launcher is used to cook and deploy builds of your projects to specified platforms for testing, debugging, and releasing your project. The following reference page breaks down the elements that make up the Project Launcher and the settings you can use when creating your own Custom Launch Profiles for deploying your content to different platforms.

![Project Launcher UI](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f3bf514-db3b-4172-bd7c-3cef47ae4341/ue5_1-01-project-launcher-ui.png "Project Launcher UI")

## Project Launcher interface

To open the Project Launcher click **Platform** and select **Project Launcher**.

![Open the Project Launcher window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eec81b0f-85d2-41cc-95a0-a046a3c55e7d/ue5_1-02-open-project-launcher.png "Open the Project Launcher window")

The Project Launcher interface can be broken up into two main areas:

![Project Launcher UI description](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ba952ee-187d-40af-8d74-a843fa0995c9/ue5_1-03-project-launcher-ui-description.png "Project Launcher UI description")

1. Default Launch Profiles
2. Custom Launch Profiles

From the **Default Launch Profiles** window, you can see the available platforms and select from the devices that you want to deploy builds to. At the top of this window, you can specify a **Project** (if it's different than the current one you have opened) and a toggle for **Advanced** settings for these default launch profiles.

When you click the **Advanced** toggle button, you'll get additional options next to the default launch profiles that enables you to select a **Build Configuration** and a **Cook** method.

![Advance options in the Project Launcher](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d00a66a3-cd69-4ad6-b2b9-f9d81de1cc0a/ue5_1-04-project-launcher-advance.png "Advance options in the Project Launcher")

In the **Custom Launch Profiles** window, you can create your own profiles that enable you to specify many more options for how content is built and deployed, which is detailed more in the [Custom Launch Profiles](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-project-launcher-in-unreal-engine#customlaunchprofiles) section.

## Custom Launch Profiles

From the Project Launcher, you can create a **Custom Launch Profile** that can be used with all platforms or even specific ones, like the Nintendo Switch. These profiles enable you to build your content in specific ways by setting how it is cooked, packaged, and even deployed using the available build operations.

To add your own Custom Launch Profile, click the **+Add** button in the **Custom Launch Profiles** section.

![Add a Custom Launch Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f8084f2-073b-4b20-9f63-4842093a1d55/ue5_1-05-add-custom-profiles.png "Add a Custom Launch Profile")

After doing so, your Custom Launcher Profile will immediately open. Be sure to give it a name so that you can identify it later on.

![Custom Launch Profile editor window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d075662-fb4a-4b99-bed3-29af575d174c/ue5_1-06-custom-launch-profile-editor.png "Custom Launch Profile editor window")

### Name and Description

In the header bar, you'll find the **Name** and **Description** that you can apply to this custom profile. To edit these, double-click on either section's text to start editing them.

![Editing of the name and description of the Custom Launcher Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc7746a1-2231-494c-8bfe-a484d1f72776/ue5_1-07-editing-name-description.png "Editing of the name and description of the Custom Launcher Profile")

### Project

In the **Project** section, you can specify what project you want this profile to be associated with or if it can be used with any project. By default **Any Project** is set, but it can be set to a specific one. This can be useful when you are developing your project for multiple platforms, and those platforms require particular ways to deploy, test, debug, and even release them.

![Specify project for the Custom Launch Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76ba935b-5fae-4d8d-847c-47f6045ffd7f/ue5_1-08-specify-project.png "Specify project for the Custom Launch Profile")

### Build

The **Build** section enables you to specify the type of configuration you want to build and deploy against depending on your project's progression in development and how you need to test, debug, or release your project.

![Build section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5351c169-c493-4c6a-8e9b-ee1b1f7a8a74/ue5_1-09-build-section.png "Build section")

| Setting | Description |
| --- | --- |
| **Build Configuration** | Choose from the available configurations you want to build and test with your project. Settings of the Build Configuration  * **DebugGame**: This configuration builds the Engine as optimized but leaves the game code debuggable. It is ideal only for debugging game modules. * **Development**: This configuration is equivalent to a release build. Unreal Editor uses the Development configuration by default. When your project is compiled using this configuration, it enables you to see code changes made to your project reflected in the Editor. * **Shipping**: This is the configuration for optimal performance and shipping your game. This configuration strips out console commands, stats, and profiling tools. This configuration should be used when you are ready to release your game. |
| **Build UAT** | When enabled, the [Unreal Automation Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine) will be built as part of the build. |
| **Additional Command Line Parameters** | Parameters specified here will be passed to the app on launch |

### Cook

In the **Cook** section, there are two ways you can cook content for your projects: **By the book** and **On the fly**.

#### By the Book

The Cook **By the book** option enables you to specify which content should be cooked and cooks everything in advance before launching the game.

![Cook By the Book option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c48f6ef0-99b6-4d0d-94b6-9410baf8de24/ue5_1-11-cook-by-the-book.png "Cook By the Book option")
