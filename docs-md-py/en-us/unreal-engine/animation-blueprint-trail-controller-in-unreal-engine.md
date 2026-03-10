# Trail Controller

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-trail-controller-in-unreal-engine

> Application Version: 5.7

Using the **Trail Controller** [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) node, you can define a chain of bones to animate based on a delayed replication parent bone motion.

![trail controller skeletal control animaiton blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d796319-4f7f-49fc-892e-2d029fd975cd/trailcontroller.png)

You can use the Trail Controller node to create more realistic trailing motion on your character's auxiliary boned objects, such as tails, capes or accessories.

![trail controller skeletal control animaiton blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8c592bf-e101-47f9-9771-097bd4684336/taildemo.gif)

By defining a bone as the **Trail Bone**, you can select how many bones up the chain from the **Trail Bone** that will be influenced by the Trail Controller node. You can then set constraints on **Stretch**, **Rotation** and even **Planer Limits** on transforms.

## Property Reference

![trail controller skeletal control animaiton blueprint node details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d3d0cfd1-24af-400f-b3ba-7a2df62bb9d1/details.png)

Here you can reference a list of the Trail Controller node's Trail properties.

| Property | Description |
| --- | --- |
| **Trail Bone** | Set the bone at the end of a chain structure to trail the parent bone motion. |
| **Chain Length** | Set the number of bones to influence up the chain from the Trail Bone. |
| **Chain Bone Axis** | Set the axis (**X**, **Y**, or **Z**) to orient the chain points to one another. |
| **Invert Chain Bone Axis** | Set a scale alpha to apply the **Relation Speed Scale Input Processor** properties. A value of 0 will disable the effect, while a value of 1 will fully enable the effect. Values greater than 1 will act as a multiplier. |
| **Trail Relaxation Speed** | Here you can use the **Trail relaxation speed graph** to set a curve to define the behavior at which the transform returns to the animated pose. trail controller trail relaxation speed scale graph details property Using the graph editor in the property's settings, you can edit the beginning and ending point of the graph to control how the behavior of the chains return to the animated pose. Or right click the graph to add a new point on the graph to manipulate the curves position.  The graph's X-axis is ranged from 0 to 1, and it is mapped to the chain of joints. 0 represents the last joint in the chain and 1 represents the closest joint to the **Trail Bone**.  The graph's Y-axis controls the rate at which the delayed motion is passed to the next joint in the chain. Values less than or equal to 0 will prevent joints from continuing to pass the delayed motion. Higher values will pass the delayed motion on quickier. The Y-axis operates as an absolute value to prevent frame dependency. The default range is from 5 to 10 resulting in a faster return from the root joint to the bottom joint. |

### Limit Properties

![trail controller skeletal control animaiton blueprint node details panel limit properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd4c960d-6b15-4af1-8803-39aeaaaf5e35/otherprops.png)
