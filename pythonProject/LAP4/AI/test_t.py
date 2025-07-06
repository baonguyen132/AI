import numpy as np
import pandas as pd
import joblib

# Tải mô hình đã lưu
model_path = "linear_regression_model.pkl"
loaded_model = joblib.load(model_path)

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

# Dự đoán giá trong 250 ngày tới
future_prices = loaded_model.predict(future_features)

# Kết quả
print(f"Dự đoán giá trong 250 ngày tới: {future_prices}")
