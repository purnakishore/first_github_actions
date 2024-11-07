import sys
import os
import pymongo
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

connection_string = os.getenv('connection_string')
client = None

def load_weather_data(transformed_data):
    """ Load transformed data in MongoDB Database"""
    try:
        client = MongoClient(connection_string, server_api=pymongo.server_api.ServerApi(
        version="1", strict=True, deprecation_errors=True))

        database = client['GitHubActions']
        collection = database['weatherdata']

        collection.insert_one(transformed_data)

        client.close()
    except Exception as e:
        raise Exception("The following error occred :",e)
    
    finally:
        if client is not None:
            client.close()
