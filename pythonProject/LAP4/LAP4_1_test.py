import numpy as np
import pickle


def predict_price(area, rooms):
    # Tải model
    with open("AI/G12_predict_1.csv", "rb") as model_file:
        w = pickle.load(model_file)
        print(w)

    # # Tạo đầu vào X cho dữ liệu mới
    # X_new = np.array([1, area, rooms])
    #
    # # Tính giá dự đoán
    # predicted_price = np.dot(X_new, w)
    #
    # return predicted_price[0]  # Trả về giá trị đầu tiên trong mảng kết quả


area = 2000
rooms = 3
price = predict_price(area, rooms)
print(f"Dự đoán giá nhà: {price}")