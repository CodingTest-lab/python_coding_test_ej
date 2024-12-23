def solution(board, h, w):
    n = len(board)   # board의 길이
    cnt = 0   # 같은 색으로 색칠된 칸 개수
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]  # h와 w의 변화량 리스트 -> 상하좌우로 움직일때 (0,1)(1,0)(-1,0)(0,-1)로 움직여야하는 거를 두개의 리스트로 분리
    for i in range(len(dh)):   # 상하좌우 네번 반복
        # 체크할 칸의 h,w좌표를 나타내는 변수(인덱스를 나타냄)
        h_check, w_check = h + dh[i], w + dw[i]
        # 체크할 칸이 0이상이고 board의 길이보다 작다면
        if 0 <= h_check < n and 0 <= w_check < n:
            # 체크할 칸이 처음 입력받은 h,w와 해당하는 색과 같다면
            if board[h][w] == board[h_check][w_check]:
                cnt += 1
    return cnt