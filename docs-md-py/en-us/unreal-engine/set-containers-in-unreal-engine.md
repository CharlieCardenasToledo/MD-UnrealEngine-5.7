# TSet

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/set-containers-in-unreal-engine

> Application Version: 5.7

`TSet` is similar to `TMap` and `TMultiMap`, but with an important difference: Rather than associating data values with independent keys, a `TSet` uses the data value itself as the key, through an overridable function that evaluates the element. `TSet` is very fast (constant time) for adding, finding, and removing elements. By default, `TSet` does not support duplicate keys, but this behavior can be activated with a template parameter.

## TSet

`TSet` is a fast container class to store unique elements in a context where order is irrelevant. For most use cases, just one parameter — the element type — is needed. However, `TSet` can be set up with different template parameters to change its behavior and make it more versatile. You can specify a derived struct based on `DefaultKeyFuncs` to provide hashing functionality, as well as permit multiple keys with the same value to exist in the set. Finally, like the other container classes, you can provide a custom memory allocator for its data storage.

Like `TArray`, `TSet` is a homogeneous container, meaning that all of its elements are strictly the same type. `TSet` is also a value type, and supports the usual copy, assignment, and destructor operations, as well as strong ownership of its elements, which are destroyed when the `TSet` is. The key type must also be a value type.

`TSet` uses hashes, which means that the `KeyFuncs` template parameter, if provided, tells the set how to determine the key from an element, how to compare two keys for equality, how to hash the key, and whether or not to permit duplicate keys. These have defaults that will return a reference to the key, use `operator==` for equality, and the non-member `GetTypeHash` function for hashing. By default, the set will not permit duplicate keys. If your key type supports these functions, it is usable as a set key without the need to provide a custom `KeyFuncs`. To write a custom `KeyFuncs`, extend the `DefaultKeyFuncs` struct.

Finally, `TSet` can take an optional allocator to control memory allocation behavior. Standard Unreal Engine 4 (UE4) allocators (such as `FHeapAllocator` and `TInlineAllocator`) cannot be used as allocators for `TSet`. Instead, `TSet` uses set allocators, which define how many hash buckets the set should use, and which standard UE4 allocators to use for element storage. See `TSetAllocator` for more information.

Unlike `TArray`, the relative order of `TSet` elements in memory is not reliable or stable, and iterating over the elements is likely to return them in a different order from the order in which they were added. Elements are also unlikely to be laid out contiguously in memory. The backing data structure of a set is a sparse array, which is an array that efficiently supports gaps between its elements. As elements are removed from the set, gaps in the sparse array will appear. Adding new elements into the array can then fill these gaps. However, even though `TSet` doesn't shuffle elements to fill gaps, pointers to set elements may still be invalidated, as the entire storage can be reallocated when it is full and new elements are added.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "TSet (like many Unreal Engine containers) assumes that the element type is trivially relocatable, meaning that elements can safely be moved from one location in memory to another by directly copying raw bytes.",
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

## Creating and Filling a Set

You can create a `TSet` like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TSet&lt;FString&gt; FruitSet;",
  "lines_of_code": 1,
  "id": 100350,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--10ad9578edb5f44deed4d699759f35dec23d00aa13ba9ca5f477686fada4f1a9",
  "settings": {
    "is_hidden": false
  }
}
```

This creates an empty `TSet` that will hold `FString` data. The `TSet` will compare elements directly with `operator==`, hash them using `GetTypeHash`, and use the standard heap allocator. No memory has been allocated at this point.

The standard way to populate a set is to use the `Add` function and provide a key (element):

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitSet.Add(TEXT(&quot;Banana&quot;));\n\tFruitSet.Add(TEXT(&quot;Grapefruit&quot;));\n\tFruitSet.Add(TEXT(&quot;Pineapple&quot;));\n\t// FruitSet == [ &quot;Banana&quot;, &quot;Grapefruit&quot;, &quot;Pineapple&quot; ]",
  "lines_of_code": 4,
  "id": 100351,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--41f6cbeb308a0352cb797c87e95c4afd8f149c5296be686d3b97f71237c3e196",
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
      "content": "While the elements are listed here in the order of insertion, there is no guarantee as to their actual order in memory. For a new set, they are likely to be in order of insertion, but as more insertions and removals happen, it becomes increasingly unlikely that new elements will appear at the end.",
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

Since this set uses the default allocator, keys are guaranteed to be unique. The following is the result of attempting to add a duplicate key:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitSet.Add(TEXT(&quot;Pear&quot;));\n\tFruitSet.Add(TEXT(&quot;Banana&quot;));\n\t// FruitSet == [ &quot;Banana&quot;, &quot;Grapefruit&quot;, &quot;Pineapple&quot;, &quot;Pear&quot; ]\n\t// Note: Only one banana entry.",
  "lines_of_code": 4,
  "id": 100352,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--1b18830add4cf16d725e5ce5d82cb497f1eb29447a2215b54cf3bc9c31372b4c",
  "settings": {
    "is_hidden": false
  }
}
```

The set now contains four elements. "Pear" brought the count up to four from three, but the new "Banana" didn't change the number of elements in the set because it replaced the old "Banana" entry.

Like `TArray`, we can also use `Emplace` instead of `Add` to avoid the creation of temporaries when inserting into the set:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitSet.Emplace(TEXT(&quot;Orange&quot;));\n\t// FruitSet == [ &quot;Banana&quot;, &quot;Grapefruit&quot;, &quot;Pineapple&quot;, &quot;Pear&quot;, &quot;Orange&quot; ]",
  "lines_of_code": 2,
  "id": 100353,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--bd38adf9b8018c2369611f2d4027c6fa9a41a29978a731c0dddcc083477d47e7",
  "settings": {
    "is_hidden": false
  }
}
```

Here, the argument is passed directly to the constructor of the key type. This avoids the creation of a temporary `FString` for the value. Unlike `TArray`, it's only possible to emplace elements into a set with single-argument constructors.

It's also possible to insert all the elements from another set by using the `Append` function to merge them:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TSet&lt;FString&gt; FruitSet2;\n\tFruitSet2.Emplace(TEXT(&quot;Kiwi&quot;));\n\tFruitSet2.Emplace(TEXT(&quot;Melon&quot;));\n\tFruitSet2.Emplace(TEXT(&quot;Mango&quot;));\n\tFruitSet2.Emplace(TEXT(&quot;Orange&quot;));\n\tFruitSet.Append(FruitSet2);\n\t// FruitSet == [ &quot;Banana&quot;, &quot;Grapefruit&quot;, &quot;Pineapple&quot;, &quot;Pear&quot;, &quot;Orange&quot;, &quot;Kiwi&quot;, &quot;Melon&quot;, &quot;Mango&quot; ]",
  "lines_of_code": 7,
  "id": 100354,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--fffd5e41180720d942c67d1bdea09d1ea55b1f62309bc0bb1377cc7af14cbb6c",
  "settings": {
    "is_hidden": false
  }
}
```

In the example above, the resulting set is equivalent to using `Add` or `Emplace` to add the elements individually. Duplicate keys from the source set will replace their counterparts in the target.

### Editing UPROPERTY TSets

If you mark the `TSet` with the `UPROPERTY` macro and one of the "editable" keywords (`EditAnywhere`, `EditDefaultsOnly`, or `EditInstanceOnly`), you can [add and edit elements in Unreal Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-details-panel-in-unreal-engine).

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UPROPERTY(Category = SetExample, EditAnywhere)\n\tTSet&lt;FString&gt; FruitSet;",
  "lines_of_code": 2,
  "id": 100355,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--881e39ac824849defe8693bd58e0bcc318ecf8c0991bfd908b3728c717a8c1b8",
  "settings": {
    "is_hidden": false
  }
}
```

## Iteration

Iteration over `TSets` is similar to `TArrays`. You can use the C++ ranged-for feature:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "for (auto&amp; Elem : FruitSet)\n\t{\n\t\tFPlatformMisc::LocalPrint(\n\t\t\t*FString::Printf(\n\t\t\t\tTEXT(&quot; \\&quot;%s\\&quot;\\n&quot;),\n\t\t\t\t*Elem\n\t\t\t)\n\t\t);\n\t}\n\t// Output:\n",
  "lines_of_code": 18,
  "id": 100356,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--5e32cba18e1e6680aad67e116b9920d4b2748f720b27760a1a3449a11bb30df4",
  "settings": {
    "is_hidden": false
  }
}
```

You can also create iterators with the `CreateIterator` and `CreateConstIterators` functions. `CreateIterator` will return an iterator with read-write access, while `CreateConstIterator` returns a read-only iterator. In either case, you can use the `Key` and `Value` functions of these iterators to examine the elements. Printing the contents of our example "fruit" set using iterators would look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "for (auto It = FruitSet.CreateConstIterator(); It; ++It)\n\t{\n\t\tFPlatformMisc::LocalPrint(\n\t\t\t*FString::Printf(\n\t\t\t\tTEXT(&quot;(%s)\\n&quot;),\n\t\t\t\t*It\n\t\t\t)\n\t\t);\n\t}",
  "lines_of_code": 9,
  "id": 100357,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--a800b3fd7be71600b7edc00f325cd80c2004eeb17d767d76965da34197737d59",
  "settings": {
    "is_hidden": false
  }
}
```

## Queries

To find out how many elements are currently in the set, call the `Num` function.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 Count = FruitSet.Num();\n\t// Count == 8",
  "lines_of_code": 2,
  "id": 100358,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--0038e1a66e9f2559528574a502ceee9374b2b09be196e087a4fe2f0da3638c18",
  "settings": {
    "is_hidden": false
  }
}
```

In order to determine whether or not a set contains a specific element, call the `Contains` function, as follows:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "bool bHasBanana = FruitSet.Contains(TEXT(&quot;Banana&quot;));\n\tbool bHasLemon = FruitSet.Contains(TEXT(&quot;Lemon&quot;));\n\t// bHasBanana == true\n\t// bHasLemon == false",
  "lines_of_code": 4,
  "id": 100359,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--de79bae8f9895f7ec9df300988811ee15b30f850184559b80b5cca78acd125d9",
  "settings": {
    "is_hidden": false
  }
}
```

You can use the `FSetElementId` struct to find the index of a key within the set. You can then use that index with `operator[]` to retrieve the element. Calling `operator[]` on a non-const set will return a non-const reference, and calling it on a const set will return a const reference.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FSetElementId BananaIndex = FruitSet.Index(TEXT(&quot;Banana&quot;));\n\t// BananaIndex is a value between 0 and (FruitSet.Num() - 1)\n\tFPlatformMisc::LocalPrint(\n\t\t*FString::Printf(\n\t\t\tTEXT(&quot; \\&quot;%s\\&quot;\\n&quot;),\n\t\t\t*FruitSet[BananaIndex]\n\t\t)\n\t);\n\t// Prints &quot;Banana&quot;\n\n",
  "lines_of_code": 18,
  "id": 100360,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--73b08a4a60202274b8287523800157495a36a41632e864b58a62fc315e663487",
  "settings": {
    "is_hidden": false
  }
}
```

If you are unsure whether or not your set contains a key, you could check with the `Contains` function, and then use `operator[]`. However, this is suboptimal, since a successful retrieval involves two lookups on the same key. The `Find` function combines these behaviors with a single lookup. `Find` returns a pointer to the value of the element if the set contains the key, or a null pointer if it does not. Calling `Find` on a const set will cause the pointer it returns to be const as well.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString* PtrBanana = FruitSet.Find(TEXT(&quot;Banana&quot;));\n\tFString* PtrLemon = FruitSet.Find(TEXT(&quot;Lemon&quot;));\n\t// *PtrBanana == &quot;Banana&quot;\n\t//  PtrLemon == nullptr",
  "lines_of_code": 4,
  "id": 100361,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--df74909560b622480a628684884a65a1d9ef4786350c23bb6405f8f86af8d880",
  "settings": {
    "is_hidden": false
  }
}
```

The `Array` function returns a `TArray` populated with a copy of all the elements in the `TSet`. The array that you pass in will be emptied at the beginning of the operation, so the resulting number of elements will always equal the number of elements in the set:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;FString&gt; FruitArray = FruitSet.Array();\n\t// FruitArray == [ &quot;Banana&quot;,&quot;Grapefruit&quot;,&quot;Pineapple&quot;,&quot;Pear&quot;,&quot;Orange&quot;,&quot;Kiwi&quot;,&quot;Melon&quot;,&quot;Mango&quot; ] (order may vary)",
  "lines_of_code": 2,
  "id": 100362,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--92a29f2595e1230f896f4a61be869cc06c20f78c5b69f3a985b3d436edfb47d9",
  "settings": {
    "is_hidden": false
  }
}
```

## Removal

Elements can be removed by index with the `Remove` function, though this is recommended only for use while iterating through the elements. The Remove function returns the number of elements removed, and will be 0 if the key provided was not contained in the set. If a `TSet` supports duplicate keys, `Remove` will remove all matching elements.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitSet.Remove(0);\n\t// FruitSet == [ &quot;Grapefruit&quot;,&quot;Pineapple&quot;,&quot;Pear&quot;,&quot;Orange&quot;,&quot;Kiwi&quot;,&quot;Melon&quot;,&quot;Mango&quot; ]",
  "lines_of_code": 2,
  "id": 100363,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--07e6188f41a953c0198540247a290807da6348e221dd1f724d14f22c5154d62e",
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
      "content": "Removing elements can leave holes in the data structure, which you can see when visualizing the set in Visual Studio's watch window, but they have been omitted here for clarity.",
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
  "code_preview": "int32 RemovedAmountPineapple = FruitSet.Remove(TEXT(&quot;Pineapple&quot;));\n\t// RemovedAmountPineapple == 1\n\t// FruitSet == [ &quot;Grapefruit&quot;,&quot;Pear&quot;,&quot;Orange&quot;,&quot;Kiwi&quot;,&quot;Melon&quot;,&quot;Mango&quot; ]\n\tFString RemovedAmountLemon = FruitSet.Remove(TEXT(&quot;Lemon&quot;));\n\t// RemovedAmountLemon == 0",
  "lines_of_code": 5,
  "id": 100364,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--3077ea94db3eaebd2c517956cd603996f57bdac7544510c787533ae972c095c8",
  "settings": {
    "is_hidden": false
  }
}
```

Finally, you can remove all elements from the set with the `Empty` or `Reset` functions.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TSet&lt;FString&gt; FruitSetCopy = FruitSet;\n\t// FruitSetCopy == [ &quot;Grapefruit&quot;,&quot;Pear&quot;,&quot;Orange&quot;,&quot;Kiwi&quot;,&quot;Melon&quot;,&quot;Mango&quot; ]\n\n\tFruitSetCopy.Empty();\n\t// FruitSetCopy == []",
  "lines_of_code": 5,
  "id": 100365,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--2bdfabbb2920147635f705acbe9d95c711cbc373f203df28cb5f7158ed91d3f2",
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
      "content": "<code>Empty</code> and <code>Reset</code> are similar, but <code>Empty</code> can take a parameter to indicate how much slack to leave in the set, while <code>Reset</code> always leaves as much slack as possible.",
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

## Sorting

A `TSet` can be sorted. After sorting, iteration over the set will present the elements in sorted order, but this behavior is only guaranteed until the next time you modify the set. Sorting is unstable, so equivalent elements in a set that supports duplicate keys may appear in any order.

The `Sort` function takes a binary predicate which specifies the sort order, as follows:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitSet.Sort([](const FString&amp; A, const FString&amp; B) {\n\t\treturn A &gt; B; // sort by reverse-alphabetical order\n\t});\n\t// FruitSet == [ &quot;Pear&quot;, &quot;Orange&quot;, &quot;Melon&quot;, &quot;Mango&quot;, &quot;Kiwi&quot;, &quot;Grapefruit&quot; ] (order is temporarily guaranteed)\n\n\tFruitSet.Sort([](const FString&amp; A, const FString&amp; B) {\n\t\treturn A.Len() &lt; B.Len(); // sort strings by length, shortest to longest\n\t});\n\t// FruitSet == [ &quot;Pear&quot;, &quot;Kiwi&quot;, &quot;Melon&quot;, &quot;Mango&quot;, &quot;Orange&quot;, &quot;Grapefruit&quot; ] (order is temporarily guaranteed)",
  "lines_of_code": 9,
  "id": 100366,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--b6861065e067aadd56419946eb7c9ef2e12f800bcf4cbe0459e620a2365a0cbe",
  "settings": {
    "is_hidden": false
  }
}
```

## Operators

Like `TArray`, `TSet` is a regular value type and as such can be copied with the standard copy constructor or assignment operator. Sets strictly own their elements, so copying a set is deep; the new set will have its own copy of the elements.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TSet&lt;int32, FString&gt; NewSet = FruitSet;\n\tNewSet.Add(TEXT(&quot;Apple&quot;));\n\tNewSet.Remove(TEXT(&quot;Pear&quot;));\n\t// FruitSet == [ &quot;Pear&quot;, &quot;Kiwi&quot;, &quot;Melon&quot;, &quot;Mango&quot;, &quot;Orange&quot;, &quot;Grapefruit&quot; ]\n\t// NewSet == [ &quot;Kiwi&quot;, &quot;Melon&quot;, &quot;Mango&quot;, &quot;Orange&quot;, &quot;Grapefruit&quot;, &quot;Apple&quot; ]",
  "lines_of_code": 5,
  "id": 100367,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--f421df7e033ec7787550624d995ba8367e13cea9965079aab2bab7312d9f0060",
  "settings": {
    "is_hidden": false
  }
}
```

## Slack

Slack is allocated memory that doesn't contain an element. You can allocate memory without adding elements by calling `Reserve`, and you can remove elements without deallocating the memory they were using by calling `Reset` or by calling `Empty` with a non-zero slack parameter. Slack optimizes the process of adding new elements to the set by using pre-allocated memory instead of having to allocate new memory. It can also help with element removal, since the system does not need to deallocate memory. This is especially efficient when you are emptying a set that you expect to repopulate immediately with the same number of elements or fewer.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code>TSet</code> does not provide a way of checking how many elements are preallocated, like the <code>Max</code> function in <code>TArray</code> does.",
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

The following code removes all elements from the set without deallocating any memory, resulting in the creation of slack:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitSet.Reset();\n\t// FruitSet == [ &lt;invalid&gt;, &lt;invalid&gt;, &lt;invalid&gt;, &lt;invalid&gt;, &lt;invalid&gt;, &lt;invalid&gt; ]",
  "lines_of_code": 2,
  "id": 100368,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--49a8b50a23d1d022bd537417d81224a316d8da86143dfab8ba9475ba0d4a3828",
  "settings": {
    "is_hidden": false
  }
}
```

To create slack directly, such as to preallocate memory before adding elements, use the `Reserve` function.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitSet.Reserve(10);\n\tfor (int32 i = 0; i &lt; 10; ++i)\n\t{\n\t\tFruitSet.Add(FString::Printf(TEXT(&quot;Fruit%d&quot;), i));\n\t}\n\t// FruitSet == [ &quot;Fruit9&quot;, &quot;Fruit8&quot;, &quot;Fruit7&quot; ... &quot;Fruit2&quot;, &quot;Fruit1&quot;, &quot;Fruit0&quot; ]",
  "lines_of_code": 6,
  "id": 100369,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNjksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--01d52cb2f896e1b34de38cca11d13c2493a8e46e3eae600def681bd49a1e92c5",
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
      "content": "Preallocating the slack has caused the new elements to be added in reverse order. Unlike arrays, sets do not attempt to maintain element order, and code dealing with sets should not expect element order to be stable or predictable.",
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

To remove all slack from a `TSet`, use the `Collapse` and `Shrink` functions. `Shrink` removes all slack from the end of the container, but this will leave any empty elements in the middle or at the start.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Remove every other element from the set.\n\tfor (int32 i = 0; i &lt; 10; i += 2)\n\t{\n\t\tFruitSet.Remove(FSetElementId::FromInteger(i));\n\t}\n\t// FruitSet == [&quot;Fruit8&quot;, &lt;invalid&gt;, &quot;Fruit6&quot;, &lt;invalid&gt;, &quot;Fruit4&quot;, &lt;invalid&gt;, &quot;Fruit2&quot;, &lt;invalid&gt;, &quot;Fruit0&quot;, &lt;invalid&gt; ]\n\n\tFruitSet.Shrink();\n\t// FruitSet == [&quot;Fruit8&quot;, &lt;invalid&gt;, &quot;Fruit6&quot;, &lt;invalid&gt;, &quot;Fruit4&quot;, &lt;invalid&gt;, &quot;Fruit2&quot;, &lt;invalid&gt;, &quot;Fruit0&quot; ]",
  "lines_of_code": 9,
  "id": 100370,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNzAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--34c7aad96dce05b6309892217d08e36ad81897c2803d4f49a568e9c69dd6bb1e",
  "settings": {
    "is_hidden": false
  }
}
```

`Shrink` only removed one invalid element in the code above because there was only one empty element at the end. To remove all slack, the `Compact` or `CompactStable` function should be called first, so that the empty spaces will be grouped together in preparation for `Shrink`. As its name implies, `CompactStable` maintains element order while consolidating empty elements.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FruitSet.CompactStable();\n\t// FruitSet == [&quot;Fruit8&quot;, &quot;Fruit6&quot;, &quot;Fruit4&quot;, &quot;Fruit2&quot;, &quot;Fruit0&quot;, &lt;invalid&gt;, &lt;invalid&gt;, &lt;invalid&gt;, &lt;invalid&gt; ]\n\tFruitSet.Shrink();\n\t// FruitSet == [&quot;Fruit8&quot;, &quot;Fruit6&quot;, &quot;Fruit4&quot;, &quot;Fruit2&quot;, &quot;Fruit0&quot; ]",
  "lines_of_code": 4,
  "id": 100371,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDAzNzEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyODoyOCswMDowMCJ9--a28ea4b9cf27ca79922a0364ee00171352ff416bd5ebdc668095dacddf982fe7",
  "settings": {
    "is_hidden": false
  }
}
```

## DefaultKeyFuncs

As long as a type has an `operator==` and a non-member `GetTypeHash` overload, TSet can use it, since the type is both the element and the key. However, it may be useful to use types as keys where it is undesirable to overload those functions. In these cases, you can provide your own custom `DefaultKeyFuncs`. To create `KeyFuncs` for your key type, you must define two typedefs and three static functions, as follows:

- `KeyInitType` — Type used to pass keys around. Usually drawn from the ElementType template parameter.
- `ElementInitType` — Type used to pass elements around. Also usually drawn from the ElementType template parameter, and therefore identical to KeyInitType.
- `KeyInitType GetSetKey(ElementInitType Element)` — Returns the key of an element. For sets, this is usually just the element itself.
- `bool Matches(KeyInitType A, KeyInitType B)` — Returns `true` if `A` and `B` are equivalent, `false` otherwise.
- `uint32 GetKeyHash(KeyInitType Key)` — Returns the hash value of `Key`.

`KeyInitType` and `ElementInitType` are typedefs to the normal passing convention of the key/element type. Usually, these will be a value for trivial types and a const reference for non-trivial types. Remember that the element type of a set is also the key type, which is why `DefaultKeyFuncs` uses only one template parameter, `ElementType`, to define both.

`TSet` assumes that two items that compare equal using `Matches` (in `DefaultKeyFuncs`) will also return the same value from `GetKeyHash` (in `KeyFuncs`).

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Do not modify the key of an existing element in a way that will change the results from either of these functions, as this will invalidate set's internal hash. These rules also apply to the overloads of <code>operator==</code> and <code>GetKeyHash</code> when using the default implementation of <code>DefaultKeyFuncs</code>.",
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

The `Dump` function takes an `FOutputDevice` and writes out some implementation information about the contents of the set. There is also a `DumpHashElements` function that lists all elements from all hash entries. These functions are usually used for debugging.
