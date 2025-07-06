import math

board = [" " for _ in range(9)]

def print_board():
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")

def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Hàng
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cột
        [0, 4, 8], [2, 4, 6]  # Đường chéo
    ]
    return any(b[c[0]] == b[c[1]] == b[c[2]] == player for c in win_conditions)

def heuric(board, player):
    i = 0
    # Kiểm tra các hàng
    for row in range(3):
        if board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2] == player:
            i+=1

    # Kiểm tra các cột
    for col in range(3):
        if board[col] == board[col + 3] == board[col + 6] == player:
            i+=1

    # Kiểm tra đường chéo
    if board[0] == board[4] == board[8] == player:
        i+=1

    if board[2] == board[4] == board[6] == player:
        i+=1

    return i


def evaluate(b):
    return heuric(b, "O") - heuric(b, "X")

def minimax(b, depth, is_maximizing):
    score = evaluate(b)
    if score == 1 or score == -1 or " " not in b:
        return score

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play():
    while " " in board:
        print_board()

        # Người chơi X đi
        move = int(input("Nhập vị trí của bạn (1-9): ")) - 1
        if board[move] != " ":
            print("Vị trí đã được chọn, hãy chọn vị trí khác.")
            continue
        board[move] = "X"

        if check_winner(board, "X"):
            print_board()
            print("Bạn thắng!")
            return

        # AI O đi
        ai_move = best_move()
        if ai_move != -1:
            board[ai_move] = "O"
            print(f"AI chọn vị trí {ai_move + 1}")

        if check_winner(board, "O"):
            print_board()
            print("AI thắng!")
            return

    print_board()
    print("Hòa!")

# Chạy trò chơi
play()
