def solution(s):
    answer = True
    
    rest = 0
    # '(' 일때는 +1
    # ')' 일때는 -1
    # 합계가 0이면 괄호가 바르게 짝지어졌다는 의미
    # ')' 로 시작하면 안됨, 모든 괄호 확인 후 '(' 가 남아있으면 안됨
    for str in s:
        if str == '(':
            rest += 1
        else:
            rest -= 1
        
        if rest < 0:   # ')' 가 '(' 보다 많음
            return False
    
    if rest != 0:
        return False

    return True