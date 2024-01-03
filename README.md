# GadgetGrove Website
> GadgetGrove is a comprehensive web application that serves as a versatile platform for buying and selling various products.
> Users can seamlessly interact with each other through a real-time chat, customize their profiles, provide additional external information, rate, comment, and review items, create and manage orders, and much more.


## Overview
> GadgetGrove represents a significant milestone in my journey to master Python, the Django framework, and database development.
> This project was designed to enhance my skills by applying the most up-to-date practices in designing an application from scratch, creating a well-structured database, and ultimately implementing the application using the knowledge I have acquired.


## Technology
 ### Key Components:
- Python 3.9+
- Django 4.2+

 ### Essential Django Features:
- Django ORM
- Django Authentication and Authorization
- Django Templates
- Django Forms and Validators
- Django Views and URLs

 ### Additional Components:
 - MySQL database
 - Redis
 - WSGI server


## Additional Tools
- **`Django Migrations:`**  Built-in system for managing database schema changes, eliminating the need for a separate tool.
- **`PyTest:`** Library offers concise syntax, fixtures for managing test data, and plugins for various tasks like mocking and code coverage.
- **`Django's built-in email functionality:`**  Django provides a convenient send_mail function for sending emails.


## Want to implement in the future
- **`Docker Compose:`** Configure a setup to create isolated environments for integration tests.
- **`Django Simple History:`**  Third-party package that tracks changes to models, providing functionality.
- **`Swagger:`** DRF has built-in support for generating Swagger documentation.


## Features
- **Login/Registration:** Users can create an account, log in, and reset their password if needed. Account creation requires email verification for security.
- **Orders history:** Users can view a history of their past orders, including details such as order date, order status, items purchased, total cost, seller number/email, and the ability to add an order review.
- **Order details:** Users can access detailed information about each individual order, including an itemized list, prices per item, seller info, recipient contacts, delivery address, and the ability to add an order review.
- **Personal comments section:** Users can see all their past comments or notes related to their orders, including details such as the comment date, rated item, and other information they provided.
- **Rate/Comment product:** Users have the ability to rate and leave comments on products they have purchased or just know about. Comment ratings don't require user authentication, so each user can rate items.
- **Profile settings:** Users can customize their profile settings, including personal information, change their username, upload a profile photo, provide contact information, social profiles, and other info.
- **User ads:** Users can see a list of all their products, update them, filter products by name, category, availability, and status, perform simultaneous actions like selecting all or several items, and delete.
- **Converstaions:** Users can see two lists of conversations, either for selling or buying products.
- **Up-to-date chat:** Users can engage in private real-time chat with sellers or customers, facilitating communication about products or transactions, enhancing the overall user experience.
- **Main page:** The main landing page of the website featuring all items, available categories, search bar and navbars with various functionality. 
- **Filtration:** Users can filter products based on category, brands, search bar and price range.
- **Item details:** Detailed information about each product includes images, specifications, ratings, seller information, features, and description, as well as customer reviews and related items. This page also provides the option to add item to the cart and send messages to the seller, requiring authentication.
- **Item comments section:** A section where users can view all comments and reviews about a specific product from other customers and leave their own comment.
- **Search:** A robust search functionality that allows users to quickly find products based on keywords.
- **Fast favorite/compare functionality:** Users can mark products as favorites or compare for quick access or future consideration.
- **Favorites:** Users can see a list of favorite products, including information about each item. They can manage the list by sorting it by category, seller, availability, and keywords. Additionally, users can delete items from the list and add them to the cart.
- **Compare section:** A feature that enables users to compare the specifications and details of multiple products side by side, compare items by category, and delete them from the comparison list.
- **Create products:** Allow users to create a product by providing various parameters and a description for it.
- **User Cart:** Users can easily manage their shopping carts, adding, deleting, and adjusting quantities of items with automated counting of the total price. The page also allows checking author information and other suggestions.
- **Order comment:** Users can comment their past orders.
- **Placing an order:** This page allows users to provide contact information, details about delivery, select a payment method, and add a comment to their order.
- **Seller catalog:** A catalog showcasing products from one seller, allowing users to filter products by category.
- **Seller reviews:** Users can see a list of all reviews from other customers related to both a specific seller and items they purchased.
- **Seller additional info:** Additional information about sellers, including contact details, business hours and an "About" section.
- **Encrypted password:** Django uses a secure user passwords hashing algorithm (PBKDF2) for enhanced security. 
- **Admin page:** An admin interface with tools and functionalities for platform admins to manage users, products and overall system settings.


## Want to implement in the future
- **Payment page:** Users can add their cards and convenient payment methods.
- **Discounts:** Users can see a list of all their personal discounts that they can apply when purchasing products.

