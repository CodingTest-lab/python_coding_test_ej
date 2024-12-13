def solution(slice, n):
    # n을 slice로 나눈 나머지가 0이면
    if n % slice == 0:
        return n // slice
    else:
        return (n // slice) + 1
    
# return ((n - 1) // slice) + 1