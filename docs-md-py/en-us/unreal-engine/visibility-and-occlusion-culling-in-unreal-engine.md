# Visibility and Occlusion Culling

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine

> Application Version: 5.7

Unreal Engine provides methods of culling for visibility and occlusion. These culling methods are useful for optimizing game performance. Each method works to reduce the number of visible Actors in the Level by setting whether they should be drawn to the screen or not. Some of these methods (such as [View Frustum](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine#viewfrustum) and [Hardware Occlusion Queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine#hardwareocclusionqueries)) can work simultaneously or are better suited to specific devices and platforms (such as [Round Robin Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine#roundrobinocclusionforvr) for virtual reality).

## How Culling Works

To get a sense of what Unreal Engine offers by default without any setup, we'll look specifically at View Frustum culling and Hardware Occlusion Queries.

The general idea of visibility and occlusion culling methods is to reduce the number of visible objects at any given time with the goal of gaining performance.

For example, if we start with only what the camera can see from its position, there are only a handful of objects visible (Scene View). However, we know that is not entirely the case because there are a lot of objects around that make up the scene that just are not visible from this position (Top Down Scene View).

Scene View

Top Down Scene View

The objects outside of the camera's field of view (the view frustum) aren't visible, and can be culled (objects outlined in red).

![Scene View](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3763eb52-9920-4cdb-aa94-227288e65480/sceneviewbase.png)

![Scene View with | View Frustum Culled Objects Removed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/035f4536-c514-4abf-ac47-a7637ffde718/sceneview_viewfrustumculled.png)

Culled objects outside of the camera's view frustum are no longer rendered, leaving only a handful of objects within this view that are occluded by another object that need to be checked for visibility. So, during this pass, a query will be sent to the GPU to test each of these object's visibility state. Those that are occluded by another are culled from view (objects outlined in blue).

![Scene View with | only objects in the View Frustum](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d935140-811d-4d5c-a8d3-6b621649b0cb/sceneviewwithonlyoccludedobjects.png)

![Occluded Objects within | the View Frustum Culled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/270e1d44-45a6-40b7-997e-6556059a53fc/sceneview_occludedobjectsremoved.png)

All objects that are outside of the view frustum or that are occluded are now culled from view. The final scene view now matches the objects we know to be visible in the scene from the camera's position.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae447558-0f06-4b44-a930-73d29fa7f264/vis_finalsceneview.png "Vis_FinalSceneView.png")
