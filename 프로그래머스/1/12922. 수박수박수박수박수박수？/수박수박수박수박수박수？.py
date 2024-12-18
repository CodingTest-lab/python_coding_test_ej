def solution(n):
    answer = '수박'
    # n 이 홀수
    if n % 2 != 0:
        return answer * (n//2) + answer[0]
    # n 이 짝수
    else:
        return answer * (n//2)
    
    