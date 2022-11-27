#!/usr/bin/python3

import requests
import datetime
import reverse_geocoder as rg

# Define URL
URL = 'http://api.open-notify.org/iss-now.json'

def main():
    """runtime code"""

    # Call the webservice
    httpresponse = requests.get(URL)
    # translate the json into python dictionary
    data = httpresponse.json()
    # slice the data
    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]
    timeoriginal = data["timestamp"]
    # convert the time into human readable format
    time = datetime.datetime.fromtimestamp(timeoriginal).strftime('%Y-%m-%d %H:%M:%S')
    coords_tuple= (lat, lon)
    result = rg.search(coords_tuple, verbose=False) #return a list
    city,country = result[0]["name"], result[0]["cc"]
    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {time}\nLon: {lon}\nLat: {lat}\nCity/Country: {city}, {country}")

if __name__ == "__main__":
    main()

 
