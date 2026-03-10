# Blueprints Technical Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/technical-guide-for-blueprints-visual-scripting-in-unreal-engine

> Application Version: 5.7

**Blueprints** are a powerful new feature introduced in Unreal Engine 4. Blueprints are a way to create new [UClasses](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/UClass?application_version=5.5) without the need for writing or compiling code. When you create a Blueprint, you can choose to extend a C++ class or another Blueprint class.
You can then add, arrange, and customize [Components](https://dev.epicgames.com/documentation/en-us/unreal-engine/components-in-unreal-engine), implement custom logic using a visual scripting language, respond to [Events](https://dev.epicgames.com/documentation/en-us/unreal-engine/events-in-unreal-engine) and interactions, define custom [Variables](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine), handle [Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine), and create a fully custom object type.

Each Blueprint has a [Construction Script](https://dev.epicgames.com/documentation/en-us/unreal-engine/construction-script-in-unreal-engine), analogous to a constructor in C++, which is run when the object is created. This script can dynamically construct the Actor instance based on any number
of factors, such as a fence that automatically sizes itself to fill a gap between buildings. In this sense, a Blueprint can be thought of as a very powerful prefab system.

- Related Document
