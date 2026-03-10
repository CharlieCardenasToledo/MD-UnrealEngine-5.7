# Precomputed Visibility Volumes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/precomputed-visibility-volumes-in-unreal-engine

> Application Version: 5.7

Like other culling methods, **Precomputed Visibility Volumes** are used for performance optimization for small to medium-sized worlds and typically for Mobile where dynamic occlusion culling is limited depending on hardware. Precomputed Visibility Volumes store the visibility state of Actor's locations in the world based on where the player or camera is. For this reason, precomputed visibility is most useful for projects with mostly statically lit environments, restricted player movement, and somewhat 2D play areas.

Visibility cells are generated during a lighting build above shadow casting geometry. Actor visibility is stored from each cells position. Because precomputed visibility is generated offline, you're trading rendering thread time, normally taken up by hardware occlusion queries, at the cost of increasing runtime memory and lighting build time. With that in mind, it is recommended to only place the volumes in player or camera accessible areas to maintain visibility culling.

![Example Scene View](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b3606ee5-7f94-46cf-a787-5533b13d3843/pvis_visualizationdisabled.png)

![Precomputed Visibility Visualization Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3390ee58-ef4f-48e5-80a9-9e074463d95e/pvis_visualizationenabled.png)

## Setup and Usage

To get started, you'll first need to enable Precomputed Visibility for your Level. Do this by opening the **World Settings** and locate the **Precomputed Visibility** section. Once there, enable the checkbox next to **Precompute Visibility**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5379454d-72c2-4e52-b553-8f7aaffbff45/ws_enablepvis.png "WS_EnablePVIS.png")
