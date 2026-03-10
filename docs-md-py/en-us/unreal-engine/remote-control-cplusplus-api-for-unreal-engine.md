# Remote Control C++ API

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-cplusplus-api-for-unreal-engine

> Application Version: 5.7

With the Remote Control C++ API, you can access different parts of the Remote Control Plugin. You can build custom integration and Remote Control adapters with Unreal Engine, and use custom transports to access the Remote Control entities.

This page introduces the Remote Control C++ API, with links to the Unreal Engine C++ API Reference for further details.

## Workflow

1. Set up a server in your Unreal Engine Project to send and receive data between Unreal Engine and your C++ application. For example, you can use  and .
2. Create an external C++ application to send and receive data from the server in your Unreal Engine project.
3. Create a parser and manager in your Unreal Engine Project to process received data and call Remote Control functions.

## API

The following classes make up the core functionality of the Remote Control C++ API:

* : Access functionality available at the [Module](https://dev.epicgames.com/documentation/en-us/unreal-engine/module-properties-in-unreal-engine) scope, such as getting and resolving Remote Control Presets.
* : Includes access to:

  + Targets that contain exposed functions, properties, and Actors.
  + Getters that use unique IDs and labels for exposed entities such as property, function, and Actor so you can access the entity from Editor, Game Mode, Simulation, and Package.
  + A listener for property changes.
  + Delegates when an entity is exposed or unexposed.
* : Access to exposed objects, properties, functions, and Actors, and their metadata
* : Represents a property exposed to Remote Control, and includes access to `FProperty` and `RemoteControlPropertyHandle` for getting and setting values of the exposed property
* : Access to the `UFunction` pointer and function argument so you can invoke the function on a specific object using `UObject->ProcessEvent(UFunction*, ArgumentsMemory)`
* : Access to the pointer for an exposed Actor.
* : Access to getters and setters to modify the values of exposed properties, and access child properties for complex types.

  You can get and set the value for a simple property type directly. Simple property types include int, float, double, string, vector, and rotator.

  You cannot get and set a property value directly for complex types such as TArray, TMap, TSet, and Structs. Instead, you must access a child property handle, and if the child property is a simple property type you can get and set its value.
* [DisplayClusterRemoteControlInterceptor](https://dev.epicgames.com/documentation/404): Use this to set any property values replicable through nDisplay.
