# Using In-App Purchases

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-inapp-purchases-in-unreal-engine-projects-for-mobile-devices

> Application Version: 5.7

In-app purchases enable you to offer additional content and features to users. You can use this as a means to monetize a free application or to provide additional paid content for your application.

## General Mobile Stores Information

Some information here is summarized. Refer to the [Google Play Billing Library documentation](https://developer.android.com/google/play/billing/integrate) or the [Apple StoreKit documentation](https://developer.apple.com/documentation/storekit) for more information. Some additional details are provided for each platform on their respective pages:

- [Related Document](en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android.md)

- [Related Document](en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios.md)

The regular flow for using in-app purchases on mobile stores is:

- Query product details to the store. Products in the store are identified by product IDs, which are string based identifiers you previously assigned when configuring in-app purchase products for your application in the store. This step provides updated store information (like pricing and localized descriptions) and makes the product available to purchase. Underlying libraries use some low-level objects retrieved from this step to be able to initiate a purchase
- Initiate a purchase for a given product ID This shows a native UI to complete the payment using the store's payment services on the device. After a successful payment, a receipt is generated representing the transaction.
- Validate the transaction You must validate the transaction is legitimate to avoid fraud. Stores provide and recommend using server-to-server calls with their servers to verify legitimate transactions and retrieve additional information about the purchased product (like expiration times for subscriptions). This is accomplished by sending the receipt information to your servers and verifying them server-side.
- Grant product Grant and persist the in-game product the user acquired after successfully validating the transaction.
- Finalize the transaction Stores expect the transaction to be marked as completed after the in-game product is granted. Not properly finalizing the transaction might lead to refunds on Google Play and performance issues on App Store. You must store that a given purchase was already completed by a given user to avoid granting the product multiple times for the same transaction. Applications should not finalize transactions if the receipt could not be validated or the content could not be granted by the backend. Unfinalized receipts should result in retries or refunds if it was not possible to safely grant the product.

Payments can be deferred because they need additional steps to complete. Examples of this include:

- Payments expected to be completed with cash in a physical store.
- Showing agreements because legal terms changed.
- Parental control that requires an adult to accept the purchase.

Underlying libraries notify you asynchronously when those payments become successful if the application is running, so you can get the new receipts and complete the purchase flow. If the application is not running the receipts will be available on next execution

Due to mobile devices particularities, any step from the purchase flow may be interrupted by unexpected reasons like network connectivity, a crash, or the user killing the application in the middle of any step. It is a good practice to check for existing receipts on startup and complete the missing steps to avoid double granting products.

Google Play and App Store differ on which information is available regarding a purchase once it has been finalized but both of them expose receipts for not finalized transactions. They also behave differently with receipts related to subscription renewal.

Stores differentiate between in-app products and subscriptions:

- In-app products may be consumable or non-consumable. Consumable products can be purchased again after the transaction is completed, so users can purchase them several times. An example of those is purchasing in-game currency chests. Once the user is granted the in-game currency and the transaction is finalized the product can be purchased again. Non-consumable products can be purchased only once and after that point the user owns them. An example of those is unlocking a premium feature.
- Subscriptions are meant to grant some kind of benefit for a period of time. They are allowed to renew automatically so they become a recurrent source of payments. Dripping resources over time or temporary access to premium content could be an example of a subscription. Subscriptions allow for different renewal plans and allow offers to be configured from the stores (like free trials, discounts on initial renewals, discounts for new subscribers, and so on).

## Implementation Examples

### Query Product Details

Using the **Read In App purchase Information2** blueprint.

![Image](https://dev.epicgames.com/community/api/documentation/image/8eac8629-983a-4844-80a0-5e7cb0f3805e)

_Blueprint example of querying for product information and adding the known product IDs to a combo box._

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// null checks ommited for simplicity\n\nFUniqueNetIdRepl PlayerNetId = ...;\nTArray&lt;FString&gt;&amp; ProductIDs = ...;\n\nIOnlineSubsystem* OnlineSub = IOnlineSubsystem::Get();\nIOnlineStoreV2Ptr StoreInterface = OnlineSub-&gt;GetStoreV2Interface();\n\t\t\t\t\nStoreInterface-&gt;QueryOffersById(*PlayerNetId, \n                                ProductIDs, \n",
  "lines_of_code": 22,
  "id": 121368,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMjEzNjgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDozMiswMDowMCJ9--45e4dd7754d72b75744c4d7e09a7894d139940c0849b2485a0f08594ba408295",
  "settings": {
    "is_hidden": false
  }
}
```

### Initiating a Purchase Using a Given Product ID

You can start the purchase flow by using the **Start an in-App Purchase** blueprint.

![Image](https://dev.epicgames.com/community/api/documentation/image/8af0f6e7-2c09-4c45-9cb4-acdebe2a9502)

_Example of starting an in-app purchase for the given Product ID and breaking the receipt data._

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// null checks ommited for simplicity\n\nFUniqueNetIdRepl PlayerNetId = ...;\nTArray&lt;FString&gt;&amp; ProductIDs = ...;\n\nIOnlineSubsystem* OnlineSub = IOnlineSubsystem::Get();\nIOnlinePurchasePtr PurchaseInterface = OnlineSub-&gt;GetPurchaseInterface();\n\t\t\t\t\nFPurchaseCheckoutRequest CheckoutRequest;\n\n",
  "lines_of_code": 21,
  "id": 121369,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMjEzNjksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDozMiswMDowMCJ9--11d4c6f0b4ec4cb1737db50701eec123d0eefcc723bc8eef97cd813073c87644",
  "settings": {
    "is_hidden": false
  }
}
```

### Final Purchase Flow Steps

![Image](https://dev.epicgames.com/community/api/documentation/image/871f840c-b974-4d37-a2a3-b8e164daed9b)

_Complete flow example with blueprints. Validate Purchase and Grant Product is a node that should be provided by the game since this has business logic details._

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// null checks ommited for simplicity\n\nFUniqueNetIdRepl PlayerNetId = ...;\nconst TSharedRef&lt;FPurchaseReceipt&gt;&amp; Receipt = ...\n\n// Games should provide a way to validate the receipt using the ValidationInfo field in FPurchaseReceipt\n\n...\n\n// Games should provide a way to grant and persist the purchased product only once\n",
  "lines_of_code": 23,
  "id": 121370,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMjEzNzAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDozMiswMDowMCJ9--b4ef54e266a28e65215c4500d96f5d9c9661a9d1c41c5018cad78acf0004e0f4",
  "settings": {
    "is_hidden": false
  }
}
```

### Querying and Completing Unfinished Transactions

![Image](https://dev.epicgames.com/community/api/documentation/image/05ed49af-ab3c-47db-896d-15ae36ad5226)

_Full blueprint example requesting owned products.Validate Purchase and Grant Product is a node that should be provided by the game since this has business logic details._

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// null checks ommited for simplicity\nFUniqueNetIdRepl PlayerNetId = ...;\n\nIOnlineSubsystem* OnlineSub = IOnlineSubsystem::Get();\nIOnlinePurchasePtr PurchaseInterface = OnlineSub-&gt;GetPurchaseInterface();\n\nPurchaseInterface-&gt;QueryReceipts(*PlayerNetId, \n                                 false, \n                                 FOnQueryReceiptsComplete::CreateLambda([PlayerNetId](const FOnlineError&amp; Result) {\n    if (Result.WasSuccessful())\n",
  "lines_of_code": 37,
  "id": 121371,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMjEzNzEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDozMiswMDowMCJ9--b17d2819ba83f23951ffc13bac6c22683658a888149d18fb3a11314001ca9760",
  "settings": {
    "is_hidden": false
  }
}
```

### Handling Asynchronous Transaction Notifications

In some cases, a transaction might complete some time after it is initially notified with an error. This can happen when being marked as deferred or if some agreement needs to be accepted before continuing with the transactions. Purchases made out of the app can also be notified using this method (like enabling a subscription from outside the application). Subscription expiration and failed deferred transactions are not notified on device in any way.

To detect when an asynchronous result arrived, you can register to the `OnUnexpectedPurchaseReceipt` delegate in 
`IOnlinePurchase`.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// null checks ommited for simplicity\n\nIOnlineSubsystem* OnlineSub = IOnlineSubsystem::Get();\nIOnlinePurchasePtr PurchaseInterface = OnlineSub-&gt;GetPurchaseInterface();\n\nDelegateHandle = PurchaseInterface-&gt;AddOnUnexpectedPurchaseReceiptDelegate_Handle(FOnUnexpectedPurchaseReceiptDelegate::CreateLambda([](const FUniqueNetId&amp; UserId)\n{\n    // Query receipts and handle new transactions or mark it to do later\n});\n",
  "lines_of_code": 9,
  "id": 121372,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMjEzNzIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDozMiswMDowMCJ9--27e1af03ee09c6ab5de8cdceee1718a3800cb2e8e640360a563bd6d7a70e4cce",
  "settings": {
    "is_hidden": false
  }
}
```

### Subscription Handling

Most of the information regarding status and expiration times is not available on  device. Subscriptions status checks are managed server-side using the APIs and services provided by each store.

## Blueprint Nodes Descriptions

### Read In App Purchase Information2

Triggers an asynchronous query to the store to retrieve information about a list of products.

![Image](https://dev.epicgames.com/community/api/documentation/image/a1f7f2ff-458e-4262-a107-370da00bb48b)

| Item | Description |
| --- | --- |
| Input Pins |   |
| **(Unlabeled)** | This execution input triggers the query for product information to the store. |
| **Player Controller** | Player controller identifying the user communicating with the store. |
| **Product Identifiers** | Array of strings that identify the product IDs you are interesting in retrieving data about. |
| Output Pins |   |
| **(Unlabeled)** | Execution output that triggers execution of the next node. |
| **On Success** | Execution output that triggers when the query succeeds. |
| **On Failure** | Execution output that triggers when the query fails. |
| **In App Offer Information** | Array of `OnlineProxyStoreOffer` containing the product information for all existing products the query was able to retrieve. ![Image](https://dev.epicgames.com/community/api/documentation/image/bd477c80-ff93-4548-9e7e-4ece0f242548) |

### Start an In-App Purchase

Starts the payment flow to purchase a given product using its product ID. On success it provides a receipt identifying the transaction

![Image](https://dev.epicgames.com/community/api/documentation/image/e33b40e5-4038-44cb-9918-7a82f30c7649)

| Item | Description |
| --- | --- |
| Input Pins |   |
| **(Unlabeled)** | This execution input triggers the start of the purchase flow. |
| **Player Controller** | Player controller identifying the user communicating with the store. |
| **Product request** | Request object to set the product ID. Can be created from a string. ![Image](https://dev.epicgames.com/community/api/documentation/image/7b54bdb2-7918-412a-94d2-d184e5b87b85) |
| Output Pins |   |
| **(Unlabeled)** | Execution output that triggers execution of the next node. |
| **OnSuccess** | Execution output that triggers when the query succeeds. |
| **OnFailure** | Execution output that triggers when the query fails. |
| **Purchase Status** | In the case of a failure, used to get the cause of the failure. ![Image](https://dev.epicgames.com/community/api/documentation/image/920877d8-7efc-458c-ac0a-5f32fc2ff42b) |
| **In App Offer Receipt** | Receipt object generated for the given purchase. In the case of a successful purchase, data contained in the receipt can be used to verify the transaction is legitimate against the store servers. ![Image](https://dev.epicgames.com/community/api/documentation/image/82d69172-1262-48e0-b494-56f84b70a58e) |

### Query for Owned In-App Products

Queries the store for known transactions and generates receipts for them. Received information might refer to new transactions and/or persistent ones depending on the platform. Take care to not grant products twice to users.

![Image](https://dev.epicgames.com/community/api/documentation/image/e90cfb1a-9ff9-43cf-b12f-f26e8fff4c40)

| Item | Description |
| --- | --- |
| Input Pins |   |
| **(Unlabeled)** | This execution input triggers the query for transaction information to the store. |
| **Player Controller** | Player controller identifying to identify the user communicating with the store |
| Output Pins |   |
| **(Unlabeled)** | Execution output that triggers execution of the next node. |
| **OnSuccess** | Execution output that triggers when the query succeeds. |
| **OnFailure** | Execution output that triggers when the query fails. |
| **Purchase Status** | In the case of a failure, used to get the cause of the failure. ![Image](https://dev.epicgames.com/community/api/documentation/image/8ebc0d22-228d-41c6-b050-472396fd4a8c) |
| **In App Offer Receipts** | Array of receipt objects generated from known transactions. Some of them may be new and others could be persistent depending on the platform, see the platform-specific pages for more. |

### Get known In-App Receipts

Gets cached receipts for transactions. This cache is filled after a successful execution of the `Query for Owned In-App Products` node. This node does not trigger a query.

![Image](https://dev.epicgames.com/community/api/documentation/image/5d4e33c5-e086-49ca-87d5-f245c6540d45)

| Item | Description |
| --- | --- |
| Input Pins |   |
| (Unlabeled) | This execution input triggers the start of the operation. |
| Player Controller | Player controller identifying to identify the user communicating with the store |
| Output Pins |   |
| (Unlabeled) | Execution output that triggers execution of the next node |
| OnSuccess | Execution output that triggers when the query succeeds. |
| OnFailure | Execution output that triggers when the operation fails. |
| Purchase Status | In the case of a failure, used to get the cause of the failure. ![Image](https://dev.epicgames.com/community/api/documentation/image/74849847-ab30-42ac-b494-71359ac515bf) |
| In App Offer Receipts | Array of receipt objects from cached data. |

### Finalize In-App Purchase Transaction

Finalizes the transaction identified by the input receipt. Not finalizing transactions can lead to refunds or bad device performance depending on the configuration and platform. See the Google Play and App Store documentation for more details.

![Image](https://dev.epicgames.com/community/api/documentation/image/470c90e1-e605-4532-a8ae-db8216dad952)

| Item | Description |
| --- | --- |
| Input Pins |   |
| **(Unlabeled)** | This execution input triggers the start of the operation. |
| **In App Purchase Receipt** | Receipt identifying the transaction to be finalized. |
| **Player Controller** | Player controller identifying the user communicating with the store. |
| Output Pins |   |
| **(Unlabeled)** | Execution output that triggers execution of the next node. |

### Restore Owned In-App Products

Queries the store to restore and generate receipts for already-completed transactions. This node usefulness is platform-dependent and will not restore consumable transactions.

![Image](https://dev.epicgames.com/community/api/documentation/image/559044a5-d6ef-4ba4-b452-9cdc43f6f3b4)

| Item | Description |
| --- | --- |
| Input Pins |   |
| **(Unlabeled)** | This execution input triggers the start of the operation. |
| **Player Controller** | Player controller identifying the user communicating with the store. |
| Output Pins |   |
| **(Unlabeled)** | Execution output that triggers execution of the next node. |
| **OnSuccess** | Execution output that triggers when the query operation succeeds. |
| **OnFailure** | Execution output that triggers when the operation fails. |
| **Purchase Status** | In the case of a failure, used to get the cause of the failure. ![Image](https://dev.epicgames.com/community/api/documentation/image/1c3e20f3-21b3-44f3-8ab6-492d0b6c970b) |
| **In App Offer Receipts** | Array of receipt objects created from restored transactions and existing transactions. Receipts for transactions marked as Restored do not need to be explicitly finalized. |

### Troubleshoot

- Set banking data in the Google Play Console and App Store Connect connect accounts and accept all legal agreements (the Paid Apps Legal Agreement is particularly important for App Store Connect). Otherwise you might find different issues potentially not triggering any specific error and won’t be able to use sandbox environments. You cannot configure in-app/subscriptions products on the Google Play Console. The option does not appear. No product information from existing products is received when using **Read In App Purchase Information2** Blueprint node or `IStoreInterface::QueryOffersById` in the Sandbox environment on iOS This is because it is possible you won’t be getting a valid net ID on iOS devices so you won’t be able to start a purchase.

- In order to run server to server calls you might need additional configuration from Google Play Cloud services (enabling APIs, OAuth credentials, service accounts) . Check [Google’s documentation](https://developers.google.com/android-publisher/getting_started) to set up the environment.
- If you have issues identifying with GameCenter be sure to enable it in your app App Store Connect services section and to add at least one leaderboard to it.
- Check you are using a provisioning profile with the AppID matching your application bundle ID and including the InApp Purchases entitlement on iOS.
