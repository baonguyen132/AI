import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# === 1. Đọc và tiền xử lý dữ liệu ===

# Đọc file dữ liệu
file_path = "AIChallenge_Training.csv"  # Thay đường dẫn tới file của bạn
data = pd.read_csv(file_path)

# Chuyển cột 'Date' sang kiểu datetime
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y')

# Loại bỏ ký tự '%' ở cột 'Change %' và chuyển sang float
data['Change %'] = data['Change %'].str.replace('%', '').astype(float)

# Xử lý các ký tự 'K' và 'M' trong cột 'Vol.'
def convert_volume(vol):
    if 'K' in vol:
        return float(vol.replace('K', '')) * 1_000
    elif 'M' in vol:
        return float(vol.replace('M', '')) * 1_000_000
    return float(vol)

data['Vol.'] = data['Vol.'].apply(convert_volume)

# Loại bỏ dấu phẩy trong các cột số và chuyển đổi sang float
for col in ['Price', 'Open', 'High', 'Low']:
    data[col] = data[col].str.replace(',', '').astype(float)

# Chuyển đổi cột 'Date' sang số ngày tính từ mốc (Epoch)
data['Days'] = (data['Date'] - data['Date'].min()).dt.days

# === 2. Chọn đặc trưng và mục tiêu ===

# Chọn các cột đặc trưng (Features) và cột mục tiêu (Target)
X = data[['Days', 'Open', 'High', 'Low', 'Vol.', 'Change %']]
y = data['Price']

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === 3. Huấn luyện mô hình ===

# Khởi tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# === 4. Lưu mô hình đã huấn luyện ===

# Lưu mô hình vào file
model_path = "linear_regression_model.pkl"
joblib.dump(model, model_path)
print(f"Mô hình đã được lưu tại: {model_path}")

# === 5. Tải lại mô hình đã lưu và kiểm tra ===

# Tải mô hình từ file
loaded_model = joblib.load(model_path)
print("Mô hình đã được tải thành công.")

# Kiểm tra dự đoán từ mô hình đã tải
y_pred_loaded = loaded_model.predict(X_test)
print(f"Dự đoán từ mô hình tải lại: {y_pred_loaded[:5]}")

# === 6. Dự đoán cho 250 ngày tiếp theo ===

# Tạo dữ liệu dự đoán cho 250 ngày tiếp theo
future_days = np.arange(data['Days'].max() + 1, data['Days'].max() + 251).reshape(-1, 1)
future_features = pd.DataFrame({
    'Days': future_days.flatten(),
    'Open': [data['Open'].mean()] * len(future_days),
    'High': [data['High'].mean()] * len(future_days),
    'Low': [data['Low'].mean()] * len(future_days),
    'Vol.': [data['Vol.'].mean()] * len(future_days),
    'Change %': [data['Change %'].mean()] * len(future_days),
})

# Tải mô hình đã lưu
model_path = "linear_regression_model.pkl"
loaded_model = joblib.load(model_path)

# Dự đoán giá trong 250 ngày tới
future_prices = loaded_model.predict(future_features)

# Kết quả
print(f"Dự đoán giá trong 250 ngày tới: {future_prices}")

# Xuất dữ liệu dự đoán ra file CSV (tùy chọn)
output_path = "future_predictions_250_days.csv"
future_features['Predicted_Price'] = future_prices
future_features.to_csv(output_path, index=False)
print(f"Dự đoán đã được lưu vào file: {output_path}")
