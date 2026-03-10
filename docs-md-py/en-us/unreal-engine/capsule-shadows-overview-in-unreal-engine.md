# Capsule Shadows Overview

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/capsule-shadows-overview-in-unreal-engine

> Application Version: 5.7

Unreal Engine supports soft shadowing for characters in lit areas with **Capsule Shadows** using a capsule representation of a Skeletal Mesh from a Physics Asset. This shadowing method grounds a character to the scene with soft area shadowing, especially in indirectly lit areas, which is not possible when using traditional shadow mapping techniques.

## Character Capsule Representation

A [Physics Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine) is used to create an approximate representation of the character to support very soft shadowing. Since the capsules are attached to the bones of the character, this
allows for the shadow to move and cast accurately within the scene.

```json
{
  "type": "comparison_slider",
  "image_left_id": 24559666,
  "caption_left": "Character with Capsule Representation",
  "image_right_id": 24559667,
  "caption_right": "Capsule Representation Only",
  "image_left": {
    "id": 24559666,
    "file_name": "CapsuleShadowPA.png",
    "file_size": 631849,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:02.954+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "58c15480-7b0a-45a9-a68f-4278538935c8",
    "context": "documentation"
  },
  "image_right": {
    "id": 24559667,
    "file_name": "CapsuleShadowPA1.png",
    "file_size": 523832,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:03.174+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "e8f219c6-8f39-4ec6-a0a4-08b324a68023",
    "context": "documentation"
  },
  "image_left_storage_key": "58c15480-7b0a-45a9-a68f-4278538935c8",
  "image_right_storage_key": "e8f219c6-8f39-4ec6-a0a4-08b324a68023",
  "context": "documentation",
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
      "content": "The shadows on the ground in the Physics Asset viewport are not representative of Capsule Shadows.",
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

## Usage

![Image](https://dev.epicgames.com/community/api/documentation/image/cfe75cf3-93ef-49a5-bc37-28cdc7862d48)

Open your Skeletal Mesh, and in the **Asset Details** panel, use the **Shadow Physics Asset** selection to assign your Physics Asset that will be used for Capsule Shadows.

## Capsule Shadow Settings

![Image](https://dev.epicgames.com/community/api/documentation/image/e56d25a9-5881-41fa-94de-ca1cc8b7f6b2)

| Property | Description |
| --- | --- |
| **Capsule Direct Shadow** | This will enable soft shadowing from direct (movable) lights when the capsule representation is assigned to the Skeletal Mesh's Shadow Physics Asset slot. |
| **Capsule Indirect Shadow** | This will enable soft shadowing from precomputed lighting (lightmaps and skylight) when the capsule representation is assigned to the Skeletal Mesh's Shadow Physics Asset slot. |
| **Capsule Indirect Shadow Min Visibility** | This will allow artists to control how dark the capsule shadow, in indirectly lit areas, can be. |

### Capsule Indirect Shadows

When you enable **Capsule Indirect Shadow**, the capsule representation of the character will be used to cast a directional soft shadow based on the [volume lighting samples](https://dev.epicgames.com/documentation/en-us/unreal-engine/indirect-lighting-cache-in-unreal-engine)
placed and computed by Lightmass during a lighting build. Capsule Indirect Shadows enables your characters to feel grounded in these areas where traditional shadow mapping will not work very well.

![Image](https://dev.epicgames.com/community/api/documentation/image/c441865c-4ec8-410c-ae0f-bd3a11d99d5d)

When Capsule Indirect Shadow is enabled, your character will cast a soft shadow that can ground them in areas with only bounce lighting.

```json
{
  "type": "comparison_slider",
  "image_left_id": 24559668,
  "caption_left": "Capsule Indirect Shadow Enabled",
  "image_right_id": 24559669,
  "caption_right": "Capsule Indirect Shadow Disabled",
  "image_left": {
    "id": 24559668,
    "file_name": "CSEnabled.png",
    "file_size": 633873,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:03.366+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "ef1726fe-d6e6-45dd-baa5-d89c0cbc4e3b",
    "context": "documentation"
  },
  "image_right": {
    "id": 24559669,
    "file_name": "CSDisabled.png",
    "file_size": 617050,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:03.712+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "e8e89c72-73f2-45f2-a7f9-cff059acd5b6",
    "context": "documentation"
  },
  "image_left_storage_key": "ef1726fe-d6e6-45dd-baa5-d89c0cbc4e3b",
  "image_right_storage_key": "e8e89c72-73f2-45f2-a7f9-cff059acd5b6",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

In an open area with only a Sky Light as the light source, there will be little directionality, since light is coming from all around. This produces a subtle soft "blob" shadow below
the character when using precomputed lighting.

```json
{
  "type": "comparison_slider",
  "image_left_id": 24559670,
  "caption_left": "Indirect Capsule Shadows Enabled",
  "image_right_id": 24559671,
  "caption_right": "Indirect Capsule Shadows Disabled",
  "image_left": {
    "id": 24559670,
    "file_name": "SkylightCS1.png",
    "file_size": 566393,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:03.896+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "24addf45-02a1-4045-a8b8-928473a59050",
    "context": "documentation"
  },
  "image_right": {
    "id": 24559671,
    "file_name": "SkylightCS2.png",
    "file_size": 565447,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:04.103+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "fc160878-1171-4d64-af76-1ba7cb6084f0",
    "context": "documentation"
  },
  "image_left_storage_key": "24addf45-02a1-4045-a8b8-928473a59050",
  "image_right_storage_key": "fc160878-1171-4d64-af76-1ba7cb6084f0",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

In an enclosed area where light is coming through an opening, the [indirect lighting cache](https://dev.epicgames.com/documentation/en-us/unreal-engine/indirect-lighting-cache-in-unreal-engine) is used to
give directionality and softness to the capsule shadow by interpolating between the placed volume lighting samples as the character moves through the space. At the doorway, the character's shadow will be
less intense with little directionality, but as the character moves further away from the doorway, the shadow's intensity and directionality will increase.

[Video: 0_10j9h19y](https://dev.epicgames.com/community/api/cms/videos/0_10j9h19y/embed.html)

#### Indirect Minimum Shadow Visibility

Artists are afforded additional control by adjusting the **Capsule Indirect Shadow Min Visibility**. This enables you to adjust how dark the capsule shadow will be in indirectly lit areas, using precomputed lighting. This can be be useful to reduce any self-shadowing from a capsule in these areas, or to soften the shadow's intensity, so that it blends nicely with surrounding shadows.

```json
{
  "type": "comparison_slider",
  "image_left_id": 24559672,
  "caption_left": "Capsule Shadow Indirect Min Visibility: 0.1 (Default)",
  "image_right_id": 24559673,
  "caption_right": "Capsule Shadow Indirect Min Visibility: 0.45",
  "image_left": {
    "id": 24559672,
    "file_name": "CSEnabled.png",
    "file_size": 633873,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:04.299+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "8c1b30f5-010d-4852-9b16-6dffc4036f07",
    "context": "documentation"
  },
  "image_right": {
    "id": 24559673,
    "file_name": "CSMinVisibility_45.png",
    "file_size": 628925,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:04.593+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "28ea2843-4919-4bdd-b6cd-e0f3c09195bc",
    "context": "documentation"
  },
  "image_left_storage_key": "8c1b30f5-010d-4852-9b16-6dffc4036f07",
  "image_right_storage_key": "28ea2843-4919-4bdd-b6cd-e0f3c09195bc",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

### Capsule Direct Shadows

Enabling **Capsule Direct Shadow** on light sources enables you to define how soft area shadowing is for the shadow caster on a shadow receiver based on the angle of the light or the size of the light source.

![Image](https://dev.epicgames.com/community/api/documentation/image/36024bb8-aed7-4869-945b-261a12797dfd)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Capsule Shadows for direct lighting should be used as a scalability option for cheaper shadows than rendering highly detailed polygonal Skeletal Meshes into shadowmaps. For additional information, see the sections directly below for specific mobilities required for the light source. Also, see the \"Limitations\" section below.",
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

#### Light Source Angle

For a Directional Light, the **Source Angle** property enables you specify the Sun's angle in degrees to soften shadows.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This property works for all light mobilities (Static, Stationary, and Movable) when <strong>Capsule Direct Shadow</strong> is enabled.",
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
  "type": "comparison_slider",
  "image_left_id": 24559674,
  "caption_left": "Light Source Angle: 1.0 (Default)",
  "image_right_id": 24559675,
  "caption_right": "Light Source Angle: 2.0",
  "image_left": {
    "id": 24559674,
    "file_name": "CS_LSA1.png",
    "file_size": 431870,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:04.832+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "f2e1e42e-ba19-4f5f-a864-fe2d35c1f253",
    "context": "documentation"
  },
  "image_right": {
    "id": 24559675,
    "file_name": "CS_LSA2.png",
    "file_size": 422532,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:04.996+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "1eef3299-c994-4326-9992-5eb7bc248e15",
    "context": "documentation"
  },
  "image_left_storage_key": "f2e1e42e-ba19-4f5f-a864-fe2d35c1f253",
  "image_right_storage_key": "1eef3299-c994-4326-9992-5eb7bc248e15",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

#### Source Radius

For Spot and Point Lights, the **Source Radius** sets the size of the light source emitting light; the larger the source the softer the shadows and smaller, the more hard the shadow contacts are.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Capsule Direct Shadowing requires that the light source have its mobility set to <strong>Stationary</strong> and that lighting has been built for the scene before the <strong>Source Radius</strong> on the light will have any effect.",
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
  "type": "comparison_slider",
  "image_left_id": 24559676,
  "caption_left": "Source Radius: 5.0",
  "image_right_id": 24559677,
  "caption_right": "Source Radius: 15.0",
  "image_left": {
    "id": 24559676,
    "file_name": "CS_SR1.png",
    "file_size": 366310,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:05.235+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "41211f17-4ee3-4bc3-b921-895e3860a17b",
    "context": "documentation"
  },
  "image_right": {
    "id": 24559677,
    "file_name": "CS_SR2.png",
    "file_size": 363098,
    "content_type": "image/png",
    "created_at": "2025-05-02T16:27:05.386+00:00",
    "height": 827,
    "width": 921,
    "storage_key": "ae39acc0-41f6-4660-989b-3211b7102e20",
    "context": "documentation"
  },
  "image_left_storage_key": "41211f17-4ee3-4bc3-b921-895e3860a17b",
  "image_right_storage_key": "ae39acc0-41f6-4660-989b-3211b7102e20",
  "context": "documentation",
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
      "content": "Once lighting has been built for your scene, you can adjust the <strong>Source Radius</strong> property without having to rebuild lighting. This property only affects movable actors with Capsule Shadows or Mesh Distance Fields enabled.",
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

## Performance

The GPU performance cost of Capsule Shadows is proportional to the number of capsules used, the number of characters, and the screen size that their shadow affects.

Using a Radeon 7870 at 1080p, for example:

| GPU Cost with 10 Capsules | Time in milliseconds (ms) |
| --- | --- |
| **A single character on screen** | 0.29 ms |
| **Each additional character on screen** | 0.05 ms |

This implementation is very efficient, since it computes shadowing at half resolution with a depth-aware upsample, while using screen tile culling to reduce the amount of shadowing work to only happen where it is needed.

## Limitations

- Not compatible with [Virtual Shadow Maps](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine?application_version=5.5).
- Requires DirectX 11, due to tiled deferred implementation using compute shaders.
- Movable Point and Spot Lights are not currently supported.
- Self-shadowing artifacts can exist for arbitrary mesh shapes.
- Can only use Sphyls and Spheres for capsule representation.
- When capsule shadows get so soft that they become ambient occlusion, there's an artifact in the shadowing that causes a hard line.
- Movable Point and Spot lights are not supported because it costs more to remove one object out of the whole scene shadows and do a per-object shadow for it. Stationary lights are always going to be a per-object shadows method so Capsule Direct Shadow for faster shadow rendering makes sense.
