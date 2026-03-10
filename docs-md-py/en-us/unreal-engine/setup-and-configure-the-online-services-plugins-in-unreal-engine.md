# Setup and Configure the Online Services Plugins

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setup-and-configure-the-online-services-plugins-in-unreal-engine

> Application Version: 5.7

The **Online Services** plugins help you connect various backend online services such as Epic, Steam, Xbox Live, PSN, NLPN, and so on to your **Unreal Engine (UE)** project. This guide shows you how to:

- [Enable the Online Services plugins.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setup-and-configure-the-online-services-plugins-in-unreal-engine#enable-the-online-services-plugins)
- [Add the Online Services plugins to your project dependencies.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setup-and-configure-the-online-services-plugins-in-unreal-engine#add-the-online-services-plugins-to-project-dependencies)
- [Configure the default services for your project.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setup-and-configure-the-online-services-plugins-in-unreal-engine#configure-default-platform-services)

## Set Up Online Services Plugins

This walkthrough uses the Online Services Null implementation for illustrative purposes. This implementation does not connect to any backend online services and is used for testing purposes. This is a good starting point since the Online Services Null plugin does not require external registration or configuration in order to work with Unreal Engine. For a full list of services supported by the Online Services plugin, see the [Online Services Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5) documentation.

### Enable the Online Services Plugins

Various Online Services plugins are available to use in your project. The Online Services base plugin is enabled by default.

To enable additional required functionality, follow these steps:

1. Create or open an Unreal Engine C++ Project.
2. From the menu bar, navigate to **Edit > Plugins**. This opens a new window or tab titled **Plugins**. In this new window, search for "Online Services" or select the **Online Platform** category from the navigation bar on the left-side. A number of plugins should appear. One of these should be titled **Online Services Null**. Enable the **Online Services Null** plugin by checking the box. ![enable plugins](https://dev.epicgames.com/community/api/documentation/image/c554f683-3cad-45eb-a253-e2ecacc9a571) A message appears stating that "You must restart Unreal Editor for changes to take effect." Restart the **Unreal Editor** by clicking **Restart Now**. ![Image](https://dev.epicgames.com/community/api/documentation/image/f2ee7f12-f7c5-4d99-9c21-47999b0241e7)
3. You have now enabled the Online Services Null plugin in your project.

### Add the Online Services Plugins to Project Dependencies

To use the Online Services plugins in your project's C++ code, you mustadd the plugins to your project module as public dependencies.

To add the plugins to your project module's public dependencies, follow these steps:

1. Open your Unreal Engine C++ Project in the **Unreal Editor**.
2. Open Visual Studio by selecting **Tools > Open Visual Studio**. This opens your project's C++ source files in Visual Studio.
3. To use the C++ code provided by the Online Services plugins, you must add the `OnlineServicesInterface` module as public dependencies to your project's **.Build.cs** file.
4. Open your project's **.Build.cs** file from the **Solution Explorer** by navigating to **Games > [YOUR\_GAME] > Source > [YOUR\_GAME] > [YOUR\_GAME].Build.cs**.
5. Add `OnlineServicesInterface` and `CoreOnline` to your `.Build.cs` public dependencies. Your `.Build.cs` file should look like this:
6. Save your changes in Visual Studio.

### Generate Project Files

Since you made a change to your project's **.Build.cs** file, you need to refresh your Visual Studio project files. This ensures that the changes you made are reflected in Visual Studio Intellisense and lets you use the functionality in the plugins that you just added.

To generate project files, follow these steps:

1. Close Visual Studio.
2. Navigate back to your open project in the Unreal Editor.
3. Regenerate your Visual Studio project files by selecting **Tools > Refresh Visual Studio Project**.

A progress bar appears, displaying the status of the updates to your code project and disappears when the process is complete.

## Configure Default Platform Services

The last step is to specify your default platform services for the Online Services plugins. The default platform services specify which backend platform services are returned by a call to `UE::Online::GetServices`. A list of available platform identifiers is given on the [Overview of Online Services](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5) documentation page.

To specify Online Services Null as the default platform services, follow these steps:

1. Open your project in Visual Studio. You can do this by navigating to **Tools > Open Visual Studio** from within the Unreal Editor.
2. Open your project's **DefaultEngine.ini** file in the Visual Studio Solution Explorer by navigating to **Games > [YOUR\_GAME] > Config > DefaultEngine.ini**.
3. Add the following to your project's **DefaultEngine.ini** file:

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Online Services Null is an online services implementation that does not use any backend online services. This is used for testing and debugging your online services implementation without a backend service. If you want to use a different backend online service as your project's default online services, you can choose one from the list provided in the <a data-anchor-id=\"18364\" data-document-id=\"3228125\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#configuration\">Configuration</a> section of the <a data-document-id=\"3228125\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5\">Online Services Overview</a>.",
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

## Access Online Services in Your Project

The Online Services plugins are now enabled and configured for use in your project. To access the Online Services plugin and its various interfaces, follow these steps:

1. Add `#include "Online/OnlineServices.h"` to the file where you want to access the Online Services plugin.
2. Obtain a pointer to the default platform services with `IOnlineServicesPtr OnlineServicesPtr = UE::Online::GetServices();`.

Now you can access the different Online Services plugin interface functionalities. For example, to access the [Auth Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/auth-interface-in-unreal-engine?application_version=5.5), follow these steps:

1. Make sure you have first obtained a pointer to the default platform services.
2. Add `#include "Online/Auth.h"` to the file where you want to access the Auth interface.
3. Obtain a pointer to the Auth interface with `IAuthPtr AuthPtr = OnlineServicesPtr->GetAuthInterface();`.

Now you can access the functionality of the Auth interface through the Auth interface pointer. The same logic works for all other Online Services interfaces.

![Image](https://dev.epicgames.com/community/api/documentation/image/cf9f909c-8d95-4ae8-b22c-d5572b34444d)
