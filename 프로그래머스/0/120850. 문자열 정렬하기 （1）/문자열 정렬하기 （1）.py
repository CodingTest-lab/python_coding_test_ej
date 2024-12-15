def solution(my_string):
    answer = []
    for str in my_string:
        if str in ['0','1','2','3','4','5','6','7','8','9']:
            j = int(str)
            answer.append(j)
    answer.sort()
    return answer