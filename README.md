# API Project
## A list of contents
- [Intro](#intro)
- [Function](#function)
- [Backend](#backend)
- [Frontend](#frontend)
- [Postman Screenshots](#Postman-screenshots)
- [API docs Screenshots](#API-docs-screenshots)
- [Author](#author)
## Intro
 This repository contains my Colruyt api. I choose this subject because i work at colruyt as a student. This is not the only reason, during the periods that i work there i consumed a lot of knowledge about the products. So it was easy to implement this in an api.
## Function
First of all, because python is an easy language to learn, i choose to program my api in python and made use of that FastAPI library. 
In order to get it to be accessible in the cloud i made use of okteto that uses an image build by docker and hosted it through okteto.
The api features 2 GET and 1 POST endpoints. You can see if there is a colruyt nearby your location, you just need to fill in your zip-code and the nearest location will bee given.
You can also search for products based of the category, you fill in a category and all products available in that category will be displayed with the product name, category and price.
If you want to add a new product that is not available in our stores that you would really like to be present. You can request which product needs to be added.
## Backend
If you want to get access to the backend of the api, it is possible through the link below:  
Link: https://api-lucasleys.cloud.okteto.net  
In case that the api backend does not work anymore could be related to the api entering sleep mode. So if this happened, give me a heads up!
## Frontend
It is easier to communicate through a frontend with an api. So i made one using ALpineJS and it's available at: https://lucasleys.github.io/API_Project
In case of the frontend being down, you can find a screen below:
![image](https://github.com/lucasleys/API_Project/blob/main/images/frontend.png)
- Repository when the frontend can be found: https://github.com/lucasleys/API_Project

## Postman screenshots
- Screen of the result when the api is used for giving the nearest branch location through postman.  
![image](https://github.com/lucasleys/API_Project/blob/main/images/filiaal_suc.png)
- Screen of the result when the api fails to provide the nearest branch location through postman.  
![image](https://github.com/lucasleys/API_Project/blob/main/images/filiaal_fail.png)
- Screen of the result when the api is used for searching products based on category through postman.
![image](https://github.com/lucasleys/API_Project/blob/main/images/product_suc.png)
- Screen of the result when the api fails to provide products based on category through postman.
![image](https://github.com/lucasleys/API_Project/blob/main/images/product_fail.png)
- Screen of the result when the api is used for adding a wanted product through postman.
![image](https://github.com/lucasleys/API_Project/blob/main/images/newproduct_suc.png)
- Screen of the result when the api fails to add a new product through postman.
![image](https://github.com/lucasleys/API_Project/blob/main/images/newproduct_fail.png)
## API docs screenshots
- Screen of the result when the docs api is used for giving the nearest branch location.  
![image](https://github.com/lucasleys/API_Project/blob/main/images/docs_filiaal_suc.png)
- Screen of the result when the docs api fails to provide the nearest branch location.  
![image](https://github.com/lucasleys/API_Project/blob/main/images/docs_filiaal_fail.png)
- Screen of the result when the docs api is used for searching products based on category.
![image](https://github.com/lucasleys/API_Project/blob/main/images/docs_product_suc.png)
- Screen of the result when the docs api fails to provide products based on category.
![image](https://github.com/lucasleys/API_Project/blob/main/images/docs_product_fail.png)
- Screen of the result when the docs api is used for adding a wanted product.
![image](https://github.com/lucasleys/API_Project/blob/main/images/docs_post_suc.png)
- Screen of the result when the docs api fails to add a new product.
![image](https://github.com/lucasleys/API_Project/blob/main/images/docs_post_fail.png)
---
## Author
Lucas Leys 
[email](mailto:r0881339@student.thomasmore.be)  
