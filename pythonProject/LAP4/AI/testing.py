from __future__ import division, print_function, unicode_literals

import pickle

import numpy as np
import pandas as pd

np.random.seed(11)

dataset = pd.read_csv("G12_predict_1.csv")

x_date = dataset["Date"]

y_price = dataset["Price"]
y_price_new = []
for item in y_price:
    item = str(item) + ""
    item_new = item.replace(",", "")
    y_price_new.append(float(item_new))
# print(y_price_new)

x_open = dataset["Open"]
x_open_new = []
for item in x_open:
    item = str(item) + ""
    item_new = item.replace(",", "")
    x_open_new.append(float(item_new))
# print(x_open_new)

x_high = dataset["High"]
x_high_new = []
for item in x_high:
    item = str(item) + ""
    item_new = item.replace(",", "")
    x_high_new.append(float(item_new))
# print(x_high_new)


x_low = dataset["Low"]
x_low_new = []
for item in x_low:
    item = str(item) + ""
    item_new = item.replace(",", "")
    x_low_new.append(float(item_new))
# print(x_low_new)

x_volume = dataset["Vol."]
x_volume_new = []
# sửa
for item in x_volume:
    item = str(item) + ""

    item_new = item.replace("K", "0")
    item_new = item_new.replace("M", "0000")
    item_new = item_new.replace(".", "")

    x_volume_new.append(float(item_new))

# print(x_volume_new)

x_change = dataset["Change %"]
x_change_new = []

for item in x_change:
    item = str(item) + ""
    item_new = item.replace("%", "")
    item_new = float(item_new) * 0.01

    x_change_new.append(float(item_new))

for item in x_change:
    item = str(item) + ""
    item_new = item.replace("%", "")
    item_new = float(item_new) * 0.01

    x_change_new.append(float(item_new))


def predict_price():
    # Tải model
    print_new =  []

    with open("G12_predict_1.csv", "rb") as model_file:
        w = pickle.load(model_file)
        print(w)

    for i in range(len(x_open_new)):

        X = np.array([1, x_open_new[i], x_high_new[i], x_low_new[i], x_volume_new[i], x_change_new[i]]).T
        # Tính giá dự đoán
        predicted_price = np.dot(X, w)
        print(predicted_price[0])
        y_price_new.append(predicted_price[0])

    return print_new


predict_price()
print(y_price_new)


