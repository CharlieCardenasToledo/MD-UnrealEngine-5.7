# Replicated Object Execution Order

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/replicated-object-execution-order-in-unreal-engine

> Application Version: 5.7

Unreal Engine's (UE) network replication uses a combination of reliable and unreliable communication methods to transfer information between servers and connected clients. *Reliable* communication is continually sent, halting all other network communication, until the receiving machine acknowledges it. *Unreliable* communication is sent and not resent during the current network tick if the receiving machine does not acknowledge receipt.

It is essential to understand what is guaranteed when it comes to actor property and remote procedure call (RPC) replication with respect to the relative ordering of this communication and what you can do to take this into account in your game code. This page describes what guarantees UE's replication system makes and, equally as important, does not make.

## Actor Properties

Actor property updates are unreliable and sent in a single bunch. They can be thought of as a single, unreliable RPC sent after all other RPCs, but before queued RPCs. For more information about queued RPCs, see the [Force Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/replicated-object-execution-order-in-unreal-engine?application_version=5.5) section of this page.

### Replicated Using Order

There is no deterministic order between the OnRep (RepNotify) callbacks of different replicated variables. The call order on the client has no relation with a variable marked dirty or its declaration location in memory. If you need a reliable order between multiple variables, we recommend that you store them together in a struct.

If the order of an actor's property replication is important to your game, you might need to implement OnReps to track per-frame property updates. After the replicated values are received and their OnReps called, you can handle the changes in the [UObject::PostRepNotifies](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/UObject/PostRepNotifies?application_version=5.5) function. You might also need to save certain received values in their respective OnReps until they are ready to be used.

## Remote Procedure Calls

The replication system in Unreal Engine executes RPCs as reliably as possible, so gameplay systems can be built without worrying about networking side effects.

### Order Across Actors

There is no mechanism in which the original call order of RPCs across multiple actors is preserved and reapplied on a remote machine. Consider the following example of RPC call order on the sending machine:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "AActor* MyActor;\n    AActor* OtherActor;\n\n    // Valid MyActor pointer\n    MyActor-&gt;ClientRPC1();\n    OtherActor-&gt;ClientRPC2();\n    MyActor-&gt;ClientRPC3();",
  "lines_of_code": 7,
  "id": 150616,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--60631fa37c5920dbb4e1d8a4f33eff5d1d40b3b82746dcf15506bc7a27d689cd",
  "settings": {
    "is_hidden": false
  }
}
```

In this example, the execution order of the RPCs on the receiving machine is *not* deterministic, and the RPCs can execute in any possible combination on the receiving machine:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC2 --&gt; RPC3\n    RPC1 --&gt; RPC3 --&gt; RPC2\n    RPC2 --&gt; RPC1 --&gt; RPC3\n    RPC2 --&gt; RPC3 --&gt; RPC1\n    RPC3 --&gt; RPC1 --&gt; RPC2\n    RPC3 --&gt; RPC2 --&gt; RPC1",
  "lines_of_code": 6,
  "id": 150617,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--25af39cf4236bc4469a85313c5845823adec273885d47da860324c852af9d549",
  "settings": {
    "is_hidden": false
  }
}
```

### Order Inside an Actor

The replication system does guarantee the call order of reliable RPCs on the same actor. The order in which they are executed on the receiving machine is the same order in which they are called on the sending machine. If the call order on the sending machine is:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "AActor* MyActor;\n\n    // Valid MyActor pointer\n    MyActor-&gt;ClientReliableRPC1();\n    MyActor-&gt;ClientReliableRPC2();\n    MyActor-&gt;ClientReliableRPC3();",
  "lines_of_code": 6,
  "id": 150618,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--e607994c2103b3cdf2c603be1240b6c12e145999decd560b5afe0c679c5d351a",
  "settings": {
    "is_hidden": false
  }
}
```

then the receiving machine always executes the RPCs in this order:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC2 --&gt; RPC3",
  "lines_of_code": 1,
  "id": 150619,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--c237913b92965ded8d0c0985d99f5a4f171e3c3d4f9332811a952eb27602c615",
  "settings": {
    "is_hidden": false
  }
}
```

### Order Between Actor and Subobjects

The order of RPC execution on the receiving machine is respected for all RPCs called on an actor and its subobjects. For example, if the sending machine sends:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "AActor* MyActor;\n\n    // Valid MyActor pointer\n    MyActor-&gt;RPC1();\n    MyActor-&gt;SubObject1-&gt;RPC2();\n    MyActor-&gt;SubObject2-&gt;RPC3();\n    MyActor-&gt;RPC4();",
  "lines_of_code": 7,
  "id": 150620,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--a52d080bb6adac4984f79d2d484e2564ef21ac057ebdc5489251b03629cf6eaa",
  "settings": {
    "is_hidden": false
  }
}
```

the execution order on the receiving machine is:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC2 --&gt; RPC3 --&gt; RPC4",
  "lines_of_code": 1,
  "id": 150621,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--f93a4faf6f91c0bfdb65ec9a3700ed05fcb331103cbf13370ec86c3b4d43d945",
  "settings": {
    "is_hidden": false
  }
}
```

### Unreliable Versus Reliable Ordering

The order of RPC execution between unreliable and reliable RPCs can seem preserved, but this is never guaranteed. When no packet loss or packet reordering occurs, the execution order between unreliable and reliable is the same on the receiving machine as on the sending machine. Consider the following example of RPC call order on the sending machine:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "AActor* MyActor;\n\n    // Valid MyActor pointers\n    MyActor-&gt;ClientReliableRPC1();\n    MyActor-&gt;ClientUnicastUnreliableRPC2();\n    MyActor-&gt;ClientReliableRPC3();",
  "lines_of_code": 6,
  "id": 150622,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--9d6d98a7182f8c3a2c61204e8f36eafe6c468357ee70a29e48982fce732e43e0",
  "settings": {
    "is_hidden": false
  }
}
```

It is possible that if no packet loss or reordering occurs, the receiving machine executes the RPCs in this order:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC2 --&gt; RPC3",
  "lines_of_code": 1,
  "id": 150623,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--cc5d43d6801862ee1f66c11d4f08dc0c6cf1c40609455d10692af705f9026120",
  "settings": {
    "is_hidden": false
  }
}
```

If `RPC1` is in an individual packet that is dropped or reordered, the receiving machine executes:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC2 --&gt; RPC1 --&gt; RPC3",
  "lines_of_code": 1,
  "id": 150624,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--6d6a3f00d3ffead4ee72ba608cc997cdaf3cd225cbd1d681bc1ac4eff57fb854",
  "settings": {
    "is_hidden": false
  }
}
```

If `RPC2` is in an individual packet that is dropped, the receiving machine executes:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC3",
  "lines_of_code": 1,
  "id": 150625,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--13b8bbd7466772bf17dc7528737ae7dbc391eda583024851a2449f4ba9dbba57",
  "settings": {
    "is_hidden": false
  }
}
```

In this last case, `RPC2` is dropped and never executed on the receiving machine since it is unreliable.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "There should be no scenario in which unreliable <code>RPC2</code> is executed after <code>RPC3</code>. If the packet containing <code>RPC2</code> is reordered and arrives later than <code>RPC3</code>, it is ignored on reception.",
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

### Multicast Versus Unicast Ordering

Multicast RPC ordering is more complicated since UE's replication system does not always preserve the call order between multicast RPCs and unicast RPCs.

#### Multicast is Reliable

The call order between reliable multicasts and other reliable unicast RPCs is preserved. For example, if the following functions are called in this order on the sending machine:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MyActor-&gt;MulticastReliableRPC1();\n    MyActor-&gt;UnicastReliableRPC2();\n    MyActor-&gt;UnicastReliableRPC3();\n    MyActor-&gt;MulticastReliableRPC4();",
  "lines_of_code": 4,
  "id": 150626,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--94b63392515083f2e09b4a74f21591abe5c181aed4df2e781c3c58332c76265c",
  "settings": {
    "is_hidden": false
  }
}
```

then the receiving machine or machines execute the RPCs in this order:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC2 --&gt; RPC3 --&gt; RPC4",
  "lines_of_code": 1,
  "id": 150627,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--dc5b9b6c2c0713ac32cd88d3af4225ab4c3cf264a2344ea2509292de43584486",
  "settings": {
    "is_hidden": false
  }
}
```

Remember that the ordering of unreliable `RPC3` is not deterministic and it could be executed earlier or not at all.

#### Multicast is Unreliable

Unreliable multicasts never preserve their call order between other unicasts and reliable multicasts. For example, if the following RPCs are called in this order on the sending machine:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MyActor-&gt;MulticastUnreliableRPC1();\n    MyActor-&gt;UnicastReliableRPC2();\n    MyActor-&gt;MulticastUnreliableRPC3();\n    MyActor-&gt;UnicastUnreliableRPC4();",
  "lines_of_code": 4,
  "id": 150628,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--33cf5015e4f8f21abe6b801c385877fa906e51ede260cdc0db1922fd01de6618",
  "settings": {
    "is_hidden": false
  }
}
```

then the receiving machine or machines execute the RPCs in this order:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC2 --&gt; RPC4 --&gt; RPC1 --&gt; RPC3",
  "lines_of_code": 1,
  "id": 150629,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MjksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--af7baa5d99c83202157696eb446a4c279036901b117cb0d059c8bf94dfb06745",
  "settings": {
    "is_hidden": false
  }
}
```

`RPC1` and `RPC3` are queued and serialized last because they are unreliable multicast RPCs. This means unicasts are executed first, and unreliable multicasts are executed last. The rules governing dropped, unreliable unicast RPCs also apply here.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If <code>RPC2</code> is in an individual packet that is dropped or reordered, the receiving machine executes the RPCs in the following order:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "code_snippet",
      "description": "",
      "snippet_type": "cpp_programming",
      "title": "",
      "code_preview": "RPC1 --&gt; RPC3 --&gt; RPC2 --&gt; RPC4",
      "lines_of_code": 1,
      "id": 150630,
      "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--0dd5fa705c49c29db7a7b9d7a0980b0ae718d45d1dbd04beb476c7de155d3d97",
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

### RPC Send Policy

It is possible to assign RPCs an explicit send policy that affects the ordering of RPCs. This can be done by specifying an `ERemoteFunctionSendPolicy`. For more information about RPC send policies, see the [Remote Procedure Call](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-procedure-calls-in-unreal-engine?application_version=5.5) documentation.

#### Force Send

An RPC with the `ERemoteFunctionSendPolicy::ForceSend` policy changes the order of unreliable multicast RPCs and prevents them from being queued. The following is an example:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MyActor-&gt;ForceSendMulticastUnreliableRPC1();\n    MyActor-&gt;UnicastReliableRPC2();\n    MyActor-&gt;MulticastUnreliableRPC3();\n    MyActor-&gt;UnicastUnreliableRPC4();",
  "lines_of_code": 4,
  "id": 150631,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--caf44e3c6686c69b6f9b1e0e269e2f9774ad7c6ea18169605d9ae4ad50d89346",
  "settings": {
    "is_hidden": false
  }
}
```

The clients execute these RPCs in the following order:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC2 --&gt; RPC4 --&gt; RPC3",
  "lines_of_code": 1,
  "id": 150632,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--67d1a3ef893cd8b7f5efd590af945158106403c85c6c677bc97f29a9db596cc9",
  "settings": {
    "is_hidden": false
  }
}
```

#### Force Queue

An RPC with the `ERemoteFunctionSendPolicy::ForceQueue` policy does not respect the call order except with other `ForceQueue` RPCs and unreliable multicasts. The following is an example:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MyActor-&gt;ForceQueueRPC1();\n    MyActor-&gt;UnicastReliableRPC2();\n    MyActor-&gt;MulticastUnreliableRPC3();\n    MyActor-&gt;UnicastUnreliableRPC4();",
  "lines_of_code": 4,
  "id": 150633,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--e2e4dfb889661cab5b19b939fafa5a22ca1f5c94f34adbd6b6652d31fd7dda71",
  "settings": {
    "is_hidden": false
  }
}
```

The clients execute these RPCs in the following order:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC2 --&gt; RPC4 --&gt; RPC1 --&gt; RPC3",
  "lines_of_code": 1,
  "id": 150634,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--4c438261f12bcd91b7e40e32049247698bbf98360cc8a25b3638bb656c25d7b3",
  "settings": {
    "is_hidden": false
  }
}
```

## Order Between RPCs and Actor Properties

It is also important to understand the order between RPC executions and when replicated property updates are applied. In this case, the following rules apply:

- RPCs are executed first.
- Properties are updated second.
- Property updates are sent as a single, unreliable data block.

The bunch payload is constructed as follows:

- Non-queued RPCs are serialized.
- Replicated property data is serialized.
- Queued RPCs are serialized.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "It is possible that a replicated variable written from inside an RPC might get lost and overwritten immediately by unprocessed property updates.",
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
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "An exception to this rule is unreliable multicast RPCs since they are queued at the call site and always serialized last. This means they are executed <em>after</em> property updates are applied.",
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

The following is an example:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MyActor-&gt;ReliableRPC1();\n    MyActor-&gt;bReplicatedVar1 = true\n    MyActor-&gt;MulticastUnreliableRPC2();\n    MyActor-&gt;bReplicatedVar2 = true;\n    MyActor-&gt;ReliableRPC3();",
  "lines_of_code": 5,
  "id": 150635,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--f33e0198df6a84c58e3259b508c48f5bcb09d86c71edf2cc0a0ad584acf0be10",
  "settings": {
    "is_hidden": false
  }
}
```

The remote machine or machines execute these in the following order:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC3 --&gt; Var1 &amp;&amp; Var2 --&gt; RPC2",
  "lines_of_code": 1,
  "id": 150636,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--b2b69700659e5de5c60d93efe6d69ca6c601f8c3568bc42794860eade3bdf426",
  "settings": {
    "is_hidden": false
  }
}
```

The following is another example of property updates mixed with RPCs:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MyActor-&gt;ReliableRPC1();\n    MyActor-&gt;bReplicatedVar1 = true\n    MyActor-&gt;MulticastUnreliableRPC2();\n    MyActor-&gt;bReplicatedVar2 = true;\n    MyActor-&gt;ReliableRPC3();",
  "lines_of_code": 5,
  "id": 150637,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--0f810a404144d7df353d67c2647dfca2a99c2b5528176cc7d1db5c6b2b6191a6",
  "settings": {
    "is_hidden": false
  }
}
```

Suppose that the property update is dropped, then the receiving machine or machines execute the RPCs and property updates in the following order:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "RPC1 --&gt; RPC3 --&gt; RPC2\n    // After the next update\n    Var1 &amp;&amp; Var2",
  "lines_of_code": 3,
  "id": 150638,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--61df8fb35d1c5ea7f6686722559abc8a2475f3532859675a646af3ff81bf7538",
  "settings": {
    "is_hidden": false
  }
}
```

Another scenario, where only the reliable RPC1 is dropped, results in the following execution order on the receiving machine or machines:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Var1 &amp;&amp; Var2 --&gt; RPC2 --&gt; RPC1 --&gt; RPC3",
  "lines_of_code": 1,
  "id": 150639,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA2MzksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowOToyNCswMDowMCJ9--0a63e380669a69c8a09158b3427dfc61ba4cab4cf45547db2dcfa14325b0cd2e",
  "settings": {
    "is_hidden": false
  }
}
```

## Test Gameplay Code with Unreliable RPCs

If you are creating or relying on code that is replicated using unreliable RPCs, it is a good idea to force them to be dropped and see how your systems react. For more information about how to do this by emulating poor network conditions, see the [Using Network Emulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-network-emulation-in-unreal-engine) documentation.
