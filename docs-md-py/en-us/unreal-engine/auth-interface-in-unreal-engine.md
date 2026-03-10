# Auth Interface

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/auth-interface-in-unreal-engine

> Application Version: 5.7

The **Online Services Auth Interface** provides an API to authenticate and verify local users with online services. Authentication of a local user returns an account ID, which your project can use to interact with many other online service features.

## API Overview

### Functions

The following table provides a high-level description of the functions included in the Auth Interface.

| Function | Description |
| --- | --- |
| [Login](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/Login?application_version=5.5) | Authenticate a local user. |
| [Logout](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/Logout?application_version=5.5) | Conclude the auth session for a local user. |
| [ModifyAccountAttributes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/ModifyAccountAttributes?application_version=5.5) | Modify attributes associated with an authenticated account. |
| [QueryExternalServerAuthTicket](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/QueryExternalServerAuthTicket?application_version=5.5) | Query a ticket to make server-to-server calls on behalf of the signed-in user. Tickets are intended to be single use. Users must call the API again to retrieve a new ticket when making repeated calls where a ticket is required. |
| [QueryExternalAuthToken](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/QueryExternalAuthToken?application_version=5.5) | Retrieve a token for linking the service account with a service account of a different service type. |
| [QueryVerifiedAuthTicket](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/QueryVerifiedAuthTicket?application_version=5.5) | Retrieve a ticket to create a verified authentication session on a remote client. |
| [CancelVerifiedAuthTicket](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/CancelVerifiedAuthTicket?application_version=5.5) | Cancel ticket associated with the verified auth session and clean up any resources associated with the ticket. |
| **Session** |   |
| [BeginVerifiedAuthSession](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/BeginVerifiedAuthSession?application_version=5.5) | Start a verified auth session for a remote user. |
| [EndVerifiedAuthSession](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/EndVerifiedAuthSession?application_version=5.5) | Clean up the remote verified auth session and any associated resources. |
| **Get Users** |   |
| [GetLocalOnlineUserByOnlineAccountId](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/GetLocalOnlineUs-?application_version=5.5) | Retrieve a logged in user account using Online Account ID. |
| [GetLocalOnlineUserByPlatformUserId](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/GetLocalOnlineUs-_1?application_version=5.5) | Retrieve a logged in user account using Platform User ID. |
| [GetAllLocalOnlineUsers](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/GetAllLocalOnlineUsers?application_version=5.5) | Retrieve all logged in user accounts. |
| **Event Listening** |   |
| [OnLoginStatusChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/OnLoginStatusChanged?application_version=5.5) | Event triggers as a result of a change in user login status. |
| [OnPendingAuthExpiration](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/OnPendingAuthExpiration?application_version=5.5) | Event triggers as a result of a soon-to-expire auth token. |
| [OnAccountAttributesChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/OnAccountAttributesChanged?application_version=5.5) | Event triggers as a result of a change to additional attributes associated with an authenticated account. |
| **Helper** |   |
| [IsLoggedIn](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAuth/IsLoggedIn?application_version=5.5) | Query the login status of a local user. |

### Enumeration Classes

The Auth Interface defines three enumeration classes that represent a user's login status ([ELoginStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__ELoginStatus?application_version=5.5)), auth ticket audience ([ERemoteAuthTicketAudience](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__ERemoteAuthTicketAud-?application_version=5.5)), and auth token method ([EExternalAuthTokenMethod](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EExternalAuthTokenMe-?application_version=5.5)).

#### ELoginStatus

| Enumerator | Description |
| --- | --- |
| `NotLoggedIn` | Player is not logged in or has chosen a local profile. |
| `UsingLocalProfile` | Player is using a local profile, but is not logged in. |
| `LoggedInReducedFunctionality` | Player is logged in, but may have reduced functionality with online services. |
| `LoggedIn` | Player is logged in and validated by the platform specific authentication service. |

#### ERemoteAuthTicketAudience

| Enumerator | Description |
| --- | --- |
| `Peer` | Generate a ticket appropriate for peer validation. |
| `DedicatedServer` | Generate a ticket appropriate for dedicated server validation. |

#### EExternalAuthTokenMethod

| Enumerator | Description |
| --- | --- |
| `Primary` | Acquire an external auth token using the primary method provided by the auth interface. |
| `Secondary` | Acquire an external auth token using the secondary method provided by the auth interface. |

### Primary Struct

The primary struct associated with a user and their login information is the [FAccountInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FAccountInfo?application_version=5.5) struct:

#### FAccountInfo

| Member | Type | Description |
| --- | --- | --- |
| `AccountId` | `FAccountId` | The account ID of this user. This represents the user's online platform account. |
| `PlatformUserId` | `FPlatformUserId` | The platform user ID associated with this online user. |
| `LoginStatus` | `ELoginStatus` | Login status of this current user. |
| `Attributes` | `TMap<FSchemaAttributeId, FSchemaVariant>` | Additional account attributes. |

## Process Flow

### Login

`Login` authenticates a local user with the chosen online services. Upon success, `Login` returns an `FAccountInfo` struct. The `FAccountInfo` struct contains an `FAccountId`, which is necessary to use many other functions included in the Auth interface. A successful login also sets the user's `LoginStatus` to `ELoginStatus::LoggedIn`. After a user logs in to their account, the status could change to `ELoginStatus::UsingLocalProfile` or `ELoginStatus::LoggedInReducedFunctionality` in the future based on other conditions.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If there are multiple local users that require login, each user must login individually. Furthermore, platform services may not require an explicit login. On these services, the user or users are implicitly logged in when the application starts. Refer to the specific platform services documentation for more information.",
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

### Authenticate with an External Server

Frequently, games have custom web services that provide game-specific functionality. These services need to verify the caller's identity before providing access. `QueryExternalServerAuthTicket` retrieves a single-use ticket for authenticating a user with an external server.

#### Link Authenticated User with Another Online Service

Many games need to make use of more than one online service. Common cases include a platform service paired with another service which extends the first's functionality. `QueryExternalAuthToken` returns a token appropriate for authentication with a different online service to avoid requiring the user from having to provide separate login credentials for secondary services.

On most platforms, this token is an OpenId token, which provides a guarantee of user identity. This token is then provided to the Login method of the secondary service by setting `CredentialsType` to `ExternalAuth` and passing the token as `CredentialsToken`.

#### Verify User Identity with P2P or Dedicated Server

Users need to prove their identity and allow for authentication session tracking when connecting to a game server or peer-to-peer network. On the client side, `QueryVerifiedAuthTicket` retrieves a single-use ticket to be sent to the game server proving the user's identity. `CancelVerifiedAuthTicket` cancels this ticket when the play session on the game server has concluded.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Since tickets obtained from a call to <code>QueryVerifiedAuthTicket</code> are single-use tickets, <code>QueryVerifiedAuthTicket</code> must be called each time a user begins a new verified auth session. The same logic applies to <code>CancelVerifiedAuthTicket</code>. <code>CancelVerifiedAuthTicket</code> must be called for every ticket that the user has created.",
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

The game server calls `BeginVerifiedAuthSession` with the client supplied ticket when the client connects. Successful completion begins a verified auth session for the user associated with the supplied ticket. `EndVerifiedAuthSession` cleans up associated resources when the game has concluded.

This process for a user client connecting to a remote game server is summarized as:

- The client obtains a session auth ticket with a call to `QueryVerifiedAuthTicket`.
- The client sends the session auth ticket, the ticket ID, and their account ID to the server.
- The server receives this information and uses it to begin a verified auth session with a call to `BeginVerifiedAuthSession`.
- At the end of the session, the client cancels their auth ticket with `CancelVerifiedAuthTicket` and the server ends the auth session with `EndVerifiedAuthSession`.

In a peer-to-peer network model the above process is different. Each user client creates a new authentication ticket for each remote client it is connecting to. The steps for authenticating with a game server then apply for each remote peer:

- Each new remote peer calls `QueryVerifiedAuthTicket` and retrieves a single-use ticket to authenticate with every other existing peer.
- Every existing peer calls `BeginVerifiedAuthSession` to begin a verified auth session for the new remote peer.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Not all interface implementations have peer-to-peer support. Refer to your platform services documentation for more information.",
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

### Modify Account Attributes

Game code may store additional custom attributes in the `FAccountInfo` struct as needed with a call to `ModifyAccountAttributes`.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Modified attributes persist in the user's data until <code>Logout</code> is called. These attributes will not persist after the auth session is ended. <code>Logout</code> destroys the user's <code>FAccountInfo</code> struct which contains these attributes.",
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

### Logout

`Logout` ends the current authentication session for the local user and cleans up associated resources and structures.

## Example

### Login with Platform Services

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();\n\tUE::Online::IAuthPtr AuthInterface = OnlineServices-&gt;GetAuthInterface();\n\n\tUE::Online::FAuthLogin::Params Params;\n\tParams.PlatformUserId = PlatformUserId;\n\tParams.CredentialsType = LoginCredentialsType::ExchangeCode;\n\tParams.CredentialsToken = TEXT(&quot;1234567890&quot;); // Exchange code from command-line\n\n\tAuthInterface-&gt;Login(MoveTemp(Params)).OnComplete([](const UE::Online::TOnlineResult&lt;UE::Online::FAuthLogin&gt;&amp; Result)\n\t{\n",
  "lines_of_code": 21,
  "id": 150009,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTAwMDksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1NzoyNyswMDowMCJ9--7d4de5e5adba8fb6eb35667a9ee0b741d0ddd5467310e7ce2e3b7c8697e2e47d",
  "settings": {
    "is_hidden": false
  }
}
```

#### Walkthrough

1. Retrieve the default online services by calling `GetServices` with no parameters, then access the Auth interface:
2. Instantiate the parameters necessary to login the user:
3. Handle the `Login.OnComplete` callback by registering the account info upon successful login or processing the resulting error:

## Converting Code from Online Subsystem

The Online Services Auth Interface is responsible for all code owned by the [Online Subsystem Identity Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-identity-interface-in-unreal-engine?application_version=5.5).

## More Information

### Header File

Consult the `Auth.h` header file directly for more information as needed. The Auth Interface header file `Auth.h` is located in the directory:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Engine\\Plugins\\Online\\OnlineServices\\Source\\OnlineServicesInterface\\Public\\Online",
  "lines_of_code": 1,
  "id": 150013,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTAwMTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1NzoyNyswMDowMCJ9--6a9bebb679c2da64be83dbd3a2756a160672aabfd3389489d11bf8fb1df3038d",
  "settings": {
    "is_hidden": false
  }
}
```

For instructions on how to obtain the UE source code, refer to our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

Refer to the Functions section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.
