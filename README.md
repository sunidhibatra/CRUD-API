# Description
A REST API using Python which allows the user to perform basinc CRUD (Create, Read, Update, Delete) operations on the Ecommerce-products Data. 
Ecommerce-products Database -
* _id (automatically assigned ObjectId)
* name
* brand_name
* regular_price_value
* offer_price_value
* currency
* classification_l1
* classification_l2
* classification_l3
* classification_l4
* image_url

## Deploy the API using Docker
You can host the API locally in Docker by using these steps:
* **Step 1:** Navigate [here](https://www.docker.com/get-started) and download the latest version of Docker. 
You can verify the installation by typing the following command in CMD
```docker -v```
* **Step 2:** Go to the directory which has *docker-compose.yml* file 
* **Step 3:** Run ```docker-compose build```
* **Step 4:** Run ```docker-compose run```
* **Step 5:** You can check the docker container, must have start running by ```docker ps```
**Note:** To stop any container from running you can use ```docker container stop docker <CONTAINER ID>```

## To access API on localhost
To see your API running go to the **Browser** and hit *127.0.0.1:5000/*


![successful](https://user-images.githubusercontent.com/34681138/95892700-87dae780-0da4-11eb-834c-8b17cfb1e6d7.PNG)

![successful_1](https://user-images.githubusercontent.com/34681138/95892864-c670a200-0da4-11eb-9d6f-034dd0114040.PNG)

For acessing the API you can download [POSTMAN](https://www.postman.com/downloads/)
To access API:
1. **Create/Insert:** *127.0.0.1:5000/insert/*
2. **Read/Search/Find:** *127.0.0.1:5000/find/*
3. **Update:** *127.0.0.1/update/*
4. **Delete:** *127.0.0.1/delete/*

## Use the API's
To use the API's open the *POSTMAN* application.
1. **Insert:** 
    1. Enter the URL (127.0.0.1/insert/)
    2. Select POST method.
    3. Go to the *Body* option and enter the keys and the corresponding values which needs to be inserted in the database.
    4. Hit the SEND button.
    5. You should get a response saying *INSERTION SUCCESSFUL*.
    ![insert](https://user-images.githubusercontent.com/34681138/95892991-f91a9a80-0da4-11eb-86f8-f3be0546221c.PNG)

2. **Find:** 
    1. Enter the URL (127.0.0.1/find/)
    2. Select POST method.
    3. Go to *Body* option and enter the keys and the corresponding values on which you want to filter the data.
    4. Hit the SEND button.
    5. You should retrieve the filtered data from the database in json format
    ![find](https://user-images.githubusercontent.com/34681138/95892999-fd46b800-0da4-11eb-95d2-eed118fe4d92.PNG)

3. **Update:**
    1. Enter the URL (127.0.0.1/update/)
    2. Select POST method.
    3. Go to *Body* option and enter the key -> *_id* and value -> *_id[value]* on which you want to update the value. Also enter the values for rest of the columns which you need to update.
    4. Hit the SEND button.
    5. You should get a response saying *UPDATE SUCCESSFUL*.
    ![update](https://user-images.githubusercontent.com/34681138/95893017-020b6c00-0da5-11eb-8294-fe330c412d2c.PNG)

4. **Delete:**
    1. Enter the URL (127.0.0.1/delete/)
    2. Select POST method.
    3. Go to *Body* option and enter the keys and value for which you want to perform delete operation.
    4. Hit the SEND button.
    5. You should get a response saying *DELETION SUCCESSFUL*.
    ![delete](https://user-images.githubusercontent.com/34681138/95893005-ff107b80-0da4-11eb-931c-60658c8a1f03.PNG)
