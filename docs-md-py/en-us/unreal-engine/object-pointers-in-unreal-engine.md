# Object Pointers

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/object-pointers-in-unreal-engine

> Application Version: 5.7

Unreal Engine provides several templated, smart pointers for a variety of use-cases. All Unreal Engine object pointer types must be constructed with `UObject` types, that is, classes that derive from `UObject`.

The following table provides an overview of the types of object pointers available in Unreal Engine and some of their properties. The table columns are:

- **Pointer Type**: Type of pointer.
- **Usage**: Is this pointer type commonly used, used with caution, marked for deprecation, or removed.
- **Supports UPROPERTY?**: Whether this pointer type can be marked as a `UPROPERTY`.
- **Impacts GC?**: Whether the existence of a pointer of this type to the target object keeps the referenced object alive.
- **Supports loading on-demand?**: Whether this pointer type tracks the path to the target object on disk so it can be loaded later.
- **Serialized?**: Whether this pointer type supports serializing the target object for storage.
- **Supports networking?**: Has network serializers and is used or supported in replicated properties or remote procedure calls.

Throughout this documentation page, assume a template type `T`.

| Pointer Type | Usage | Supports UPROPERTY? | Impacts GC? | Supports loading on-demand? | Serialized? | Networking support? |
| --- | --- | --- | --- | --- | --- | --- |
| `T*` (Raw Pointer) | Common | ❌\* | ❌\* | ❌ | ❌\* | ❌\* |
| `TObjectPtr<T>` | Common | ✔️ | ✔️ † | ❌ | ✔️ | ✔️ |
| `TLazyObjectPtr<T>` | Deprecated ‡ | ✔️ | ❌ | ❌ | ✔️ | ❌ |
| `TSoftObjectPtr<T>` | Common | ✔️ | ❌ | ✔️ | ✔️ | ✔️ |
| `TWeakObjectPtr<T>` | Common | ✔️ | ❌ | ❌ | ✔️ | ✔️ |
| `TStrongObjectPtr<T>` | Use Caution § | ❌ | ✔️ ❡ | ❌ | ❌ | ❌ |

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<b>Table Footnotes:</b>",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "* Unreal Header Tool (UHT) can be configured to enable raw pointers marked as <code class=\"inline-code\">UPROPERTY</code>, in which case raw pointers impact GC, support serialization, and support networking. Existing <code class=\"inline-code\">UPROPERTY</code>-marked raw pointers should migrate to use <code class=\"inline-code\">UPROPERTY</code>-marked <code class=\"inline-code\">TObjectPtr</code> if possible.    ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "† <code class=\"inline-code\">TObjectPtr</code> is only garbage collection safe if it is marked as a <code class=\"inline-code\">UPROPERTY</code>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "‡ \n\n<code class=\"inline-code\">TLazyObjectPtr</code> is deprecated and marked for removal in a future engine version, use <code class=\"inline-code\">TSoftObjectPtr</code> instead.    ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "§\n\nSee the <code class=\"inline-code\">TStrongObjectPtr</code> section below for more information.   ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "❡ Since <code class=\"inline-code\">TStrongObjectPtr</code> cannot be marked as a <code class=\"inline-code\">UPROPERTY</code>, it affects garbage collection everywhere (on the stack, captured in lambdas, etc.).",
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

## Quick Guide to Object Pointers

Below is a quick guide to determine which pointer to use for the most common use-cases. `TLazyObjectPtr` is omitted from the following table as it is deprecated.

| Use Case... | Use Pointer Type... |
| --- | --- |
| Local variables, parameters, or short-lived references that are not `UPROPERTY`-marked fields. | `T*` (Raw Pointer) |
| Persistent `UObject` reference on a `UCLASS` or `USTRUCT` that is tracked for garbage collection, serialized, or replicated. | `TObjectPtr<T>` |
| Reference to an asset that should not be forced to load until requested or create a hard dependency. | `TSoftObjectPtr<T>` |
| Non-owning reference or cache to a `UObject` that may be destroyed at any point. | `TWeakObjectPtr<T>` |
| Strong reference to a `UObject` from a non-`UObject` class or struct. | `TStrongObjectPtr<T>` |

## Types of Pointers

This section goes into more detail about each pointer type and provides sample use-cases to help you determine when to use each type.

### TObjectPtr

`TObjectPtr` is meant as a drop-in replacement for a raw pointer. `TObjectPtr` can only be used with types derived from `UObject`. It is serialized in the same way as a raw pointer to a `UObject`. When `TObjectPtr` is marked as a `UPROPERTY`, it is a strong reference to an object that impacts garbage collection and prevents garbage collection from destroying the target object.

`TObjectPtr` should be used in place of raw pointers when possible as it supports advanced cook-time dependency tracking and enables barriers for garbage collection which unlocks incremental garbage collection marking. `TObjectPtr` also supports replication.

You should never directly access a `UObject` through a `TObjectPtr` from worker threads unless you are certain the objects they contain are properly rooted already and cannot be garbage collected while you’re accessing them. For working with `UObject`s from worker threads, use a `TWeakObjectPtr` with the `TWeakObjectPtr::Pin` method to obtain a `TStrongObjectPtr` to the target `UObject` if the target object is still valid.

Example use-cases for `TObjectPtr` include:

- `UPROPERTY`-maked pointer to a `UObject` inside another `UObject`.
- Hard reference to an actor component.

### TLazyObjectPtr

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">TLazyObjectPtr</code> is marked for deprecation in a future engine version. New features should use <code class=\"inline-code\">TSoftObjectPtr</code> instead.",
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

`TLazyObjectPtr` is a lazy, GUID-based, weak pointer. `TLazyObjectPtr` does not load the target object if not already loaded and can toggle between valid and pending as the object is loaded and unloaded into memory. `TLazyObjectPtr` does not prevent the target object from being garbage collected.

### TSoftObjectPtr

`TSoftObjectPtr` is a weak reference to an object that tracks the path to the target object on disk and has no impact on whether the pointed to object is garbage collected. Since `TSoftObjectPtr` tracks the path to the object on disk, it may change back and forth between valid and pending as the referenced object loads and unloads into and out of memory. This is useful for assets that you want to load asynchronously on demand or for preventing hard dependencies. You must explicitly load the target object synchronously or asynchronously if it is not yet valid.

Example use-cases for `TSoftObjectPtr` include:

- Synchronous or asynchronous loading of object by path.

### TWeakObjectPtr

`TWeakObjectPtr` is a weak pointer to an object. A `TWeakObjectPtr` does not need to be marked as a `UPROPERTY`, although `UPROPERTY` is supported. `TWeakObjectPtr` supports serialization and is also supported for networking. Most often, `TWeakObjectPtr` is used when you explicitly do not want to prevent an object from being garbage collected. If the target object is garbage collected or destroyed, the weak pointer becomes null automatically. Always check whether a `TWeakObjectPtr` is valid with `TWeakObjectPtr::IsValid` or use `TWeakObject::Get` and test nullity before use.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">TWeakObjectPtr</code> is not supported as a key in a <code class=\"inline-code\">TMap</code>, nor as an element in a <code class=\"inline-code\">TSet</code>. If you wish to use a <code class=\"inline-code\">UObject</code> as a key, use <code class=\"inline-code\">TObjectKey</code> instead.",
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

Example use-cases for `TWeakObjectPtr` include:

- Caching objects.
- Capture a weak object pointer in a lambda.

### TStrongObjectPtr

`TStrongObjectPtr` is a strong pointer to an object. `TStrongObjectPtr` counts references to the target object and prevents garbage collection while it is in scope forcibly keeping the target object alive. `TStrongObjectPtr` does not support `UPROPERTY`, so it is not suited for fields in `UObject`-derived classes. Marking a `TStrongObjectPtr` inside a `UObject` as a `UPROPERTY` is prone to creating uncollectable cycles. For example, if a `UObject`-derived class has a `TStrongObjectPtr` member field that is set to point to itself, this creates an uncollectable cycle, that is, the object will never be deleted, not even if there are no other references to that object (this is not the case with a `TObjectPtr` self-reference). Since `TStrongObjectPtr` does not support `UPROPERTY`, it is also less visible to debugging tools, which makes it more difficult to determine why the target object is still alive.

Creating and destroying a `TStrongObjectPtr` are expensive operations and should be avoided if possible. Use `TStronObjectPtr` for long-lived references that do not change often. As a result, `TStrongObjectPtr` should be avoided in systems such as Mass where objects are unlikely to be deleted between frame updates. Every `TStrongObjectPtr` adds a tracked reference for garbage collection. `TStrongObjectPtr` is always a strong reference keeping the target object alive, even if the object is unreachable and can be garbage collected. As a result, using `TStrongObjectPtr` can degrade performance.

`TStrongObjectPtr` is meant for storing strong references to a `UObject` inside a non-`UObject` owning class, such as a class that does not derive from `UObject` or a struct, since `UPROPERTY` is not available outside of a `UObject`.

For the following use-cases, use the suggested pointer type instead of `TStrongObjectPtr`:

- For owning references inside a `UObject` class, use a `TObjectPtr` marked as a `UPROPERTY`.
- For non-owning references, use a `TWeakObjectPtr`. For asset references, use a `TWeakObjectPtr`.

Example use-cases for `TStrongObjectPtr` include:

- Strong reference to `UObject` in non-`UObject` owner.
