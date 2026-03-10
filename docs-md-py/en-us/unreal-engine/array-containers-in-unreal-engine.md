# TArray: Arrays in Unreal Engine

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/array-containers-in-unreal-engine

> Application Version: 5.7

The simplest container class in Unreal Engine is `TArray`. `TArray` is responsible for the ownership and organization of a sequence of other objects (called "elements") of the same type. As a `TArray` is a sequence, its elements have a well-defined order and its functions are used to deterministically manipulate those objects and their order.

## TArray

`TArray` is the most common container class within Unreal Engine. It is fast, memory efficient, and safe. `TArray` types are defined by two properties: Element type, and an optional allocator.

The element type is the type of the objects that will be stored in the array. `TArray` is what is called a homogenous container, meaning that all of its elements are strictly the same type; you cannot store elements of different types in a single `TArray`.

The allocator is quite frequently omitted and will default to one which is appropriate for most use cases. It defines how the objects are laid out in memory and how the array should grow to accommodate more elements. There are a number of different allocators you can use if you decide that the default behavior is not for you, or you can write your own. More on this later.

`TArray` is a value type, meaning that it should be treated similarly as any other built-in type, like `int32` or `float`. It is not designed to be extended, and creating or destroying `TArray` instances with `new` and `delete` is not a recommended practice. The elements are also value types, and the array owns them. Destruction of a `TArray` will result in the destruction of any elements it still contains. Creating a TArray variable from another will copy its elements into the new variable; there is no shared state.

## Creating and Filling an Array

To create an array, define it like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;int32&gt; IntArray;",
  "lines_of_code": 1,
  "id": 97972,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk3MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--bcddd1a6cda3d1c4034c101ceb348b9da9824da24d3d3dff404a9a228cc66bbb",
  "settings": {
    "is_hidden": false
  }
}
```

This creates an empty array designed to hold a sequence of integers. The element type can be any value type that is copyable and destructible according to normal C++ value rules, like `int32`, `FString`, `TSharedPtr`, and so on. No allocator has been specified, so the `TArray` will use the default, heap-based allocator. At this point, no memory has been allocated.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">TArray</code> (like many Unreal Engine containers) assumes that the element type is trivially relocatable, meaning that elements can safely be moved from one location in memory to another by directly copying raw bytes.",
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

`TArrays` can be populated in several ways. One way is with the `Init` function, which will fill an array with a number of copies of an element:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "IntArray.Init(10, 5);\n\t// IntArray == [10,10,10,10,10]",
  "lines_of_code": 2,
  "id": 97973,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk3MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--e1df6213cbedc8868840307997bc0045d9784e83d24e2f382f39fc50d07e5dd1",
  "settings": {
    "is_hidden": false
  }
}
```

`Add` and `Emplace` functions can create new elements at the end of the array:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;FString&gt; StrArr;\n\tStrArr.Add    (TEXT(&quot;Hello&quot;));\n\tStrArr.Emplace(TEXT(&quot;World&quot;));\n\t// StrArr == [&quot;Hello&quot;,&quot;World&quot;]",
  "lines_of_code": 4,
  "id": 97974,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk3NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--97a51b9136f454f8690abfffe6cb87dda1bdbb735177a641843acff54f3616a7",
  "settings": {
    "is_hidden": false
  }
}
```

The array's allocator provides memory as needed when new elements are added to the array. The default allocator adds enough memory for multiple new elements whenever the current array size is exceeded. `Add` and `Emplace` do much the same thing but with a subtle difference:

- `Add` (or `Push`) will copy (or move) an instance of the element type into the array.
- `Emplace` will use the arguments you give it to construct a new instance of the element type.

In the case of our `TArray<FString>`, `Add` will create a temporary `FString` from the string literal and then move the contents of that temporary `FString` into a new `FString` inside the container, whereas `Emplace` will just create the new `FString` directly using the string literal. The end result is the same, but `Emplace` avoids creating a temporary variable, which is often undesirable for non-trivial value types like `FString`.

In general, `Emplace` is preferable to `Add`, in that it avoids creating unnecessary temporary variables at the call site which are then copied or moved into the container. As a rule of thumb, use `Add` for trivial types and `Emplace` otherwise. `Emplace` will never be less efficient than `Add`, but `Add` may read better.

`Append` adds multiple elements at once from either another `TArray`, or a pointer to a regular C array and the size of that array:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString Arr[] = { TEXT(&quot;of&quot;), TEXT(&quot;Tomorrow&quot;) };\n\tStrArr.Append(Arr, ARRAY_COUNT(Arr));\n\t// StrArr == [&quot;Hello&quot;,&quot;World&quot;,&quot;of&quot;,&quot;Tomorrow&quot;]",
  "lines_of_code": 3,
  "id": 97975,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk3NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--bcbf50c920efe915a5159da6d7fc8e6404ea6492a278368aeed8f9e079d9ee51",
  "settings": {
    "is_hidden": false
  }
}
```

`AddUnique` only adds a new element to the container if an equivalent element doesn't already exist. Equivalence is checked by using the element type's `operator==`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr.AddUnique(TEXT(&quot;!&quot;));\n\t// StrArr == [&quot;Hello&quot;,&quot;World&quot;,&quot;of&quot;,&quot;Tomorrow&quot;,&quot;!&quot;]\n\n\tStrArr.AddUnique(TEXT(&quot;!&quot;));\n\t// StrArr is unchanged as &quot;!&quot; is already an element",
  "lines_of_code": 5,
  "id": 97976,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk3NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--528d89a35476aebed120ea240fb09fa7a3f2d1853e1b66710e6d05ea1526b1bc",
  "settings": {
    "is_hidden": false
  }
}
```

`Insert`, like `Add`, `Emplace` and `Append`, adds a single element or a copy of an array of elements at a given index:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr.Insert(TEXT(&quot;Brave&quot;), 1);\n\t// StrArr == [&quot;Hello&quot;,&quot;Brave&quot;,&quot;World&quot;,&quot;of&quot;,&quot;Tomorrow&quot;,&quot;!&quot;]",
  "lines_of_code": 2,
  "id": 97977,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk3NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--41e1cf7254931fc88fb74b9b5260fb29703de2ff33446d32b369d91aebbd92fa",
  "settings": {
    "is_hidden": false
  }
}
```

The `SetNum` function can directly set the number of array elements, with new elements being created using the element type's default constructor if the new number is greater than the current one:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr.SetNum(8);\n\t// StrArr == [&quot;Hello&quot;,&quot;Brave&quot;,&quot;World&quot;,&quot;of&quot;,&quot;Tomorrow&quot;,&quot;!&quot;,&quot;&quot;,&quot;&quot;]",
  "lines_of_code": 2,
  "id": 97978,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk3OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--0707b3f4741f9ed3f3909090588a6a5e5db90a710e4ffb42cb7ced4a725f642f",
  "settings": {
    "is_hidden": false
  }
}
```

`SetNum` will also remove elements if the new number is less than the current one. More detailed information on element removal will come later:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr.SetNum(6);\n\t// StrArr == [&quot;Hello&quot;,&quot;Brave&quot;,&quot;World&quot;,&quot;of&quot;,&quot;Tomorrow&quot;,&quot;!&quot;]",
  "lines_of_code": 2,
  "id": 97979,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk3OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--2fc1d9f698dbc10b50515e4f046f5d1fb47e26d3467ffb298c03d7b21c961836",
  "settings": {
    "is_hidden": false
  }
}
```

## Iteration

There are several ways to iterate over the elements of your array, but the recommended way is to use the C++ ranged-for feature:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString JoinedStr;\n\tfor (auto&amp; Str : StrArr)\n\t{\n\t\tJoinedStr += Str;\n\t\tJoinedStr += TEXT(&quot; &quot;);\n\t}\n\t// JoinedStr == &quot;Hello Brave World of Tomorrow ! &quot;",
  "lines_of_code": 7,
  "id": 97980,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--81d4032b504eb0771b4aacd9aaeef1b99e254ac9c666c28d1ebe1f7f99813e5d",
  "settings": {
    "is_hidden": false
  }
}
```

Regular index-based iteration is also possible, of course:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "for (int32 Index = 0; Index != StrArr.Num(); ++Index)\n\t{\n\t\tJoinedStr += StrArr[Index];\n\t\tJoinedStr += TEXT(&quot; &quot;);\n\t}",
  "lines_of_code": 5,
  "id": 97981,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--44e12a01a2beb0d9d585ad58e323c73e81348742e021b64005add0bc3c1eebd5",
  "settings": {
    "is_hidden": false
  }
}
```

Finally, arrays also have their own iterator type for more control over your iteration. There are two functions called `CreateIterator` and `CreateConstIterator` which can be used for read-write or read-only access to the elements respectively:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "for (auto It = StrArr.CreateConstIterator(); It; ++It)\n\t{\n\t\tJoinedStr += *It;\n\t\tJoinedStr += TEXT(&quot; &quot;);\n\t}",
  "lines_of_code": 5,
  "id": 97982,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--5197fa56a47252d4b6321464eb8f30f897f7c2af99fbf894422313163ed0ca49",
  "settings": {
    "is_hidden": false
  }
}
```

## Sorting

Arrays can be sorted simply by calling the `Sort` function:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr.Sort();\n\t// StrArr == [&quot;!&quot;,&quot;Brave&quot;,&quot;Hello&quot;,&quot;of&quot;,&quot;Tomorrow&quot;,&quot;World&quot;]",
  "lines_of_code": 2,
  "id": 97983,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--4fe568eeb5f9864a5f41191417136fdf18c350510adb565fb1f47c8f5ec80ffc",
  "settings": {
    "is_hidden": false
  }
}
```

Here, the values are sorted by means of the element type's `operator<`. In FString's case, this is a case-insensitive lexicographical comparison. A binary predicate can also be implemented to provide different ordering semantics, like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr.Sort([](const FString&amp; A, const FString&amp; B) {\n\t\treturn A.Len() &lt; B.Len();\n\t});\n\t// StrArr == [&quot;!&quot;,&quot;of&quot;,&quot;Hello&quot;,&quot;Brave&quot;,&quot;World&quot;,&quot;Tomorrow&quot;]",
  "lines_of_code": 4,
  "id": 97984,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--3f6f0e6db8adec8fb1de99755a2e3c82b37504aa9bece4c134101d7354519814",
  "settings": {
    "is_hidden": false
  }
}
```

Now the strings are sorted by their lengths. Note how the three strings with the same length - "Hello", "Brave" and "World" - have changed order relative to their positions in the array beforehand. This is because `Sort` is unstable and the relative order of equivalent elements (those strings are equivalent here because the predicate only compares length) is not guaranteed. `Sort` is implemented as a quicksort.

The `HeapSort` function, with or without a binary predicate, can be used to perform a heap sort. Whether or not you choose to use it depends on your particular data and how efficiently it sorts compared to the Sort function. Like `Sort`, `HeapSort` is not stable. If we had used `HeapSort` instead of `Sort` above, this would be the result (the same, in this case):

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr.HeapSort([](const FString&amp; A, const FString&amp; B) {\n\t\treturn A.Len() &lt; B.Len();\n\t});\n\t// StrArr == [&quot;!&quot;,&quot;of&quot;,&quot;Hello&quot;,&quot;Brave&quot;,&quot;World&quot;,&quot;Tomorrow&quot;]",
  "lines_of_code": 4,
  "id": 97985,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--6d792dfb4383e5ff3f1b48ba331dee3c546b11bc2f5cebd0cc2b3a1e77c7b35f",
  "settings": {
    "is_hidden": false
  }
}
```

Finally, `StableSort` can be used to guarantee the relative order of equivalent elements after sorting. If we had called `StableSort` instead of `Sort` or `HeapSort` above, the result would have been as follows:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr.StableSort([](const FString&amp; A, const FString&amp; B) {\n\t\treturn A.Len() &lt; B.Len();\n\t});\n\t// StrArr == [&quot;!&quot;,&quot;of&quot;,&quot;Brave&quot;,&quot;Hello&quot;,&quot;World&quot;,&quot;Tomorrow&quot;]",
  "lines_of_code": 4,
  "id": 97986,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--ec985127d64f8218dd25ef9bb88b85388b32e68cbd10461a97cf02b28459f179",
  "settings": {
    "is_hidden": false
  }
}
```

That is, "Brave", "Hello" and "World" remain in their same relative order after previously having been lexicographically sorted. `StableSort` is implemented as a merge sort.

## Queries

We can ask the array how many elements it holds by using the `Num` function:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 Count = StrArr.Num();\n\t// Count == 6",
  "lines_of_code": 2,
  "id": 97987,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--0fc6cf2970532e759b3251cb458519a4da411e58f4523aba296adc8e1ae93549",
  "settings": {
    "is_hidden": false
  }
}
```

If you need direct access to the array memory, perhaps for interoperability with a C-style API, you can use the `GetData` function to return a pointer to the elements in the array. This pointer is only valid as long as the array exists and before any mutating operations are made to the array. Only the first `Num` indices from the `StrPtr` are dereferenceable:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString* StrPtr = StrArr.GetData();\n\t// StrPtr[0] == &quot;!&quot;\n\t// StrPtr[1] == &quot;of&quot;\n\t// ...\n\t// StrPtr[5] == &quot;Tomorrow&quot;\n\t// StrPtr[6] - undefined behavior",
  "lines_of_code": 6,
  "id": 97988,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--1697ab06f0d22644f61cfbcf6cff512d0e5377b13cb43b1c8e49d29caa49be12",
  "settings": {
    "is_hidden": false
  }
}
```

If the container is const, then the returned pointer will also be const.

You can also ask the container how big the elements are:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "uint32 ElementSize = StrArr.GetTypeSize();\n\t// ElementSize == sizeof(FString)",
  "lines_of_code": 2,
  "id": 97989,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk4OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--a6a5cc7651207a0896c749474ea7a664e13c475313cdcc4764b8537e706a29a4",
  "settings": {
    "is_hidden": false
  }
}
```

To retrieve elements, you can use the indexing `operator[]` and pass it a zero-based index to the element you want:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString Elem1 = StrArr[1];\n\t// Elem1 == &quot;of&quot;",
  "lines_of_code": 2,
  "id": 97990,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--caa9b3b755bb849cbbce16afde9f17f11a8456cde3e8e73f036cd534efda4e12",
  "settings": {
    "is_hidden": false
  }
}
```

Passing an invalid index — less than 0 or greater than or equal to Num() — will cause a runtime error. You can ask the container if a particular index is valid using the `IsValidIndex` function:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "bool bValidM1 = StrArr.IsValidIndex(-1);\n\tbool bValid0  = StrArr.IsValidIndex(0);\n\tbool bValid5  = StrArr.IsValidIndex(5);\n\tbool bValid6  = StrArr.IsValidIndex(6);\n\t// bValidM1 == false\n\t// bValid0  == true\n\t// bValid5  == true\n\t// bValid6  == false",
  "lines_of_code": 8,
  "id": 97991,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--558031ad6587341c0d5805b7f51ee1669a403c321ef07a283ef886293d0a4041",
  "settings": {
    "is_hidden": false
  }
}
```

`operator[]` returns a reference, so it can also be used to mutate the elements inside the array, assuming your array isn't const:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "StrArr[3] = StrArr[3].ToUpper();\n\t// StrArr == [&quot;!&quot;,&quot;of&quot;,&quot;Brave&quot;,&quot;HELLO&quot;,&quot;World&quot;,&quot;Tomorrow&quot;]",
  "lines_of_code": 2,
  "id": 97992,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--7d036677d3f375caa032ade13128989ed478756af70b9e93a7749b05e9332527",
  "settings": {
    "is_hidden": false
  }
}
```

Like the GetData function, `operator[]` will return a const reference if the array is const. You can also index from the end of the array backward by using the `Last` function. The index defaults to zero. The `Top` function is a synonym for `Last`, except it doesn't take an index:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString ElemEnd  = StrArr.Last();\n\tFString ElemEnd0 = StrArr.Last(0);\n\tFString ElemEnd1 = StrArr.Last(1);\n\tFString ElemTop  = StrArr.Top();\n\t// ElemEnd  == &quot;Tomorrow&quot;\n\t// ElemEnd0 == &quot;Tomorrow&quot;\n\t// ElemEnd1 == &quot;World&quot;\n\t// ElemTop  == &quot;Tomorrow&quot;",
  "lines_of_code": 8,
  "id": 97993,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--3fe6365f8dac8cef063e245dfed95f15de0d4dbba65958d4a0f7166f3d246537",
  "settings": {
    "is_hidden": false
  }
}
```

We can ask the array if it contains a certain element:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "bool bHello   = StrArr.Contains(TEXT(&quot;Hello&quot;));\n\tbool bGoodbye = StrArr.Contains(TEXT(&quot;Goodbye&quot;));\n\t// bHello   == true\n\t// bGoodbye == false",
  "lines_of_code": 4,
  "id": 97994,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--de6198da7da35fdeabdd8e2da5d37eaa67e67d18d4bfbb3c943d5cc978deba77",
  "settings": {
    "is_hidden": false
  }
}
```

Or ask the array if it contains an element which matches a specific predicate:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "bool bLen5 = StrArr.ContainsByPredicate([](const FString&amp; Str){\n\t\treturn Str.Len() == 5;\n\t});\n\tbool bLen6 = StrArr.ContainsByPredicate([](const FString&amp; Str){\n\t\treturn Str.Len() == 6;\n\t});\n\t// bLen5 == true\n\t// bLen6 == false",
  "lines_of_code": 8,
  "id": 97995,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--6a53523964ad5d2c7392c415b6d99207e356c4dc36e6cf0bc5a6f35b5d7baee0",
  "settings": {
    "is_hidden": false
  }
}
```

We can find elements by using the `Find` family of functions. To check if an element exists and return its index, we use Find:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 Index;\n\tif (StrArr.Find(TEXT(&quot;Hello&quot;), Index))\n\t{\n\t\t// Index == 3\n\t}",
  "lines_of_code": 5,
  "id": 97996,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--ed6e09cab8604e623abeb38ddf6a07e39e60e522eb57f33fe1c0ecb00c48053d",
  "settings": {
    "is_hidden": false
  }
}
```

This sets `Index` to be the index of the first element found. If there are duplicate elements and we instead want to find the index of last element, we use the `FindLast` function instead:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 IndexLast;\n\tif (StrArr.FindLast(TEXT(&quot;Hello&quot;), IndexLast))\n\t{\n\t\t// IndexLast == 3, because there aren&#39;t any duplicates\n\t}",
  "lines_of_code": 5,
  "id": 97997,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--eeba787a3ae4b379e9bc6151c597ed1becf31b6813ab3f0fcb336bcd6719aa1f",
  "settings": {
    "is_hidden": false
  }
}
```

Both of these functions return a bool to indicate whether or not an element was found, while also writing the index of that element into a variable when it was found.

`Find` and `FindLast` can also return an element index directly. They will do this if you do not pass the index as an explicit argument. This can be more succinct than the above function, and which function you use depends on what suits your particular need or style.

If no element was found, the special `INDEX_NONE` value is returned:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 Index2     = StrArr.Find(TEXT(&quot;Hello&quot;));\n\tint32 IndexLast2 = StrArr.FindLast(TEXT(&quot;Hello&quot;));\n\tint32 IndexNone  = StrArr.Find(TEXT(&quot;None&quot;));\n\t// Index2     == 3\n\t// IndexLast2 == 3\n\t// IndexNone  == INDEX_NONE",
  "lines_of_code": 6,
  "id": 97998,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--15bc5c534e7d8ad5c49aedf402d7864e6f9768510f3bd2e5bc35fbdfcd3c078b",
  "settings": {
    "is_hidden": false
  }
}
```

`IndexOfByKey` works similarly, but allows comparison of the elements with an arbitrary object. With the `Find` functions, the argument is actually converted to the element type (`FString` in this case) before the search begins. With `IndexOfByKey`, the key is compared directly, supporting searches even when the key type isn't directly convertible to the element type.

`IndexOfByKey` works for any key type for which `operator==(ElementType, KeyType)` exists. `IndexOfByKey` will return the index of the first found element, or `INDEX_NONE` if no element was found:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 Index = StrArr.IndexOfByKey(TEXT(&quot;Hello&quot;));\n\t// Index == 3",
  "lines_of_code": 2,
  "id": 97999,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5Nzk5OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--cefe77555136f16af1105cfedcf9bf740fc06a6657afba6edb4abc3db427cf68",
  "settings": {
    "is_hidden": false
  }
}
```

The `IndexOfByPredicate` function finds the index of the first element that matches the specified predicate, again returning the special `INDEX_NONE` value if none was found:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 Index = StrArr.IndexOfByPredicate([](const FString&amp; Str){\n\t\treturn Str.Contains(TEXT(&quot;r&quot;));\n\t});\n\t// Index == 2",
  "lines_of_code": 4,
  "id": 98000,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--37248c577ab02942439af9f6e5b352d7f35e809736d9d709a4ab56a2a82f541e",
  "settings": {
    "is_hidden": false
  }
}
```

Instead of returning indices, we can return pointers back to the elements we find. `FindByKey` works like `IndexOfByKey`, comparing the elements to an arbitrary object, but returning a pointer to the element it finds. If it does not find an element, it will return `nullptr`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "auto* OfPtr  = StrArr.FindByKey(TEXT(&quot;of&quot;)));\n\tauto* ThePtr = StrArr.FindByKey(TEXT(&quot;the&quot;)));\n\t// OfPtr  == &amp;StrArr[1]\n\t// ThePtr == nullptr",
  "lines_of_code": 4,
  "id": 98001,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--6f88b9118d429c43b6ddc9fe89043760c8c76588bf4aaed45faa362d0dc590bb",
  "settings": {
    "is_hidden": false
  }
}
```

`FindByPredicate` can be used like `IndexOfByPredicate`, except that it returns pointer instead of an index:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "auto* Len5Ptr = StrArr.FindByPredicate([](const FString&amp; Str){\n\t\treturn Str.Len() == 5;\n\t});\n\tauto* Len6Ptr = StrArr.FindByPredicate([](const FString&amp; Str){\n\t\treturn Str.Len() == 6;\n\t});\n\t// Len5Ptr == &amp;StrArr[2]\n\t// Len6Ptr == nullptr",
  "lines_of_code": 8,
  "id": 98002,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--b62d3bf3d640e5e25db7f217a395b5e0d4a252245fa0391c1fb3136204088273",
  "settings": {
    "is_hidden": false
  }
}
```

Finally, you can retrieve an array of elements matching a particular predicate with the `FilterByPredicate` function:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "auto Filter = StrArray.FilterByPredicate([](const FString&amp; Str){\n\t\treturn !Str.IsEmpty() &amp;&amp; Str[0] &lt; TEXT(&#39;M&#39;);\n\t});",
  "lines_of_code": 3,
  "id": 98003,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--f77e34ff9239192c16c3c25ce98aa666a15bb17565ceed957b9aee7d830ca92f",
  "settings": {
    "is_hidden": false
  }
}
```

## Removal

You can erase elements from the array using the `Remove` family of functions. The `Remove` function removes all elements that are considered equal to the element you provide, according to the element type's `operator==` function. For example:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;int32&gt; ValArr;\n\tint32 Temp[] = { 10, 20, 30, 5, 10, 15, 20, 25, 30 };\n\tValArr.Append(Temp, ARRAY_COUNT(Temp));\n\t// ValArr == [10,20,30,5,10,15,20,25,30]\n\n\tValArr.Remove(20);\n\t// ValArr == [10,30,5,10,15,25,30]",
  "lines_of_code": 7,
  "id": 98004,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--a4da660aff8f001122c83c2ba9e1c30ba7ad57404db71ee3988fac874e0fd227",
  "settings": {
    "is_hidden": false
  }
}
```

You can also use `RemoveSingle` to erase the first matching element in the array. This is useful if you know your array may contain duplicates and you only want to erase one, or as an optimization if you know that your array can only ever contain one matching element:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "ValArr.RemoveSingle(30);\n\t// ValArr == [10,5,10,15,25,30]",
  "lines_of_code": 2,
  "id": 98005,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--414f826c26212268be7b670c672f3e17e94f68068afff5d7a9cf62593e837812",
  "settings": {
    "is_hidden": false
  }
}
```

We can also remove elements by their zero-based index by using the `RemoveAt` function. You may wish to use `IsValidIndex` to verify that the array has an element with the index you plan to provide, as passing an invalid index to this function will cause a runtime error.:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "ValArr.RemoveAt(2); // Removes the element at index 2\n\t// ValArr == [10,5,15,25,30]\n\n\tValArr.RemoveAt(99); // This will cause a runtime error as\n\t                       // there is no element at index 99",
  "lines_of_code": 5,
  "id": 98006,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--51f5a56d0040db833f624bd1a956cb58736266b919cb5ac4432f705c2616957f",
  "settings": {
    "is_hidden": false
  }
}
```

We can also remove elements which match a predicate by using the `RemoveAll` function. For example, removing all values which are a multiple of 3:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "ValArr.RemoveAll([](int32 Val) {\n\t\treturn Val % 3 == 0;\n\t});\n\t// ValArr == [10,5,25]",
  "lines_of_code": 4,
  "id": 98007,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--82d1027412ceb30aec9dbbb96c35f1a940f5530e8471bff962a54abfc7570848",
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
      "content": "In all of these cases, when elements were removed, the elements that followed were shuffled down into lower indices, as there can never be holes left in the array.",
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

The shuffling process has an overhead. If you don't really care what order the remaining elements are left in, this overhead can be reduced by using the `RemoveSwap`, `RemoveAtSwap` and `RemoveAllSwap` functions, which work like their non-swapping variants except that they don't guarantee the order of the remaining elements, enabling them to complete their tasks more quickly:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;int32&gt; ValArr2;\n\tfor (int32 i = 0; i != 10; ++i)\n\t\tValArr2.Add(i % 5);\n\t// ValArr2 == [0,1,2,3,4,0,1,2,3,4]\n\n\tValArr2.RemoveSwap(2);\n\t// ValArr2 == [0,1,4,3,4,0,1,3]\n\n\tValArr2.RemoveAtSwap(1);\n\t// ValArr2 == [0,3,4,3,4,0,1]\n",
  "lines_of_code": 15,
  "id": 98008,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--7e7365d381cdd5d056ff7652df03925d3fc3e9c03cff2a95d264ae6e9141fe67",
  "settings": {
    "is_hidden": false
  }
}
```

Finally, the `Empty` function will remove everything from the array:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "ValArr2.Empty();\n\t// ValArr2 == []",
  "lines_of_code": 2,
  "id": 98009,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAwOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--5c393817ce857eff5c99c46551c7acb1ad7040f6821aeba593688d3a2d048882",
  "settings": {
    "is_hidden": false
  }
}
```

## Operators

Arrays are regular value types and as such can be copied by the standard copy constructor or assignment operator. As arrays strictly own their elements, copying an array is deep and so the new array will have its own copy of the elements:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;int32&gt; ValArr3;\n\tValArr3.Add(1);\n\tValArr3.Add(2);\n\tValArr3.Add(3);\n\n\tauto ValArr4 = ValArr3;\n\t// ValArr4 == [1,2,3];\n\tValArr4[0] = 5;\n\t// ValArr3 == [1,2,3];\n\t// ValArr4 == [5,2,3];",
  "lines_of_code": 10,
  "id": 98010,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--494a30e380ce3ecbff4cd2c7945d8ad760860034805b556f74031fd220a609ec",
  "settings": {
    "is_hidden": false
  }
}
```

As an alternative to the `Append` function, you can concatenate arrays with `operator+=`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "ValArr4 += ValArr3;\n\t// ValArr4 == [5,2,3,1,2,3]",
  "lines_of_code": 2,
  "id": 98011,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--b53acedbd31a24ef44fc16f3d5ca51fc515147014900fd26d00d64c4536f38c9",
  "settings": {
    "is_hidden": false
  }
}
```

`TArray` also supports move semantics, which can be invoked using the `MoveTemp` function. After a move, the source array is guaranteed to be left empty:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "ValArr3 = MoveTemp(ValArr4);\n\t// ValArr3 == [5,2,3,1,2,3]\n\t// ValArr4 == []",
  "lines_of_code": 3,
  "id": 98012,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--065c0247176e630b85f597b6bed93564f0694c60923a5429c5306feadc3a26fa",
  "settings": {
    "is_hidden": false
  }
}
```

Arrays can be compared using the `operator==` and `operator!=`. The order of the elements are important — two arrays are only equal if they have the same number of elements in the same order. Elements are compared using their own `operator==`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;FString&gt; FlavorArr1;\n\tFlavorArr1.Emplace(TEXT(&quot;Chocolate&quot;));\n\tFlavorArr1.Emplace(TEXT(&quot;Vanilla&quot;));\n\t// FlavorArr1 == [&quot;Chocolate&quot;,&quot;Vanilla&quot;]\n\n\tauto FlavorArr2 = Str1Array;\n\t// FlavorArr2 == [&quot;Chocolate&quot;,&quot;Vanilla&quot;]\n\n\tbool bComparison1 = FlavorArr1 == FlavorArr2;\n\t// bComparison1 == true\n",
  "lines_of_code": 25,
  "id": 98013,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--299d5ba4b8fdb0fb4b041f886e0b5ac0252dafc8e3546cb098de776b16c9ceca",
  "settings": {
    "is_hidden": false
  }
}
```

## Heap

`TArray` has functions that support a binary heap data structure. A heap is a type of binary tree in which any parent node is equivalent to or ordered before all of its child nodes. When implemented as an array, the root node of the tree is at element 0 and the indices of the left and right child nodes of a node at index N are 2N+1 and 2N+2 respectively. The children are not in any particular order with respect to one another.

Any existing array can be turned into a heap by calling the `Heapify` function. This is overloaded to take a predicate or not, where the non-predicated version will use the element type's `operator<` to determine ordering:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;int32&gt; HeapArr;\n\tfor (int32 Val = 10; Val != 0; --Val)\n\t{\n\t\tHeapArr.Add(Val);\n\t}\n\t// HeapArr == [10,9,8,7,6,5,4,3,2,1]\n\tHeapArr.Heapify();\n\t// HeapArr == [1,2,4,3,6,5,8,10,7,9]",
  "lines_of_code": 8,
  "id": 98014,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--baa7d788c3b8d619ecfe084ee804b104ee44e6058223b54cf660d0298977b81a",
  "settings": {
    "is_hidden": false
  }
}
```

This is a visualization of the tree:

![image alt text](https://dev.epicgames.com/community/api/documentation/image/cf9d1918-b79c-4d56-b727-3b75ec3089bd)

The nodes in the tree can be read from left-to-right, top-to-bottom as the order of the elements in the heapified array. Note that the array isn't necessarily sorted after being transformed into a heap. While a sorted array would also be a valid heap, the heap structure definition is loose enough to allow multiple valid heaps for the same set of elements.

New elements can be added to the heap via the HeapPush function, reordering other nodes to maintain the heap:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "HeapArr.HeapPush(4);\n\t// HeapArr == [1,2,4,3,4,5,8,10,7,9,6]",
  "lines_of_code": 2,
  "id": 98015,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--32b37dd0d3938084c49317dd2c22ed4648856e4d4585c58f0d5579b646d87474",
  "settings": {
    "is_hidden": false
  }
}
```

![image alt text](https://dev.epicgames.com/community/api/documentation/image/1f3e88ac-70c4-47d9-951b-6b6296f784c5)

The `HeapPop` and `HeapPopDiscard` functions are used to remove the top node from the heap. The difference between the two is that the former takes a reference to an element type to return a copy of the top element, and the latter simply removes the top node without returning it in any way. Both functions result in the same change to the array, and the heap is again maintained by reordering other elements appropriately:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 TopNode;\n\tHeapArr.HeapPop(TopNode);\n\t// TopNode == 1\n\t// HeapArr == [2,3,4,6,4,5,8,10,7,9]",
  "lines_of_code": 4,
  "id": 98016,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--bfcf20033d45b04ad4d9d9380a3e02270b0ea8fda3c73defca53fc6f2aeec723",
  "settings": {
    "is_hidden": false
  }
}
```

![image alt text](https://dev.epicgames.com/community/api/documentation/image/b35a334b-1617-4cb8-ba43-e74907f8ba28)

`HeapRemoveAt` will remove an element from the array at a given index, and then reorder elements to maintain the heap:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "HeapArr.HeapRemoveAt(1);\n\t// HeapArr == [2,4,4,6,9,5,8,10,7]",
  "lines_of_code": 2,
  "id": 98017,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--f75307ddd67261844ae4a32cdb36705275a009e7d668f8e9c0316f78e4c41750",
  "settings": {
    "is_hidden": false
  }
}
```

![image alt text](https://dev.epicgames.com/community/api/documentation/image/675ef883-c76b-4e42-93cb-107037bf9938)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code>HeapPush</code>, <code>HeapPop</code>, <code>HeapPopDiscard</code> and <code>HeapRemoveAt</code> should only be called when the structure is already a valid heap, such as after a <code>Heapify</code> call, any other heap operation, or by manually manipulating the array into a heap.",
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

Each of these functions, including `Heapify`, can take an optional binary predicate to determine the order of the node elements in the heap. By default, heap operations use the element type's `operator<` to determine order. When using a custom predicate, it is important to use the same predicate on all heap operations.

Finally, the top node of the heap can be inspected using `HeapTop`, without changing the array:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 Top = HeapArr.HeapTop();\n\t// Top == 2",
  "lines_of_code": 2,
  "id": 98018,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--122fec3e39b8a563e9d07bc374a28ba6685fd83ddc26bd0a1f42975a65e19b56",
  "settings": {
    "is_hidden": false
  }
}
```

## Slack

Because arrays can resize, they use a variable amount of memory. To avoid reallocation every time elements are added, allocators usually provide more memory than was requested so that future `Add` calls don't pay a performance penalty for reallocation. Likewise, removing elements doesn't usually free memory. This leaves the array with slack elements, which are effectively pre-allocated element storage slots that are not currently in use. The amount of slack in an array is defined as the difference between the number of elements stored in the array and the number of elements that the array could store with the amount of memory it has allocated.

As a default-constructed array allocates no memory, the slack will initially be zero. You can find out how much slack there is in an array by using the `GetSlack` function. The maximum number of elements that the array can hold before the container reallocates can be obtained by the `Max` function. `GetSlack` is equivalent to the difference between `Max` and `Num`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;int32&gt; SlackArray;\n\t// SlackArray.GetSlack() == 0\n\t// SlackArray.Num()      == 0\n\t// SlackArray.Max()      == 0\n\n\tSlackArray.Add(1);\n\t// SlackArray.GetSlack() == 3\n\t// SlackArray.Num()      == 1\n\t// SlackArray.Max()      == 4\n\n",
  "lines_of_code": 17,
  "id": 98019,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAxOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--721ed1c2790e7eb38cc0eb6134c9a5f3d3bb916880ee6adc73edcd2127a000e5",
  "settings": {
    "is_hidden": false
  }
}
```

The amount of slack in a container after a reallocation is decided by the allocator, so users should not rely on slack remaining constant.

Although slack management is not required, you can use it to your advantage to give the array optimization hints. For example, if you know you are about to add 100 new elements to the array, you can ensure you have a slack of at least 100 before adding, so that the array will not need to allocate memory while adding the new elements. The `Empty` function, mentioned above, takes an optional slack argument:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "SlackArray.Empty();\n\t// SlackArray.GetSlack() == 0\n\t// SlackArray.Num()      == 0\n\t// SlackArray.Max()      == 0\n\tSlackArray.Empty(3);\n\t// SlackArray.GetSlack() == 3\n\t// SlackArray.Num()      == 0\n\t// SlackArray.Max()      == 3\n\tSlackArray.Add(1);\n\tSlackArray.Add(2);\n",
  "lines_of_code": 14,
  "id": 98020,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAyMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--a755ac2a16baaf712cb3e429eaf9cca1a7bfc279bde68b218fbdc9e1d385588d",
  "settings": {
    "is_hidden": false
  }
}
```

There is a `Reset` function which works similarly to Empty, except that it doesn't free memory if the requested slack is already provided by the current allocation. However, it will allocate more memory if the requested slack is larger:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "SlackArray.Reset(0);\n\t// SlackArray.GetSlack() == 3\n\t// SlackArray.Num()      == 0\n\t// SlackArray.Max()      == 3\n\tSlackArray.Reset(10);\n\t// SlackArray.GetSlack() == 10\n\t// SlackArray.Num()      == 0\n\t// SlackArray.Max()      == 10",
  "lines_of_code": 8,
  "id": 98021,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAyMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--7a9023fe2add9a047eed03794c00d096fdae536c17c778fcdd0aeb5af9efb93e",
  "settings": {
    "is_hidden": false
  }
}
```

And finally, you can remove all slack with the `Shrink` function, which will resize the allocation to be the minimum size required to hold the current elements. `Shrink` does not have any effect on the elements in the array:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "SlackArray.Add(5);\n\tSlackArray.Add(10);\n\tSlackArray.Add(15);\n\tSlackArray.Add(20);\n\t// SlackArray.GetSlack() == 6\n\t// SlackArray.Num()      == 4\n\t// SlackArray.Max()      == 10\n\tSlackArray.Shrink();\n\t// SlackArray.GetSlack() == 0\n\t// SlackArray.Num()      == 4\n",
  "lines_of_code": 11,
  "id": 98022,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAyMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--83bbfef9aec6b7f600b0cf8720fd38de8d6b08c766b0509c62ed8f94c4277df1",
  "settings": {
    "is_hidden": false
  }
}
```

## Raw Memory

`TArray` is ultimately just a wrapper around allocated memory. It can be useful to treat it as such by direct modification of the bytes of the allocation and by creating elements yourself. `TArray` will always try to do the best it can with the information it has, but sometimes you may need to drop to a lower level.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The following functions give you fast, low-level access to <code>TArray</code> and the data it holds, but, if used improperly,  give you the ability to put the container into invalid states and cause undefined behavior.  It is up to you to return the container to a valid state after invoking these functions but before any other regular function is called.",
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

The `AddUninitialized` and `InsertUninitialized` functions will add some uninitialized space to the array. They work like the `Add` and `Insert` functions, respectively, but they will not call the constructor of the element type. This can be useful to avoid calling constructors. You might do this in cases like the following example, where you plan to overwrite the entire struct with a `Memcpy` call:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "int32 SrcInts[] = { 2, 3, 5, 7 };\n\tTArray&lt;int32&gt; UninitInts;\n\tUninitInts.AddUninitialized(4);\n\tFMemory::Memcpy(UninitInts.GetData(), SrcInts, 4*sizeof(int32));\n\t// UninitInts == [2,3,5,7]",
  "lines_of_code": 5,
  "id": 98023,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAyMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--c6ea005cc19d163b188368c5a0f41dc8dec7708fa7bee6f1bdd57d0dd9cdfbd5",
  "settings": {
    "is_hidden": false
  }
}
```

You can also use this feature to reserve memory for objects which you plan to construct yourself:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TArray&lt;FString&gt; UninitStrs;\n\tUninitStrs.Emplace(TEXT(&quot;A&quot;));\n\tUninitStrs.Emplace(TEXT(&quot;D&quot;));\n\tUninitStrs.InsertUninitialized(1, 2);\n\tnew ((void*)(UninitStrs.GetData() + 1)) FString(TEXT(&quot;B&quot;));\n\tnew ((void*)(UninitStrs.GetData() + 2)) FString(TEXT(&quot;C&quot;));\n\t// UninitStrs == [&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;D&quot;]",
  "lines_of_code": 7,
  "id": 98024,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAyNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--a74c6d00ac7059eab0786e17d1db0a92042b22d1fb86c77efcf8a55f25bda450",
  "settings": {
    "is_hidden": false
  }
}
```

`AddZeroed` and `InsertZeroed` work similarly, except they also zero the bytes of the added/inserted space:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "struct S\n\t{\n\t\tS(int32 InInt, void* InPtr, float InFlt)\n\t\t\t: Int(InInt)\n\t\t\t, Ptr(InPtr)\n\t\t\t, Flt(InFlt)\n\t\t{\n\t\t}\n\t\tint32 Int;\n\t\tvoid* Ptr;\n",
  "lines_of_code": 15,
  "id": 98025,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAyNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--37b463d0e3fd058c8caaf038def711dbc419c473b4014f4555abd873368b623a",
  "settings": {
    "is_hidden": false
  }
}
```

There are also `SetNumUninitialized` and `SetNumZeroed` functions which work like `SetNum` except that, in the case where the new number is greater than the current one, the space for the new elements will be left uninitialized or bitwise-zeroed respectively. As with the `AddUninitialized` and `InsertUninitialized` functions, you should ensure that, if necessary, new elements are properly constructed into the new space if they need to be:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "SArr.SetNumUninitialized(3);\n\tnew ((void*)(SArr.GetData() + 1)) S(5, (void*)0x12345678, 3.14);\n\tnew ((void*)(SArr.GetData() + 2)) S(2, (void*)0x87654321, 2.72);\n\t// SArr == [\n\t//   { Int: 0, Ptr: nullptr,    Flt: 0.0f  },\n\t//   { Int: 5, Ptr: 0x12345678, Flt: 3.14f },\n\t//   { Int: 2, Ptr: 0x87654321, Flt: 2.72f }\n\t// ]\n\n\tSArr.SetNumZeroed(5);\n",
  "lines_of_code": 17,
  "id": 98026,
  "url_signature": "eyJzbmlwcGV0X2lkIjo5ODAyNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjU0KzAwOjAwIn0=--805f001cdb04ddc1869d687c0ca5f6707716a1c8f5732e4de5024d79aebcb85b",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Use the \"Uninitialized\" and \"Zeroed\" families of functions carefully. If an element type includes a member that needs construction, or that doesn't have a valid bitwise-zeroed state, it can result in invalid array elements and undefined behavior. These functions are most useful on arrays of types that will likely never change, like FMatrix or FVector.",
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

The `BulkSerialize` function is a serialization function that can be used as an alternative `operator<<` in order to serialize the array as a block of raw bytes, rather than doing per-element serialization. This can improve performance with trivial elements, like a built-in type or a plain data struct.

The `CountBytes` and `GetAllocatedSize` functions are used to estimate how much memory is currently being utilized by the array. `CountBytes` takes an `FArchive`, while `GetAllocatedSize` can be called directly. These functions are typically used for stats reporting.

The `Swap` and `SwapMemory` functions both take two indices and will swap the value of the elements at those indices. They are equivalent except that `Swap` does some extra error checking on the indices and will assert if the indices are out of range.
