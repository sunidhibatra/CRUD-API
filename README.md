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
<img src = "images/successful.png">
![fig 1.2](images/successful_1.png)

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
    ![fig 2](images/insert.png)

2. **Find:** 
    1. Enter the URL (127.0.0.1/find/)
    2. Select POST method.
    3. Go to *Body* option and enter the keys and the corresponding values on which you want to filter the data.
    4. Hit the SEND button.
    5. You should retrieve the filtered data from the database in json format
    ![fig 3](images/find.png)
3. **Update:**
    1. Enter the URL (127.0.0.1/update/)
    2. Select POST method.
    3. Go to *Body* option and enter the key -> *_id* and value -> *_id[value]* on which you want to update the value. Also enter the values for rest of the columns which you need to update.
    4. Hit the SEND button.
    5. You should get a response saying *UPDATE SUCCESSFUL*.
    ![fig 4](images/update.png)

4. **Delete:**
    1. Enter the URL (127.0.0.1/delete/)
    2. Select POST method.
    3. Go to *Body* option and enter the keys and value for which you want to perform delete operation.
    4. Hit the SEND button.
    5. You should get a response saying *DELETION SUCCESSFUL*.
    ![fig 5](images/delete.png)
