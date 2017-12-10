import numpy as np
import matplotlib.pyplot as plt
import math
import pandas
import sklearn as sk
import urllib2
import json

STATUS_CHOICES = [
    "airport",
    "amusement_park",
    "aquarium",
    "atm",
    "bus_station",
    "casino",
    "fire_station",
    "gas_station",
    "hindu_temple",
    "library",
    "mosque",
    "movie_theater",
    "museum",
    "night_club",
    "park",
    "police",
    "restaurant",
    "shopping_mall",
    "spa",
    "stadium",
    "taxi_stand",
    "train_station",
    "travel_agency",
    "zoo",
    "lodging",
    "meal_delivery",
    "meal_takeaway"
    ]

transport = ["travel_agency", "train_station", "taxi_stand", "airport", "bus_station"]
stay = ["lodging"]
food = ["restaurant", "meal_delivery", "meal_takeaway"]
access_pts = ["shopping_mall", "police", "fire_station", "gas_station", "atm"]
alts = ["aquarium", "amusement_park", "zoo", "stadium", "spa", "park", "hindu_temple", "library", "mosque", "movie_theater", "museum", "night_club", "casino"]

place_list = []

for i in STATUS_CHOICES:
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=28.6129167,77.2273157&radius=50000&type=' + i + '&sensor=true&key=AIzaSyC6eFunlAN73H7fKPeoypqh_CRcecda_PU'
    response = urllib2.urlopen(url)

    res = json.load(response)

    for j in res['results']:
        cat = ""
        if i in transport:
            cat = "transport"
        elif i in stay:
            cat = "stay"
        elif i in food:
            cat = "food"
        elif i in access_pts:
            cat = "access_points"
        elif i in alts:
            cat = "alts"

        place_list.append([j['geometry']['location']['lat'], j['geometry']['location']['lng'], cat, "DELHI", i])

print(len(place_list))

tf = open('delhi.txt', 'w')

for item in place_list:
    tf.write("%s\n" % item)




