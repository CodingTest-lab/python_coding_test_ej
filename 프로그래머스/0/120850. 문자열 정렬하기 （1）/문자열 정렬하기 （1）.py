def solution(my_string):
    answer = []
    for str in my_string:
        if str in ['0','1','2','3','4','5','6','7','8','9']:
            j = int(str)
            answer.append(j)
    answer.sort()
    return answer

# isdigit() : 문자열이 온전한 정수인지 판별
# return sorted([int(c) for c in my_string if c.isdigit()])
