# Full-Body IK

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-full-body-ik-in-unreal-engine

> Application Version: 5.7

Use Control Rig's Full Body Inverse Kinematic (FBIK) feature to construct rigs in Control Rig with a high degree of control and flexibility. The overall solver method is built on a **Position Based IK** framework, which enables faster rig performance, per-bone settings, preferred angles, squash and stretch, and more. FBIK is designed to act as a procedural adjustment tool within Control Rig, such as for ground alignment, or arm reaching behavior.

This document provides an overview of how to create the FBIK node, and its various features.

#### Prerequisites

* FBIK is a node within the [**Control Rig Graph**](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#riggraph), therefore you should have an understanding of the Control Rig Editor.
* You must enable the **FullBodyIK** plugin. To do this, navigate in the Unreal Editor menu bar to **Edit > Plugins** and locate **FullBodyIK**. Ensure the plugin is enabled and restart the editor.

  ![full body ik plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f22d319-df61-431f-b1e7-f3d3c6ea7402/plugin.png)
* You must have created a Control Rig asset for a character and know how to create controls. See the **[Control Rig Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine)** page for information on how to do this.

## Creation and Setup

FBIK is achieved within Control Rig by creating the FBIK node, then assigning bones and effectors to the appropriate pins.

To start, right-click in the Control Rig graph, and in the context menu select **Hierarchy > Full Body IK**. This will create the Full Body IK node. Connect the node to the **[Forwards Solve](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-forwards-solve-and-backwards-solve-in-unreal-engine#forwardssolve)** node.

![create full body ik control rig node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/387734ef-8d2a-46b5-a261-b56195616e30/createnode.png)
