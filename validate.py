def valid(board, x, y, value, n=3):
    for i in range(n*n):
        if board[x][i]== value:
            return False
        if board[i][y]== value:
            return False
    large_row = (x//n) * n
    large_col = (y//n) * n
    for i in range(large_row, large_row + n):
        for j in range (large_col, large_col + n):
            if board[i][j]== value:
                return False
    return True