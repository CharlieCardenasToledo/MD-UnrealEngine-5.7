# Viewport Modes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-modes-in-unreal-engine

> Application Version: 5.7

![Viewmode Header](https://dev.epicgames.com/community/api/documentation/image/ae606e1e-1ee6-4de0-a103-7ae5188e0051)

```json
{
  "type": "include",
  "excerpt_id": 1929,
  "excerpt_assignment_id": 2728,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Unreal Editor viewports have a large number of visualization modes to help you see the type of data being processed in your scene, as well as to diagnose any errors or unexpected results. The more common view modes have their own hotkeys, but all can be accessed from the viewport within the <strong>View Mode</strong> menu.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25777817,
      "caption": "Click image for full size.",
      "alt_text": "Viewmode Menu",
      "image": {
        "id": 25777817,
        "file_name": "02-viewmode-menu.png",
        "file_size": 186118,
        "content_type": "image/png",
        "created_at": "2025-07-03T18:58:21.168+00:00",
        "height": 397,
        "width": 528,
        "storage_key": "f0b875c4-9e6f-4dde-828c-3a66f34d7cfe",
        "context": "documentation"
      },
      "storage_key": "f0b875c4-9e6f-4dde-828c-3a66f34d7cfe",
      "context": "documentation",
      "width": 300,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25777818,
      "caption": "Click image for full size.",
      "alt_text": "Viewmodes Submenu Button",
      "image": {
        "id": 25777818,
        "file_name": "03-viewmodes-sub-menu-button.png",
        "file_size": 99471,
        "content_type": "image/png",
        "created_at": "2025-07-03T18:58:21.465+00:00",
        "height": 842,
        "width": 431,
        "storage_key": "eb151b7a-b4f4-463f-84d2-ecd8caadad7b",
        "context": "documentation"
      },
      "storage_key": "eb151b7a-b4f4-463f-84d2-ecd8caadad7b",
      "context": "documentation",
      "width": 300,
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "0Za",
  "settings": {
    "is_hidden": false
  }
}
```

## Lit

![Viewmode Lit](https://dev.epicgames.com/community/api/documentation/image/67cad9cd-4f53-4651-8934-60fd744e17cd)

_Click image for full size._

- View Mode Hotkey: **Alt + 4**
- Console command: `viewmode lit`

**Lit** view mode shows the final result of your scene once all of the Materials and lighting have been applied.

## Unlit

![Viewmode Unlit](https://dev.epicgames.com/community/api/documentation/image/7be85fbf-c793-45bc-abcf-6d7de13412fb)

_Click image for full size._

- View Mode Hotkey: **Alt + 3**
- Console command: `viewmode unlit`

**Unlit** view mode removes all lighting from the scene, showing you Base Color only.

## Wireframe

![Viewmode Wireframe](https://dev.epicgames.com/community/api/documentation/image/f6a3dbd1-2f20-4b33-9175-05f5ce57df8e)

_Click image for full size._

- View Mode Hotkey: **Alt + 2**
- Console command: `viewmode wireframe`

**Wireframe** shows all of the polygon edges in the scene. In the case of Brushes, you will see the resultant geometry.

## Detail Lighting

![Detail Lighting](https://dev.epicgames.com/community/api/documentation/image/ca221031-a803-477e-a758-69128a87a825)

_Click image for full size._

- View Mode Hotkey: **Alt + 5**
- Console command: `viewmode lit_detaillighting`

**Detail Lighting** activates a neutral Material across the entire scene, using the normal maps of the original materials. This is useful for isolating whether your BaseColor is obscuring lighting by being too dark or noisy.

## Lighting Only

![Lighting Only](https://dev.epicgames.com/community/api/documentation/image/751564c5-42d2-4980-9596-c3ecdb045e5a)

_Click image for full size._

- View Mode Hotkey: **Alt + 6**
- Console command: `viewmode lightingonly`

**Lighting Only** shows a neutral Material that is only affected by lighting. It differs from *Detail Lighting* mode in that you will not see normal maps.

## Light Complexity

![Optimization Viewmodes Menu](https://dev.epicgames.com/community/api/documentation/image/1fa8d9a3-9f01-4b8e-b84e-fb9e72f0b398)

_Click image for full size._

![Light Complexity](https://dev.epicgames.com/community/api/documentation/image/e9b719fa-6f60-428b-9891-a596a4ceffd3)

_Click image for full size._

- View Mode Hotkey: **Alt + 7**
- Console command: `viewmode lightcomplexity`

Light Complexity shows the number of non-static lights affecting your geometry. This is useful for tracking lighting cost - the more lights affecting a surface, the more expensive it will be to shade.

| Light Complexity Coloration |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
| **Color** | ![LightComplexity_0](https://dev.epicgames.com/community/api/documentation/image/84a4f99c-32bd-4bd8-becf-a1f4733cbfe3) | ![LightComplexity_1](https://dev.epicgames.com/community/api/documentation/image/d17d1ad2-177b-4e4c-94df-e69ad676019e) | ![LightComplexity_2](https://dev.epicgames.com/community/api/documentation/image/7ff6086e-ecee-4f52-a0b3-6b8d09e95fc4) | ![LightComplexity_3](https://dev.epicgames.com/community/api/documentation/image/36dc4885-9366-486b-8208-d4994eb62481) | ![LightComplexity_4](https://dev.epicgames.com/community/api/documentation/image/0d45edde-4609-41de-9318-e67766626c68) | ![LightComplexity_5](https://dev.epicgames.com/community/api/documentation/image/1fee7155-9dc1-4633-b0cf-9fe8c598f115) |
| **Number of Lights Affecting Surface** | **0** | **1** | **2** | **3** | **4** | **5+** |

This color scheme is defined in the shader code.

## Shader Complexity

![Shader Complexity](https://dev.epicgames.com/community/api/documentation/image/c7d35cb2-1fae-4d42-95b5-b11e81e755c2)

_Click image for full size._

- View Mode Hotkey: **Alt + 8**
- Console command: `viewmode shadercomplexity`

**Shader Complexity** Mode is used to visualize the number of shader instructions being used to calculate each pixel of your scene. It is generally a good indication of how performance-friendly your scene will be. In general, it is used to test overall performance for your base scene, as well as to optimize particle effects, which tend to cause performance spikes with a large amount of overdraw for a short period of time.

Only instruction count is used to calculate shader complexity, which may not always be accurate. For example, a shader with 16 instructions, all texture lookups, will be much slower on all platforms than a shader with 16 math instructions. Also shaders which contain loops that are not unrolled will not be represented accurately by the instruction count, this is mainly an issue for vertex shaders. Overall the instruction count is a good metric in the vast majority of cases.

The view mode uses a color spectrum to indicate how expensive the scene is. Green through red represent a linear relationship of "very inexpensive" to "expensive", while pink and white indicate a large jump to "very expensive" pixels. Small areas of white can be tolerated, but if the majority of your screen is covered in bright red or white, the performance will be poor.

|   |   |   |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shader Complexity Coloration |   |   |   |   |   |   |   |   |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/7b7d30ce-43a2-47ab-8cef-4790bad85e0b) | ![Image](https://dev.epicgames.com/community/api/documentation/image/b18fd1f8-78d8-4f25-bd7e-b192d17c461c) | ![Image](https://dev.epicgames.com/community/api/documentation/image/406af721-bfab-4d17-8ce2-204c30d6d8d7) | ![Image](https://dev.epicgames.com/community/api/documentation/image/862cb40c-658a-4c71-abdb-c5362da4834c) | ![Image](https://dev.epicgames.com/community/api/documentation/image/3bbec4a9-5cf9-4037-8f70-e0cfab25f6af) | ![Image](https://dev.epicgames.com/community/api/documentation/image/95d6250f-0fd5-4516-aef7-d95bd2b96ff8) | ![Image](https://dev.epicgames.com/community/api/documentation/image/97280a3d-dcdb-449d-87b8-ee0541b2b882) | ![Image](https://dev.epicgames.com/community/api/documentation/image/29dffeb8-4592-4f40-9f8d-f7edbbc6b3d8) | ![Image](https://dev.epicgames.com/community/api/documentation/image/a8e795ab-8455-48d3-9f29-70dd9058e4a1) |
| **Ideal** |   |   | **Moderate** |   |   | **Expensive** | **Very Expensive** |   |

**+ShaderComplexityColors** is defined in the `BaseEngine.ini` file and is linearly interpolated (lerped) based on the total number of instructions for a given pixel.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "+ShaderComplexityColors=(R=0.0,G=1.0,B=0.127,A=1.0)  \n+ShaderComplexityColors=(R=0.0,G=1.0,B=0.0,A=1.0)  \n+ShaderComplexityColors=(R=0.046,G=0.52,B=0.0,A=1.0)  \n+ShaderComplexityColors=(R=0.215,G=0.215,B=0.0,A=1.0)  \n+ShaderComplexityColors=(R=0.52,G=0.046,B=0.0,A=1.0)  \n+ShaderComplexityColors=(R=0.7,G=0.0,B=0.0,A=1.0)  \n+ShaderComplexityColors=(R=1.0,G=0.0,B=0.0,A=1.0)  \n+ShaderComplexityColors=(R=1.0,G=0.0,B=0.5,A=1.0)  \n+ShaderComplexityColors=(R=1.0,G=0.9,B=0.9,A=1.0)",
  "lines_of_code": 9,
  "id": 163122,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMxMjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxODo0OSswMDowMCJ9--1cbc7c09d9347b9f7ca9f6607fe9cd6f276069894a082e93cfd89afe2ea3b72f",
  "settings": {
    "is_hidden": false
  }
}
```

**MaxPixelShaderAdditiveComplexityCount** is set to a default range of 2000, however, this value can be changed in the `BaseEngine.ini` file to help with the optimization of materials in your project.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MaxPixelShaderAdditiveComplexityCount=2000",
  "lines_of_code": 1,
  "id": 163123,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMxMjMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxODo0OSswMDowMCJ9--c74969909985f68f128f37dbb9d0687fecc8d127c7f27468d6bfbd7706c822fe",
  "settings": {
    "is_hidden": false
  }
}
```

**MaxES3PixelShaderAdditiveComplexityCount** defines the range in the ES3 Preview Mode and is set to a default range of 800.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MaxES3PixelShaderAdditiveComplexityCount=800",
  "lines_of_code": 1,
  "id": 163124,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMxMjQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxODo0OSswMDowMCJ9--7455aa4346da210e9249f38fc76f50296e46670e90b72b432fc669842916a01a",
  "settings": {
    "is_hidden": false
  }
}
```

These Colors can be modified in the `BaseEngine.ini` file. The max pixel shader additive complexity count variables can also be overridden in your project's `DefaultEngine.ini` file.

## Stationary Light Overlap

![Stationary Light Overlap](https://dev.epicgames.com/community/api/documentation/image/24d881a7-231e-49ca-bc44-a540d2f83bef)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

## Lightmap Density

![Lightmap Density](https://dev.epicgames.com/community/api/documentation/image/c166cf58-7661-4380-9241-fb2bcb9ea93a)

_Click image for full size._

View Mode Hotkey: **Alt + 0**

**Lightmap Density** mode displays the lightmap density of objects that are texture mapped, color coding them by their relation to an ideal/max density setting and displaying a grid that maps to the actual lightmap texels. It is important to have even texel density across your scene to get consistent lightmap lighting.

| ![Lightmap Density Light](https://dev.epicgames.com/community/api/documentation/image/2491c6bb-de0e-4a81-9c24-cf7160db9487) | ![Lightmap Density Medium](https://dev.epicgames.com/community/api/documentation/image/695fef7f-6e95-42d1-b6f4-7e170ef7e7c2) | ![Lightmap Density Heavy](https://dev.epicgames.com/community/api/documentation/image/7504e048-a26a-43da-923d-0e91bd56468c) |
| --- | --- | --- |
| Less than ideal texel density | Ideal texel density | Max or greater than ideal texel density |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Skeletal Meshes will appear in light brown and are not considered in this calculation.",
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

## Reflections

![Reflections](https://dev.epicgames.com/community/api/documentation/image/3f21a8cb-f153-413d-acf7-bc72d5a26a1f)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Reflections** view mode overrides all materials with a flat normal and a roughness of 0, which is a mirror. This is useful for diagnosing the detail of reflections and allowing you to place more Reflection Capture Actors in areas where you need more detail.

## Player Collision

![Player Collision](https://dev.epicgames.com/community/api/documentation/image/009ad7b4-1309-4c36-a51b-f0674128c34d)

_Click image for full size._

- Console command: `viewmode CollisionPawn`

The **Player Collision** viewmode highlights assets that collide with a character or Pawn and uses the following colors:

| Player Collision Coloration |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
| **Color** | ![Image](https://dev.epicgames.com/community/api/documentation/image/acb2b9d4-d721-4016-a908-56e3f05e44bb) | ![Image](https://dev.epicgames.com/community/api/documentation/image/dbaaee64-fa57-4177-b8c4-3a709932559d) | ![Image](https://dev.epicgames.com/community/api/documentation/image/dac7fcfb-7666-4da9-8515-1038488e5c52) | ![Image](https://dev.epicgames.com/community/api/documentation/image/6eeebc15-7c8c-4ba4-9cb5-5ce2b7809763) | ![Image](https://dev.epicgames.com/community/api/documentation/image/7b5a2fda-85c2-4e52-a12b-cc87c7251a5c) | ![Image](https://dev.epicgames.com/community/api/documentation/image/5705b16d-ffa8-4ced-bafe-718259badefd) |
| **Description** | **Static Mesh** | **Stationary Static Mesh** | **Movable Static Mesh** | **Volume** | **Trigger Volume** | **Brush** |

## Visibility Collision

![Visibility Collision](https://dev.epicgames.com/community/api/documentation/image/f6964f2d-6804-4ffa-ba6c-c15de4545f4d)

_Click image for full size._

- Console command: `viewmode CollisionVisibility`

The **Collision Visibility** viewmode highlights whitch Actors will block visibility. It uses the following colors:

| Collision Visibility Coloration |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| **Color** | ![Image](https://dev.epicgames.com/community/api/documentation/image/f4e5e017-4e2e-4ec2-a5ce-6c0054098b41) | ![Image](https://dev.epicgames.com/community/api/documentation/image/95302600-8546-490b-a8bf-ab0868ba87a6) | ![Image](https://dev.epicgames.com/community/api/documentation/image/b1ce98b2-830d-412d-a462-b466552991ad) | ![Image](https://dev.epicgames.com/community/api/documentation/image/7e60bdab-69b0-4147-82e7-59d5ef5ce81e) | ![Image](https://dev.epicgames.com/community/api/documentation/image/0739082c-542f-42fd-8352-18dfa42f92a5) |
| **Description** | **Static Mesh** | **Stationary Static Mesh** | **Movable Static Mesh** | **Volume** | **Brush** |

## LOD Coloration

![Level of Detail Coloration Menu](https://dev.epicgames.com/community/api/documentation/image/d3f52a56-1636-4b86-86b2-1a2162aa6c23)

_Click image for full size._

![LOD Coloration](https://dev.epicgames.com/community/api/documentation/image/57ad9e1f-0fb0-4d4a-9bb0-7b934006cfcb)

_Click image for full size._

- Console command: `viewmode LODColoration`

**LOD Coloration** view mode displays the current LOD index of a primitive. This is useful for diagnosing any LOD issues or to see at which distance your LODs are switching.

| LOD Primitive Coloration |   |   |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | ![LOD Coloration_0](https://dev.epicgames.com/community/api/documentation/image/83ec2d4e-681b-49f3-8f59-aa0d445d7354) | ![LOD Coloration_1](https://dev.epicgames.com/community/api/documentation/image/e3936c03-c976-498f-bfbb-7fdc7ffcc1d4) | ![LOD Coloration_2](https://dev.epicgames.com/community/api/documentation/image/340bd008-dde8-407a-8731-d8ec6593ec4d) | ![LOD Coloration_3](https://dev.epicgames.com/community/api/documentation/image/12e1e13b-ee38-496e-abce-8ae0560e6287) | ![LOD Coloration_4](https://dev.epicgames.com/community/api/documentation/image/72ca4369-e32d-4d28-8621-ebb9bf52fc7b) | ![LOD Coloration_5](https://dev.epicgames.com/community/api/documentation/image/f8722f17-f46d-4c02-b116-8e1449cdb4a3) | ![LOD Coloration_6](https://dev.epicgames.com/community/api/documentation/image/565b189f-1c76-4c75-8a10-73bd6d712f9e) | ![LOD Coloration_7](https://dev.epicgames.com/community/api/documentation/image/17ebe058-cbff-4098-ada2-849e828eb95f) |
| **LOD Primitive Color** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** |

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "+LODColorationColors=(R=1.0,G=1.0,B=1.0,A=1.0)     \n+LODColorationColors=(R=1.0,G=0.0,B=0.0,A=1.0)     \n+LODColorationColors=(R=0.0,G=1.0,B=0.0,A=1.0)     \n+LODColorationColors=(R=0.0,G=0.0,B=1.0,A=1.0)     \n+LODColorationColors=(R=1.0,G=1.0,B=0.0,A=1.0)     \n+LODColorationColors=(R=1.0,G=0.0,B=1.0,A=1.0)     \n+LODColorationColors=(R=0.0,G=1.0,B=1.0,A=1.0)     \n+LODColorationColors=(R=0.5,G=0.0,B=0.5,A=1.0)",
  "lines_of_code": 8,
  "id": 163125,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMxMjUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxODo0OSswMDowMCJ9--1d90ffea2648025ea654d31fc8e720909d9dc6bb6d3691a2f5e722b6224ebe33",
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
      "content": "By default the engine uses only four LODs, but this can be extended in the source code.",
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

## HLOD Coloration

![Hierarchical LOD Coloration](https://dev.epicgames.com/community/api/documentation/image/40d6ff67-d836-406d-b5d8-408e9272f34d)

_Click image for full size._

- Console command: `viewmode hlodcoloration`

**HLOD Coloration** view mode displays the Hierarchial LOD Cluster index of a primitive.

| HLOD Primitive Coloration |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| **Color** | ![LOD Coloration_3](https://dev.epicgames.com/community/api/documentation/image/797cf27c-ed99-45fb-bc82-2b43845d88d3) | ![LOD Coloration_4](https://dev.epicgames.com/community/api/documentation/image/d56e1aa1-3c35-477b-b34c-621c3ad3b258) | ![LOD Coloration_7](https://dev.epicgames.com/community/api/documentation/image/91cf2fe7-b465-480b-9fb2-43187bfde72a) | ![LOD Coloration_6](https://dev.epicgames.com/community/api/documentation/image/dfaaa790-9d51-4c47-97db-52209a025d98) | ![LOD Coloration_8](https://dev.epicgames.com/community/api/documentation/image/61181b45-df94-4779-8ea6-86ab11e8695b) |
| **HLOD Primitive Color** | **0** | **1** | **2** | **3** | **4** |

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "+HLODColorationColors=(R=1.0,G=1.0,B=1.0,A=1.0)  //white (not part of HLOD)   \n+HLODColorationColors=(R=0.0,G=1.0,B=0.0,A=1.0)  //green (part of HLOD but being drawn outside of it)   \n+HLODColorationColors=(R=0.0,G=0.0,B=1.0,A=1.0)  //blue (HLOD level 0)   \n+HLODColorationColors=(R=1.0,G=1.0,B=0.0,A=1.0)  //yellow (HLOD level 1)   \n+HLODColorationColors=(R=1.0,G=0.0,B=1.0,A=1.0)  //purple   \n+HLODColorationColors=(R=0.0,G=1.0,B=1.0,A=1.0)  //cyan   \n+HLODColorationColors=(R=0.5,G=0.5,B=0.5,A=1.0)  //grey",
  "lines_of_code": 7,
  "id": 163126,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMxMjYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxODo0OSswMDowMCJ9--d5ebd077af5d5de4a4d7e1533f0f8849d604dea10d9a1f34bab3ae1d293e3e59",
  "settings": {
    "is_hidden": false
  }
}
```

## Buffer Visualization

![Buffer Visualization](https://dev.epicgames.com/community/api/documentation/image/728120a6-9338-4946-ba73-b6a850aa1b6c)

_Click image for full size._

The **Buffer Visualization** area offers you access to individual buffers within the graphics card, which can help you diagnose problems how your scenes look. In order to make the most out of the buffer visualization modes, it will help to understand the basics of [Material Inputs](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-inputs-in-unreal-engine) and [Material Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-properties).

### Buffer Overview

![Buffer Overview](https://dev.epicgames.com/community/api/documentation/image/2f34eb8e-9dc6-49b0-b08f-a3e46983b626)

_Click image for full size._

The **Buffer Overview** visualization mode allows you to see multiple images from the graphics card's GBuffer. Many of these correlate to inputs on Materials, meaning you can see how the scene looks with just a single Material input being used.

### Base Color

![Base Color](https://dev.epicgames.com/community/api/documentation/image/e13fc7ed-7e43-4227-8931-f57cbb0e74cd)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

The **Base Color** mode allows you to see the only the Base Color of the Materials in your scene.

### Decal Mask

![Decal Mask](https://dev.epicgames.com/community/api/documentation/image/773f4da7-0c84-48f6-8f2b-da293b2588a5)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

The **Decal Mask** mode shows in white any surface which can receive deferred decals. Objects which cannot, appear in black.

### Diffuse Color

![Diffuse Color](https://dev.epicgames.com/community/api/documentation/image/50503557-b287-4e01-89fa-f4b46a25b884)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Diffuse Color** shows the result of Base Color and the Material's Ambient Occlusion inputs.

### Shading Model

![Shading Model](https://dev.epicgames.com/community/api/documentation/image/6adff719-eb92-43fe-b205-d1f51fb3c007)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

The **Shading Model** mode shows value of the Shading Model property for each Material in the scene.

| Light Complexity Coloration |   |   |   |   |
| --- | --- | --- | --- | --- |
| **Color** | ![Light Model Lit](https://dev.epicgames.com/community/api/documentation/image/d02cc398-6ae6-47e7-8338-ac9e3e2681f6) | ![Light Model Unlit](https://dev.epicgames.com/community/api/documentation/image/a596be6e-f59a-4cad-8bc7-3c7d0f2bda4b) | ![Light Model Subsurface](https://dev.epicgames.com/community/api/documentation/image/4420439c-df16-4830-ada2-5a43c176e7f6) | ![Light Model Preintegratedskin](https://dev.epicgames.com/community/api/documentation/image/f5b36809-833d-42ee-b516-7399a00c42fe) |
| **Material's Shading Model** | **Default Lit** | **Unlit** | **Subsurface** | **Preintegrated Skin** |

### Material AO

```json
{
  "type": "comparison_slider",
  "image_left_id": 26457089,
  "caption_left": "Scene in Lit Mode (Game View On)",
  "image_right_id": 26457090,
  "caption_right": "Scene in Buffer Material AO Mode (Game View On)",
  "image_left": {
    "id": 26457089,
    "file_name": "24-scene-in-lit-mode.png",
    "file_size": 1709783,
    "content_type": "image/png",
    "created_at": "2026-02-19T21:22:09.060+00:00",
    "height": 804,
    "width": 1334,
    "storage_key": "b3f6897d-3a59-4d95-878c-13f2196dc9b6",
    "context": "documentation"
  },
  "image_right": {
    "id": 26457090,
    "file_name": "25-scene-in-buffer-material-ambient-occlusion.png",
    "file_size": 888328,
    "content_type": "image/png",
    "created_at": "2026-02-19T21:22:09.238+00:00",
    "height": 804,
    "width": 1334,
    "storage_key": "208f73b6-d814-4a52-9681-f31b63b958c6",
    "context": "documentation"
  },
  "image_left_storage_key": "b3f6897d-3a59-4d95-878c-13f2196dc9b6",
  "image_right_storage_key": "208f73b6-d814-4a52-9681-f31b63b958c6",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

- View Mode Hotkey: **None (Menu only by default)**

The **Material AO** visualization mode shows the result of any texturing or Material Expression nodes that are connected to the Material's *Ambient Occlusion* input.

### Metallic

![Metallic](https://dev.epicgames.com/community/api/documentation/image/cac66dab-7854-4775-a95a-02fecb2b152b)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

The **Metallic** visualization mode shows the result of any texturing or Material Expression nodes that are connected to the Material's *Metallic* input.

Note: Materials should generally have Metallic values of 0 or 1, not in between. Values between 0 and 1 will happen due to layer blending, but physical materials will always be a metal or not.

### Opacity

```json
{
  "type": "comparison_slider",
  "image_left_id": 26457091,
  "caption_left": "Scene in Lit Mode",
  "image_right_id": 26457092,
  "caption_right": "Scene in Buffer Material Opacity Mode (Game View On)",
  "image_left": {
    "id": 26457091,
    "file_name": "27-scene-in-lit-mode.png",
    "file_size": 1709783,
    "content_type": "image/png",
    "created_at": "2026-02-19T21:22:09.478+00:00",
    "height": 804,
    "width": 1334,
    "storage_key": "b9ef67a3-6cf3-4c87-b427-0389f07f987a",
    "context": "documentation"
  },
  "image_right": {
    "id": 26457092,
    "file_name": "28-scene-in-buffer-material-opacity-mode.png",
    "file_size": 409574,
    "content_type": "image/png",
    "created_at": "2026-02-19T21:22:09.718+00:00",
    "height": 804,
    "width": 1334,
    "storage_key": "a4047d66-8beb-4566-924a-b12903915773",
    "context": "documentation"
  },
  "image_left_storage_key": "b9ef67a3-6cf3-4c87-b427-0389f07f987a",
  "image_right_storage_key": "a4047d66-8beb-4566-924a-b12903915773",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

- View Mode Hotkey: **None (Menu only by default)**

**Opacity** visualization mode shows the result of any texturing or Material Expression nodes that are connected to the Material's Opacity input. In the images above, you can see the outer shell of the character is somewhat transparent.

The Opacity viewmode only shows opaque materials with Opacity being used, which is important in the case of subsurface scattering materials, as the Opacity controls how far light can penetrate.

### Roughness

![Roughness](https://dev.epicgames.com/community/api/documentation/image/0cb807c8-04f6-40f1-829e-a4e8fcddaa96)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Roughness** visualization mode shows the result of any texturing or Material Expression nodes that are connected to the Material's Roughness input. Roughness variation is where a lot of reflection variation will come from.

### Scene Color

![Scene Color](https://dev.epicgames.com/community/api/documentation/image/3134aa4a-3565-4872-afff-7a3e4382622c)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Scene Color** shows the result of the scene before any post processing is done. This means before any exposure, bloom, color correction, or antialiasing. In the above image, the scene appears very dark because exposure has not brightened it up for us.

### Scene Depth

![Scene Depth](https://dev.epicgames.com/community/api/documentation/image/da9e35f0-383e-4849-bced-1273b213212e)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Scene Depth** shows the depth of the scene in a constant gradient from white (farthest away) to black (closest).

### Separate Translucency RGB

![Separate Translucency RGB](https://dev.epicgames.com/community/api/documentation/image/8030af65-1b34-4f8e-9aee-662eb47b73bb)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Separate Translucency RGB** shows the color information of any Materials that are Translucent and using Separate Translucency.

### Separate Translucency A

![Separate Translucency A](https://dev.epicgames.com/community/api/documentation/image/fca7afb7-3e9d-4630-ae21-a61db5fa73cd)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Separate Translucency A** shows only the alpha information of any Materials that are Translucent and using Separate Translucency.

### Specular Color

![Specular Color](https://dev.epicgames.com/community/api/documentation/image/2cd0e5ee-dc39-405f-8b3d-3fc74fe06840)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Specular Color** shows the color being imparted to the specular reflections of a Material. Generally, this is inferred from a combination of the Base Color and Metallic values.

### Specular

![Specular](https://dev.epicgames.com/community/api/documentation/image/474849fc-3c54-42bc-a3c3-167190457ccf)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Specular** shows the results of any texturing or Material Expression nodes that are fed into a Material's Specular input.

### Subsurface Color

![Subsurface Color](https://dev.epicgames.com/community/api/documentation/image/3a49c2d0-74fa-45fa-a427-f73e6fd4efcf)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Subsurface Color** shows the results of any texturing or Material Expression nodes that are fed into a Material's Subsurface Color input.

### World Normal

![World Normal](https://dev.epicgames.com/community/api/documentation/image/c0db531d-89df-450f-8200-7b1c785014a2)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**World Normal** shows the world space normal of any opaque surfaces.

### Ambient Occlusion

![Ambient Occlusion](https://dev.epicgames.com/community/api/documentation/image/4bc0129e-7b45-4c08-ba6c-b172d0cb4212)

_Click image for full size._

- View Mode Hotkey: **None (Menu only by default)**

**Ambient Occlusion (AO)** shows the result of any ambient occlusion calculations that are taking place on the scene. This is separate from any AO textures applied to Materials, as this is a calculation the engine makes based on surfaces and normal maps.

## Landscape Visualizers

![Landscape Visualizers](https://dev.epicgames.com/community/api/documentation/image/c856811d-4790-4156-b337-f63f08f2eeb3)

_Click image for full size._

### Normal

![Landscape Normal](https://dev.epicgames.com/community/api/documentation/image/2f14bb50-5e10-4193-b036-ccefb23e17a9)

_Click image for full size._

The **Normal** Landscape visualization mode shows a Landscape in its normal, lit state.

### LOD

![Landscape LOD](https://dev.epicgames.com/community/api/documentation/image/4ebf53fe-b7bf-44ee-b555-6c023ea82f3a)

_Click image for full size._

The **LOD** Landscape visualization mode breaks a landscape up into color-coded panels which represent their current LOD state.

### Layer Density

![Layer Density](https://dev.epicgames.com/community/api/documentation/image/8cff6896-3de6-4c94-bc87-ed5dc09e7520)

_Click image for full size._

The **Layer Density** Landscape visualization mode shows the landscape in a color-coded mode which shifts from green to red as more layers are added to the Landscape.

## Exposure

![Exposure](https://dev.epicgames.com/community/api/documentation/image/772431ab-8be5-41fc-abe0-0df827d4ec23)

Exposure is a post-processing effect that controls the overall brightness of a scene. This can be set to a fixed value or left to automatic.

### Automatic vs. Fixed Exposure

When playing games with Exposure activated in your post processing, you will notice that moving from a light to a dark area or vice versa will cause the camera to temporarily adjust, similarly to how our eyes adjust when moving to different light environments. In most cases, this will be the desired result. However, if the constant shifting is distracting in your particular level, then you can set the view to a fixed exposure. This will lock the exposure in place so it no longer automatically changes as you move from light to dark or dark to light, but it also means that you can easily end up in a situation where the lights are overbright or overdark for the work you need to do.
