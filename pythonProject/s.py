import numpy as np

# Dữ liệu từ bảng
enginesize = np.array([1.5, 2.0, 2.4, 3.5, 3.5, 3.5, 3.5, 3.7, 3.7])
co2emissions = np.array([136, 196, 221, 255, 244, 230, 232, 255, 267])

# Tính trung bình
mean_x = np.mean(enginesize)
mean_y = np.mean(co2emissions)

# Tính (x - mean_x), (x - mean_x)^2, (y - mean_y), (x - mean_x)(y - mean_y)
x_minus_mean = enginesize - mean_x
x_minus_mean_sq = x_minus_mean ** 2
y_minus_mean = co2emissions - mean_y
x_y_cov = x_minus_mean * y_minus_mean

# Tính tổng các giá trị để dùng trong tính toán
sum_x_minus_mean_sq = np.sum(x_minus_mean_sq)
sum_x_y_cov = np.sum(x_y_cov)

# Tính hệ số hồi quy
phi_1 = sum_x_y_cov / sum_x_minus_mean_sq  # Hệ số góc
phi_2 = mean_y - phi_1 * mean_x  # Hệ số chặn

# Dự đoán giá trị trên tập huấn luyện
predictions_train = phi_1 * enginesize + phi_2

# Tính |y - y| và (y - y)^2
absolute_errors = np.abs(co2emissions - predictions_train)
squared_errors = (co2emissions - predictions_train) ** 2

# In bảng chi tiết
print("No.\tEnginesize\tActual CO2\tPredicted CO2\t|y - ŷ|\t(y - ŷ)^2\t(x - x̄)\t(x - x̄)^2\t(y - ȳ)\t(x - x̄)(y - ȳ)")
for i in range(len(enginesize)):
    print(f"{i+1}\t{enginesize[i]:.2f}\t\t{co2emissions[i]:.2f}\t\t{predictions_train[i]:.2f}\t\t"
          f"{absolute_errors[i]:.2f}\t\t{squared_errors[i]:.2f}\t\t"
          f"{x_minus_mean[i]:.2f}\t\t{x_minus_mean_sq[i]:.2f}\t\t"
          f"{y_minus_mean[i]:.2f}\t\t{x_y_cov[i]:.2f}")

# In tổng MAE, MSE và các hệ số hồi quy
mae = np.mean(absolute_errors)
mse = np.mean(squared_errors)

print(f"\nTổng (x - x̄)^2: {sum_x_minus_mean_sq:.2f}")
print(f"Tổng (x - x̄)(y - ȳ): {sum_x_y_cov:.2f}")
print(f"\nHệ số góc (φ₁): {phi_1:.2f}")
print(f"Hệ số chặn (φ₂): {phi_2:.2f}")
print(f"\nMAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
