# Fab in Unreal Engine

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine

> Application Version: 5.7

When working in Unreal Engine, you can access Fab directly to acquire and download plugins and assets for your project, by using the Fab window. This works similarly to accessing [Fab](https://www.fab.com/) through your browser or in the Epic Games Launcher, but there are some differences.

## Accessing Fab

To access Fab in Unreal Engine, navigate to the **Window** menu, and scroll down to **Fab** in the Get Content section.

![Fab in the Window menu](https://dev.epicgames.com/community/api/documentation/image/0d3b4c7d-68fd-416d-a9cf-5972dacf76dd)

Alternatively, you can open the **Content Drawer**, then click on the **Fab** button right next to the **Add+** button.

![Fab button in the Content Drawer](https://dev.epicgames.com/community/api/documentation/image/cc0e0b2f-4131-4b84-84b3-10c4b24ac1f2)

### Fab Plugin

The Fab window requires the **Fab plugin**, which is enabled by default in Unreal Engine. If you can't access the Fab window, navigate to [Edit > Plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine), then search for and enable the Fab plugin.

![Fab plugin in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/5b195133-49b9-4fdc-a75b-5dff6f96fbd2)

## Fab Products

The Fab window provides a way for you to find, view, and evaluate product listings, so that you can acquire these products for use in your projects in Unreal Engine. Product listings can be either free or priced. You can interact with listings both as product tiles in the Fab window, and by clicking the product tiles to view the full listing.

### Product Tiles

Product tiles in the Fab window show you basic information about the associated product. This includes:

1. Name
2. Publisher
3. Rating
4. Price (or Free)
5. Whether the product is already saved in your library. ![Fab product saved in My Library](https://dev.epicgames.com/community/api/documentation/image/0458f5fe-b546-4351-9b71-acc6eb416524)

You can interact with listings directly in the Fab window using the product tiles.

1. Mousing over the product tile shows you the product type, and compatible file formats. ![Mousing over a product tile](https://dev.epicgames.com/community/api/documentation/image/7085fab7-6f7f-4cff-87ea-b704624e7c8d)
2. You can click the **cart icon** to add the product to your [cart](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#cart-view), and the **wishlist icon** to add it to your [wishlist](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#wishlist-view). ![Adding products to cart and wishlist](https://dev.epicgames.com/community/api/documentation/image/4e8d53e5-da21-413d-9a5a-d7146a0d780c)
3. When you click to add a product to your cart, you must also select a [license](https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab). ![Select a license when adding a product to your cart in the Discover view.](https://dev.epicgames.com/community/api/documentation/image/5bb828e0-31f5-474c-8909-da02176aa1f3)

## Product Preview

When you click a product tile in the Fab window, you are shown a preview of the full product.

![Unreal Engine Fab window product preview](https://dev.epicgames.com/community/api/documentation/image/fb814cad-428b-43c1-a1c2-57b71dfbe44e)

_Click image for full size._

```json
{
  "type": "include",
  "excerpt_id": 2463,
  "excerpt_assignment_id": 2451,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The product preview shows basic information about the product, including:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "ordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "Publisher",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Name",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Product type",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Rating",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Available license types and terms",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Included file formats",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Publish date",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Age rating",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "AI usage and generation.",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can expand images to view them in full screen, and you can view certain products with 3D models in the <a data-document-id=\"3221884\" href=\"https://dev.epicgames.com/documentation/en-us/fab/using-the-3d-editor-in-fab\">Fab 3D Viewer</a>. ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can also scroll down the preview to find a full description of the product, with all the relevant technical information for each supported file type.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "lY6b",
  "settings": {
    "is_hidden": false
  }
}
```

![Fab window product preview details](https://dev.epicgames.com/community/api/documentation/image/1f4d01e4-2d18-4c78-b50a-f086dffc8776)

_Click image for full size._

### Add to My Library

When viewing a free product preview, you can add it to your library immediately by clicking **Add to My Library**.

![Add a free product to your Fab library](https://dev.epicgames.com/community/api/documentation/image/894ccb77-5058-4b73-a436-9094c9880183)

_Click image for full size._

### Buy Now

When viewing a priced product preview, you can click **Buy now** to purchase the product immediately. This triggers the checkout process for the product you are previewing.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you haven't selected a license, you need to do so first.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26265892,
      "caption": "",
      "alt_text": "Buy now license error",
      "image": {
        "id": 26265892,
        "file_name": "fab-plugin-select-license-error.png",
        "file_size": 25635,
        "content_type": "image/png",
        "created_at": "2025-11-13T18:23:07.920+00:00",
        "height": 316,
        "width": 982,
        "storage_key": "58c0adc0-af1d-4627-b377-a193301f95d2",
        "context": "documentation"
      },
      "storage_key": "58c0adc0-af1d-4627-b377-a193301f95d2",
      "context": "documentation",
      "width": 400,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26265893,
      "caption": "",
      "alt_text": "Fab window product preview select a license",
      "image": {
        "id": 26265893,
        "file_name": "fab-plugin-listing-license.png",
        "file_size": 84700,
        "content_type": "image/png",
        "created_at": "2025-11-13T18:23:07.993+00:00",
        "height": 778,
        "width": 1017,
        "storage_key": "651d2577-8834-4352-81fa-8b27a5a24a86",
        "context": "documentation"
      },
      "storage_key": "651d2577-8834-4352-81fa-8b27a5a24a86",
      "context": "documentation",
      "width": 400,
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

You are shown the checkout page for the selected product, and can choose your method of payment and other relevant details.

![Fab window buy now checkout](https://dev.epicgames.com/community/api/documentation/image/62480bc9-a170-42c7-a179-07fac54c019e)

_Click image for full size._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Prices will display in USD by default. If you are logged in to Fab, then prices will display in your local currency.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26265895,
      "caption": "Click image for full size.",
      "alt_text": "Fab window buy now checkout in CA$",
      "image": {
        "id": 26265895,
        "file_name": "fab-plugin-buy-now-currency.png",
        "file_size": 272760,
        "content_type": "image/png",
        "created_at": "2025-11-13T18:23:08.251+00:00",
        "height": 1750,
        "width": 2392,
        "storage_key": "f1bc3dbb-46fc-4817-9ded-c1e577ca5dd0",
        "context": "documentation"
      },
      "storage_key": "f1bc3dbb-46fc-4817-9ded-c1e577ca5dd0",
      "context": "documentation",
      "width": null,
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

### Add to Cart / Wishlist

If you do not want to purchase the previewed product immediately, you can click **Add to cart** to add it to your [cart](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#cart-view) to purchase later. You can also click the **Wishlist button** to the right of the Add to cart button to add the product to your [wishlist](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#wishlist-view).

![Add to cart and wishlist buttons](https://dev.epicgames.com/community/api/documentation/image/d1a0f918-4f88-462a-82ae-609001982eb9)

If you have already added the product to your cart and/or to your wishlist, the buttons change. You can click View in cart to go to your cart and finalize your purchases. You can click the Wishlist button to remove the product from your wishlist.

![VIew in cart and remove from wishlist buttons](https://dev.epicgames.com/community/api/documentation/image/faa73c11-1c7c-4728-810e-86e8b4cc8582)

## Discover View

When you open the Fab window, you are shown the **Discover** view. This is the default view of the Fab window. The Fab window has several sections with different features that help you find products to use in your projects.

![The Fab window Discover view](https://dev.epicgames.com/community/api/documentation/image/9d3328de-0e13-4d6d-bb2b-0c03aa698d12)

_Click image for full size._

1. [Search bar](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#search-bar)
2. [Navigation controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#navigation-controls)
3. [Account controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#account-controls)
4. [Featured products](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#featured-products) (Discover view only) [Featured Unreal Engine products](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#featured-unreal-engine-products) [Quixel](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#quixel) [UE samples](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#ue-samples)
5. [Product type panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#product-type-panel)
6. [Product list and filter menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#product-list-and-filter-menu)

### Search Bar

The Fab window has a search bar, available in every view, that you can use to filter the Fab products by text string.

![Fab window search bar](https://dev.epicgames.com/community/api/documentation/image/b76543ea-d8d5-4427-a88d-a21a174738b9)

![Fab window search results](https://dev.epicgames.com/community/api/documentation/image/69203558-298f-412a-b4b0-27a3f58a730e)

_Click image for full size._

You can use Boolean operators like AND and OR to modify your search using additional terms if your initial results are insufficient (too broad or too narrow, for example).

![Fab window search results using Boolean AND operator](https://dev.epicgames.com/community/api/documentation/image/883443a8-c86f-48f3-91ef-91c61814cc0b)

_Click image for full size._

You can also use the [product type panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#product-type-panel),  and the [product filter menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#product-list-and-filter-menu), to further refine your search.

### Navigation Controls

```json
{
  "type": "include",
  "excerpt_id": 2464,
  "excerpt_assignment_id": 2452,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The navigation controls help you move between different pages of search and filter results.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25962766,
      "caption": "",
      "alt_text": "Fab window navigation control icons",
      "image": {
        "id": 25962766,
        "file_name": "image.png",
        "file_size": 4546,
        "content_type": "image/png",
        "created_at": "2025-08-20T18:05:09.561+00:00",
        "height": 110,
        "width": 220,
        "storage_key": "e4f2fba3-9d01-4aa3-9766-94468f3593f3",
        "context": "documentation"
      },
      "storage_key": "e4f2fba3-9d01-4aa3-9766-94468f3593f3",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "ordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "Click the <b>Home</b> icon to return to the Fab window Discover view.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Click the <b>Back (&lt;)</b> icon to return to the previous set of search and filter results. If you have only one set of results, this returns you to the Fab window home view.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Click the <b>Forward (&gt;)</b> icon to return to the set of results you were viewing before you clicked the Back icon. Does nothing if you are already viewing your most recent results.",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "9kxa",
  "settings": {
    "is_hidden": false
  }
}
```

### Account Controls

The account controls help you manage your account, your cart, and the Fab settings. They provide access to your Fab library and your wishlist.

![Fab window account control icons](https://dev.epicgames.com/community/api/documentation/image/7d6b372e-6bb1-464d-ab12-466ea83ec098)

1. Shows the **My Library** view in the Fab window.
2. Shows the **Wishlist** view in the Fab window.
3. Shows your **Cart** contents for checkout; the icon also shows the number of items in your cart.
4. Opens the localization menu so you can choose your language for the Fab window. ![Fab window localization dropdown menu](https://dev.epicgames.com/community/api/documentation/image/3226b411-21be-47ac-aa61-0303bac39702)
5. Opens the Account menu, which provides additional options. ![Fab window account menu](https://dev.epicgames.com/community/api/documentation/image/01b986b6-9094-47b6-97e8-42ea77923375) Click **Help** to open the [Fab documentation](https://dev.epicgames.com/documentation/en-us/fab/fab-documentation) in your browser. Click **Fab settings** to open the [Fab settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#fab-settings) in a separate window. Click **Account settings** to open your Epic Games account settings in your browser. You might need to sign in. Click **Sign out** to sign out of your Epic Games account.

### Featured Products

In the default Discover view, the Fab window shows a selection of featured products in three categories. For each of these, you can click **Forward (>)** and **Back (<)** on the right of the category to scroll horizontally through the carousel of products shown.

![Forward and back carousel scroll icons](https://dev.epicgames.com/community/api/documentation/image/9cff3608-ed73-499a-af34-760bb167c655)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "\nOnly Fab products usable by Unreal Engine show in the Fab window. If you\n want to browse products usable by other applications, go to the <a href=\"https://www.fab.com/\">Fab home page</a>.\n\n",
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

#### Featured Unreal Engine Products

This category shows a selection of featured products available for sale, created by third-party vendors.

#### Quixel

This category shows a selection of products created by Quixel, some free and some for sale.

#### UE Samples

This category shows free samples created by Epic Games developers to demonstrate various features and projects.

### Product Type Panel

You can use the product type panel on the left of the Fab window to view only specific types of products. You can expand each of the product types listed to show subtypes or tags, which provide a way for you to refine your list of viewed products. From there, you can use the [filter menus](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#product-list-and-filter-menu) to further limit the list of products you are shown in the Fab window. You can reset your product type filter by clicking **All products** at the top of the panel.

![Fab window product type panel](https://dev.epicgames.com/community/api/documentation/image/c852bea4-77e7-41c2-8389-b974e4f4911f)

### Product List and Filter Menu

The Fab window provides a full list of products available to purchase (for priced products) or add to your library (for free products). It also provides a broad range of filtering and sorting options, available in the filter menu at the top of the product list. These are at the top of the Fab window in any view showing multiple products except the Discover view, where they are available beneath the [featured products](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#featured-products).

![Fab window filters menus left side](https://dev.epicgames.com/community/api/documentation/image/8b9ad762-1beb-499d-accf-7d0b4f5c7b87)

![Fab window filter menus right side](https://dev.epicgames.com/community/api/documentation/image/8a5f8b04-10bc-4e78-8b56-c2d146a420c4)

Each of the filter menu options provides a different way for you to refine your search for products in the Fab window. You can use as many filters as you like, and can clear them individually or all together using the filter tags at the top of the product list.

![Fab window multiple filters](https://dev.epicgames.com/community/api/documentation/image/1784f345-ea73-4f87-a5b5-1554eb2f30e7)

_Click image for full size._

For more information on the filter menu, see the [Fab documentation](https://dev.epicgames.com/documentation/en-us/fab/purchasing-and-downloading-assets-in-fab#preview-products).

#### Include 3D compatible formats

The **Include 3D** **compatible formats** toggle expands the range of file formats in the products shown in the Fab window to include the following 3D compatible file types:

- GLB
- GLTF
- FBX
- Unreal Engine

![Fab window 3D compatible formats toggle](https://dev.epicgames.com/community/api/documentation/image/0f65f6cc-ad60-4f3e-82df-aa7770b56df8)

#### Style

The **Style** dropdown menu provides a simple search bar, and expandable lists of filter options based on rendering styles and period/theme styles. You can select multiple filters.

![Fab window Style filter](https://dev.epicgames.com/community/api/documentation/image/4a8c3fd6-c6d4-431d-b30d-283aad0da229)

#### Compatibility

The **Compatibility** dropdown menu has submenus you can use to choose minimum and maximum supported versions of UE, and a checklist of supported platforms to choose from. You can select multiple filters.

![Fab window Compatibility filter](https://dev.epicgames.com/community/api/documentation/image/547d73d6-7c9c-444d-a0f4-5facec3162ee)

#### Technical features

The **Technical features** dropdown menu provides a simple search bar, and expandable lists of filter options for animation, functionality, and Unreal Engine features. You can select multiple filters.

![Fab window Technical features filter](https://dev.epicgames.com/community/api/documentation/image/145c0ee8-13be-4b51-b103-f773c2a8f2d7)

#### Tags

The **Tags** dropdown menu provides a simple search bar you can use to find products that have specific tags.

![Fab window Tags search bar](https://dev.epicgames.com/community/api/documentation/image/c902ea70-4c83-45f9-89ca-21309602688c)

```json
{
  "type": "include",
  "excerpt_id": 2465,
  "excerpt_assignment_id": 2453,
  "blocks": [
    {
      "type": "header",
      "content": "Price",
      "level": 4,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <b>Price </b>dropdown menu provides fields for you to filter by minimum and maximum price. It also has a checkbox to filter for free products, and a toggle to show only products on sale.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25963570,
      "caption": "",
      "alt_text": "Fab window Price filter",
      "image": {
        "id": 25963570,
        "file_name": "image.png",
        "file_size": 37480,
        "content_type": "image/png",
        "created_at": "2025-08-20T21:15:53.846+00:00",
        "height": 508,
        "width": 687,
        "storage_key": "dbfa1122-9b97-460d-bd2c-702a17a0216b",
        "context": "documentation"
      },
      "storage_key": "dbfa1122-9b97-460d-bd2c-702a17a0216b",
      "context": "documentation",
      "width": 300,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Licenses",
      "level": 4,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Licenses dropdown menu provides filter options based on the <a data-document-id=\"3706182\" href=\"https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab\">license types supported by Fab</a>, including:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "ordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "The <a href=\"https://creativecommons.org/licenses/by/4.0/\">Creative Commons Attribution license (CC-BY 4.0)</a>.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Standard Fab personal and professional licenses.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "The legacy UE marketplace license.",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "8WLW",
  "settings": {
    "is_hidden": false
  }
}
```

![Fab window License filter](https://dev.epicgames.com/community/api/documentation/image/9f46e872-c376-4d2c-966f-af93c28257c5)

#### Publishers

The **Publishers** dropdown menu provides a simple search bar you can use to find products from specific publishers.

![Fab window Publishers search bar](https://dev.epicgames.com/community/api/documentation/image/0c23bd27-6a2d-4a44-b60f-30e35417c1b3)

#### Date published

The **Date published** dropdown menu provides a way for you to limit your search according to how recently a product was published.

![Fab window Date published filter](https://dev.epicgames.com/community/api/documentation/image/dea1565a-7ef4-448e-8b11-67e58881b8c7)

#### Ratings

The **Ratings** dropdown menu provides a way for you to limit your search according to the community star ratings for products.

![Fab window Ratings filter](https://dev.epicgames.com/community/api/documentation/image/2781887d-966b-4f5a-a6b1-fa62a23f5664)

```json
{
  "type": "include",
  "excerpt_id": 2466,
  "excerpt_assignment_id": 2454,
  "blocks": [
    {
      "type": "header",
      "content": "Sort by",
      "level": 4,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <b>Sort by</b> dropdown menu does not provide a filter for your search results. Instead, it determines how to sort and display the products shown in the Fab window. <br>",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25963578,
      "caption": "",
      "alt_text": "Fab window Sort by dropdown",
      "image": {
        "id": 25963578,
        "file_name": "image.png",
        "file_size": 34297,
        "content_type": "image/png",
        "created_at": "2025-08-20T21:25:02.154+00:00",
        "height": 596,
        "width": 368,
        "storage_key": "4b6feb9d-8b8e-4ea5-8ad9-6d1fcb242b70",
        "context": "documentation"
      },
      "storage_key": "4b6feb9d-8b8e-4ea5-8ad9-6d1fcb242b70",
      "context": "documentation",
      "width": 200,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Content preferences",
      "level": 4,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can click the <b>Content preferences</b> button, located on the right side of the Fab window beside the filter dropdown menus, to open the Content preferences window.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25963579,
      "caption": "",
      "alt_text": "Fab window content preferences button",
      "image": {
        "id": 25963579,
        "file_name": "image.png",
        "file_size": 1579,
        "content_type": "image/png",
        "created_at": "2025-08-20T21:25:02.121+00:00",
        "height": 70,
        "width": 75,
        "storage_key": "78a00f6c-ba44-4c38-b232-911d2d645aff",
        "context": "documentation"
      },
      "storage_key": "78a00f6c-ba44-4c38-b232-911d2d645aff",
      "context": "documentation",
      "width": 75,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can choose whether or not to show products created with AI, and whether you want to hide, blur, or show mature content. Once you have decided on your preference settings, you can click Save to apply your preferences everywhere on Fab.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25963580,
      "caption": "",
      "alt_text": "Fab window Content preferences options",
      "image": {
        "id": 25963580,
        "file_name": "image.png",
        "file_size": 99103,
        "content_type": "image/png",
        "created_at": "2025-08-20T21:25:02.564+00:00",
        "height": 816,
        "width": 1620,
        "storage_key": "cbe63457-c7bc-4581-8b11-ccb8263f113e",
        "context": "documentation"
      },
      "storage_key": "cbe63457-c7bc-4581-8b11-ccb8263f113e",
      "context": "documentation",
      "width": 600,
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "7jLk",
  "settings": {
    "is_hidden": false
  }
}
```

## My Library View

Clicking on the **My Library** icon shows you the My Library view.

![Fab window My Library icon](https://dev.epicgames.com/community/api/documentation/image/158c011f-1d9b-4f11-ba30-abe7e5bb3d83)

By default, this displays every free and priced Fab product associated with your Epic Games account usable in Unreal Engine.

![Fab window My Library view](https://dev.epicgames.com/community/api/documentation/image/968d3301-fe0d-47b8-96b9-c8186be8ced4)

_Click image for full size._

```json
{
  "type": "include",
  "excerpt_id": 2467,
  "excerpt_assignment_id": 2455,
  "blocks": [
    {
      "type": "paragraph",
      "content": "There are a number of filter and sort options available to you to manage your library:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "You can use the Search bar to find specific products.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "You can filter your library by using the product type panel on the left.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "You can toggle showing 3D compatible formats.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "You can filter your library by purchase date.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "You can toggle between sorting from newest to oldest, or from oldest to newest, using the drop-down menu on the right.",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can download products and add them directly to your current project by clicking the + icon in the bottom right of each product tile.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "k1eP",
  "settings": {
    "is_hidden": false
  }
}
```

![Fab window product tile add to project button](https://dev.epicgames.com/community/api/documentation/image/f8368ada-76dc-49b6-a7bc-e8709616a2dc)

## Wishlist View

Clicking on the **Wishlist** icon in the account controls shows you the Wishlist view.

![Fab window Wishlist icon](https://dev.epicgames.com/community/api/documentation/image/f5336a3e-7811-45fd-b60a-8853df9c355d)

By default this view shows you all the products where you clicked on the Wishlist icon on the product tile in the Fab window.

![Fab window Wishlist view](https://dev.epicgames.com/community/api/documentation/image/1a808bf5-0ef0-42c1-a147-51ebcbe0c1c8)

_Click image for full size._

```json
{
  "type": "include",
  "excerpt_id": 2468,
  "excerpt_assignment_id": 2456,
  "blocks": [
    {
      "type": "paragraph",
      "content": "There are a number of filter and sort options available to you to manage your wishlist:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "You can use the Search bar to find specific products.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "You can filter your wishlist by using the product type panel on the left; only product types where you have at least one matching product wishlisted are shown.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "You can filter your wishlist using any of the standard filter menu options.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "You can sort your wishlist by title, rating, or price.",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "rBP0",
  "settings": {
    "is_hidden": false
  }
}
```

## Cart View

You can view your cart by clicking on the **Cart** icon in the Discover, My Library, or Wishlist view, or by clicking **View in cart** on a [product preview](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3#product-preview).

![Fab window Cart icon](https://dev.epicgames.com/community/api/documentation/image/0d85ef78-2b35-4ad6-8ad4-1e41f6d2cec8)

Your cart shows a summary of the products you have selected for purchase. You can review your purchases, or remove any you no longer want. When you are satisfied, you can click **Checkout** to pay for your products.

![Fab window Cart view](https://dev.epicgames.com/community/api/documentation/image/865313ee-746a-4736-946a-a251d07ec535)

_Click image for full size._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Prices will display in USD by default. If you are logged in to Fab, then prices will display in your local currency.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26265926,
      "caption": "Prices will display in USD by default. If you are logged in to Fab, then prices will display in your local currency.",
      "alt_text": "Fab window Cart view CA$ currency",
      "image": {
        "id": 26265926,
        "file_name": "fab-plugin-checkout-currency.png",
        "file_size": 417894,
        "content_type": "image/png",
        "created_at": "2025-11-13T18:23:12.563+00:00",
        "height": 1280,
        "width": 3840,
        "storage_key": "cefa101b-2a07-4eaa-89a7-776d03880b54",
        "context": "documentation"
      },
      "storage_key": "cefa101b-2a07-4eaa-89a7-776d03880b54",
      "context": "documentation",
      "width": null,
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

## Fab Settings

The **Fab Settings** window provides a way for you to control some of the basic functions of the Fab window.

![Fab settings window](https://dev.epicgames.com/community/api/documentation/image/8fbd0a82-f99d-4c5d-a6ed-ac37c7608a93)

**General**

- **Enable Debug Options:** This checkbox enables the Chrome debug options for Fab.
- **Cache Directory Path:** This field provides a way for you to set the Fab cache location. The default path is: `C:/Users/[AccountName]/AppData/Local/Temp/FabLibrary` You can click the **ellipse (...)** next to the field to browse for a location on your local device.
- **Cache Directory Size:** This field shows you the size of the current Fab cache in bytes. You can click **Clean Directory** to empty the cache.

**Megascans**

- **Preferred Quality Tier:** You can use this field to pick your preferred quality for Megascans assets. Your options are: Low Medium (default) High Raw
