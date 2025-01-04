# '미로 탈출' 문제와 비슷한 형태로 풀이
# 차이점 : '미로 탈출' 문제는 이동한 한칸한칸을 모두 visited 큐에 넣었다면 
#     이 문제는 장애물 'D'나 보드 경계를 만날 때까지 이동할 수 있는 좌표를 visited 큐에 넣음
from collections import deque

def solution(board): 
    
    # board에서 'R'과 'G'의 위치 찾기
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'R': 
                start = (i, j)  # 시작 지점
            elif cell == 'G': 
                goal = (i, j)  # 목표 지점
    
    # BFS를 통해 최단 거리 계산
    return bfs(board, start, goal)


def bfs(board, start, end):
    # 상하좌우 움직이는 변화량
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # need_visit 큐 생성
    q = deque()
    q.append(start)  # 시작 좌표 추가
    
    # 방문 처리 및 이동 거리 저장 디렉토리
    distance = {start: 0}  # 시작 좌표의 이동거리 0으로 초기화
    
    # q에 값이 있는 동안 반복
    while q:
        # 첫번째 값 추출
        now = q.popleft()
        
        # 추출한 값이 도착점과 같다면 거리 반환
        if now == end:
            return distance[now]
        
        # 상하좌우 돌아다님
        for dx, dy in move:
            x, y = now  # 현재 좌표
            # 장애물 'D'나 보드 경계를 만날 때까지 이동
            while True:
                nx, ny = x + dx, y + dy
                
                # 이동이 가능한 경우 계속 이동
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != 'D':
                    x, y = nx, ny  # 좌표 업데이트
                    continue
                # 이동이 불가능한 경우 (장애물이나 경계에 도달)
                break
                
            # 최종 이동한 좌표가 방문하지 않은 경우 큐에 추가
            if (x, y) not in distance:
                q.append((x, y))
                distance[(x, y)] = distance[now] + 1  # 이동 거리 갱신
                    
    # 목표지점에 도착하지 못하면 -1 리턴
    return -1


# from collections import deque

# def solution(board):
#     # 상하좌우 이동
#     direction = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
    
#     # need_visit 큐에 로봇의 처음 위치 'R'을 추가
#     que = deque()
#     for x, row in enumerate(board):
#         for y, each in enumerate(row):
#             if each == 'R':
#                 # 처음위치 좌표와 이동거리 추가
#                 que.append((x, y, 0))
#     # visited 큐를 set으로 만들기(중복 방문 방지)
#     visited = set()
    
#     while que:
#         x, y, length = que.popleft()
        
#         # 이미 방문한 좌표면 다음 반복문 진행(need_visit 큐의 다음 값을 검사)
#         if (x, y) in visited:
#             continue
#         # 목표 위치면 이동거리 리턴
#         if board[x][y] == 'G':
#             return length
#         # 위의 아무 조건도 만나지 않으면 visited 큐에 추출한 좌표 추가(현재 위치)
#         visited.add((x, y))
        
#         # 상하좌우 이동
#         for diff_x, diff_y in direction:
#             # 현재 좌표(need_visit 큐에서 추출)
#             now_x, now_y = x, y
            
#             # 로봇이 장애물('D')에 부딪히거나 보드의 경계를 넘어설 때까지 계속 이동
#             while True:
#                 # 이동한 좌표
#                 next_x, next_y = now_x + diff_x, now_y + diff_y
                
#                 # 이동한 좌표가 행과 열의 길이를 넘지 않고(보드 내에 있고) 장애물이 아니면
#                 if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != 'D':
#                     # 이동한 좌표를 현재 좌표로 대입(좌표를 계속 이동)
#                     now_x, now_y = next_x, next_y
#                     continue
#                 # 이동 불가한 경우(보드를 벗어나거나 장애물을 만날 경우) need_visit 큐에 이동한 좌표 추가 및 이동거리 +1
#                 que.append((now_x, now_y, length + 1))
#                 break
                
#     # 모든 위치를 탐색해도 목표에 도달하지 못한 경우
#     return -1



