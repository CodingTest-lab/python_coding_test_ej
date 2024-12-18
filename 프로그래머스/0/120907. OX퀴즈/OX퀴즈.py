def solution(quiz):
    i = -1
    answer = []
    while 1:
        if i == len(quiz) -1:
            break
        i += 1
        str = quiz[i].split()
        if str[1] == '+':
            if int(str[0]) + int(str[2]) == int(str[4]):
                answer.append('O')
            else:
                answer.append('X')
        if str[1] == '-':
            if int(str[0]) - int(str[2]) == int(str[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer