def solution(quiz):
    answer = []
    for equation in quiz:
        # 각각의 식을 공백으로 나눔(list로 반환)
        str = equation.split()
        
        # '+' 기호
        if str[1] == '+':
            if int(str[0]) + int(str[2]) == int(str[4]):
                answer.append('O')
            else:
                answer.append('X')
                
        # '-' 기호
        if str[1] == '-':
            if int(str[0]) - int(str[2]) == int(str[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer