# Customizable Sequencer Track

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/customizable-sequencer-track-in-unreal-engine

> Application Version: 5.7

Using Blueprints and child classes, you can create your own customizable Sequencer tracks. This feature can be used to extend Sequencer track functionality without using C++. It can be useful for prototyping or implementing new tracks you may need on your project.

This document provides an overview of the Custom Sequencer Track feature, how to create new track types, and the various functions used to communicate with common Sequencer objects.

#### Prerequisites

* The Customizable Sequencer Track feature is a [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) that must be enabled prior to use. From Unreal Engine's main menu, go to **Edit > Plugins**, locate **Customizable Sequencer Tracks** in the **Runtime** section, and click the checkbox to enable it. Then, restart Unreal Engine.

  ![customizable sequencer tracks plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9bb0e03b-da3c-4118-a0a6-7941a04b4211/plugin.png)
* You should be familiar with creating and using [Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine).

## Create New Track

New custom Sequencer tracks require creating three different Blueprint classes that are inherited from:

* `SequencerSectionBP`
* `SequencerTrackBP`
* `SequencerTrackInstanceBP`

To do this, in the **Content Browser**, click **Add (+) > Blueprint Class**, then navigate in the **All Classes** section to these three classes. Create a new child Blueprint class for each one.

![create track classes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed3d6383-a18e-403b-80f9-2b96ad83cde5/create1.png)
