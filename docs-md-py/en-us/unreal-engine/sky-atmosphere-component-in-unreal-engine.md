# Sky Atmosphere Component

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine

> Application Version: 5.7

The **Sky Atmosphere** component in Unreal Engine is a physically-based sky and atmosphere-rendering technique. It's flexible enough to create an Earth-like atmosphere with time-of-day featuring sunrise and sunset, or to create extraterrestrial atmospheres of an exotic nature. It also provides an aerial perspective to which you can simulate transitions from ground to sky to outer space with proper planetary curvature.

![Sky Atmosphere with time-of-day featuring sunrise and sunset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c2b618f2-43c4-4e14-a044-1c9e627742b9/01-sky-atmosphere-day-dusk.png)

The Sky Atmosphere gives an approximation of light scattering through a planetary atmosphere's participating media, giving outdoor levels a more realistic or exotic look by including the following:

* You can have two atmospheric Directional Lights that receive sun disk representation in the atmosphere with sky color that depends on the sunlight and atmosphere properties.
* A sky color that will vary, depending on the altitude of the sun, or in other terms, how close the dominant Directional Light's vector gets to being parallel with the ground.
* Control over scattering and fuzzy settings, allowing for full control of your atmospheric density.
* Aerial perspective that simulates the curvature of the world when transitioning from ground to sky to space views.

## Enabling the Sky Atmosphere Component

Enable the Sky Atmosphere component by following these steps using the **Place Actors** panel in the Level Editor:

1. Place a **Sky Atmosphere** component in the scene.

   ![Drag a Sky Atmosphere into your scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d6ca1e7-0172-4c74-bf5f-97bb19c2adda/02-placing-sky-atmosphere.png)
2. Place a **Directional Light** in the scene.

   ![Drag a Directional Light into your scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61fa493b-d8e5-4b4b-9a4c-808a410f8b65/03-placing-directional-light.png)
3. From its **Details** panel, enable **Atmosphere Sun Light**.

   ![Select Directional Light and enable Atmosphere Sun Light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1124206-508e-4f83-81a5-6e28bb7cdda0/04-enabling-atmosphere-sun-light.png)
   1. If using multiple **Directional Lights**, set the **Atmosphere Sun Light Index** for each; for instance, 0 for the Sun and 1 for the Moon.
4. Place a **Sky Light** in the scene to capture Sky Atmosphere and have it contribute to the scene lighting.

   ![Drag a Sky Light into your scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f5b12bd3-a2fc-4df4-97ae-31bd3e984ab3/05-placing-sky-light.png)

### Adjusting Atmospheric Directional Lights

When you've enabled **Atmosphere Sun Light** on your **Directional Light(s)** and set the **Atmosphere Sun Light Index** for each, you can quickly adjust each light's position using the following keyboard shortcuts:

* **Right Ctrl + L** with mouse movement will adjust the Directional Light set to index 0. Typically this would be the Sun.
* **Right Ctrl + L + Shift** with mouse movement will adjust the Directional Light set to index 1. Typically this would be the Moon.

Moving these light sources will affect the atmosphere based on properties set in the Sky Atmosphere component for each Directional Light.

## Sky Atmosphere Model

Simulating the sky and atmosphere requires several properties that mimic the look and feel of a real-world atmosphere. These properties can be used to define the look of the sky and atmosphere by scattering light in an appropriate and accurate manner. By default, the Sky Atmosphere component represents the Earth.

For an Earth-like planet, the atmosphere is made up of multiple layers of gasses. They themselves are made up of particles and molecules that have their own shape, size and density. When photons (or light energy) enter the atmosphere and collide with the particles and molecules there, they are either scattered (reflected) or absorbed (see below).

![Particle Light Interaction](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47c9ee59-842d-429c-9267-7950fd238e09/06-particle-light-interaction.png)

(1) Incident Light from the Sun; (2) Particles in the Atmosphere; (3) Redirected Light Energy.

The Sky Atmosphere system simulates absorption with Mie scattering and Rayleigh scattering. These scattering effects enable the sky to appropriately change colors during time-of-day transitions by simulating how the incident light interacts with particles and molecules in the atmosphere.

The sky color changes depending on the time-of-day simulation when using the Sky Atmosphere component.

### Rayleigh Scattering

The interaction of light with smaller particles (such as air molecules) results in **Rayleigh scattering**. This type of scattering is highly dependent on the light wavelength. For instance, in the Earth's sky, blue scatters more than other colors, giving the sky its blue color during the daytime. However, at sunset, it appears red because light rays need to travel further in the atmosphere. After long distances, all blue light is scattered away before other colors, resulting in colorful sunsets full of yellow, orange, and red colors.

![Rayleigh Scattering](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dbdbc6db-5e21-4093-8aa1-36d090895b09/07-rayleigh-particle-shape.png)

(1) Incident light; (2) Small particles in the atmosphere; (3) Rayleigh scattered light energy.

In an Earth-like atmosphere, when sunlight interacts with small particles (1) in the atmosphere (2), Rayleigh scattering happens throughout the atmosphere. The upper atmosphere is less dense compared to the lower atmosphere near the Earth's surface (3).

![Rayleigh Atmosphere Interaction](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e77b518-1aab-4fa7-8b62-c1b35267e6ad/08-rayleigh-atmosphere-interaction.png)

Increasing or decreasing the density of particles in the atmosphere causes light to scatter more or less.

![Decreased Rayleigh Scattering Scale](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fe38a8f6-bd8d-4263-aac4-e2a4f31b5aea/09-ray-leigh.png)
![Default Rayleigh Scattering Scale](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c70c46d4-9682-4a4e-9264-bb0f7a98d7df/10-ray-leigh2.png)
![Increased Rayleigh Scattering Scale](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a16d195-5794-4812-a57c-f8e40662647c/11-ray-leigh3.png)

**Drag the slider to see the effects of decreasing and increasing the Rayleigh Scattering Scale. (Left to right, 1–3)**

1. **Decreased** scattering causes light to scatter less through the atmosphere. This is 10x less dense than Earth's atmosphere.
2. This is representative of an Earth-like atmospheric density.
3. **Increased** scattering allows light to scatter more through the atmosphere. This is 10x more dense than Earth's atmosphere.

### Mie Scattering

The interaction of light with larger particles—such as those from dust, pollen, or air pollution—suspended in the atmosphere results in **Mie scattering**. These particles are referred to as aerosols and can be caused naturally or by human activity. Incident light that follows the Mie scattering theory usually absorbs light, causing the clarity of the sky to appear hazy by occluding light. Light also usually scatters more forward, resulting in bright halos around the light's source, such as around the sun disk in the sky.

![Mie Scattering](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44a418d5-427a-465c-92b3-3d3ef20a3f88/12-mie-particle-shape.png)
