def solution(n):
    answer = []
    # 소수는 2부터 시작
    x = 2
    while x <= n:
        # n이 x의 배수면
        if n % x == 0:
            # if문으로 중복 제거
            if x not in answer:
                answer.append(x)
            # n은 계속 x로 나눈 몫이 대입됨
            n //= x   # n = n // x
        # n이 x의 배수가 아니면
        else:
            x += 1
    return answer

    # 결과값의 중복을 제거하기 위해 set으로 만들고
    # 리스트로 변환 후 오름차순 정렬
    # answer = []
    # i = 2
    # while i <= n :
    #     if n % i == 0 :
    #         answer.append(i)
    #         n = n // i
    #     else:
    #         i += 1
    # return sorted(list(set(answer)))