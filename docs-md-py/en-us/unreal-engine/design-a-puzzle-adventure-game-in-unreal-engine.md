# Design a Puzzle Adventure

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine

> Application Version: 5.7

Unreal Engine provides users with the professional-grade tools to bring their game ideas to life. Once you have made decisions about what types of gameplay you want, it’s time to start building the play spaces and environments that will define the visual world of your game.

[Video: V_EhkYJw](https://dev.epicgames.com/community/api/cms/videos/V_EhkYJw/embed.html)

Game and Level Design is about designing experiences that challenge players while still providing a fun and engaging world that supports those experiences. While the Code a First-Person Adventure Game tutorial focuses on using C++ to create gameplay, you can create many of the same elements using the Blueprint Scripting language. Blueprints provide non-programmers with a flexible scripting language that can be used to create gameplay, scripted events, and interactable elements. Unreal Engine provides the ability to create games using Blueprints, C++, or a mix of both.

This tutorial series takes you through the design process of building a level and several puzzles using blueprints to create a completely playable gameplay experience. You will learn how to create gameplay using Blueprints, as well as how to use and reuse gameplay elements to prototype a level using a process called grayboxing.

![Designer Track Puzzles](https://dev.epicgames.com/community/api/documentation/image/bb5d5a4a-2437-4295-8b48-72fc52f5be9c)

_Designer Track Puzzles_

## Designer Track Overview

Throughout this tutorial, you will build an adventure puzzle game with multiple rooms, showcasing different kinds of mechanics.

![Overview Diagram of the Designer Track Level](https://dev.epicgames.com/community/api/documentation/image/946207a5-ebf2-4d52-ab05-f21632b18759)

_Overview Diagram of the Designer Track Level_

1. Set up and grayboxing your level. This is an important first step to thinking through your level’s design before you start digging into the level’s mechanics and gameplay.
2. Create a key and door open and close mechanic.
3. Implement a heads-up-display (HUD) on the player’s user interface using UMG.
4. Design the cube puzzles, first with a light switch activator and then with moving platforms.
5. Build traps under the platformer and learn about player failure and how to set damage over time.
6. Configure enemy pawns to attack the player, and then a sprint movement for the player so they can get past the enemies quickly!
7. Add an end state so the game knows when the game is over, plus additional polish!

When you finish the tutorial, you will have a fully functional puzzle game!

## Before You Begin

- If you’re new to Unreal Engine, read the other getting-started pages in [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users).
- The Code a First-Person Adventure Game is a tutorial series that uses C++ and Unreal Editor to build a custom player character. You can use what you build in the Programmer Track as a starting point for this track.

## Example Project

Below is a link to download the final sample project that you can build using this tutorial series. You can use this example project to see what your final project might look like, or as a reference to see how we built and designed the project.

```json
{
  "type": "attachment",
  "attachment_id": 44933,
  "caption": "Download the Designer Track here",
  "attachment": {
    "id": 44933,
    "file_name": "adventuredesigner.zip",
    "file_size": 80824626,
    "content_type": "application/zip",
    "created_at": "2026-03-06T18:40:27.099+00:00",
    "original_url": "https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/bcb4d714-941a-4a93-9d50-25ff231868e6/adventuredesigner.zip"
  },
  "settings": {
    "is_hidden": false
  }
}
```

*(Download size: 75 MB)*

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To open the project, unzip the file and move the <b>adventuredesigner</b> folder to your Unreal Projects directory (by default, find this in <code class=\"inline-code\">C:\\Users\\<i>UserName</i>\\Documents\\Unreal Projects</code>).",
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

## Let’s Go!

- [Related Document](en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine.md)
