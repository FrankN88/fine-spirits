# Fine Spirits Shop

<h1 align="center">Fine Spirits :cocktail: | Milestone :four: Project </h1>

![Image of the mockup of the live website](readme_files/testing/mockup/mockup.png)

### [View live project here](https://fine-spirits.herokuapp.com/)
### [View the testing information here - (TESTING.md) ](TESTING.md)

## Overview

Fine Spirits shop is an ecommerce website allowing users to purchase bottles. It has been developed as milestone project 4 as part of the Code Institute - Diploma in Software Development (Full stack) course.
The website is designed to be responsive and accessible on all devices; being at the same time simple but pleasant.

---

## Table of Contents

1. [UX](#ux)
- [User Stories](#user-stories)
- [User Centered Design](#user-centered-design)
  - [Strategy](#strategy)
    - [User needs](#user-needs)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton and Wireframes](#Skeleton-and-Wireframes)

2. [DESIGN](#design)
- [Color scheme](#color-scheme)
- [Typography](#typography)
- [Imagery](#imagery)
- [Logo](#logo)

3. [DATABASE MODEL](#database-model)
- [Database model features](#database-model-features)

4. [FEATURES](#features)
- [Admin Feature](#Admin-Feature)
- [Design Features](#design-features)
- [Features left to implement](#features-left-to-implement)

5. [TECHNOLOGIES USED](#technologies-used)
- [Syntax](#syntax)
- [Frameworks, Libraries & Programs](#frameworks-libraries-&-programs)

6. [TESTING](#testing)
- [Testing document](TESTING.md)

7. [API](#api)
- [Stripe](#stripe)
- [Gmail for Django](#Gmail-for-Django)

8. [DEPLOYMENT](#deployment)
- [Heroku and Postgres DB](#Heroku-and-Postgres-DB)
- [Amazon Web Services](#amazon-web-services)
- [Github](#github)
  - [Forking the repository](#forking-the-repository)
  - [Creating a Clone](#creating-a-clone)

9. [CREDITS](#credits)

10. [REFERENCES](#references)

11. [ACKNOWLEDGEMENTS](#acknowledgements)

## UX

### **User stories**

 #### As an anonymous user/ first time visitor I want to:
  1. Be able to easily navigate throughout the site to visualise content and contacts.
  2. Check out a specific bottle, visualise the relative details and price.
  3. Purchase a bottle.
  4. Locate their social media links to see their followings on social media in order to be updated about their latest releases.

 #### As a registered user/frequent visitor I want to (in addition to the anonymous user functionalities):
  5. Be able to log in.
  6. Be able to log out.
  7. Be able to delete my account.
  8. Be able to add personal details.
  9. Be able to update personal details.
  10. Be able view my order history.

 #### As the admin I want to:
  11. Be able to add products to the site.
  12. Be able to update product details.
  13. Be able to delete products from the site. 
  14. Have unique access to all features.

  #### As the website owner I want to:
  15. Make the website as accessible and responsive as possible.
  16. Gain a better understanding of the audience by checking their feedback both via the social networks.
  17. Use reviews to increase customer satisfaction.
  18. Find the best way to allow communication bewteen customers and the organization.

---

## USER CENTERED DESIGN

### **Strategy**

- #### User needs

The main goal of this website is to increase more and more the popularity of the shop in order to increase sales too.
Registered users will be able to see their previous orders, their current ones and get discounts as the registration is treated like a loyalty card membership. In addition to that, as in most e-commerce shops, the convenience of having the personal data already saved is itself a good reason to register.
- The message "Register and get free delivery on orders over 50???" is visible also to registered user so that they have a reminder that when purchasing products and spending over 50??? the delivery is free.
- The website will show a bright palette as well as minimalistic but aesthetically pleasing imagery to invite users to check out the products.

- **Demographic:**
  - 18 + years of age.
  - Anyone who is interested in spirits.
  - Anyone who would like to purchase a bottle as a present for a friend.

The steps a new user would ideally take when landing onto the website are the following:
  - Explore the websites landing page, where the information will explain the user the reason to be of the site.
  - Create a new account.
  - Explore the additional features available to registered users.
  - Purchase the desired bottle.
  - Get the feedback of the purchase.
  - Log in/out.
  - Check out the links in the footer.

The website needs to enable the **User** to:
  - Easy access the features of the website.
  - Register and log in if further interested.
  - Get in touch with the website owner and/or admin.
  - Give feedback.

The website needs to enable the **Website owner and/or admin** to:
  - Develop an online presence .
  - Provide an easily navigable website for users.
  - Improve the website thanks to the contacts.

This will all be achieved through creating a clear and strong UI focusing on well structured content. Having a clear hierarchy will allow the user to navigate and use the functionality of the website without the need of instructions. Simplicity and UX friendly functionality will be the strongholds of the whole project. 

---

### **Scope**

- **Features within the design plan with highest priority:**
  - Minimal but functional and appealing homepage .
  - Navigation links clearly visible on the top of the website.
  - Responsive navigation bar.
  - Only allow registered users to create and manage their own accounts.
  - Only allow registered users to check out their previous orders.
  - Only allow registered users to delete their account.

- **Lower priority features that may not be included in the initial release of the website:**
  - The ability for logged in users to search the website database.
  - The possibility to leave comments.
  - Contact section to send an email to the Admin directly from the website (like emailJS).

---

### Structure

The information architecture was organized in a fluid and clear way in order to ensure that users could navigate through the site with ease and efficiency.

![Site Map](readme_files/wireframes/structure/structure.png)

---

### Skeleton and Wireframes
Wireframe mockups were created in Figma Workspace [Click here for final wireframes](readme_files/wireframes).
The mobile view is intentionally made disproportionate to show how the full page might look on a mobile screen.
Several style changes were made in the final project compared to the inital wireframe on [Figma](https://www.figma.com/ "Link to Figma page"). Those changes were mainly related to colours, font size, positioning on the page; all aimed at providing the best user experience and responsiveness. The desktop views represent the first wireframes while the tablet and mobile views the last ones, modified specifically for smaller devices.

---

## DESIGN

The design of the website was created to be as simple and harmonious as possible, not to distract the user with too many color schemes and trying to bring the focus onto the products.

### **Color scheme**

The colours used in this project are presented on a light background, to keep a minimalistic and tidy website, as well as keeping the color contrast the highest possible to facilitate the screen readers and make this site accessible to all. In addition to that there are also some brighter features thought specifically to draw the attention of the user to the main parts.
 
Please check out the colour Colour palette.
 <details><summary>Colour palette</summary>
    <img src="readme_files/colours/colours.png">
 </details>

---

### **Typography**

- The selected font for the whole project is [Poppins](https://fonts.google.com/specimen/Poppins) with [Sans-Serif](https://en.wikipedia.org/wiki/Sans-serif) as the fallback font in case, for any reason, the font will not be imported into the site correctly.

---

### **Imagery**

- For this specific project imagery has been kept simple in order to concentrate the work on the functionality of the app. Images have been selected from [Unsplash](https://unsplash.com/ "Link to Unsplash page").
- Other images come from my personal archive.

---

### **Logo**

- The favicon was created using [Favicon.io](https://favicon.io/favicon-converter/) and the logo used to create it was created using an online application called [Freelogodesign](https://it.freelogodesign.org/). It represents a simple glass/bottle with the "Fine Spirits" words.
 <details><summary>Logo</summary>
    <img src="static/img/logo.jpg">
 </details>

---

## Database Model

### Database model features

- The website is a data-centric one with html, javascript, css used with the bootstrap (version 5) framework as a frontend.
- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version (production).
- [Postgres](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- [SQLLite](https://www.sqlite.org/index.html) database was used for local development. 

- This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database.

![DB Data Structure](readme_files/testing/db_scheme/db_diagram.png)

---

## Features

The website has the following features based on:

1. A user not logged into the site
2. A regular user logged into the site
3. An admin user
The navigation buttons update depending on whether a user is logged in or not, and whether that user is the admin:

 Nav Link              |Not logged in  |Logged in as regular user|Logged in as admin
:-------------         |:------------- |:----------------|:------------- |
Home     |&#9989;        |&#9989;          |&#9989; |
Products           |&#9989;        |&#9989;          |&#9989; |
Product Detail           |&#9989;        |&#9989;          |&#9989; |
Product Management(Add Product)     |&#10060;       |&#10060;         |&#9989; |
Product Management(Edit Product)     |&#10060;       |&#10060;         |&#9989; |
Product Management(Delete Product)     |&#10060;       |&#10060;         |&#9989; |
My Profile             |&#10060;       |&#9989;          |&#9989; |
Order History         |&#10060;       |&#9989;          |&#9989; |
Log out               |&#10060;       |&#9989;          |&#9989; |
Register               |&#9989;        |&#10060;         |&#10060; |
Log in               |&#9989;        |&#10060;         |&#10060; |
Bag |&#9989;        |&#9989;          |&#9989; |
Checkout |&#9989;        |&#9989;          |&#9989; |
Checkout success |&#9989;        |&#9989;          |&#9989; |

<br>

### Admin Feature
There are a number of admin views that have been configured at https://fine-spirits.herokuapp.com/admin; They give excellent CRUD operations to the data in the Postgres database as well as search and filter options. They are as follows:

- Email addresses
![Email addresses](readme_files/admin/admin_emails.png)

- Users
![Users](readme_files/admin/admin_users.png)

- Orders
![Orders](readme_files/admin/admin_orders.png)

- Categories
![Categories](readme_files/admin/admin_categories.png)

- Products
![Products](readme_files/admin/admin_products.png)

- Sites
![Sites](readme_files/admin/admin_sites.png)

#### Admin Functionality in the website
- Other than through the default Django admin interface, products can be added/created, edited and removed (CRUD) directly from the website when entering with admin credentials. This feature facilitates the management of products thanks to a more friendly and direct user interface. This feature makes things easier for the website owner in case he/she needs to make changes on the products without having to access the Django admin interface.

- Add new product
![Add new product](readme_files/features/product_management/add_product.gif)

- Delete Product
![Delete Product](readme_files/features/product_management/edit_delete_products.png)

- Update/Edit product Details
![Update product details](readme_files/features/product_management/edit_delete_products.png)

<br>

### Design Features
Each page of the website features a consistent responsive navigational system:

<br>

#### Header
- The **Header** contains a conventionally placed **logo** at the top left of the page (clicking this will redirect users back to the home page) and **navigation bar** at the top right of the page. Hovering over the buttons in the navbar will trigger hover effect.
<ul>
    <li><strong>User stories covered by this feature:</strong>  
    </li>
    <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
    </li>
    <li><strong>2</strong> - Check out a specific bottle, visualise the relative details and price.
    </li>
    <li><strong>5</strong> - Be able to log in.
    </li>
    <li><strong>6</strong> - Be able to log out.
    </li>
    <li><strong>15</strong> - Make the website as accessible and responsive as possible.
    </li>
</ul>
  <details><summary>Header</summary>
    <img src="readme_files/features/gif/logo.gif">
  </details>

<br>

#### Navigation bar on smaller devices
- On smaller screens, the navbar links turn into an hamburger menu/toggle button in the top right corner of the page after the login and bag buttons.
<ul>
    <li><strong>User stories covered by this feature:</strong>  
    </li>
    <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
    </li>
    <li><strong>2</strong> - Check out a specific bottle, visualise the relative details and price.
    </li>
    <li><strong>15</strong> - Make the website as accessible and responsive as possible.
    </li>
</ul>
  <details><summary>Navbar on small devices</summary>
    <img src="readme_files/features/toggle_btn.png">
  </details>

<br>

#### Footer
- In the footer is embedded a pop up that warns about the legal age to access pages that sell alcoholic beverages. This is a legal requirement in many countries.
  <details><summary>POP UP</summary>
    <img src="readme_files/popup/over_18_popup.png">
  </details>
- The **Footer** contains the appropriate **social media icons**, linking users to the main social media pages of the shop. 
<ul>
    <li><strong>User stories covered by this feature:</strong>  
    </li>
    <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
    </li>
    <li><strong>4</strong> - Locate their social media links to see their followings on social media in order to be updated about their latest releases.
    </li>
    <li><strong>15</strong> - Make the website as accessible and responsive as possible.
    </li>
    <li><strong>16</strong> - Gain a better understanding of the audience by checking their feedback both via the social networks.
    </li>
    <li><strong>17</strong> - Use reviews to increase customer satisfaction.
    </li>
</ul>
  <details><summary>Footer</summary>
    <img src="readme_files/features/footer.png">
  </details>

<br>

#### Mailto
- In the footer, there is a **Mailto** embedded in the email. Hovering over the email will trigger hover effect.
<ul>
    <li><strong>User stories covered by this feature:</strong>  
    </li>
    <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
    </li>
    <li><strong>18</strong> - Find the best way to allow communication bewteen customers and the organization.
    </li>
</ul>
  <details><summary>Mailto</summary>
    <img src="readme_files/features/gif/hovering_links_footer.gif">
  </details>

<br>

#### Search Button 
- In the top right corner of every page, there is a **Search Button** . The customer can enter directly the name of the product he/she interested to purchase or the kind of spirit (e.g. Cognac). This improves the UX experience.
<ul>
    <li><strong>User stories covered by this feature:</strong>  
    </li>
    <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
    </li>
    <li><strong>2</strong> - Check out a specific bottle, visualise the relative details and price.
    </li>
    <li><strong>15</strong> - Make the website as accessible and responsive as possible.
    </li>
</ul>
  <details><summary>Search Button</summary>
    <img src="readme_files/features/gif/search_button.gif">
  </details>

<br>

#### Back to the top button
- **Back to the top button**  - This <strong>button</strong> :arrow_up: is present in the footer so that the user can comfortably click them to be redirected to the top of the page. This feature improves the quality of navigation, especially if using smartphones.
<ul>
    <li><strong>User stories covered by this feature:</strong>  
    </li>
    <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
    </li>
    <li><strong>15</strong> - Make the website as accessible and responsive as possible.
    </li>
</ul>
  <details><summary>Btn back to the top</summary>
    <img src="readme_files/features/gif/btn_up.gif">
  </details>

<br>

<dl>
  <dt><a href="index.html" target="_blank" alt="Quiz game Home Page">Home Page</a></dt>
     <ul>
        <li><strong>User stories covered by this feature:</strong>  
        </li>
        <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
        </li>
        <li><strong>4</strong> - Locate their social media links to see their followings on social media in order to be updated about their latest releases.
        </li>
        <li><strong>15</strong> - Make the website as accessible and responsive as possible.
        </li>
        <li><strong>16</strong> - Gain a better understanding of the audience by checking their feedback both via the social networks
        </li>
        <li><strong>17</strong> - Use reviews to increase customer satistaction.
        </li>
        <li><strong>18</strong> - Fino the best wav to allow communication bewteen customers and the organization.
        </li>
     </ul>

  <dd>The Home Page consists of the following elements:
     <ul>
          <li><strong>Page</strong> - Red banner with catchy phrase.
          </li>
          <li><strong>Page</strong> - Carousel with "Visit the shop" button in the middle.
          </li>
     </ul>
        <details><summary>Home</summary>
        <img src="readme_files/features/feature_devices/home_devices_feature.png">
        </details>
  </dd>

  <br>

  <dt><a href="login.html" target="_blank" alt="login Page">Login page</a></dt>
     <ul>
         <li><strong>User stories covered by this feature:</strong>  
      </li>
          <li><strong>5</strong> - Be able to log in.
      </li>
          <li><strong>6</strong> - Be able to log out.
      </li>
          <li><strong>7</strong> - Be able to delete my account.
      </li>
          <li><strong>11</strong> - Be able to add products to the site (if admin).
      </li>
          <li><strong>12</strong> - Be able to update product details (if admin).
      </li>
      </li>
          <li><strong>13</strong> - Be able to delete products from the site (if admin).
      </li>
      </li>
          <li><strong>14</strong> - Have unique access to all features (if admin).
      </li>
      </li>
          <li><strong>15</strong> - Make the website as accessible and responsive as possible
      </li>
     </ul>

  <dd>The Login page consists of the following elements:
     <ul>
          <li><strong>Login</strong> - Red banner with catchy phrase.
          </li>
          <li><strong>Anonymous user</strong> - Allows the user who does not want to register to keep checking anyway by clicking on the appropriate button. The ideal situation would be to have as many registered users as possible but it is always good to allow choice to those who do not want to register.
          </li>
          <li><strong>Register</strong> - It opens the registration page.
          </li>
     </ul>
         <details><summary>Login</summary>
         <img src="readme_files/features/feature_devices/login_devices_feature.png">
         </details>
  </dd>

  <br>

  <dt><a href="registration.html" target="_blank" alt="registration Page">Registration Page</a></dt>
     <ul>
         <li><strong>User stories covered by this feature:</strong>  
      </li>
          <li><strong>7</strong> - Be able to delete my account.
      </li>
          <li><strong>8</strong> - Be able to add personal details.
      </li>
          <li><strong>9</strong> - Be able to update personal details.
      </li>
          <li><strong>10</strong> - Be able view my order history.
      </li>
          <li><strong>15</strong> - Make the website as accessible and responsive as possible
      </li>
     </ul>

  <dd>The Registration page consists of the following elements:
     <ul>
          <li><strong>Banner</strong> - Red banner with catchy phrase.
          </li>
          <li><strong>Email</strong> - Type your email.
          </li>
          <li><strong>Repeat Email</strong> - Repeat your email for confirmation.
          </li>
          <li><strong>Username</strong> - Type your username.
          </li>
          <li><strong>Password</strong> - Type your password.
          </li>
          <li><strong>Repeat password</strong> - Repeat your password for confirmation.
          </li>
     </ul>
         <details><summary>Registration</summary>
         <img src="readme_files/features/feature_devices/register_devices_feature.png">
         </details>
  </dd>

  <br>

  <dt><a href="bag.html" target="_blank" alt="Bag">Bag</a></dt>
     <ul>
         <li><strong>User stories covered by this feature:</strong>  
      </li>
         <li><strong>2</strong> - Check out a specific bottle, visualise the relative details and price.
      </li>
          <li><strong>3</strong> - Purchase a bottle.
      </li>
          <li><strong>15</strong> - Make the website as accessible and responsive as possible
     </ul>

  <dd>The bag page consists of the following elements:
     <ul>
          <li><strong>Title</strong> - Shopping bag
          </li>
          <li><strong>Centrale element</strong> - The user will see the name of the added product(s), quantity, price and buttons to update and remove.
          </li>
          <li><strong>BTN Keep shopping</strong> - Button to go back to the products page to check out other bottles.
          </li>
          <li><strong>BTN secure checkout</strong> - Button to proceed to secure checkout.
          </li>
     </ul>
         <details><summary>Bag</summary>
         <img src="readme_files/features/feature_devices/bag_devices_feature.png">
         </details>
  </dd>

  <br>

  <dt><a href="products.html" target="_blank" alt="Products Page">Products Page</a></dt>
     <ul>
         <li><strong>User stories covered by this feature:</strong>  
      </li>
          <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
      </li>
          <li><strong>2</strong> - Check out a specific bottle, visualise the relative details and price.
      </li>
          <li><strong>15</strong> - Make the website as accessible and responsive as possible.
      </li>
     </ul>

  <dd>The Products page consists of the following elements:
     <ul>
          <li><strong>Title</strong> - Products.
          </li>
          <li><strong>Drop down btn</strong> - This button is for sorting by the elements.
          </li>
          <li><strong>Products</strong> - List of products in boostrap cards.
          </li>
     </ul>
         <details><summary>Products</summary>
         <img src="readme_files/features/feature_devices/products_devices_feature.png">
         </details>
  </dd>

  <br>

  <dt><a href="product_detail.html" target="_blank" alt="Product detail">Product Detail</a></dt>
     <ul>
         <li><strong>User stories covered by this feature:</strong>  
      </li>
          <li><strong>2</strong> - Check out a specific bottle, visualise the relative details and price.
      </li>
          <li><strong>15</strong> - 15. Make the website as accessible and responsive as possible.
      </li>
     </ul>

  <dd>The Product Detail page consists of the following elements:
     <ul>
          <li><strong>Product name</strong> - Product name with its description, category (e.g gin), alcohol % and measure (e.g 100 cl)
          </li>
          <li><strong>BTN quantity</strong> - Button to increase and decrease quantity up to a maximum of 15. This feature has been added to make it more realistic. Most bottle stores have in fact very limited stocks on spirits and legal requirements for selling online up to a certain quantity.
          </li>
          <li><strong>2 More buttons</strong> - Button to keep shopping and button to add to bag.
          </li>
     </ul>
         <details><summary>Product Detail</summary>
         <img src="readme_files/features/feature_devices/product_detail_devices_feature.png">
         </details>
  </dd>

  <br>

  <dt><a href="profile.html" target="_blank" alt="Profile">Profile</a></dt>
     <ul>
         <li><strong>User stories covered by this feature:</strong>  
      </li>
         <li><strong>5</strong> - Be able to login.
      </li>
         <li><strong>6</strong> - Be able to log out.
      </li>
      </li>
         <li><strong>7</strong> - Be able to delete my account.
      </li>
         <li><strong>8</strong> - Be able to add personal details.
      </li>
         <li><strong>9</strong> - Be able to update personal details.
      </li>
         <li><strong>10</strong> - Be able view my order history.
      </li>
     </ul>

  <dd>The Profile page consists of the following elements:
     <ul>
          <li><strong>Form</strong> - Form with default delivery information boxes.
          </li>
          <li><strong>BTN</strong> - Button to update information.
          </li>
          <li><strong>BTN</strong> - Button to delete your profile.
          </li>
          <li><strong>Order history</strong> - In the right part of the page you can see your order history complete of all details.
          </li>
     </ul>
         <details><summary>Profile</summary>
         <img src="readme_files/features/feature_devices/profile_devices_feature.png">
         </details>
  </dd>

  <dt><a href="news.html" target="_blank" alt="News">News</a></dt>
     <ul>
         <li><strong>User stories covered by this feature:</strong>  
      </li>
         <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
      </li>
         <li><strong>2</strong> - Check out a specific bottle, visualise the relative details and price.
      </li>
      </li>
         <li><strong>4</strong> - Locate their social media links to see their followings on social media in order to be updated about their latest releases.
      </li>
     </ul>

  <dd>The News page consists of the following elements:
     <ul>
          <li><strong>Title</strong> - Title of the with the number of new items
          </li>
          <li><strong>Item</strong> - You will be able to see the list of items and a more detailed description by clicking on them.
          </li>
     </ul>
         <details><summary>News</summary>
         <img src="readme_files/wireframes/desktop/news_page.png">
         </details>
  </dd>

  <dt><a href="posts.html" target="_blank" alt="Blogs">Blogs</a></dt>
     <ul>
         <li><strong>User stories covered by this feature:</strong>  
      </li>
         <li><strong>1</strong> - Be able to easily navigate throughout the site to visualise content and contacts.
      </li>
         <li><strong>2</strong> - Check out a specific bottle, visualise the relative details and price.
      </li>
      </li>
         <li><strong>4</strong> - Locate their social media links to see their followings on social media in order to be updated about their latest releases.
      </li>
     </ul>

  <dd>The Blogs page consists of the following elements:
     <ul>
          <li><strong>Title</strong> - Title of the with the number of new items
          </li>
          <li><strong>Categories</strong> - A list of categories with the possibility to filter.
          </li>
          <li><strong>Macro areas</strong> - Such as "Friends of Grappa", "We all love gin" etc...
          </li>
     </ul>
         <details><summary>Blogs</summary>
         <img src="readme_files/wireframes/desktop/blog_readme.png">
         </details>
  </dd>

  <br>

### Features left to implement

- Improved searching and filtering on the products page.
- The functionality to add and display multiple images on each product.
- API like EmailJS to facilitate communication between customers and shop owner.
- Downloading and implementing a Py currency package that would allow purchases in other currencies.
- A FAQ page.
- Login with social media accounts.
- A live chat to improve the UX experience.
- Implementing other payment systems like Paypal.

---

## TECHNOLOGIES USED

### **Syntax**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Markdown](https://www.markdownguide.org/basic-syntax/)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [JQuery](https://jquery.com/)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

### Frameworks, Libraries & Programs

- [Figma:](https://www.figma.com/login)
  - Figma was used to create the [wireframes](put link to wireframes) during the design process.

- [Font Awesome](https://fontawesome.com/)
  - Used to include icons.

- [Google Fonts](https://fonts.google.com/)
  - Used to import the three fonts used throughout the site xxxxxxxx.

- [GitHub](https://github.com/)
  - Used to host the entire repository for the project.

- [GitPod](https://www.gitpod.io/)
  - The code editor used to build the entire project.

- [TinyPNG](https://tinypng.com/)
  - Used this to compress the images used on the website to make files smaller.

- [Favicon](https://favicon.io/)
  - Used to generate the websites favicon logo of various sizes for different devices.

- [W3C Validator HTML](https://validator.w3.org/)
  - Validator for HTML.

- [W3C Validator CSS](https://jigsaw.w3.org/css-validator/)
  - Validator for CSS.

- [JSHint](https://jshint.com/)
  - This is a tool used to detect errors or potential problems within Javascript code, used to test and validate all Javascript written for this project.

- [Django](https://www.djangoproject.com/)
  - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- [Heroku](https://id.heroku.com/login)
  - Heroku is a cloud platform as a service (PaaS) supporting several programming languages.
  - The Heroku network runs the customer's apps in virtual containers which execute on a reliable runtime environment.

- [BrowserStack](https://www.browserstack.com/)
  - Test the functionality and appearance of the project on all main browsers.

- [W3Schools](https://www.w3schools.com/)
  - To check demos and explanations.

- [Stack overflow](https://stackoverflow.com/)
  - To find answers to most common problems.

- [Lambda Test](https://www.lambdatest.com/)
  - For cross-browser testing among the major browsers.

- [Postgres Db](https://www.postgresql.org/)
  - PostgreSQL is a powerful, open source object-relational database system.

- [PEP8 Online Check](http://pep8online.com/)
  - PEP8 online is an online validator for the PY Code.


---

## Testing
Testing information can be found in a separate testing :information_source: [file](TESTING.md "Link to testing file")

---

## API

### Stripe
To set up Stripe, proceed as follows:

1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in.
3. Under Developers, click on the API keys section.

![API keys](readme_files/api/api_key.png)

4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values.
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>

6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/, for example: https://fine-spirits.herokuapp.com/checkout/wh/

![Webhook](readme_files/stripe/wb_created.png)

8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send.
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>

11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting.
![Webhook](readme_files/stripe/webhook_successful.png)
12. For futher information please check Stripe Testing in the [(TESTING.md) ](TESTING.md) file.

<br>

### Gmail for Django

To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required:
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings.
2. Turn on 2-step verification and follow the steps to enable.
3. Click on app passwords, select Other as the app and give the password a name, for example Django.
4. Click create and a 16 digit password will be generated, note the password down.
5. In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password.
6. In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account.
7. Set and confirm the following values in the settings.py file to successfully send emails.
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>

8. You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku.
9. For futher information please check GMAIL testing in the [(TESTING.md) ](TESTING.md) file, bottom of the page (Other Features).

---

## Deployment

### Heroku and Postgres DB
To deploy this application to Heroku, run the following steps:

1. Create an account at heroku.com
2. Create an app, give it a name (for example fine-spirits), and select a region.
3. Under resources search for postgres, and add a Postgres database to the app.

![Heroku Postgres](readme_files/heroku/heroku_postgres.png)
    
4. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
5. Install the plugins dj-database-url and psycopg2-binary.
6. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
7. Create a Procfile with the text: web: gunicorn fine_spirits.wsgi:application for example.
8. In the settings.py ensure the connection is to the Heroku postgres database.
9. Ensure debug is set to false in the settings.py file.
10. Add localhost and fine-spirits.herokuapp.com to the ALLOWED_HOSTS variable in settings.py.
11. Run "python3 manage.py showmigrations" to check the status of the migrations.
12. Run "python3 manage.py migrate" to migrate the database.
13. Run "python3 manage.py createsuperuser" to create a super/admin user.
14. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
15. From the CLI login to Heroku using the command heroku git:remote -a fine-spirits
16. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a fine-spirits
17. Push the code to Heroku using the command git push heroku master.
18. Ensure the following environment variables are set in Heroku.

![Heroku Env variables](readme_files/heroku/heroku_vars.png)

19. Connect the app to GitHub, and enable automatic deploys from main

![Heroku Postgres](readme_files/heroku/heroku_connected.png)
    
20. Click deploy to deploy your application to Heroku for the first time
21. Click on the link provided to access the application
22. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

### Amazon Web Services
To set up AWS S3 Bucket, proceed as follows:

1. Create an account at aws.amazon.com
2. Open the S3 application and create an S3 bucket named "fine-spirits".
3. Uncheck the "Block All Public access setting".
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit.
5. Enable the setting, and set the index.html and the error.html values.
![AWS Static](readme_files/aws/aws_img1.png)
6. In the Permissions section, click edit on the CORS configuration and set the below configuration.
![AWS CORS](readme_files/aws/aws_img3_CORS.png)
7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings).
![AWS Bucket Policy](readme_files/aws/aws_img2_bucket_policy.png)
8. In the permissions section, click edit on the Access control list(ACL).
9. Set Read access for the Bucket ACL for Everyone (Public Access).
10. The bucket is created, the next step is to open the IAM application to set up access.
11. Create a new user group named "add_group_name".
12. Add the "AmazonS3FullAccess" policy permission for the user group.
![AWS Bucket Policy](readme_files/aws/aws_img4_amz_fullaccess.png)
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource" to the following:

<br><code>"Resource": [</code>
<br><code>"arn:aws:s3:::add_fine-spirits",</code>
<br><code>"arn:aws:s3:::add_fine-spirits/*"</code>
<br><code>]</code>

16. Give the policy a name and click "Create Policy".
17. Add the newly created policy to the user group.
18. Go to Users and create a new user
19. Add the user to the user group "add_group_name"
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup.
22. The user is now created with the correct user group and policy.
23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage.
![AWS Settings](readme_files/aws/aws_img5_settings.png)
24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account.
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files.
26. AWS S3 Stored images.
![AWS Bucket Policy](readme_files/aws/aws_images.png)
27. AWS S3 Stored static files.
![AWS Bucket Policy](readme_files/aws/aws_objects.png)

### Github

#### Forking the Repository
By forking the GitHub Repository a copy of the original repository is made on the GitHub account. To view and/or to make  changes without affecting the original repository: 
1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/FrankN88/fine-spirits "Link to GitHub Repo").
3. At the top of the repository, on the right side of the page, select "Fork".
4. You should now have a copy of the original repository in your GitHub account.

#### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login/ "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
4. Locate the [GitHub Repository](https://github.com/FrankN88/fine-spirits "Link to GitHub Repo").
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new gitPod workspace to be created from the code in github where you can work locally. 
Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process

---

## CREDITS

### Content
- Stack Overflow for guidance
- Psychological properties of text colour in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page") for the Boostrap features.

### Media
- Some images come from my personal archive.
- All the other Images were downloaded from [Unsplash](https://unsplash.com/ "Link to Unsplash page").

### Code
The developer consulted multiple sites in order to better understand the code that they were trying to implement. The following sites were used on a more regular basis:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [MDN Web Docs](https://developer.mozilla.org/en-US/ "Link to MDN Web Docs")
- [jQuery](https://jquery.com/ "Link to jQuery page")
- [Django](https://www.djangoproject.com/ "Link to Django project page")
- [Python](https://www.python.org/ "Link to Python page")

### Acknowledgements
- My mentor Mo Shami for continuous helpful feedback.
- Tutor support at Code Institute for their support.
- My family for opinions and feedback.

***

---

