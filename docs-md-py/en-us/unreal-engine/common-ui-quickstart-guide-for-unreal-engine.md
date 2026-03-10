# Common UI Quickstart Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/common-ui-quickstart-guide-for-unreal-engine

> Application Version: 5.7

This page provides a walkthrough for how to set up **Common UI** in your project. You will learn the following in this guide:

* Setting up your viewport to support **Input Routing**.
* How to create **Input Action Data Tables**, which map controller buttons to actions within your UI.
* How to set up **Default Navigation Actions**, which support global click and back button functionality.
* How to create **Controller Data Assets** and assign them to specific types of controllers on specific platforms.

## 1. Viewport Input Routing Setup

The **Viewport** is the base for all input routing in Common UI. When Common UI captures input, it sends it to the Viewport first, which then sends it to whichever root node is drawn on top. To support this functionality, perform the following setup steps:

1. Open **Edit** > **Project Settings** > **Engine** > **General Settings**.
2. Set your **Game Viewport Client Class** to **CommonGameViewportClient**.

   ![Setting the viewport class to use Input Routing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7d3390c-3117-4a6c-8c2b-1130da4ea884/gameviewportclass.png)

If you need your own custom game viewport class, you will need to extend it from CommonGameViewportClient to use Common UI.

## 2. Creating an Input Action Data Table

Common UI uses Input Action Data Tables to create named actions that can be associated with various platform-specific inputs. For examples, see **GenericInputActionDataTable** in Common UI's content folder, or **NavigationInputActionDataTable** in the Content Example project.

Common UI's Input Action Data Tables are not related to the input actions used in Project Settings or the Advanced Input System. They are exclusively used for managing UI input.

1. Right-click in the **Content Browser**, then click **Miscellaneous** > **Data Table Asset**.
2. Select **CommonInputActionDataBase** as your row structure, then click **OK** to create a new Input Action Data Table.

   ![Common Input Action Data Base as the row structure for a new data table](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/58125f9c-7fe6-4c63-8073-b910a25f50c1/inputactiondatarow.png)
3. To add a new Input Action row, click **Add** in the top bar.

   ![Click the Add button to add a row](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9693e53-50cb-470b-925f-0e7cfee3e9bc/addbutton.png)
4. Populate the Input Action with a name and information about which keys activate it.

Input Actions consist of the following parameters:

| **Parameter** | **Description** |
| --- | --- |
| **Display Name** | Name of input action. Displayed in Nav-bar if present. |
| **Hold Display Name** | Name of the input action if it requires the user to hold the button down. |
| **Nav Bar Priority** | Priority used when sorting actions in Nav-bar from left to right. |
| **Keyboard Input Type Info** | Key used for this action when using Mouse & Keyboard, if any. |
| **Default Gamepad Input Type Info** | Key used for this action when using Gamepad, if any. |
| **Gamepad Input Overrides** | Key used for this action on a *specific* gamepad. Useful for platform-specific button overrides, such as swapping the back and forward buttons for the gamepad on the Nintendo Switch. The A and B buttons on the Switch, switched |
| **Touch Input Type Info** | Key used for this action when using a touch interface, if any. |

Common UI widgets map these abstract actions to actual inputs. For example, you can add a data table and row name reference to the **Triggering Input Action** in the **CommonButtonBase** widget. After that, pressing the button associated with that action will activate the Common UI button.

![Defining the triggering input action for a Common UI button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/140b1fb8-f998-41c0-8249-b1c588c9c269/triggeringinputaction.png)
