# Remote Control Web Application

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-web-application-for-unreal-engine

> Application Version: 5.7

Parameters and functions exposed in the [Remote Control Preset](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-remote-control-presets-in-unreal-engine) can be connected to widgets in a companion web application provided by the **Remote Control Web Interface** plugin to control the engine remotely. This web application has a built-in UI editor so you can customize its interface without any additional code to create or format it.

![Remotely editing post process contrast using a widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffbdb74d-7eb6-418e-98c1-0ff43477a46d/rm-con-pst.gif)

Since this is a web application, you can run multiple clients at the same time. Any properties that are modified in one client will have their changes propagated through the web server to all the other clients. This can help create a collaborative workflow in a live environment.

This page covers how to connect exposed properties and functions to widgets in the companion Remote Control web application, and build your own UI with the application's UI builder.

## Prerequisites

The **Remote Control Web Interface** uses NodeJS to provide a companion web app with default widgets, such as gauges, sliders, and color pickers, for controlling the engine remotely without any additional code.

Follow these steps to connect the web application to your project:

1. [Install NodeJS](https://nodejs.org/en/download/) on your machine.

   1. Minimum version: 8.
   2. Maximum version: 14.15.5.
2. Open your project in the Unreal Editor.
3. In the Editor's main menu, choose **Edit > Plugins** to open the **Plugins** window.
4. In the **Plugins** window, find the **Remote Control Web Interface** plugin in the **Messaging** category. Check its **Enabled** checkbox.

   ![Remote Control web interface plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b4a19ec-c517-42c2-a7c8-5b048ef90403/01-rem-con-w-i.png)
5. Restart the engine.
6. Verify the web app launched successfully. In the Editor's main menu, choose **Window > Developer Tools > Output Log** and filter by "remote control web" to see a success log similar to: LogRemoteControlWebInterface:

   `[Success] Remote Control Web Interface is running - WebApp started, port: 7000`

   ![Success message displayed in the output log](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f190b852-3c89-4104-9fa4-305a060e7879/02-com-l.png)

## Getting Started with the Remote Control Web Application

Connect properties and functions in the Remote Control Panel to a web application. The web application will read any Remote Control Preset that you have open in your Unreal session. The following browsers are officially supported: Chrome, Firefox, and Safari.

To see updates in the Editor as you change property values in the web app, open **Edit > Editor Preferences** and, in the **Performance** section under **General**, disable **Use Less CPU when in Background**.

![Use Less CPU in the Background setting in the Editor Preferences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b7e7b437-7725-4173-847f-75b8fb6fd039/03-les-cpu.png)

Follow these steps to launch the web application and add an exposed property:

1. Open your web browser on the same machine running the engine and enter the URL 127.0.0.1:7000. See the Remote Control Quick Start for details on how to expose the Remote Control API to other machines.

   ![Enter the URL in your browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8edb4c80-5dfc-4b34-b3c0-f5d8e1e4551f/enter-url.png)


   You can change which port the **Remote Control Web Interface** uses for your project. In the Editor's main menu, choose **Edit > Project Settings…** to open the **Project Settings** window. In the **Project Settings** window, select **Remote Control** in the **Plugins** section to see its settings, where you can change the default port.

   ![Remote control web interface plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/003fe0fb-e2c8-4b4f-8cfb-3a2cc11737e7/05-rem-web-prt.png)


   You can also launch the web application from the **Remote Control Preset**. See [Remote Control Panel Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-panel-reference-for-unreal-engine#menu) for more details.
2. When the page loads, you should see a blank Remote Control application. Click the **Control** toggle in the web application to switch to **Design** mode so you can start adding widgets.

   ![Mode toggle in Control mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec139294-3323-48c0-af5e-da4d35085d77/mode-toggle-control.png)
   ![Mode toggle in Design mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2510801f-fe97-4cec-a4d2-a46800c4ca98/06-des-but.png)
3. Select the **Properties** tab.

   ![Remote control properties tab](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e12f83b0-80e8-41d6-bae6-298da1be72b5/07-prop-b.png)
4. Drag and drop one of the exposed properties into the right panel. When you add a property from the **Properties** panel, a **Panel Widget** is created if one doesn't currently exist, and the associated widget for the property is added to the Panel Widget.

   In the following example, a Panel Widget was created and a Color Picker Widget added to the Panel Widget. The Color Picker is bound to the **Contrast** field for the scene's **PostProcessVolume**.

   ![Color Picker Widget bound to Post Process Volume Contrast property](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59baf4e2-c6fe-4aa1-b1c1-336a1c6dca77/08-con-arr.png)
5. Switch to **Control** mode.

   ![Color Picker Widget in Control mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf53f39f-a4ee-4752-9514-8cc41071090b/09-con-web.png)
6. Modify the exposed property in the web app and verify the associated property is updated in the Editor.

   ![Remotely editing post process contrast using a widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e22ad17a-0893-42f9-a9ba-71792705be57/rm-con-pst.gif)
7. Save your changes to the web application by saving the corresponding Remote Control Preset in the Unreal Editor. The next time you open the web application, the layout will be the same as when you last saved the Asset.

## Presets

You can have multiple remote presets available in the web application, but you can only have one Remote Control Preset open at a time. In **Design** mode, go to the **Presets** section to see the available remote presets on the left side of the window and select the one you want to view. The name of the currently opened Remote Control Preset is displayed in the top right of the window.

![Multiple presets in the Remote Control window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/003ad56f-06b9-403b-b0c5-44033da1a9e4/10-1rem-pr.png)
