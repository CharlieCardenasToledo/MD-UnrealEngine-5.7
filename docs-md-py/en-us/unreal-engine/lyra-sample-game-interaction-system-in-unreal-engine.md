# Lyra Interaction System

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-interaction-system-in-unreal-engine

> Application Version: 5.7

## Lyra Interaction System

Lyra uses its interaction [Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/interfaces-in-unreal-engine?application_version=5.5)/[IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/IInterface?application_version=5.5) through its own [Gameplay Ability](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine)/[UGameplayAbility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GameplayAbilities/Abilities/UGameplayAbility?application_version=5.5) (ULyraGameplayAbility\_Interact) which establishes a cause and effect relationship between how the player Interacts with objects in Lyra, and how those objects interact with the player.

Using the `LyraGameplayAbility_Interact` class, you can manage the logic of how your interactions are called.

**ULyraGameplayAbility\_Interact.h**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#pragma once\n\t\t#include &quot;CoreMinimal.h&quot;\n\t\t#include &quot;AbilitySystem/Abilities/LyraGameplayAbility.h&quot;\n\t\t#include &quot;Interaction/InteractionQuery.h&quot;\n\t\t#include &quot;Interaction/IInteractableTarget.h&quot;\n\t\t#include &quot;LyraGameplayAbility_Interact.generated.h&quot;\n\n\t\tclass FIndicatorDescriptor;\n\t\t/**\n\n",
  "lines_of_code": 48,
  "id": 149397,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNDkzOTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowMzo1MSswMDowMCJ9--fa3c831c75ef689eb029bfabba73af4103b44e66237daf9048372c6b435c838f",
  "settings": {
    "is_hidden": false
  }
}
```

`AbilityTask_WaitForInteractableTargets_SingleLineTrace` is a Gameplay [Ability Task](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-tasks-in-unreal-engine), which performs a line trace and waits in a looped timer until it hits an Actor that implements the interface.

As an example:

A player controlling a LyraPawnActor is low on health, the player directs the Pawn towards a collectible health item pickup. Upon aligning the player's crosshair with the Collectible, and pressing the "Use/Interact" key, a Line Trace is fired from the Pawn. When the trace hits the Collectible, the interaction interface implemented on the Collectible will handle the logic to restore the Player's health to its full amount.

## Interaction Ability Tasks

`UAbilityTask_WaitForInteractableTargets` is used to make a new method of tracing for interactable targets.

As an example:

A player controlling a LyraPawnActor approaches a door that they want to open. Upon aligning the player's crosshair with the door and pressing the "Use" key, a radial menu appears with the options to "Unlock/Lock" the door, or attempt to open the door.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For additional information on Line Traces in Unreal, See <a data-document-id=\"3230152\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/traces-tutorials-in-unreal-engine\">Tracing</a>",
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

**UAbilityTask\_WaitForInteractableTargets.h**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#pragma once\n\t\t#include &quot;CoreMinimal.h&quot;\n\t\t#include &quot;UObject/ObjectMacros.h&quot;\n\t\t#include &quot;Abilities/Tasks/AbilityTask.h&quot;\n\t\t#include &quot;Engine/EngineTypes.h&quot;\n\t\t#include &quot;CollisionQueryParams.h&quot;\n\t\t#include &quot;WorldCollision.h&quot;\n\t\t#include &quot;Engine/CollisionProfile.h&quot;\n\t\t#include &quot;Abilities/GameplayAbilityTargetDataFilter.h&quot;\n\t\t#include &quot;Interaction/InteractionOption.h&quot;\n",
  "lines_of_code": 44,
  "id": 149398,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNDkzOTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowMzo1MSswMDowMCJ9--18550bf2df6ea01de1b583e01a794cf489880fd946c9a8b0c79300a143094154",
  "settings": {
    "is_hidden": false
  }
}
```

Your chosen AbilityTask for tracing delivers a set of Interactable targets from the `FInteractionQuery` struct.

**struct FInteractionQuery**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#pragma once\n\t\t#include &quot;CoreMinimal.h&quot;\n\t\t#include &quot;Abilities/GameplayAbility.h&quot;\n\t\t#include &quot;InteractionQuery.generated.h&quot;\n\n\t\t/**  */\n\t\tUSTRUCT(BlueprintType)\n\t\tstruct FInteractionQuery\n\t\t{\n\n",
  "lines_of_code": 25,
  "id": 149399,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNDkzOTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowMzo1MSswMDowMCJ9--6efac5a637dd58fc93bf92d8465ebd779018c641e352c6b072da0b4888296cd5",
  "settings": {
    "is_hidden": false
  }
}
```

to the method `UAbilityTask_WaitForInteractableTargets::UpdateInteractableOptions`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "void UAbilityTask_WaitForInteractableTargets::UpdateInteractableOptions(const FInteractionQuery&amp; InteractQuery, const TArray&lt;TScriptInterface&lt;IInteractableTarget&gt;&gt;&amp; InteractableTargets)\n\t\t{\n\n\t\t\tTArray&lt;FInteractionOption&gt; NewOptions;\n\n\t\t\tfor (const TScriptInterface&lt;IInteractableTarget&gt;&amp; InteractiveTarget : InteractableTargets)\n\n\t\t\t{\n\n\t\t\t\tTArray&lt;FInteractionOption&gt; TempOptions;\n",
  "lines_of_code": 126,
  "id": 149400,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNDk0MDAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowMzo1MSswMDowMCJ9--6db480342b1220cf61ff436a160f51dfafb96b7f7d6e18e764af4c6375c85c36",
  "settings": {
    "is_hidden": false
  }
}
```

which will call `IInteractableTarget::GatherInteractionOptions` on each interactable target.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "virtual void GatherInteractionOptions(const FInteractionQuery&amp; InteractQuery, FInteractionOptionBuilder&amp; OptionBuilder) = 0;",
  "lines_of_code": 1,
  "id": 149401,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNDk0MDEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowMzo1MSswMDowMCJ9--0afba408803448ef5d2affb0bb6ccfc39371e6dae9b933c80edb0c134f3da87f",
  "settings": {
    "is_hidden": false
  }
}
```

Once you update the set of interactable objects, the interaction ability (GA\_Interact) calls the `TriggerInteraction` function when the player focuses on an object to interact with and receives input from the player that they want to interact with that particular object.

Once you invoke the current Option, there are two methods by which interactions can occur. The first method grants an ability to the player's Ability System Component through the function `FInteractionOption::InteractionAbilityToGrant`, using this function is recommended for simple logic such as the Weapon Pickup Actor.

Alternatively, if you're interacting with an object that contains its own Ability System Component to handle complex logic, then you can invoke the `FInteractionOption::TargetAbilitySystem` and the `FInteractionOption::TargetInteractionHandle` functions, this invokes the ability on the interactable object, instead of invoking the ability on the Lyra Character's (Avatar) Ability System Component.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The interaction function <code>FInteractionOption::InteractionAbilityToGrant</code> is inherited from the base class of your <code>ULyraGameplayAbility_Interact</code> interaction ability, which runs the task function <code>AbilityTask_GrantNearbyInteraction</code>, as a ranged loop and timer that collects nearby abilities and grants them to your character before you attempt to interact with them. You can increase the <code>InteractionScanRate</code> float to be at a larger radius than your <code>InteractionRange</code>, otherwise, replication will not deliver the ability to the client soon enough.",
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

The ability is invoked through the event [Gameplay Tag](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-gameplay-tags-in-unreal-engine?application_version=5.5), `FInteractionOption::InteractionEventTag`. This tag needs to match up to a trigger in your ability. For example, the `GA_Collect_Interaction` is triggered when the `Ability.Type.Interact.Collect` event is sent, which is set in the interaction option.

![Image](https://dev.epicgames.com/community/api/documentation/image/e9a930d2-0c77-4053-9634-4b342fd2a5ad)

`GA_Collect_Interaction` represents only one kind of interaction, it is an ability that provides you the capability to pick up objects on the ground and add them to your inventory. There is no limit to your imagination, you can make an ability to eat Apples on the ground that will refill your player's health, or you could make an ability to open doors, get into a vehicle, or open a chest.

This decoupling behavior provides you with all kinds of different interactions from the central passive interaction scanner.

#### Important Lyra Interaction Terminology

**InteractableTarget** - An Actor or Component that implements the IInteractableTarget interface, this determines what objects in the world can be interacted with.

**InteractionOption** - The "Affordance" or "Option", for example, an apple might provide both a "Collect" and a "Consume".

**InteractionInstigator** - The Pawn (LyraPawnActor) that initiates the interaction. They may or may not implement the `IInteractionInstigator` interface, which allows further customization of options and how they are presented.
