from collections import Counter
from matplotlib import pyplot as plt
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Tải tập dữ liệu EMNIST
transform = transforms.Compose([
    transforms.ToTensor(),  # Chuyển đổi ảnh thành tensor
    transforms.Normalize((0.5,), (0.5,))  # Chuẩn hóa giá trị pixel về [-1, 1]
])

# Tải tập dữ liệu EMNIST
emnist_trainset = datasets.EMNIST(root='./data', split='letters', train=True, download=True, transform=transform)
emnist_testset = datasets.EMNIST(root='./data', split='letters', train=False, download=True, transform=transform)

# Tạo DataLoader
train_loader = DataLoader(emnist_trainset, batch_size=32, shuffle=True)
test_loader = DataLoader(emnist_testset, batch_size=32, shuffle=False)

# Hiển thị 100 mẫu từ EMNIST theo dạng lưới 10x10
fig, axes = plt.subplots(10, 10, figsize=(15, 15))  # 10 hàng, 10 cột
fig.suptitle("100 mẫu chữ viết tay từ EMNIST", fontsize=18)

for i, idx in enumerate(range(100, 200)):  # Đảm bảo chỉ số hợp lệ trong khoảng 100 đến 199
    image, label = emnist_trainset[idx]
    ax = axes[i // 10, i % 10]  # Vị trí trên lưới
    ax.imshow(image.squeeze(), cmap="gray")
    ax.set_title(f"{label}", fontsize=8)  # Hiển thị label
    ax.axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Đặt khoảng cách
plt.show()

# Lấy nhãn của 100 hình ảnh đầu tiên từ chỉ số 100 đến 199
labels_100 = [emnist_trainset[idx][1] for idx in range(100, 200)]

# In các nhãn đầu tiên
print("100 nhãn đầu tiên:", labels_100)

# Đếm số lượng của từng nhãn
label_counts = Counter(labels_100)
print("Số lượng từng nhãn trong 100 hình ảnh đầu tiên:", label_counts)

# Thông tin về train_loader
print("Số lượng hình ảnh trong tập train:", len(emnist_trainset))
