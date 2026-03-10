# Control Rig Quick Start

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine

> Application Version: 5.7

This page provides an overview of Control Rig, and shows how to create and animate rigs in Unreal Engine.

## What is a Control Rig?

Control Rig is Unreal Engine's solution to animating characters directly in the engine.

The **Control Rig Editor** is where you can create custom controls, channels, and other manipulators for your characters. After a rig is created, you can animate these controls within other areas of Unreal Engine, such as **[Sequencer](animating-characters-and-objects/Sequencer)**.

![control rig editor overview](https://dev.epicgames.com/community/api/documentation/image/316c068c-51e6-4d0d-aea8-4b0bbfef697a)

Control Rigs require the creation of **Control Rig Assets**, which are created and stored in the **Content Browser**.

![Control-rig-asset-content-browser](https://dev.epicgames.com/community/api/documentation/image/9177c05e-924e-4e6b-a4c3-34915ab916b0)

## How do I Create and Open a Control Rig?

The main way to create a new Control Rig asset is to right-click on a **[Skeletal Mesh](working-with-content/SkeletalMeshes)** in the Content Browser and select **Create > Control Rig**. This creates a Control Rig asset in the same directory with the postfix "\_CtrlRig".

![create control rig](https://dev.epicgames.com/community/api/documentation/image/3c73c635-1ac1-43ed-98f9-a89edc1f2c6c)

Next, double-click on the Control Rig asset to open the **Control Rig Editor**.

![open control rig](https://dev.epicgames.com/community/api/documentation/image/1513445a-ab66-4c8e-8d13-9a5e378424a7)

## How do I Rig and Animate with Control Rig?

One of the simplest control types you can create is an **FK Control**. This guide gives an overview of how to create this control and animate it in **Sequencer**.

### Create Control

In the Control Rig Editor, select the **Rig Hierarchy** tab to view the skeleton hierarchy for your character. Navigate to the bone you want to animate, right-click it, and select **New Element > New Control**.

![Create-new-control](https://dev.epicgames.com/community/api/documentation/image/e5b779c9-8918-44c7-9e04-ee0a1fd874e7)

This creates a control at the same location and orientation of the bone. The control is also named the same as the bone with the postfix "\_ctrl".

![create new control](https://dev.epicgames.com/community/api/documentation/image/04df25db-6876-4e85-b42d-9ccfa25ceb5f)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Although you can keep the control nested within the skeleton hierarchy, it is best practice to remove it from the hierarchy and build your own control rig hierarchy adjacent to the skeleton. Select the control and press <strong>Shift+P</strong> to unparent the control from the skeleton.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26229031,
      "caption": "",
      "alt_text": "unparent control",
      "image": {
        "id": 26229031,
        "file_name": "ShiftP.gif",
        "file_size": 79624,
        "content_type": "image/gif",
        "created_at": "2025-11-05T19:12:33.275+00:00",
        "height": 301,
        "width": 427,
        "storage_key": "284efd06-e51c-4cf2-92ad-24521d6bb1c4",
        "context": "documentation"
      },
      "storage_key": "284efd06-e51c-4cf2-92ad-24521d6bb1c4",
      "context": "documentation",
      "width": null,
      "autoplay": true,
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

### Edit Control Shape

In order to better see and select the control in the viewport, you can change the **Control Shape**. To do this, navigate to the **Details** panel and locate the **Shape** property category. Here you can set a new shape using the **Shape Properties**, as well as customize the scale and offset of it using the **Shape** **Transform** properties.

For this example, the shape is set to **Circle\_Thick**, Rotation Y is set to **90**, and all Scale axes are set to **3.0**.

![change control shape](https://dev.epicgames.com/community/api/documentation/image/fcfea6c5-03ce-4fc6-afc3-fe90c90ec7d9)

### Drive Bone with Control

Next, reference your control and bone in the **Rig Graph**. Do this by dragging the control from the **Rig Hierarchy** panel into the graph, then select **Get Control**.

![get control graph](https://dev.epicgames.com/community/api/documentation/image/f0461ae1-f775-4929-b109-a371555141f4)

Do the same for the bone you want this control to affect. Drag the bone from the **Rig Hierarchy** panel into the graph, then select **Set Bone**.

![set bone graph](https://dev.epicgames.com/community/api/documentation/image/e934eae8-6163-4945-a59d-89226ed100e0)

Connect the **Transform** output data pin from the **Get Transform - Control** node to the **Value**input data pin of the **Set Transform - Bone** node, then connect the **Execute** output pin from the **Forwards Solve** node to the input execution pin of the **Set Transform - Bone** node.

![set bone transform control](https://dev.epicgames.com/community/api/documentation/image/5637a331-f1ef-4f67-b7d4-da558a3b3490)

You can now manipulate the control in the viewport and see the control driving the bone.

![test control](https://dev.epicgames.com/community/api/documentation/image/233c2b8d-7536-4114-a12a-43d3e266a3c7)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Clicking <strong>Compile </strong>resets the control position back to default.",
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

### Animate Control in Sequencer

Now that your control is appropriately manipulating a character's bone, you can start to animate it in **[Sequencer](animating-characters-and-objects/Sequencer)**.

![Animate-control-in-sequencer](https://dev.epicgames.com/community/api/documentation/image/7c0520e9-07c5-4b45-8eb8-eb411718d520)

Drag the **Control Rig Asset** from the **Content Browser** into the Level viewport. Once this is done, Sequencer opens with the character added to it as a **[Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine)**.

[Video: V_LfEtbF](https://dev.epicgames.com/community/api/cms/videos/V_LfEtbF/embed.html)

Expand the **Control Rig** track to locate the controls you created. You can either select them here, or in the viewport.

![control rig in sequencer](https://dev.epicgames.com/community/api/documentation/image/65269ed8-f1b7-40e2-9383-6708e70c381d)

With the control selected in the Viewport, press the **S** key to create a transform **Keyframe** for the selected control at the [Playhead](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#playhead). Afterward, drag the **Playhead** to a different location in the sequence, manipulate your control, then press **S** again to set a second **Keyframe**.

[Video: V_0EKVEB](https://dev.epicgames.com/community/api/cms/videos/V_0EKVEB/embed.html)

Now when playing or scrubbing the sequence, you should see your control and character animate between the two keyframes.

![keyframe control rig](https://dev.epicgames.com/community/api/documentation/image/8f42c997-f91c-4fe8-b3d9-e64667f8ad2a)
