from __future__ import division, print_function, unicode_literals
import pickle

import numpy as np
import pandas as pd

np.random.seed(11)

dataset = pd.read_csv("AIChallenge_Training.csv")

y_price = dataset["Price"]
y_price_new = []
for item in y_price:
    item = item+""
    item_new = item.replace(",", "")
    y_price_new.append(float(item_new))
# print(y_price_new)

x_open = dataset["Open"]
x_open_new = []
for item in x_open:
    item = item+""
    item_new = item.replace(",", "")
    x_open_new.append(float(item_new))
# print(x_open_new)

x_high = dataset["High"]
x_high_new = []
for item in x_high:
    item = item+""
    item_new = item.replace(",", "")
    x_high_new.append(float(item_new))
# print(x_high_new)


x_low = dataset["Low"]
x_low_new = []
for item in x_low:
    item = item+""
    item_new = item.replace(",", "")
    x_low_new.append(float(item_new))
# print(x_low_new)

x_volume = dataset["Vol."]
x_volume_new = []
# sửa
for item in x_volume:
    item = item+""

    item_new = item.replace("K", "0")
    item_new = item_new.replace("M", "0000")
    item_new = item_new.replace(".", "")

    x_volume_new.append(float(item_new))

# print(x_volume_new)

x_change = dataset["Change %"]
x_change_new = []

for item in x_change:
    item = item+""
    item_new = item.replace("%", "")
    item_new = float(item_new) * 0.01

    x_change_new.append(float(item_new))

# print(x_change_new)

X = np.array([x_open_new, x_high_new, x_low_new, x_volume_new,x_change_new]).T
y = np.array([y_price_new]).T


def Linear_Regression():
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)


    A = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, y)
    w = np.dot(np.linalg.pinv(A), b)

    return w


if __name__ == '__main__':
    w = Linear_Regression()
    with open("G12_predict_1.csv", "wb") as model_file:
        pickle.dump(w, model_file)
    # print(g1)


