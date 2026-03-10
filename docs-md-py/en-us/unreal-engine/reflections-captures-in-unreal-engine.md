# Reflections Captures

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/reflections-captures-in-unreal-engine

> Application Version: 5.7

**Reflection Capture** Actors are probes that can be placed around the world to capture a static image of the area they cover. This reflection method reprojects the captured cubemap onto surrounding reflective materials. It is a low-cost method of reflections with no runtime performance cost.

## Reflection Capture Shapes

There are currently two reflection capture shapes: sphere and box. The shape is very important because it controls what part of the level is captured into the cubemap, what shape the level is reprojected onto in reflections, and which part of the level can receive reflections from that cubemap (area of influence).

### Sphere shape

The sphere shape is currently the most useful. It never matches the shape of the geometry being reflected but has no discontinuities or corners, therefore, the error is uniform.

![Sphere Shape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/acf17925-7308-4f2b-b7cc-17311cc2ea2e/01-capt-refl-sphere-shape.png)

The sphere shape has an orange influence radius that controls which pixels can be affected by that cubemap, and the sphere that the level will be reprojected onto.

Smaller captures will override larger ones, so you can provide refinement by placing smaller captures around the level.

### Box shape

The box shape is very limited in usefulness and generally only works for hallways or rectangular rooms. The reason is that only pixels inside the box can see the reflection, and at the same time all geometry inside the box is projected onto the box shape, creating significant artifacts in many cases.

![Box Shape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4f84d1e-4ca7-42b9-8f83-3cf634036626/02-capt-refl-box-shape.png)

The box has an orange preview for the projection shape when selected. It only captures the level within **Box Transition Distance** outside this box. The influence of this capture fades in over the transition distance as well, inside the box.

## Setting Up a Level to use the Reflection Environment

The first step toward having good reflections is setting up diffuse lighting including indirect lighting
through the use of lightmaps. The [Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine#precomputedglobalillumination) page contains more info on how to accomplish this if you are unfamiliar with using it. Common errors preventing Lightmass indirect lighting from working after a build include but are not limited to the following:

* A shadow casting skybox.
* Lack of a **LightmassImportanceVolume**.
* Missing or incorrectly setup lightmap UVs.
* Having **Force No Precomputed Lighting** set to **True** in the **World Properties**.

Since the level's diffuse color is what will be reflected through the Reflection Environment you will need to do the following for the best results.

* Ensure significant contrast between directly lit and shadowed areas.
* Remember that the bright diffuse lit areas are what will show up clearly in reflections.
* Darker shadowed areas are where the reflections will be most visible.
* Use the Lit viewmode together with the Specular show flag disabled to see the level as the reflection captures see it.

It is also extremely important to setup your level's Materials to work well with the Reflection Environment by keeping the following in mind.

* A flat, mirror surface will reveal the inaccuracies of combining cubemaps projected onto simple shapes.
* Curvy geometry or rough surfaces can both obscure these artifacts and provide convincing results.
* It is important to use detail Normal maps and specify some degree of roughness on Materials that will be used in flat areas as this will help them better show off reflections.

|  |  |  |
| --- | --- | --- |
| Curvy and Sharp | Flat and Rough | Flat and Sharp |
| Smooth surface but curvy geometry: Good quality reflections | Rough surface but flat geometry: Good quality reflections | Smooth surface AND flat geometry: Evident that reflections do not match up |

Place reflection captures in the areas that you want to have reflections. Try to place the sphere captures such that the part of the level you want to reflect is contained just inside their radius since the level will be reprojected onto that sphere shape. Try to avoid placing captures too close to any level geometry, as that nearby geometry will dominate and block important details behind it.

## Glossy Indirect Specular

In technical terms, the Reflection Environment provides indirect specular. We get direct specular through analytical lights, but that only provides reflections in a few bright directions. We also get specular from the sky through a Sky Light, but that does not provide local reflections since the Sky Light cubemap is infinitely far away. Indirect specular allows all parts of the level to reflect on all other parts, which is especially important for Materials like metal which have no diffuse response.

![Diffuse Only](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/32cf9566-d972-450b-80f6-316b81af72e5/06-capt-refl-diffuse-only.png)

![Reflection Only](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4b1017f-8e49-40c8-8d1e-c201ed380031/07-capt-refl-reflection-only.png)

**Full lighting**

![Full Scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e0df3a0-b157-40ff-913a-31d8c5eb53b3/08-capt-refl-complete-scene.png)
