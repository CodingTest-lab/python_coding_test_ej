def solution(mats, park):
    # 한변이 가장 큰 정수부터 깔 자리가 있는지 확인
    mats.sort(reverse = True)
    # 전체 행 길이
    row = len(park)
    # 전체 열 길이
    col = len(park[0])
    # 한변이 큰거부터 확인
    for mat in mats:
        # 전체 행과 전체 열을 돌면서
        for r in range(row):
            for c in range(col):
                # 해당 변만큼의 돗자리를 깔 수 있는지 확인
                if access(mat, park, r, c):
                    return mat
    # 아무 돗자리도 깔 수 없으면
    return -1

# 해당 범위 내에 해당 변의 돗자리를 깔 수 있는지 확인
def access(mat, park, start_r, start_c):
    # 끝점이 배열 범위를 벗어나면
    if start_r+mat > len(park) or start_c+mat > len(park[0]):
        return False
    
    # 행이 시작점부터 시작점+변길이 까지 반복
    for i in range(start_r, start_r + mat):
        # 열이 시작점부터 시작점+변길이 까지 반복
        for j in range(start_c, start_c + mat):
            
            # 해당 범위 내에 알파벳이 있다면 돗자리를 깔 수 없음
            if park[i][j] != '-1':
                return False
    
    # 위 조건을 아무것도 만나지 않는다면 돗자리를 깔 수 있음
    return True
                    