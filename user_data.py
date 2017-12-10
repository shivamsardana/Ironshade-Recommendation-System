import pandas as pd
import ast
import random
import numpy as np

kochi = open('kochi.txt', 'r')
delhi = open('delhi.txt', 'r')

kochi_data = []
delhi_data = []

for i in kochi:
    il = ast.literal_eval(i[:-1])
    kochi_data.append(il)

for i in delhi:
    il = ast.literal_eval(i[:-1])
    delhi_data.append(il)

users = []
ds = len(delhi_data)
dk = len(kochi_data)

for i in range(250):
    a = random.randrange(0, 11)
    b = 10 - a

    j = random.sample(range(0, ds), a)
    k = random.sample(range(0, dk), b)

    d_data = np.array([delhi_data[r] for r in j])
    k_data = np.array([kochi_data[r] for r in k])
    users.append([x for x in d_data])
    users[i].extend([y for y in k_data])

users_np = np.array(users)
print(users_np.dtype)
print(users_np.shape)

np.save('users_data.txt', users_np, allow_pickle=True)

