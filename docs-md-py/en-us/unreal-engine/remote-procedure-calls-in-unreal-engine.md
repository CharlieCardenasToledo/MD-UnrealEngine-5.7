# Remote Procedure Calls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-procedure-calls-in-unreal-engine

> Application Version: 5.7

**Remote Procedure Calls (RPCs)** are functions called locally that execute remotely on one or more connected machines. RPCs help clients and the server call functions on one another over a network connection. RPCs are unidirectional function calls, as such, they cannot specify a return value. The primary use case for RPCs is to perform unreliable gameplay events that are transient or cosmetic in nature. These could include events such as:

- Playing sounds
- Spawning particles
- Performing Animations

RPCs are an important mechanism that supplement replicated properties that use the `Replicated` or `ReplicatedUsing` specifiers. To call an RPC, you must call the RPC from an actor or actor component and set the actor and relevant actor component to replicate.

It is important to first understand how ownership works with RPCs, since actor ownership determines where RPCs remotely execute. For more information about actor ownership, see the [Actor Owner and Owning Connection](https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-owner-and-owning-connection-in-unreal-engine?application_version=5.5) documentation.

## Types of RPC

There are four different types of RPCs as outlined in the following table:

| Metadata Specifier | Description |
| --- | --- |
| `Client` | The RPC is executed on the owning client connection for this actor. |
| `Server` | The RPC is executed on the server. |
| `Remote` | The RPC is executed on the remote side of the connection. |
| `NetMulticast` | The RPC is executed on the server and all currently connected clients the actor is relevant for. |

## Structure of an RPC

All RPCs consist of two pieces:

- The base function defined in your header file.
- The implementation function that contains the base function implementation in your source file.

Unreal Engine's reflection and replication systems manage the lower level details, but require that you define and implement these pieces. The following sections explain how to declare and implement an RPC.

## Create an RPC

To create an RPC for an actor, follow these steps:

1. Choose one of the function metadata specifiers from the [Types of RPC](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-procedure-calls-in-unreal-engine?application_version=5.5) section:
2. Ensure that your `AActor`-derived class is set to replicate within the derived actor's constructor:
3. Implement your RPC’s `_Implementation` function:

## Execute an RPC

To execute an RPC, call the standard version of the RPC function:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Call from client to run on server\n\tADerivedClientActor* MyDerivedClientActor;\n\tMyDerivedClientActor-&gt;ServerRPC();\n\n\t// Call from server to run on client\n\tADerivedServerActor* MyDerivedServerActor;\n\tMyDerivedServerActor-&gt;ClientRPC();\n\n\t// Call from server to run on server and all relevant clients\n\tADerviedServerActor* MyDerivedServerActor;\n",
  "lines_of_code": 11,
  "id": 150798,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA3OTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDoxNiswMDowMCJ9--1bd3b5a76560acdc5c88d2b20b56020231746a80375263f1b1ac7f9d35ac7b76",
  "settings": {
    "is_hidden": false
  }
}
```

## Unicast Versus Multicast

`Client`, `Server`, and `Remote` RPCs are unicast RPCs. *Unicast* RPCs are so named because they execute on a single machine. `NetMulticast` is a *multicast* RPC because it executes on multiple machines.

## Matrix of RPC Execution

The following table describes on which machine an RPC is executed depending on what type of RPC it is, what machine it is called from, and the owning connection for the actor calling the RPC. You can read the columns of the following tables as follows:

A [*Type of RPC*] called from a/the [*Calling Machine*] whose associated actor's owning connection is a/the [*Owning Connection*] is executed on the [*Executing Machine*].

For example, the first row in the Server RPC table reads:

- A *Server RPC* called from the *Server* whose associated actor's owning connection is the *Client* is executed on the *Server*.

The last row in the Client RPC table reads:

- A *Client RPC* called from the *Client* whose associated actor's owning connection is *None* is executed on the *Invoking Client*.

### Server RPC

| Calling Machine | Owning Connection | Executing Machine |
| --- | --- | --- |
| Server | Client | Server |
| Server | Server | Server |
| Server | None | Server |
| Client | Invoking Client | Server |
| Client | Different Client | Dropped |
| Client | Server | Dropped |
| Client | None | Dropped |

### Client RPC

| Calling Machine | Owning Connection | Executing Machine |
| --- | --- | --- |
| Server | Owning Client | Owning Client |
| Server | Server | Server |
| Server | None | Server |
| Client | Invoking Client | Invoking Client |
| Client | Different Client | Invoking Client |
| Client | Server | Invoking Client |
| Client | None | Invoking Client |

### Remote RPC

| Calling Machine | Owning Connection | Executing Machine |
| --- | --- | --- |
| Server | Owning Client | Owning Client |
| Server | Server | Dropped |
| Server | None | Dropped |
| Client | Invoking Client | Server |
| Client | Different Client | Dropped |
| Client | Server | Dropped |
| Client | None | Dropped |

### Net Multicast RPC

| Calling Machine | Owning Connection | Executing Machine |
| --- | --- | --- |
| Server | Client | Server and all Clients the invoking actor is relevant for |
| Server | Server | Server and all Clients the invoking actor is relevant for |
| Server | None | Server and all Clients the invoking actor is relevant for |
| Client | Invoking Client | Invoking Client |
| Client | Different Client | Invoking Client |
| Client | Server | Invoking Client |
| Client | None | Invoking Client |

## Reliability

RPCs in Unreal Engine are marked as either reliable or unreliable:

| Metadata Specifier | Description | Order of Execution |
| --- | --- | --- |
| `Reliable` | This RPC is re-sent until it is acknowledged by the receiver. All subsequent RPC executions are suspended until this RPC is acknowledged. | Guaranteed in order. |
| `Unreliable` | This RPC is not executed if the packet is dropped. | No order guarantee. |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "RPCs are unreliable by default. Reliable RPCs require additional bandwidth, as such, use them sparingly.",
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

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For more information about order of execution guarantees for replication in Unreal Engine, see the <a data-document-id=\"3230527\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/replicated-object-execution-order-in-unreal-engine?application_version=5.5\">Replicated Object Execution Order</a> documentation.",
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

### Specify RPC Reliability

To specify the reliability of an RPC, add the appropriate metadata specifier for your RPC:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "DerivedActor.h",
  "code_preview": "#pragma once\n\n\t#include &quot;DerivedActor.generated.h&quot;\n\n\tUCLASS()\n\tclass ADerivedActor : public AActor\n\t{\n\t\tGENERATED_BODY()\n\n\tpublic:\t\n",
  "lines_of_code": 23,
  "id": 150799,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA3OTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDoxNiswMDowMCJ9--df37efd60bbc0f3e875aae6715cbc67c05fbac4d628b24e045c6254ba16f61f2",
  "settings": {
    "is_hidden": false
  }
}
```

## Send Policy

It is possible to assign RPCs an explicit send policy that affects the ordering of RPCs. This can be done by specifying an `ERemoteFunctionSendPolicy`:

| Value | Description |
| --- | --- |
| `Default` | The RPC is serialized in the [bunch](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-procedure-calls-in-unreal-engine?application_version=5.5#bunch) immediately and the bunch is sent in the next net update at the end of the frame. |
| `ForceSend` | If the RPC is triggered in `NetDriver::PostTickDispatch`, the RPC is serialized in the bunch immediately and sent over the network. If the RPC is triggered during the rest of the tick, the RPC is sent according to the `Default` behavior. This is a special RPC optimization that works under the following conditions: Only supported by Replication Graph and Iris Works on RPCs called in `NetWorldTickTime` where incoming packets are processed and RPCs sent from remote connections are executed. |
| `ForceQueue` | The RPC is serialized in the bunch at the end of the net update if there is any bandwidth left. |

To specify a send policy for RPCs in your project, see [UNetDriver::ProcessRemoteFunctionForChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Engine/UNetDriver/ProcessRemoteFunctionForChannel?application_version=5.5). For more information about guarantees with respect to the order of execution for RPCs on remote machines, see the [Replicated Object Execution Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/replicated-object-execution-order-in-unreal-engine?application_version=5.5) documentation.

##### Bunch

In Unreal Engine networking, a network packet is composed of several bunches. A *bunch* is a collection of property changes and RPCs for a particular replicated object, such as an actor.

## Server RPC Validation

Server RPC validation implements a *trust and verify* networking policy. The server trusts the information that the client communicates to it, but always verifies that this information follows the rules and constraints defined by the game on the server.

You can mark a server RPC with the `WithValidation` `UFUNCTION` metadata and define a corresponding server RPC validation function. The validation function has the same name as your RPC function, but with `_Validate` appended to the end of the function name. The return type is a boolean, and it takes the same parameters as the RPC function that it is associated with. The validation function helps the server determine whether an RPC should or should not run, depending on the validation logic you define. When a client makes a call to execute a server RPC, the validation function is called first on the server.

The following occurs based on the output of the validation function:

- If the inputs pass validation, the implementation is called.
- If the inputs fail validation, the invoking client is disconnected from the server.

### Add a Validation Implementation

To add a validation function for your RPC, follow these steps:

1. Follow the steps to [Declare a Server RPC](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-procedure-calls-in-unreal-engine?application_version=5.5) and add the `WithValidation` metadata specifier:
2. Implement the validation function:

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If a server RPC fails validation, the calling client is disconnected.",
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

## RPCs in Blueprint

The same types of RPCs, reliability options, and execution logic that exist for RPCs in C++ also exist for RPCs in Blueprint.

### Create a Blueprint RPC

You can also create RPCs in Blueprint using replicated Blueprint events. To create a replicated Blueprint event, follow these steps:

1. Create or open a Blueprint Actor or Actor-derived class.
2. Ensure that your Blueprint is set to **Replicate** in your Blueprint's **Details Panel**. ![Set actor to replicate.](https://dev.epicgames.com/community/api/documentation/image/b53b0018-4dab-45f5-81ed-b2c302a1e65c)
3. Open your Blueprint's **Event Graph**. ![Open Blueprint event graph.](https://dev.epicgames.com/community/api/documentation/image/93300fea-6bb0-4738-9d9a-8249264004ff)
4. Right-click and choose **Add Event > Add Custom Event…** ![Add a custom event.](https://dev.epicgames.com/community/api/documentation/image/d24ac34e-7675-4fde-b8db-d22014da2e77)
5. Click on your **CustomEvent** node to bring up the **Details Panel**. ![Open Custom Event details panel.](https://dev.epicgames.com/community/api/documentation/image/3fad3640-437f-4a4c-b301-6c7b85285fed)
6. You can choose whether your event replicates, which type of replication it uses, and whether it is reliable or unreliable under **Details Panel > Graph > Replicates**. ![Set Custom Event to replicate.](https://dev.epicgames.com/community/api/documentation/image/b71204c0-dcb7-43f9-a2fb-fddc702bf79a)
7. Once you have chosen your desired settings, define your RPC functionality in your Blueprint's Event Graph. ![Implement replicated event.](https://dev.epicgames.com/community/api/documentation/image/ffb707ce-f97f-4601-b3b5-6b080878f3df)

### Execute a Blueprint RPC

You can execute a Blueprint RPC like any other Blueprint event, but the same rules apply as for RPCs defined in C++. An RPC can only be executed from a replicated actor or actor component with a valid owner and owning connection.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code>Remote</code> RPCs are not currently exposed to Blueprints.",
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
