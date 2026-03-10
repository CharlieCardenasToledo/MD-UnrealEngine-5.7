# Setting Up a Perforce Connection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine

> Application Version: 5.7

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Using the content of this page requires a custom license support agreement with Epic Games that includes access to the Unreal Engine P4 Perforce depot.",
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

Epic Games makes QA-approved builds of Unreal Engine, as well as other specialized code drops, available to licensees through a Perforce depot that can be accessed externally. This is one of the methods licensees use to first obtain the engine, as well as update to new versions as they are released and it is deemed appropriate by the licensee. This document covers the steps to set up Perforce locally in order to connect to the Epic Games' Unreal Engine depot and sync to a build of the engine.

## Connectivity Policy

Please note that only one authorized user should log into the Perforce account. Multiple users logging into the same account is a violation of the Perforce terms of service.

Epic Games' guidance is for a single user or automation to use the account to sync engine builds to your local Perforce depot, and allow your staff access with their own individual Perforce accounts licensed by your company.

If you don’t already have a Perforce license for your team, it is [free for up to 5 users](https://www.perforce.com/products/helix-core/free-version-control) or you can [explore licensing options](https://www.perforce.com/how-buy).

The complete process for downloading builds or revisions of Unreal Engine from Epic Games' Perforce depot is detailed on the [Downloading Unreal Engine with Perforce](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce) page.

## Installation and Configuration

### Setting Up P4V

The P4V client is the current client provided by Perforce. It provides access to versioned files through a graphical interface and also includes tools for merging and visualizing code evolution.

![Image](https://dev.epicgames.com/community/api/documentation/image/eab6cfb5-d8aa-479e-8061-a259cb3b6004)

The full P4V installer can be downloaded from the [Perforce Downloads](https://www.perforce.com/downloads) page. Refer to Perforce's [P4V documentation](https://help.perforce.com/helix-core/server-apps/p4v/current/Content/P4V/Home-p4v.html) for instructions on installing and setting up P4V.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Be sure to download the version that applies to your operating system, including 32- or 64-bit.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You must be running a 2017.2 or later version of a Perforce client",
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

### Character Encoding

If you store Unicode files as text in Perforce, it will add in a 0xd to match the local line end; so the Unicode line end 0x0a 0x00 0x0d 0x00 will be converted to 0x0a 0x0d 0x00 0x0d 0x00 and break. However, when it does this, it will leave your local version unchanged (and working). Sync to a previous version and then back to head to see the problem.

Perforce defines UTF-8 as Unicode. UTF-16 is ideal, provided no one accidentally converts to ASCII. Binary also works OK provided you do not miss merging or multiple checkouts.

Unreal Engine will load ASCII or UTF-16 with BOM, provided they are valid files.

### Setting up Perforce for Unreal Engine Distribution

Your team is granted a single account on Epic Games’ Perforce P4 server from which you can download the Unreal Engine source. Follow the instructions below to set up a process for sharing builds with your team.

#### Perform initial setup and import

1. Create your own (local) P4 Server.
2. Create a stream’s depot on that server for importing into, for example: `//UE5`
3. Create a stream for the particular release you are importing from Epic, for example: `//UE5/Release-5.6.0` Do not add any files to this local stream – you will add them below as a separate step.
4. Create a workspace on the Epic Games Perforce P4 Server (see [Downloading Unreal Engine with Perforce](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce)) and sync the data you want. Set the workspace Root folder to something like: `c:\UE5\release-5.6` Note the latest changelist you are syncing to (view the history tab in P4V with the stream selected).
5. Create a new connection in P4V to your own Perforce P4 Server.
6. Create a workspace for your new Stream (`//UE5/Release-5.6.0`)
7. Set the root of the workspace to be the same folder as for your workspace on the Epic Games Perforce P4 server (in this example, `c:\UE\release-5.6`).
8. Right click on the root folder and select **Mark for Add**.
9. Go to the pending changelists folder, and submit the changelist. In the description, note the particular changelist number you synced from the Epic Games server

### Get and Import a New Snapshot from Epic Games

This is a regular process using the workspaces you previously created. It is a modified subset of the steps above, and this workflow assumes you still have your workspaces as previously set up. You will import the latest changes.

1. Connect to the Epic Games Perforce P4 server Select the workspace you previously created. Click **Get Latest** to update the files. Note the latest changelist you synced to.
2. Connect to your local Perforce P4 Server.
3. Select the workspace you previously created.
4. Right click on the root folder and select **Reconcile offline work**.
5. Go to the pending changelists folder, and submit the changelist. In the description, note the particular changelist number you synced from the Epic Games server.

## Support

### Connection Issues

If you are unable to connect to the Perforce depot for any reason, please contact [developer-access@unrealengine.com](mailto:developer-access@unrealengine.com) or post on [Epic Pro Support](https://epicprosupport.epicgames.com/).
