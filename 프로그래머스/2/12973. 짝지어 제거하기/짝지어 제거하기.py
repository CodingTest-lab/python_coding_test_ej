def solution(s):
    # 빈 스택
    stack = []
    for i in s:
        # 스택에 값이 없으면
        if len(stack) == 0:
            stack.append(i)
        # 스택의 마지막 값이 i와 같으면
        elif stack[-1] == i:
            # 스택의 마지막 값 제거
            stack.pop()
        # 스택에 값이 있으면서 마지막 값이 i와 다르면
        else:
            stack.append(i)
    # 최종 스택의 길이가 0이면
    if len(stack) == 0:
        return 1
    return 0
    