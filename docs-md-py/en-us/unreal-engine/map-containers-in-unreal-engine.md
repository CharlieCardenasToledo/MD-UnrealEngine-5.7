# TMap

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/map-containers-in-unreal-engine

> Application Version: 5.7

After [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/array-containers-in-unreal-engine), the most commonly used container in **Unreal Engine** is [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap?application_version=5.5). **TMap** is similar to [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/set-containers-in-unreal-engine) in that its structure is based on hashing keys. However, unlike [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TSet?application_version=5.5), TMap stores data as key-value pairs (`TPair<KeyType, ValueType>`), using keys only for storage and retrieval.

## Types of Maps in Unreal Engine

There are two types of map in Unreal Engine:

- [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap?application_version=5.5)
- [TMultiMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMultiMap?application_version=5.5)

### Overview of TMap

- In a TMap, key-value pairs are treated as the element type of the map as if each pair were an individual object. In this document, element means a key-value pair, while individual components are referred to as the element's key or the element's value.
- The element type is a `TPair<KeyType, ElementType>`, though it should be rare to need to refer to the TPair type directly.
- TMap keys are unique.
- Similar to TArray, TMap is a homogeneous container, meaning that all of its elements are strictly the same type.
- TMap is a value type, and supports the usual copy, assignment, and destructor operations, as well as strong ownership of its elements, which are destroyed when the map is destroyed. The key and value must also be value types.
- TMap is a hashing container, which means that the key type must support the [GetTypeHash](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/GenericPlatform/GetTypeHash?application_version=5.5) function and provide an `operator==` for comparing keys for equality

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "TMap and TMultimap (like many Unreal Engine containers) assume that the element type is trivially relocatable, meaning that elements can safely be moved from one location in memory to another by directly copying raw bytes.",
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

### Overview of TMultiMap

- Supports storing multiple, identical keys.
- When adding a new key-value pair to a TMap with a key that matches an existing pair, the new pair will replace the old one.
- In a TMultiMap, the container stores both the new pair and the old.

TMap can take an optional allocator to control the memory allocation behavior. However, unlike TArray, these are set allocators rather than the standard Unreal allocators like [FHeapAllocator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/FHeapAllocator?application_version=5.5) and [TInlineAllocator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/TraceLog/TInlineAllocator?application_version=5.5). **Set Allocators**, ([TSetAllocator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TSetAllocator?application_version=5.5)), define how many hash buckets the map should use and which standard UE allocators should be used for hash and element storage.

The final TMap template parameter is `KeyFuncs`, which tells the map how to retrieve the key from the element type, how to compare two keys for equality, and how to hash the key. These have defaults that return a reference to the key, then use `operator==` for equality, and call the non-member [GetTypeHash](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/GenericPlatform/GetTypeHash?application_version=5.5) function for hashing. If your key type supports these functions, you can use it as a map key without supplying a custom `KeyFuncs`.

Unlike TArray, the relative order of TMap elements in memory is not reliable or stable, and iterating over the elements is likely to return them in a different order from the order in which they were added. Elements are unlikely to be laid out contiguously in memory.

The base data structure of a map is a sparse array, which is an array that efficiently supports gaps between its elements. As elements are removed from the map, gaps in the sparse array will appear. Adding new elements to the array can then fill these gaps. However, even though TMap doesn't shuffle elements to fill gaps, pointers to map elements may still be invalidated, as the entire storage can be reallocated when it is full and new elements are added.

## Create and Fill a Map

The following code creates a **TMap**:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TMap&lt;int32, FString&gt; FruitMap;",
  "lines_of_code": 1,
  "id": 139581,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--351cc6b6bc2bd28c737a16714cd5bcb9a344beeee956bf1afc38f3edc13f756f",
  "settings": {
    "is_hidden": false
  }
}
```

`FruitMap` is now an empty TMap of strings that are identified by integer keys. We have specified neither an allocator nor a `KeyFuncs`, so the map performs standard heap allocation and compares the key of type `int32` using `operator==` and hashes the key using [GetTypeHash](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/GenericPlatform/GetTypeHash?application_version=5.5). No memory has been allocated at this point.

### Add

The standard way to populate a map is to call [Add](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Add?application_version=5.5) with a key and a value:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap.Add(5, TEXT(&quot;Banana&quot;));\nFruitMap.Add(2, TEXT(&quot;Grapefruit&quot;));\nFruitMap.Add(7, TEXT(&quot;Pineapple&quot;));\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Banana&quot;     },\n// \t{ Key: 2, Value: &quot;Grapefruit&quot; },\n// \t{ Key: 7, Value: &quot;Pineapple&quot;  }\n// ]",
  "lines_of_code": 8,
  "id": 139582,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--9b7caa4bdc315986a0443d0551739dae7c08e08d36d5419db083a89e07bf6cf3",
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
      "content": "While the elements are listed here in the order of insertion, there is no guarantee of their actual order in memory. For a new map, they are likely to be in order of insertion, but as more insertions and removals happen, it becomes increasingly unlikely that new elements will appear at the end.",
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

This is not a `TMultiMap`; therefore, the keys are guaranteed to be unique. The following is the result of attempting to add a duplicate key:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap.Add(2, TEXT(&quot;Pear&quot;));\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Banana&quot;    },\n// \t{ Key: 2, Value: &quot;Pear&quot;      },\n// \t{ Key: 7, Value: &quot;Pineapple&quot; }\n// ]",
  "lines_of_code": 6,
  "id": 139583,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--2a042e847fd147e7ffc52e4dd67d06ffcccef63d7ce81259d087091c0edcaaae",
  "settings": {
    "is_hidden": false
  }
}
```

The map still contains three elements, but the previous Grapefruit value with a key of 2 has been replaced with Pear.

The [Add](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Add?application_version=5.5) function can accept a key without a value. When this overloaded `Add` is called, the value will be default-constructed:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap.Add(4);\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Banana&quot;    },\n// \t{ Key: 2, Value: &quot;Pear&quot;      },\n// \t{ Key: 7, Value: &quot;Pineapple&quot; },\n// \t{ Key: 4, Value: &quot;&quot;          }\n// ]",
  "lines_of_code": 7,
  "id": 139584,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--b3776986e7067468e2b8c9bda8b77117e675dc15e724dc91b115e5dca9fd8dac",
  "settings": {
    "is_hidden": false
  }
}
```

### Emplace

Like TArray, we can use [Emplace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Emplace?application_version=5.5) instead of `Add` to avoid the creation of temporaries when inserting into the map:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap.Emplace(3, TEXT(&quot;Orange&quot;));\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Banana&quot;    },\n// \t{ Key: 2, Value: &quot;Pear&quot;      },\n// \t{ Key: 7, Value: &quot;Pineapple&quot; },\n// \t{ Key: 4, Value: &quot;&quot;          },\n// \t{ Key: 3, Value: &quot;Orange&quot;    }\n// ]",
  "lines_of_code": 8,
  "id": 139585,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--d77b83f00a2fb19ecaa12eece800b52348351ed59971c48622ce5569bddd89eb",
  "settings": {
    "is_hidden": false
  }
}
```

Here, the key and value are passed directly to their respective type constructors. While this isn't meaningful for the `int32` key, it does avoid the creation of a temporary `FString` for the value. Unlike TArray, it's only possible to emplace elements into a map with single-argument constructors.

### Append

You can merge two maps with the [Append](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap/Append?application_version=5.5) function, which moves all elements from the argument map into the calling object map:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TMap&lt;int32, FString&gt; FruitMap2;\nFruitMap2.Emplace(4, TEXT(&quot;Kiwi&quot;));\nFruitMap2.Emplace(9, TEXT(&quot;Melon&quot;));\nFruitMap2.Emplace(5, TEXT(&quot;Mango&quot;));\nFruitMap.Append(FruitMap2);\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Mango&quot;     },\n// \t{ Key: 2, Value: &quot;Pear&quot;      },\n// \t{ Key: 7, Value: &quot;Pineapple&quot; },\n// \t{ Key: 4, Value: &quot;Kiwi&quot;      },\n",
  "lines_of_code": 14,
  "id": 139586,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--fc9aec301358a3d3adb8acb7da61e0fddf0f6ba4326ac4ca336d6db025187836",
  "settings": {
    "is_hidden": false
  }
}
```

In the above example, the resulting map is equivalent to using `Add` or `Emplace` to add each element of `FruitMap2` individually, emptying `FruitMap2` when the process is complete. This means that any element from `FruitMap2` that shares its key with an element already in `FruitMap` replaces that element.

If you mark the TMap with the [UPROPERTY](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties) macro and one of the "editable" keywords (`EditAnywhere`, `EditDefaultsOnly`, or `EditInstanceOnly`), you can [add and edit elements in the Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-details-panel-in-unreal-engine).

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UPROPERTY(EditAnywhere, Category = MapsAndSets)\nTMap&lt;int32, FString&gt; FruitMap;",
  "lines_of_code": 2,
  "id": 139587,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--b6b4e14d5952518d466029fbfc7051184bb9d6e9fe2a1073133d11c0fb179526",
  "settings": {
    "is_hidden": false
  }
}
```

## Iterate

Iteration over TMaps is similar to TArrays. You can use the C++ ranged-for feature, remembering that the element type is a TPair:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "for (auto&amp; Elem : FruitMap)\n{\n\tFPlatformMisc::LocalPrint(\n\t\t*FString::Printf(\n\t\t\tTEXT(&quot;(%d, \\&quot;%s\\&quot;)\\n&quot;),\n\t\t\tElem.Key,\n\t\t\t*Elem.Value\n\t\t)\n\t);\n}\n",
  "lines_of_code": 18,
  "id": 139588,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--49947fb815ef137c441b468b6936527ee00bf98b4e1390541dbb89a22bd4f480",
  "settings": {
    "is_hidden": false
  }
}
```

You can create iterators with the [CreateIterator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/CreateIterator?application_version=5.5) and [CreateConstIterator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/CreateConstIterator?application_version=5.5) functions.

| Function | Description |
| --- | --- |
| `CreateIterator` | Return an iterator with read-write access. |
| `CreateConstIterator` | Returns a read-only iterator. |

In either case, you can use the `Key` and `Value` functions of these iterators to examine the elements. Printing the contents of our example `FruitMap` using iterators would look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "for (auto It = FruitMap.CreateConstIterator(); It; ++It)\n{\n\tFPlatformMisc::LocalPrint(\n\t\t*FString::Printf(\n\t\t\tTEXT(&quot;(%d, \\&quot;%s\\&quot;)\\n&quot;),\n\t\t\tIt.Key(),   // same as It-&gt;Key\n\t\t\t*It.Value() // same as *It-&gt;Value\n\t\t)\n\t);\n}",
  "lines_of_code": 10,
  "id": 139589,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1ODksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--fcd4268c70f1a07beaef73d1b9418deb15ffe1e10dacf02cd7a329e7a3c418ad",
  "settings": {
    "is_hidden": false
  }
}
```

## Get Value

If you know that your map contains a certain key, you can look up the corresponding value with `operator[]`, using the key as the index. Doing this with a non-const map returns a non-const reference, while a const map returns a const reference.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You should always check that the map contains the key before using <code>operator[]</code>. If the map does not contain the key, it will assert.",
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
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString Val7 = FruitMap[7];\n// Val7 == &quot;Pineapple&quot;\nFString Val8 = FruitMap[8];\n// Assert!",
  "lines_of_code": 4,
  "id": 139590,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--2aaf72719da8928322544de7479176618e8f7504fa1b6a919258ff0254c2885f",
  "settings": {
    "is_hidden": false
  }
}
```

## Query

To determine how many elements are currently in a TMap, call the [Num](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Num?application_version=5.5) function:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 Count = FruitMap.Num();\n// Count == 6",
  "lines_of_code": 2,
  "id": 139591,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--eb7d073a6320e5a61942a540da09342cb269d29ed2626fb9c4ff117efe2f66e7",
  "settings": {
    "is_hidden": false
  }
}
```

To determine whether or not a map contains a specific key, call the `Contains` function:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "bool bHas7 = FruitMap.Contains(7);\nbool bHas8 = FruitMap.Contains(8);\n// bHas7 == true\n// bHas8 == false",
  "lines_of_code": 4,
  "id": 139592,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--b0886bdd31ab783578b3709797e61ed37c568efd87bc93ce70f1e87c43f4701a",
  "settings": {
    "is_hidden": false
  }
}
```

If you are uncertain whether or not your map contains a key, you could check using the [Contains](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Contains?application_version=5.5) function, and then use `operator[]`. However, this is suboptimal, since a successful retrieval involves two lookups on the same key.

The [Find](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Find?application_version=5.5) function combines these behaviors with a single lookup. `Find` returns a pointer to the value of the element if the map contains the key, or a null pointer if it does not. Calling `Find` on a const map returns a const pointer.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString* Ptr7 = FruitMap.Find(7);\nFString* Ptr8 = FruitMap.Find(8);\n// *Ptr7 == &quot;Pineapple&quot;\n//  Ptr8 == nullptr",
  "lines_of_code": 4,
  "id": 139593,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--2588bcad42df473d7996af0be88bc900aef256a4bf65f8535ebb584c733c38aa",
  "settings": {
    "is_hidden": false
  }
}
```

Alternatively, to ensure that you receive a valid result from your query, you can use [FindOrAdd](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/FindOrAdd?application_version=5.5) or [FindRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/FindRef?application_version=5.5):

| Function | Description |
| --- | --- |
| `FindOrAdd` | Return a reference to the value associated with the key you provide. If the key is not in the map, `FindOrAdd` returns a newly-created element, with your key and the default-constructed value, that it will add to the map. |
| `FindRef` | Despite its name, returns a copy of the value associated with your key, or a default-constructed value if your key is not found in the map. `FindRef` does not create a new element, and thus is available for use with both const and non-const maps. |

Because `FindOrAdd` and `FindRef` succeed even when the key isn't found in the map, you can safely call them without the usual safety procedures like checking `Contains` in advance, or null-checking the return value.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString&amp; Ref7 = FruitMap.FindOrAdd(7);\n// Ref7     == &quot;Pineapple&quot;\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Mango&quot;     },\n// \t{ Key: 2, Value: &quot;Pear&quot;      },\n// \t{ Key: 7, Value: &quot;Pineapple&quot; },\n// \t{ Key: 4, Value: &quot;Kiwi&quot;      },\n// \t{ Key: 3, Value: &quot;Orange&quot;    },\n// \t{ Key: 9, Value: &quot;Melon&quot;     }\n// ]\n",
  "lines_of_code": 36,
  "id": 139594,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--0ba50339b3524d17e5a210e9f42405c3bc005369bebb7557b8c18bf573aadfb0",
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
      "content": "Because <code>FindOrAdd</code> can add new entries to the map, as it does when initializing <code>Ref8</code> in our example, previously-obtained pointers or references could become invalid. This is a result of the addition operation allocating memory and moving existing data if the map's backend storage needs to expand to contain the new element. In the example above, <code>Ref7</code> may be invalidated after <code>Ref8</code> after the call to <code>FindOrAdd(8)</code>.",
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

The [FindKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/FindKey?application_version=5.5) function performs a reverse lookup, meaning that a supplied value is matched to a key, and returns a pointer to the first key that's paired to the provided value. Searching for a value that isn't present in the map returns a null pointer.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "const int32* KeyMangoPtr   = FruitMap.FindKey(TEXT(&quot;Mango&quot;));\nconst int32* KeyKumquatPtr = FruitMap.FindKey(TEXT(&quot;Kumquat&quot;));\n// *KeyMangoPtr   == 5\n//  KeyKumquatPtr == nullptr",
  "lines_of_code": 4,
  "id": 139595,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--0daa3b83c14e2ddb0221754594e24b4a536c9ad83e3c5cb10240087e4f69b3b5",
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
      "content": "Lookups by value are slower (linear time) than lookups by key. This is because the map is hashed by key, not by value. In addition, if a map has multiple keys with the same value, <code>FindKey</code> may return any of them.",
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

The [GenerateKeyArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/GenerateKeyArray?application_version=5.5) and [GenerateValueArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/GenerateValueArray?application_version=5.5) functions populate a [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/TraceLog/TArray?application_version=5.5) with a copy of all the keys and values respectively. In both cases, the array being passed is emptied before population, so the resulting number of elements will always equal the number of elements in the map.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;int32&gt;   FruitKeys;\nTArray&lt;FString&gt; FruitValues;\nFruitKeys.Add(999);\nFruitKeys.Add(123);\nFruitMap.GenerateKeyArray  (FruitKeys);\nFruitMap.GenerateValueArray(FruitValues);\n// FruitKeys   == [ 5,2,7,4,3,9,8 ]\n// FruitValues == [ &quot;Mango&quot;,&quot;Pear&quot;,&quot;Pineapple&quot;,&quot;Kiwi&quot;,&quot;Orange&quot;,\n//                  &quot;Melon&quot;,&quot;&quot; ]",
  "lines_of_code": 9,
  "id": 139596,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--acae129e18cfd1c1a7fdaa966d61b95744e50ed922935c6b49752c5a266f7dc1",
  "settings": {
    "is_hidden": false
  }
}
```

## Remove

You can remove elements from a map using the [Remove](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Remove?application_version=5.5) function and providing the key of the element to remove. The return value is the number of elements that were removed, and can be zero if the map didn't contain any elements matching the key.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap.Remove(8);\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Mango&quot;     },\n// \t{ Key: 2, Value: &quot;Pear&quot;      },\n// \t{ Key: 7, Value: &quot;Pineapple&quot; },\n// \t{ Key: 4, Value: &quot;Kiwi&quot;      },\n// \t{ Key: 3, Value: &quot;Orange&quot;    },\n// \t{ Key: 9, Value: &quot;Melon&quot;     }\n// ]",
  "lines_of_code": 9,
  "id": 139597,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--911324a8b9bbe10816355db9b3fabfca559ce4b455752a46903c67c14e214082",
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
      "content": "Removing elements can leave holes in the data structure, which you can see when visualizing the map in Visual Studio's watch window, but they have been omitted here for clarity.",
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

The `FindAndRemoveChecked` function can be used to remove an element from the map and return its value. The "checked" part of the name indicates that the map calls check if the key does not exist.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString Removed7 = FruitMap.FindAndRemoveChecked(7);\n// Removed7 == &quot;Pineapple&quot;\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Mango&quot;  },\n// \t{ Key: 2, Value: &quot;Pear&quot;   },\n// \t{ Key: 4, Value: &quot;Kiwi&quot;   },\n// \t{ Key: 3, Value: &quot;Orange&quot; },\n// \t{ Key: 9, Value: &quot;Melon&quot;  }\n// ]\n\n",
  "lines_of_code": 12,
  "id": 139598,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--57b8664ce506ee38fd3adc455cf5127701157f20a8206656f3d9dbdc7e826d2e",
  "settings": {
    "is_hidden": false
  }
}
```

The [RemoveAndCopyValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap/RemoveAndCopyValue?application_version=5.5) function is similar to `Remove`, but copies the value of the removed element out to a reference parameter. If the key you specified is not present in the map, the output parameter will be unchanged and the function returns `false`.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString Removed;\nbool bFound2 = FruitMap.RemoveAndCopyValue(2, Removed);\n// bFound2  == true\n// Removed  == &quot;Pear&quot;\n// FruitMap == [\n// \t{ Key: 5, Value: &quot;Mango&quot;  },\n// \t{ Key: 4, Value: &quot;Kiwi&quot;   },\n// \t{ Key: 3, Value: &quot;Orange&quot; },\n// \t{ Key: 9, Value: &quot;Melon&quot;  }\n// ]\n",
  "lines_of_code": 20,
  "id": 139599,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk1OTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--5d70ab9b106842c877132e4031bb05a49345c38de7452130091857a5a6c67b83",
  "settings": {
    "is_hidden": false
  }
}
```

Finally, you can remove all elements from the map with the [Empty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Empty?application_version=5.5) or [Reset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Reset?application_version=5.5) functions.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TMap&lt;int32, FString&gt; FruitMapCopy = FruitMap;\n// FruitMapCopy == [\n// \t{ Key: 5, Value: &quot;Mango&quot;  },\n// \t{ Key: 4, Value: &quot;Kiwi&quot;   },\n// \t{ Key: 3, Value: &quot;Orange&quot; },\n// \t{ Key: 9, Value: &quot;Melon&quot;  }\n// ]\n\nFruitMapCopy.Empty();\t\t// You can also use Reset() here.\n// FruitMapCopy == []",
  "lines_of_code": 10,
  "id": 139600,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk2MDAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--d033cbde691723f9b3e8c41c79a57695ca73c257057e16cdfc4559bd05776f9f",
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
      "content": "<code>Empty</code> can take a parameter to indicate how much slack to leave in the map, while <code>Reset</code> always leaves as much slack as possible.",
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

## Sort

You can sort a TMap by key or by value. After sorting, iteration over the map presents the elements in sorted order, but this behavior is only guaranteed until the next time you modify the map. Sorting is unstable, so equivalent elements in a `TMultiMap` may appear in any order.

You can sort by key or by value using the [KeySort](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TSortableMapBase/KeySort?application_version=5.5) or [ValueSort](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TSortableMapBase/ValueSort?application_version=5.5) functions, respectively. Both functions take a binary predicate which specifies the sort order.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap.KeySort([](int32 A, int32 B) {\n\treturn A &gt; B; // sort keys in reverse\n});\n// FruitMap == [\n// \t{ Key: 9, Value: &quot;Melon&quot;  },\n// \t{ Key: 5, Value: &quot;Mango&quot;  },\n// \t{ Key: 4, Value: &quot;Kiwi&quot;   },\n// \t{ Key: 3, Value: &quot;Orange&quot; }\n// ]\n\n",
  "lines_of_code": 19,
  "id": 139601,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk2MDEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--3d6f2d6ce509b045c6299c8b21cb774ebee1bec381a80904e4e1b0894325e57d",
  "settings": {
    "is_hidden": false
  }
}
```

## Operators

Like TArray, TMap is a regular value type and can be copied with the standard copy constructor or assignment operator. Maps strictly own their elements, so copying a map is deep; the new map will have its own copy of the elements.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TMap&lt;int32, FString&gt; NewMap = FruitMap;\nNewMap[5] = &quot;Apple&quot;;\nNewMap.Remove(3);\n// FruitMap == [\n// \t{ Key: 4, Value: &quot;Kiwi&quot;   },\n// \t{ Key: 5, Value: &quot;Mango&quot;  },\n// \t{ Key: 9, Value: &quot;Melon&quot;  },\n// \t{ Key: 3, Value: &quot;Orange&quot; }\n// ]\n// NewMap == [\n",
  "lines_of_code": 14,
  "id": 139602,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk2MDIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--1c7f2c4cfb523e2869f63246b174015abeee32c1b57681420d8cbfc6cb45ce51",
  "settings": {
    "is_hidden": false
  }
}
```

TMap supports move semantics, which can be invoked using the `MoveTemp`function. After a move, the source map is guaranteed to be empty:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap = MoveTemp(NewMap);\n// FruitMap == [\n// \t{ Key: 4, Value: &quot;Kiwi&quot;  },\n// \t{ Key: 5, Value: &quot;Apple&quot; },\n// \t{ Key: 9, Value: &quot;Melon&quot; }\n// ]\n// NewMap == []",
  "lines_of_code": 7,
  "id": 139603,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk2MDMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--e263bed265f862c786916ab9a5047ac11c13c7540ba68c51f1c625d414ff556c",
  "settings": {
    "is_hidden": false
  }
}
```

## Slack

Slack is allocated memory that doesn't contain an element. You can allocate memory without adding elements by calling [Reserve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Reserve?application_version=5.5), and you can remove elements without deallocating the memory they were using by calling [Reset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Reset?application_version=5.5) or by calling [Empty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Empty?application_version=5.5) with a non-zero slack parameter. Slack optimizes the process of adding new elements to the map by using pre-allocated memory instead of having to allocate new memory. It can also help with element removal since the system does not need to deallocate memory. This is especially efficient when you are emptying a map that you expect to repopulate immediately with the same number of elements or fewer.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "TMap does not provide a way of checking how many elements are preallocated the way the <a><code>Max</code></a> function in TArray does.",
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

In the code below, the `Reserve` function allocates space for the map to contain up to ten elements:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap.Reserve(10);\nfor (int32 i = 0; i &lt; 10; ++i)\n{\n\tFruitMap.Add(i, FString::Printf(TEXT(&quot;Fruit%d&quot;), i));\n}\n// FruitMap == [\n// \t{ Key: 9, Value: &quot;Fruit9&quot; },\n// \t{ Key: 8, Value: &quot;Fruit8&quot; },\n// \t...\n// \t{ Key: 1, Value: &quot;Fruit1&quot; },\n",
  "lines_of_code": 12,
  "id": 139604,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk2MDQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--27da1e30737caf743b9ae446c801c79ebd3fda3de42b3b10de99b937b6d841f4",
  "settings": {
    "is_hidden": false
  }
}
```

To remove all slack from a TMap, use the `Collapse` and [Shrink](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Shrink?application_version=5.5) functions. `Shrink` removes all slack from the end of the container, but leaves any empty elements in the middle or at the start.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "for (int32 i = 0; i &lt; 10; i += 2)\n{\n\tFruitMap.Remove(i);\n}\n// FruitMap == [\n// \t{ Key: 9, Value: &quot;Fruit9&quot; },\n// \t&lt;invalid&gt;,\n// \t{ Key: 7, Value: &quot;Fruit7&quot; },\n// \t&lt;invalid&gt;,\n// \t{ Key: 5, Value: &quot;Fruit5&quot; },\n",
  "lines_of_code": 29,
  "id": 139605,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk2MDUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--207631c0c9a8c1b9fd3900305b87d72dc92302b33703e45b0f352c9687027b9d",
  "settings": {
    "is_hidden": false
  }
}
```

`Shrink` only removed one invalid element in the code above because there was only one empty element at the end. To remove all slack, use the [Compact](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Compact?application_version=5.5) function first so that the empty spaces will be grouped together in preparation for `Shrink`.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitMap.Compact();\n// FruitMap == [\n// \t{ Key: 9, Value: &quot;Fruit9&quot; },\n// \t{ Key: 7, Value: &quot;Fruit7&quot; },\n// \t{ Key: 5, Value: &quot;Fruit5&quot; },\n// \t{ Key: 3, Value: &quot;Fruit3&quot; },\n// \t{ Key: 1, Value: &quot;Fruit1&quot; },\n// \t&lt;invalid&gt;,\n// \t&lt;invalid&gt;,\n// \t&lt;invalid&gt;,\n",
  "lines_of_code": 21,
  "id": 139606,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk2MDYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--e16c1a33cef0c133f0adf40a28cb979eefb87973808e77736a91497c486a8610",
  "settings": {
    "is_hidden": false
  }
}
```

## KeyFuncs

As long as a type has an `operator==` and a non-member [GetTypeHash](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/GenericPlatform/GetTypeHash?application_version=5.5) overload, you can use it as a key type for a TMap without any changes. However, you may want to use types as keys without overloading those functions. In these cases, you can provide your own custom [KeyFuncs](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/DefaultKeyFuncs?application_version=5.5). To create KeyFuncs for your key type, you must define two typedefs and three static functions, as follows:

| Type Definition | Description |
| --- | --- |
| `KeyInitType` | Type used to pass keys around. |
| `ElementInitType` | Type used to pass elements around. |

| Function | Description |
| --- | --- |
| `KeyInitType GetSetKey(ElementInitType Element)` | Returns the key of an element. |
| `bool Matches(KeyInitType A, KeyInitType B)` | Returns `true` if `A` and `B` are equivalent, `false` otherwise. |
| `uint32 GetKeyHash(KeyInitType Key)` | Returns the hash value of `Key`. |

`KeyInitType` and `ElementInitType` are typedefs to the normal passing convention of the key type and element type. Usually, these will be a value for trivial types and a const reference for non-trivial types. Remember that the element type of a map is a `TPair`.

The following code snippet is an example of a custom KeyFuncs:

MyCustomKeyFuncs.cpp

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "struct FMyStruct\n{\n\t// String which identifies our key\n\tFString UniqueID;\n\n\t// Some state which doesn&#39;t affect struct identity\n\tfloat SomeFloat;\n\n\texplicit FMyStruct(float InFloat)\n\t\t: UniqueID (FGuid::NewGuid().ToString())\n",
  "lines_of_code": 49,
  "id": 139607,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzk2MDcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowNDo0MyswMDowMCJ9--0db02ab8b6bda14b76f291ad9536fbe37356d9ff5a37136a1bfc8f7f85d3fc60",
  "settings": {
    "is_hidden": false
  }
}
```

`FMyStruct` features a unique identifier, as well as some other data that does not contribute to its identity. `GetTypeHash` and `operator==` would be inappropriate here, because `operator==` should not ignore any of the type's data for general-purpose usage, but would simultaneously need to do so in order to be consistent with the behavior of `GetTypeHash`, which only looks at the *UniqueID* field.

To create a custom `KeyFuncs` for `FMyStruct`, follow these steps:

1. Inherit from `BaseKeyFuncs`, as it defines some helpful types, including `KeyInitType` and `ElementInitType`. `BaseKeyFuncs` takes two template parameters: The element type of the map. As with all maps, the element type is a `TPair`, taking `FMyStruct` as its `KeyType` and the template parameter of `TMyStructMapKeyFuncs` as its `ValueType`. The replacement `KeyFuncs` is a template, so that you can specify `ValueType` on a per-map basis, rather than needing to define a new `KeyFuncs` every time you want to create a TMap keyed on `FMyStruct`. The type of our key. The second `BaseKeyFuncs` argument is the type of the key, not to be confused with the `KeyType` from TPair, the Key field of the element stores. Since this map should use `UniqueID` (from `FMyStruct`) as its key, `FString` is used here.
2. Define the three required `KeyFuncs` static functions. The first is [GetSetKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/DefaultKeyFuncs/GetSetKey?application_version=5.5), which returns the key for a given element type. Our element type is `TPair`, and our key is `UniqueID`, so the function can simply return `UniqueID` directly. The second static function is [Matches](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/DefaultKeyFuncs/Matches?application_version=5.5), which takes the keys of two elements retrieved by `GetSetKey`, and compares them to see if they are equivalent. For `FString`, the standard equivalence test (`operator==`) is case-insensitive; to replace this with a case-sensitive search, use the `Compare()` function with the appropriate case-comparison option. The third static function is `GetKeyHash`, which takes an extracted key and returns a hashed value for it. Because the `Matches` function is case-sensitive, `GetKeyHash` must also be. A case-sensitive [FCrc](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Misc/FCrc?application_version=5.5) function calculates the hash value from the key string.
3. Now that the structure supports the behaviors that TMap requires, you can create instances of it.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When providing your own KeyFuncs, be aware that <code>TMap</code> assumes that two items that compare as equal with <a data-document-id=\"3532485\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/DefaultKeyFuncs/Matches?application_version=5.5\">Matches</a> also return the same value from <code>GetKeyHash</code>. In addition, modifying the key of an existing map element in a way that changes the results from either of these functions is considered an undefined behavior, as this invalidates the map's internal hash. These rules also apply to overloads of <code>operator==</code> and <code>GetKeyHash</code> when using the default <code>KeyFuncs</code>.",
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

## Miscellaneous

The `CountBytes` and `GetAllocatedSize` functions estimate how much memory the internal array is currently utilizing. `CountBytes` takes an `FArchive` parameter, while `GetAllocatedSize` does not. These functions are typically used for stats reporting.

The [Dump](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Dump?application_version=5.5) function takes an `FOutputDevice` and writes out some implementation information about the contents of the map. This function is usually used for debugging.
