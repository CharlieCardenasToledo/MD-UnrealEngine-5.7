# First Person Rendering

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-rendering

> Application Version: 5.7

Native first-person rendering supports functionality often required when creating experiences using a first-person camera perspective, such as being able to render only certain objects with a field of view that differs from the one rendering the rest of the scene. For example, rendering things like the character's hands and arms or weapons are ideal for first person rendering so that they don’t clip with (protrude into) walls as you get close to them.

The First Person rendering offers the following features:

- Render first person primitives with a custom field of view (FOV).
- Apply a scaling factor to first person primitives to effectively shrink them closer towards the camera, making it possible to avoid most cases where first person geometry would intersect, often called clipping, with the scene. This enables first person primitives to always render on top of the scene.
- Includes a complete shadowing solution where first person geometry receives scene shadows, it casts shadows on itself, and players can see their own shadow being cast onto the scene.
- Has integration with [Hardware Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) (HWRT) whereby players can see themselves reflected in the scene, and they can cast ray-traced shadows.
- Integration with materials: Per-vertex control over the first person effect. This optional output allows for interpolating between world space and what is considered first person space. It is useful when there is a need to have some parts of the geometry be in world space to connect with the world, such as having the characters feet on the ground. Use the material graph to query first person rendering parameters and to transform arbitrary positions from world space into first person space.

- It works on most primitive types. This includes static meshes, skinned meshes, and [Niagara Particle Effects](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine).

## First Person Rendering Implementation

For development of first-person games, you usually want the player camera to render first person geometry in a way that it has a custom field of view and does not intersect with the world. The implementation of First Person rendering in Unreal Engine can be thought of as morphing the first-person geometry in such a way that it achieves the desired effect of a custom field of view and has anti-clipping behavior. This morphing happens after World Position Offset is applied but before the vertex is projected into clip space.

Consequently, the geometry technically exists in world space but for the most part looks like it is rendered with a different projection matrix. The caveat here is that the geometry is now very small and slightly skewed. This is done so that it will look good from the point of view of the camera, but it is unsuitable for other perspectives and therefore shouldn’t cast shadows on the scene or be visible in hardware ray tracing reflections — which is prevented by design.

The advantage of implementing First Person rendering in this way is that it allows first person primitives to render in the same pass as other primitives, thus avoiding the need for, or the complexity of, additional rendering passes which would have an impact on memory and performance.

### First Person Primitives Settings

Components include a setting to determine how they are rendered by the first-person camera when their **First Person Primitive Type** is set to **First Person** or **World Space Representation**.

![Image](https://dev.epicgames.com/community/api/documentation/image/edb2d5d4-6de7-4d59-8a02-89418017bdf1)

_First Person settings for Primitives._

This setting includes the following selection:

- **None:** This primitive does not interact with first person rendering.
- **First Person:** This primitive is rendered as first person and is affected by first person properties on the camera for First Person Field of View and First Person Scale, which are used to render the component with different fields of view and smaller depth range such that clipping with the scene can be avoided. The primitive does not cast shadows onto the scene and will also not be visible in the raytracing world.
- **World Space Representation:** This primitive represents a first person primitive in world space. This is the primitive that other players would see and is used to cast shadow onto the ground and for reflections with hardware ray tracing, among other things. It is invisible to the owning first person camera. This implicitly sets Cast Hidden Shadow to false and Owner No See to true behind the scenes, which is required for first person shadow to work correctly with Virtual Shadow Maps.

### First Person Shadows

There are two considerations for shadowing you need to take into account when setting up a player character using first person rendering:

- Enabling lights to cast shadows so that primitives set to First Person can cast shadows onto themselves.
- Setting up components that are the world space representation of first person primitives for scene shadows and reflections.

#### First Person Self-Shadow

**First Person Self-Shadowing** is a specialized shadowing solution for primitives rendered in first person perspective. It enables these first person primitives to cast shadows on themselves, such as a weapon casting a shadow onto itself and the player’s arm, but not onto the scene. This prevents the geometry that is morphed and skewed to the first person camera perspective from being visible in the scene shadows.

Currently, first person self-shadowing is implemented with screen space tracing. While this method is fairly cheap, it is limited to only shadow casters on screen. For most first person setups this won’t be a problem in practice since  all relevant shadow casters are usually on the screen. Keep in mind that other typical limitations of screen space rendering also apply to first person rendering, such as a single layer depth buffer (rays can go behind geometry).

Below are examples with a Directional light that has enabled First Person Self Shadow.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26059378,
  "caption_left": "First Person Self-Shadow: Disabled",
  "image_right_id": 26059379,
  "caption_right": "First Person Self-Shadow: Enabled",
  "image_left": {
    "id": 26059378,
    "file_name": "FP_SelfShadow_OFF.png",
    "file_size": 1549322,
    "content_type": "image/png",
    "created_at": "2025-09-12T13:25:01.787+00:00",
    "height": 783,
    "width": 1434,
    "storage_key": "9121ea25-b546-4b88-8056-7f5d1b2d669d",
    "context": "documentation"
  },
  "image_right": {
    "id": 26059379,
    "file_name": "FP_SelfShadow_On.png",
    "file_size": 1524641,
    "content_type": "image/png",
    "created_at": "2025-09-12T13:25:01.991+00:00",
    "height": 783,
    "width": 1434,
    "storage_key": "974f5960-a47b-4a39-acdb-a05b35b10369",
    "context": "documentation"
  },
  "image_left_storage_key": "9121ea25-b546-4b88-8056-7f5d1b2d669d",
  "image_right_storage_key": "974f5960-a47b-4a39-acdb-a05b35b10369",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

First Person Self-Shadow is currently (as of 5.6) controlled with console variables. This was done to make it easier to control the effect in maps with many lights. The effect only actually costs performance if the light overlaps the first person geometry, so assuming there are little to no overlapping lights, it’s fine to enable it on all local lights. However, this means of controlling the feature might change in the future.To set up First Person Self-Shadow, follow these steps:

1. Set `r.FirstPerson.SelfShadow` to **`1`**. This enables the feature on shadow casting lights (Cast Dynamic Shadows) as determined by the following console variable:
2. Set `r.FirstPerson.SelfShadow.LightTypes` to: `0`, enabling First Person Self-Shadow only on directional lights `1`, enabling it on local lights only `2`, enabling it on all lights (local and directional)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Enabling <b>First Person Self Shadow</b> does have some small impact on performance. Having many overlapping lights with it enabled might affect performance negatively. Be mindful of the light sources you’re enabling this on. For additional info on limitations of this feature, see the <a data-anchor-id=\"18211\" data-document-id=\"3962921\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-rendering#limitations-and-notes\">Limitations</a> section below. ",
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

#### First Person World Space Representation Shadows

When you have a first person player character that has the property **First Person Primitive Type** set to **First Person**, shadows are not cast onto the scene from these components. Having a mesh that is seen by the world and other players is necessary to cast a shadow, and its primitive type must be set to **World Space Representation**. Once set, this mesh will cast shadows onto the scene, along with making this primitive visible in hardware ray-traced reflections.

### Setting Up A First Person Camera

When setting up a camera for first person rendering, the complexity depends on the type of game or experience you’re building. You can follow along with the basic setup below to get you started with a first person player character. The advanced setup offers guidance on setting up parts of your character that are viewed by the world, or other players in a multiplayer game.

For example, in a basic setup, you would set up a character with only components you would see while in a first person perspective. This can be a skeletal mesh with only arms to hold a weapon. In an Advanced setup, you can add to this by adding visible legs in first person and a full character mesh that is visible to the world for casting shadows and appearing in reflections.

#### Basic Setup of a First Person Camera

The process of creating a First Person camera setup is fairly straightforward; primitives can be tagged as being first person and cameras can be configured to apply a custom field of view and scaling to these assets separate from the rest of the scene’s rendering.

The steps to do this can be broken up into two categories:

- Setting up the components and their initial settings.
- Configuring properties of these components to fit the look of your primitives and first person game

#### Setting up the Camera and First Person Components

Follow these steps to set up the camera and its first person components:

1. Create a new **Camera** actor.
2. In the Details panel, click **Add** and select a desired **Primitive** component (Static Mesh, Skeletal Mesh, Particle System, and so on) to add to this actor. ![Add a primitive component.](https://dev.epicgames.com/community/api/documentation/image/7afba4fe-5c40-4f8a-9674-5e26bd8385ef) With the Primitive component selected, use the **Details** panel to locate the property **First Person Primitive Type** under **Rendering > Advanced** properties. Use the dropdown selection to set it to **First Person**. ![Set the First Person Primitive Type to First Person.](https://dev.epicgames.com/community/api/documentation/image/c51abd72-6d18-4e63-bcad-d2b026ecdad4) In the Details panel, click on the **Camera Component** and check the boxes next to **Enable First Person Field Of View** and **Enable First Person Scale** under **Camera Options** properties. ![Enable First Person Field of View and First Person Scale on the Camera Component.](https://dev.epicgames.com/community/api/documentation/image/2eef1abc-f602-4ed1-a915-33d14d86476c)

With the **Camera Component** selected, you can observe the results in the camera preview window in the bottom-right corner of the editor viewport.

![First Person Camera view result.](https://dev.epicgames.com/community/api/documentation/image/7005d7cf-5924-4d41-9fe9-a5770f10f158)

#### Configuring First Person Field of View and Scale Settings

When you’ve enabled the Camera Component properties for **Enable First Person Field of View** and **Enable First Person Scale**, you can use the similarly named settings under the **Camera Settings** category to make adjustments.

![First Person field of view and scale camera settings.](https://dev.epicgames.com/community/api/documentation/image/e50b5ede-b6b6-4542-914d-d04550b15a35)

_First Person Field of View and First Person Scale camera settings._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "These settings will work for this camera on any primitives that have had their <b>First Person Primitive Type</b> set to <b>First Person</b>. Otherwise the camera will see them in World Space. Use the Camera Preview window in the viewport to inspect the changes. The editor viewport still shows any First Person primitive as unchanged. This is because the implicit camera used for the viewport does not have the first person properties set up. ",
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

You can adjust the **First Person Field of View** value to change the horizontal field of view (in degrees) of any primitives this First person camera renders. When you adjust the field of view slider, you can observe the primitive’s field of view changing in the camera preview window.

[Video: V_vMQ5iy](https://dev.epicgames.com/community/api/cms/videos/V_vMQ5iy/embed.html)

You can adjust the **First Person Scale** value to scale down “first person” primitives towards the camera such that they are small enough to not intersect with the scene for this First Person camera. From the camera’s point of view, the primitive should look the exact same, even though it’s now smaller. When the scale value is too small, the primitive will disappear. This is because it’s been scaled small enough that it intersects the near clipping plane.

[Video: V_LqHFqF](https://dev.epicgames.com/community/api/cms/videos/V_LqHFqF/embed.html)

When adjusting the scale for a proper setup with your camera and primitives, you should find a scale value that is small enough to not cause clipping with the scene but that is big enough to not disappear because of the Near Clip Plane. In practice, it is often sufficient to scale down the first person geometry only as much as is required for it to be contained in the player bounds.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Depending on your content and setup, it may be necessary to adjust the Near Clip Plane’s default value for the editor. You can adjust this in the project settings under <b>Engine &gt; General</b> settings with the <b>Near Clip Plane</b>, but this does adjust it globally for the entire project.  ",
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

[Video: V_Y31AzM](https://dev.epicgames.com/community/api/cms/videos/V_Y31AzM/embed.html)

The advanced setup of the First Person camera and components is similar to how you would set up this view using the basic setup outlined above. When using the advanced setup below, you'll want to consider how the character is represented in the world for a multiplayer game or how they're represented in game scenes using hardware ray tracing features. This will ensure consistency between how the player is seen by the world — or other players — around them. It also affects how the player sees their character in shadows and reflections.

Consider the following when using the advanced first person workflow:

- Adding World Space Representation primitives for casting shadow onto the world.
- a character's feet in first person and having the feet connect to the shadows cast by the player onto the ground.
- Player reflections when viewing themselves with hardware ray-traced reflections.

All of these features require a suitable representation of the first person primitives in the world. That representation is what other players would see in a multiplayer game when they look at this player. Alternatively, you can think of this as the third-person version of the player character. In Unreal Engine, this is called the **First Person World Space Representation**. It is used to cast shadows onto the scene and is how the player is represented in the raytracing scene.

#### First Person Geometry

First Person geometry should include a mesh for the lower body and legs. This mesh can either be completely in World Space or could use an interpolation gradient in the material to have the feet fully in World Space, and the rest of the body in First Person space (see the [Integration with Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-rendering#integration-with-materials) section below).

This setup alone will improve realism as players can now see their own legs when looking down in First Person view.

#### Set Up of First Person Components and Their World Space Representations

In the [Basic Setup of a First Person Camera](https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-rendering#basic-setup-of-a-first-person-camera), the components you want seen by only the first person camera have their **First Person Primitive Type** set to **First Person**. For any geometry you want to be seen in world space by features like hardware raytraced reflections or other players in multiplayer games, you can set the primitive type to **World Space Representation**, and this ensures they can cast shadows onto the world and have player representation in ray-traced reflections.

In the scene below, there are two immediate things to be aware of when setting a component to **World Space Representation**:

- The component is no longer visible to the first person camera in the camera preview window.
- The component casts a shadow onto the world.

![First Person components and their world space representations.](https://dev.epicgames.com/community/api/documentation/image/027d3b8f-ae26-4294-bc95-2f0455ed959c)

_First Person components and their world space representations._

Behind the scenes, this World Space Representation option uses the “Owner No See” functionality to hide the geometry from the camera, but this requires that the primitives be owned by the camera, which can be achieved by making them child components of the camera actor.

Once you have a character set up with a first person mesh primitive and a World Representation mesh primitive, the feet of your first person mesh should line up with its world representation. You can see an example of this set up below looking at the first person primitives only and then the combined first person and world representation primitives to cast shadows onto the scene and have them “connect” the shadows at the feet of your character.

|   |   |
| --- | --- |
| ![First person mesh only.](https://dev.epicgames.com/community/api/documentation/image/40eb19b4-2aea-46ed-81cd-0857c7abf108) | ![First person mesh with world representation mesh casting shadows.](https://dev.epicgames.com/community/api/documentation/image/42ec43a2-b7db-4b2b-8a66-1d99ff8b4f3f) |
| **Only the first person mesh primitive set the “First Person” is shown. This mesh doesn’t cast shadows onto the scene.** | **Both the mesh primitives set to First Person and World Representation are shown together. The World Representation mesh is invisible to the first person camera but casts shadows onto the world. These should line up with the First Person primitive mesh.** |

To the world, or any other players in a multiplayer setup, your character’s mesh and components should be set to World Space Representation.

The demonstration below shows a “world” camera looking at the first person character reflected on a mirror-like surface. You can also see the first person camera view and how the world representation mesh is viewed when set to None, First Person, or World Space Representation and how this affects its ability to cast shadows on the scene, or be rendered by the first person camera.

[Video: V_4ofvBD](https://dev.epicgames.com/community/api/cms/videos/V_4ofvBD/embed.html)

## Integration with Materials

The material graph includes the following nodes that support first person rendering configurations:

### First Person Output Node

The **First Person Output** node uses an alpha value to interpolate between world space and first person space using values between 0 and 1 on a per-vertex frequency. This is very useful if first person geometry needs to connect to the rest of the scene. One example of this would be having the feet mesh of the first person character geometry connecting to the ground. You can achieve this by applying a gradient from 0.0 (world space) to 1.0 (first person space) along the length of the legs (which would be set as a first person primitive).

![First Person Output material expression.](https://dev.epicgames.com/community/api/documentation/image/f5fe078d-77e2-416d-9f88-de1254c24406)

_First Person Output material expression._

Alternatively, you can also use **Set Material Attributes** to set the same property without needing to add the First Person Output node to the material. This is useful in cases where you want to set the value from a material function, as material functions do not allow usage of custom output nodes.

![First Person Set Material Attributes material expression.](https://dev.epicgames.com/community/api/documentation/image/8e01c15b-eb42-457e-8f31-366f4731517c)

_First Person Set Material Attributes material expression._

### Transform Position Node

The **Transform Position** node supports transforming arbitrary positions to first person space. This is useful for calculating where some point would end up on the screen when it is rendered as first person.

![First Person Transform Position material expression.](https://dev.epicgames.com/community/api/documentation/image/368f4085-01af-48be-ad63-6c7f8d3e519f)

_First Person Transform Position material expression._

With the node selected, use the **Details** panel to set the following:

![First Person Transform Position settings.](https://dev.epicgames.com/community/api/documentation/image/eddee3e3-4e98-4b03-a997-073c6d7e9d7e)

_First Person Transform Position settings._

- **Source:** Camera Relative World Space This is the source format of the position that will be transformed.
- **Destination:** First Person Space (Camera Relative World Space) This is the type of transform to apply to the input expression.
- **(Optional) First Person Interpolation Alpha:** 0 to 1 This interpolates between translated world space and first person space, where 0 is world space and 1 is first person space. This node can be used in any material, including post process materials, where it can be used to transform any arbitrary position to first person so we can't know the value of the First Person Output node. This value is supplied by the user for what makes sense for their game, but in most cases, it is sensible to leave the default value. An example of when to use this node is when calculating where the reticule should be at in first person for something like a scoped weapon's post process material. In this case, you can assume that every position that needs to be cared about (points on the gun and scope) will be fully in first person.

### Is First Person Node

The **Is First Person** node can be used to apply different effects in the material depending on whether the current primitive being rendered has its **First Person Primitive Type** set to **First Person** or not.

![Is First Person material expression.](https://dev.epicgames.com/community/api/documentation/image/3fcafa40-85c2-4445-8d0a-6e0cc7eb316d)

_Is First Person material expression._

The material graph below is a simple setup using the IsFirstPerson node to set a color for geometry that is rendered in World Space (red) versus First Person Space (green).

![Example using the Is First Person material expression.](https://dev.epicgames.com/community/api/documentation/image/de550a4b-5277-4439-9b55-2e526bcf2dec)

_Example using the Is First Person material expression._

In the scene below, you can see how this material with the Is First Person node is used to drive the color of the rifle used for its world space representation and the first person view. The First Person Rifle primitive (green) is visible in the player camera (bottom right) and is rendered with the first person parameters on the camera. The World Space Representation Rifle (red) is invisible to the player camera, but it is used to cast shadow onto the ground and will be seen by hardware ray-traced reflections and shadows in the raytracing world.

![Example scene using the Advanced Setup of a First person Camera with first person and world space representation mesh primitives.](https://dev.epicgames.com/community/api/documentation/image/ee7143d3-33d0-4a04-82f1-11484e8babfb)

_Example scene using the Advanced Setup of a First person Camera with first person and world space representation mesh primitives._

### View Property Node

The **View Property** node can be used for querying the **First Person Field of View** and **First Person Scale** of the current view.

- **First Person Field of View** returns the horizontal and vertical first person field of view angles in radians. ![First Person Field of View material expression](https://dev.epicgames.com/community/api/documentation/image/6581e5eb-a3bc-48d2-b352-0372fb262cd2)
- First Person Scale returns the scaling factor applied to first person primitives to keep them from intersecting with the scene. ![First Person Scale material expression](https://dev.epicgames.com/community/api/documentation/image/71064181-8ae4-4e9b-9bec-85cf3513733b)

With the node selected, use the **Details** panel to set the **View Property** dropdown list to the view you want to query.

![First Person View Property Selection.](https://dev.epicgames.com/community/api/documentation/image/816b3c2c-5958-4cc8-9650-3b2fb99912b4)

### Scene Texture Node

The **Scene Texture** node can sample the GBuffer to tell whether a given pixel was drawn by a first person primitive that uses an opaque material.

![Scene Texture: Is First Person material expression.](https://dev.epicgames.com/community/api/documentation/image/3559ca1c-9746-478b-a265-cc818e9e3b41)

_Scene Texture: Is First Person material expression._

With the node selected, use the **Details** panel to set the **Scene Texture Id** dropdown list to set the scene texture to **IsFirstPerson.**

![IsFirstPerson Scene Texture ID](https://dev.epicgames.com/community/api/documentation/image/7ca787d8-0f0b-425e-a70b-4770451deed7)

_IsFirstPerson Scene Texture ID_

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "  For additional info, see the <a data-anchor-id=\"18211\" data-document-id=\"3962921\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-rendering#limitations-and-notes\">Limitations</a> section below.",
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

## Limitations and Notes

- The custom first person field of view (FOV), anti-clipping scaling, the per-vertex interpolation controls and most of the material graph integration features work on all platforms and in all configurations.
- **First Person GBuffer Bit** Certain advanced first person rendering features require first person pixels to be marked with a bit in the GBuffer. The first consequence of this is that these features do not work with the mobile renderer or with forward rendering. The second consequence is that **Allow Static Lighting** needs to be **disabled** in the project settings. By disabling static lighting for the project, some GBuffer bits are freed up to be used by first person rendering. This might change in the future, but as of 5.6, this is a tradeoff that needs to be made. Alternatively, very advanced users could instead decide to do local changes to their version of Unreal Engine and instead sacrifice a different feature in the GBuffer that is not needed for their project. The impacted features are as follows: First Person Self-Shadow Using World Space Representation primitives to cast shadow onto the scene. Seeing World Space Representation primitives reflected in the scene. Using the Scene Texture node to tell whether a given pixel is first person. All these features have a graceful fallback in case the first person GBuffer bit is not available: Shadows and reflections will simply not be there and the Scene Texture node will always return 0.0 (false).
- **General Feature Support** Without Virtual Shadow Map (or Ray-traced Shadows) there won't be first person shadows on the ground. Grooms and strand-based hair is currently not supported.

## Additional Resources

### First Person Template

The **First Person Template** is setup to use native First Person rendering. You can explore the First Person Shooter variant when creating the First Person template to see this feature in action.

[Video: V_NV8CV0](https://dev.epicgames.com/community/api/cms/videos/V_NV8CV0/embed.html)

For more information on this template, see [First Person Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.5).
