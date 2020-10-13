# Importing Libraries--------------------------------------------------------------------------
from flask import Flask, jsonify, Response, json
import pymongo
from flask_restful import reqparse
from bson import ObjectId
#----------------------------------------------------------------------------------------------


# Used when creating our own MongoDB Database-----------------------------------------------------
#connection_url = 'mongodb://localhost:27017/'  # When only Mongo DB is running on Docker.
#connection_url = 'mongodb://db:27017/'   # When both Mongo and This application is running on
                                                # Docker and we are using Docker Compose
#--------------------------------------------------------------------------------------------------

# Connection with MongoDB Atlas (which stores our database on cloud) ----------------------
connection_url = 'mongodb+srv://sunidhi:79gOL4lexl5TH31e@cluster0.llgkq.mongodb.net/test'

app = Flask(__name__)

# Creating Connection with Mongo Database----------------------
client = pymongo.MongoClient(connection_url)
Database = client.get_database('Ecommerce')
Table = Database.Ecommerce
#--------------------------------------------------------------


# Base function------------------------------------------------
@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')

# Inserts the input data to database-------------------------------
@app.route('/insert/',methods = ['POST'])
def insert():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, help = 'Name')
        parser.add_argument('brand_name', type = str, help = 'Brand Name')
        parser.add_argument('regular_price_value', type = str, help = "Regular price of item")
        parser.add_argument('offer_price_value', type = str, help = "Offer price of item")
        parser.add_argument('currency', type = str, help="Currency")
        parser.add_argument('classification_l1', type = str, help = 'Classification 1 of item')
        parser.add_argument('classification_l2', type = str, help = 'Classification 2 of item')
        parser.add_argument('classification_l3', type = str, help = 'Classification 3 of item')
        parser.add_argument('classification_l4', type = str, help = 'Classification 4 of item')
        parser.add_argument('image_url', type = str, help = 'Image URL')

        args = parser.parse_args()

        queryObject = {}
        if(args['name'] is None):
            args['name'] = ""
        if(args['brand_name'] is None):
            args['brand_name'] = ""
        if(args['regular_price_value'] is None):
            args['regular_price_value'] = ""
        if(args['offer_price_value'] is None):
            args['offer_price_value'] = ""
        if(args['currency'] is None):
            args['currency'] = ""
        if(args['classification_l1'] is None):
            args['classification_l1'] = ""
        if(args['classification_l2'] is None):
            args['classification_l2'] = ""
        if(args['classification_l3'] is None):
            args['classification_l3'] = ""
        if(args['classification_l4'] is None):
            args['classification_l4'] = ""
        if(args['image_url'] is None):
            args['image_url'] = ""

        queryObject = {
            'name' : args['name'],
            'brand_name' : args['brand_name'],
            'regular_price_value' : args['regular_price_value'],
            'offer_price_value' : args['offer_price_value'],
            'currency' : args['currency'],
            'classification_l1': args['classification_l1'],
            'classification_l2': args['classification_l2'],
            'classification_l3': args['classification_l3'],
            'classification_l4': args['classification_l4'],
            'image_url' : args['image_url']     
        }
        query = Table.insert_one(queryObject)
        return "Insertion Successful"
    except Exception as e:
        return str(e)

# Searches the data from the database according to the filters provided----------------------
@app.route('/find/', methods = ['POST'])
def find():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type = str, help = 'ID')
        parser.add_argument('name', type = str, help = 'Name')
        parser.add_argument('brand_name' ,type = str, help = 'Brand Name')
        parser.add_argument('regular_price_value', type = str, help = "Regular price of item")
        parser.add_argument('offer_price_value', type = str, help = "Offer price of item")
        parser.add_argument('currency', type = str, help="Currency")
        parser.add_argument('classification_l1', type = str, help = 'Classification 1 of item')
        parser.add_argument('classification_l2', type = str, help = 'Classification 2 of item')
        parser.add_argument('classification_l3', type = str, help = 'Classification 3 of item')
        parser.add_argument('classification_l4', type = str, help = 'Classification 4 of item')
        parser.add_argument('image_url', type = str, help = 'Image URL')

        args = parser.parse_args()
        queryObject = {}
        if(args['_id'] is not None):
            queryObject['_id'] = ObjectId(args['_id'])
        if(args['name'] is not None):
            queryObject['name'] = args['name']
        if(args['brand_name'] is not None):
            queryObject['brand_name'] = args['brand_name']
        if(args['regular_price_value'] is not None):
            queryObject['regular_price_value'] = args['regular_price_value']
        if(args['offer_price_value'] is not None):
            queryObject['offer_price_value'] = args['offer_price_value']
        if(args['currency'] is not None):
            queryObject['currency'] = args['currency']
        if(args['classification_l1'] is not None):
            queryObject['classification_l1'] = args['classification_l1']
        if(args['classification_l2'] is not None):
            queryObject['classification_l2'] = args['classification_l2']
        if(args['classification_l3'] is not None):
            queryObject['classification_l3'] = args['classification_l3']
        if(args['classification_l4'] is not None):
            queryObject['classification_l4'] = args['classification_l4']
        if(args['image_url'] is not None):
            queryObject['image_url'] = args['image_url']
        query = Table.find(queryObject)
        output = {}
        i = 0
        for x in query:
            x['_id'] = str(x['_id'])
            output[i] = x
            i = i + 1
        return jsonify(output)
    except Exception as e:
        return str(e)

# Updates the existing data in the Database--------------------------------------------------------
@app.route('/update/', methods = ['POST'])
def update():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type = str, help = 'ID') # Criteria for update 
        parser.add_argument('name', type = str, help = 'Name')
        parser.add_argument('brand_name' ,type = str, help = 'Brand Name')
        parser.add_argument('regular_price_value', type = str, help = "Regular price of item")
        parser.add_argument('offer_price_value', type = str, help = "Offer price of item")
        parser.add_argument('currency', type = str, help="Currency")
        parser.add_argument('classification_l1', type = str, help = 'Classification 1 of item')
        parser.add_argument('classification_l2', type = str, help = 'Classification 2 of item')
        parser.add_argument('classification_l3', type = str, help = 'Classification 3 of item')
        parser.add_argument('classification_l4', type = str, help = 'Classification 4 of item')
        parser.add_argument('image_url', type = str, help = 'Image URL')

        args = parser.parse_args()
        if(args['name'] is None):
            args['name'] = ""
        if(args['brand_name'] is None):
            args['brand_name'] = ""
        if(args['regular_price_value'] is None):
            args['regular_price_value'] = ""
        if(args['offer_price_value'] is None):
            args['offer_price_value'] = ""
        if(args['currency'] is None):
            args['currency'] = ""
        if(args['classification_l1'] is None):
            args['classification_l1'] = ""
        if(args['classification_l2'] is None):
            args['classification_l2'] = ""
        if(args['classification_l3'] is None):
            args['classification_l3'] = ""
        if(args['classification_l4'] is None):
            args['classification_l4'] = ""
        if(args['image_url'] is None):
            args['image_url'] = ""
        query = Table.update_one(
                {"_id" : ObjectId(args['_id'])},
                {   
                    "$set" : {
                        'name' : args['name'],
                        'brand_name' : args['brand_name'],
                        'regular_price_value' : args['regular_price_value'],
                        'offer_price_value' : args['offer_price_value'],
                        'currency' : args['currency'],
                        'classification_l1': args['classification_l1'],
                        'classification_l2': args['classification_l2'],
                        'classification_l3': args['classification_l3'],
                        'classification_l4': args['classification_l4'],
                        'image_url' : args['image_url']  
                    }
                }
            )
        if query.acknowledged:
            return "Update Successful"
        else:
            return "Update Unsuccessful"
    except Exception as e:
        return str(e)

# Deletes the existing data from the database-----------------------------------------------------------
@app.route('/delete/', methods = ['POST'])
def delete():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type = str, help = 'ID')
        parser.add_argument('name', type = str, help = 'Name')
        parser.add_argument('brand_name' ,type = str, help = 'Brand Name')
        parser.add_argument('regular_price_value', type = str, help = "Regular price of item")
        parser.add_argument('offer_price_value', type = str, help = "Offer price of item")
        parser.add_argument('currency', type = str, help="Currency")
        parser.add_argument('classification_l1', type = str, help = 'Classification 1 of item')
        parser.add_argument('classification_l2', type = str, help = 'Classification 2 of item')
        parser.add_argument('classification_l3', type = str, help = 'Classification 3 of item')
        parser.add_argument('classification_l4', type = str, help = 'Classification 4 of item')
        parser.add_argument('image_url', type = str, help = 'Image URL')

        args = parser.parse_args()
        queryObject = {}
        if(args['_id'] is not None):
            queryObject['_id'] = ObjectId(args['_id'])
        if(args['name'] is not None):
            queryObject['name'] = args['name']
        if(args['brand_name'] is not None):
            queryObject['brand_name'] = args['brand_name']
        if(args['regular_price_value'] is not None):
            queryObject['regular_price_value'] = args['regular_price_value']
        if(args['offer_price_value'] is not None):
            queryObject['offer_price_value'] = args['offer_price_value']
        if(args['currency'] is not None):
            queryObject['currency'] = args['currency']
        if(args['classification_l1'] is not None):
            queryObject['classification_l1'] = args['classification_l1']
        if(args['classification_l2'] is not None):
            queryObject['classification_l2'] = args['classification_l2']
        if(args['classification_l3'] is not None):
            queryObject['classification_l3'] = args['classification_l3']
        if(args['classification_l4'] is not None):
            queryObject['classification_l4'] = args['classification_l4']
        if(args['image_url'] is not None):
            queryObject['image_url'] = args['image_url']
        
        query = Table.delete_many(queryObject)
        if query.acknowledged:
            return "Deletion Successful"
        else:
            return "Deletion Unsuccessful"

    except Exception as e:
        return str(e)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

