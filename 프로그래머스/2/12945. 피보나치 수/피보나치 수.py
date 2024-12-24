def solution(n):
    # 피보나치 수열 : 각 숫자가 앞의 두 숫자의 합으로 정의되는 수열
    # 앞, 뒤를 정해놓고 시작
    number = [0, 1]
    # 1부터 시작해서 n번째 까지는 n-1번 움직여야 함
    for i in range(2, n+1):   # 2부터 시작하는 이유는 위 배열 뒤에 요소를 추가하려고
        number.append(number[i-1] + number[i-2])  # 앞 + 뒤한 합을 배열 뒤에 추가
    
    return number[n]%1234567

    # 위는 배열을 사용한 방법이고 아래는 그냥
    # if n == 0:
    #     return 0
    # elif n == 1: 
    #     return 1 
    # a, b = 0, 1
    # for _ in range(2, n + 1):
    #     a, b = b, a+b 
    #     # temp = b 
    #     # b = temp + a 
    #     # a = temp 
    # return b % 1234567

#######################################
# 동적 계획법을 활용한 예제, 위의 배열 사용한 버전과 비슷
# def fibo_dp(num):
#     cache = [ 0 for index in range(num + 1)]  # 저장공간(0~num을 가지는 배열 -> 배열 길이는 num+1)
#     cache[0] = 0
#     cache[1] = 1
    
#     for index in range(2, num + 1):   # 리스트에 0,1 이 채워져있고 그다음(2)부터 num까지 반복문 진행, 
#         cache[index] = cache[index - 1] + cache[index - 2]
#     return cache[num]
