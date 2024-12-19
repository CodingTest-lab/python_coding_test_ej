def solution(s):
    # 공백을 기준으로 
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + " " + str(max(arr))