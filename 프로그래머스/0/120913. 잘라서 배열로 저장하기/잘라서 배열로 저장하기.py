def solution(my_str, n):
    # n 개씩 자르기로 했으므로 [ i : i+n ]과 같이 슬라이싱 가능
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(str(my_str[i:i+n]))
    return answer

    # return [my_str[i: i + n] for i in range(0, len(my_str), n)]
