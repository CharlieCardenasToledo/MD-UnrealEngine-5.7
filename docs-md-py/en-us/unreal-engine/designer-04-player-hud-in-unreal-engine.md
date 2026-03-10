# Player HUD

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-04-player-hud-in-unreal-engine

> Application Version: 5.7

A game’s user interface (UI) is anything the player interacts with visually, like menus, pause screens, inventory, dialogue boxes, and the player’s heads-up display, or HUD. The HUD is any part of the UI that stays visible on screen during gameplay, like the player’s health, equipment, or objective indicators.

Now that your character can pick up items, you’ll learn how to use Unreal Engine’s UMG (Unreal Motion Graphics) system to build a HUD that shows the player what keys they have picked up. With UMG, you can design a HUD by dragging and arranging UI elements in a visual editor, so you’ll know exactly what the player will see in game.

![Image](https://dev.epicgames.com/community/api/documentation/image/f1e37e5f-e22d-4a30-bd00-afd03a1bd113)

## Before You Begin

Make sure you understand these topics covered in previous sections of [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine):

- Blueprint basics like variables, functions, event graphs, and adding nodes.

You’ll need the following assets from [Create a Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine):

- `BP_Key` Blueprint Class
- `BP_AdventureCharacter` Blueprint Class
- `Enum_KeyType` Enumeration

## Create a Widget Blueprint

UMG includes a special type of blueprint called a Widget that you’ll use to build various UI elements. To start building your HUD, create a new **Widget Blueprint** asset.

To create a new widget blueprint, do the following:

1. In the **Content Browser**, go to C**ontent > AdventureGame > Designer > Blueprints**, and create a folder named `Widgets` to store your UI assets. ![Image](https://dev.epicgames.com/community/api/documentation/image/6c67e87c-f5d6-4c59-a316-cc43696df924)
2. In the new **Widgets** folder, create a new asset by right-clicking an empty area in the folder and selecting **User Interface > Widget Blueprint**. ![Image](https://dev.epicgames.com/community/api/documentation/image/2c613ea7-ae6d-4b39-a1c0-a68eb7b12a5c)
3. In the **Pick Parent Class** window, click **User Widget**. ![Image](https://dev.epicgames.com/community/api/documentation/image/ef0223c0-f3bc-4bf1-a568-e93caeed3320)
4. Enter a name for your widget. This tutorial uses `WBP_PlayerHUD`.
5. Double-click the blueprint to open it.

## Explore the Widget Blueprint Editor

Widget Blueprints open in a special widget editor that has two modes: **Designer** and **Graph**. To switch between modes, use the buttons near the top-right corner of the editor.

![Image](https://dev.epicgames.com/community/api/documentation/image/468dc93a-b335-4ff5-a4f1-49d43904dab2)

In **Designer** mode, you can add and edit individual parts of your UI.

On the left side of the widget editor, the **Palette** contains all the different widget types you can add to your UI. The **Hierarchy** panel shows the structure of your UI components. The order and nesting of widgets in this panel affects the layout and rendering of your UI.

The grid in the middle of the window is the **visual designer**. Just like in your blueprint event graphs, use the mouse scroll wheel to zoom in and out, and use the right mouse button to pan around your design.

The zoom level in the top-left corner of the grid updates as you zoom in or out. **Zoom 1:1** means you’re viewing your UI at 100% scale, showing how your UI elements will appear in-game on a screen of that resolution. If a player runs your game on a smaller screen, Unreal Engine uses **DPI scaling** to scale your UI to fit that screen.

The bottom-left corner of the grid contains information about the current screen size preset. This is the screen size your widget blueprint is previewing. By default, it’s set to a 720p television screen.

## Start With a Canvas Panel

In the **Palette** tab, widgets are sorted by type. **Panel**-type widgets don’t display anything on-screen; they are like containers that control the layout and positioning of widgets placed inside them. Panels are useful for automatically scaling the UI to fit different TV screen sizes and monitor resolutions.

**Canvas** panels are the most flexible type of panel widget and are perfect for HUDs. While other panels arrange widgets in a certain layout or orientation, canvas panels use anchors to place widgets exactly where you want them on the screen, ensuring everything stays in place if the screen changes size.

To create a Canvas Panel, follow these steps:

1. In the **Palette** tab, search for `Canvas`, and drag a **Canvas Panel** into the **Hierarchy** panel on top of **[WBP\_PlayerHUD]** so it becomes nested underneath. ![Image](https://dev.epicgames.com/community/api/documentation/image/0ac60072-20b8-4719-8b2a-a5b0540b79ad) A rectangle appears in the visual designer area in the middle of the window.

This canvas is the UI’s **root widget**. Every widget blueprint must have one root widget, the top-level UI element that holds all other widgets. When you place another widget inside the canvas, there’s a hierarchical relationship between the two where the canvas is the parent and the other widget is a child.

By default, a canvas panel is 1920x1080 pixels and represents the entire screen. This is a common resolution and a great starting point to work with, so keep this canvas size. At runtime, Unreal Engine scales the UI to fit the player’s screen.

## Build the Layout for Your HUD

Now that you have a canvas, you’ll anchor areas for player health and inventory to the top-left corner of the UI.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When a person looks at a screen, they tend to look near the top-left corner first, so this is the best place for critical information such as player health.",
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

To define the areas for text on the canvas, follow these steps:

1. In the **Palette**, search for `Overlay`, and drag an **Overlay** panel into the Hierarchy so it’s nested as a child widget under the **Canvas Panel**. ![Image](https://dev.epicgames.com/community/api/documentation/image/d51dc432-b217-41e6-b6f9-e4892653d64f) Overlays are a type of panel that layers multiple widgets on top of each other in the same space. They are useful for adding a background image behind UI elements, or a static icon or text label on top of UI elements. For this HUD, you’ll layer a blur effect behind the UI text so it’s easier to read.
2. Select the new **Overlay**. This panel is a child of the canvas, so it gets an anchor point in the top-left corner of the canvas. ![Image](https://dev.epicgames.com/community/api/documentation/image/8ca6ad85-a83f-42d3-8314-de3cac334d7d) ![Image](https://dev.epicgames.com/community/api/documentation/image/317bb5aa-d861-424a-8d7b-c88413b784a4)
3. In the **Details** panel, set the **Position X** and **Position Y** to `20`. This is the number of pixels the overlay panel is positioned away from the anchor. Adding an offset improves the UI’s look and prevents text from being cut off the edge of the screen.
4. To define the area you’ll draw your UI text in, drag the handles on the overlay panel’s bounding box to resize it until it’s about 250 pixels wide and 200 pixels tall. Or, in the **Details** panel, use **Size X** and **Size Y** to resize the panel. ![Image](https://dev.epicgames.com/community/api/documentation/image/9ce8bb49-0fec-4ba4-9d11-6b7bb46e2abf) This area will display the player’s health (HP) and names of the keys they’ve collected.
5. In the **Palette**, search for and drag a **Vertical Box** panel to be a child under the **Overlay**. This type of panel arranges UI elements inside it vertically, like in a column of a table.
6. Add two **Horizontal Box** panels as children of the **Vertical Box**. Horizontal boxes arrange any UI elements inside it horizontally, like in a row of a table. One horizontal box is a container for the player’s health information and the other horizontal box is a container for a Keys Collected label. ![Image](https://dev.epicgames.com/community/api/documentation/image/263456bf-bdfe-4c9e-b049-c07c72c61e98)

Vertical and horizontal boxes are layout widgets. These panels are like invisible organizers — they don’t have a visible frame in the designer and automatically resize themselves to fit their contents.

Each type of box aligns and organizes the text you’ll add to the UI:

- The Overlay panel enables overlapping, so the vertical box forces the horizontal boxes to align vertically instead of stacking on top of each other.
- You’ll have two text boxes in the first row, so by adding Horizontal Boxes, you can control the alignment and spacing of each text box in the row.

## Add Text Labels

Now that you’ve defined the HUD’s structure, you can add the static text that won’t change based on what happens in the game.

You’ll need an `HP` label before the player’s health and a `Keys Collected` label before the list of key names. For now, you’ll also add placeholder text for the player’s current HP value. In a later section of this tutorial series, you’ll change this placeholder to a variable to reflect the player’s real health.

To add text labels for the player’s health (HP), follow these steps:

1. In the **Palette**, search for `text`, and drag two Text widgets into the **Hierarchy** as children of the first **Horizontal Box**. ![Image](https://dev.epicgames.com/community/api/documentation/image/a911ef9a-8233-4d81-acb5-2f9284a11005)
2. Select the first **Text** widget under the **Horizontal Box**. In the **Details** panel, in the **Slot (Horizontal Box Slot)** section, set the **Padding** to `5`. This sets the text 5 pixels in from the edge of the horizontal box. ![Image](https://dev.epicgames.com/community/api/documentation/image/cf2c7155-093b-465f-a7d1-18fb2dcc5cdf)
3. In the **Content** section, set the **Text** to `HP :`. ![Image](https://dev.epicgames.com/community/api/documentation/image/8b59c769-f881-4708-9d92-52c8c68ba256)
4. In the **Appearance** section, click the color swatch next to **Color and Opacity**, and pick a color for your text. This tutorial uses green (**Hex sRGB** = `78FF3FFF`). ![Image](https://dev.epicgames.com/community/api/documentation/image/7da5d9b6-803f-4582-94af-6d5f156ebdb0)
5. Select the second **Text** widget. At the top of the **Details** panel, rename the widget from `TextBlock` to `txtHP`. In future parts of this tutorial, you’ll need to refer to this widget, so give it a unique and descriptive variable name now. ![Image](https://dev.epicgames.com/community/api/documentation/image/2d20d0fa-24f2-404a-bb3f-de89d07384d9)
6. Change the **Padding** to `5` and the **Text** to `100`. ![Image](https://dev.epicgames.com/community/api/documentation/image/f4598387-9f2b-491e-95a6-5190bf10b465)

To add a text label for the keys the player has collected, follow these steps:

1. In the **Palette**, drag a **Text** widget to become a child of the second **Horizontal Box**.
2. Change its **Padding** to `5` and the **Text** to `Keys Collected :`.
3. For `Color and Opacity`, pick a color. This tutorial uses orange (**Hex sRGB** = `FF6200FF`).

Now that there’s some text in each horizontal box, you can see the flexible structure of this layout. If you select a horizontal box or text widget, arrow buttons appear on the edges of that widget. Click the arrows to reorganize the widgets. By using each text widget’s alignment and padding options, you have a lot of control over the spacing between elements in the same row and across different rows.

![Image](https://dev.epicgames.com/community/api/documentation/image/bb60f3db-bcc5-45d1-9b09-fe7061a93235)

## Add Space for a Variable

In a game, most of the player’s HUD needs to update during gameplay because of the actions you take, such as taking damage, receiving or using items, or getting a power up. To do this in your project, you’ll connect the HUD to a variable that tracks the player’s keys, so it can update as the player collects them.

To add an input text box for displaying the list of keys, follow these steps:

1. In the **Palette**, search for and drag a **Text Box (Multi-Line)** to become the last child of the **Vertical Box**. This input widget takes multiple lines of user-entered text. However, you can use event graph logic to add text to this widget when the user collects a key. ![Image](https://dev.epicgames.com/community/api/documentation/image/ac8688ce-62a5-4cfa-9288-f92e16420ab6)
2. In the **Hierarchy**, select the textbox. In the **Details** panel, rename it `txtKeys`. ![Image](https://dev.epicgames.com/community/api/documentation/image/e563d57d-a4bb-4ad7-9025-95b77153a5e9)
3. In the visual designer, you’ll see the input textbox comes with a default background, so remove it: Near the top of the **Details** panel, expand **Padding** and set the following values to pad the text box with an indent: Left: `15` **Top**, **Right**, and **Bottom**: `4` ![Image](https://dev.epicgames.com/community/api/documentation/image/768673aa-42aa-47c1-92d5-03bb8727b1df) In the **Style** section, expand **Style > Background Image Normal**, and click the color swatch next to **Tint**. ![Image](https://dev.epicgames.com/community/api/documentation/image/a414685c-5bdb-4a02-a996-b3c86ac3a249) Change **Hex sRGB** to `FFFFFF00` to make the background transparent, then click OK. ![Image](https://dev.epicgames.com/community/api/documentation/image/f119835e-ab02-4445-b55c-aafaa52d52e9)
4. This widget doesn’t come with a default font style, so you’ll need to set the font properties yourself. In the Style section, expand Text Style > Font, and set the following: Change **Font Family** to **Roboto**. Change **Typeface** to **Bold**. Change **Size** to `24`. Change the **Color** to white. ![Image](https://dev.epicgames.com/community/api/documentation/image/b1785704-da77-4a88-bcf3-6150290f8b5d)

With **txtKeys** selected, at the top of the **Details** panel, you’ll see **Is Variable** is enabled. Textboxes expect user-entered text, so they’re automatically set up as variables. With **Is Variable** enabled, you’ll be able to reference and use **txtKeys** in your widget blueprint’s event graph.

![Image](https://dev.epicgames.com/community/api/documentation/image/046991ae-9177-4535-8972-5b4f5b4b68f1)

## Layer in a Special Effect

You can make your HUD text easier to read by blurring the background of the overlay’s bounding box. Use the layering feature of the overlay panel to place a blur effect behind the vertical and horizontal boxes.

To use a widget to blur the area of the screen behind your HUD text, follow these steps:

1. In the **Palette**, search for `blur`, and drag a **Background Blur** widget into the **Hierarchy** as a child of the **Overlay**.
2. The editor adds the **Background Blur** to the bottom of the list, so drag it to be the first child under the **Overlay**, above the **Vertical Box**. ![Image](https://dev.epicgames.com/community/api/documentation/image/9d16a11a-abfa-428c-bb1e-e23be9306c11)
3. In the Details panel, in the Appearance section, set the Blur Strength to `2`.
4. Make the effect fill the overlay widget’s dimensions: In the **Slot (Overlay Slot)** section, next to **Horizontal Alignment**, click **Fill Horizontally**. Next to **Vertical Alignment**, select **Fill Vertically**. ![Image](https://dev.epicgames.com/community/api/documentation/image/2a030410-0504-47f1-81a9-02717cc57e6e)

Here’s an example of how the UI text appears without a blurred background and with an exaggerated blur effect:

![Image](https://dev.epicgames.com/community/api/documentation/image/49149c0c-0e45-4481-9fa7-a341847025aa)

## Build the HUD’s Logic

To finish your widget blueprint, you’ll build the logic that displays the name of any key the player picks up.

### Set Up Building Blocks for Key Pickups

Before you can start building the logic that adds key names to the HUD, you’ll need:

- An array variable that tracks the player’s keys.
- A function that your character’s blueprint can call when the player finds a new key.

To trigger the execution of the HUD’s logic from other blueprints, you’ll use a function instead of the event graph. The function will take the key the player has collected, save it in the named variable, and enter the names of the keys in that variable into the txtKeys box.

To add a new variable and function that tracks the player’s keys, follow these steps:

1. Near the top-right corner of the window, click **Graph** to edit the widget blueprint’s event graph. This graph functions the same as the other blueprints you’ve been working on so far. ![Image](https://dev.epicgames.com/community/api/documentation/image/9a90d4ca-8609-498e-be83-b4a33fa491fe) Your `txtKeys` variable is listed in the panel on the left side of the window.
2. Create a function that will execute all HUD logic when called: In the **Functions** section, click the **plus (+)**button to add a function. A new tab for that function appears above the graph. Name the function `fnAddKeyHUD`. With the function selected, in the **Details** panel, in the **Inputs** section, click **+** to add a new function input. ![Image](https://dev.epicgames.com/community/api/documentation/image/0682985d-5d19-4990-8937-31b7a8c9d9b5) Name the input `KeyType` and change its type to **Enum Key Type**. ![Image](https://dev.epicgames.com/community/api/documentation/image/f4a2f814-2b5d-4bce-bd6a-f3953a2296b0)
3. In the **My Blueprint** panel, create an array variable to store the player’s keys: In the **Variables** section, click **+** to create a new variable. Name the variable `KeysToDisplay`. Change its type to **Enum Key Type**. This is the enum you made with Red, Yellow, and Blue key type options. Right-click the variable type to turn it into an array. Or, use the **Details** panel to change its container type. ![Image](https://dev.epicgames.com/community/api/documentation/image/587483f9-c846-4c89-b290-1d8667bb2faf)
4. To print the key names in the multi-line textbox, you’ll need to combine them all in a string. In the **Local Variables** section, click the **+** button to add a new variable. Name it `Keys` and change its type to **String** and its container type to **Single**. ![Image](https://dev.epicgames.com/community/api/documentation/image/5cf176c1-92e7-4c63-a153-4472fe9256d9)

### Print the Player’s Keys On Screen

Now you can start adding logic to the **fnAddKeyHUD** function.

When this function is called, it will start with a red, yellow, or blue **KeyType**. You need to add that key type to your **KeysToDisplay** array, add all the keys to your string variable, and then convert that string to text so you can display it on screen.

First, to build the **KeysToDisplay** array, follow these steps:

1. In the widget blueprint’s **Graph** view, make sure you’re viewing the **fnAddKeyHUD** tab.
2. To build the **KeysToDisplay** array, add an **Add Unique** node after the function entry node.
3. For its **Target Array**, connect a reference to the **KeysToDisplay** variable.
4. For its second input, connect the **Key Type** function input. ![Image](https://dev.epicgames.com/community/api/documentation/image/7b1a8c62-1303-4e70-be51-806a82f71a0b) The **Add Unique** node takes an array and a new value and adds that value to the array (if it’s not already in the array). This node ensures that key names won’t appear on the HUD more than once.

To combine all collected keys into the Keys string, follow these steps:

1. Loop through each item in the **KeysToDisplay** array. After the **Add Unique** node, add a **For Each Loop** node.
2. Connect another **KeysToDisplay** reference to the loop’s **Array** input. ![Image](https://dev.epicgames.com/community/api/documentation/image/ff22ee94-4783-4d79-91d5-ad07794803c0) For each item (or element) in the array, or each iteration of the loop, you need to convert that element to a string, add it to the Keys string variable, and then add a new line after that key name (like pressing Enter on your keyboard).
3. Right-click in the node graph, search for `Append String`, and add a string-type **Append** node. This combines string inputs together to form a single string return value.
4. Set up the **Append** node to take the current contents of the **Keys** variable, add the new array element, and then add a line break: For its **A** input, connect a reference to **Keys**. For its **B** input, connect the loop node’s **Array Element** pin. Unreal Engine adds an **Enum to String** node to convert the value. Click **Add pin** to add a **C** input. Click into the textbox and press **Shift + Enter** to add a new line. ![Image](https://dev.epicgames.com/community/api/documentation/image/0b755528-28e0-4a16-81d0-f801971fbe2a)
5. Drag off the **Append** node’s **Return Value** pin and add a **Set Keys** node.
6. Connect the loop’s execution output pin to the **Set Keys** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/d3bd7069-729c-49d3-a855-da13c095469e)

When the loop body completes, you’ll have one long string with the names of all the player’s keys.

To pass the **Keys** string to the HUD’s **TxtKeys** text box, follow these steps:

1. Drag off the loop’s **Completed** execution pin and add a **SetText (Multi-Line Text Box)** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/56ac361b-445b-4dc9-aebd-4a79f60ac9d7) The **SetText** node takes text-type input and displays it in a target text box.
2. Set up the **SetText (Multi-Line Text Box**) node: For the **Target**, connect a reference to **TxtKeys**. For the **In Text**, connect a reference to **Keys**. Unreal Engine adds a **To Text (String)** node that converts the **Keys** string to text. ![Image](https://dev.epicgames.com/community/api/documentation/image/c5c72afa-d181-46f2-990d-92e225591aa3)
3. **Compile** and **Save** your blueprint.

Your complete **fnAddKeyHUD** function should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "blueprint",
  "title": "",
  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_FunctionEntry Name=&quot;K2Node_FunctionEntry_0&quot; ExportPath=&quot;/Script/BlueprintGraph.K2Node_FunctionEntry&#39;/Game/AdventureGame/Designer/Blueprints/Widgets/WBP_PlayerHUD.WBP_PlayerHUD:fnAddKeyHUD.K2Node_FunctionEntry_0&#39;&quot;\n   LocalVariables(0)=(VarName=&quot;Keys&quot;,VarGuid=7CFB4DE2472FB89562B43DA4067A4B19,VarType=(PinCategory=&quot;string&quot;),FriendlyName=&quot;Keys&quot;,Category=NSLOCTEXT(&quot;KismetSchema&quot;, &quot;Default&quot;, &quot;Default&quot;),PropertyFlags=5)\n   ExtraFlags=201457664\n   FunctionReference=(MemberName=&quot;fnAddKeyHUD&quot;)\n   bIsEditable=True\n   NodePosX=-144\n   NodeGuid=4ECB65CA4D6AC7845C07B58BCAA0CC3E\n   CustomProperties Pin (PinId=0E4F48E14D945C747BB3B7BB32B106B5,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallArrayFunction_0 947B29634A44E616483F9094D92CE754,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n   CustomProperties Pin (PinId=CFE8C37F434814AB5DE2B5BE3C41BBB1,PinName=&quot;Key Type&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;byte&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=&quot;/Script/Engine.UserDefinedEnum&#39;/Game/AdventureGame/Designer/Blueprints/Core/Enum_KeyType.Enum_KeyType&#39;&quot;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;NewEnumerator0&quot;,AutogeneratedDefaultValue=&quot;NewEnumerator0&quot;,LinkedTo=(K2Node_Knot_0 08C2243645687F98862A67B2DD49127F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n   CustomProperties UserDefinedPin (PinName=&quot;Key Type&quot;,PinType=(PinCategory=&quot;byte&quot;,PinSubCategoryObject=&quot;/Script/Engine.UserDefinedEnum&#39;/Game/AdventureGame/Designer/Blueprints/Core/Enum_KeyType.Enum_KeyType&#39;&quot;),DesiredPinDirection=EGPD_Output,PinDefaultValue=&quot;NewEnumerator0&quot;)\n",
  "lines_of_code": 192,
  "id": 150054,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTAwNTQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyNTo1OCswMDowMCJ9--0c83664b959bf66d3cc7d79c7b23c2d9ee4cf1aa60b87cfe52fcae00a045c533",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you copy this snippet into your project, you need to connect the function entry node’s pins to the <b>Add Unique</b> node.",
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

Your HUD is ready to go! Now you need to add it to your player character so that it displays on screen when you start the game.

## Update the Player Character

To finish setting up your HUD, you need to add logic to your character blueprint that adds the HUD widget when the game begins, and updates it when the player picks up a key.

### Call FnAddKeyHUD from the Character Blueprint

Connect the key logic in `BP_AdventureCharacter` to the HUD’s logic so that adding a key to the player also adds a key to the HUD.

To trigger the HUD when the player gets a key, follow these steps:

1. Open your `BP_AdventureCharacter` blueprint. In the **My Blueprint** panel, in the **Variables** section, click **+** to add a new variable.
2. Name the variable `HUD` and change the type to **WBP Player HUD (Object Reference)**. ![Image](https://dev.epicgames.com/community/api/documentation/image/6abe094a-522b-433c-9bee-f7cd0c618ebb) This stores the HUD widget you’ll create in the character’s event graph.
3. Go to the section of the Event Graph where **Event fnBPIAddKey** adds a new key to the player’s **HeldKeys** array. ![Image](https://dev.epicgames.com/community/api/documentation/image/87d9f9c7-faf3-4ed0-bb14-467b2fd90341)
4. After the **Add** node, connect an **FnAddKeyHUD** node.
5. Set up the **FnAddKeyHUD** node: For the **Target**, connect a reference to the **HUD** variable. For **Key Type**, connect the pin to the **Event fnBPIAddKey** node’s **Key Type** pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/66f6f8f6-a2aa-43c9-9362-d05dad14336a) Now, this takes the player’s new key and calls the **FnAddKeyHUD** function in the HUD widget blueprint.
6. **Save** and **Compile** your blueprint.

### Display the HUD When the Game Starts

To create a HUD when the player spawns in the level, follow these steps:

1. Find an empty space in your character’s event graph and add an **Event Possessed** node. This is the event that broadcasts when the player takes control of, or possesses, the player character.
2. Right-click the **Event Possessed** node and select **Add Call To Parent Function** to ensure the **Event Possessed** logic in the parent character class still executes. Connect each node’s **exec** and **New Controller** pins. ![Image](https://dev.epicgames.com/community/api/documentation/image/44fde19c-760f-4b34-b7a6-04344faacd12)
3. To create the HUD, connect a **Create Widget** node, and change its **Class** to **WBP Player HUD**. This creates an instance of your widget blueprint.
4. After the **Create Widget** node, add a **Set HUD** node, connecting both pins. This saves the new widget blueprint to your variable. ![Image](https://dev.epicgames.com/community/api/documentation/image/4ce1a9cb-2265-417e-b872-f3fbf7f4eab5)
5. To display the HUD object on the screen, add an **Add to Viewport** node. Set its **Target** to your **HUD** variable. ![Image](https://dev.epicgames.com/community/api/documentation/image/70e9eb5e-2f71-49bc-9137-77da7123a754)
6. **Compile** and **Save**.

Your new character blueprint logic should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "blueprint",
  "title": "",
  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_Event Name=&quot;K2Node_Event_1&quot; ExportPath=&quot;/Script/BlueprintGraph.K2Node_Event&#39;/Game/AdventureGame/Designer/Blueprints/Characters/BP_AdventureCharacter.BP_AdventureCharacter:EventGraph.K2Node_Event_1&#39;&quot;\n   EventReference=(MemberParent=&quot;/Script/Engine.BlueprintGeneratedClass&#39;/Game/AdventureGame/Designer/Blueprints/Core/BPI_PlayerKeys.BPI_PlayerKeys_C&#39;&quot;,MemberName=&quot;fnBPIAddKey&quot;,MemberGuid=5DDCBD08481325B5AB238394857DBDAF)\n   bOverrideFunction=True\n   NodePosX=-160\n   NodePosY=-1120\n   NodeGuid=EF46CB6E430961CF70F537BA672FB989\n   CustomProperties Pin (PinId=9BA72DAC4678F98FDD59039F467E3E64,PinName=&quot;OutputDelegate&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;delegate&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/Engine.BlueprintGeneratedClass&#39;/Game/AdventureGame/Designer/Blueprints/Core/BPI_PlayerKeys.BPI_PlayerKeys_C&#39;&quot;,MemberName=&quot;fnBPIAddKey&quot;,MemberGuid=5DDCBD08481325B5AB238394857DBDAF),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n   CustomProperties Pin (PinId=7BD469F64A8C918E8B4573908669C6F2,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallArrayFunction_1 D6AC984149E8867DA63F7A84ED1EA506,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n   CustomProperties Pin (PinId=F18AD5E443622BDDF51B9EBA89FC7256,PinName=&quot;Key Type&quot;,PinToolTip=&quot;Key Type\\nEnum_KeyType Enum&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;byte&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=&quot;/Script/Engine.UserDefinedEnum&#39;/Game/AdventureGame/Designer/Blueprints/Core/Enum_KeyType.Enum_KeyType&#39;&quot;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;NewEnumerator0&quot;,LinkedTo=(K2Node_Knot_9 453D81D14171C65AAA2370A7E293E707,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\nEnd Object\n",
  "lines_of_code": 130,
  "id": 150055,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTAwNTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzoyNTo1OCswMDowMCJ9--ac109cf89ac20e56335028b05530a0fe7efe86e46415ff511c2f3f9f2b885a0c",
  "settings": {
    "is_hidden": false
  }
}
```

## Test the HUD

Click **Play** to test out your game. When the game begins, you should see the player’s HP and Keys Collected labels displayed on the HUD. Touching a key should add the name of that key to the HUD.

![Image](https://dev.epicgames.com/community/api/documentation/image/7153f9c6-b454-4f4b-88fc-28709fefde94)

Make adjustments to the HUD if you wish. Some things you could try on your own are:

- Adjust the overlay panel’s size.
- Change font sizes and styles.
- Move the placement to other areas than the top-left.
- Add different widgets for backgrounds, such as textures or materials.

To take your HUD further, try experimenting with replacing the text labels with icons. To do this, import an image into the Content Browser and add it to your HUD with an Image widget. For more information about importing assets into Unreal Editor, see [Importing Assets Directly](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-assets-directly-into-unreal-engine).

## Designing Effective HUDs

Here are some more design strategies to create a clean, player-friendly HUD.

**Make It Easy to Read:**

Use high-contrast text, clean fonts, and appropriate font sizes. Ensure your HUD is readable at a typical viewing distance from the screen and when the player is moving through a busy environment, not just while standing still.

**Keep it Clear and Concise:**

Only show what the player needs right now and hide or minimize less relevant information until it’s needed. However, the player should always be able to see what they need at a glance so they can make confident decisions.

**Add Feedback:**

When the HUD updates (like picking up a key), use a short animation, color change, or sound to make the player aware of the change.

**Prioritize with Size and Position:**

Important information should stand out — use bigger text, bold colors, or place this information near the top-left or center where players naturally look first.

## Next Up

In the next section, you’ll keep adding more gameplay elements to your level and learn how to program a switch to perform an action when pressed.

- [Related Document](en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine.md)
