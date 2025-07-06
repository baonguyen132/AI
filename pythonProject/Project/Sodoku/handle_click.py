import random
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL.ImImagePlugin import number


def randomLocationHandle(k):
    return random.sample(range(0, 80), k)


def is_valid_sudoku(board):
    # Kiểm tra các hàng
    for row in board:
        if not is_valid_group(row):
            return False

    # Kiểm tra các cột
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False

    # Kiểm tra các ô 3x3
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [
                board[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if not is_valid_group(box):
                return False

    return True


def is_valid_group(group):
    # Lọc bỏ các ô trống (giá trị 0) và kiểm tra trùng lặp các số từ 1 đến 9
    numbers = [num for num in group if num != 0]
    if len(numbers) != 9:
        return False
    return len(numbers) == len(set(numbers))


def ask_for_number():
    root = tk.Tk()
    root.withdraw()

    user_input = simpledialog.askstring("Nhập số", "Vui lòng nhập một số:")

    if user_input is not None:
        try:
            # Chuyển đổi đầu vào sang số nguyên
            numbers = int(user_input)
            return numbers
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ.")
            return 0
