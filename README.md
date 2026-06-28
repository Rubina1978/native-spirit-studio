
# [native-spirit-studio](https://native-spirit-studio-3057c5b47433.herokuapp.com)

Developer: Hana Rubesova ([Rubina1978](https://www.github.com/Rubina1978))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Rubina1978/native-spirit-studio)](https://www.github.com/Rubina1978/native-spirit-studio/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Rubina1978/native-spirit-studio)](https://www.github.com/Rubina1978/native-spirit-studio/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Rubina1978/native-spirit-studio)](https://www.github.com/Rubina1978/native-spirit-studio)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://native-spirit-studio-3057c5b47433.herokuapp.com)


## Project Introduction and Rationale

Native Spirit Studio is an e-commerce platform inspired by ancient wisdom and traditions I have experienced and leart about during my time in South America within idigenous famly in Ecuador. It is also inspired by mindfulness, self-reflection, personal wellbeing, and a connection to nature. The website offers a carefully curated selection of products, including jewellery, home décor, wellness gifts, blankets, candles, and teas, designed to bring comfort, balance, and positive energy into everyday life.

In addition to the online store, the platform includes a personalised Mindfulness Journal feature that allows registered users to record reflections, thoughts, and moments of gratitude. This combination of shopping and self-reflection creates a unique experience that encourages users to focus not only on products but also on their personal wellbeing and self-development.

The target audience includes individuals who are interested in mindfulness, spirituality, wellness, self-care, and creating a calm and meaningful living environment. The website is designed to provide an easy and enjoyable shopping experience while also offering a space for personal reflection and growth.

The main goal of the project is to create a welcoming and user-friendly platform where visitors can discover products that support their wellbeing and, at the same time, engage in mindful practices through journaling. Features such as user accounts, profiles, order history, product management, shopping bag functionality, secure checkout, and personal journal entries provide users with a complete and engaging experience.

I chose this topic because mindfulness, gratitude, and self-reflection are subjects that I find personally meaningful. I wanted to create a project that combines practical e-commerce functionality with a more personal and positive purpose. Rather than building a generic online store, I wanted to develop a platform that encourages users to slow down, reflect, and connect with themselves while exploring products that support wellbeing and mindful living.

The project also provided an opportunity to combine a wide range of full-stack development skills, including database design, user authentication, CRUD functionality, payment processing, profile management, and responsive front-end design, within a theme that reflects my personal interests and values.


**Site Mockups**
*([amiresponsive](https://ui.dev/amiresponsive?url=https://native-spirit-studio-3057c5b47433.herokuapp.com), [techsini](https://techsini.com/multi-mockup), etc.)*

![screenshot](documentation/amiresponsive.png)

source: [native-spirit-studio amiresponsive](https://fireship.dev/amiresponsive?url=https://native-spirit-studio-3057c5b47433.herokuapp.com/)

> [!IMPORTANT]  
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "Boutique Ado".

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide a seamless and intuitive e-commerce experience for customers to browse, filter, and purchase products.
- Empower site owners to manage the store's inventory and customer orders efficiently.
- Encourage users to self-reflection, journaling, mindfulness and focus on own wellbeing

**Primary User Needs**
- Guest users need to browse products and checkout with ease.
- Registered customers need a streamlined shopping experience with account and order history features.
- Site owners need tools for inventory and order management.

**Business Goals**
- Drive sales by providing a user-friendly shopping experience.
- Build customer loyalty through personalized and efficient account features.
- Maintain an organized and up-to-date store inventory.
- Improve traffic to the site and awareness about the brand.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Product details, including name, price, size(where applicable), description, category, and images.
- Clear prompts and instructions for browsing, filtering, and purchasing.
- Order details, confirmation pages, status messages and email notifications.
- Secure payment processing using Stripe.
- Payment success emails sent to users.
- 404 page for lost users.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Products, Shopping, Personal Reflections Journal (only registered users), and Account sections.
- **Hierarchy**:
  - Prominent product categories and filters for easy navigation.
  - Shopping bag and checkout options displayed prominently for convenience.
  - Personal Reflection Journal displayed prominently for registered user

**User Flow**
1. Guest user browses the store → filters and sorts products by category, price, or name.
2. Guest user adds items to the Shopping bag → proceeds to checkout.
3. Guest user creates an account or logs in during checkout → completes purchase.
4. Returning customers log in → view past orders and track purchase history.
5. Registered users can navigate to Personal Reflections Journal, add reflection, update and delete via Reflection Form while reading randomly populated motivational quotes for better, more personal experience.
6. Site owners manage inventory → add, update, or delete products and categories.


#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

I used extention from [pallete.site](https://palette.site/) to generate my color palette.

- `#000000` primary text.
- `#17a2b8` primary highlights.
- `#DF2935` secondary text.
- `#FDCA40` secondary highlights.

![screenshot](documentation/color-palette/color-palette.png)

### Typography

- [Lato](https://fonts.google.com/specimen/Lato) was used throughout the site.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Canva](https://canva.link/o2hicsh64mpbmf9) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.png) | ![screenshot](documentation/wireframes/tablet-profile.png) | ![screenshot](documentation/wireframes/desktop-profile.png) |
| Home | ![screenshot](documentation/wireframes/mobile-landing.png) | ![screenshot](documentation/wireframes/tablet-landing-page.png) | ![screenshot](documentation/wireframes/desktop-landing.png) |
| Products | ![screenshot](documentation/wireframes/mobile-product-listing.png) | ![screenshot](documentation/wireframes/tablet-product-listing.png) | ![screenshot](documentation/wireframes/desktop-product-listing.png) |
| Product Details | ![screenshot](documentation/wireframes/mobile-product-detail.png) | ![screenshot](documentation/wireframes/tablet-product-details.png) | ![screenshot](documentation/wireframes/desktop-product-details.png) |
| Bag | ![screenshot](documentation/wireframes/mobile-shopping-bag.png) | ![screenshot](documentation/wireframes/tablet-shopping-bag.png) | ![screenshot](documentation/wireframes/desktop-shoppingbag.png) |
| Checkout | ![screenshot](documentation/wireframes/mobile-making-order.png) | ![screenshot](documentation/wireframes/tablet-making-order.png) | ![screenshot](documentation/wireframes/desktop-make-order.png) |
| Checkout Success | ![screenshot](documentation/wireframes/checkout-success.png) | ![screenshot](documentation/wireframes/tablet-checkout-success.png) | ![screenshot](documentation/wireframes/desktop-checkout-success.png) |
| Add Product | ![screenshot](documentation/wireframes/mobile-add-product.png) | ![screenshot](documentation/wireframes/tablet-add-product.png) | ![screenshot](documentation/wireframes/desktop-add-product.png) |
| Edit Product | ![screenshot](documentation/wireframes/mobile-edit-product.png) | ![screenshot](documentation/wireframes/tablet-edit-product.png) | ![screenshot](documentation/wireframes/desktop-edit-product.png) |
| Journal | ![screenshot](documentation/wireframes/mobile-journal.png) | ![screenshot](documentation/wireframes/tablet-journal.png) | ![screenshot](documentation/wireframes/desktop-journal.png) |
| Add reflection | ![screenshot](documentation/wireframes/mobile-add-reflection.png) | ![screenshot](documentation/wireframes/tablet-add-reflection.png) | ![screenshot](documentation/wireframes/desktop-add-reflection.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I would to see a list of products | so that I can select some to purchase before deciding to create an account. |
| As a guest user | I would like to be able to register, sign in out | so that I can enjoy the benefits of being a member. |
| As a user | I would like to have a place where I can do journaling by adding my reflection as and when I feel like to | so that I can improve my mental health through simple mindfulness action for my personal wellbeing. |
| As a customer | would like to be able to sort available products by category | so that I can easily identify best priced, rated and categorically sorter products. |
|As a customer | I would like to see my balance anywhere on the screen | so that I don't overspend|
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. |
| As a customer | see individual product details (description, price, image, etc.) | so that I can see what interests me. |
| As a customer | I would like to be able to change, adjust or delete products in my shopping bag using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. |
| As a customer| I would like to see any deals, clearance and special offers | so that I can take advantage of special savings and save money or buy more products |
| As a customer | I would like to view and manage my shopping bag | so that I can review, add, or remove items before proceeding to checkout. |
| As a customer | I would like to adjust the quantity of items in my shopping bag | so that I can modify my purchase preferences without leaving the shopping bag. |
| As a customer | I would like to remove items from my shopping bag | so that I can remove products I no longer wish to buy. |
| As a customer | I would like to proceed to checkout where I see my shopping bag items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. |
| As a customer | I would like get real time confirmation of payment | so that I can have a record of my transaction and order details. |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can confidently provide the information needed to make a purchase. |
| As a returning customer | I would like have personal profile | keep track of my purchases and add my payment details

## Acceptance Criteria 
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. |
| As a site owner | I would like add new products with a name, description, size(if applicable) price, images, and category | so that I can keep the store up to date. |
| As a site owner | I would like to update product details (name, price, size(if applicable), description, image, category) at any time | so that I can keep the store up to date. |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can keep the store up to date. |
| As a site owner | I would like to see all orders made on the website | so that I can track track customers purchases. |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/sign-out.png) |
| See All Categories | User can see all product categories | ![screenshot](documentation/features/categories.png) |
| Product List | Users can browse all available products with sorting, filtering by categories, and search functionality. | ![screenshot](documentation/features/product-listing.png) |
| Product Details | Displays detailed information about a selected product, including its name, description, price, an image, and available sizes. | ![screenshot](documentation/features/product-details.png) |
| Product Sorting | User can sort products by price, name, rating etc. | ![screenshot](documentation/defensive-programing/sorting-products-def-prog.png) |
| Add Amount of products to shopping bag | User can modify the amount of products to be added to a shopping bag | ![screenshot](documentation/features/update-quantity.png) |
| Add to Bag | Users can add items to their shopping bag, with support for selecting different sizes if applicable. | ![screenshot](documentation/features/add-to-shoppingbag.png) |
| View Bag | Users can view the contents of their shopping bag, adjust quantities, or remove items. | ![screenshot](documentation/features/view-bag.png) |
| Remove item from bag | Shopper can remove item from a shopping bag before proceeding to checkout | ![screenshot](documentation/features/remove-item-from-bag.png) |
| Shipping Details remembered | User shipping details of user are captured and remembered for user's future visit | ![screenshot](documentation/defensive-programing/shipping-address-remembering.png) |
| Checkout | Users can proceed to checkout, where they provide their delivery details and payment information using Stripe integration. | ![screenshot](documentation/features/checkout.png) |
| Order Confirmation | Users receive an on-screen and email confirmation with details of their purchase. | ![screenshot](documentation/features/order-confirmation.png) |
| Profile Management | Users can manage their profile information, including their default delivery address and order history. | ![screenshot](documentation/features/profile-management.png) |
| Order History | Users can view their past orders and access details of each order, including products purchased and the delivery status. | ![screenshot](documentation/features/order-history.png) |
| Product Management | Superusers can add, edit, and delete products from the site via a CRUD interface. | ![screenshot](documentation/features/product-management.png) |
| Journal | Users can register their email address to receive newsletters from the site. Currently, this only stores the email in the database. | ![screenshot](documentation/features/journal.png) |
| Managing Categories | Owner can manage categories to make sure products are correctly placed and easy to find for shoppers | ![screenshot](documentation\features\categories-for-owner.png) |
| List of all orders | Owner of the site can see all orders made | ![screenshot](documentation/defensive-programing/all-orders-placed.png) |
| Add Reflection with Motivational Quotes | Users can submit a message via the contact form, which stores their name, email, and message in the database. | ![screenshot](documentation/features/add-reflection-and-quotes.png) |
| Quotes | While writing reflection users can read one of the randomly selected quotes. Every time user gets to the form to submit reflection, different randomly chosen quote will display | ![screenshot](documentation/features/quotes.png) |
| User Feedback | Clear and concise Django messages are used to provide feedback to users when interacting with various features (e.g., adding products to the bag, checking out, etc.). | ![screenshot](documentation/features/user-feedback.png) |
| Heroku Deployment | The site is deployed to Heroku, making it accessible online for users. | ![screenshot](documentation/features/deployed-to-heroku.png) |
| SEO | SEO optimization with a sitemap.xml, robots.txt, and appropriate meta tags to improve search engine visibility. | ![screenshot](documentation/features/SEO.png) |
| Marketing | Social media presence is available in the footer using external links, as well as a Facebook Marketplace wireframe in the README for future integrations. | ![screenshot](documentation/features/marketing-socials.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/page-404.png) |

### Future Features

- **Product Reviews & Ratings**: Allow customers to leave reviews and rate products, with admin moderation. Display average ratings and review counts on product pages.
- **Wishlist**: Enable users to save products to a personal wishlist for future purchases. Notify users if wishlist items go on sale or are back in stock.
- **Product Recommendations**: Implement a "Other customers often also buy" feature to suggest related products.
- **Live Chat Support**: Provide real-time customer support through an integrated live chat or chatbot.
- **Discount Codes and Vouchers**: Allow promotions, discounts and marketing campaigns.
- **Countdown**: Implement countdown to specif events, promotions, discounts and other perks.
- **Membership Club**: Implement Membership scheme where customers will be encouranged to become members of the club with perks such as get notified first about new arrivals, promotions, discounts.
- **Loyalty Program**: Introduce a points-based loyalty system where customers earn points for purchases, which can be redeemed for discounts.
- **Newsletter**: Encourage customers to signup for Newsletter.
- **Contact Form**: Allow customers to communicate with the store via messaging in contact form.
- **Wellbeing and Mindfulness Blog**: Create a block app to provide customers with variety of topics on mental health, wellbeing, ancient and indigenous wisdom, spirituality, culture customs and other related topics.
- **Video Collection Channels**: Implement fuction to incorporate motivational, mindfulness, neuroscience documents and podcasts.
- **Paid for Extra Services**: Offer paid for additional services e.g. healing sessions, meditations, yoga.
- **Event calendar**: Implement calendar functions listing all upcoming events, talks and webinars on personal wellbeing, mindfulness and other niche topics.
- **Sponsorship**: Implement ways to benefit from spnsorships and display logos of companies sponsoring the site and its activities.
- **Product Inventory Alerts**: Notify customers when out-of-stock items are back in stock, or when low inventory is approaching.
-**Dark Scheme**Implement function of dark background if prefered by users.
- **Multi-Currency and Multi-Language Support**: Expand the application to support multiple currencies and languages to reach a global audience.
- **Product Bundles**: Offer discounted product bundles (e.g., buy 3 for the price of 2) or custom product kits.
- **Shipping Tracking Integration**: Provide real-time shipping updates and tracking information directly within the user’s order history.
- **Advanced Analytics Dashboard for Admin**: Offer an in-depth dashboard that displays sales trends, popular products, customer behavior, and more.
- **Mobile App**: Develop a mobile app for iOS and Android, providing users with a more optimized shopping experience on mobile devices.
- **Push up notifications**: Implement push up notifications to alert users about upcoming events, product promotions and others.
- **Affiliate Marketing**: Enable use of affiliate marketing for generating extra income.
- **Returns, Cookies and Privacy Policy**: Incorporate Return, Cookies and Privacy Policy for customers who need to return pruducts or are conscious about their personal data. Also as legislation requirements in the EU.
-**Display Awards achievemts and company history**: Implement display of awards, milestones and history of the business.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/Copilot-grey?logo=githubcopilot&logoColor=##000000)](https://github.com/copilot) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/favicon.io-grey?logo=fi&logoColor=209CEE)](https://favicon.io) | Generating the favicon. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERDs) are used to visualise the database architecture before creating models. Understanding the relationships between tables helps to design an efficient database structure and reduces the likelihood of issues later in development.

Django uses an Object Relational Mapper (ORM) to interact with the database. A model in Django functions as a Python class that defines the structure and behaviour of a database table. Relationships between models are created using fields such as ForeignKey, OneToOneField, and ManyToManyField.

- ForeignKey creates a one-to-many relationship. For example, one user can create many journal reflections.
- OneToOneField creates a one-to-one relationship. For example, one registered user has one user profile.
- Many-to-many relationships occur when multiple records from one model can relate to multiple records from another model. In this project, the relationship between Orders and Products is implemented through the OrderLineItem model, allowing one order to contain many products while also allowing a product to appear in many different orders.

## Custom models of Native Spirit Studio

Native spirit studio contains the following custom made models:

### Reflection(Journal) model

The Reflection model stores journal entries created by registered users. The relationship between User and Reflection is one-to-many, meaning one user can create multiple reflections while each reflection belongs to only one user. 

Reflection model contains:

- Automatically generated by Django PK
- user (ForeignKey)
- publish date (DateTimeField)
- mood (Charfield)
- happy moment (textfield)
- challenge (textfield)
- notes (textfield)

The user field is configured with on_delete=models.CASCADE, meaning that if a user account is deleted, all associated reflections are deleted as well. The creation date is generated automatically when a reflection is created. The mood field is limited to 100 characters, while the reflection content fields use TextFields to allow users to enter longer responses. The notes field is optional and can be left blank.

### ProductSize model

The ProductSize model was introduced to support products that are available in multiple sizes with different pricing, such as blankets and rugs. Products that do not require size variants remain unaffected by this functionality.

This approach allows products requiring size variants to store separate size, price, and stock information while maintaining a clean database structure.

The relationship between Product and ProductSize is one-to-many. A single Product can have multiple ProductSize records, while each ProductSize record belongs to only one Product. For example, a blanket may be available in Small, Medium, and Large variants, each with its own price and stock level.

Product model contains:
- Product (ForeignKey)
- Label (CharField)
- SKU (Charfield, optional)
- Price (DecimalField) 
- Stock (IntegerField)

In addition the model also includes meta to ensure the correct singular and plural names are displayed within Django administration panel.

## Core models

### UserProfile 

The UserProfile model extends Django's built-in User model and stores default delivery information and order history for registered users.

The model has a one-to-one relationship with the User model, meaning each user has one profile and each profile belongs to one user. The UserProfile model also has one-to-many relationships with the Reflection and Order models, as a single user can create multiple journal reflections and place multiple orders.

UserProfile model contains: 

- User (OnetoOneField) set to on_delete.models=CASCADE meaning if user is deleted all information related to the user is deleted
- default_phone_number (Charfield)
- default_street_address1 (CharField)
- default_street_address2 (CharField)
- default_town_or_city (CharField)
- default_county (CharField)
- default_postcode (CharField)
- default_country (CountryField), optional

The model allows authenticated users to save and update their default delivery details, improving the checkout experience by automatically populating order forms with previously stored information.
       
## Order

The Order model stores customer delivery details and order information after a successful checkout. It has a one-to-many relationship with the UserProfile model, meaning one user can place multiple orders, while each order belongs to a single user profile. The model also has a one-to-many relationship with the OrderLineItem model, as one order can contain multiple ordered products.

Order model contains:

- order_number (Charfield)
- user_profile (ForeignKey)
- full_name (Charfield)
- email (emailField)
- phone_number (Charfield)
- country (CountryField)
- postcode (Charfield)
- town_or_city (Charfield)
- street_address1 (Charfield)
- street_address2 (Charfield)
- county (Charfield)
- date (DateTimeField)
- delivery_cost (DecimalField)
- order_total (DecimalField)
- grand_total (DecimalField)
- original_bag (TextField)
- stripe_pid = (Charfield)

TThe model automatically generates a unique order number using UUID when an order is created. It also includes custom methods that calculate the order total and grand total whenever items are added or updated. Delivery costs are automatically applied when the order value is below the free delivery threshold of £50, while qualifying orders receive free delivery. The grand total is then calculated as the sum of the order total and any applicable delivery charge.

## OrderLineItem

The OrderLineItem model acts as a junction table between the Order and Product models. It stores information about individual products purchased within an order, including quantity, selected size, and calculated line total.

The model has a one-to-many relationship with both Order and Product. One order can contain multiple OrderLineItems, while one product can appear in multiple OrderLineItems across different customer orders. This structure creates a many-to-many relationship between Orders and Products through the OrderLineItem model.

The OrderLineItem model contains:

- order (ForeignKey)
- product (ForeignKey)
- product_size (CharField)
- quantity (IntegerField)
- size_price (DecimalField)
- lineitem_total (DecimalField)

The model overrides the save method to automatically calculate the line item total based on the selected product price, size-specific price (where applicable), and quantity ordered. This ensures that order totals remain accurate and are automatically reflected in the related Order model.

## Product

The Product model represents all products available within the Native Spirit Studio store. It has a many-to-one relationship with the Category model, meaning multiple products can belong to a single category, while each product belongs to only one category.

The Product model also has one-to-many relationships with the ProductSize and OrderLineItem models. A single product can have multiple size variants (for example, blankets and rugs available in Small, Medium, and Large sizes), and a single product can appear in multiple OrderLineItems across different customer orders.
Product model includes:

- category (ForeignKey)
- sku (CharField)
- name (CharField)
- description (TextField)
- has_sizes (BooleanField)
- available_sizes (CharField)
- size (CharField)
- price (DecimalField)
- rating (DecimalField)
- image (ImageField)

The model includes helper methods that determine whether a product has size variants and retrieve the lowest available size price. This allows products with multiple size options to display the most relevant pricing information while products without size variants continue to use their standard product price.

This structure provides flexibility for managing products with different size and pricing combinations while maintaining a consistent shopping experience for customers.

## Category

### Category Model

The Category model is used to organise products into groups, making it easier for customers to browse and filter products throughout the store.

The model has a one-to-many relationship with the Product model, meaning one category can contain multiple products, while each product belongs to a single category. For example, the Jewellery category may contain multiple products such as rings, necklaces, and bracelets.

The Category model contains:

- name (CharField)
- friendly_name (CharField)

The model includes a helper method that returns the category's friendly name. This allows categories to be stored using system-friendly names within the database while displaying more user-friendly names to customers throughout the website.

Entity Relationship Diagram (ERD) of the Native Spirit Studio database structure, created using `Mermaid` with assistance from `ChatGPT`.

![screenshot](documentation/entity_relationship_diagram/ERD.png)

User
 │
 │ 1:1
 ▼
UserProfile
 │
 │ 1:Many
 ▼
Order
 │
 │ 1:Many
 ▼
OrderLineItem
 ▲
 │ Many:1
 │
Product
 ▲
 │ 1:Many
 │
ProductSize

Category
 │
 │ 1:Many
 ▼
Product

User
 │
 │ 1:Many
 ▼
Reflection


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/Rubina1978/native-spirit-studio/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/agile_development/screenshot-projects.png)

### GitHub Issues

[GitHub Issues](https://github.com/Rubina1978/native-spirit-studio/issues?q=is%3Aissue%20state%3Aopen%20sort%3Arelevance-desc%20label%3Abug) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/Rubina1978/native-spirit-studio?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://github.com/Rubina1978/native-spirit-studio/issues?q=is%3Aissue%20state%3Aopen%20sort%3Arelevance-desc%20label%3Abug) | ![screenshot](documentation/agile_development/open-bugs.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/Rubina1978/native-spirit-studio?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://github.com/Rubina1978/native-spirit-studio/issues?q=is%3Aissue%20state%3Aclosed%20sort%3Arelevance-desc%20label%3Abug) | ![screenshot](documentation/agile_development/closed-bugs.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://native-spirit-studio-3057c5b47433.herokuapp.com/).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user-inserts-own-aws-access-key-id |        # only if using AWS
| `AWS_SECRET_ACCESS_KEY` | user-inserts-own-aws-secret-access-key |       # only if using AWS
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url-including-api-key-and-api-secret |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user-inserts-own-gmail-api-key |
| `EMAIL_HOST_USER` | user-inserts-own-gmail-email-address |
| `SECRET_KEY` | any-random-secret-key |
| `STRIPE_PUBLIC_KEY` | user-inserts-own-stripe-public-key |
| `STRIPE_SECRET_KEY` | user-inserts-own-stripe-secret-key |
| `STRIPE_WH_SECRET` | user-inserts-own-stripe-webhook-secret |
| `USE_AWS` | True |            # only if using AWS

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://native-spirit-studio-3057c5b47433.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (*verify your password and account*)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (*search for it at the top, if not*).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or `native-spirit-studio`
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - If your 16-character password contains *spaces*, make sure to remove them entirely.
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user-inserts-own-aws-access-key-id")  # only if using AWS
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user-inserts-own-aws-secret-access-key")  # only if using AWS
os.environ.setdefault("CLOUDINARY", "user-inserts-cloudinary-api-url")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("EMAIL_HOST_PASS", "user-inserts-own-gmail-host-api-key")
os.environ.setdefault("EMAIL_HOST_USER", "user-inserts-own-gmail-email-address")
os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user-inserts-own-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "user-inserts-own-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "user-inserts-own-stripe-webhook-secret")  # only if using Stripe Webhooks

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/Rubina1978/native-spirit-studio).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/Rubina1978/native-spirit-studio.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/Rubina1978/native-spirit-studio)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/Rubina1978/native-spirit-studio).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

During deployment, user registration creates accounts successfully but an unresolved issue occurs during the email verification process, resulting in a 500 error. SMTP configuration was tested successfully and emails can be sent through Django. If testing registration locally, emails are sent successfully and display in console, however, on the live site it shows error 500 and if attempt the registration with the same credentials again, an error shows on registration, that user with this credentials already exists. By researching Heroku CLI logs, this is understood to be due to the SMTP compatibility issue identified in production, email delivery could not be verified. This limitation is documented in the Known Issues section. As a temporary measure for assessment purposes, email verification was disabled to allow examiners to register and access all functionality.


There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Online payment services |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Sending payment confirmation emails |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations, correcting written content,as well as AI generated Hero Image on Native Spirit Studio |
| [GitHub Copilot](https://github.com/features/copilot) | Help with code logic, trace and resolve bugs |
| [Codex](https://openai.com/codex/) | Help with code logic, trace and resolve bugs |
| [Bootstrap Free Examples & Tutorial](https://mdbootstrap.com/docs/standard/navigation/footer/) | To gerate footer for my app Native Spirit Studio |
| [79 Positive Quotes To Uplift Yourself](https://wisdomquotes.com/positive-quotes/) | to generate motivational quotes on Journal App Add Reflection |
| [Mermaid](https://mermaid.js.org/) | with ChatGPT assistance generate ERD |
| [Canva](https://canva.com) | for creating wireframes and AI generated images for product listing |

### Media

- Images
   
    - [Pixabay](https://pixabay.com)
- Audio
   N/A
- Video
  N/A
- Image Compression
  N/A

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pixabay](https://pixabay.com/vectors/signpost-direction-choice-decision-2009312/) | 404 page image |
| [Canva](https://canva.link/o2hicsh64mpbmf9) | for creating wireframes and AI generated images for product listing |


### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank  to [Code Institute Discord community](https://discord-portal.codeinstitute.net) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my friends, for believing in me, and being tolerant for me not socialising as much with them during the busy periods
- I would like to thank trainer from EKC College Rachel Furlong, for supporting me in my career development change towards becoming a software developer and giving moral support in times when deadline was announced too close to completion date of the course.
- I would like to thank my mother for supporting me providing comfort when I thought I will give up and loose.

