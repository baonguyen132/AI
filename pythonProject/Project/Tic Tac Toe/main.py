import tkinter as tk
from tkinter import messagebox

from min_max import check_winner, best_move

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="#FFFF00")  # Màu nền tối cho cửa sổ chính

# Biến lưu trạng thái của trò chơi
board = [" " for _ in range(9)]
buttons = []

def is_board_full():
    return all(cell != " " for cell in board)
# Hàm xử lý khi nhấn nút
def button_click(index):

    if board[index] == " " and not check_winner(board , "X"):  # Chỉ cho phép đánh vào ô trống
        board[index] = "X"
        buttons[index].config(text="X", state="disabled", disabledforeground="#FF4500" )

        if check_winner(board, "X"):
            messagebox.showinfo("Kết quả", f"Người chơi thắng!")
            reset_game()
            return

        ai_move = best_move(board)
        if ai_move != -1:
            board[ai_move] = "O"
            buttons[ai_move].config(text="O", state="disabled", disabledforeground="#1E90FF" )

            if check_winner(board, "O"):
                messagebox.showinfo("Kết quả", f"AI thắng!")
                reset_game()
                return

    if is_board_full():
        messagebox.showinfo("Kết quả", f"Hoà!")
        reset_game()


# Hàm đặt lại trò chơi
def reset_game():
    global board
    board = [" "] * 9
    for button in buttons:
        button.config(text="", state="normal", bg="#FFFFFF")


# Tạo các nút trên bàn cờ
for i in range(9):
    button = tk.Button(root, text="", width=8, height=3,
                       font=("Arial", 24), bg="#FFFFFF", fg="#333333",
                       relief="solid", borderwidth=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)  # Tạo khoảng cách giữa các nút
    buttons.append(button)

# Bắt đầu vòng lặp giao diện
root.mainloop()