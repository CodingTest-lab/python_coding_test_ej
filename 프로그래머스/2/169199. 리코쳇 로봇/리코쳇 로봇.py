from collections import deque

def solution(board):
    # 상하좌우
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 행 길이, 열 길이
    board_r, board_c = len(board), len(board[0])
    # visited 큐(열길이 * 행길이의 2차원 리스트, Flase로 초기화)
    visited = [[False] * board_c for _ in range(board_r)]
    
    # 로봇의 처음 위치인 'R'의 좌표 추출
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 'R':
                start = [i, j]
    
    # 게임판 위의 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동
    def move_untill_wall(r, c, dx, dy):
        while True:
            r += dx
            c += dy
            # now_r, now_c = r + dx, c + dy
            # 게임판 위의 말이 행과 열의 길이를 벗어나면(지도를 벗어나면) 
            if r < 0 or r >= board_r or c < 0 or c >= board_c: 
                # 반복문 종료(이동 중단)
                break
            # 이동한 좌표가 장애물을 만난다면
            elif board[r][c] == 'D':
                # 반복문 종료(이동 중단)
                break
        
        # break로 while문을 빠져나온 위치는 이미 지도를 벗어나거나 장애물 위치
        # 멈춰야할 위치는 그 직전 위치이므로 반대로 한칸 돌아감
        r -= dx
        c -= dy
        return [r, c]
        
    
    # need_visit 큐
    q = deque()
    # 시작 좌표와 이동 거리를 추가
    q.append([start[0], start[1], 0])
    # 시작 위치 방문 처리
    visited[start[0]][start[1]] = True
    
    while q:
        r, c, dis = q.popleft()
        # 상하좌우 돌아다님
        for dx, dy in move:
            # 이동한 위치 리턴
            dr, dc = move_untill_wall(r, c, dx, dy)
            
            # 이미 지나간 위치면 다음 반복문 진행(need_visit 큐의 다음 값을 검사)
            if visited[dr][dc]:
                continue
                
            # 목표 위치면 현재 이동 거리 +1
            elif board[dr][dc] == 'G':
                return dis + 1
            
            # 단순 이동(추출한 visited에 없을때 visited큐에 추출한 값 추가 및 need_visit 큐에 이동한 좌표와 이동거리 추가)
            else:
                q.append([dr, dc, dis + 1])
                visited[dr][dc] = True 
            
    # 목표위치에 도달할 수 없다면
    return -1

