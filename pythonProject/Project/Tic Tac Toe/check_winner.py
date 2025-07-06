def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Hàng
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cột
        [0, 4, 8], [2, 4, 6]  # Đường chéo
    ]
    return any(b[c[0]] == b[c[1]] == b[c[2]] == player for c in win_conditions)