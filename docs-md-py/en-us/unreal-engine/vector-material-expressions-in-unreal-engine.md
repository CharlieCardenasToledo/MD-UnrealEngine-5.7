# Vector Material Expressions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine

> Application Version: 5.7

This page documents the available Vector Material Expressions that output vector values mapped to RGBA. These are useful for many different spatial Material effects, including getting an object's position in world space so that the Material can react, or transitioning colors on a character when they enter a specific area. There are many others that enable you to control local Material effects that you can learn more about in the examples below.

## ActorPositionWS

**ActorPositionWS** outputs Vector3 (RGB) data representing the location of the object with this material on it in world-space.

![Actor Position WS expression](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53445aab-229e-434d-b74d-d05eead79c52/actor-position-ws.png)

In this example, ActorPositionWS is passed directly into the Base Color of the Material. As a result, each of the objects with the Material applied to them show a different color as they are moved to different locations in 3D space. Note that the result of the ActorPositionWS node is being divided by 1600 to create a nice blend-in color, rather than an abrupt pop.



## CameraPositionWS

The **CameraWorldPosition** expression outputs a three-channel vector value representing the camera's position in world space.

In the example below, Camera Position is passed into the base color of the Material. Note how the preview sphere changes color as the camera position changes.

## CameraVectorWS

The **CameraVector** expression outputs a three-channel vector value representing the direction of the camera with respect to the surface. In other words, the direction from the pixel to the camera.

**Example Usage:** CameraVector is often used to fake environment maps by connecting the CameraVector to a ComponentMask and using the X and Y channels of the CameraVector as texture coordinates.

![Camera Vector example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f87352e2-bb2c-4bdf-89ea-68d9e3287f50/camera-vector-ws.png)

## Constant2Vector

The **Constant2Vector** expression outputs a two-channel vector value, in other words, two constant numbers.

| Property | Description |
| --- | --- |
| **R** | Specifies the float value of the red (first) channel of the vector the expression outputs. |
| **G** | Specifies the float value of the green (second) channel of the vector the expression outputs. |

**Examples:** (0.4, 0.6), (1.05, -0.3)

**Example Usage:** The Constant2Vector is useful for modifying texture scale or offset, as UV coordinates require two-channel values.

![Constant2Vector Example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/072b88b5-0c58-442e-aed9-0848ea268122/constant-2-example.png)


To quickly create a Constant2Vector node, hold the **2** key and **left-click** anywhere in the background of the Material Graph.

## Constant3Vector

The **Constant3Vector** expression outputs a three-channel vector value, in other words, three constants numbers. A Constant3Vector is often used to define a solid RGB color, where each channel is assigned to a color (red, green, blue). You can double-click the Constant3Vector node in the Material Graph to summon a color picker dialog.

| Property | Description |
| --- | --- |
| **R** | Specifies the float value of the red (first) channel of the vector the expression outputs. |
| **G** | Specifies the float value of the green (second) channel of the vector the expression outputs. |
| **B** | Specifies the float value of the blue (third) channel of the vector the expression outputs. |

**Examples:** (0.4, 0.6, 0.0), (1.05, -0.3, 0.3)

In this example an Constant3Vector is multiplied by a Texture Sample to change the tint of the texture.

![Constant3Vector Example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c6dd366-edf7-4e61-bc1a-1a2e78bc359e/color-tint-constant-3-vector.png)


To quickly create a Constant3Vector node, hold **3** key and **left-click** anywhere in the Material Graph.

## Constant4Vector

The **Constant4Vector** expression outputs a four-channel vector value, in other words, four constant numbers. You can use the Constant4Vector expression to define RGBA color, where each chanel is assigned to a color (red, green, blue, alpha).

| Property | Description |
| --- | --- |
| **R** | Specifies the float value of the red (first) channel of the vector the expression outputs. |
| **G** | Specifies the float value of the green (second) channel of the vector the expression outputs. |
| **B** | Specifies the float value of the blue (third) channel of the vector the expression outputs. |
| **A** | Specifies the float value of the alpha (fourth) channel of the vector the expression outputs. |

**Examples:** (0.4, 0.6, 0.0, 1.0), (1.05, -0.3, 0.3, 0.5)

In the example below, a Constant4Vector expression is used to define both the **Base Color** and **Opacity** of the Material. The top pin outputs the RGB color, while the bottom pin outputs the value in the alpha channel. The alpha value of 0.5 results in a semi-transparent Material.

![Constant4Vector Example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80138764-eff2-4c09-91d0-699723a90df6/constant-4-example.png)


To quickly create a Constant4Vector, hold the **4** key and **left-click** anywhere in the background of the Material Graph.

## LightVector

When used with a **Deferred Decal** Material and Decal actor, the LightVector Material Expression outputs Vector (RGB) data, which represents the normalized (in a range between 0 and 1) position of the current pixel relative to decal projection box, in the decal's coodinate space.

If used with a **LightFunction** Material, the LightVector Material Expression outputs Vector (RGB) data representing the vector from the light to the pixel, in the light's coordinate space.

In other Material Domains, the LightVector expression is unused.

The LightVector Material Expression should only be used with the **Deferred Decal** or **LightFunction** Material Domains.

### Example

You can use the LightVector Material Expression to create a linear falloff effect for a Deferred Decal. In the graph below, there are two parameters which control the depth and falloff of the blend between the decal and the receiving surface.

The result is shown below.

## Object Bounds

The **Object Bounds** expression outputs the size of the object on which the Material is applied for each axis. The expression outputs a float3, representing the X, Y, and Z axis. If this node is plugged into Base Color, the axes correspond to R, G, and B, respectively.

![Object Bounds graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/866c9160-9304-46ba-97a9-fc3618b65ce2/object-bounds-graph.png)

In the video below, note how the Material changes color when the object is scaled on each axis.



## ObjectOrientation

The **ObjectOrientation** expression outputs the world-space up vector of the object on which the Material is applied. In other words, the object's local positive z-axis is pointing in this direction.

![Object Orientation expression](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20beb353-b166-46c5-8f6a-dd793edd3d3f/object-orientation.png)


## ObjectPositionWS

The **ObjectPositionWS** expression outputs the world-space center position of the object's bounds. Each sphere in the image below displays a different color as they are moved to a different position in space. The RGB color channels correspond to the X, Y and Z axes in the level. This node is useful when creating spherical lighting for foliage.

![Object Position Expression](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b1589a5-ae06-4f6a-b63c-1dc00fc753dd/object-position-ws.png)

## ParticlePositionWS

The **ParticlePositionWS** expression outputs Vector3 (RGB) data representing each individual particle's position in world space.

![Particle Position WS example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f95e3f5e-95d9-481a-8cb5-5d61fd1c7387/particle-position-worldspace.png)

In this image, ParticlePositionWS is being fed into emissive color to visualize the data. The particle system has been scaled up to show how the color is changing based on position.

## PixelNormalWS

The **PixelNormalWS** expression outputs vector data representing the direction that pixels are facing based on the current normal.

![Pixel Normal WS Example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d20e157e-d161-48f9-9b87-db886d169f68/pixel-normal-ws.png)

In this example, PixelNormalWS is fed into Base Color. Notice how the normal map is used to give the per-pixel result.

## Pre-Skinned Local Normal

The **Pre-Skinned Local Normals** Vector Expression outputs a three-channel vector value representing the local surface normal for Skeletal and Static Meshes. This enables you to achieve locally-aligned tri-planar Materials and mesh aligned effects in your Materials.

In this example, the Material below is using a tri-planar texture aligned to the mesh's local surface normal.

Click to enlarge image.

|  |  |
| --- | --- |
|  |  |
| Tri-Planar Pre-Skinned Local Normal Vector Expression | Tri-Planar Material |

## Pre-Skinned Local Position

The **Pre-Skinned Local Position** Vector Expression outputs a three-channel vector value that gives access to a Skeletal Mesh's default pose position data for use in
per-vertex outputs. This enables you to have localized effects on an animated character. This vector expression can also be used with Static Meshes, which will return
the standard local position.

Click to enlarge image.

In this example, the Skeletal Mesh's default pose is used for mapping versus the default UV mapping on the right.

|  |  |
| --- | --- |
|  |  |
| Pre-Skinned Local Position Vector Expression | Skeletal Mesh's Default UV Layout |

## ReflectionVectorWS

The **ReflectionVectorWS** expression is similar in spirit to [CameraVectorWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#cameravectorws), but it outputs a three-channel vector value representing the camera direction reflected across the surface normal.

**Example Usage:** ReflectionVector is commonly used in environment maps, where the Reflection Vector is passed into the UV coordinates of a cubemap texture. This enables you to create arbitrary reflections on a Material which do not match the physical environment. You can also use the Reflection Vector to create cheap, fake reflections on translucent Materials that do not have **Surface TranslucencyVolume** or **Surface ForwardShading** enabled.

![Fake translucent reflections](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebd98987-9da8-4e4e-a0c5-cd2b7aa739b6/fake-translucent-reflections.png)
