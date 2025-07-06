
numbersCustome = [1,2,3,4,5,6,7,8,9]

def is_safe(row,col,number,board):

    for i in range(9):
        if board[row][i] == number:
            return False

        # Kiểm tra cột
    for j in range(9):
        if board[j][col] == number:
            return False

    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == number:
                return False

    return True

def backtracking(index, boardSodoku):
    if index == 81:
        return True

    row = index // 9
    col = index % 9

    if boardSodoku[row][col] != 0:
        return backtracking(index + 1, boardSodoku)

    for num in numbersCustome:
        if is_safe(row, col, num, boardSodoku):
            boardSodoku[row][col] = num
            if backtracking(index + 1, boardSodoku):
                return boardSodoku
            boardSodoku[row][col] = 0

    return False