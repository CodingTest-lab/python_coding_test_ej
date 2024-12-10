def solution(n):
    # n을 7의 배수면 그냥 몫을 리턴
    # n이 7의 배수가 아니면 몫 +1
    if n % 7 == 0 : return n // 7
    else : return (n // 7) + 1
    
# return (n - 1) // 7 + 1