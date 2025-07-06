from check_winner import check_winner
import math


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

def minimax(b, depth, alpha, beta, is_maximizing):
    score = evaluate(b)
    if score == 1 or score == -1 or " " not in b:
        return score

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, alpha, beta, False)
                b[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Cắt tỉa beta
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, alpha, beta, True)
                b[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Cắt tỉa alpha
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, -float('inf'), float('inf'), False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
