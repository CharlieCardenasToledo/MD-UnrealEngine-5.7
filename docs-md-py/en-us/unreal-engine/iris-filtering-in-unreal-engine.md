# Filtering

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine

> Application Version: 5.7

The **Iris Filtering System** determines what objects are replicated to which connections. There might be actors or objects in your game that you only want replicated to certain connections. To save time and bandwidth, the filtering system filters which connections an actor or object can replicate. The filtering system supports four different filtering types:

- [Owner](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine#owner): Object replicates to the same connections as its owner.
- [Connection](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine#connection): Object replicates to specified, allowed connections and does not replicate to specified, disallowed connections.
- [Group](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine#group): Object replicates to the same connections as all other objects in its group.
- [Dynamic](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine#dynamic): Object replicates based on custom, dynamic filtering.

## Owner

Actors with the `bOnlyRelevantToOwner` flag set to `true` automatically enable owner filtering. You can also enable owner filtering for standalone objects other than actors.

### Set Owner Filters For Objects

To enable owner filtering for objects other than actors, follow these steps:

1. Include the necessary Iris files in order to access required Iris functionality.
2. In your gameplay code, retrieve the replication system and replication bridge for your replicated object.
3. Retrieve the `FNetRefHandle` for your replicated object. Iris uses this identifier to locate your object within the replication system.
4. Set the owner filter handle for your replicated object.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You should assign the owner filter just after an object's owner is assigned.",
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

### Clear All Filters

To clear all filters on a replicated object, first follow Step 1 and 2 from [Set Owner Filters for Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine), then set the filter to use the following special filter handle:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if UE_WITH_IRIS\n\t#include &quot;Net/Iris/ReplicationSystem/ReplicationSystemUtil.h&quot;\n\t#include &quot;Iris/ReplicationSystem/ReplicationSystem.h&quot;\n\t#include &quot;Net/Iris/ReplicationSystem/ActorReplicationBridge.h&quot;\n\t#include &quot;Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h&quot;\n\t#endif UE_WITH_IRIS\n\n\tUReplicationSystem* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr);\n\tUActorReplicationBridge* ReplicationBridge = UE::Net::FReplicationSystemUtil::GetActorReplicationBridge(RepActorPtr);\n\n",
  "lines_of_code": 14,
  "id": 78143,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE0MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--b8deb9e6aecfbc018bc3143d6158011b3e0e9246d94e9b6a65492b48459354ee",
  "settings": {
    "is_hidden": false
  }
}
```

## Connection

You can set the connections an object replicates to by specifying connection IDs. We advise using this option when:

- The allowed connections for the object in question are static, and…
- Only a few objects are affected if the connection IDs change for some reason.

If a large number of objects might be affected, consider using group filtering instead. Connection filtering enables you to add either allowed or disallowed connections to an object.

### Set Connection Filters

To add allowed connections:

1. Set the bits for all connections for which the object is allowed to be replicated
2. Initialize the connection with a maximum number of allowed connections before setting the connection filter.

Similar logic applies to add disallowed connections. Instead of using the `ENetFilterStatus::Allow`, use the `ENetFilterStatus::Disallow` value. In this case, the provided connections are disallowed connections for the object to replicate to.

### Clear Connection Filters

Connection filtering for an object is cleared differently than owner filters. To clear connection filters for an object, set a disallowed connection filter, but specify no provided connections to disallow:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if UE_WITH_IRIS\n\t#include &quot;Net/Iris/ReplicationSystem/ReplicationSystemUtil.h&quot;\n\t#include &quot;Iris/ReplicationSystem/ReplicationSystem.h&quot;\n\t#include &quot;Net/Iris/ReplicationSystem/ActorReplicationBridge.h&quot;\n\t#include &quot;Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h&quot;\n\t#endif UE_WITH_IRIS\n\n\tUReplicationSystem* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr);\n\tUActorReplicationBridge* ReplicationBridge = UE::Net::FReplicationSystemUtil::GetActorReplicationBridge(RepActorPtr);\n\n",
  "lines_of_code": 15,
  "id": 78145,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE0NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--9c4962fa974911b9284a711106b80624ccadbb08151b32d2a12f2fdc6f837e50",
  "settings": {
    "is_hidden": false
  }
}
```

## Group

Iris includes an API for creating groups and managing the objects those groups contain. You can also use groups as a filtering mechanism. This is a flexible way of changing which connections a set of objects can replicate to without requiring you to manually keep track of which objects belong to which groups. Example use cases include filtering based on:

- Team
- Squad
- Streaming Level

An object can belong to more than one group. You must add groups to the filtering system for it to consider them for replication. Once you add them, you can modify which connections members of the group are allowed to replicate. You can set groups as allowed or disallowed for replication to:

- A single connection
- A set of connections
- All connections

### Create a Group

To create a filter group, call the `CreateGroup` function, which returns a unique group handle:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if UE_WITH_IRIS\n\t#include &quot;Net/Iris/ReplicationSystem/ReplicationSystemUtil.h&quot;\n\t#include &quot;Iris/ReplicationSystem/ReplicationSystem.h&quot;\n\t#endif UE_WITH_IRIS\n\n\tUReplicationSystem* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr);\n\tUE::Net::FNetObjectGroupHandle GroupHandle = ReplicationSystem-&gt;CreateGroup();",
  "lines_of_code": 7,
  "id": 78146,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE0NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--ca1a7e085ddc5b55fed77a573ac30158d5469f095f925da18db25604766b8f0e",
  "settings": {
    "is_hidden": false
  }
}
```

### Add Group Filter

You must add the group filter to the filtering system before setting the filter status and adding objects:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if UE_WITH_IRIS\n\t#include &quot;Iris/ReplicationSystem/ReplicationSystem.h&quot;\n\t#endif UE_WITH_IRIS\n\n\t// Add a valid FNetObjectGroupHandle\n\tReplicationSystem-&gt;AddGroupFilter(GroupHandle);",
  "lines_of_code": 6,
  "id": 78147,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE0NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--60a409f77ccb55076ac77907cfa1ca1fbee1077cc97c9014beaa1d9da7caf38f",
  "settings": {
    "is_hidden": false
  }
}
```

### Set Group Filtering

Once you create a group and add the group filter to the replication system, you can set the group filtering. In this example, any object belonging to the group with handle `GroupHandle` is allowed to replicate only to the connection with ID `SpecialConnectionId`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if UE_WITH_IRIS\n\t#include &quot;Iris/ReplicationSystem/ReplicationSystem.h&quot;\n\t#include &quot;Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h&quot;\n\t#endif UE_WITH_IRIS\n\n\t// With a valid FNetObjectGroupHandle and uint32 connection id\n\tReplicationSystem-&gt;SetGroupFilterStatus(GroupHandle, SpecialConnectionId, UE::Net::ENetFilterStatus::Allow);",
  "lines_of_code": 7,
  "id": 78148,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE0OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--13b53f5606881511d7d457a0a70c6856db03c096509187cf5d3614a6ca9a212e",
  "settings": {
    "is_hidden": false
  }
}
```

### Add Object to Group

You can now add your desired object to the group:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if UE_WITH_IRIS\n\t#include &quot;Net/Iris/ReplicationSystem/ActorReplicationBridge.h&quot;\n\t#include &quot;Iris/ReplicationSystem/ReplicationSystem.h&quot;\n\t#endif UE_WITH_IRIS\n\n\tUE::Net::FNetRefHandle RepActorNetRefHandle = ReplicationBridge-&gt;GetReplicatedRefHandle(RepActorPtr);\n\n\t// With a valid FNetObjectGroupHandle and FNetHandle\n\tReplicationSystem-&gt;AddToGroup(GroupHandle, RepActorNetRefHandle);",
  "lines_of_code": 9,
  "id": 78149,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE0OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--d51e3c7a6363c848475acd0afa6087f8823b09e6e35eeed5c56c0d75997e85bd",
  "settings": {
    "is_hidden": false
  }
}
```

## Dynamic

Iris’s filtering system can also implement custom, dynamic filtering with a `UNetObjectFilter`-derived class. Dynamic filters can restrict objects from replicating based on custom logic. Dynamic filters are applied after connection and group filters. This means that a dynamic filter cannot enable replication for an object that has already been filtered out by connection or group filters. An object can only have one dynamic filter set at a time.

Dynamic filters always run on an object, whereas connection and group filtering only run when the system is informed of changes. This is due to the fact that a dynamic filter can be implemented in any way, so there is no way for the system to know whether the dynamic filter needs to run or not. There are situations where a dynamic filter provides the best solution. If you modify groups often, such as moving actors between groups or changing which connections the group may be replicated to, a dynamic filter may provide the best solution.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You should only set a dynamic filter for an object as a last resort. This adds significant CPU overhead versus connection and group filters.",
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

UE provides a few dynamic filters in the directory `..\Engine\Source\Runtime\Experimental\Iris\Core\Public\Iris\ReplicationSystem\Filtering\`:

- `UFilterOutNetObjectFilter`: Disallow replication of any objects added to it.
- `UNetObjectConnectionFilter`: Pre-poll filter that supports per-connection filtering for dependent objects.
- `UNetObjectGridFilter`: Divide the game world into cells and only replicate objects in cells near the player’s view.

To use a custom dynamic filter, you must implement the `UNetObjectFilter` interface and it must be configured with filter definitions in order to be used at runtime.

### Create a Dynamic Filter

To use a custom, dynamic filter, implement the `UNetObjectFilter` interface and configure its filter definitions to use the filter at runtime. The base class your custom filter must inherit from is located at the following file path:

- `..\Engine\Source\Runtime\Experimental\Iris\Core\Public\Iris\ReplicationSystem\Filtering\NetObjectFilter.h`

A minimal, working example of a custom, dynamic filter is provided in:

- `..\Engine\Source\Runtime\Experimental\Iris\Core\Public\Iris\ReplicationSystem\Filtering\NopNetObjectFilter.h`

### Dynamic Filter Configuration

Below is the syntax for engine configuration to use a custom dynamic filter:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[/Script/IrisCore.NetObjectFilterDefinitions]\n\t+NetObjectFilterDefinitions=(FilterName=&lt;FILTER_NAME&gt;, ClassName=/Script/&lt;PROJECT_NAME&gt;.&lt;FILTER_NAME&gt;, ConfigClassName=/Script/&lt;PROJECT_NAME&gt;.&lt;FILTER_NAME&gt;Config)",
  "lines_of_code": 2,
  "id": 78150,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE1MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--7c02ee0eaf6d2e87644240895edb321ee326d243834b90886fc96cbe344fafd5",
  "settings": {
    "is_hidden": false
  }
}
```

For example, a custom, dynamic filter named `MyCustomFilter` in a project named `MyProject` is configured as follows in the engine configuration hierarchy, such as your project’s `DefaultEngine.ini` file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[/Script/IrisCore.NetObjectFilterDefinitions]\n\t+NetObjectFilterDefinitions=(FilterName=MyCustomFilter, ClassName=/Script/MyProject.MyCustomFilter, ConfigClassName=/Script/MyProject.MyCustomFilterConfig)",
  "lines_of_code": 2,
  "id": 78151,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE1MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--252abade1e293bf1599065aa7db0cadf85ae2022fe5f7d3ec955be6caf5952a6",
  "settings": {
    "is_hidden": false
  }
}
```

Once your filter is registered with Iris, you can configure your filter as follows in an engine configuration file such as your project’s `DefaultEngine.ini` file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[/Script/MyProject.MyCustomFilterConfig]\n\tMyCustomFilterVar=100",
  "lines_of_code": 2,
  "id": 78152,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE1MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--f049d695f717544378e00fbb439c37a7be190cabe432da3796753ef2be085b2e",
  "settings": {
    "is_hidden": false
  }
}
```

### Assign Object to Dynamic Filter

To assign a dynamic filter to a replicated object, use the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "const UE::Net::FNetObjectFilterHandle FilterHandle = ReplicationSystem-&gt;GetFilterHandle(FName(&quot;&lt;FILTER_NAME&gt;&quot;));\n\tif (FilterHandle != UE::Net::InvalidNetObjectFilterHandle)\n\t{\n\t\tconst bool bSuccess = ReplicationSystem-&gt;SetFilter(ObjectNetHandle, FilterHandle);\n\t}",
  "lines_of_code": 5,
  "id": 78153,
  "url_signature": "eyJzbmlwcGV0X2lkIjo3ODE1MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjE4KzAwOjAwIn0=--e59824b77a4424bdc5574e008eb44833df505df38a5b0b3333606d49249482da",
  "settings": {
    "is_hidden": false
  }
}
```

### Remove Dynamic Filter

Dynamic filters are removed in the same way as owner filters. To remove any filter, see the [Clear All Filters](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine) section of this page.
