import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split

# Tải tập dữ liệu EMNIST
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Chuẩn hóa giá trị pixel về [-1, 1]
])

# Tải EMNIST dataset
emnist_trainset = datasets.EMNIST(root='./data', split='letters', train=True, download=False, transform=transform)

# Chia tập dữ liệu train thành train và validation
train_size = int(0.9 * len(emnist_trainset))
val_size = len(emnist_trainset) - train_size
emnist_trainset, emnist_valset = random_split(emnist_trainset, [train_size, val_size])

# Tải tập test
emnist_testset = datasets.EMNIST(root='./data', split='letters', train=False, download=False, transform=transform)

# Tạo DataLoaders
train_loader = DataLoader(emnist_trainset, batch_size=64, shuffle=True)
val_loader = DataLoader(emnist_valset, batch_size=32, shuffle=False)
test_loader = DataLoader(emnist_testset, batch_size=32, shuffle=False)

print("Training dataset size: ", len(emnist_trainset))
print("Validation dataset size: ", len(emnist_valset))
print("Test dataset size: ", len(emnist_testset))


# Định nghĩa mô hình CNN
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


# Tạo mô hình, định nghĩa hàm mất mát và tối ưu hóa
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Đang sử dụng thiết bị: {device}")
model = HandwritingCNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# Hàm huấn luyện mô hình
def train_model(model, train_loader, val_loader, criterion, optimizer, num_epochs=10, save_path="handwriting_model.pth"):
    for epoch in range(num_epochs):
        model.train()
        train_loss = 0

        # Thanh tiến trình với tqdm
        train_progress = tqdm(train_loader, total=len(train_loader), desc=f"Epoch {epoch + 1}/{num_epochs}")
        for images, labels in train_progress:
            images, labels = images.to(device), (labels - 1).to(device)  # Chuyển nhãn về 0-25
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()

            # Cập nhật tiến trình
            train_progress.set_postfix({"Batch Loss": loss.item()})

        # Đánh giá trên tập validation
        model.eval()
        val_loss = 0
        correct = 0
        total = 0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), (labels - 1).to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                val_loss += loss.item()
                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        # In thông tin cuối epoch
        print(f"Epoch [{epoch + 1}/{num_epochs}], Train Loss: {train_loss / len(train_loader):.4f}, "
              f"Validation Loss: {val_loss / len(val_loader):.4f}, Accuracy: {100 * correct / total:.2f}%")

        # Lưu trạng thái mô hình sau mỗi epoch
        torch.save(model.state_dict(), save_path)
        print(f"Mô hình đã được lưu tại {save_path}")


# Huấn luyện mô hình
train_model(model, train_loader, val_loader, criterion, optimizer, num_epochs=10, save_path="handwriting_vietnamese_model.pth")
