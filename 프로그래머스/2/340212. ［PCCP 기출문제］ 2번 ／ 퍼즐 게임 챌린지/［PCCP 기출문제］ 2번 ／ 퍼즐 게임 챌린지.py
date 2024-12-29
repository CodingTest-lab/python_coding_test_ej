# 이진 탐색이 필요한 경우
# 답이 특정 범위 안에 있다는 것이 확실할 때, 데이터가 정렬되어 있을때
def solution(diffs, times, limit):
    # level의 최소
    low = 1
    # level의 최대(숙련도가 난이도를 넘어가면 모든 문제를 현재 시간으로 풀 수 있으므로 최고의 경우, 이보다 크면 의미 없음)
    high = max(diffs)
    
    # 이진 탐색 : 찾는 값의 범위를 슬슬 줄여가는 형식
    # 찾는 값 : level
    # 범위 : 최소/최대 level
    while low <= high:
        # 중간 숙련도
        mid = (low + high) // 2
        # 해당 level이 제한시간 내에 문제를 풀수 있는지
        result = puzzle(diffs, times, limit, mid)
        
        # 결과가 성공이면 이 이상의 숙련도는 확인할 필요 없음
        if result: high = mid - 1
        # 결과가 실패면 이 이하의 숙련도는 확인할 필요 없음
        else : low = mid + 1
        
    return low

# diff를 순회하면서 제한시간 내에 특정 level이 문제를 풀 수 있는지 확인
def puzzle(diffs, times, limit, level):
    clear_time = 0   # 총 퍼즐 푸는 시간
    
    # diff를 순회
    for i in range(len(diffs)):
        # 1. 난이도 <= 숙련도 -> 현재 소요 시간만 사용
        if diffs[i] <= level : clear_time += times[i]
    
        # 2. 난이도 > 숙련도 -> (난이도-숙련도) * (현재 소요 시간+이전 소요 시간) + (현재 소요 시간) 사용
        else : clear_time += (diffs[i]-level) * (times[i]+times[i-1]) + times[i]
        
        # 총 퍼즐 푸는 시간은 limit을 넘으면 안됨
        if clear_time > limit : return False
    
    return True
    