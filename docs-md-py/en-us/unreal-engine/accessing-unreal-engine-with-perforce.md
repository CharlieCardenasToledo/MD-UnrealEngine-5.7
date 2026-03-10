# Accessing Unreal Engine with Perforce

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/accessing-unreal-engine-with-perforce

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

One of the ways Epic Games provides access to Unreal Engine is by making the source code available through a Perforce depot that licensees can connect to in order to download the engine. Since Unreal Engine is updated regularly, as a licensee working on a project, you may choose to update your version of the engine to a newer version at one or more times during the development cycle. From the outset, it's important to accurately set up Perforce so that it can sync and integrate engine builds.

## Required Step

Before continuing, make sure that your company has entered into a [custom licensing agreement](https://www.unrealengine.com/en-US/custom-licensing) with Epic Games. After entering into a custom license support agreement with us, our support staff will set up your account and contact your company’s technical license administrator with information that gets you started with our services.

If you already have a custom license support agreement but do not have Perforce access, you can request access to Epic's Perforce proxy server by reaching out to your Epic Games Business Development representative.  After your access is approved, we will set up your Perforce account, and provide login credentials and onboarding documentation to your technical license administrator.

To connect to the Epic Games Perforce depot, your account needs to be validated through **Okta**. Access to the Perforce repository requires a valid password, but Epic Games' Okta access also requires multi-factor authentication (MFA). The [Epic Games Developer-Access team](mailto:developer-access@unrealengine.com) will help your company’s technical license administrator get your Okta account set up, including providing a temporary password. You will need to update your password once a year at minimum.

## Connecting to Epic Games' Depot

Once your Okta account is established, you will be able to access the depot securely from your location using the Perforce client. The client needs to be installed and configured properly to connect. An overview of the process for installing and connecting with the **P4V Perforce Client** is provided below:

1. Download the client from the [Perforce Software Download Page](http://www.perforce.com/downloads/complete_list).
2. Install the client and run it.
3. Fill in the appropriate **Server** and **User****info** in the **Connection Dialog** and click **OK**.
4. Provide the password you set in Epic Games’ Okta.
5. The client opens and connects to Epic Games's Perforce depot.

Refer to Perforce's [P4V documentation](https://help.perforce.com/helix-core/server-apps/p4v/current/Content/P4V/Home-p4v.html) for more information.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Please note that only one authorized user should log into the Perforce account. <b>Multiple users logging into the same account is a violation of the Perforce terms of service.</b> ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Epic Games's guidance is for a single user or automation to use the account to sync engine builds to your local Perforce depot, and allow your staff access with their own individual Perforce accounts licensed by your company.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "If you don’t already have a Perforce license for your team, it is<a href=\"https://www.perforce.com/products/helix-core/free-version-control\"> free for up to 5 users</a> or you can<a href=\"https://www.perforce.com/how-buy\"> explore licensing options</a>.\n\n",
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

## Syncing from Streams

Epic Games hosts a variety of Perforce streams that you can use to sync to our code. Every development team has one "dev" stream, which provides the most recent code from those teams, and our Quality Assurance (QA) department regularly tests "dev" streams before copying up to the "main" engine stream.

Snapshots of the "main" stream are copied into "release" streams periodically for heavy QA testing and bug-fixing, leading up to an official release. Following a full release, preview release, or hotfix, a snapshot of the "release" stream is used to migrate fixes back to the "main" stream.

When syncing, consider what code you need (for example, do you need the whole engine, just a specific stream, or a cherry-picked feature or fix?), how up-to-date you want the code to be, and what level of stability you require.

The following table describes the four types of streams, provides example stream names, and describes the content, relative age, and stability of each stream type:

| Stream Type | Example Stream Names | Description |
| --- | --- | --- |
| **Main** | //UE5/Main //UE5/Dev-Main | Code in this stream is relatively up-to-date, and has passed through some testing. The "Dev-Main" variant is a virtual stream that excludes some samples. Development streams copy up to, and merge down from, this stream. |
| **Development** | //UE5/Dev-Core //UE5/Dev-Rendering //UE5/Dev-Framework | The source for the most up-to-date work on features relating to a specific area of the engine is the development stream for the team who works on that feature. This code is actively in development and is therefore the least stable type of stream. |
| **Release** | //UE5/Release-5.6.0 //UE5/Release-5.5.4 //UE5/Release-Latest | These streams correspond to Epic's official public releases, and are heavily tested and considered very stable. They will contain the latest revision of the named engine version. The "Release-Latest" stream is virtual and always points to the most recent official release that Epic has shipped. Other than "Release-Latest", these streams can be recognized by their three-part version numbers (such as "Release-5.6.0"). |
| **Release Stabilization** | //UE5/Release-5.6 //UE5/Release-5.5 | When Epic is preparing to release a new version of Unreal Engine 4, a stream will be created from a current snapshot of the main stream. This stream will undergo daily testing and bug-fixing leading up to its public release, so it may be unstable. They can be distinguished from "Release" streams by their two-part version numbers (such as "Release-5.6"). |

### Additional Information

- [Related Document](en-us/unreal-engine/accessing-unreal-engine-with-perforce.md)
