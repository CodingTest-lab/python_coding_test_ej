def solution(board, h, w):
    n = len(board)
    cnt = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(len(dh)):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                cnt += 1
    return cnt