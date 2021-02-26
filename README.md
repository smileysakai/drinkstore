# drinkstore
Pre-requisties to run:
Follow steps as per (https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release)

Running this app:
Set python environment variables or follow step 2 of https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release.
Navigate to project (drinkstore) folder with cmd and run "python manage.py runserver".

Admin Credentials:
Username: Admin
Password: drinkstore

PayPal Sandbox details:
https://www.sandbox.paypal.com

Sandbox business account:
sb-y1ewq5206132@business.example.com
password: "s^6RbzW

Sandbox Customer Account:
sb-ic3im5206604@personal.example.com
Password: Bn=W/K5F
   
Resources used:
Styling - https://getbootstrap.com/
jQuery/JavaScript - https://jquery.com/ 
Web Framework - https://www.djangoproject.com/
PayPal API - https://developer.paypal.com/docs/business/javascript-sdk/javascript-sdk-reference/

Index Page:
![Alt text](media/readme/index.jpg?raw=true "Index")
*The index page will have 4 drinks available by default.*
Selecting a drink via the image or the link below the image will bring the user to that specific drink's page.
Below the available drinks is the user's cart (mini cart). Users will be able to add drinks to their cart for purchase.
This page also has an "add a new drink" link at the top left of the page.

Add New Drink Page:
![Alt Text](media/readme/add_drink.jpg?raw=true "Add_Drink")
*The fields for this form were generated using Django's "creating forms from models"*
Users will be able to add drinks, assigning it a category (list dropdown), name, price and image. 
The description and ingredients fields are optional.

Admin Pages:
![Alt Text](media/readme/admin_login.jpg?raw=true "Admin_Login")
*See admin login credentials above*

![Alt Text](media/readme/admin_index.jpg?raw=true "Admin_Index")
The admin page can be thought of as the backend.
The "drinks" object's foreign key, "category", is related to the "beverages" object.

![Alt Text](media/readme/admin_beverages.jpg?raw=true "Admin_Beverages")
Here shows what groups drinks can be a part of.
Additional "categories" for drinks may be added here.

Drink Page:
![Alt Text](media/readme/drink.jpg?raw=true "Drink")
The drink page will show the following information - name, price, category, product details, ingredients and the image for the product.
This page also shows the user's cart (mini cart) below.
Users can go back to the drinks list (index) via the top left link.
On the top right, users will be able to add a quantity of the drink to their cart.
If a drink is added to your cart, you will be directed back to the index page.
![Alt Text](media/readme/drink_cart_rel.jpg?raw=true "Drink_Cart_Rel")
If the user's cart already has an item from the drink they are looking at, the quantity and button will be reflect this.

Mini Cart:
![Alt Text](media/readme/mini_cart_empty.jpg?raw=true "Mini_Cart_Empty")
*Empty cart*
![Alt Text](media/readme/mini_cart_items.jpg?raw=true "Mini_Cart_Items")
*Cart with items*
If the cart is empty, it will display "no items" with a red background.
If the cart has items, the cart will display each cart item's price per unit, quantity, subtotal for the cart item, and the total cart price.
The checkout cart will direct the user to the checkout page where they will be able to process payment for their cart.

View Cart/Checkout Page:
![Alt Text](media/uploads/readme/cart_checkout.jpg?raw=true)
*If the cart is empty, the paypal payment button will not be available*
Users will be able to update quantities of their cart items and remove items form their cart.
Cart calculations will be reflected to any cart changes on this page.
Payment is done via paypal API. 
Paypal sandbox credentials above - use the business account to see payment received and the customer account to see payment executed.
*After payment, the cart does not remove all items; payment details are not saved to the database attached to a specific user. This may be expanded upon in the future.*

![Alt text](media/uploads/cola.jpg?raw=true)
