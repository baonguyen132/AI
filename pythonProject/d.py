import os
import shutil


def move_jpg_files(source_folder, target_folder):
    """Di chuyển tất cả các file .jpg từ source_folder vào target_folder."""

    # Kiểm tra thư mục nguồn có tồn tại không
    if not os.path.isdir(source_folder):
        print("Lỗi: Thư mục nguồn không tồn tại!")
        return

    # Tạo thư mục đích nếu chưa có
    os.makedirs(target_folder, exist_ok=True)

    # Lặp qua tất cả các file trong thư mục nguồn
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):  # Kiểm tra đuôi .jpg
            source_path = os.path.join(source_folder, file_name)
            target_path = os.path.join(target_folder, file_name)

            # Di chuyển file
            shutil.move(source_path, target_path)
            print(f"Đã di chuyển: {file_name} -> {target_folder}")


# Nhập đường dẫn thư mục nguồn
source_folder = input("Nhập đường dẫn thư mục nguồn: ").strip()
target_folder = os.path.join(source_folder, "jpg_folder")  # Thư mục đích

# Gọi hàm di chuyển file
move_jpg_files(source_folder, target_folder)
print("\n✅ Hoàn thành! Các file .jpg đã được chuyển vào thư mục:", target_folder)
