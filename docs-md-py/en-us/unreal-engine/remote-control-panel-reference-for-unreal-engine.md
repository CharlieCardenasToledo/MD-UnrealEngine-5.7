# Remote Control Panel Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-panel-reference-for-unreal-engine

> Application Version: 5.7

This page outlines the interface elements and options contained within the Remote Control Panel. You will learn how to organize the Remote Control Panel, connect external devices, and rename elements for simpler reference in the Remote Control API.

## Remote Control Panel Interface

Click image to expand

1. [Menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-panel-reference-for-unreal-engine#menu)
2. [Exposed Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-panel-reference-for-unreal-engine#exposedproperties)
3. [Remote Control Entity](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-panel-reference-for-unreal-engine#remotecontrolentity)
4. [Remote Control Plugins for DMX, MIDI, and OSC](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-panel-reference-for-unreal-engine#remotecontrolplugins)
5. [Protocol Log](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-panel-reference-for-unreal-engine#protocollog)

## Menu

The following table describes each element as it appears in the Menu, from left to right.

![Menu elements](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e2c14128-31c6-4614-a0d4-d45ce2106032/menu-elements.png)

| UI Element | Description |
| --- | --- |
| **Create Group** | Create multiple groups to organize similar properties and functions together. |
| **Expose** | Add other items to the panel where you want to expose functionality that is not merely a property. The following options are available to expose to the Remote Control API:   * Blueprint Library Function * Subsystem Function * Actor Function * Actor * Actors by Class |
| **Open Web App** | Launches the [Remote Control Web Application](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-web-application-for-unreal-engine) in your browser. |
| **Edit Mode** | When enabled, you can expose properties from the Editor, add functions to the Preset, and modify the groups and positions of the properties and functions. |
| **Enable Log** | Shows the Protocol Log. See [the Protocol Log section](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-panel-reference-for-unreal-engine#protocollog) for more details. |
| **Remote Control Preset Name** | Displays the name of the Remote Control Preset Asset that's currently open. |

## Exposed Properties

The following table describes each element as it appears for each exposed property, from left to right.

![Exposed Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/81431ac4-4c9e-4ebe-ae97-867d5385c38b/exposed-properties.png)

| Action | Description |
| --- | --- |
| **Expand** | (Optional) Shows additional information for the data value, if it exists. |
| **Move** | Rearrange properties, functions, and groups by dragging and dropping the elements in the panel. |
| **Rename** | Change the names of the properties, functions, or groups to make their references clearer and simpler in function calls. |
| **Data Values** | Matches the data format for the property in the Editor. |
| **Reset** | Return the property's value back to its default value. |
| **Remove** | Remove the property or function from the Panel and make it no longer exposed to the Remote Control API. |

## Remote Control Entity

This section appears when you select an exposed property. The following table describes the Metadata that you can associate with each property. Some of the properties might have more fields depending on their data format.

![Remote Control Entity metadata](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09495ec8-d913-486b-aaef-c7b28d868d1a/remote-control-entity-metadata.png)

| Metadata | Description |
| --- | --- |
| **Label** | The unique label for the property that matches the label in the Remote Control Preset. This can be used in the Remote Control API to access an exposed property. |
| **ID** | The engine's unique identifier for the property. This can be used in the Remote Control API to access an exposed property. |
| **FieldName** | The name of the associated field. |
| **Widget** | The default widget type to use for this property in the Remote Control Web Application. |
| **Description** | This field overrides the label that is displayed in the Remote Control Web Application. |

## Remote Control Protocols for DMX, MIDI, and OSC

In the Remote Control Panel, you can map exposed properties to an external device through [DMX](https://dev.epicgames.com/documentation/en-us/unreal-engine/dmx-in-unreal-engine), MIDI, and [OSC](https://dev.epicgames.com/documentation/en-us/unreal-engine/osc-plugin-overview-for-unreal-engine). The table below describes the UI for adding and viewing Protocol Mappings.

![Remote Control protocol mapping user interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac2288f7-3c36-4a74-9f66-6774d83ebfbe/protocol-mapping-ui.png)

| UI Element | Description |
| --- | --- |
| **Protocol Mapping Option** | Options include:   * DMX * MIDI * OSC |
| **Add Protocol** | Creates a new Protocol Mapping for the currently selected option in the Protocol Mapping Option dropdown. |
| **Viewing Options** | Filter which protocol mappings you want to view. |

Each Protocol Mapping also has its own **Mapping** and **Ranges** sections to define which external device and input to connect to. The sections below explain the differences between mappings for Protocol types, and the functionality of ranges shared between the Protocol types.

Use the autobinding button to capture the latest input for the current protocol and apply it to the mapping. This provides a convenient and faster alternative to specifying the properties manually.

For example, in either an existing or newly created MIDI binding, you can toggle autobinding, press a note on the device, and the mapping properties will be populated accordingly. To complete the autobinding and stop recording to any new input, toggle the autobinding button again so that it's no longer red.

The following are the available states for autobinding:
 ***Grey**: Not listening for input* **Red**: Listening for input
\* **Green**: With a bound input

![OSC autobinding settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e7fa4d8-05b7-4cff-95b8-bc23d5a37bee/osc-enable-disable.gif)

### DMX Protocol Mapping

The following table describes the options for connecting to a specific input on an external device with the DMX Protocol.

![DMX protocol mapping options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/70a41bc3-de3f-462a-9a15-a3b8dfac0fd8/dmx-protocol-mapping.png)
