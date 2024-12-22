def solution(n):
    # 연속된 자연수들로 n을 표현하는 방법의 수(1로 초기화한건 n 자기자신을 포함시켜 놓았기 때문, 15 = 15)
    result = 1
    # n의 절반까지만 반복(n의 절반을 초과하는 연속된 자연수들의 합은 n을 초과하기 때문에)
    for i in range(1, n // 2 + 1):
        # 각 반복에서의 연속된 자연수들의 합을 저장할 변수
        total = 0
        # 연속된 자연수들을 더하는 동안 그 합이 n보다 작은 경우에는 계속 반복
        while total < n:
            # 자연수들을 더함
            total += i
            # 자연수를 더한 값이 n과 같다면
            if total == n:
                # 경우의 수에 포함시키고 while문 중단
                result += 1
                break
            # 연속된 자연수의 합이므로 i를 1씩 증가
            i += 1
    return result