import urllib2 as ur
import pandas as pd
import numpy as np
import json
from sklearn import linear_model
import random
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

feature_matrix = pd.read_csv("feature_matrix.csv", header=0)
# from sklearn.cross_validation import train_test_split

user_places = np.load('users_data.txt.npy', allow_pickle=True)

X, y = feature_matrix.iloc[:, :-1], feature_matrix.iloc[:, -1]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

regr = linear_model.LinearRegression()
regr.fit(X, y)

lat = 28.6442032
lng = 77.1118042

response = ur.urlopen("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=en&latlng=" + str(lat) + "," + str(lng))
res = json.load(response)
res = res['results']
city = res[0]['address_components'][6]['long_name']
idx = []

for i in range(250):
    flag = False
    for j in range(10):
        if city.upper() == user_places[i][j][3]:
            flag = True
            break

    if flag is True:
        idx.append(i)

filtered_matrix = feature_matrix.iloc[idx, :]

# print(filtered_matrix)

d = np.random.randint(1, high=250, size=None)
user = feature_matrix.iloc[d, :-1]
pred_value = regr.predict(user)

filtered_matrix['ed'] = pd.Series(abs(filtered_matrix.y - pred_value))
sorted_matrix = filtered_matrix.sort('ed')

sort_mat = pd.DataFrame(sorted_matrix)

idx = []
for i in range(5):
    idx.append(int(sort_mat.iloc[i, 0]))

recommend = []
for i in idx:
    for j in range(10):
        if user_places[i][j][3] == city.upper():
            if user_places[i][j][0] != lat and user_places[i][j][1] != lng:
                recommend.append([user_places[i][j][0], user_places[i][j][1], user_places[i][j][2]])

import json

recommend = json.dumps(recommend)
print (recommend)
'''
sorted_matrix = filtered_matrix.sort('y')

#sorted_matrix = filtered_matrix.ix[(filtered_matrix.y-pred_value).abs().argsort()[:550]]
print(pred_value)
print(sorted_matrix)

yolo=

yolo=[]

for i in range(0,250):
    if(sorted_matrix[i].y == pred_value):
        yolo.append(i);

    else
        a=sorted_matrix[i].

'''




'''
print("Mean squared error: %.2f"
      % np.mean((pred_value - y_test) ** 2))

print('Variance score: %.2f' % regr.score(X_test, y_test))

# Plot outputs
plt.scatter(X_test.iloc[:, 0], y_test,  color='black')
plt.plot(X_test.iloc[:, 0], pred_value, color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

'''

