# Skeletons

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine

> Application Version: 5.7

A **Skeleton** is a hierarchy that is used to define **Bones** (sometimes called **joints**) in a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine). In some ways, these Bones mimic a real biological skeleton due to their position and control over how characters deform.

In Unreal Engine, Skeletons are used to store and associate animation data, the overall skeletal hierarchy, and [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine). Skeleton Assets can also be shared through a variety of methods, enabling for additional animations and data to be shared between different Skeletons.

This document provides an overview of how to create and use Skeletons.

#### Prerequisites

- Your project contains a [Skeletal Mesh Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine), or you have a skinned FBX character to import into Unreal Engine.

## Creating Skeletons

The primary way to create a Skeleton is to [import](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-skeletal-meshes-using-fbx-in-unreal-engine) a skinned character FBX, which then converts to a **Skeletal Mesh** in Unreal Engine. When importing a Skeletal Mesh, in the [FBX Import Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine) window, leaving the **Skeleton** field empty will automatically create a Skeleton Asset based on the skinned character being imported.

![import skeletal mesh](https://dev.epicgames.com/community/api/documentation/image/1860201f-7f79-4544-9def-d4343d0d6c35)

After importing your character, the **Skeleton Asset** will be created along with other Skeletal Mesh Assets.

![skeleton asset](https://dev.epicgames.com/community/api/documentation/image/af6caf6a-5b5c-426f-8ed9-576e4e62f910)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can also create a copy of a Skeleton from any Skeletal Mesh by right-clicking on it in the <strong>Content Browser</strong> and selecting <strong>Skeleton &gt; Create Skeleton</strong>. This creates a new Skeleton associated with an existing mesh. If that mesh had another Skeleton associated with it, it will re-link to the new Skeleton and any animations will then link to the new Skeleton.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25769913,
      "caption": "",
      "alt_text": "create skeleton copy",
      "image": {
        "id": 25769913,
        "file_name": "Create4.png",
        "file_size": 54573,
        "content_type": "image/png",
        "created_at": "2025-06-26T19:30:01.570+00:00",
        "height": 414,
        "width": 695,
        "storage_key": "08921957-56ff-46b7-a53c-a16453d95d8e",
        "context": "documentation"
      },
      "storage_key": "08921957-56ff-46b7-a53c-a16453d95d8e",
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

Double-click the Skeleton Asset to open the [Skeleton Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine).

![skeleton editor](https://dev.epicgames.com/community/api/documentation/image/39338a8a-cf34-4791-85de-41d24a4a3da9)

## Skeleton Tree Information

Bones and other items displayed in the [Skeleton Tree](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine) can appear different depending on several factors.

| Icon | Description |
| --- | --- |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/3ccb6e2d-e77b-4c45-b2b2-e96190b5e6f4) | A normal Bone that influences vertices on the Skeletal Mesh. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/6581f5b5-7754-4ec5-bacb-4fb8623a56dd) | A Bone in the current Skeleton that doesn't influence vertices on the Skeletal Mesh. These Bones are typically used in an auxiliary manner, such as for attaching weapons or props, while still being animatable as a Bone. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/5b1fa4d8-0116-4fb7-be4e-847f36d66289) | A [Socket](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine), which is a static point that acts as an offset attachment point for Bones. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/9c37adf2-a9a3-4192-b3fb-b2923ba94667) | A [Virtual Bone](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine), which is a Bone that follows the transforms of another Bone, but in a different Bone space. These are useful for locking down unwanted joint movements, and are used in conjunction with [IK](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-two-bone-ik-in-unreal-engine). |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/4b133b7e-5f18-4907-9f06-bf42301659ed) | A Bone that exists in the Skeleton, but is not used by the current Skeletal Mesh. This can happen if you have [merged](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine) Skeletons, or are previewing different LODs on this Skeleton that are not using certain Bones. |

## Animation Data Storage

In addition to controlling animation, Skeletons in Unreal Engine also store animation-specific data. When data is created from those sources, such as creating an [Animation Notify](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine) in an Animation Sequence, it gets added to the Skeleton as shared data.

Skeletons store the following types of animation data:

- [Animation Notifies](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine).
- [Animation Curves](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine).
- [Slots](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-slots-in-unreal-engine).
- [Retarget Sources](https://dev.epicgames.com/documentation/en-us/unreal-engine/retarget-manager-in-unreal-engine).
- [Blend Profiles and Blend Masks](https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-masks-and-blend-profiles-in-unreal-engine).

This data can be viewed in dedicated tool panels by clicking **Window** in the Skeleton Editor menu, then enabling one or more of these panels.

![animation data panels](https://dev.epicgames.com/community/api/documentation/image/414c1977-a8fd-4328-bfda-04f6e83f479e)

## Sharing Skeletons

An important feature of Skeleton Assets is that a single Skeleton Asset can be used by multiple Skeletal Meshes, so long as the Skeletal Meshes use the same general rig hierarchy. This means that the names and hierarchical order of your Bones must be consistent in order for sharing to work correctly.

For example, consider a limb with three Bones in a Skeletal Mesh. The bones are named **1**, **2**, and **3**:

![sharing skeleton example 1](https://dev.epicgames.com/community/api/documentation/image/b06107b9-d22d-42fc-b96a-0994f88d605b)

If you want to share this Skeleton with another Skeletal Mesh, you will need to keep these Bones in the same order and with the same names. The second Skeletal Mesh, however, can contain Bones that are additions or peripheral to the hierarchy. Any time animation data is received for a Bone that is not included in the Skeletal Mesh, that animation data will be ignored.

In that case, your new hierarchy could look like the image below. Here, the second Skeletal Mesh has extra Bones, while still retaining and not interfering with the original hierarchy from the first Skeletal Mesh.

![sharing skeleton example 2](https://dev.epicgames.com/community/api/documentation/image/a3b49396-4c79-49ab-9172-40e6b36f2f44)

However, in order for both Skeletal Meshes to use the same Skeleton Asset, you cannot change the hierarchy order or rename the Bones. If a second Skeletal Mesh uses a different Bone hierarchy and naming structure, you will need to create a new Skeleton Asset.

![sharing skeleton example 3](https://dev.epicgames.com/community/api/documentation/image/b5822c1c-67c2-441b-9f75-d51226cffeda)

If you insert a bone into the hierarchy without changing the order, you will be able to share successfully. However in most cases the extra bone may cause unintended transform offsets in your skeleton. It is recommended that you avoid this if possible.

![sharing skeleton example 4](https://dev.epicgames.com/community/api/documentation/image/f59c6a74-174d-42e8-a36e-e31eb29ae828)

Taking these sharing rules into account, there are several ways you can share Skeletons between Skeletal Meshes in Unreal Engine. These are detailed below.

### Merging during Import

The first method for sharing Skeletons is done during the FBX import process. When importing your new Skeletal Mesh (with additional and peripheral Bones compliant with the rules above), you can select a Skeleton from a Skeletal Mesh that already exists in your project. Unreal Engine will then merge the Skeletons, appending any new Bones into the hierarchy. Additionally, your Skeleton's proportions will be defined by the original Skeletal Mesh from which it was created.

![merge sharing](https://dev.epicgames.com/community/api/documentation/image/b8b1fbb7-509d-4e37-b8da-ffe7bc4bec0d)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you are importing a Skeleton that is vastly different from the Skeleton you are attempting to merge to and breaks any sharing rules, you will see an error message:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25769926,
      "caption": "",
      "alt_text": "failed to merge bones",
      "image": {
        "id": 25769926,
        "file_name": "Share2.png",
        "file_size": 18655,
        "content_type": "image/png",
        "created_at": "2025-06-26T19:30:02.617+00:00",
        "height": 260,
        "width": 577,
        "storage_key": "d96a0b6c-5f50-4c61-9d18-413e9385e1f7",
        "context": "documentation"
      },
      "storage_key": "d96a0b6c-5f50-4c61-9d18-413e9385e1f7",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "In this case, you may need to create a new Skeleton Asset for the Skeletal Mesh you are importing, rather than merge into an existing one.",
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

When viewing your merged Skeleton, you will see these additional Bones listed in your hierarchy, but they will only be visible and active for the Skeletal Mesh they are intended for.

| ![Image](https://dev.epicgames.com/community/api/documentation/image/3cfad35d-61ca-4095-9b84-34629d390056) | ![Image](https://dev.epicgames.com/community/api/documentation/image/97a8b7ed-5a3e-4a2d-8b81-aa6700d0f360) |
| --- | --- |
| Skeletal Mesh Variant 1 | Skeletal Mesh Variant 2 |

### Compatible Skeletons

Additionally, skeletons can non-destructively share animation assets by defining other skeletons as compatible. Compatible skeletons can share [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine), [Montages](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-montage-in-unreal-engine), [Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine), and more.

To define another skeleton as compatible for a character, open the character's skeleton asset in the [Skeleton Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine), and then open the **Retarget Manager** by clicking the button in the **Toolbar**.

![compatible skeletons](https://dev.epicgames.com/community/api/documentation/image/05ade0b6-4518-4afb-8fd0-09bdf27bcf88)

In the **Retarget Manager**, locate the **Manage Compatible Skeletons** section of the **Retarget Sources** panel and click **Add Skeleton** to select another skeleton asset in your project using the context menu.

![add compatible skeleton](https://dev.epicgames.com/community/api/documentation/image/11332bc4-1d5a-4564-b16d-82955a981dfe)

Now, animations can be shared from the Skeleton that was added to the **Manage Compatible Sources** list.

![compatible skeletons](https://dev.epicgames.com/community/api/documentation/image/407efd6f-e84d-4823-9c0e-81bb849b0555)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Skeleton compatibility is bi-directional. If you set Skeleton 1 to be compatible with Skeleton 2, that also means that Skeleton 2 is now compatible with Skeleton 1.",
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

Creating and managing a system of compatible skeletons can be an effective way to optimize the number of animation assets your project requires to animate multiple characters. However, in order to utilize the Compatible Skeletons system, all characters must have nearly identical skeleton hierarchy structures and naming conventions. Additionally, all characters must have similar mesh proportions to achieve ideal results.

To share animations across characters with the same skeleton structure but with different proportions see the [Animation Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-retargeting-in-unreal-engine) documentation.

To rebuild animation sequences to work across characters with radically different skeleton structures, see the [IK Rig Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine) documentation.

## Skeleton Features

Skeletons in Unreal Engine support a variety of features for attaching, blending, and other settings. Refer to the following pages to learn more about these features:

- [Related Document](en-us/unreal-engine/skeletons-in-unreal-engine.md)
