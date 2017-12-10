import numpy as np
import pandas as pd
import random

column_names = [
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
    "meal_takeaway",
    "transport",
    "stay",
    "food",
    "access_points",
    "alts"
]

user_places = np.load('users_data.txt.npy', allow_pickle=True)

feature_matrix = pd.DataFrame(data=np.zeros((250, 32)), columns=column_names)

for i in range(250):
    for j in range(10):
        f = user_places[i][j][2]
        f1 = user_places[i][j][4]
        feature_matrix.loc[i, f] += 1
        feature_matrix.loc[i, f1] += 1

p = 0.1
f = 1/p

for i in range(250):
    for j in column_names:
        if feature_matrix.loc[i, j] == 0:
            feature_matrix.loc[i, j] = random.randrange(0.0*f, 0.3*f, 0.1*f)/f


y = np.array([random.randrange(0.1*f, 0.5*f, 0.1*f)/f for i in range(250)])

feature_matrix['y'] = pd.Series(y)
print(feature_matrix.shape)

# np.save('feature_matrix.csv', feature_matrix, allow_pickle=True)

feature_matrix.to_csv("feature_matrix.csv")
