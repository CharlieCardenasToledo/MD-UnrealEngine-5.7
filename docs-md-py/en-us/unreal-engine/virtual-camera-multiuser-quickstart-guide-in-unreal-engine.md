# Virtual Camera Multi-User Quick-Start Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine

> Application Version: 5.7

You can use a **Multi-User** **Virtual Camera** (**VCam**) workspace to control and render Vcams in the same scene using multiple workstations. This lets multiple users simultaneously work on the same scene. **Multi-User Vcam** Multi-User Actor Replication feature, which is in beta.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Multi-User Vcam can only be used in Virtual Production projects.",
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

This document provides an example workflow, which you can use to set up a connected work environment that enables [multiple users](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine) to operate [VCams](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/VirtualCamera) in the same scene simultaneously.

#### Prerequisites

- Enable the **Multi-User Editing** [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/plugins-in-unreal-engine). In the **Menu Bar**, navigate to **Edit** > **Plugins**, and locate the **Multi-User Editing** plugin under the **Editor** section. Alternatively, you can use the **Search Bar**. After enabling the plugin, restart the editor.

![The Plugins window showing the Multi-User Plugin](https://dev.epicgames.com/community/api/documentation/image/07ed671d-613d-438f-a1f8-986732d2752f)

- You must have a functional **Virtual Production** project. If you do not have one, you can use the [Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine) project.
- You must have a **Multi-User Editor Server**. For more information, refer to the [Multi-User Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine).
- Your project must have a [Virtual Camera (VCam) Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine).

#### Launching an MU Session

Replication of a virtual camera between instances of Unreal Engine uses Multi-User Editing. All clients must be in a shared Multi-User (MU) session. For more information on joining an MU, session see [Multi-User Editing in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine)

#### Replicating a VCam Actor

When a VCam actor is added to the scene in an MU session, the actor is displayed in the editor on every client. This is because no client has declared that it is the author of the VCam’s properties.

To declare authorship over a VCam, tap or click the **Multi User** button in the lower left corner of the VCam. This disables the output providers and modifier stack evaluation on the other clients, which hides the HUD and ensures that this client determines the values used by the Vcam. Tapping again relinquishes authorship and enables the output providers, HUD, and modifiers on every client so that a new client can claim authorship.

![Image](https://dev.epicgames.com/community/api/documentation/image/45f97f85-93dc-43e6-97a4-c38d237e3d00)

#### Recording Remotely

To record a Virtual Camera on a machine other than its host machine, you must add its respective Record Camera (named [VCamActorName]\_Record) to [Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/record-gameplay-in-unreal-engine), rather than the VCamActor itself.

## Legacy Roles for MU

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The legacy Virtual Camera Multi-User workflows are deprecated, but still function in Unreal Engine 5.4.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This workflow does not support new, high-frequency replication",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This section provides an example workflow for using the legacy system for limited, low-frequency virtual camera operation in Multi-User mode.",
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

#### Prerequisites

- Enable the **Switchboard** [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/plugins-in-unreal-engine). In the **Menu Bar**, navigate to **Edit** > **Plugins** and locate the **Switchboard** plugin under the **Virtual Production** section. Alternatively, you can use the **Search Bar**. After enabling the Plugin, restart the editor.

![image alt text](https://dev.epicgames.com/community/api/documentation/image/5907e048-ebc1-4a55-9fcc-1798ff55093f)

You can access the Switchboard application using the Icon in the Unreal Engine Toolbar, after the plugin has been successfully installed.

![image alt text](https://dev.epicgames.com/community/api/documentation/image/45ae9f03-458a-4840-b403-7000c6511deb)

- You must have a functional **Virtual Production** project. If you do not have one, you can use the [Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine) project.
- You must have a **Multi-User Editor Server**. For more information, refer to the [Multi-User Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine).
- Your project must have a [Virtual Camera (VCam) Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine).

## Declare Virtual Production Roles

The **Switchboard** application requires each user to occupy a **VP Role**, such as an **Editor** or **Render**, to differentiate and identify which user is associated with which VCam Actor.

```json
{
  "type": "include",
  "excerpt_id": 2710,
  "excerpt_assignment_id": 2600,
  "blocks": [
    {
      "type": "enhanced_list",
      "style": "ordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "On your primary workstation in the Unreal Editor, navigate to the Toolbar, and select the <strong>VP Roles</strong>, then select (<strong>+</strong>) <strong>Add Role</strong> from the drop-down menu. Give the new role a name. In this workflow example the primary workstation is named Editor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 26354479,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 26354479,
              "file_name": "AddNewRole.png",
              "file_size": 10244,
              "content_type": "image/png",
              "created_at": "2025-12-18T15:10:29.665+00:00",
              "height": 113,
              "width": 990,
              "storage_key": "c576c77f-fb6e-4d14-a11b-5b3b94de16c5",
              "context": "documentation"
            },
            "storage_key": "c576c77f-fb6e-4d14-a11b-5b3b94de16c5",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 26354480,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 26354480,
              "file_name": "EditorProdRole.png",
              "file_size": 5058,
              "content_type": "image/png",
              "created_at": "2025-12-18T15:10:29.862+00:00",
              "height": 142,
              "width": 228,
              "storage_key": "dcb2af16-a4e2-4951-8865-a60625b80910",
              "context": "documentation"
            },
            "storage_key": "dcb2af16-a4e2-4951-8865-a60625b80910",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Using the same steps, add a second <strong>Role</strong> for your secondary device to occupy. In this workflow example, the secondary workstation is named Render.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 26354481,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 26354481,
              "file_name": "RenderProdRole.png",
              "file_size": 5531,
              "content_type": "image/png",
              "created_at": "2025-12-18T15:10:29.956+00:00",
              "height": 154,
              "width": 228,
              "storage_key": "60a3a0f8-7ecc-4b0e-97cf-88f5ad066a00",
              "context": "documentation"
            },
            "storage_key": "60a3a0f8-7ecc-4b0e-97cf-88f5ad066a00",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "In the <strong>Menu Bar</strong>, navigate to<strong> Edit</strong> &gt; <strong>Project Settings</strong>, and under the<strong> Multi-User Editing</strong> section,set the <strong>Validation Mode</strong> property to <strong>Soft</strong>, using the drop-down menu.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 26354482,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 26354482,
              "file_name": "SoftAuto.png",
              "file_size": 34606,
              "content_type": "image/png",
              "created_at": "2025-12-18T15:10:30.021+00:00",
              "height": 372,
              "width": 828,
              "storage_key": "64897658-2a64-427c-a6f7-896981a116fa",
              "context": "documentation"
            },
            "storage_key": "64897658-2a64-427c-a6f7-896981a116fa",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "callout",
      "callout_type": "note",
      "blocks": [
        {
          "type": "paragraph",
          "content": "If your project contains any dirty packages, an error prompt displays when you join a multi-user session. You then have the opportunity to cancel the connection or to fix any present issues. If you choose to proceed any dirty packages will be deleted.",
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
  "excerpt_hash_id": "Z6vE",
  "settings": {
    "is_hidden": false
  }
}
```

Your project is now ready to connect other devices using Switchboard for multiple users to operate VCams simultaneously in the same scene.

For more information about connecting multiple users using the **Switchboard** plugin, refer to the [Switchboard](https://dev.epicgames.com/documentation/en-us/unreal-engine/switchboard-in-unreal-engine) and the [Switchboard Quick-Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/switchboard-quick-start-for-unreal-engine) documentation.

## Connect Your Devices

After creating your VP Roles in the Unreal Editor, use the Switchboard application to connect your devices to the Multi-User session.

1. In the Toolbar, click the options menu next to the Switchboard button, and select **Launch Switchboard Listener.** ![image alt text](https://dev.epicgames.com/community/api/documentation/image/9c7d9d99-7328-4470-818e-a86fe5e4f0d8)
2. In the Toolbar, launch the **Switchboard application**. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/07dbf6f2-103f-43ff-b8a3-8f1b2d49ecd4)
3. In the **Add Device** drop-down, select **Unreal**. This creates a new Switchboard Device, which represents the primary workstation. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/638e4a9d-c987-480c-a799-80bdfebd0196)
4. In the provided field, set the **Name** and **IP Address** for the primary work station. The name must be the same name as the primary workstation role set in Unreal Engine. This workflow example uses **Editor** as the name. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/009ccf3a-aeec-4063-af3d-2b8ddf22f232)
5. Repeat steps 1-3 to create a second Switchboard Device. For the second device, use the same name as the second workstation's role. Both devices should now be listed in the Switchboard application, in the **Unreal Devices** list. This workflow example uses the name **Render**. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/6c1ce74b-01d3-47d4-a1f0-c76356bfbd3c)
6. To automatically open a network connection and to connect a device to the Multi-User Editor session, select the **Auto-Join** and **Network Connection** icons for each device in the **Unreal Devices** list. When a device successfully connects to the network, the **Connection Indicator** appears blue. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/911c9674-746d-4bba-bc15-d6280a603659)
7. Assign a **VP Role** to each connected device. In the Switchboard's **Menu Bar**, navigate to **Settings** > **Settings**, and scroll down to each connected device's section. In the **Roles** property, select one of the Unreal Engine **VP Roles**, for each device, using the drop-down menu. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/c9e6a0c5-3f53-42e2-9b7d-aa4ab02b15a1)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can open a <strong>Network Connection</strong> and enable <strong>Auto-Join</strong> for every listed device by using the <strong>Auto-Join</strong> and <strong>Network Connection</strong> icons in the Unreal Device's list header.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26354494,
      "caption": "",
      "alt_text": "image alt text",
      "image": {
        "id": 26354494,
        "file_name": "EnableAll.png",
        "file_size": 11111,
        "content_type": "image/png",
        "created_at": "2025-12-18T15:10:31.476+00:00",
        "height": 150,
        "width": 585,
        "storage_key": "b9490338-10d2-421a-882c-6a57d846a737",
        "context": "documentation"
      },
      "storage_key": "b9490338-10d2-421a-882c-6a57d846a737",
      "context": "documentation",
      "width": null,
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

With your workstations connected, and their roles assigned, you can now launch each device and start operating VCams in a Multi-User environment.

## Multi-User Virtual Camera Operation

1. To connect your primary workstation to the multi-user session, open the Switchboard application, go to the **Unreal Devices** list, locate the primary **Editor** device, and click the **Launch**. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/69bd6a81-fac4-4516-b698-004ebc79b692) Once your project has launched, you can verify that the editor is connected to the multi-user session in the **Multi-User Browser** window. You can open the Multi-User Browser in the Menu bar, navigating to **Window** > **Multi-User Browser**. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/e862b765-f9e5-43b6-8b2b-87177f11d608)
2. In the **World Outliner**, select the **VCamActor**.
3. Select the **VCam component** in the VCam actor's **Details** panel.
4. Set the **Role** property to **Edit** in the **Virtual Camera** properties section and select the **Editor** VP Role from the drop down menu. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/a72a0b4d-b3d5-457d-b900-b00e0d4cf0b6)
5. Enable the Virtual Camera by toggling the **Enabled** property.
6. In the Switchboard application, launch the **Render** device by clicking the **Launch** icon. Following the steps above, verify that the secondary **Render** device is also connected to the multi-user session, using the **Multi-User Browser** window.
7. Now that both editor instances are open, move the **Virtual Camera** on the primary **Editor** device and see the changes replicated in the secondary **Render** device in real time. In the example below the **Editor** device (**Left**) is operating a **VCam Actor** and the **Render** device (**Right**) is receiving the changes and rendering the scene.

[Video: V_OMYaa5](https://dev.epicgames.com/community/api/cms/videos/V_OMYaa5/embed.html)
