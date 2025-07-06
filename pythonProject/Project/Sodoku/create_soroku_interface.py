import tkinter as tk
from tkinter import messagebox

from Project.Sodoku.backTracking import backtracking
from Project.Sodoku.handle_click import randomLocationHandle, is_valid_sudoku, ask_for_number


def display_board(board, entries):
    for i in range(9):
        for j in range(9):
            # Xóa nội dung cũ và đặt giá trị mới từ board
            entries[i][j].delete(0, tk.END)
            entries[i][j].config(state="normal")
            if board[i][j] != 0:  # Chỉ hiển thị số nếu không phải là 0
                entries[i][j].insert(0, str(board[i][j]))
                entries[i][j].config(disabledforeground="red")
                entries[i][j].config(state="disabled")


def create_soroku_interface():
    window = tk.Tk()
    window.title("Sodoku Game")
    window.geometry("620x700")
    window.configure(bg="white")  # Màu nền cho giao diện
    window.resizable(False, False)

    entries = []
    for i in range(9):
        row = []
        for j in range(9):
            # Thiết lập màu nền và viền của ô
            bg_color = "#D3D3D3" if (i // 3 + j // 3) % 2 == 0 else "#FFFFFF"
            entry = tk.Entry(
                window,
                font=("Arial", 18),
                justify="center",
                relief="solid",
                borderwidth=1,
                background=bg_color,
                disabledbackground=bg_color,  # Màu nền khi trạng thái bị khóa
                state="disabled"  # Khóa ô nhập liệu
            )
            entry.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)  # Thêm khoảng cách giữa các ô
            row.append(entry)
        entries.append(row)

    for i in range(9):
        window.grid_rowconfigure(i, weight=1)  # Thiết lập hàng co dãn
        window.grid_columnconfigure(i, weight=1)  # Thiết lập cột co dãn

    def startGame():
        # Khởi tạo bảng trò chơi (9x9)
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
        randomNumberStart = randomLocationHandle(9)

        numbers = ask_for_number()

        if numbers != 0:
            # Chèn các số ngẫu nhiên vào bảng
            for i in range(1, 10):
                index = randomNumberStart[i-1]
                row = index // 9
                col = index % 9
                board[row][col] = i

            # Giải quyết bài toán Sudoku bằng backtracking
            board = backtracking(0, board)

            # Xóa các ô ngẫu nhiên
            random_numbers = randomLocationHandle(numbers)
            for i in random_numbers:
                row = i // 9
                col = i % 9
                board[row][col] = 0

            # Hiển thị bảng Sudoku
            display_board(board, entries)

    def check():
        board = [[int(entries[i][j].get()) if entries[i][j].get().isdigit() else 0 for j in range(9)] for i in range(9)]
        if is_valid_sudoku(board):
            messagebox.showinfo("Sodoku", "Chính xác!")
            for i in range(9):
                for j in range(9):
                    entries[i][j].config(state="normal")  # Cho phép chỉnh sửa tạm thời
                    entries[i][j].delete(0, 'end')  # Xóa nội dung cũ
                    entries[i][j].config(state="disabled")  # Khóa lại sau khi xóa
        else:
            messagebox.showinfo("Sodoku", "Còn lỗi")

    # Các nút điều khiển
    check_button = tk.Button(window, text="Start", command=startGame, font=("Arial", 14), bg="#4CAF50", fg="white")
    check_button.grid(row=9, column=0, columnspan=4, sticky="nsew")

    save_button = tk.Button(window, text="Check", command=check, font=("Arial", 14), bg="#4CAF50", fg="red")
    save_button.grid(row=9, column=4, columnspan=5, sticky="nsew")

    # Cho phép nút kiểm tra thay đổi kích thước theo chiều cao
    window.grid_rowconfigure(9, weight=1)

    # Xử lý đóng cửa sổ
    def on_closing():
        if messagebox.askyesno("Thoát", "Bạn có chắc muốn thoát không?"):
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)


    window.mainloop()


