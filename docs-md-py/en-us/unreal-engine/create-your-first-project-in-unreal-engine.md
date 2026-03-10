# Create your First Project in Unreal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/create-your-first-project-in-unreal-engine

> Application Version: 5.7

In this guide, you’ll learn how to launch an installed version of Unreal Engine, create a new project, use an existing project template, and how to download and install content from Fab.

## Launching Unreal Engine

Once you have downloaded and [installed Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine), the engine tile associated with that version will display the **Launch** button. Click the Launch button to open the engine and display the **Unreal Project Browser** window. In this window you can create a new project or open an existing project in your machine.

![Image](https://dev.epicgames.com/community/api/documentation/image/30f0f75e-9145-41a1-956d-a82680c5de39)

Alternatively, you can open an existing project directly by double clicking on the project tile under the **My Projects** section. This will open the project with its associated Unreal Engine version.

![Image](https://dev.epicgames.com/community/api/documentation/image/4956a2ed-c96d-4adc-b2e1-5bac85a4e4ce)

## Unreal Project Browser

The **Unreal Project Browser** window opens when you launch Unreal Engine. This window contains a list of your **Recent Projects**, as well as specific templates based on four main categories - **Games**, **Film / Video & Live Events**, **Automotive Product Design & Manufacturing**, and **Simulation**.

The Project Browser is divided into the following sections:

![Image](https://dev.epicgames.com/community/api/documentation/image/7158dc6a-ed8b-4968-bc3c-2724ab42b1e1)

| Number | Name | Description |
| --- | --- | --- |
| 1 | Recent Projects and Template Categories | This is a list of categories to filter through the available templates. |
| 2 | Templates for the selected Category | This is a list of templates available in a selected category. |
| 3 | Project Defaults | These settings can be changed to set the project defaults. Following selections can be made: **Blueprints or C++** can be used to choose whether to create a project using **Blueprint Visual Scripting** or **C++**. You can still add blueprints and C++ code to a project independent of this selection. **T****arget Platform** can be used to select a platform you want to build your project for. **Quality Preset** can be used to select the project’s visual fidelity. **Maximum** will turn on the high-end features, while **Scalable** balances the visual fidelity to optimize for performance. All settings can be toggled after the project is created. Starter Content can be enabled to include an additional content pack containing simple placeable meshes with materials and textures. The Starter Content can be added after creating the project too. To learn more about this, see the [Starter Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/starter-content-in-unreal-engine?application_version=5.1) page. |
| 4 | Project Creation Menu | These settings specify the **Project Location**, and **Project Name**. |

## Creating a Project with the First Person Template

The Games category has the following templates:

| Template Name |   |
| --- | --- |
| Blank | This template creates an empty project with no additional gameplay functionality. |
| First Person | This template features a first-person character Blueprint. It comes with a shooter and horror variant to demonstrate functionality common to those game types. |
| Third Person | This template features a third-person character Blueprint. It comes with a platformer and combat variants to demonstrate functionality typical of these popular third person game genres. |
| Top Down | This template features a top-down view of your character. It comes with a strategy and twin stick shooter variants. |
| Handheld AR | This template demonstrates common functionality found on handheld augmented reality projects. |
| Virtual Reality | This template demonstrates common functionality found on virtual realty projects. |
| Vehicle | This template comes with a drivable vehicle. It comes with a time trial and off-road variants. |

For this example,  select the **First Person** template. Pick **Blueprint** in the Project Defaults and enter your project location and name. Click **Create** to create your new project.

![Image](https://dev.epicgames.com/community/api/documentation/image/fedd2a2b-edb5-48f7-877f-af2d434f4a21)

Once Unreal Engine opens the project you will see the **Unreal Engine Level Editor** opened on the default template level. You can learn more about the editor by reading the [Unreal Editor Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-editor-interface) documentation.

You can navigate the level by holding down the **right mouse button (RMB)**, and using the **W**, **A**, **S**, and **D** keys. To learn more about navigating a level, see the [Viewport Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-controls-in-unreal-engine) page.

[Video: V_cPzYkN](https://dev.epicgames.com/community/api/cms/videos/V_cPzYkN/embed.html)

The project is currently running with high visual fidelity. When working on resource-intensive levels, you can lower the visual fidelity by clicking the **Performance and Scalability** button **> Viewport Scalability** and picking one of the lower tier **Scalability Groups**, such as Low or Medium.

[Video: V_Hd5dDC](https://dev.epicgames.com/community/api/cms/videos/V_Hd5dDC/embed.html)

To learn more about scalability options, see the Scalability Reference Scalability Reference page.

## Downloading Content from Fab

Fab is a marketplace where you can find a variety of content, including 3D models, materials, textures, sound files, and more. You can also download free sample projects created by Epic Games.

For this example, you will download the **Stack O Bot** sample project from Fab.

Go to [Fab](http://www.fab.com) and search for Stack O Bot to go to the product page.

![Image](https://dev.epicgames.com/community/api/documentation/image/b6f7fda0-44f3-4dc9-bc04-09352ef0afef)

On the product page click **Add to My Library** to add the sample project into your Fab library. Go back to the Epic Games Launcher, and go to **Unreal Engine > Library > Fab Library**. Click the **Refresh** button to refresh the list of content in your Fab library. You should now see the Stack O Bot sample.

[Video: V_PyYrRH](https://dev.epicgames.com/community/api/cms/videos/V_PyYrRH/embed.html)

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you haven't signed in to Fab on the website after creating your Epic Games account, Fab will require you to sign in before you can add content to your library.",
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

To learn more about creating projects with templates, see the [Projects and Templates](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine) page.
