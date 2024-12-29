def solution(brown, yellow):
    answer = []
    # yellow = n*m
    # brown = 4+2(n+m) -> n+m = (brown-4)/2
    # n, m을 구해서 전체 카펫 크기 구하기
    # 전체 카펫 크기는 n+2, m+2
    
    # yellow 가로 최소 길이 1
    range_n = int((brown-4)/2)
    # n의 최대값은 (brown-4)/2
    for n in range(range_n):
        if n * (range_n - n) == yellow:
            answer.append(n+2)
            answer.append(range_n - n + 2)
            break
    answer.sort(reverse=True)
    return answer