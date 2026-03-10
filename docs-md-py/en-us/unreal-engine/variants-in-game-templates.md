# Game Template Variants

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/variants-in-game-templates

> Application Version: 5.7

When creating a new project, you can optionally choose a **Variant** of the template you're creating. Not all templates will have a variant to choose from, but the ones that do offer different types of gameplay and content for a base template project.

For example, when creating a Third Person template project, you can choose from the standard template, or its variants for Combat, Platforming, and Side Scroller.

If you prefer to work with the standard template, select the **None** option from the Variant dropdown menu when creating your project.

![Variant menu options associated with the third-person template in the games category.](https://dev.epicgames.com/community/api/documentation/image/43cbf5aa-77ea-4f54-926a-343bc01eb6fc)

## First Person Variants

The **F****irst Person** variants focus on gameplay using a first person field of view (FOV).

The following variants are included:

- Arena Shooter
- Survival Horror

### Arena Shooter

The **Arena Shooter** variant is a shooter environment that has a selection of weapons and combat movements.

![Image of the arena shooter template with a first-person view over the weapon.](https://dev.epicgames.com/community/api/documentation/image/8f67390f-51e3-442a-801a-78fa7bff9967)

_Arena Shooter variant._

Features include:

- Range of weapon pickups
- Range of bullet types
- AI opponents
- Ammo UI
- Example arena map

### Survival Horror

The **Survival Horror** variant features pre-configured lighting and mood setup for a low-light, high-contrast atmosphere.

![Image of columns with grazing light, high contrast sun filtered through wall openings.](https://dev.epicgames.com/community/api/documentation/image/68a52237-21da-483a-b43d-937677719d0d)

_Survival Horror variant._

Features include:

- Flashlight for the player pawn
- Example map that demonstrates simplistic lighting dark environments
- Sprint mechanic with associated user interface
- Flickering lights

## Third Person Variants

The **Third Person** variants are designed to support a broader range of gameplay styles, focusing on character-action development.

The following variants are included:

- Combat
- Side Scroller
- Platformer

### Combat

The **C****ombat** variant focuses on combat mechanics, enemy targeting, and a built-in health management system.

![Image of the combat arena with an AI character charging into the arena.](https://dev.epicgames.com/community/api/documentation/image/835116e1-8bd3-4724-8867-a1437f1bad28)

_Combat variant._

Features include:

- Simple hand combat
- Combo attack
- AI opponents
- In-world health bar UI
- Example combat map

### Side Scroller

The **Side Scroller** variant adapts the third-person perspective to a locked side-scrolling format, with pre-configured camera and movement systems.

![Image of the character moving across the screen from left to right, seen from the character's right side only.](https://dev.epicgames.com/community/api/documentation/image/9d68310a-acf9-4d5d-a296-588acaf10d0e)

_Side Scroller variant._

Features include:

- Fixed camera example
- Constrained plane setup
- Pickups
- Single-sided and drop-through collision interaction
- Fix to floor and locked camera example
- Example side scrolling map

### Platforming

The **Platforming** variant focuses on advanced jumping, climbing, and well-controlled movement mechanics.

![Image of character jumping with green ribbons streaming from their feet.](https://dev.epicgames.com/community/api/documentation/image/a128682a-283f-4ff5-bd9a-78b2e758efa1)

_Platforming variant._

Features include:

- Dash mechanic
- Wall jump
- Example platforming map

## Top Down Variants

The **Top Down** variants deliver the foundation for games with an overhead perspective that now includes a grid-base and a dual-axis base.

The following variants are included:

- Strategy
- Twin Stick

### Strategy

The **Strategy** variant assists in developing strategy games through a grid-based movement system.

![Top-down camera view of the game space with AI characters.](https://dev.epicgames.com/community/api/documentation/image/badc4a0c-9fdb-4bee-95cd-75c0469a1b39)

_Strategy variant._

Features include:

- Drag-select AI characters
- Simple character interactions
- Roof transition effect
- Simple AI move to examples
- Orthographic camera setup

### Twin Stick

The **Twin Stick** variant offers mechanics for twin stick shooter games with dual axis aiming and movement and has a character system.

![Image of the Twin Stick variant in a top down view of the arena.](https://dev.epicgames.com/community/api/documentation/image/f38e97d0-0b40-484d-9bdc-2252f043ee46)

_Twin Stick variant._

Features include:

- Simple AI opponents
- Bomb and shoot mechanic
- Simple arena map
- Score and multiplier user interface

## Vehicle Variants

The **Vehicle** variants are the starting point for creating driving and racing games. Vehicle models have been modularized into static mesh pieces attached to an empty skeleton to simplify customization. [Runtime Virtual Texturing](https://dev.epicgames.com/documentation/en-us/unreal-engine/runtime-virtual-texturing-in-unreal-engine) (RVT) has also been enabled and set up for each map.

The following variants are included:

- Offroad
- Timetrial

### Offroad

The **Offroad** variant delivers modular components and simplified assets for offroad-style gameplay, including a sample map.

![Image of the offroad variant with a dune buggy on a road in the desert.](https://dev.epicgames.com/community/api/documentation/image/7021459a-dfa2-47bc-b5ac-45cc80af459a)

_Offroad variant._

Features include:

- Open world exploration map
- Offroad all-wheel-drive vehicle example
- Spline roads
- Runtime Virtual Texturing map setup
- Hierarchical Level of Detail (HLOD) structure

### Timetrial

The **Timetrial** variant speeds up the creation of time-based racing experiences with lap timing systems, checkpoint logic, and specific UI elements. Features include:

- Simple track map
- Gate structure to mark traversal through a lap
- Time and best time UI

![Image of the Timetrial variant with an orange car on the track in an arena.](https://dev.epicgames.com/community/api/documentation/image/c9b3995e-fd21-4c50-869e-4678275307bd)

_Timetrial variant._
