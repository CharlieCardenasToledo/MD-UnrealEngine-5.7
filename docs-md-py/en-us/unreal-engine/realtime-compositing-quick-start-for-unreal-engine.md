# Legacy Composure Quick Start

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/realtime-compositing-quick-start-for-unreal-engine

> Application Version: 5.7

The most basic of composites is the three piece comp: a CG background, a middle media (video) plate, and a CG foreground. In this topic, we'll demonstrate how to use composure to build a basic three piece comp.

## 1 - Load Composure

### Steps

1. Enable the **Composure Plugin**. ![Enable plugin](https://dev.epicgames.com/community/api/documentation/image/1623882d-6779-49d3-80ce-52c73d7cb2d8)
2. Open the compositing tree panel (listed as **Composure Compositing** in the **Window** menu under **Virtual Production** section). ![Open the compositing tree panel](https://dev.epicgames.com/community/api/documentation/image/765b7dda-eb88-47a7-a287-1a4daf91dca4)

## 2 - Add a Root Comp Element

Next, add a root Element to the compositing tree.

### Steps

1. Right-click in the compositing tree panel, and select **Create New Comp** from the menu. Then, select **Empty Comp Shot** from the **Pick a Comp Class** dialog. ![Create New Comp](https://dev.epicgames.com/community/api/documentation/image/23f9cf22-078a-41bf-8564-25fd17e927b5) This Element will not render anything immediately as it represents your final composite. This Element will be responsible for combining all of the other Elements.

## 3 - Add a Media/Video Element

Once you have a top-level comp Element, you need to add child Elements. Child Elements feed into their parent (for compositing).

### Steps

1. Add a **Media Plate** to the comp tree. Right-click on the comp Element in the compositing tree panel, and then select **Add Layer Element** from the menu. When prompted to pick a Element type, select **Media Plate**. ![Add a Media Plate](https://dev.epicgames.com/community/api/documentation/image/40244871-5f8a-4502-8bf9-5e1a609c71ed)
2. Set your **Media Source**. By default, your media Element will not be connected to a media source (such as a streaming video). You can apply a media texture to act as an input In the Element's details. Select the new media Element. Then, in the details panel, find the **Media Source** section (under **Composure**→**Inputs**). The **MediaSource** texture property will be empty. ![Set a Media Source](https://dev.epicgames.com/community/api/documentation/image/11d0e0c5-7cd6-4ef4-9d0c-a7da05083295)
3. Configure the **Chroma Key Color**. The **Media Plate** Element has a set of predefined transform Passes on it. Those Passes are for adjusting the media image before it gets composited. The first of those passes is for **Chroma Keying**. To pick a **Chroma Key Color**, under **Transform Passes** navigate to the keying Pass, then find the one named **Chroma Keying**. After expanding **Chroma Keying**, you'll find a **Key Colors** property. Add a new **Key Color** using the picker button next to the color box. ![Configure the Chroma Key Color](https://dev.epicgames.com/community/api/documentation/image/4d70dc00-bb7a-4153-8698-10cfa5f800d7) Clicking the picker button will open up a large picker window to enable you to select a color. To pick a color, click the mouse anywhere on the image to sample that pixel. Click and dragging will average the sampled pixels together, so you can get a more homogenous chroma color. Once you're happy with the result, click **Accept**. Along with the key color, there are many other settings that can be adjusted to perfect the keying. Review the **Material Parameters** section inside the Pass. ![Material Parameters](https://dev.epicgames.com/community/api/documentation/image/00b45c02-fe43-4309-b6e2-d2ed420f78a7) In addition to the **Chroma Keying Pass**, there is a separate **Despill Pass** for removing green bounce on your subject. For more details on chroma keying and despill, see the blog post [here](https://www.unrealengine.com/en-US/tech-blog/setting-up-a-chroma-key-material-in-ue4).
4. Preview the Results. Sometimes it's hard to get a sense of how good of a job your keyer is doing. For every Element, you can open up a larger preview window, and look at individual color channels for that image. ![Preview the Results](https://dev.epicgames.com/community/api/documentation/image/cb776d33-4686-422f-90bd-7b0cbe38a9c9) The **Key Picker** window and the **Level Editor** preview pane also both have this functionality. At this point in the process, don't worry if it's not perfect. You can always adjust it later when you preview the whole composited scene.

## 4 - Add CG Elements

Similar to adding the media Element, we want to add Elements for foreground and background layers.

### Steps

1. Add a **CG Layer**. Right-click on the top-level comp Element in the tree panel, and then select **Add Layer Element** from the menu and pick **CG Layer**. [Video: V_gu6x1d](https://dev.epicgames.com/community/api/cms/videos/V_gu6x1d/embed.html) Add two CG Elements – one for foreground objects, another for background objects, and name them appropriately: fg\_element, and bg\_element.
2. Link to a Scene Camera. CG Elements requires a camera in the world to cue off of – the camera tells them the viewpoint to render from. Without a camera in your scene, CG Elements will display a "Missing Camera" warning message. To resolve this, simply add a camera actor to your scene. ![Add Cine Camera Actor](https://dev.epicgames.com/community/api/documentation/image/79c62e96-696c-44f4-80b6-693114ee492d)
3. Setup Actor Layers. Now that you have two CG Elements (one for foreground, and one for background), you need to specify what scene actors should be rendered to each. For this, we will leverage the level editor's layer system. In our test scene, we've added some basic primitives – a cube, a cone, a sphere, and a cylinder. In this case, the cone and cylinder are in the foreground, and everything else in the background. To start, create an editor layer for just the cone and cylinder. ![Add Actor Layers](https://dev.epicgames.com/community/api/documentation/image/4c426436-f888-4e07-aa04-31027425cecd) Now, in the foreground Element (fg\_element), find the **Capture Actors** property (under **Composure**→**Inputs**), and add an entry to it. The **Capture Actors** list specifies what the CG Element should render. ![Capture Actors](https://dev.epicgames.com/community/api/documentation/image/a093acc6-6996-41ab-9bb7-a734b1486102) In the new **Capture Actors** entry, set the **ActorSet** property to the **ConeAndCylinder** layer that we created earlier. Because the entry's **InclusionType** is set to **Include**, it will render only those actors. You can add as many **Capture Actor** layers to the Element as you wish. You can mix/match includes and excludes. For the background Element, we want everything except the **ConeAndCylinder** layer. So we use the same layer, but switch the **InclusionType** to **Exclude**. For your CG renders to have the proper opacity for compositing, you will need to set **Enable alpha channel support in post processing** to **Linear color space only enable** in project settings: ![Enable alpha channel support in post processing](https://dev.epicgames.com/community/api/documentation/image/4e60a748-d8a2-40dc-be89-f14fd82dcd3f) *Click image to expand*

## 5 - Setup a Compositing Material

Now that you have four Elements (the top-level comp, a **Media Plate**, and two CG Elements), you can layer them all to produce your comp. The top-level comp Element is responsible for merging all of the other Elements. We're going to add a transform Pass to the comp Element and set it up to composite the other three layers.

![Compositing Elements](https://dev.epicgames.com/community/api/documentation/image/43577ab4-8d31-49c9-aba5-18c4c817e783)

### Steps

1. Add a Comp Transform Pass. Select the comp Element, and then in details find the **Transform Passes** property. Add an entry to the **Transform Passes** list. The default entry is **Custom Material Pass**, which is what we want. ![Add a Comp Transform Pass](https://dev.epicgames.com/community/api/documentation/image/a1a306d9-56fe-4e4c-a6fb-a9de1935cca7)
2. Create a Comp Material. The new Pass expects a material for rendering. Expand the Pass's details and create a new material for its **Material** property. [Video: V_o8oTQZ](https://dev.epicgames.com/community/api/cms/videos/V_o8oTQZ/embed.html) Set the new material to be a **Post Process** material – this ensures that you're outputting the result to the correct channel. ![Set a Post Process](https://dev.epicgames.com/community/api/documentation/image/6910e9aa-3437-443f-aaeb-95fb515fc26d) In the new material, we need texture samplers for each of the three sub-Elements. To do this, create three texture sampler parameters and name them to match the child Elements. These texture params will get automatically filled out with the results from the three child Elements. To combine the three Elements all you need are a couple **Over** nodes. The **Over** node takes **input A** and layers it over **input B**, using **input** **A**'s alpha. We want to sandwich the media plate between our two CG layers. [Video: V_159g4p](https://dev.epicgames.com/community/api/cms/videos/V_159g4p/embed.html)
3. Set one Over node so the media plate (**A**) renders over the bg Element (**B**). Next, use the result from that Over node and plug it into **B** on another Over node. Lastly, put the **fg** Element on top by plugging it into **A** on that second Over node. The second Over node's output should be plugged into the material's **Emissive Color** channel. Save and apply the material. /ul>

Review your results back in the compositing window. You should have a single image with all three Elements composited together.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Over node expects a <strong>float4</strong> input, so use the texture sampler's <strong>RGBA</strong> output pin, not its top <strong>RGB</strong> pin.",
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

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Over node uses input <strong>A</strong>'s alpha for Blending. By default, projects are not set up to pipe alpha data through the post process pipeline. So for the CG layers to work, you have to enable this project setting.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26199268,
      "caption": "",
      "alt_text": "Enable alpha channel support in post processing",
      "image": {
        "id": 26199268,
        "file_name": "13-enable-alfa-channel_ue5.png",
        "file_size": 64925,
        "content_type": "image/png",
        "created_at": "2025-10-28T20:30:04.466+00:00",
        "height": 592,
        "width": 1367,
        "storage_key": "4ff8c0be-d387-4706-916d-1ce48c37266d",
        "context": "documentation"
      },
      "storage_key": "4ff8c0be-d387-4706-916d-1ce48c37266d",
      "context": "documentation",
      "width": 800,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<em>Click image to expand</em>",
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

## 6 - Output Your Comp

If you're happy previewing your comp in the editor, then ignore this last step. However, if you want to route the result of your comp to disk or run it out through a capture card, then you will want to use an **Output Pass**.

In this example, we want our comp to be broadcast via a capture card.

### Steps

1. In the top-level comp Element's details, find the **Outputs** property and add an entry to that list. The default is **Media Capture**, which is what we want. [Video: V_Qcdl1h](https://dev.epicgames.com/community/api/cms/videos/V_Qcdl1h/embed.html)
2. In the new output Pass, you will need to specify the target in the Pass's **Capture Output** property, and create a new asset for it. ![Specify the Target](https://dev.epicgames.com/community/api/documentation/image/3c7c1632-29df-4101-90b7-3b3c1a5b3fa9) Configure this asset for your capture target, and you should be all set. The comp Element should start broadcasting.

### Using Sequencer

Alternatively, you can render out comps and AOVs with [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview), our in-engine cinematic editor. For more information, see [Real-Time Compositing with Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine).

![Using with Sequencer](https://dev.epicgames.com/community/api/documentation/image/8a7f509b-f94f-4e80-9f87-5eaffa29839a)
