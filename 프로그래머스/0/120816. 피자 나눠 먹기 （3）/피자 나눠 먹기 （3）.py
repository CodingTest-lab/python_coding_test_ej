def solution(slice, n):
    # slice 가 n의 배수면 몫 반환
    if n % slice == 0:
        return n // slice
    else:
        return (n // slice) + 1

# 그냥 올림을 사용하는 문제
# from math import ceil
# def solution(slice, n):
#    return ceil(n/slice)
    
# math 의 ceil을 사용하지 않는 버전
# return ((n - 1) // slice) + 1

