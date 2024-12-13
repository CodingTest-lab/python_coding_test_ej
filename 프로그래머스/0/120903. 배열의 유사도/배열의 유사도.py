def solution(s1, s2):
    result = 0
    for i in s1:
        for j in s2:
            if i == j:
                result += 1
    return result

# 교집합 사용
# return len(set(s1)&set(s2));