# Unreal Interfaces

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/interfaces-in-unreal-engine

> Application Version: 5.7

When a class inherits from an **Unreal Interface** class, the interface ensures that the new class implements a common set of functions. This is useful when certain functionality might be shared by large, complex classes that are otherwise dissimilar.

For example, suppose your game has a system where a player character entering a trigger volume can activate traps, alert enemies, or award points to the player depending on the circumstances. You might implement this with a `ReactToTrigger` function on traps, enemies, or point awards. Even though all of these activating objects implement the `ReactToTrigger` function, they might otherwise be quite dissimilar. For example:

- Traps derive from `AActor`.
- Enemies derive from `APawn` or `ACharacter`.
- Point-awards derive from `UDataAsset`.

These classes need shared functionality, but have no common parent other than the base `UObject`. In this case, an Unreal Interface can enforce all of these objects to implement the necessary functions.

## Declare an Interface in C++

Declaring an interface in C++ is similar to declaring an ordinary Unreal class. However, there are some primary differences:

- Interface classes use the `UINTERFACE` macro instead of the `UCLASS` macro.
- Interface classes inherit from `UInterface` instead of `UObject`.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The <code>UINTERFACE</code> class is not the actual interface, but rather an empty class that provides visibility to the reflection system.",
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

### C++ Class Wizard

To create a new Unreal Interface class from the Unreal Editor, follow the steps in the [C++ Class Wizard](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-cplusplus-class-wizard-in-unreal-engine) documentation with the following information:

- **Class:** Unreal Interface

### C++ Interface Declaration Example

The following is an example of a C++ interface declaration named `ReactToTriggerInterface`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "ReactToTriggerInterface.h",
  "code_preview": "#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;UObject/Interface.h&quot;\n#include &quot;ReactToTriggerInterface.generated.h&quot;\n\n/*\nThis class does not need to be modified.\nEmpty class for reflection system visibility.\nUses the UINTERFACE macro.\n",
  "lines_of_code": 27,
  "id": 150598,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1OTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--8824c423e0d9a0c9fb4ebbdc06e0acca5012c6ac959de6acb537dc8a195f3070",
  "settings": {
    "is_hidden": false
  }
}
```

As you can see in this example, the actual interface has the same name as the empty class, but the `U`-prefix is replaced by `I`. The `U`-prefixed class needs no constructor or any other functions. The `I`-prefixed class contains all interface functions and is the class that is inherited from by classes intended to implement the interface.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The <code>Blueprintable</code> specifier is required if you want a Blueprint to implement this interface.",
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

## Interface Specifiers

Use interface specifiers to expose your class to the [Unreal Reflection System](https://dev.epicgames.com/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine). The following table contains relevant interface specifiers:

| Interface Specifier | Description |
| --- | --- |
| `Blueprintable` | Exposes this interface so it can be [implemented by a Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine). Interfaces can’t be exposed to Blueprint if they contain anything other than `BlueprintImplementableEvent` and `BlueprintNativeEvent` functions. Use `NotBlueprintable` or `meta=(CannotImplementInterfaceInBlueprint)` to specify that an interface is not safe to implement in a Blueprint. |
| `BlueprintType` | Exposes this class as a type that can be used for variables in Blueprints. |
| `DependsOn=(ClassName1, ClassName2, ...)` | The build system compiles all classes listed with this specifier before it compiles this class. `ClassName` must specify a class in the same (or a previous) package. You can specify multiple dependency classes using a single `DependsOn` line delimited by commas, or can be specified using a separate `DependsOn` line for each class. |
| `MinimalAPI` | Causes only the class’s type information to be exported for use by other modules. The class can be cast to, but the functions of the class cannot be called, with the exception of inline methods. This improves compile times by avoiding exporting everything for classes that do not need all of their functions accessible in other modules. |

## Implement an Interface in C++

To use your interface in a new class:

- Include your interface header file.
- Inherit from your `I`-prefixed interface class.

The following is an example of the trap mentioned in the introduction to this page:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "Trap.h",
  "code_preview": "#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;ReactToTriggerInterface.h&quot;\n#include &quot;Trap.generated.h&quot;\n\nUCLASS(Blueprintable, Category=&quot;MyGame&quot;)\nclass ATrap : public AActor, public IReactToTriggerInterface\n{\n\tGENERATED_BODY()\n\n",
  "lines_of_code": 13,
  "id": 150599,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1OTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--0a0a62fdd08538a9381850a26485542b6fdefd554628411db4a4f9f53a4289f9",
  "settings": {
    "is_hidden": false
  }
}
```

## Declare Interface Functions

There are several methods you can use to declare functions in your interfaces, each of which is implementable or callable in different contexts. All of them must be declared in the `I`-prefixed class for your interface, and they must be public in order to be visible to external classes.

### C++ Only Interface Functions

You can declare a virtual C++ function in your interface’s header file, with no `UFUNCTION` specifiers. These functions must be virtual so you can override them in classes that implement your interface.

#### Interface Class

The following is an example of what this would look like in the `ReactToTriggerInterface` class:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "ReactToTriggerInterface.h",
  "code_preview": "#pragma once\n\n#include &quot;ReactToTriggerInterface.generated.h&quot;\n\n/*\nEmpty class for reflection system visibility.\nUses the UINTERFACE macro.\nInherits from UInterface.\n*/\nUINTERFACE(MinimalAPI, Blueprintable)\n",
  "lines_of_code": 23,
  "id": 150600,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--593f7fd4840f1031b322757eeb87f298a79c3ba69c37eceadea21053c5a61be9",
  "settings": {
    "is_hidden": false
  }
}
```

You can provide a default implementation either within the header itself or within the interface’s `.cpp` file.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "ReactToTriggerInterface.cpp",
  "code_preview": "#include &quot;ReactToTriggerInterface.h&quot;\n\nbool IReactToTriggerInterface::ReactToTrigger()\n{\n\treturn false;\n}",
  "lines_of_code": 6,
  "id": 150601,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--c51705e9a8954d526003da59e59683630e9bbc53863fbda29988c7272097998b",
  "settings": {
    "is_hidden": false
  }
}
```

#### Derived Class

When you implement your interface in a derived class, you can create and implement an override specific to that class. The following is an example of what this would look like if the `ATrap` actor implemented the `IReactToTriggerInterface`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "Trap.h",
  "code_preview": "#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;ReactToTriggerInterface.h&quot;\n#include &quot;Trap.generated.h&quot;\n\nUCLASS(Blueprintable, Category=&quot;MyGame&quot;)\nclass ATrap : public AActor, public IReactToTriggerInterface\n{\n\tGENERATED_BODY()\n\n",
  "lines_of_code": 13,
  "id": 150602,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--9864bdff0ee5b03231dbe0473779126aacc5cf06a2ca4e35a94ea834b94fa572",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "Trap.cpp",
  "code_preview": "#include &quot;Trap.h&quot;\n\nbool ATrap::ReactToTrigger()\n{\n\treturn false;\n}",
  "lines_of_code": 6,
  "id": 150603,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--eb78ba8d91d5abcfe7a5d19d909760388c06bdabd87177ba05f4f0907f3f1bdb",
  "settings": {
    "is_hidden": false
  }
}
```

C++ interface functions declared in this way are not visible to Blueprint and cannot be used in Blueprintable interfaces.

### Blueprint Callable Interface Functions

To make a Blueprint callable interface function, you must do the following:

- Specify a `UFUNCTION` macro in the function’s declaration with the `BlueprintCallable` specifier.
- Use either the `BlueprintImplementableEvent` or `BlueprintNativeEvent` specifiers.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Blueprint callable interface functions cannot be virtual.",
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

Functions with the `BlueprintCallable` specifier can be called in C++ or Blueprint using a reference to an object that implements your interface.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If your Blueprint callable function does not return a value, Unreal Engine treats your function as an event in Blueprint.",
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

#### Blueprint Implementable Event

Functions with the `BlueprintImplementableEvent` specifier can not be overridden in C++, but can be overridden in any Blueprint class that implements or inherits your interface. The following is an example of a C++ interface declaration for a `BlueprintImplementableEvent`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "ReactToTriggerInterface.h",
  "code_preview": "#pragma once\n\n#include &quot;ReactToTriggerInterface.generated.h&quot;\n\n/*\nEmpty class for reflection system visibility.\nUses the UINTERFACE macro.\nInherits from UInterface.\n*/\nUINTERFACE(MinimalAPI, Blueprintable)\n",
  "lines_of_code": 25,
  "id": 150604,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--5067ec6606e0c44def9c5e657e856d3925ea7ed1ca2d62310da758f22fa05a60",
  "settings": {
    "is_hidden": false
  }
}
```

#### Blueprint Native Event

Functions with the `BlueprintNativeEvent` specifier can be implemented in C++ or Blueprint. The following is an example of a C++ interface declaration for a `BlueprintNativeEvent`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "ReactToTriggerInterface.h",
  "code_preview": "#pragma once\n\n#include &quot;ReactToTriggerInterface.generated.h&quot;\n\n/*\nEmpty class for reflection system visibility.\nUses the UINTERFACE macro.\nInherits from UInterface.\n*/\nUINTERFACE(MinimalAPI, Blueprintable)\n",
  "lines_of_code": 25,
  "id": 150605,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--2270949cb56999b24388037a07b87f1a1c9822d89e16fc6258eeb5ffada8a3d4",
  "settings": {
    "is_hidden": false
  }
}
```

##### Override a Blueprint Native Event in C++

To implement a `BlueprintNativeEvent` in C++, create an additional function with the same name as the `BlueprintNativeEvent` with an additional `_Implementation` suffix appended to the name. The following is an example of what this looks like from the `ATrap` example:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "Trap.h",
  "code_preview": "#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;ReactToTriggerInterface.h&quot;\n#include &quot;Trap.generated.h&quot;\n\nUCLASS(Blueprintable, Category=&quot;MyGame&quot;)\nclass ATrap : public AActor, public IReactToTriggerInterface\n{\n\tGENERATED_BODY()\n\n",
  "lines_of_code": 16,
  "id": 150606,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--b85ab4f15e45c4a5cfabbdbfc35736415f62cbcf38cb6d1ee6d34264fe4bc088",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "Trap.cpp",
  "code_preview": "#include &quot;Trap.h&quot;\n\nbool ATrap::ReactToTrigger()\n{\n\treturn false;\n}\n\n// Blueprint Native Event override implementation\nbool ATrap::ReactToTrigger_Implementation() \n{\n",
  "lines_of_code": 12,
  "id": 150607,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--ad37c3b3927f4d5b0ebbe75f4744d0373f8543706caaeb35aba7ff9f3c94d9c9",
  "settings": {
    "is_hidden": false
  }
}
```

##### Override a Blueprint Native Event in Blueprint

The `BlueprintNativeEvent` specifier also allows implementations to be overridden in Blueprint. To implement a `BlueprintNativeEvent` in Blueprint, see the [Implement Blueprint Interfaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine) documentation for more information.

#### Call a Blueprint Event from C++

To safely call a `BlueprintImplementableEvent` or `BlueprintNativeEvent` on a `Blueprintable` interface from C++, you must use the special static `Execute_` function wrapper. The following example call works for interfaces whether they are implemented in C++ or Blueprint:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// OriginalObject is an object that implements the IReactToTriggerInterface\nbool bReacted = IReactToTriggerInterface::Execute_ReactToTrigger(OriginalObject);",
  "lines_of_code": 2,
  "id": 150608,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--0231282215d984ba97138f1f89be9cea909589d26d0d36557ff30577672202a2",
  "settings": {
    "is_hidden": false
  }
}
```

## Interface Function Types

There are three different types of interface functions:

- Base
- Implementation
- Execute

The following table explains what each type is used for:

| Type | Definition Location | Purpose | Use this to… |
| --- | --- | --- | --- |
| Base function | Base interface class. (`MyInterface.h`) | Function definition you can implement in child classes. | Only use if interface and implementations are only defined in C++. |
| Implementation wrapper | C++ Class that implements interface. (`MyInterfaceActor.h`, `MyInterfaceActor.cpp`) | Implement interface functionality in C++. | Call only C++ implementation, but not any Blueprint overrides. |
| Execute wrapper | Created automatically by Unreal Engine’s reflection system. (`MyInterface.generated.h`, `MyInterface.gen.cpp`) | Facilitates communication between implementations defined in C++ and Blueprint. | Call function implementations including C++ and Blueprint overrides. |

Consider the following example:

- `MyFunction` is a `BlueprintNativeEvent` interface function defined in `MyInterface.h`.
- `MyInterfaceActor` implements `MyInterface`.
- `MyFunction_Implementation` is defined in `MyInterfaceActor.cpp`.
- A variety of C++ and Blueprint spawned actors that inherit from `MyInterfaceActor`.

To safely call `MyFunction` for all Blueprint and C++ objects that inherit from `MyInterfaceActor`, you can do the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;AActor*&gt; OutActors;\nUGameplayStatics::GetAllActorsOfClass(GetWorld(), AMyInterfaceActor::StaticClass(), OutActors);\n\n// OutActors contains all BP and C++ actors that are or inherit from AMyInterfaceActor\nfor (AActor* CurrentActor : OutActors)\n{\n\t// Each CurrentActor calls its own MyFunction implementation\n\tUE_LOG(LogTemp, Log, TEXT(&quot;%s : %s&quot;), *CurrentActor-&gt;GetName(), *IMyInterface::Execute_MyFunction(Cast&lt;AMyInterfaceActor&gt;(CurrentActor)));\n}",
  "lines_of_code": 9,
  "id": 150609,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MDksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--f403f8df8556b6a7ee0900649e55c0bc50b2eb0dc29f2a9d60a85364907cc0a6",
  "settings": {
    "is_hidden": false
  }
}
```

## Determine Whether a Class Implements an Interface

For compatibility with both C++ and Blueprint classes that implement your interface, use any of the following functions to determine whether a class implements an interface:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "bool bIsImplemented;\n\n/* bIsImplemented is true if OriginalObject implements UReactToTriggerInterface */\nbIsImplemented = OriginalObject-&gt;GetClass()-&gt;ImplementsInterface(UReactToTriggerInterface::StaticClass());\n\n/* bIsImplemented is true if OriginalObject implements UReactToTriggerInterface */\nbIsImplemented = OriginalObject-&gt;Implements&lt;UReactToTriggerInterface&gt;();\n\n/* ReactingObject is non-null if OriginalObject implements UReactToTriggerInterface in C++ */\nIReactToTriggerInterface* ReactingObject = Cast&lt;IReactToTriggerInterface&gt;(OriginalObject);",
  "lines_of_code": 10,
  "id": 150610,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--69632a66de4ebf71b4aa2cde82371ed127bb4c825d3ae9c64adbb355334c76c3",
  "settings": {
    "is_hidden": false
  }
}
```

The templated `Cast<>` method only works if the interface is implemented in a C++ class. Interfaces implemented in a Blueprint do not exist in the C++ version of the object, so `Cast<>` returns null. `TScriptInterface<>` can also be used in C++ code to safely copy an interface pointer and the `UObject` that implements it.

## Cast to Other Unreal Types

Unreal Engine’s casting system supports casting from one interface to another, or from an interface to an Unreal type where appropriate. The following examples are some methods that you can use to cast interfaces:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "/* ReactingObject is non-null if the interface is implemented */\nIReactToTriggerInterface* ReactingObject = Cast&lt;IReactToTriggerInterface&gt;(OriginalObject);\n\n/* DifferentInterface is non-null if ReactingObject is non-null and it implements ISomeOtherInterface */\nISomeOtherInterface* DifferentInterface = Cast&lt;ISomeOtherInterface&gt;(ReactingObject);\n\n/* ReactingActor is non-null if ReactingObject is non-null and OriginalObject is an AActor or AActor-derived class */\nAActor* ReactingActor = Cast&lt;AActor&gt;(ReactingObject);",
  "lines_of_code": 8,
  "id": 150611,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--845768a317389ed84c4eedac250a159dc9e1be1ada20a64874743f48b96a015a",
  "settings": {
    "is_hidden": false
  }
}
```

## Safely Store Object and Interface Pointers

To store a reference to an object that implements a specific interface, you can use `TScriptInterface`. If you have an object that implements an interface, you can initialize `TScriptInterface` as follows:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UMyObject* MyObjectPtr;\nTScriptInterface&lt;IMyInterface&gt; MyScriptInterface;\n\nif (MyObjectPtr-&gt;Implements&lt;UMyInterface&gt;())\n{\n\tMyScriptInterface = TScriptInterface&lt;IMyInterface&gt;(MyObjectPtr);\n}\n\n// MyScriptInterface holds a reference to MyObjectPtr and MyInterfacePtr",
  "lines_of_code": 9,
  "id": 150612,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--c421715c5a3ca335183ace00b8db674060cf28bc029df9c52860a384b7a2633f",
  "settings": {
    "is_hidden": false
  }
}
```

To retrieve a pointer to the original object, use `GetObject`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UMyObject* MyRetrievedObjectPtr = MyScriptInterface.GetObject();",
  "lines_of_code": 1,
  "id": 150613,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--ab263408b2ad579ed65bae8de21108fb7ac1cb77886a35e61315666bba28fd43",
  "settings": {
    "is_hidden": false
  }
}
```

To retrieve a pointer to the interface that the original object implements, use `GetInterface`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "IMyInterface* MyRetrievedInterfacePtr = MyScriptInterface.GetInterface();",
  "lines_of_code": 1,
  "id": 150614,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0NzowMiswMDowMCJ9--3bb07c3d2a570a37f92a69d92600a61b6546fbbb76e1a5823ce79e476da6d182",
  "settings": {
    "is_hidden": false
  }
}
```

For more information about `TScriptInterface`, see [TScriptInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/TScriptInterface?application_version=5.5) and the linked [FScriptInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/FScriptInterface?application_version=5.5) API pages.

## Blueprint Implementable Interfaces

If you want a Blueprint to implement this interface, you must use the `Blueprintable` metadata specifier. Every interface function (other than static functions) must be a `BlueprintNativeEvent` or a `BlueprintImplementableEvent`. When a Blueprint implements an interface declared in C++, it works like a Blueprint interface asset. This means that an instance of that Blueprint class will not actually contain the C++ version of the interface, so it cannot be used with `Cast<>`. From C++, only the `Execute_` static wrapper functions will work properly.
