from collections import deque

def solution(maps):
    # maps 리스트에서 'S', 'L', 'E' 찾기
    # enumerate를 사용해서 2차원 리스트안을 탐색
    for i, row in enumerate(maps):    # 리스트 내 각 행 탐색
        for j, cell in enumerate(row):   # 각 행의 문자열 하나씩 탐색
            if cell == 'S': begin = (i, j)
            elif cell == 'L': lever = (i, j)
            elif cell == 'E': exit = (i, j)
    
    # 시작 -> 레버까지 최단거리
    s_to_l = bfs(maps, begin, lever)
    if s_to_l == -1 : return -1
    # 레버 -> 출구까지 최단거리
    l_to_e = bfs(maps, lever, exit)
    if l_to_e == -1 : return -1
    
    return s_to_l + l_to_e

def bfs(maps, start, end):
    # 상하좌우 움직이는 변화량
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # need_visit 큐 생성
    q = deque()
    q.append(start)
    
    # 방문 처리 및 이동 거리 저장 디렉토리
    distance = {start:0}
    
    # q 에 값이 있는 동안 반복
    while q:
        # 첫번째 값 추출
        now = q.popleft()
        
        # 추출한 값이 도착점과 같다면(도착 지점에 갔다면) 거리 반환
        if now == end:
            return distance[now]
        
        # 상하좌우 돌아다님
        for dx, dy in move:
            # 추출한 값에서 상하좌우 움직인 좌표
            nx, ny = now[0] + dx, now[1] + dy
            
            # 움직인 좌표가 maps의 행과 열의 길이를 넘으면 안되고 움직인 좌표의 문자열이 'X' 즉 벽이면 안됨
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X':
                # 움직인 좌표가 visited에 있지 않다면
                if (nx, ny) not in distance:
                    # 움직인 좌표를 q에 추가
                    q.append((nx, ny))
                    distance[(nx, ny)] = distance[now] + 1
                    
    # 도착점에 도착하지 못하면 -1 리턴
    return -1
            
        