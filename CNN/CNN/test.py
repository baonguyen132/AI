import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms
import numpy as np

# Định nghĩa lại mô hình (giống như trong quá trình huấn luyện)
class HandwritingCNN(nn.Module):
    def __init__(self):
        super(HandwritingCNN, self).__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 27)  # 27 lớp (26 chữ cái + 1 lớp không sử dụng)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x

# Tải mô hình đã huấn luyện
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = HandwritingCNN().to(device)
model.load_state_dict(torch.load("handwriting_vietnamese_model.pth", map_location=device))
model.eval()

# Tiền xử lý ảnh
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Đảm bảo ảnh là grayscale
    transforms.Resize((28, 28)),  # Đưa ảnh về kích thước 28x28
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Chuẩn hóa giá trị pixel về [-1, 1]
])

# Đọc ảnh từ file
img_path = 'Screenshot 2025-01-24 223329.png'  # Thay thế bằng đường dẫn đến ảnh của bạn
img = Image.open(img_path)

# Tiền xử lý ảnh
img_tensor = transform(img).unsqueeze(0).to(device)  # Thêm một chiều batch

# Dự đoán
with torch.no_grad():
    outputs = model(img_tensor)
    _, predicted = torch.max(outputs, 1)
    predicted_label = predicted.item()

# Hiển thị ảnh và kết quả dự đoán
plt.imshow(img, cmap='gray')
plt.title(f"Predicted Label: {predicted_label + 1}")  # Thêm 1 vì nhãn bắt đầu từ 0
plt.axis('off')
plt.show()

# In kết quả dự đoán
print(f"Predicted Label (from model): {predicted_label + 1}")  # Dự đoán nhãn của mô hình
