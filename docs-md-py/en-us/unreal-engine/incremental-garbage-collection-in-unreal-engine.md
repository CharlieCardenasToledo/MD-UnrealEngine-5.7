# Incremental Garbage Collection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/incremental-garbage-collection-in-unreal-engine

> Application Version: 5.7

Unreal Engine (UE) uses a mark-and-sweep garbage collector to manage [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/objects-in-unreal-engine) memory. For soft-real-time applications, garbage collectors have historically had one major drawback; the potential to generate gameplay hitches while the garbage collector determines which objects’ memory can be reclaimed. In UE, this process is called **reachability analysis**. UE relies on this phase of garbage collection to complete within a single frame, which temporarily stops all UObject processing (in particular, gameplay). The more objects reachability analysis has to scan, the longer the pause, which can introduce visible gameplay hitches as a result. There are several ways programmers can avoid hitches, such as:

- Keeping tight UObject budgets.
- Using UObject pools.
- Disabling garbage collection during normal gameplay.

However, these workarounds tend to increase code complexity and overall project costs.

## Incremental Reachability Analysis

UE improves upon this using **incremental reachability analysis**. Users now have the ability to split the garbage collector’s reachability analysis phase across multiple frames with a configurable per-frame, soft time limit. The engine tracks UObject references between reachability iterations through `TObjectPtr` properties. This means that any assignment to a `TObjectPtr`-exposed `UPROPERTY` immediately marks the object as reachable while garbage collection is in progress. This is also known as a garbage collector **write barrier**.

The engine has already been converted to use `TObjectPtr` instead of raw C++ pointers in any place that exposes UObjects to the garbage collector, including any UObject or `FGCObject` `AddReferencedObjects` functions. To use incremental reachability analysis in projects built with Unreal Engine, it’s critical to convert all `UPROPERTY` instances to use `TObjectPtr` instead of raw C++ otherwise garbage collection might reclaim some of UObjects’ memory too early. We are initially releasing this feature as experimental, as it’s still possible that the reachability analysis phase can exceed the specified time limit.

## Enable Incremental Reachability Analysis

Incremental reachability analysis can be enabled with the following console variables when added to your project’s `DefaultEngine.ini`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[ConsoleVariables]\ngc.AllowIncrementalReachability=1 ; enables Incremental Reachability Analysis\ngc.AllowIncrementalGather=1 ; enables Incremental Gather Unreachable Objects\ngc.IncrementalReachabilityTimeLimit=0.002 ; sets the soft time limit to 2ms",
  "lines_of_code": 4,
  "id": 110184,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMTAxODQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMjoxMiswMDowMCJ9--fbe18997a1bbff203c20047147ce7d0a09619e0e9e45ecb73c83cb81ac65479d",
  "settings": {
    "is_hidden": false
  }
}
```

## Additional Console Variables

You can also use console variables for stress-testing and debugging purposes:

| Console Variable | Description | Type |
| --- | --- | --- |
| `gc.DelayReachabilityIteration` | Delay reachability analysis by the specified number of frames. Used for stress-testing the GC barrier. | `<INTEGER>`: Number of Frames (default: 10) |
| `gc.VerifyNoUnreachableObjects` | Run a test after reachability analysis is complete to make sure no reachable (valid) object is referencing an unreachable (soon to be destroyed) object. | 0: disabled, 1: enabled |
| `gc.ContinuousIncrementalGC` | Keep restarting incremental garbage collection after the previous one has completed. | 0: disabled, 1: enabled |

## Performance Comparison

Below is an [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) visualization of a sample project's performance graph with incremental reachability turned off. The blue line represents the total frame time and the orange line shows the time taken up by reachability analysis. Unreal Insights plots a continuous graph line between single events separated by multiple frames; even though it may seem like garbage collection is running throughout the entire timeline, it only actually runs for a single frame at a time.

In the first image of the following graph comparison, you can see a spike each time garbage collection runs (denoted by the **GC** labels at the top of the timeline).

```json
{
  "type": "comparison_slider",
  "image_left_id": 26032039,
  "caption_left": "Without Incremental Reachability",
  "image_right_id": 26032040,
  "caption_right": "With Incremental Reachability",
  "image_left": {
    "id": 26032039,
    "file_name": "without-igc.png",
    "file_size": 29739,
    "content_type": "image/png",
    "created_at": "2025-09-03T16:41:57.499+00:00",
    "height": 254,
    "width": 951,
    "storage_key": "ba2d9034-ca00-42a7-bb3d-1de8a66745fb",
    "context": "documentation"
  },
  "image_right": {
    "id": 26032040,
    "file_name": "with-igc.png",
    "file_size": 32464,
    "content_type": "image/png",
    "created_at": "2025-09-03T16:41:57.729+00:00",
    "height": 263,
    "width": 966,
    "storage_key": "4db3e889-0f33-49aa-84fd-32a1b4a62be4",
    "context": "documentation"
  },
  "image_left_storage_key": "ba2d9034-ca00-42a7-bb3d-1de8a66745fb",
  "image_right_storage_key": "4db3e889-0f33-49aa-84fd-32a1b4a62be4",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

In the second image, with incremental reachability turned on, you can see that the GC lag spikes are gone, and that incremental reachability is now split across multiple frames (represented by the now wider light green bars).

## Known Limitations

Incremental reachability is not fully thread safe. Under some circumstances, an object that is being manipulated on a worker thread will not be marked as reachable while the garbage collector is scanning the UObject graph. This can result in the object being garbage collected prematurely. We recommend enabling incremental reachability in single-threaded builds only (for example, dedicated servers).
