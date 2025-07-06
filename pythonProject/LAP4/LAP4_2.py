from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(11)

Customer_id = []
Age = []
Edu = []
Years_Employed = []
Income = []
Card_Debt = []
Other_Debt=[]
Defaulted = []
Address=[]
DebtIncomeRatio = []

with open("Cust_Segmentation.csv" , "r") as file:
    next(file)
    for line in file:
        line = line.strip()

        Customer_id_item, Age_item, Edu_item, Years_Employed_item, Income_item, Card_Debt_item, Other_Debt_item , Defaulted_item, Address_item, DebtIncomeRatio_item  = line.split(",")

        Customer_id.append(float(Customer_id_item))
        Age.append(float(Age_item))
        Edu.append(float(Edu_item))
        Years_Employed.append(float(Years_Employed_item))
        Income.append(float(Income_item))
        Card_Debt.append(float(Card_Debt_item))
        Other_Debt.append(float(Other_Debt_item))
        Defaulted.append(Defaulted_item)
        Address.append(Address_item)
        DebtIncomeRatio.append(float(DebtIncomeRatio_item))

import numpy as np

# random các center
def kmean_init_center(X, k):
    return X[np.random.choice(X.shape[0], k, replace=False)]

# Tính toán khoảng cách và gán nhãn cụm cho từng điểm
def kmeans_assign_labels(X, centers):
    D = np.zeros((X.shape[0], centers.shape[0]))
    for i in range(X.shape[0]):
        for j in range(centers.shape[0]):
            D[i, j] = np.sqrt(np.sum((X[i] - centers[j]) ** 2))
    return np.argmin(D, axis=1)

# Cập nhật lại các center
def kmean_update_centers(X, labels, K):
    centers = np.zeros((K, X.shape[1]))
    for k in range(K):
        Xk = X[labels == k]
        if len(Xk) > 0:
            centers[k, :] = np.mean(Xk, axis=0)
        else:
            centers[k, :] = centers[k, :]
    return centers

# điều kiện kết thúc
def has_converged(centers, new_centers, tol=1e-4):
    return np.allclose(centers, new_centers, atol=tol)

def kmeans(X, K):
    centers = kmean_init_center(X, K)
    labels = None
    it = 0
    while True:
        labels = kmeans_assign_labels(X, centers)
        new_centers = kmean_update_centers(X, labels, K)
        if has_converged(centers, new_centers):
            break
        centers = new_centers
        it += 1
    return centers, labels, it


def print_kmean(X, labels):
    colors = ['r', 'g', 'b' , 'y']

    for k in range(4):
        plt.scatter(X[labels == k, 0], X[labels == k, 1], s=10, color=colors[k], label=f'Cluster {k}')

    plt.xlabel("Years Employed")
    plt.ylabel("Age")
    plt.legend()
    plt.show()



X = np.array([Years_Employed, Age]).T
centers, labels, it = kmeans(X, 4)
print(centers)
print_kmean(X, labels)