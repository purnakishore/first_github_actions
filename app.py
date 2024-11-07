from data_handling.data import extract_weather_data,transform_weather_data
from data_handling.database_connection import load_weather_data
import sys


if __name__ == "__main__":
    try:
        weather_data = extract_weather_data()
        trasformed_data = transform_weather_data(weather_data)
        load_weather_data(trasformed_data)

        print("record inseted on MongoDB collection ")
        
    except Exception as e:
        raise Exception("The following error occured :",e)
