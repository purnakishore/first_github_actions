import sys
import os
import pymongo
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


# client = None

def load_weather_data(transformed_data):
    """ Load transformed data in MongoDB Database"""
    connection_string = os.getenv('connection_string')

    if not connection_string:
        print("Error: MogoDB connection string is not set")
        return
    print(f"Received connection string of length: {len(connection_string)}")

    if not connection_string.startswith("mongodb://") and not connection_string.startswith("mongodb+srv://"):
        print("Error: Connection string does not start with 'mongodb://' or 'mongodb+srv://'")
        return
    
    try:
        client = MongoClient(connection_string)

        print("MongoDB client created successfully")

        database = client['GitHubActions']
        collection = database['weatherdata']

        collection.insert_one(transformed_data)

        client.close()
    except Exception as e:
        raise Exception("The following error occred :",e)
    

