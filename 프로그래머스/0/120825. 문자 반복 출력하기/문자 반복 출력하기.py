def solution(my_string, n):
    # my_string 각각 for문 돌고
    # answer = ''
    # for i in my_string:
    #     answer += i
    return ''.join([i * n for i in my_string ])