def solution(m, n, puddles):
    # 격자 모양으로 2차원 배열 생성(시작 좌표가 1,1 로 시작하므로 (N+1) * (M+1) 크기의 배열 생성) 
    road = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # 시작점 1로 초기화
    road[1][1] = 1
            
    # 웅덩이 좌표는 그 칸까지 가기 위한 방법의 수가 0이므로 0으로 지정
    for [x, y] in puddles:
        road[y][x] = 0
    
    # 2차원 배열을 돌면서 특정 셀의 값은 해당 셀의 왼쪽값 + 위쪽값
    for i in range(n+1):
        for j in range(m+1):
            # 해당 셀이 시작점이면 다음 반복문 실행
            if i == 1 and j == 1: continue
            # 웅덩이 좌표를 만나면 셀의 값은 0
            if [j, i] in puddles : road[i][j] = 0
            # 특정 셀의 값은 해당 셀의 왼쪽값 + 위쪽값
            else :
                road[i][j] = (road[i][j-1] + road[i-1][j]) % 1000000007
    
    return road[n][m] 