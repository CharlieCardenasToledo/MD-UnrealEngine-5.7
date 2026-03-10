# Using Mobile Service Leaderboards

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-mobile-service-leaderboards-in-unreal-engine-projects-for-mobile-devices

> Application Version: 5.7

Leaderboards enable you to track and display high scores for players on a per-platform basis. This lets players compete for bragging rights and helps to build community.

![iOS Game Center](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ef61503-8472-42d7-a424-2074e9852504/iosleaderboard.png)

![Google Play](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e649bc0f-bfc8-449a-a7ef-113d2fe836db/androidleaderboard.png)

## Configuration

See the appropriate platform-specific page below for details on configuring leaderboards for each platform:

* [Using Google Play Services Leaderboards](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-google-play-services-leaderboards-in-unreal-engine-projects)

## Reading from a Leaderboard

The **Read Leaderboard Integer** node will request from the platform's game service (currently iOS Game Center, or Google Play Services), the value stored on the given **Stat Name** for the provided **Player Controller**.

Note that it is a **latent** node, and thusly has a number of execution output pins. The top most is a "pass through," that works like any other execution output pin. The other two pins (**On Success**, and **On Failure**) will execute when the online service returns (or fails to return) a value. The value of **Leaderboard Value** before a successful return (or if the service fails to get a response) will be `0`.

**In Blueprints:**

The example below is from the **Global Game Instance** Blueprint in the Unreal Match 3 sample game. In these few nodes we're calling the **Read Leaderboard Integer** node for the Player Controller at Player Index 0 on the Stat Name (Leaderboard) "Match3HighScore":

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36c3ccc9-52e7-44fe-b2e6-4570fbb9e93f/readleaderboard.png)
