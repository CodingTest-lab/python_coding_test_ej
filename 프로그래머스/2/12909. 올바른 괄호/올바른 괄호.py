def solution(s):
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

    # 스택 구조 사용
    # "("는 무조건 스택에 추가
    # ")"가 나오면 스택에서 "("를 제거
    # 스택이 비어있는데 ")"가 나오면 False
    # 최종적으로 스택이 비어있어야 True
    # stack = []
    # for i in s:
    #     if i == "(":
    #         stack.append(i)
    #     else:  # i == ")"
    #         if not stack:
    #             return False
    #         stack.pop()
    # return len(stack) == 0
