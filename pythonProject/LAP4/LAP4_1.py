from __future__ import division, print_function, unicode_literals
import numpy as np
import pickle  # Để lưu trữ model
import matplotlib.pyplot as plt

x_area = []
y_room = []
z_price = []

X = []
y = []
with open("priceHouse.txt", "r") as file:
    for line in file:
        line = line.strip()

        x, y, z = line.split(",")

        x_area.append(int(x))
        y_room.append(int(y))
        z_price.append(int(z))

    X = np.array([x_area, y_room]).T
    y = np.array([z_price]).T


def Linear_Regression():
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)


    A = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, y)
    w = np.dot(np.linalg.pinv(A), b)

    return w


if __name__ == '__main__':
    w = Linear_Regression()
    with open("model.csv", "wb") as model_file:
        pickle.dump(w, model_file)

    x0 = np.linspace(1000, 5000, 100)
    x1 = np.linspace(1, 5, 100)
    X0, X1 = np.meshgrid(x0, x1)
    y0 = w[0] + w[1] * X0 + w[2] * X1

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], y, color='r', label='Dữ liệu')  # Dữ liệu thực tế
    ax.plot_surface(X0, X1, y0, color='g', alpha=0.5)  # Mặt phẳng hồi quy

    # Nhãn trục
    ax.set_xlabel('Diện tích (sq ft)')
    ax.set_ylabel('Số phòng ngủ')
    ax.set_zlabel('Giá nhà ($)')
    plt.show()

