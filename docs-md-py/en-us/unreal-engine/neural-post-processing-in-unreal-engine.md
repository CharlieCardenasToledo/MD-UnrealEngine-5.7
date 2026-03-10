# Neural Post Processing

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/neural-post-processing-in-unreal-engine

> Application Version: 5.7

**Neural Post Processing** is a user-friendly way to use neural networks in the post processing pipeline. You can use the material editor to setup Post Process Materials that utilize neural networks without writing any code.

## Enabling Neural Post Processing

Before you can begin, you must first enable the **Neural Rendering** plugin in your project. You can do so from the **Plugins** browser located in the main menu under **Edit**. This plugin contains all the necessary code to run the network based on the neural profile and the neural buffer / texture set by the material editor.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9632e8e-0c12-4faa-b9d4-901e7e521379/npp-pluginbrowser.png)

## Setting up a Neural Post Processing Material

Follow the sections below to import and set up an ONNX format neural network, and create a Post Process Material that can use this neural network.

### Setting up the Neural Network Profile

Follow these steps to import and set up a compatible neural network model in Unreal Engine.

1. Import an **ONNX (\*.onnx)** machine learning model file into Unreal Engine to create a **NNE Model Data** asset.
2. In the Content Browser, use the **Add (+)** menu to create a **Neural Profile** asset. You can add one from the **Material > Profiles** rollout menu.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5e0c019-e8d3-417e-8a4b-3d05a571a289/npp-addneuralprofile.png)
3. Open the newly created **Neural Profile** asset.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9690425-34e0-4597-9ec4-15dd4a9144d0/npp-neuralprofileasseteditor.png)
4. Use the NNE Model Data assignment slot to set the NNE Model Data asset created when you imported your ONNX file.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19bb0787-eeb6-4385-9f23-269b8e314eb9/npp-neuralprofile-nnemodeldataslot.png)

### Creating the Post Process Material

Follow these steps to set up a Post Process Material that uses the Neural Profile with some graph logic.

1. In the Content Browser, create a new **Material** and open it.
2. In the Material Editor, use the **Details** panel to set the following:

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f19e9962-c1b2-46e2-8749-00d2a8176702/npp-materialsettings.png)
   * **Material Domain:** Post Process
   * **Used with Neural Networks:** Checked
   * **Neural Profile:** Neural Profile asset.
3. In the Material Graph, prepare the input to the network using the **Neural Input** node, and get the output from the network through the **Neural Output** node. Once connected to the **Emissive Color** pin of the main material node so that you have something that looks like this:

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d5d416b-bb2c-4608-95e7-10f43eaea375/npp-materialgraph.png)
4. Click **Apply** in the Material Editor toolbar.

With this setup, the material can pre-process and post-process the data using all available nodes in the material editor. This example applies a simple gamma correction of 1/2.2 and scales the value range from 0 ~ 1 to 0 ~ 255 for the input, and reverses it back for the display after getting the output from the neural output. Scaling is not always required. It depends on the neural network model input and output range. If the model input and output is in range 0 ~ 1, we have a simpler setup as below:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56b3023b-22db-444c-8752-a9b2f5c32b4f/npp-exampematerial1.png)

Below is an example taking this further to apply custom regions to use a default light material as a mask.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c812421-64a7-48e9-86e8-3ae39cb6a52f/npp-examplematerial2.png)

This setup can create results like the following:

![Basic Scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/989f78b3-828c-4ff6-b7c2-f4093f90e215/npp-examplescene1.png)

![Scene with Neural Post Process Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56246ef2-b313-46fd-bcd2-1d4e7e21c8af/npp-examplescene2.png)

## Neural Profile Asset Settings

The neural profile is used to bind with neural networks, specify the runtime, batch size and tile configuration.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d5ec91a-eb98-4947-91d6-1d5612a26304/npp-neuralprofileasseteditor1.png)
